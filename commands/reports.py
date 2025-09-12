"""
Report commands for alliance coordination
"""
import discord
from utils.embeds import create_embed

def setup_report_commands(client):
    """Set up all report-related commands"""
    
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
            "title": "=� We've been attacked!",
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

    @client.tree.command(name="report_scout", description="Report being scouted by enemy forces")
    async def report_scout_command(
        interaction: discord.Interaction,
        scout: str = None,
        victim: str = None
    ):
        # Determine victim - use user's display name if not provided
        victim_name = victim if victim else interaction.user.display_name
        
        # Build description based on available information
        if scout:
            description = f"{victim_name} was scouted by {scout}! They may be planning an attack on our alliance!"
        else:
            description = f"{victim_name} was scouted by enemy forces! They may be planning an attack on our alliance!"
        
        # Create embed with dynamic fields
        embed_data = {
            "title": "=A We've been scouted!",
            "description": description,
            "color_key": "scout",
            "fields": [
                {"name": "Victim", "value": victim_name, "inline": True},
                {"name": "Reported by", "value": interaction.user.display_name, "inline": True}
            ]
        }
        
        # Add scout field only if provided
        if scout:
            embed_data["fields"].insert(1, {"name": "Scout", "value": scout, "inline": True})
        
        embed = create_embed(**embed_data)
        await interaction.response.send_message(embed=embed)
        print(f"Sent 'report scout' command response. Victim: {victim_name}, Scout: {scout or 'Unknown'}")