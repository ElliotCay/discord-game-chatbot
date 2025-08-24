"""Utilities for reading and writing game data files."""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path("game_data")


def _ensure_user_dir(user_id: int) -> Path:
    """Return the directory for a user and create it if needed."""
    path = BASE_DIR / str(user_id)
    path.mkdir(parents=True, exist_ok=True)
    return path


def read_json(user_id: int, filename: str, default):
    """Read JSON data for a user. If missing, write and return default."""
    path = _ensure_user_dir(user_id) / filename
    if path.exists():
        with path.open(encoding="utf-8") as f:
            return json.load(f)
    write_json(user_id, filename, default)
    return default


def write_json(user_id: int, filename: str, data) -> None:
    """Write JSON data for a user."""
    path = _ensure_user_dir(user_id) / filename
    with path.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def read_text(user_id: int, filename: str) -> str:
    path = _ensure_user_dir(user_id) / filename
    if path.exists():
        return path.read_text(encoding="utf-8")
    return ""


def append_text(user_id: int, filename: str, text: str) -> None:
    path = _ensure_user_dir(user_id) / filename
    with path.open("a", encoding="utf-8") as f:
        f.write(text + "\n")
