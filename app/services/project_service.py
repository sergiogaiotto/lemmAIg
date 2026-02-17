from pathlib import Path
from app.core.config import SPECS_DIR
from app.models.schemas import ProjectStatus


def get_project_dir(project_name: str) -> Path:
    project_dir = SPECS_DIR / project_name
    project_dir.mkdir(parents=True, exist_ok=True)
    return project_dir


def read_file_safe(path: Path) -> str:
    if path.exists():
        return path.read_text(encoding="utf-8")
    return ""


def save_artifact(project_name: str, filename: str, content: str) -> Path:
    project_dir = get_project_dir(project_name)
    filepath = project_dir / filename
    filepath.write_text(content, encoding="utf-8")
    return filepath


def get_project_status(project_name: str) -> ProjectStatus:
    project_dir = get_project_dir(project_name)
    espec = read_file_safe(project_dir / "ESPEC.md")
    dp = read_file_safe(project_dir / "DP.md")
    plan = read_file_safe(project_dir / "PLAN.md")
    tasks = read_file_safe(project_dir / "TASKS.md")
    implementation = read_file_safe(project_dir / "IMPLEMENTATION.md")

    return ProjectStatus(
        project_name=project_name,
        has_espec=bool(espec),
        has_dp=bool(dp),
        has_plan=bool(plan),
        has_tasks=bool(tasks),
        has_implementation=bool(implementation),
        espec_content=espec,
        dp_content=dp,
        plan_content=plan,
        tasks_content=tasks,
        implementation_content=implementation,
    )


def list_projects() -> list[str]:
    if not SPECS_DIR.exists():
        return []
    return [d.name for d in SPECS_DIR.iterdir() if d.is_dir()]
