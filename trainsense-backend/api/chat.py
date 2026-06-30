"""
Chat API endpoints.
"""

from fastapi import APIRouter, HTTPException

router = APIRouter(
    prefix="/chat",
    tags=["Chat"],
)


@router.post("/", summary="Process chat request")
async def chat() -> dict:
    """Handle a train search request."""

    raise HTTPException(
        status_code=501,
        detail="Chat service is not implemented yet.",
    )