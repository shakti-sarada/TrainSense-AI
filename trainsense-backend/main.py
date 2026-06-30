"""
Application entry point.
"""

from contextlib import asynccontextmanager
import logging

from fastapi import FastAPI

from api.health import router as health_router
from core.config import settings
from core.logger import configure_logging
from db.connection import database

# Configure application logging
configure_logging()

# Module logger
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Run application startup and shutdown tasks."""

    logger.info("Starting %s...", settings.APP_NAME)

    await database.connect()

    yield

    await database.disconnect()

    logger.info("Stopping %s...", settings.APP_NAME)


# FastAPI application instance
app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    debug=settings.DEBUG,
    lifespan=lifespan,
)

# Register API routers
app.include_router(health_router)


@app.get("/", tags=["Root"])
async def root() -> dict:
    """Return API welcome message."""

    return {
        "message": f"Welcome to {settings.APP_NAME}",
        "docs": "/docs",
    }