import discord
import asyncio
from discord.ext import commands
from discord.ext.commands import bot
import random
import praw

reddit = praw.Reddit(client_id = "oqxjNa18tQU_mQ", client_secret = "QmkRGc5Vl1L1ocqWbQ_zsXqsP7S0LA", username = "PythonAPIBot", password = "chrisv23@minecraft", user_agent = "Winston")

class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name = "dice")
    async def roll(self, ctx):
        choices = [1, 2, 3 , 4, 5, 6]
        number = random.choice(choices)
        embed = discord.Embed(name = "Dice", description = f"You have rolled {number}", color = discord.Color.dark_gray())
        await ctx.send(embed = embed)

    @commands.command(name = "meme")
    async def meme(self, ctx, subsred = "dankmemes"):
        subreddit = reddit.subreddit(subsred)
        all_subs = []

        top = subreddit.top(limit = 50)

        for submission in top:
            all_subs.append(submission)

        choice_sub = random.choice(all_subs)
        
        name = choice_sub.title
        url = choice_sub.url

        embed = discord.Embed(name = name)
        embed.set_image(url = url)

        await ctx.send(embed = embed)




def setup(client):
    client.add_cog(Fun(client))
    
