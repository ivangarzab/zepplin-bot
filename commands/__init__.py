"""
Command modules for the Zepplin Bot
"""

from .reports import setup_report_commands
from .rallies import setup_rally_commands
from.invasion import setup_invasion_commands

def setup_commands(client):
    """Set up all command modules"""
    print("Setting up command modules...")
    setup_report_commands(client)
    setup_rally_commands(client)
    setup_invasion_commands(client)