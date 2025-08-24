"""Default game data structures."""
from __future__ import annotations


def default_character(name: str) -> dict:
    return {
        "name": name,
        "day": 1,
        "time": "dawn",
        "stats": {
            "health": 100,
            "hunger": 100,
            "thirst": 100,
            "fatigue": 20,
            "stress": 0,
            "radiation": 0,
        },
        "skills": {
            "combat": 0,
            "survival": 0,
            "stealth": 0,
            "charisma": 0,
            "engineering": 0,
            "medicine": 0,
        },
        "conditions": [],
        "location": "Station de métro abandonnée",
        "coordinates": {"x": 0, "y": 0},
    }


def default_inventory() -> dict:
    return {
        "items": [
            {"name": "ration", "quantity": 2},
            {"name": "bouteille d'eau", "quantity": 1},
            {"name": "couteau rouillé", "quantity": 1},
            {"name": "briquet", "quantity": 1, "uses": 5},
        ]
    }


def intro_text() -> str:
    return (
        "Vous vous réveillez dans les entrailles d'une station de métro abandonnée.\n"
        "L'air est lourd, chargé de poussière et d'une odeur âcre de moisissure.\n"
        "Un faible rayon de lumière filtre par une grille au plafond, révélant les contours de votre abri de fortune.\n"
        "Dehors, le monde n'est plus que ruines et dangers. Mais vous êtes vivant. Pour l'instant."
    )
