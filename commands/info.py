"""
Info commands for bot help and guidance
"""
import discord
from utils.embeds import create_embed
from utils.checks import bot_commands_only

def setup_info_commands(client):
    """Set up all info-related commands"""
    
    @client.tree.command(name="help", description="Show all available commands and how to use them")
    @bot_commands_only()
    async def help_command(interaction: discord.Interaction):
        embed_data = {
            "title": "🚀 Zepplin Bot Commands",
            "description": "Alliance coordination commands for **Shred Zepplin** in *Avatar: Realms Collide*",
            "color_key": "base",
            "fields": [
                {
                    "name": "⚔️ Combat Reporting",
                    "value": "`/report_attack [attacker] [victim]` - Report attacks\n`/report_scout [scout] [victim]` - Report enemy scouts",
                    "inline": False
                },
                {
                    "name": "🎯 Rally Coordination", 
                    "value": "`/rally_leader <target>` - Call attack on enemy\n`/rally_stronghold <target>` - Organize stronghold capture",
                    "inline": False
                },
                {
                    "name": "👹 Invasion Management",
                    "value": "`/invasion` - Instant alliance call to arms\n`/schedule_invasion <minutes>` - Schedule invasion (1-1440 min)",
                    "inline": False
                },
                {
                    "name": "💡 Usage Tips",
                    "value": "• Use `[optional]` parameters as needed\n• `<required>` parameters must be provided\n• All times shown in your local timezone\n• Bot sends daily motivation at midnight UTC",
                    "inline": False
                }
            ]
        }
        
        embed = create_embed(**embed_data)
        await interaction.response.send_message(embed=embed, ephemeral=True)
        print(f"Sent help command response to {interaction.user.display_name}")