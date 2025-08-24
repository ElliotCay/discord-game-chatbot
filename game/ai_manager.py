"""AI agents management for narration, NPCs and events."""
from __future__ import annotations

import asyncio
from typing import Dict, List

import google.generativeai as genai

from config import settings


genai.configure(api_key=settings.gemini_api_key)


class BaseAgent:
    """Common utilities for AI agents with basic memory."""

    def __init__(self, model_name: str, **model_config: object) -> None:
        self.client = genai.GenerativeModel(model_name=model_name, **model_config)
        self.memory: Dict[int, List[str]] = {}

    def _build_prompt(self, context: str) -> str:
        return context

    async def generate(self, user_id: int, context: str) -> str:
        prompt = self._build_prompt(context)
        history = self.memory.setdefault(user_id, [])
        history.append(prompt)
        response = await asyncio.to_thread(self.client.generate_content, "\n".join(history))
        text = response.text or ""
        history.append(text)
        if len(history) > settings.max_context_messages:
            self.memory[user_id] = history[-settings.max_context_messages :]
        return text


class NarratorAgent(BaseAgent):
    """Handles narrative responses."""

    def __init__(self) -> None:
        super().__init__(
            "gemini-pro",
            temperature=0.8,
            top_p=0.95,
            top_k=40,
            max_output_tokens=800,
        )

    async def narrate_action(self, user_id: int, context: str) -> str:
        return await self.generate(user_id, context)


class NPCAgent(BaseAgent):
    """Generates NPC dialogue."""

    def __init__(self) -> None:
        super().__init__(
            "gemini-pro",
            temperature=0.7,
            top_p=0.9,
            max_output_tokens=400,
        )

    async def generate_response(self, user_id: int, context: str) -> str:
        return await self.generate(user_id, context)


class EventAgent(BaseAgent):
    """Produces random world events."""

    def __init__(self) -> None:
        super().__init__("gemini-pro", temperature=0.6, max_output_tokens=200)

    async def trigger_event(self, user_id: int, context: str) -> str:
        return await self.generate(user_id, context)


class AIManager:
    """Simple container for all agents."""

    def __init__(self) -> None:
        self.narrator = NarratorAgent()
        self.npc = NPCAgent()
        self.event = EventAgent()

