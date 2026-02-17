from pydantic import BaseModel


class SpecifyRequest(BaseModel):
    project_name: str
    description: str


class PlanRequest(BaseModel):
    project_name: str
    stack: str
    constraints: str = ""
    dp_template_id: str | None = None


class TasksRequest(BaseModel):
    project_name: str


class ImplementRequest(BaseModel):
    project_name: str
    task_index: int | None = None


class PhaseResponse(BaseModel):
    phase: str
    content: str
    project_name: str


class ProjectStatus(BaseModel):
    project_name: str
    has_espec: bool
    has_dp: bool
    has_plan: bool
    has_tasks: bool
    has_implementation: bool
    espec_content: str = ""
    dp_content: str = ""
    plan_content: str = ""
    tasks_content: str = ""
    implementation_content: str = ""


class DPTemplateInfo(BaseModel):
    id: str
    name: str
    filename: str
    preview: str
