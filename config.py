"""Central configuration for the Discord game chatbot."""
from __future__ import annotations

import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()

# Environment variables
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN", "")

# Game constants
DIFFICULTIES = ("easy", "normal", "hard")
MAX_INVENTORY_SLOTS = 20

# Timeouts and limits
REQUEST_TIMEOUT = int(os.getenv("REQUEST_TIMEOUT", "30"))
COMMAND_COOLDOWN = int(os.getenv("COMMAND_COOLDOWN", "1"))
MAX_CONTEXT_MESSAGES = int(os.getenv("MAX_CONTEXT_MESSAGES", "20"))


@dataclass(frozen=True)
class Settings:
    """Typed access to configuration values."""

    gemini_api_key: str = GEMINI_API_KEY
    discord_token: str = DISCORD_TOKEN

    difficulties: tuple[str, ...] = DIFFICULTIES
    max_inventory: int = MAX_INVENTORY_SLOTS

    request_timeout: int = REQUEST_TIMEOUT
    command_cooldown: int = COMMAND_COOLDOWN
    max_context_messages: int = MAX_CONTEXT_MESSAGES


settings = Settings()
