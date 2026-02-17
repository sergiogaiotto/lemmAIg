import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent.parent
SPECS_DIR = BASE_DIR / "specs"
TEMPLATES_DIR = BASE_DIR / "app" / "templates"

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
APP_NAME = os.getenv("APP_NAME", "lemmAIngs")
APP_HOST = os.getenv("APP_HOST", "0.0.0.0")
APP_PORT = int(os.getenv("APP_PORT", "8000"))
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4o")
