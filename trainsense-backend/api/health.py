"""
Health check endpoint.
"""

from fastapi import APIRouter

from core.config import settings

router = APIRouter(
    prefix="/health",
    tags=["Health"],
)


@router.get("/", summary="Health Check")
async def health_check() -> dict:
    """Return application health status."""

    return {
        "status": "healthy",
        "application": settings.APP_NAME,
        "version": settings.APP_VERSION,
    }