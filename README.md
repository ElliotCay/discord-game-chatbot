# discord-game-chatbot

Chatbot de jeu post-apocalyptique pour Discord.

## Installation

1. Créez un fichier `.env` à partir de `.env.example` et renseignez votre `DISCORD_TOKEN` et votre `GEMINI_API_KEY`.
2. Installez les dépendances :
   ```bash
   pip install -r requirements.txt
   ```
3. Lancez le bot :
   ```bash
   python bot.py
   ```

Les données de jeu sont stockées dans le dossier `game_data/` et sont séparées par identifiant d'utilisateur Discord.
