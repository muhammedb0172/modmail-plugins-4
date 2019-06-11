import discord

from discord.ext import commands

from core import checks

from core.models import PermissionLevel

#Cog = getattr(commands, 'Cog', object)

class BotStats(commands.Cog):

    """Get  Useful Stats About Your ModMail Bot"""

    

    def __init__(self, bot):

        self.bot = bot

    

    @commands.command()

    @checks.has_permissions(PermissionLevel.ADMINISTRATOR)

    async def stats(self, ctx):

        """Get A Neat Embed With Many Useful Stats About Your ModMail Bot."""

        embed = discord.Embed(

            title="Stats",

            color=discord.Color.blue(),

            description=f"Here is the stats for {self.bot.user.name}, enjoy them.",

        )
        embed.add_field(name=f"Invite Link For {self.bot.user.name}",value=f"[Here](https://discordapp.com/api/oauth2/authorize?client_id={self.bot.user.id}&permissions=268443792&scope=bot) Is The Invite Link For {self.bot.user.name}.")
        embed.add_field(name="Bot User ID",value=f"`{self.bot.user.id}` Is The User ID For {self.bot.user.name}")
        embed.add_field(name=f"Bot Prefix",value=f"The Prefix For {self.bot.user.name} Is `{self.bot.prefix}` Or {self.bot.user.mention}")
        embed.add_field(name=f"Latency",value=f"The Latency For {self.bot.user.name} Is {self.bot.latency * 1000:.2f} MilliSeconds / {self.bot.latency:.3f} Seconds")
        embed.set_thumbnail(url=str(self.bot.user.avatar_url))
        embed.set_footer(text=f"Remember To :star: The [Repo](https://github.com/kyb3r/modmail) And Become A Patreon [Here](https://patreon.com/kyber) ")

        await ctx.send(embed=embed)

def setup(bot):

    bot.add_cog(BotStats(bot))
