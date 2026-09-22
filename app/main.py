from fastapi import FastAPI

from app.core.config import settings
from app.routers import webhooks

app = FastAPI(title=settings.app_name)
app.include_router(webhooks.router)


@app.get("/health")
def health() -> dict:
    return {"status": "ok", "env": settings.env}
