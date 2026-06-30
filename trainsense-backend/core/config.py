"""
Application configuration loaded from environment variables.
"""

from functools import lru_cache

import logging

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Central application configuration."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    # Project
    APP_NAME: str = "TrainSense AI"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = False

    # Server
    HOST: str = "0.0.0.0"
    PORT: int = 8000

    # Groq
    GROQ_API_KEY: str = Field(default="", repr=False)

    # Railway APIs
    ERAIL_API_KEY: str = Field(default="", repr=False)
    INDIANRAIL_API_KEY: str = Field(default="", repr=False)

    # Database
    NEON_DSN: str = Field(default="", repr=False)

    # Cache
    CACHE_ENABLED: bool = True
    CACHE_DEFAULT_TTL: int = 300

    # Session
    SESSION_TIMEOUT_MINUTES: int = 30

    # Logging
    LOG_LEVEL: str = "INFO"


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    """Return a cached settings instance."""
    return Settings()


settings = get_settings()


def configure_logging() -> None:
    """Configure application logging."""

    logging.basicConfig(
        level=settings.LOG_LEVEL,
        format="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )