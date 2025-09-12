# 🚀 Zepplin Bot

A powerful Discord bot for **Shred Zepplin** alliance coordination in *Avatar: Realms Collide*. Built to streamline communication, coordinate attacks, and rally your alliance members for maximum tactical advantage.

<div align="center">
  <img src="public/icon.png" alt="Zepplin Bot Icon" width="200"/>
</div>

## ✨ Features

### 📅 Daily Motivation

**Automatic daily messages** at midnight UTC with randomized motivational content

### ⚔️ Combat Reporting

- **`/report_attack`** - Report attacks on alliance members
  - Optional `attacker` and `victim` parameters
  - Defaults to command user if no victim specified
  - Rich embeds with color-coded threat levels
  
- **`/report_scout`** - Report enemy reconnaissance activities
  - Optional `scout` and `victim` parameters
  - Early warning system for potential incoming attacks

### 🎯 Rally Coordination
- **`/rally_leader`** - Call for targeted attacks against specific enemies
  - Requires `target` parameter
  - Perfect for coordinated strikes on rival players

- **`/rally_stronghold`** - Organize stronghold capture missions
  - Requires `target` parameter
  - Welcoming tone encourages broad alliance participation

### 👹 Invasion Management
- **`/invasion`** - Instant alliance-wide call to arms
  - No parameters needed - maximum urgency
  - All-hands-on-deck emergency coordination

- **`/schedule_invasion`** - Plan invasions in advance
  - Specify delay in `minutes` (1-1440 max)
  - Shows live countdown with user-localized timestamps
  - Automatically triggers invasion call when time arrives
  - Updates original message to show completion status

## 🚀 Setup

### Prerequisites
- Python 3.9+
- Discord.py library
- python-dotenv for environment management

### Installation
1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Create `.env` file with your Discord bot token:
   ```
   ZEPPLIN_TOKEN=your_discord_bot_token_here
   ```
4. Configure `DEFAULT_CHANNEL` in `main.py` for your alliance channel
5. Run: `python main.py`

### Bot Permissions Required
- Send Messages
- Use Slash Commands
- Embed Links
- Add Reactions

## 🎮 Usage Examples

### Quick Strike Coordination
```
/rally_leader target:EnemyPlayer
/invasion
```

### Planned Operations
```
/schedule_invasion minutes:60
# Wait for automatic invasion trigger...
```

### Intelligence Gathering
```
/report_scout scout:EnemyName victim:AllyName
/report_attack attacker:EnemyForce victim:DefenderName
```

## 🔮 Future Enhancements (v2+)

- Battle strategy sharing
- Achievement celebrations
- Reaction-based participation tracking
- @everyone mentions for urgent alerts

## ⚡️ Built For Shred Zepplin

This bot is specifically designed for the **Shred Zepplin** alliance in _**Avatar: Realms Collide**_. Every feature is crafted to enhance tactical coordination and maintain alliance unity through the four nations.

---

*"Perfect day to bend all four elements! 🔥💨💧🪨"*