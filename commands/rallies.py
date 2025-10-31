"""
Rally commands for alliance coordination
"""
import discord
from utils.embeds import create_embed
from utils.checks import bot_commands_only

def setup_rally_commands(client):
    """Set up all rally-related commands"""
    
    @client.tree.command(name="rally_leader", description="Call for alliance members to rally against a target")
    @bot_commands_only()
    async def rally_leader_command(
        interaction: discord.Interaction,
        target: str
    ):
        embed_data = {
            "title": "🎯 Rally Call!",
            "description": f"Prepare to rally against **{target}**! All alliance members are called to action!",
            "color_key": "rally",
            "fields": [
                {"name": "Target", "value": target, "inline": True},
                {"name": "Reported by", "value": interaction.user.display_name, "inline": True},
            ]
        }
        
        embed = create_embed(**embed_data)
        await interaction.response.send_message(embed=embed)
        print(f"Sent 'rally leader' command response. Target: {target}, Reporter: {interaction.user.display_name}")

    @client.tree.command(name="rally_stronghold", description="Call for alliance members to rally towards a stronghold")
    @bot_commands_only()
    async def rally_stronghold_command(
        interaction: discord.Interaction,
        target: str
    ):
        embed_data = {
            "title": "🏰 We're taking a Stronghold 🏯",
            "description": f"Prepare to rally towards **{target}**! All alliance members are welcomed to join!!",
            "color_key": "stronghold",
            "fields": [
                {"name": "Target", "value": target, "inline": True},
                {"name": "Reported by", "value": interaction.user.display_name, "inline": True},
            ]
        }
        
        embed = create_embed(**embed_data)
        await interaction.response.send_message(embed=embed)
        print(f"Sent 'rally stronghold' command response. Target: {target}, Reporter: {interaction.user.display_name}")