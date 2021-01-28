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
    async def meme(self, ctx, *, subsred = "dankmemes"):
        subreddit = reddit.subreddit(subsred)
        all_subs = []

        top = subreddit.top(limit = 50)

        for submission in top:
            all_subs.append(submission)

        choice_sub = random.choice(all_subs)
        url = choice_sub.url

        embed = discord.Embed(title = f"{choice_sub.title}", color = discord.Color.dark_gray())
        embed.set_image(url = url)
        embed.set_footer(text = f"Taken from {subsred}")
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

        embed = discord.Embed(title = " Poll", description = txt , color = discord.Color.dark_dray())
        message = await ctx.send(embed = embed)
        await message.add_reaction("✅")
        await message.add_reaction("❎")
        await ctx.message.delete()



def setup(client):
    client.add_cog(Fun(client))
    
