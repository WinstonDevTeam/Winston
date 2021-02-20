import discord
import asyncio
from discord.ext import commands
from discord.ext.commands import bot
import random
import praw

class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name = "dice")
    async def roll(self, ctx):
        choices = [1, 2, 3 , 4, 5, 6]
        number = random.choice(choices)
        embed = discord.Embed(description = f"You have rolled {number}", color = discord.Color.dark_gray)
        await ctx.send(embed = embed)

    @commands.command(name = "poll")
    async def poll(self, ctx, *, msg):
        channel = ctx.channel
        try:
            op1, op2 = msg.split("or")
            txt = f"React with ✅ for {op1} and ❎ for {op2}"
        except:
            await channel.send("Correct Syntax: [Choice 1] or [Choice 2]")
            return

        embed = discord.Embed(title = " Poll", description = txt , color = discord.Color.dark_gray())
        message = await channel.send(embed = embed)
        await message.add_reaction("✅")
        await message.add_reaction("❎")
        await ctx.message.delete()



def setup(client):
    client.add_cog(Fun(client))
