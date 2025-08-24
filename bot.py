"""Discord bot entry point for the post-apocalyptic game."""
from __future__ import annotations

import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

from game import data_manager, game_logic, models

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def setup_hook():
    await bot.tree.sync()


@bot.tree.command(name="start", description="Initialise une nouvelle partie")
async def start(interaction: discord.Interaction, name: str):
    user_id = interaction.user.id
    character = game_logic.start_game(user_id, name)
    await interaction.response.send_message(models.intro_text())


@bot.tree.command(name="status", description="Affiche l'état du personnage")
async def status(interaction: discord.Interaction):
    user_id = interaction.user.id
    character = data_manager.read_json(user_id, game_logic.CHARACTER_FILE, None)
    if not character:
        await interaction.response.send_message("Aucune partie trouvée. Utilisez /start pour débuter.")
        return
    stats = character["stats"]
    msg = (
        f"Santé: {stats['health']} | Faim: {stats['hunger']} | Soif: {stats['thirst']} | "
        f"Fatigue: {stats['fatigue']}"
    )
    await interaction.response.send_message(msg)


def main() -> None:
    if not TOKEN:
        raise RuntimeError("DISCORD_TOKEN is not set in environment")
    bot.run(TOKEN)


if __name__ == "__main__":
    main()
