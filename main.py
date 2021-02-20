from re import M, S
import discord
import random
import os
import asyncio
from discord.enums import ActivityType
from discord.ext.commands import bot
import praw
from dotenv import load_dotenv

from discord.ext import commands, tasks
from itertools import cycle

#Loading .env
load_dotenv('.env')

#Intents

intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)
client = commands.Bot(command_prefix = "/", case_insensitive = True, intents = intents)

#Status Loop

server_count = len(client.guilds)
status_a = cycle(["bedwars with Scandlex", "Minecraft", "Survival", "Skywars",])
status_b = cycle(["Anime", "YouTube", "F1"])

async def status():
    while True:
        await client.wait_until_ready()
        await client.change_presence(status = discord.Status.idle, activity = discord.Game(next(status_a)))
        await asyncio.sleep(10)
        await client.change_presence(status = discord.Status.idle, activity = discord.Activity(type = discord.ActivityType.watching, name =(next(status_b))))
        await asyncio.sleep(10)
        await client.change_presence(status = discord.Status.idle, activity = discord.Activity(type = discord.ActivityType.listening, name = "/help"))
        await asyncio.sleep(10)

supporters = [773893391485370378, 400355889187389450, 400857098121904149, 635019218991054848, 254219520980287489, 733532987794128897]
TOKEN = "NzkyNjcxNDkwMTUxNjc3OTYy.X-hG2g.G-kNm4-KVo9b-Z9alw1OjeNKeD4"
THEME = discord.Color.dark_gray()

@client.event
async def on_ready():
    print("Winston is now Online.")
client.loop.create_task(status())

#Logging

@client.event
async def on_guild_join(guild):
    log_channel = client.get_channel(796677487823945728)
    await log_channel.send(f"Winston joined {guild}.\nOwner: {guild.owner}")

@client.event
async def on_guild_remove(guild):
    log_channel = client.get_channel(796677487823945728)
    await log_channel.send(f"Winston left **{guild}**.\nOwner: **{guild.owner}**\nOwner ID: **{guild.owner.id}**")

@client.command(name = "invite")
async def invite(ctx):
    invite_url = "https://discord.com/api/oauth2/authorize?client_id=792671490151677962&permissions=8&scope=bot"
    embed = discord.Embed(
        title = "Click here to invite Winston!", url = invite_url, color = THEME)
    await ctx.send(embed = embed)

@client.command(name = "support")
async def support(ctx):
    await ctx.send("Support Server:\nhttps://discord.gg/ASw7eUBssP")

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")
        print(f"{filename} has loaded.")

client.run(os.getenv('TOKEN'))
