"""
The main file for the Discord bot.
Handles bot initialization, event handling, and scheduling tasks.
"""
import os
import random
import discord
from datetime import datetime, time
from dotenv import load_dotenv
from discord.ext import commands
from discord.ext import tasks
from commands import setup_commands

DEFAULT_CHANNEL = 1391787701954674719 #general channel
# DEFAULT_CHANNEL = 1039326367973642363 # Chernobyl
load_dotenv(override=True)
TOKEN = os.getenv("ZEPPLIN_TOKEN")

REACTIONS = ['⚡️', '💨', '🍄', '🌙', '🔥', '👾', '💧', '🐺', '🍁', '🪨']

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
# Setup commands from modules (do this once at startup)
setup_commands(client)

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

client.run(TOKEN) # Run the bot with your bot token