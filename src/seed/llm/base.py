"""The Seed LLM Base - Abstract base class for LLM providers."""

from abc import ABC, abstractmethod
from typing import List, Dict, Any, Optional


class LLMProvider(ABC):
    """Abstract base class for LLM providers.

    All provider implementations (OpenAI, Anthropic, Google, Custom, etc.)
    must inherit from this class and implement the abstract methods.
    """

    def __init__(
        self,
        model: str,
        api_key: Optional[str] = None,
        api_base: Optional[str] = None,
        **kwargs,
    ):
        """Initialize the LLM provider.

        Args:
            model: Model name or identifier
            api_key: API key for authentication
            api_base: Custom API base URL (for self-hosted or proxy setups)
        """
        self.model = model
        self.api_key = api_key
        self.api_base = api_base

    @abstractmethod
    def chat(
        self,
        messages: List[Dict[str, Any]],
        tools: Optional[List[Dict[str, Any]]] = None,
        **kwargs,
    ) -> str:
        """Send a chat request and return the response text.

        Args:
            messages: List of message dicts with 'role' and 'content'
            tools: Optional list of tool definitions

        Returns:
            The response text from the model
        """
        ...

    @abstractmethod
    def chat_stream(
        self,
        messages: List[Dict[str, Any]],
        tools: Optional[List[Dict[str, Any]]] = None,
        **kwargs,
    ):
        """Stream chat responses.

        Yields response chunks as they arrive.
        """
        ...

    def __repr__(self):
        return f"{self.__class__.__name__}(model={self.model!r})"