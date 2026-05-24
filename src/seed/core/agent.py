"""The Seed Core Agent - Main agent class."""

from typing import Optional


class TheSeedAgent:
    """The Seed Agent - A next-generation AI Agent built for everyone."""

    def __init__(
        self,
        name: str = "TheSeedAgent",
        model: str = "gpt-4o",
        provider: str = "openai",
        api_key: Optional[str] = None,
        api_base: Optional[str] = None,
        personality: str = "helpful",
        **kwargs,
    ):
        """Initialize TheSeedAgent.

        Args:
            name: Agent name
            model: Model name (e.g. gpt-4o, claude-sonnet-4)
            provider: LLM provider (openai, anthropic, google, qwen, wenxin, local, custom)
            api_key: API key for the provider
            api_base: Custom API base URL
            personality: Agent personality description
        """
        self.name = name
        self.model = model
        self.provider = provider
        self.api_key = api_key
        self.api_base = api_base
        self.personality = personality
        self._tools = []
        self._memory = []

    def chat(self, message: str) -> str:
        """Send a message and get a response."""
        return f"[{self.name}] Received: {message}"

    def run(self):
        """Run the agent interactively."""
        print(f"🌱 {self.name} is running. Type 'exit' to quit.")
        while True:
            try:
                msg = input("You: ")
                if msg.lower() in ("exit", "quit", "q"):
                    print("Goodbye!")
                    break
                print(f"{self.name}: {self.chat(msg)}")
            except (EOFError, KeyboardInterrupt):
                print("\nGoodbye!")
                break

    def __repr__(self):
        return f"TheSeedAgent(name={self.name!r}, model={self.model!r}, provider={self.provider!r})"