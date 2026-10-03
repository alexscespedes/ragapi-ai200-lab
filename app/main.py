import os
from fastapi import FastAPI

app = FastAPI(title="ragapi")

@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}

@app.get("/version")
def version() -> str:
    return os.environ.get("APP_VERSION", "dev")