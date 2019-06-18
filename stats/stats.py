import discord
from discord.ext import commands
from core import checks
from core.models import PermissionLevel

#Cog = getattr(commands, 'Cog', object)

class Stats(commands.Cog):

    """Get useful stats directly in an embed about either the ModMail bot, a user or the server."""

    

    def __init__(self, bot):

        self.bot = bot
  
    @commands.group(name="stats", aliases=["stat"], invoke_without_command=True)
    @checks.has_permissions(PermissionLevel.ADMINISTRATOR)
    async def stats(self, ctx):
        """Get a cool embed with a lot of cool stats about your ModMail, server or a user"""

        await ctx.send_help(ctx.command)
        
   
    @stats.command(name="server")
    @checks.has_permissions(PermissionLevel.ADMINISTRATOR)
    async def server(self, ctx):
        """Get a cool embed with many useful stats about your server"""


        embed = discord.Embed(

            color=discord.Color.blue(),

            description=f"**Here are the stats for {ctx.guild.name}, enjoy them:**",

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
          if m.status != discord.Status.offline:
             online += 1
          else:
             continue
                
        embed.add_field(name=f"Member Count",value=f"There are {ctx.guild.member_count} members in {ctx.guild.name}, {humans} of them are humans, {bots} of them are bots and {online} members are online")
        embed.add_field(name="Guild ID",value=f"The ID for {ctx.guild.name} is `{ctx.guild.id}`")
        embed.add_field(name="Text Channel Count",value=f"There are {len(ctx.guild.text_channels)} text channels in {ctx.guild.name}")
        embed.add_field(name="Voice Channel Count",value=f"There are {len(ctx.guild.voice_channels)} voice channels in {ctx.guild.name}")
        embed.add_field(name="Role Count",value=f"There are {len(ctx.guild.roles)} roles in {ctx.guild.name}")
        embed.add_field(name="Category Count",value=f"There are {len(ctx.guild.categories)} categories in {ctx.guild.name}")
        embed.add_field(name="Server Region",value=f"The region of {ctx.guild.name} is {ctx.guild.region}")
        embed.add_field(name=f"Server Owner",value=f"The owner of {ctx.guild.name} is {ctx.guild.owner.mention}")
        embed.add_field(name=f"Server Creation Date And Time",value=f"{ctx.guild.name} was created {ctx.guild.created_at:%A %d %B %Y} and the time was {ctx.guild.created_at:%H:%M:%S %p}")
        embed.add_field(name=f"Important Information",value=f"Remember to :star: the [repo](https://github.com/kyb3r/modmail) and become a patreon [here](https://patreon.com/kyber)")
        embed.set_thumbnail(url=str(ctx.guild.icon_url))
        embed.set_footer(text=f'If you have suggestions for more stats, please use the command "?stat info" for more info on how you do it')
        embed.set_author(name=f"{ctx.guild.name} stats")

        await ctx.send(embed=embed)
        
    @stats.command(name="bot")
    @checks.has_permissions(PermissionLevel.ADMINISTRATOR)
    async def bot(self, ctx):

        """Get A Neat Embed With Many Useful Stats About Your ModMail Bot."""

        embed = discord.Embed(

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

        """Sends All Stats Embeds At Once"""

        await ctx.invoke(self.bot.get_command("stats bot"))
        await ctx.invoke(self.bot.get_command(f'stats server'))
        await ctx.invoke(self.bot.get_command("stats user"))
        
	
    @stats.command(name="user")
    @checks.has_permissions(PermissionLevel.ADMINISTRATOR)
    async def user(self, ctx, member: discord.Member = None):

        """Get A Cool Embed With Many Useful Stats About A User"""
		
        if member is None:
            member = ctx.author

        embed = discord.Embed(

            color=discord.Color.blue(),

            description=f"**Here is the stats for {member.name}, enjoy them:**",

        )
	
        roles = ""
        for r in ctx.author.roles:
            if r.name != "@everyone":
               roles += f"{r.mention} "

        embed.add_field(name=f"User Creation Date And Time",value=f"{member.name} Was Created {member.created_at:%A %d %B %Y} And The Time Was {member.created_at:%H:%M:%S %p}")
        embed.add_field(name="User ID",value=f"The ID For {member.name} Is `{member.id}`")
        embed.add_field(name="User Roles",value=f"{member.name} has these roles: {roles}")
        embed.add_field(name=f"User Join Date And Time",value=f"{member.name} Joined The Server {member.joined_at:%A %d %B %Y} And The Time Was {member.joined_at:%H:%M:%S %p}")
        embed.add_field(name="User Status",value=f"The Status For {member.name} Is {member.status}")
        embed.add_field(name=f"Important Information",value=f"Remember To :star: The [Repo](https://github.com/kyb3r/modmail) And Become A Patreon [Here](https://patreon.com/kyber)")
        embed.set_thumbnail(url=str(member.avatar_url))
        embed.set_footer(text=f'If You Have Suggestions For More Stats, Please Use The Command "?suggestion" For More Info On How You Do It')
        embed.set_author(name=f"{member.name}'s Stats")

        await ctx.send(embed=embed)
        
def setup(bot):

    bot.add_cog(Stats(bot))
