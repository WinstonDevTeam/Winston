import discord
import random
import os
import asyncio

from discord.ext import commands, tasks
from itertools import cycle\

#Intents

intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)
client = commands.Bot(command_prefix = ".", intents = intents)

status_a = cycle(["bedwars with Scandlex", "Minecraft", "Anime SMP", "Hypixel", "with AcidicBlaster", "Skywars", "BlocksMC", "Competetive Cracked Bedwars"])
status_b = cycle(["Hentai", "Anime", "YouTube", "AcidicBlaster", "RayVene", "F1"])

#Changing Statuses

async def status():
    while True:
        await client.wait_until_ready()
        await client.change_presence(status = discord.Status.idle, activity = discord.Game(next(status_a)))
        await asyncio.sleep(10)
        await client.change_presence(status = discord.Status.idle, activity = discord.Activity(type = discord.ActivityType.watching, name =(next(status_b))))
        await asyncio.sleep(10)

@client.event
async def on_ready():
    print("Winston is now Online.")
client.loop.create_task(status())

#Errors

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
       await ctx.send("Invalid Command. Please try again.")
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You don't have permission to run this command.") 

#Logging

@client.event
async def on_member_join(ctx, member):
    log_channel = client.get_channel("796677487823945728")
    await log_channel.send("{member} has joined a server.")

@client.event
async def on_member_remove(ctx, member):
    log_channel = client.get_channel("796677487823945728")
    await log_channel.send("{member} has joined a server.")

#Commands

@client.command()
async def ping(ctx):
    await ctx.send(f"Pong!\n\nThe Latency is {round(client.latency * 1000)}ms.")

@client.command(aliases = ["dice"])
async def roll(ctx):
    choices = [1, 2, 3 , 4, 5, 6]
    number = random.choice(choices)
    await ctx.send(f"The number is {number}.")

#Loading Cogs

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")
        print(f"{filename} has loaded.")

client.run("NzkyNjcxNDkwMTUxNjc3OTYy.X-hG2g.HUyrILSMzZVY1IDIqHetw8ecj-w")

