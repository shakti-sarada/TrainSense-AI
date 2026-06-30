"""
User preference endpoints.
"""

from fastapi import APIRouter, HTTPException

router = APIRouter(
    prefix="/preferences",
    tags=["Preferences"],
)


@router.get("/", summary="Get preferences")
async def get_preferences() -> dict:
    """Return saved user preferences."""

    raise HTTPException(
        status_code=501,
        detail="Preferences service is not implemented yet.",
    )