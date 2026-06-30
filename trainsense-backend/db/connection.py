"""
Async PostgreSQL connection manager.
"""

import logging
from typing import Optional

import asyncpg
from asyncpg import Pool

from core.config import settings

# Module logger
logger = logging.getLogger(__name__)


class Database:
    """Manage the PostgreSQL connection pool."""

    def __init__(self) -> None:
        self._pool: Optional[Pool] = None

    @property
    def pool(self) -> Pool:
        """Return the active database pool."""

        if self._pool is None:
            raise RuntimeError("Database connection has not been initialized.")

        return self._pool

    async def connect(self) -> None:
        """Create and verify the connection pool."""

        if self._pool is not None:
            logger.info("Database pool already initialized.")
            return

        try:
            self._pool = await asyncpg.create_pool(
                dsn=settings.NEON_DSN,
                min_size=1,
                max_size=10,
                command_timeout=30,
            )

            async with self._pool.acquire() as connection:
                version = await connection.fetchval("SELECT version();")

            logger.info("Database connected successfully.")
            logger.debug("PostgreSQL Version: %s", version)

        except Exception:
            logger.exception("Failed to connect to the database.")
            raise

    async def disconnect(self) -> None:
        """Close the connection pool."""

        if self._pool is None:
            return

        await self._pool.close()
        self._pool = None

        logger.info("Database connection closed.")


database = Database()