import discord

from discord.ext import commands

from core import checks

from core.models import PermissionLevel

#Cog = getattr(commands, 'Cog', object)

class BotStats(commands.Cog):

    """Get Stats about your ModMail bot"""

    

    def __init__(self, bot):

        self.bot = bot

    

    @commands.command()

    @checks.has_permissions(PermissionLevel.ADMINISTRATOR)

    async def stats(self, ctx):

        """Get a neat embed with many useful stats for your bot."""

        embed = discord.Embed(

            title="Stats",

            color=discord.Color.blue(),

            description=f"Here is the stats for {self.bot.user.name}, enjoy them.\n",

        )
        embed.add_field(name=f"Invite link for {self.bot.user.name}",value=f"[Here](https://discordapp.com/api/oauth2/authorize?client_id={self.bot.user.id}&permissions=268443792&scope=bot) is the invite link for your bot.")
        embed.add_field(name="Bot User ID",value=f"`{self.bot.user.id}` is the user id for {self.bot.user.name}")
        embed.set_thumbnail(url=str(self.bot.user.avatar_url))

        await ctx.send(embed=embed)

def setup(bot):

    bot.add_cog(BotStats(bot))
