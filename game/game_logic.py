"""Game logic helpers."""
from __future__ import annotations

from . import data_manager as dm
from . import models


CHARACTER_FILE = "character.json"
INVENTORY_FILE = "inventory.json"
LOCATIONS_FILE = "locations.json"
RELATIONSHIPS_FILE = "relationships.json"
WORLD_EVENTS_FILE = "world_events.json"
SUMMARY_FILE = "story_summary.txt"


def start_game(user_id: int, name: str) -> dict:
    """Initialise a new game for the user."""
    character = models.default_character(name)
    dm.write_json(user_id, CHARACTER_FILE, character)
    dm.write_json(user_id, INVENTORY_FILE, models.default_inventory())
    dm.write_json(user_id, LOCATIONS_FILE, {})
    dm.write_json(user_id, RELATIONSHIPS_FILE, {})
    dm.write_json(user_id, WORLD_EVENTS_FILE, {})
    dm.append_text(user_id, SUMMARY_FILE, models.intro_text())
    return character


def has_game(user_id: int) -> bool:
    data = dm.read_json(user_id, CHARACTER_FILE, None)
    return data is not None
