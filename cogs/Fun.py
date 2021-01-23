import discord
import asyncio
from discord.ext import commands
from discord.ext.commands import bot
import random

class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name = "dice")
    async def roll(self, ctx):
        choices = [1, 2, 3 , 4, 5, 6]
        number = random.choice(choices)
        embed = discord.Embed(name = "Dice", description = f"You have rolled {number}", color = discord.Color.dark_gray())
        await ctx.send(embed = embed)


def setup(client):
    client.add_cog(Fun(client))
    