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

from api.chat import router as chat_router
from api.clear import router as clear_router
from api.preferences import router as preferences_router
from api.subscribe import router as subscribe_router
from api.metrics import router as metrics_router

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
app.include_router(chat_router)
app.include_router(clear_router)
app.include_router(preferences_router)
app.include_router(subscribe_router)
app.include_router(metrics_router)


@app.get("/", tags=["Root"])
async def root() -> dict:
    """Return API welcome message."""

    return {
        "message": f"Welcome to {settings.APP_NAME}",
        "docs": "/docs",
    }