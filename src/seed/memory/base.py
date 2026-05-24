"""The Seed Memory Base - Abstract base class for memory stores."""

from abc import ABC, abstractmethod
from typing import List, Dict, Any, Optional


class MemoryStore(ABC):
    """Abstract base class for memory stores."""

    def __init__(self, session_id: str = "default"):
        self.session_id = session_id

    @abstractmethod
    def add(self, role: str, content: str, metadata: Optional[Dict[str, Any]] = None):
        """Add a message to memory."""
        ...

    @abstractmethod
    def get_history(self, limit: int = 50) -> List[Dict[str, Any]]:
        """Retrieve conversation history."""
        ...

    @abstractmethod
    def clear(self):
        """Clear all memory for this session."""
        ...

    def __repr__(self):
        return f"{self.__class__.__name__}(session_id={self.session_id!r})"