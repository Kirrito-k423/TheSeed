"""The Seed Platform Base - Abstract base class for platform adapters."""

from abc import ABC, abstractmethod
from typing import Any


class PlatformAdapter(ABC):
    """Abstract base class for platform integrations."""

    def __init__(self, token: str = None, **kwargs):
        self.token = token

    @abstractmethod
    def send(self, message: str, target: str = None):
        """Send a message through the platform."""
        ...

    @abstractmethod
    def receive(self) -> str:
        """Receive a message from the platform."""
        ...

    def __repr__(self):
        return f"{self.__class__.__name__}()"