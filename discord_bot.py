import discord
from discord.ext import commands
from Environment import Environment


class Client(commands.Bot):
    def __init__(self):
        self.environment = Environment()
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(command_prefix='!', intents=intents)
        
    async def on_ready(self):
        try:
            
            guild_id = discord.Object(id=self.environment.guild_id) if self.environment.stage == Environment.DEV else None
            print(guild_id)
            synced = await self.tree.sync(guild=guild_id)
        except Exception as e:
            print(e)
        
            
    


bot = Client()
@bot.tree.command(name="ham-text", description="will say random words about Ham")
async def  sayHam(interaction: discord.Interaction):
    await interaction.response.send_message("Slab of Ham")
    

bot.run(bot.environment.discord_key)