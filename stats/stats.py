import discord

from discord.ext import commands

from core import checks

from core.models import PermissionLevel

#Cog = getattr(commands, 'Cog', object)

class Stats(commands.Cog):

    """Get  Useful Stats Directly In An Embed About Either The ModMail Bot Or The Server."""

    

    def __init__(self, bot):

        self.bot = bot
  
    @commands.command()

    @checks.has_permissions(PermissionLevel.ADMINISTRATOR)

    async def botstats(self, ctx):

        """Get A Neat Embed With Many Useful Stats About The ModMail Bot."""

        embed = discord.Embed(

            title=" ",

            color=discord.Color.blue(),

            description=f"**Here is the stats for {self.bot.user.name}, enjoy them:**",

        )
        embed.add_field(name=f"Invite Link For {self.bot.user.name}",value=f"[Here](https://discordapp.com/api/oauth2/authorize?client_id={self.bot.user.id}&permissions=268443792&scope=bot) Is The Invite Link For {self.bot.user.name}.")
        embed.add_field(name="Bot User ID",value=f"`{self.bot.user.id}` Is The User ID For {self.bot.user.name}")
        embed.add_field(name=f"Bot Prefix",value=f"The Prefix For {self.bot.user.name} Is `{self.bot.prefix}` Or {self.bot.user.mention}")
        embed.add_field(name=f"Latency",value=f"The Latency For {self.bot.user.name} Is {self.bot.latency * 1000:.2f} MilliSeconds / {self.bot.latency:.3f} Seconds")
        embed.add_field(name=f"Important Information",value=f"Remember To :star: The [Repo](https://github.com/kyb3r/modmail) And Become A Patreon [Here](https://patreon.com/kyber)")
        embed.set_thumbnail(url=str(self.bot.user.avatar_url))
        embed.set_footer(text=f"Stats missing? DM MiTonder#1792 with a suggestion for new stats")
        embed.set_author(name=f"{self.bot.user.name} Stats")

        await ctx.send(embed=embed)
        
   
    @commands.command()

    @checks.has_permissions(PermissionLevel.ADMINISTRATOR)

    async def serverstats(self, ctx):

        """Get A Neat Embed With Many Useful Stats About Your Server"""

        embed = discord.Embed(

            title=" ",

            color=discord.Color.blue(),

            description=f"**Here is the stats for {ctx.guild.name}, enjoy them:**",

        )
        embed.add_field(name=f"Member Count",value=f"There Are {ctx.guild.member_count} Members In {ctx.guild.name}")
        embed.add_field(name="Guild ID",value=f"The ID For {ctx.guild.name} Is `{ctx.guild.id}`")
        embed.add_field(name=f"Server Owner",value=f"The Owner Of {ctx.guild.name} Is {ctx.guild.owner}")
        embed.add_field(name=f"Server Creation Date And Time",value=f"{ctx.guild.name} Was {ctx.guild.created_at:%d-%m-%Y} And The Time Was {ctx.guild.created_at:%X}")
        embed.add_field(name=f"Important Information",value=f"Remember To :star: The [Repo](https://github.com/kyb3r/modmail) And Become A Patreon [Here](https://patreon.com/kyber)")
        embed.set_thumbnail(url=str(ctx.guild.icon_url))
        embed.set_footer(text=f"Stats missing? DM MiTonder#1792 with a suggestion for new stats")
        embed.set_author(name=f"{ctx.guild.name} Stats")

        await ctx.send(embed=embed)
        
        
    @commands.command()

    @checks.has_permissions(PermissionLevel.ADMINISTRATOR)

    async def allstats(self, ctx):

        """Sends 2 Embeds, Both `{prefix}serverstats` And `{prefix}botstats`"""

        embed = discord.Embed(

            title=" ",

            color=discord.Color.blue(),

            description=f"**Here is the stats for {ctx.guild.name}, enjoy them:**",

        )
        embed.add_field(name=f"Member Count",value=f"There Are {ctx.guild.member_count} Members In {ctx.guild.name}")
        embed.add_field(name="Guild ID",value=f"The ID For {ctx.guild.name} Is `{ctx.guild.id}`")
        embed.add_field(name=f"Server Owner",value=f"The Owner Of {ctx.guild.name} Is {ctx.guild.owner}")
        embed.add_field(name=f"Server Creation Date And Time",value=f"{ctx.guild.name} Was {ctx.guild.created_at:%d-%m-%Y} And The Time Was {ctx.guild.created_at:%X}")
        embed.add_field(name=f"Important Information",value=f"Remember To :star: The [Repo](https://github.com/kyb3r/modmail) And Become A Patreon [Here](https://patreon.com/kyber)")
        embed.set_thumbnail(url=str(ctx.guild.icon_url))
        embed.set_footer(text=f"Stats missing? DM MiTonder#1792 with a suggestion for new stats")
        embed.set_author(name=f"{ctx.guild.name} Stats")

        await ctx.send(embed=embed)
        
        embed = discord.Embed(

            title=" ",

            color=discord.Color.blue(),

            description=f"**Here is the stats for {self.bot.user.name}, enjoy them:**",

        )
        embed.add_field(name=f"Invite Link For {self.bot.user.name}",value=f"[Here](https://discordapp.com/api/oauth2/authorize?client_id={self.bot.user.id}&permissions=268443792&scope=bot) Is The Invite Link For {self.bot.user.name}.")
        embed.add_field(name="Bot User ID",value=f"`{self.bot.user.id}` Is The User ID For {self.bot.user.name}")
        embed.add_field(name=f"Bot Prefix",value=f"The Prefix For {self.bot.user.name} Is `{self.bot.prefix}` Or {self.bot.user.mention}")
        embed.add_field(name=f"Latency",value=f"The Latency For {self.bot.user.name} Is {self.bot.latency * 1000:.2f} MilliSeconds / {self.bot.latency:.3f} Seconds")
        embed.add_field(name=f"Important Information",value=f"Remember To :star: The [Repo](https://github.com/kyb3r/modmail) And Become A Patreon [Here](https://patreon.com/kyber)")
        embed.set_thumbnail(url=str(self.bot.user.avatar_url))
        embed.set_footer(text=f"Stats missing? DM MiTonder#1792 with a suggestion for new stats")
        embed.set_author(name=f"{self.bot.user.name} Stats")

        await ctx.send(embed=embed)
        
def setup(bot):

    bot.add_cog(Stats(bot))
