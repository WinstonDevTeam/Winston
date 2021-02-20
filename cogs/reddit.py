from main import THEME
import discord
import asyncio
from discord.ext import commands
import praw
import random

reddit = praw.Reddit(client_id = "oqxjNa18tQU_mQ", client_secret = "QmkRGc5Vl1L1ocqWbQ_zsXqsP7S0LA", username = "PythonAPIBot", password = "chrisv23@minecraft", user_agent = "Winston")

class Reddit(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name = "meme")
    async def meme(self, ctx, *, subsred = "dankmemes"):
        subreddit = reddit.subreddit(subsred)
        all_subs = []

        top = subreddit.top(limit = 50)

        for submission in top:
            all_subs.append(submission)

        choice_sub = random.choice(all_subs)
        url = choice_sub.url

        if subreddit.over18 and not ctx.channel.is_nsfw():
            nsfw_url = "https://i.imgur.com/oe4iK5i.gif"
            embed = discord.Embed(title = "Channel is not marked as NSFW!", url = nsfw_url, color = discord.Color.dark_gray())
            await ctx.send(embed = embed)
            return

        embed = discord.Embed(title = f"{choice_sub.title}", url = f"https://www.reddit.com/{choice_sub.permalink}", color = discord.Color.dark_gray())
        embed.set_image(url = url)
        embed.set_footer(text = f"Post taken from r/{choice_sub.subreddit.display_name} made by u/{choice_sub.author}")
        await ctx.send(embed = embed)

def setup(client):
    client.add_cog(Reddit(client))