from re import M, S
import discord
import random
import os
import asyncio
from discord.enums import ActivityType
from discord.ext.commands import bot
import praw

from discord.ext import commands, tasks
from itertools import cycle

#Intents

intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)
client = commands.Bot(command_prefix = "/", case_insensitive = True, intents = intents)

#Status Loop

server_count = len(client.guilds)
status_a = cycle(["bedwars with Scandlex", "Minecraft", "Survival", "Skywars",])
status_b = cycle(["Anime", "YouTube", "F1"])

#Changing Statuses

async def status():
    while True:
        await client.wait_until_ready()
        await client.change_presence(status = discord.Status.idle, activity = discord.Game(next(status_a)))
        await asyncio.sleep(10)
        await client.change_presence(status = discord.Status.idle, activity = discord.Activity(type = discord.ActivityType.watching, name =(next(status_b))))
        await asyncio.sleep(10)
        await client.change_presence(status = discord.Status.idle, activity = discord.Activity(type = discord.ActivityType.listening, name = "/help"))
        await asyncio.sleep(10)

@client.event
async def on_ready():
    print("Winston is now Online.")
client.loop.create_task(status())

supporters = [773893391485370378, 400355889187389450, 400857098121904149, 635019218991054848, 254219520980287489, 733532987794128897]

#Errors

#Logging

@client.event
async def on_guild_join(guild):
    log_channel = client.get_channel(796677487823945728)
    await log_channel.send(f"Winston joined {guild}.\nOwner: {guild.owner}")

@client.event
async def on_guild_remove(guild):
    log_channel = client.get_channel(796677487823945728)
    await log_channel.send(f"Winston left {guild}.\nOwner: {guild.owner}\nOwner ID: {guild.owner.id}")

#Commands

@client.command(name = "ping")
async def ping(ctx):
    embed = discord.Embed(name = "Ping", description = f"The Latency is {round(client.latency * 1000)}ms!", color = discord.Color.dark_gray())
    await ctx.send(embed = embed)

@client.command(name = "userinfo", aliases = ["whois"])
async def user(ctx, *, member : discord.Member = None):
    member = ctx.author if not member else member
    roles = [role for role in member.roles if role != ctx.guild.default_role]
    embed = discord.Embed(name = member.name, description = member.mention, color = discord.Color.dark_gray(), timestamp = ctx.message.created_at)
    embed.add_field(name = "ID:", value = member.id, inline = False)
    embed.add_field(name = "Joined Discord:", value = member.created_at.strftime("%a, %d %b %Y %I:%M %p"), inline = False)
    embed.add_field(name = "Joined Server:", value = member.joined_at.strftime("%a, %d %b %Y %I:%M %p"), inline = False)
    embed.add_field(name = "Roles:", value = " ".join([role.mention for role in roles]), inline = False)
    embed.add_field(name = "Bot:", value = member.bot, inline = False)

    embed.set_thumbnail(url = member.avatar_url)
    embed.set_footer(icon_url = ctx.author.avatar_url, text = f"Requested by {ctx.author.name}")
    await ctx.send(embed = embed)

@client.command(name = "avatar", aliases = ["av"])
async def avatar(ctx, member : discord.Member = None):
    member = ctx.author if not member else member
    embed = discord.Embed(title = f"{member}", color = discord.Color.dark_gray(), timestamp = ctx.message.created_at)
    embed.set_image(url = member.avatar_url)
    embed.set_footer(icon_url = ctx.author.avatar_url, text = f"Requested by {ctx.author.name}")
    await ctx.send(embed = embed)

@client.command(name = "serverinfo", aliases = ["guildinfo"])
async def serverinfo(ctx):
    embed = discord.Embed(title = f"{ctx.guild.name} Server Information", description = ctx.guild.description, color = discord.Color.dark_gray(), timestamp = ctx.message.created_at)
    embed.add_field(name = "Owner:", value = ctx.guild.owner, inline = True)
    embed.add_field(name = "Server ID:", value = ctx.guild.id, inline = True)
    embed.add_field(name = "Region:", value = ctx.guild.region, inline = True)
    embed.add_field(name = "Total Members:", value = ctx.guild.member_count, inline = True)
    
    embed.set_thumbnail(url = ctx.guild.icon_url)
    embed.set_footer(icon_url = ctx.author.avatar_url, text = f"Requested by {ctx.author.name}")
    await ctx.send(embed = embed)

@client.command(name = "invite")
async def invite(ctx):
    invite_url = "https://discord.com/api/oauth2/authorize?client_id=792671490151677962&permissions=8&scope=bot"
    embed = discord.Embed(
        title = "Click here to invite Winston!", url = invite_url, color = discord.Color.dark_gray())
    await ctx.send(embed = embed)

@client.command(name = "support")
async def support(ctx):
    await ctx.send("Support Server:\nhttps://discord.gg/Cy8UA5va")
    
#Import cog

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")
        print(f"{filename} has loaded.")

client.run("NzkyNjcxNDkwMTUxNjc3OTYy.X-hG2g.G-kNm4-KVo9b-Z9alw1OjeNKeD4")
