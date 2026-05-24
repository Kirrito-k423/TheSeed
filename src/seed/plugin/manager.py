"""The Seed Plugin Manager - Hot-pluggable extension framework."""

import importlib
import sys
from pathlib import Path
from typing import List, Dict, Any


class PluginManager:
    """Manages hot-pluggable plugins for The Seed framework."""

    def __init__(self, plugin_dir: str = None):
        self.plugin_dir = plugin_dir
        self._plugins: Dict[str, Any] = {}

    def load_plugin(self, name: str):
        """Dynamically load a plugin by name."""
        if name in self._plugins:
            return self._plugins[name]

        try:
            mod = importlib.import_module(f"seed_plugins.{name}")
            self._plugins[name] = mod
            return mod
        except ImportError:
            raise ImportError(f"Plugin '{name}' not found.")

    def list_plugins(self) -> List[str]:
        """List all available plugins."""
        return list(self._plugins.keys())

    def __repr__(self):
        return f"PluginManager({len(self._plugins)} loaded)"