import discord

from discord.ext import commands

from core import checks

from core.models import PermissionLevel

#Cog = getattr(commands, 'Cog', object)

class BotInvite(commands.Cog):

    """Invite your ModMail bot"""

    

    def __init__(self, bot):

        self.bot = bot

    

    @commands.command()

    @checks.has_permissions(PermissionLevel.ADMINISTRATOR)

    async def invite(self, ctx):

        """Invite this bot, useful for communities that spread over many servers."""

        embed = discord.Embed(

            title="Bot Invite Link",

            color=discord.Color.blue(),

            description=f"The invite link for the bot is [here](https://discordapp.com/api/oauth2/authorize?client_id={self.bot.user.id}&permissions=268443792&scope=bot)",

        )

        embed.set_thumbnail(url=str(ctx.guild.icon_url))

        await ctx.send(embed=embed)

def setup(bot):

    bot.add_cog(BotInvite(bot))
