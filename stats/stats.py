import discord

from discord.ext import commands

from core import checks

from core.models import PermissionLevel

#Cog = getattr(commands, 'Cog', object)

class Stats(commands.Cog):

    """Get Useful Stats Directly In An Embed About Either The ModMail Bot, A User Or The Server."""

    

    def __init__(self, bot):

        self.bot = bot
  
    @commands.group(name="stats", aliases=["stat"], invoke_without_command=True)
    @checks.has_permissions(PermissionLevel.ADMINISTRATOR)
    async def stats(self, ctx):
        """Get A Cool Embed With A Lot Of Cool Stats About: Your ModMail, Server Or A User"""

        await ctx.send_help(ctx.command)
        
   
    @stats.command(name="server")
    @checks.has_permissions(PermissionLevel.ADMINISTRATOR)
    async def server(self, ctx):
        """Get A Cool Embed With Many Useful Stats About Your Server"""


        embed = discord.Embed(

            title=" ",

            color=discord.Color.blue(),

            description=f"**Here is the stats for {ctx.guild.name}, enjoy them:**",

        )
                
        humans = 0
        bots = 0
        for m in ctx.guild.members:
          if m.bot:
             bots += 1
          else:
             humans += 1
                
        online = 0
        for m in ctx.guild.members:
          if m.status == discord.Status.offline:
             online += 1
          else:
             continue
                
        embed.add_field(name=f"Member Count",value=f"There Are {ctx.guild.member_count} Members In {ctx.guild.name}, {humans} Of Them Are Humans, {bots} Of Them Are Bots And {ctx.guild.member_count-online} Members Are Online")
        embed.add_field(name="Guild ID",value=f"The ID For {ctx.guild.name} Is `{ctx.guild.id}`")
        embed.add_field(name="Text Channel Count",value=f"There Are {len(ctx.guild.text_channels)} Text Channels In {ctx.guild.name}")
        embed.add_field(name="Voice Channel Count",value=f"There Are {len(ctx.guild.voice_channels)} Voice Channels In {ctx.guild.name}")
        embed.add_field(name="Role Count",value=f"There Are {len(ctx.guild.roles)} Roles In {ctx.guild.name}")
        embed.add_field(name="Category Count",value=f"There Are {len(ctx.guild.categories)} Categories In {ctx.guild.name}")
        embed.add_field(name="Server Region",value=f"The Region Of {ctx.guild.name} Is {ctx.guild.region}")
        embed.add_field(name=f"Server Owner",value=f"The Owner Of {ctx.guild.name} Is {ctx.guild.owner.mention}")
        embed.add_field(name=f"Server Creation Date And Time",value=f"{ctx.guild.name} Was Created {ctx.guild.created_at:%A %d %B %Y} And The Time Was {ctx.guild.created_at:%H:%M:%S %p}")
        embed.add_field(name=f"Important Information",value=f"Remember To :star: The [Repo](https://github.com/kyb3r/modmail) And Become A Patreon [Here](https://patreon.com/kyber)")
        embed.set_thumbnail(url=str(ctx.guild.icon_url))
        embed.set_footer(text=f'If You Have Suggestions For More Stats, Please Use The Command "?suggestion" For More Info On How You Do It')
        embed.set_author(name=f"{ctx.guild.name} Stats")

        await ctx.send(embed=embed)
        
    @stats.command(name="bot")
    @checks.has_permissions(PermissionLevel.ADMINISTRATOR)
    async def bot(self, ctx):

        """Get A Neat Embed With Many Useful Stats About Your ModMail Bot."""

        embed = discord.Embed(

            title=" ",

            color=discord.Color.blue(),

            description=f"**Here is the stats for {self.bot.user.name}, enjoy them:**",

        )
        embed.add_field(name=f"Invite Link For {self.bot.user.name}",value=f"[Here](https://discordapp.com/api/oauth2/authorize?client_id={self.bot.user.id}&permissions=268443792&scope=bot) Is The Invite Link For {self.bot.user.name}.")
        embed.add_field(name="Bot User ID",value=f"`{self.bot.user.id}` Is The User ID For {self.bot.user.name}")
        embed.add_field(name=f"Bot Prefix",value=f"The Prefix For {self.bot.user.name} Is `{self.bot.prefix}` Or {self.bot.user.mention}")
        embed.add_field(name=f"Latency",value=f"The Latency For {self.bot.user.name} Is {self.bot.latency * 1000:.2f} MilliSeconds / {self.bot.latency:.3f} Seconds")
        embed.add_field(name="Bot Uptime",value=f"The Uptime For {self.bot.user.name} Is {self.bot.uptime}")
        embed.add_field(name=f"Bot User Creation Date And Time",value=f"{self.bot.user.name} Was Created {self.bot.user.created_at:%A %d %B %Y} And The Time Was {self.bot.user.created_at:%H:%M:%S %p}")
        embed.add_field(name=f"Important Information",value=f"Remember To :star: The [Repo](https://github.com/kyb3r/modmail) And Become A Patreon [Here](https://patreon.com/kyber)")
        embed.set_thumbnail(url=str(self.bot.user.avatar_url))
        embed.set_footer(text=f'If You Have Suggestions For More Stats, Please Use The Command "?suggestion" For More Info On How You Do It')
        embed.set_author(name=f"{self.bot.user.name} Stats")

        await ctx.send(embed=embed)
        
    @stats.command(name="all")
    @checks.has_permissions(PermissionLevel.ADMINISTRATOR)
    async def all(self, ctx):

        """Sends Two Embeds, Both The Servers Stats And The Bots Stats"""

        embed = discord.Embed(

            title=" ",

            color=discord.Color.blue(),

            description=f"**Here is the stats for {ctx.guild.name}, enjoy them:**",

        )
                
        humans = 0
        bots = 0
        for m in ctx.guild.members:
          if m.bot:
             bots += 1
          else:
             humans += 1
                
        online = 0
        for m in ctx.guild.members:
          if m.status == discord.Status.offline:
             online += 1
          else:
             continue
                
        embed.add_field(name=f"Member Count",value=f"There Are {ctx.guild.member_count} Members In {ctx.guild.name}, {humans} Of Them Are Humans, {bots} Of Them Are Bots And {ctx.guild.member_count-online} Members Are Online")
        embed.add_field(name="Guild ID",value=f"The ID For {ctx.guild.name} Is `{ctx.guild.id}`")
        embed.add_field(name="Text Channel Count",value=f"There Are {len(ctx.guild.text_channels)} Text Channels In {ctx.guild.name}")
        embed.add_field(name="Voice Channel Count",value=f"There Are {len(ctx.guild.voice_channels)} Voice Channels In {ctx.guild.name}")
        embed.add_field(name="Role Count",value=f"There Are {len(ctx.guild.roles)} Roles In {ctx.guild.name}")
        embed.add_field(name="Category Count",value=f"There Are {len(ctx.guild.categories)} Categories In {ctx.guild.name}")
        embed.add_field(name="Server Region",value=f"The Region Of {ctx.guild.name} Is {ctx.guild.region}")
        embed.add_field(name=f"Server Owner",value=f"The Owner Of {ctx.guild.name} Is {ctx.guild.owner.mention}")
        embed.add_field(name=f"Server Creation Date And Time",value=f"{ctx.guild.name} Was Created {ctx.guild.created_at:%A %d %B %Y} And The Time Was {ctx.guild.created_at:%H:%M:%S %p}")
        embed.add_field(name=f"Important Information",value=f"Remember To :star: The [Repo](https://github.com/kyb3r/modmail) And Become A Patreon [Here](https://patreon.com/kyber)")
        embed.set_thumbnail(url=str(ctx.guild.icon_url))
        embed.set_footer(text=f'If You Have Suggestions For More Stats, Please Use The Command "?suggestion" For More Info On How You Do It')
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
        embed.add_field(name="Bot Uptime",value=f"The Uptime For {self.bot.user.name} Is {self.bot.uptime}")
        embed.add_field(name=f"Bot User Creation Date And Time",value=f"{self.bot.user.name} Was Created {self.bot.user.created_at:%A %d %B %Y} And The Time Was {self.bot.user.created_at:%H:%M:%S %p}")
        embed.add_field(name=f"Important Information",value=f"Remember To :star: The [Repo](https://github.com/kyb3r/modmail) And Become A Patreon [Here](https://patreon.com/kyber)")
        embed.set_thumbnail(url=str(self.bot.user.avatar_url))
        embed.set_footer(text=f'If You Have Suggestions For More Stats, Please Use The Command "?suggestion" For More Info On How You Do It')
        embed.set_author(name=f"{self.bot.user.name} Stats")

        await ctx.send(embed=embed)
        
    @commands.command()
    @checks.has_permissions(PermissionLevel.ADMINISTRATOR)
    async def user(self, ctx, member: discord.Member = None):

        """Get A Cool Embed With Many Useful Stats About A User"""
		
        if member is None:
            member = ctx.author

        embed = discord.Embed(

            title=" ",

            color=discord.Color.blue(),

            description=f"**Here is the stats for {member.name}, enjoy them:**",

        )
        embed.add_field(name=f"User Creation Date And Time",value=f"{member.name} Was Created {member.created_at:%A %d %B %Y} And The Time Was {member.created_at:%H:%M:%S %p}")
        embed.add_field(name="User ID",value=f"The ID For {member.name} Is `{member.id}`")
        embed.add_field(name="Member Roles",value=f"{member.name} Has These Roles: {member.roles}")
        embed.add_field(name="Coming Soon",value=f"Coming Soon")
        embed.add_field(name="Coming Soon",value=f"Coming Soon")
        embed.add_field(name=f"Important Information",value=f"Remember To :star: The [Repo](https://github.com/kyb3r/modmail) And Become A Patreon [Here](https://patreon.com/kyber)")
        embed.set_thumbnail(url=str(member.avatar_url))
        embed.set_footer(text=f'If You Have Suggestions For More Stats, Please Use The Command "?suggestion" For More Info On How You Do It')
        embed.set_author(name=f"{member.name}'s Stats")

        await ctx.send(embed=embed)
        
def setup(bot):

    bot.add_cog(Stats(bot))
