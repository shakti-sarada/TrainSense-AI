"""
Session management endpoints.
"""

from fastapi import APIRouter, HTTPException

router = APIRouter(
    prefix="/clear",
    tags=["Session"],
)


@router.post("/", summary="Clear session")
async def clear_session() -> dict:
    """Clear the active conversation session."""

    raise HTTPException(
        status_code=501,
        detail="Session clearing is not implemented yet.",
    )