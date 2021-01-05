import discord
import random
import os

from discord.ext import commands, tasks
from itertools import cycle

intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)

client = commands.Bot(command_prefix = ".", intents = intents)
status = cycle(["bedwars with Scandlex", "Minecraft", "Anime SMP", "Hypixel", "with AcidicBlaster", "Skywars", "BlocksMC", "Competetive Cracked Bedwars"])
status_ = cycle(["Hentai", "Anime", "YouTube", "AcidicBlaster", "RayVene", "F1"])


@client.event
async def on_ready():
    await client.change_presence(status = discord.Status.idle, activity = discord.Activity(
        type = discord.ActivityType.watching, name = "Hentai"
    ))
    change_status.start()
    change_status_a.start()
    print("Winston is now Online.")

@tasks.loop(seconds = 10)
async def change_status():
    await client.change_presence(status = discord.Status.idle, activity = discord.Game(next(status)))
    
@tasks.loop(seconds = 10)
async def change_status_a():
    await client.change_presence(status = discord.Status.idle, activity = discord.Activity(type = discord.ActivityType.watching, name =(next(status_))))

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

@client.command()
@commands.has_permissions(manage_messages = True)
async def clear(ctx, amount : int):
    await ctx.channel.purge(limit = amount)
    await ctx.send(f"{amount} message's have been cleared!")

@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please specify a amount of messages to delete.")
    
@client.command()
@commands.has_permissions(kick_members = True, administrator = True)
async def kick(ctx, member : discord.Member, *, reason = None):
    await member.kick(reason = reason)
    await ctx.send(f"{member} has been kicked for {reason}.")

@kick.error
async def kick_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please specify a user.")

@client.command()
@commands.has_permissions(ban_members = True, administrator = True)
async def ban(ctx, member: discord.Member, *, reason = None):
    await member.ban(reason = reason)
    await ctx.send(f"{member} has been banned for {reason}.")

@ban.error
async def ban_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please specify a user.")

@client.command()
@commands.has_permissions(ban_members = True, administrator = True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split("#")

    for ban_entry in banned_users:
        user = ban_entry.user
        
        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f"{member_name}#{member_discriminator} has been unbanned.")
            return
        else:
            await ctx.send("User is not banned.")

@unban.error
async def unban_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please specify a user.")

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

