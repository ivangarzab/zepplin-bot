"""
Invasion commands for alliance coordination
"""
import asyncio
import discord
from datetime import datetime, timedelta
from utils.embeds import create_embed

def setup_invasion_commands(client):
    """Set up all invasion-related commands"""
    
    async def send_invasion_message(channel, initiator_name):
        """Helper function to send the invasion message"""
        embed_data = {
            "title": "👻 INVASION TIME! 👹",
            "description": "The time has come! All alliance members are called to arms for a coordinated invasion! Drop everything and join the fight!",
            "color_key": "invasion",
            "fields": [
                {"name": "Call to Arms", "value": "ALL HANDS ON DECK! 😈", "inline": True},
                {"name": "Initiated by", "value": initiator_name, "inline": True}
            ]
        }
        
        embed = create_embed(**embed_data)
        await channel.send(embed=embed)

    @client.tree.command(name="invasion", description="Call all alliance members for a massive invasion")
    async def invasion_command(interaction: discord.Interaction):
        await interaction.response.defer()
        await send_invasion_message(interaction.channel, interaction.user.display_name)
        print(f"Sent 'invasion' command response. Initiated by: {interaction.user.display_name}")

    @client.tree.command(name="schedule_invasion", description="Schedule an invasion to begin in X minutes")
    async def schedule_invasion_command(
        interaction: discord.Interaction,
        minutes: int
    ):
        if minutes <= 0 or minutes > 1440:  # Max 24 hours
            await interaction.response.send_message("⚠️ Please specify between 1-1440 minutes (24 hours max)", ephemeral=True)
            return

        # Send initial scheduling message
        invasion_time = datetime.now() + timedelta(minutes=minutes)
        time_str = invasion_time.strftime("%I:%M %p")
        
        embed_data = {
            "title": "⏰ Invasion Scheduled",
            "description": f"An invasion has been scheduled to begin in **{minutes} minutes** at **{time_str}**!\n\nPrepare your forces and be ready!",
            "color_key": "invasion",
            "fields": [
                {"name": "Time until invasion", "value": f"{minutes} minutes", "inline": True},
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
            await send_invasion_message(channel, initiator)
            print(f"Sent scheduled invasion message. Originally scheduled by: {initiator}")
        
        # Start the delayed task
        asyncio.create_task(delayed_invasion())
        print(f"Scheduled invasion for {minutes} minutes. Scheduled by: {initiator}")