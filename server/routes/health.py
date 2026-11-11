"""Endpoint cek status server."""
from fastapi import APIRouter

from server.config import get_settings

router = APIRouter(prefix="/api", tags=["health"])


@router.get("/health")
def health():
    settings = get_settings()
    return {
        "status": "ok",
        "app": settings.APP_NAME,
        "model": settings.GROQ_MODEL,
        "groq_key_configured": bool(settings.GROQ_API_KEY),
    }
