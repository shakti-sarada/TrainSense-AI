"""
Observability endpoints.
"""

from fastapi import APIRouter, HTTPException

router = APIRouter(
    prefix="/metrics",
    tags=["Observability"],
)


@router.get("/", summary="Application metrics")
async def metrics() -> dict:
    """Return application metrics."""

    raise HTTPException(
        status_code=501,
        detail="Metrics service is not implemented yet.",
    )