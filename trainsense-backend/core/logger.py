"""
Application logging configuration.
"""

import logging

from core.config import settings


def configure_logging() -> None:
    """Configure the application logger."""

    logging.basicConfig(
        level=getattr(logging, settings.LOG_LEVEL.upper(), logging.INFO),
        format="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )