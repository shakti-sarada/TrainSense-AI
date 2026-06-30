"""
Notification subscription endpoints.
"""

from fastapi import APIRouter, HTTPException

router = APIRouter(
    prefix="/subscribe",
    tags=["Notifications"],
)


@router.post("/", summary="Create notification")
async def subscribe() -> dict:
    """Create a notification subscription."""

    raise HTTPException(
        status_code=501,
        detail="Notification service is not implemented yet.",
    )