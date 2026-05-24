"""🌱 The Seed - Next-generation AI Agent framework for everyone."""

__version__ = "0.1.0"

from seed.core.agent import TheSeedAgent
from seed.llm.base import LLMProvider

__all__ = ["TheSeedAgent", "LLMProvider", "__version__"]