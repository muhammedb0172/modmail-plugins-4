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
        
        timer = 15

        await ctx.send(embed=discord.Embed(
            color=discord.Color.blurple(),
            description=f"Process Started, Deleting Cached Logs"
        ))
        
        await asyncio.sleep(0,5)
        
        await ctx.invoke(self.bot.get_command("debug wipe"))
        
        await asyncio.sleep(0,5)
         
        msg = await ctx.send(embed=discord.Embed(
            color=discord.Color.blurple(),
            description=f"{timer} Seconds Back, Do The Command Now"
        ))
        
        for i in range(timer):
            await asyncio.sleep(1)
            timer = timer-1
            await msg.edit(embed=discord.Embed(
            color=discord.Color.blurple(),
            description=f"{timer} Seconds Back, Do The Command Now"
            ))
        
        msg = await ctx.send(embed=discord.Embed(
            color=discord.Color.blurple(),
            description=f"Done, Your Hastebin Link Is Coming Now, While You Wait For It, Remeber To :star: The [Repo](https://github.com/kyb3r/modmail) If You Havent Done Already"
        ))
        
        await asyncio.sleep(3)
        
        await ctx.invoke(self.bot.get_command("debug hastebin"))

def setup(bot):

    bot.add_cog(Debug(bot))
