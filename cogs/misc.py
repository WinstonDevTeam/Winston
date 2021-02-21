import discord
import asyncio
from discord.ext import commands

class Misc(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name = "ping")
    async def ping(self, ctx):
        embed = discord.Embed(description = f"{self.client.latency}", color = discord.Color.dark_gray())
        await ctx.send(embed = embed)

    @commands.command(name = "userinfo", aliases = ["whois"])
    async def user(self, ctx, *, member : discord.Member = None):
        member = ctx.author if not member else member
        roles = [role for role in member.roles if role != ctx.guild.default_role]
        embed = discord.Embed(title = member.name, description = member.mention, color = discord.Color.dark_gray(), timestamp = ctx.message.created_at)
        embed.add_field(name = "ID:", value = member.id, inline = False)
        embed.add_field(name = "Joined Discord:", value = member.created_at.strftime("%a, %d %b %Y %I:%M %p"), inline = False)
        embed.add_field(name = "Joined Server:", value = member.joined_at.strftime("%a, %d %b %Y %I:%M %p"), inline = False)
        embed.add_field(name = "Roles:", value = " ".join([role.mention for role in roles]), inline = False)
        embed.add_field(name = "Bot:", value = member.bot, inline = False)

        embed.set_thumbnail(url = member.avatar_url)
        embed.set_footer(icon_url = ctx.author.avatar_url, text = f"Requested by {ctx.author.name}")
        await ctx.send(embed = embed)    

    @commands.command(name = "avatar", aliases = ["av"])
    async def avatar(self, ctx, member : discord.Member = None):
        member = ctx.author if not member else member
        embed = discord.Embed(title = f"{member}", color = discord.Color.dark_gray(), timestamp = ctx.message.created_at)
        embed.set_image(url = member.avatar_url)
        embed.set_footer(icon_url = ctx.author.avatar_url, text = f"Requested by {ctx.author.name}")
        await ctx.send(embed = embed)

    @commands.command(name = "guildinfo", aliases = ["serverinfo"])
    async def serverinfo(self, ctx):
        embed = discord.Embed(title = f"{ctx.guild.name} Server Information", description = ctx.guild.description, color = discord.Color.dark_gray(), timestamp = ctx.message.created_at)
        embed.add_field(name = "Owner:", value = ctx.guild.owner, inline = True)
        embed.add_field(name = "Server ID:", value = ctx.guild.id, inline = True)
        embed.add_field(name = "Region:", value = ctx.guild.region, inline = True)
        embed.add_field(name = "Total Members:", value = ctx.guild.member_count, inline = True)
        embed.set_thumbnail(url = ctx.guild.icon_url)
        await ctx.send(embed = embed)

def setup(client):
    client.add_cog(Misc(client))