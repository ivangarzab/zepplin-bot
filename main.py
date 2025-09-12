import os
import random
import discord
from datetime import datetime, time
from dotenv import load_dotenv
from discord.ext import commands
from discord.ext import tasks
from utils.embeds import create_embed

# DEFAULT_CHANNEL = 1391787701954674719 # some other channel...
DEFAULT_CHANNEL = 1039326367973642363 # Chernobyl
load_dotenv(override=True)
TOKEN = os.getenv("ZEPPLIN_TOKEN")

REACTIONS = ['⚡️', '👽', '🍄', '🌙', '🔥', '👾', '🦉', '🐺', '🍁']

DAILY_MESSAGES = [
    "Perfect day to bend all four elements! 🔥💨💧🪨",
    "Welcome to a new day! 🌞",
    "Today will be full of new constructions 🏗️",
    "How many benders will you recruit today? 👥",
    "⚖️ A great day to restore balance into the world!",
    "🙏 Remember to donate to the alliance today!",

]

if not TOKEN:
    raise ValueError("TOKEN environment variable is not set.")
print(f'~~~~~~Got Discord TOKEN successfully~~~~~~')

intents = discord.Intents.all()
client = commands.Bot(command_prefix='/', intents=intents)

@tasks.loop(time=time(hour=0, minute=0))
async def daily_message():
    print(f"Daily alarm triggered at {datetime.now()}")
    channel = client.get_channel(DEFAULT_CHANNEL)
    if channel:
        message = random.choice(DAILY_MESSAGES)
        await channel.send(message)

@client.event
async def on_ready():
    print(f'~~~~~~We have logged in as {client.user}~~~~~~')
    if not daily_message.is_running():
        daily_message.start()
    
    # Sync slash commands
    try:
        synced = await client.tree.sync()
        print(f'Synced {len(synced)} command(s)')
    except Exception as e:
        print(f'Failed to sync commands: {e}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return # Avoid the bot responding to itself
    
    author = message.author.mention
    msgFormat = message.content.lower()
    allowed_mentions = discord.AllowedMentions(everyone = True)

    print(f'Got a new message=\'{message.content}\'\n\tguild={message.guild}\n\tauthor={message.author.name}')

    # Add a reaction to message
    if not message.content.startswith('!') and random.random() < 0.3:
        await message.add_reaction(random.choice(REACTIONS))

    # This line is necessary to process commands within on_message()
    await client.process_commands(message) 
    
@client.event
async def on_member_join(member):
    print(f"{member} joined the server")
    channel = client.get_channel(DEFAULT_CHANNEL)
    if not channel:
        return
    await channel.send(f"Welcome, {member}, to the Shred Zepplin discord server!")

@client.tree.command(name="report_attack", description="Report an attack on you, or any other alliance member")
async def report_attack_command(
    interaction: discord.Interaction,
    attacker: str = None,
    victim: str = None
):
    # Determine victim - use user's display name if not provided
    victim_name = victim if victim else interaction.user.display_name
    
    # Build description based on available information
    if attacker:
        description = f"{victim_name} was attacked by {attacker}! Please assist them in defending our alliance!"
    else:
        description = f"{victim_name} was attacked by enemy forces! Please assist them in defending our alliance!"
    
    # Create embed with dynamic fields
    embed_data = {
        "title": "🗡️ We've been attacked!",
        "description": description,
        "color_key": "attack",
        "fields": [
            {"name": "Victim", "value": victim_name, "inline": True},
            {"name": "Reported by", "value": interaction.user.display_name, "inline": True}
        ]
    }
    
    # Add attacker field only if provided
    if attacker:
        embed_data["fields"].insert(1, {"name": "Attacker", "value": attacker, "inline": True})
    
    embed = create_embed(**embed_data)
    await interaction.response.send_message(embed=embed)
    print(f"Sent 'report attack' command response. Victim: {victim_name}, Attacker: {attacker or 'Unknown'}")

client.run(TOKEN) # Run the bot with your bot token