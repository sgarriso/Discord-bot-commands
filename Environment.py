import os
from dotenv import load_dotenv

class Environment:
    DEV = "dev"
    PROD = "prod"
    
    def __init__(self):
        load_dotenv()
        self.guild_id = os.getenv('guild_id')
        self.stage = os.getenv("stage")
        self.discord_key = os.getenv("discord_key")