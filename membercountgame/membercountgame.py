import discord
import asyncio
from discord.ext import commands
from core import checks
from core.models import PermissionLevel

#Cog = getattr(commands, 'Cog', object)

class Gamemembercount(commands.Cog):

    """Something"""

    
    def __init__(self, bot):

        self.bot = bot
  
    @commands.command(name="dbug", invoke_without_command=True)
    @checks.has_permissions(PermissionLevel.ADMINISTRATOR)
    async def gameactivity(self, ctx):
        """Let your modmail's game activity be changed to Listening to {ctx.guild.member_count} users"""

        for i in range(6):
            await ctx.invoke(self.bot.get_command(f"activity Listening to {ctx.guild.member_count} users"))
            
            await asyncio.sleep(10)
            
def setup(bot):

    bot.add_cog(Gamemembercount(bot))
