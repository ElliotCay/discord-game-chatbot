"""Logging configuration and metrics tracking for the game."""
from __future__ import annotations

import logging
from logging.handlers import RotatingFileHandler
from dataclasses import dataclass, field
from typing import Dict
import time

import structlog

LOG_FILE = "game.log"
MAX_BYTES = 1_000_000
BACKUP_COUNT = 5

handler = RotatingFileHandler(LOG_FILE, maxBytes=MAX_BYTES, backupCount=BACKUP_COUNT)
logging.basicConfig(handlers=[handler], level=logging.INFO, format="%(message)s")

structlog.configure(
    processors=[
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.processors.JSONRenderer(),
    ],
    wrapper_class=structlog.make_filtering_bound_logger(logging.INFO),
    context_class=dict,
    logger_factory=structlog.stdlib.LoggerFactory(),
)

logger = structlog.get_logger()


def get_user_logger(user_id: int) -> structlog.BoundLogger:
    """Return a logger bound to a specific user id."""
    return logger.bind(user_id=user_id)


@dataclass
class Metrics:
    """In-memory metrics for basic monitoring."""

    response_times: Dict[str, float] = field(default_factory=dict)
    api_calls: int = 0
    player_stats: Dict[int, Dict[str, int]] = field(default_factory=dict)


metrics = Metrics()


def track_response(command: str, start_time: float) -> None:
    """Store response time for a command."""
    metrics.response_times[command] = time.time() - start_time


def track_api_call() -> None:
    """Increment Gemini API usage counter."""
    metrics.api_calls += 1


def update_player_stat(user_id: int, stat: str, value: int) -> None:
    """Update a stat for a player."""
    player = metrics.player_stats.setdefault(user_id, {})
    player[stat] = player.get(stat, 0) + value
