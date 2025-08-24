# 🎮 ROADMAP - Chatbot Discord Post-Apocalyptique

## 📊 État actuel du projet
- ✅ Structure de base du bot Discord
- ✅ Système de persistance des données (partiel)
- ✅ Commandes `/start` et `/status` basiques
- ❌ Intégration IA (Gemini)
- ❌ Système de jeu complet
- ❌ Narration interactive

---

## 🎯 Phase 1 : Infrastructure Core (Semaine 1)

### 1.1 Configuration et environnement
- [x] Ajouter `GEMINI_API_KEY` dans `.env.example`
- [x] Mettre à jour `requirements.txt` avec :
  ```
  google-generativeai>=0.3.0
  aiofiles>=23.0.0
  asyncio>=3.4.3
  python-dateutil>=2.8.2
  ```
- [x] Créer `config.py` pour centraliser la configuration
  - [x] Charger les variables d'environnement
  - [x] Définir les constantes du jeu (difficultés, seuils, etc.)
  - [x] Configurer les timeouts et limites

### 1.2 Architecture des agents IA
- [x] Créer `AGENTS.md` avec la spécification des agents
- [x] Créer `game/ai_manager.py`
  - [x] Classe `NarratorAgent` pour la narration
  - [x] Classe `NPCAgent` pour les PNJs
  - [x] Classe `EventAgent` pour les événements aléatoires
  - [x] Système de prompts contextuels
  - [x] Gestion de la mémoire conversationnelle

### 1.3 Logging et monitoring
- [x] Créer `game/logger.py`
  - [x] Configuration des niveaux de log
  - [x] Rotation des fichiers de log
  - [x] Logs spécifiques par utilisateur
- [x] Ajouter des métriques de performance
  - [x] Temps de réponse des commandes
  - [x] Usage de l'API Gemini
  - [x] Statistiques des joueurs

---

## 🎲 Phase 2 : Système de jeu complet (Semaine 2)

### 2.1 Mécanique de jets de dés
- [ ] Créer `game/dice_system.py`
  - [ ] Fonction `roll_d20(skill_bonus=0)`
  - [ ] Calcul des difficultés dynamiques
  - [ ] Gestion des critiques (1 et 20)
  - [ ] Modificateurs situationnels
  - [ ] Historique des jets

### 2.2 Système de progression
- [ ] Créer `game/progression.py`
  - [ ] Compteur d'utilisation des compétences
  - [ ] Système de level up automatique
  - [ ] Déblocage de capacités spéciales
  - [ ] Calcul de l'XP par action

### 2.3 Cycle temporel
- [ ] Créer `game/time_manager.py`
  - [ ] Enum des périodes : `DAWN`, `MORNING`, `NOON`, `AFTERNOON`, `EVENING`, `NIGHT`
  - [ ] Fonction `advance_time(user_id, periods=1)`
  - [ ] Déclencheurs automatiques par période
  - [ ] Événements liés au temps
  - [ ] Modificateurs selon l'heure (vision nocturne, etc.)

### 2.4 Système de besoins vitaux
- [ ] Créer `game/survival_system.py`
  - [ ] Gestion dynamique faim/soif/fatigue
  - [ ] Effets des carences (malus aux jets)
  - [ ] Système de maladies et blessures
  - [ ] Radiation et mutations
  - [ ] Température corporelle

---

## 🗺️ Phase 3 : Monde et exploration (Semaine 3)

### 3.1 Système de carte
- [ ] Créer `game/map_system.py`
  - [ ] Grille hexagonale 100x100
  - [ ] Génération procédurale des zones
  - [ ] Types de terrain (ruines, forêt, zones irradiées)
  - [ ] Calcul des distances et déplacements
  - [ ] Brouillard de guerre

### 3.2 Lieux dynamiques
- [ ] Créer `game/locations.py`
  - [ ] Base de données des lieux types
  - [ ] Génération de points d'intérêt
  - [ ] État des lieux (pillé, occupé, dangereux)
  - [ ] Ressources disponibles par lieu
  - [ ] Événements spécifiques aux lieux

### 3.3 Système de déplacement
- [ ] Implémenter dans `game_logic.py`
  - [ ] Commande `/move [direction]`
  - [ ] Calcul du temps de trajet
  - [ ] Rencontres aléatoires
  - [ ] Consommation de fatigue
  - [ ] Découverte de nouveaux lieux

---

## ⚔️ Phase 4 : Combat et dangers (Semaine 4)

### 4.1 Système de combat
- [ ] Créer `game/combat_system.py`
  - [ ] Initiative et ordre des tours
  - [ ] Actions de combat (attaquer, défendre, fuir)
  - [ ] Calcul des dégâts et armure
  - [ ] États de combat (étourdi, saignement)
  - [ ] Combat à distance vs mêlée

### 4.2 Ennemis et créatures
- [ ] Créer `game/enemies.py`
  - [ ] Base de données des ennemis types
  - [ ] IA de combat basique
  - [ ] Système de loot
  - [ ] Niveaux de difficulté
  - [ ] Comportements spéciaux (embuscade, fuite)

### 4.3 Système de factions
- [ ] Créer `game/factions.py`
  - [ ] Relations entre factions
  - [ ] Système de réputation
  - [ ] Missions de faction
  - [ ] Territoires contrôlés
  - [ ] Conflits inter-factions

---

## 💼 Phase 5 : Inventaire et crafting (Semaine 5)

### 5.1 Gestion avancée de l'inventaire
- [ ] Améliorer `game/inventory_manager.py`
  - [ ] Poids et encombrement
  - [ ] Catégories d'objets
  - [ ] Durabilité des objets
  - [ ] Objets stackables
  - [ ] Conteneurs (sacs, coffres)

### 5.2 Système de crafting
- [ ] Créer `game/crafting_system.py`
  - [ ] Recettes de base
  - [ ] Découverte de recettes
  - [ ] Outils requis
  - [ ] Taux de réussite
  - [ ] Améliorations d'objets

### 5.3 Commerce
- [ ] Créer `game/trading_system.py`
  - [ ] Système de troc
  - [ ] Valeur des objets
  - [ ] Marchands PNJs
  - [ ] Marchés dynamiques
  - [ ] Inflation/déflation

---

## 🤖 Phase 6 : PNJs et relations (Semaine 6)

### 6.1 Système de PNJs
- [ ] Créer `game/npc_system.py`
  - [ ] Génération procédurale de PNJs
  - [ ] Personnalités et traits
  - [ ] Dialogues contextuels via Gemini
  - [ ] Mémoire des interactions
  - [ ] Routines quotidiennes

### 6.2 Relations sociales
- [ ] Créer `game/social_system.py`
  - [ ] Niveaux de relation (-100 à +100)
  - [ ] Actions sociales (persuader, menacer, séduire)
  - [ ] Conséquences des choix sociaux
  - [ ] Alliances et trahisons
  - [ ] Romance et amitié

### 6.3 Quêtes
- [ ] Créer `game/quest_system.py`
  - [ ] Quêtes principales
  - [ ] Quêtes secondaires générées
  - [ ] Système de récompenses
  - [ ] Branches narratives
  - [ ] Journal de quêtes

---

## 🎮 Phase 7 : Commandes Discord complètes (Semaine 7)

### 7.1 Commandes de base
- [ ] `/action [texte]` - Action libre avec parsing IA
- [ ] `/inventory` - Affichage formaté de l'inventaire
- [ ] `/map` - Carte ASCII ou image
- [ ] `/rest` - Repos (court/long)
- [ ] `/save` - Sauvegarde manuelle
- [ ] `/summary` - Résumé de l'histoire

### 7.2 Commandes avancées
- [ ] `/craft [objet]` - Interface de crafting
- [ ] `/trade [pnj]` - Commerce
- [ ] `/examine [objet/lieu]` - Description détaillée
- [ ] `/use [objet] [cible]` - Utilisation d'objets
- [ ] `/talk [pnj]` - Dialogue
- [ ] `/sneak` - Mode furtif
- [ ] `/search` - Fouiller la zone

### 7.3 Commandes de gestion
- [ ] `/settings` - Préférences utilisateur
- [ ] `/help [commande]` - Aide contextuelle
- [ ] `/stats detailed` - Statistiques complètes
- [ ] `/achievements` - Succès débloqués
- [ ] `/leaderboard` - Classement global

### 7.4 Interface Discord améliorée
- [ ] Embeds riches avec images
- [ ] Boutons interactifs pour actions rapides
- [ ] Menus déroulants pour sélections
- [ ] Réactions pour choix multiples
- [ ] Thread automatique par session de jeu

---

## 🌟 Phase 8 : Événements et narration (Semaine 8)

### 8.1 Système d'événements
- [ ] Créer `game/event_system.py`
  - [ ] Pool d'événements par contexte
  - [ ] Déclencheurs conditionnels
  - [ ] Chaînes d'événements
  - [ ] Événements mondiaux
  - [ ] Conséquences à long terme

### 8.2 Narration IA avancée
- [ ] Améliorer `ai_manager.py`
  - [ ] Contexte enrichi pour Gemini
  - [ ] Styles narratifs variés
  - [ ] Descriptions dynamiques
  - [ ] Génération de lore
  - [ ] Cohérence narrative

### 8.3 Ambiance et immersion
- [ ] Créer `game/atmosphere.py`
  - [ ] Descriptions météo dynamiques
  - [ ] Sons ambiants (textuels)
  - [ ] Effets visuels ASCII
  - [ ] Messages atmosphériques
  - [ ] Easter eggs

---

## 🔧 Phase 9 : Optimisation et polish (Semaine 9)

### 9.1 Performance
- [ ] Cache des données fréquentes
- [ ] Optimisation des requêtes Gemini
- [ ] Compression des sauvegardes
- [ ] Chargement asynchrone
- [ ] Pool de connexions

### 9.2 Équilibrage
- [ ] Ajustement des difficultés
- [ ] Balance économique
- [ ] Courbes de progression
- [ ] Rareté des ressources
- [ ] Tests de gameplay

### 9.3 Qualité de vie
- [ ] Auto-save périodique
- [ ] Système d'undo limité
- [ ] Raccourcis de commandes
- [ ] Tutoriel interactif
- [ ] Mode histoire facile

---

## 🚀 Phase 10 : Features avancées (Semaine 10)

### 10.1 Multijoueur coopératif
- [ ] Créer `game/multiplayer.py`
  - [ ] Parties partagées
  - [ ] Échanges entre joueurs
  - [ ] Raids en groupe
  - [ ] Chat in-game
  - [ ] Synchronisation des mondes

### 10.2 Système de saisons
- [ ] Créer `game/seasons.py`
  - [ ] Événements saisonniers
  - [ ] Récompenses limitées
  - [ ] Leaderboards temporaires
  - [ ] Défis communautaires
  - [ ] Lore évolutif

### 10.3 Modding et personnalisation
- [ ] API de modding
- [ ] Éditeur de scénarios
- [ ] Partage de mondes
- [ ] Thèmes personnalisés
- [ ] Workshop communautaire

---

## 📝 Documentation et tests

### Documentation
- [ ] README complet avec exemples
- [ ] Wiki des commandes
- [ ] Guide du joueur
- [ ] Documentation API
- [ ] Changelog détaillé

### Tests
- [ ] Tests unitaires pour chaque module
- [ ] Tests d'intégration Discord
- [ ] Tests de charge
- [ ] Tests de régression
- [ ] Beta testing communautaire

---

## 🎯 Métriques de succès

### KPIs techniques
- Temps de réponse < 2s
- Uptime > 99%
- Utilisation API Gemini < quota gratuit
- Taux d'erreur < 1%

### KPIs gameplay
- Rétention J7 > 40%
- Session moyenne > 30 min
- Actions par session > 20
- Taux de complétion tutoriel > 80%

---

## 🚦 Prochaines étapes immédiates

1. **Aujourd'hui** : Créer `AGENTS.md` et `config.py`
2. **Demain** : Intégrer Gemini API avec un NarratorAgent basique
3. **J+2** : Implémenter la commande `/action` avec parsing IA
4. **J+3** : Système de jets de dés complet
5. **J+4** : Cycle temporel fonctionnel
6. **J+5** : Première version jouable avec narration

---

## 📅 Planning suggéré

| Semaine | Focus | Livrable |
|---------|-------|----------|
| 1 | Infrastructure | Bot connecté avec IA |
| 2 | Mécaniques core | Système de jeu jouable |
| 3 | Exploration | Monde navigable |
| 4 | Combat | Dangers et survie |
| 5 | Économie | Inventaire et craft |
| 6 | Social | PNJs interactifs |
| 7 | UX Discord | Interface complète |
| 8 | Narration | Immersion maximale |
| 9 | Polish | Version stable |
| 10 | Avancé | Features bonus |

---

## ⚠️ Risques et mitigations

| Risque | Impact | Mitigation |
|--------|--------|------------|
| Limite API Gemini | Critique | Cache agressif + fallback |
| Complexité narration | Élevé | Prompts prédéfinis + templates |
| Performance Discord | Moyen | Pagination + async |
| Sauvegarde corrompue | Élevé | Backups + validation |
| Équilibrage gameplay | Moyen | Analytics + feedback |
