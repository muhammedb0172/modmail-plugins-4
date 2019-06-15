import discord

from discord.ext import commands

from core import checks

from core.models import PermissionLevel

#Cog = getattr(commands, 'Cog', object)

class debug(commands.Cog):

    """Get Useful Stats Directly In An Embed About Either The ModMail Bot, A User Or The Server."""

    

    def __init__(self, bot):

        self.bot = bot
  
    @commands.group(name="dbug", invoke_without_command=True)
    @checks.has_permissions(PermissionLevel.ADMINISTRATOR)
    async def dbug(self, ctx):
        """Send Debug Links Directly To Hastebin In Much Shorter Time Than Normal"""

        await ctx.send_help(ctx.command)
        
   
    @dbug.command(name="clear")
    @checks.has_permissions(PermissionLevel.ADMINISTRATOR)
    async def clear(self, ctx, *, command: commands.clean_content):
        """Debug A Command"""


        await ctx.invoke(bot.get_command("debug wipe"))
        await ctx.invoke(bot.get_command(f"{message}"))
        await ctx.invoke(bot.get_command("debug hastebin"))

def setup(bot):

    bot.add_cog(debug(bot))
