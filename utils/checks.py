"""
Custom checks for command restrictions
"""
import discord
from discord import app_commands

BOT_COMMANDS_CHANNEL_ID = 1433660698268925993 #bot-commands channel

def bot_commands_only():
    """Decorator to restrict commands to bot-commands channel only"""
    async def predicate(interaction: discord.Interaction) -> bool:
        if interaction.channel_id != BOT_COMMANDS_CHANNEL_ID:
            await interaction.response.send_message(
                "⚠️ This command can only be used in <#{BOT_COMMANDS_CHANNEL_ID}>",
                ephemeral=True
            )
            return False
        return True
    return app_commands.check(predicate)