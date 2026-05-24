"""The Seed Tools Registry - Dynamic tool registration and execution."""

from typing import Callable, Dict, List, Any


class ToolRegistry:
    """Registry for agent tools.

    Tools are functions decorated with @register_tool.
    """

    def __init__(self):
        self._tools: Dict[str, Callable] = {}
        self._descriptions: Dict[str, str] = {}

    def register(self, name: str, func: Callable, description: str = ""):
        """Register a tool function."""
        self._tools[name] = func
        self._descriptions[name] = description

    def get(self, name: str) -> Callable:
        """Get a registered tool by name."""
        return self._tools[name]

    def list_tools(self) -> List[str]:
        """List all registered tool names."""
        return list(self._tools.keys())

    def execute(self, name: str, **kwargs) -> Any:
        """Execute a tool by name with given arguments."""
        return self._tools[name](**kwargs)

    def __repr__(self):
        return f"ToolRegistry({len(self._tools)} tools registered)"


# Global registry instance
_global_registry = ToolRegistry()


def register_tool(name: str = None, description: str = ""):
    """Decorator to register a tool function."""
    def decorator(func: Callable) -> Callable:
        tool_name = name or func.__name__
        _global_registry.register(tool_name, func, description or func.__doc__ or "")
        return func
    return decorator