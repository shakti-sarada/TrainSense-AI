"""
Async PostgreSQL connection manager.
"""

import asyncio
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
        """Return the active database connection pool."""

        if self._pool is None:
            raise RuntimeError("Database connection pool has not been initialized.")

        return self._pool

    async def connect(self) -> None:
        """Create and verify the database connection pool."""

        if self._pool is not None:
            logger.info("Database pool already initialized.")
            return

        for attempt in range(1, settings.DB_CONNECT_RETRIES + 1):
            try:
                logger.info(
                    "Connecting to database (Attempt %d/%d)...",
                    attempt,
                    settings.DB_CONNECT_RETRIES,
                )

                self._pool = await asyncpg.create_pool(
                    dsn=settings.DATABASE_URL,
                    min_size=settings.DB_POOL_MIN_SIZE,
                    max_size=settings.DB_POOL_MAX_SIZE,
                    timeout=settings.DB_CONNECT_TIMEOUT,
                    command_timeout=settings.DB_COMMAND_TIMEOUT,
                )

                async with self._pool.acquire() as connection:
                    if settings.DEBUG:
                        version = await connection.fetchval("SELECT version();")
                        logger.debug("PostgreSQL Version: %s", version)
                    else:
                        await connection.execute("SELECT 1")

                logger.info("Database connected successfully.")

                return

            except Exception:
                logger.exception(
                    "Database connection attempt %d failed.",
                    attempt,
                )

                if self._pool is not None:
                    await self._pool.close()
                    self._pool = None

                if attempt == settings.DB_CONNECT_RETRIES:
                    logger.error("All database connection attempts failed.")
                    raise

                delay = settings.DB_RETRY_DELAY * (2 ** (attempt - 1))

                logger.warning(
                    "Retrying database connection in %d second(s)...",
                    delay,
                )

                await asyncio.sleep(delay)

    async def disconnect(self) -> None:
        """Close the database connection pool."""

        if self._pool is None:
            logger.info("Database pool already closed.")
            return

        await self._pool.close()
        self._pool = None

        logger.info("Database connection closed.")


database = Database()