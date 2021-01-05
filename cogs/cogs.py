import discord
from discord.ext import commands

#Cogs

class cogs(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def hello(self, ctx):
        await ctx.send(f"Hello")


def setup(client):
    client.add_cog(cogs(client))