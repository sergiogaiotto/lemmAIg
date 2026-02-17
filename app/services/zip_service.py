import io
import zipfile
import re
from pathlib import Path
from app.services.project_service import get_project_dir, read_file_safe


def _parse_implementation_files(impl_content: str) -> list[dict]:
    """Extrai arquivos de codigo do IMPLEMENTATION.md gerado pelo agente.

    Busca blocos no formato:
        ### Arquivo: caminho/do/arquivo.py
        ```python
        conteudo aqui
        ```
    Ou variantes como:
        **caminho/do/arquivo.py**
        ```
        conteudo aqui
        ```
    """
    files = []

    # Padrao 1: ### Arquivo: path ou ### path
    pattern1 = re.compile(
        r'#{1,4}\s*(?:Arquivo:\s*)?[`"]?([^\n`"]+\.\w+)[`"]?\s*\n'
        r'```[\w]*\n(.*?)```',
        re.DOTALL,
    )
    for match in pattern1.finditer(impl_content):
        filepath = match.group(1).strip()
        content = match.group(2)
        files.append({"path": filepath, "content": content})

    # Padrao 2: **path** seguido de ```
    pattern2 = re.compile(
        r'\*\*([^\n*]+\.\w+)\*\*\s*\n```[\w]*\n(.*?)```',
        re.DOTALL,
    )
    for match in pattern2.finditer(impl_content):
        filepath = match.group(1).strip()
        content = match.group(2)
        seen = {f["path"] for f in files}
        if filepath not in seen:
            files.append({"path": filepath, "content": content})

    return files


def build_project_zip(project_name: str) -> io.BytesIO:
    """Gera um ZIP com todos os artefatos e arquivos de codigo do projeto."""
    project_dir = get_project_dir(project_name)

    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, "w", zipfile.ZIP_DEFLATED) as zf:
        root = project_name

        # Adiciona artefatos .md do spec-driven flow
        for md_file in ("ESPEC.md", "DP.md", "TASKS.md", "IMPLEMENTATION.md"):
            content = read_file_safe(project_dir / md_file)
            if content:
                zf.writestr(f"{root}/docs/{md_file}", content)

        # Parseia IMPLEMENTATION.md e gera arquivos de codigo
        impl_content = read_file_safe(project_dir / "IMPLEMENTATION.md")
        if impl_content:
            parsed_files = _parse_implementation_files(impl_content)
            for f in parsed_files:
                filepath = f["path"].lstrip("/").lstrip("\\")
                zf.writestr(f"{root}/src/{filepath}", f["content"])

            if not parsed_files:
                # Se nao encontrou blocos parseados, coloca o raw como referencia
                zf.writestr(f"{root}/src/IMPLEMENTATION_RAW.md", impl_content)

        # Gera README basico no ZIP
        readme = (
            f"# {project_name}\n\n"
            f"Projeto gerado pelo lemmAIngs - Spec-Driven Development\n\n"
            f"## Estrutura\n\n"
            f"- `docs/` - Artefatos do spec-driven flow (ESPEC, DP, TASKS)\n"
            f"- `src/` - Codigo-fonte gerado\n"
        )
        zf.writestr(f"{root}/README.md", readme)

    buffer.seek(0)
    return buffer
