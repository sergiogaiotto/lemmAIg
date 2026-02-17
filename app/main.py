from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.api.routes import router
from app.core.config import APP_NAME, TEMPLATES_DIR, BASE_DIR

app = FastAPI(title=APP_NAME, version="1.0.0")
app.include_router(router)

templates = Jinja2Templates(directory=str(TEMPLATES_DIR))

static_dir = BASE_DIR / "app" / "static"
if static_dir.exists():
    app.mount("/static", StaticFiles(directory=str(static_dir)), name="static")


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("default.html", {"request": request})


@app.get("/tutorial", response_class=HTMLResponse)
async def tutorial(request: Request):
    return templates.TemplateResponse("tutorial.html", {"request": request})


@app.get("/health")
async def health():
    return {"status": "ok", "app": APP_NAME}
