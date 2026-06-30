"""
In-memory session storage.
"""

import logging
from datetime import datetime, timedelta
from typing import Any

from core.constants import SESSION_EXPIRY_MINUTES

# Module logger
logger = logging.getLogger(__name__)


class SessionMemory:
    """Manage temporary conversation sessions."""

    def __init__(self) -> None:
        self._sessions: dict[str, dict[str, Any]] = {}

    def create(self, session_id: str) -> None:
        """Create a new session."""

        self._sessions[session_id] = {
            "messages": [],
            "last_active": datetime.utcnow(),
        }

        logger.info("Session created: %s", session_id)

    def get(self, session_id: str) -> dict[str, Any] | None:
        """Return a session if it exists."""

        return self._sessions.get(session_id)

    def update_activity(self, session_id: str) -> None:
        """Update session activity time."""

        session = self.get(session_id)

        if session:
            session["last_active"] = datetime.utcnow()

    def cleanup(self) -> None:
        """Remove expired sessions."""

        now = datetime.utcnow()

        expired = [
            session_id
            for session_id, session in self._sessions.items()
            if now - session["last_active"]
            > timedelta(minutes=SESSION_EXPIRY_MINUTES)
        ]

        for session_id in expired:
            del self._sessions[session_id]

        if expired:
            logger.info("Removed %d expired sessions.", len(expired))


session_memory = SessionMemory()