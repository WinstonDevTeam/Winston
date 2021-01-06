import discord
import random
import os
import asyncio

from discord.ext import commands, tasks
from itertools import cycle

intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)

client = commands.Bot(command_prefix = ".", intents = intents)
status_a = cycle(["bedwars with Scandlex", "Minecraft", "Anime SMP", "Hypixel", "with AcidicBlaster", "Skywars", "BlocksMC", "Competetive Cracked Bedwars"])
status_b = cycle(["Hentai", "Anime", "YouTube", "AcidicBlaster", "RayVene", "F1"])

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

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
       await ctx.send("Invalid Command. Please try again.")
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You don't have permission to run this command.") 

@client.event
async def on_member_join(member):
    print(f"{member} has joined a server.")

@client.event
async def on_member_remove(member):
    print(f"{member} has left a server.")

@client.command()
async def ping(ctx):
    await ctx.send(f"Pong!\n\nThe Latency is {round(client.latency * 1000)}ms.")

@client.command(aliases = ["dice"])
async def roll(ctx):
    choices = [1, 2, 3 , 4, 5, 6]
    number = random.choice(choices)
    await ctx.send(f"The number is {number}.")

#Cogs 

@client.command()
async def load(ctx, extension):
    client.load_extension(f"cogs.{extension}.")

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f"cogs.{extension}.")

for filename in os.listdir("./cogs"):
    if filename.endswith('.py'):
        client.load_extension(f"cogs.{filename[:-3]}")

@client.command()
async def spam(ctx, amount, *, message):
    await ctx.send(f"{message * int(amount)}")

@spam.error
async def spam_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please specify required arguments.")
    

client.run("NzkyNjcxNDkwMTUxNjc3OTYy.X-hG2g.HUyrILSMzZVY1IDIqHetw8ecj-w")
