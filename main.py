import os
import random
import discord
from dotenv import load_dotenv
from discord.ext import commands
from discord.ext import tasks

DEFAULT_CHANNEL = 1391787701954674719
load_dotenv(override=True)
TOKEN = os.getenv("ZEPPLIN_TOKEN")

if not TOKEN:
    raise ValueError("TOKEN environment variable is not set.")
print(f'~~~~~~Got Discord TOKEN successfully~~~~~~')

intents = discord.Intents.all()
client = commands.Bot(command_prefix='/', intents=intents)

@client.event
async def on_ready():
    print(f'~~~~~~We have logged in as {client.user}~~~~~~')

@client.event
async def on_message(message):
    if message.author == client.user:
        return # Avoid the bot responding to itself
    
    author = message.author.mention
    msgFormat = message.content.lower()
    allowed_mentions = discord.AllowedMentions(everyone = True)

    print(f'Got a new message=\'{message.content}\'\n\tguild={message.guild}\n\tauthor={message.author.name}')

    #TODO: Implement message handling logic

    # This line is necessary to process commands within on_message()
    await client.process_commands(message) 
    
@client.event
async def on_member_join(member):
    println(f"{member} joined the server")
    channel = client.get_channel(DEFAULT_CHANNEL)
    if not channel:
        return
    await channel.send(f"Welcome, {member}, to the Shred Zepplin discord server!")

client.run(TOKEN) # Run the bot with your bot token