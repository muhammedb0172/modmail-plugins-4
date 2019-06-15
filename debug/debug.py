import discord
import asyncio
from discord.ext import commands

from core import checks

from core.models import PermissionLevel

#Cog = getattr(commands, 'Cog', object)

class Debug(commands.Cog):

    """Get Useful Stats Directly In An Embed About Either The ModMail Bot, A User Or The Server."""

    
    
    def __init__(self, bot):

        self.bot = bot
  
    @commands.group(name="dbug", invoke_without_command=True)
    @checks.has_permissions(PermissionLevel.ADMINISTRATOR)
    async def dbug(self, ctx):
        """Send Debug Links Directly To Hastebin In Much Shorter Time Than Normal"""

        await ctx.send_help(ctx.command)
        
   
    @dbug.command(name="start")
    @checks.has_permissions(PermissionLevel.ADMINISTRATOR)
    async def start(self, ctx):
        """Debug A Command"""
        
        timer = 10
        
        await ctx.invoke(self.bot.get_command("debug wipe"))
        
        textchannel.last_message.delete
        
        msg = await ctx.send(embed=discord.Embed(
            color=discord.Color.blurple(),
            description="10 Seconds Back"
        ))
        
        for i in range(10):
            await asyncio.sleep(1)
            timer = timer-1
            await msg.edit(embed=discord.Embed(
            color=discord.Color.blurple(),
            description=f"{timer} Seconds Back"
            ))
            
        await msg.edit(embed=discord.Embed(
            color=discord.Color.blurple(),
            description=f"Done, Your Hastebin Link Is Coming Now"
        ))    
        
        await ctx.invoke(self.bot.get_command("debug hastebin"))

def setup(bot):

    bot.add_cog(Debug(bot))
