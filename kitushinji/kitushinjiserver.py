import discord

from discord.ext import commands

from core import checks

from core.models import PermissionLevel

Cog = getattr(commands, 'Cog', object)

class Welcome(Cog):

    """Say welocme to the users with this command"""

    

    def init(self, bot):

        self.bot = bot

    

    @commands.command()

    @checks.has_permissions(PermissionLevel.ADMINISTRATOR)

    async def information(self, ctx):

        """Say welcome"""

        embed = discord.Embed(

            title="Information",

            color=discord.Color.blue(),

            description="Welcome to KituShinji discord",

        )

        embed.set_thumbnail(url=ctx.guild.icon_url)

        await ctx.send(embed=embed)

def setup(bot):

    bot.add_cog(Welcome(bot))
