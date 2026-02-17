from fastapi import APIRouter, HTTPException, UploadFile, File, Form
from fastapi.responses import StreamingResponse
from app.models.schemas import (
    SpecifyRequest,
    PlanRequest,
    TasksRequest,
    ImplementRequest,
    PhaseResponse,
    ProjectStatus,
    DPTemplateInfo,
)
from app.agents.spec_agent import run_phase
from app.services.project_service import (
    save_artifact,
    get_project_status,
    list_projects,
)
from app.services.dp_catalog_service import (
    save_dp_template,
    list_dp_templates,
    get_dp_template_content,
    delete_dp_template,
)
from app.services.zip_service import build_project_zip

router = APIRouter(prefix="/api")


# ── Projetos ──────────────────────────────────────────────────────────


@router.get("/projects", response_model=list[str])
async def get_projects():
    return list_projects()


@router.get("/projects/{project_name}", response_model=ProjectStatus)
async def get_project(project_name: str):
    return get_project_status(project_name)


# ── Fases do Spec-Driven Flow ────────────────────────────────────────


@router.post("/specify", response_model=PhaseResponse)
async def specify(req: SpecifyRequest):
    prompt = (
        f"Projeto: {req.project_name}\n\n"
        f"Descricao:\n{req.description}"
    )
    content = await run_phase("specify", req.project_name, prompt)
    save_artifact(req.project_name, "ESPEC.md", content)
    return PhaseResponse(
        phase="specify", content=content, project_name=req.project_name
    )


@router.post("/plan", response_model=PhaseResponse)
async def plan(req: PlanRequest):
    status = get_project_status(req.project_name)
    if not status.has_espec:
        raise HTTPException(400, "Execute /specify antes de /plan")

    dp_context = ""
    if req.dp_template_id:
        try:
            dp_text = get_dp_template_content(req.dp_template_id)
            dp_context = (
                f"\n\n## Design Pattern de referencia (cadastrado previamente):\n\n"
                f"{dp_text}\n\n"
                f"Use este design pattern como base e adapte ao projeto.\n"
            )
        except FileNotFoundError:
            raise HTTPException(404, "Template de DP nao encontrado.")

    prompt = (
        f"Stack desejada: {req.stack}\n"
        f"Restricoes: {req.constraints}\n"
        f"{dp_context}\n"
        f"Gere o DP.md (Design Pattern) para o projeto {req.project_name}."
    )
    content = await run_phase("plan", req.project_name, prompt)
    save_artifact(req.project_name, "DP.md", content)
    return PhaseResponse(
        phase="plan", content=content, project_name=req.project_name
    )


@router.post("/tasks", response_model=PhaseResponse)
async def tasks(req: TasksRequest):
    status = get_project_status(req.project_name)
    if not status.has_dp:
        raise HTTPException(400, "Execute /plan antes de /tasks")
    content = await run_phase("tasks", req.project_name, "Gere as tarefas.")
    save_artifact(req.project_name, "TASKS.md", content)
    return PhaseResponse(
        phase="tasks", content=content, project_name=req.project_name
    )


@router.post("/implement", response_model=PhaseResponse)
async def implement(req: ImplementRequest):
    status = get_project_status(req.project_name)
    if not status.has_tasks:
        raise HTTPException(400, "Execute /tasks antes de /implement")
    task_msg = (
        f"Implemente a tarefa #{req.task_index}"
        if req.task_index is not None
        else "Implemente todas as tarefas listadas."
    )
    content = await run_phase("implement", req.project_name, task_msg)
    save_artifact(req.project_name, "IMPLEMENTATION.md", content)
    return PhaseResponse(
        phase="implement", content=content, project_name=req.project_name
    )


# ── Edicao manual de artefatos ───────────────────────────────────────


@router.put("/projects/{project_name}/{artifact}")
async def update_artifact(project_name: str, artifact: str, body: dict):
    allowed = {"ESPEC.md", "DP.md", "TASKS.md", "IMPLEMENTATION.md"}
    if artifact not in allowed:
        raise HTTPException(400, f"Artefato deve ser um de: {allowed}")
    content = body.get("content", "")
    save_artifact(project_name, artifact, content)
    return {"status": "saved", "artifact": artifact}


# ── Catalogo de Design Patterns (upload PDF/DOCX) ───────────────────


@router.get("/dp-catalog", response_model=list[DPTemplateInfo])
async def get_dp_catalog():
    return list_dp_templates()


@router.post("/dp-catalog/upload", response_model=DPTemplateInfo)
async def upload_dp_template(
    file: UploadFile = File(...),
    name: str = Form(""),
):
    if not file.filename:
        raise HTTPException(400, "Arquivo obrigatorio.")
    ext = file.filename.rsplit(".", 1)[-1].lower() if "." in file.filename else ""
    if ext not in ("pdf", "docx", "doc"):
        raise HTTPException(400, "Formato nao suportado. Envie PDF ou DOCX.")
    file_bytes = await file.read()
    if len(file_bytes) > 20 * 1024 * 1024:
        raise HTTPException(400, "Arquivo muito grande (max 20MB).")
    try:
        return save_dp_template(file.filename, file_bytes, name)
    except ValueError as e:
        raise HTTPException(400, str(e))


@router.get("/dp-catalog/{template_id}")
async def get_dp_template(template_id: str):
    try:
        content = get_dp_template_content(template_id)
        return {"id": template_id, "content": content}
    except FileNotFoundError:
        raise HTTPException(404, "Template nao encontrado.")


@router.delete("/dp-catalog/{template_id}")
async def remove_dp_template(template_id: str):
    if delete_dp_template(template_id):
        return {"status": "deleted", "id": template_id}
    raise HTTPException(404, "Template nao encontrado.")


# ── Download do projeto como ZIP ─────────────────────────────────────


@router.get("/projects/{project_name}/download")
async def download_project(project_name: str):
    status = get_project_status(project_name)
    if not status.has_espec:
        raise HTTPException(400, "Projeto sem artefatos para download.")
    zip_buffer = build_project_zip(project_name)
    return StreamingResponse(
        zip_buffer,
        media_type="application/zip",
        headers={
            "Content-Disposition": f'attachment; filename="{project_name}.zip"'
        },
    )
