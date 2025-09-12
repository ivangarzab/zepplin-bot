"""
Invasion commands for alliance coordination
"""
import asyncio
import discord
import time
from datetime import datetime, timedelta
from utils.embeds import create_embed

def setup_invasion_commands(client):
    """Set up all invasion-related commands"""
    
    def create_invasion_embed(initiator_name):
        """Helper function to create the invasion embed"""
        embed_data = {
            "title": "👻 INVASION TIME! 👹",
            "description": "The time has come! All alliance members are called to arms for a coordinated invasion! Drop everything and join the fight!",
            "color_key": "invasion",
            "fields": [
                {"name": "Call to Arms", "value": "ALL HANDS ON DECK! 😈", "inline": True},
                {"name": "Initiated by", "value": initiator_name, "inline": True}
            ]
        }
        
        return create_embed(**embed_data)

    @client.tree.command(name="invasion", description="Call all alliance members for a massive invasion")
    async def invasion_command(interaction: discord.Interaction):
        embed = create_invasion_embed(interaction.user.display_name)
        await interaction.response.send_message(embed=embed)
        print(f"Sent 'invasion' command response. Initiated by: {interaction.user.display_name}")

    @client.tree.command(name="schedule_invasion", description="Schedule an invasion to begin in X minutes")
    async def schedule_invasion_command(
        interaction: discord.Interaction,
        minutes: int
    ):
        if minutes <= 0 or minutes > 1440:  # Max 24 hours
            await interaction.response.send_message("⚠️ Please specify between 1-1440 minutes (24 hours max)", ephemeral=True)
            return

        # Send initial scheduling message with Discord timestamp
        invasion_timestamp = int(time.time() + (minutes * 60))
        
        embed_data = {
            "title": "⏳ Invasion Scheduled",
            "description": f"An invasion has been scheduled to begin <t:{invasion_timestamp}:R> at <t:{invasion_timestamp}:F>!\n\nPrepare your forces and be ready!",
            "color_key": "invasion",
            "fields": [
                {"name": "Time until invasion", "value": f"<t:{invasion_timestamp}:R>", "inline": True},
                {"name": "Scheduled by", "value": interaction.user.display_name, "inline": True}
            ]
        }
        
        embed = create_embed(**embed_data)
        await interaction.response.send_message(embed=embed)
        
        # Schedule the actual invasion message
        channel = interaction.channel
        initiator = interaction.user.display_name
        
        async def delayed_invasion():
            await asyncio.sleep(minutes * 60)  # Convert to seconds
            
            # Edit the original schedule message to show completion
            completed_embed_data = {
                "title": "⌛️ Scheduled Invasion Launched",
                "description": f"An invasion was scheduled at <t:{invasion_timestamp}:F>!\n\nAll forced must be deployed!",
                "color_key": "invasion",
                "fields": [
                    {"name": "Time until invasion", "value": f"past", "inline": True},
                    {"name": "Scheduled by", "value": initiator, "inline": True}
                ]
            }
            completed_embed = create_embed(**completed_embed_data)
            
            try:
                # Get the original message and edit it
                original_message = await interaction.original_response()
                await original_message.edit(embed=completed_embed)
            except:
                pass  # If editing fails, continue anyway
            
            # Send the invasion message
            embed = create_invasion_embed(initiator)
            await channel.send(embed=embed)
            print(f"Sent scheduled invasion message. Originally scheduled by: {initiator}")
        
        # Start the delayed task
        asyncio.create_task(delayed_invasion())
        print(f"Scheduled invasion for {minutes} minutes. Scheduled by: {initiator}")