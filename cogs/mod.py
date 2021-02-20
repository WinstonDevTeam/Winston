import discord
import asyncio
import typing
from discord.ext import commands
from discord import utils

class Moderator(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name = "clear")
    @commands.has_guild_permissions(manage_messages = True)
    async def clear(self, ctx, amount : int):
        if amount == None:
            await ctx.send("Please specify a amount of messages to be deleted!")
        await ctx.channel.purge(limit = amount)
        await ctx.send(f"{amount} message('s) have been cleared!", delete_after = 3)

    @commands.command(name = "kick")
    @commands.has_guild_permissions(kick_members = True)
    async def kick(self, ctx, member : discord.Member, *, reason = None):
        if member == None or reason == None:
            await ctx.send("Insufficient arguments!")
        elif ctx.author.top_role.position <= member.top_role.position:
            await ctx.send("You cannot kick this user because their role is higher than or equal to yours!")
        else:
            await member.kick(reason = reason)
        if reason:
            await ctx.send(f"**{member}** has been kicked for **{reason}**.")
        else:
            await ctx.send("**{member}** has been kicked.")

    @commands.command(name = "ban")
    @commands.has_guild_permissions(ban_members = True)
    async def ban(self, ctx, member: typing.Union[discord.Member, int], *, reason = None):
        if member == None:
            await ctx.send("Insufficient arguments!")
        if not isinstance(member, int):
            if ctx.author.top_role.position <= member.top_role.position and ctx.guild.owner.id != ctx.author.id:
                await ctx.send("You cannot ban this user because their role is higher than or equal to yours!"
                )
                return
            
        if isinstance(member, int):
            member_str = f"<@{member}>"
            member = discord.Object(id = member)

        else:
            member_str = member

        try:
            await member.send(f"You have been banned from **{ctx.guild}** by **{ctx.author}**\nReason: **{reason}**"
            )
        except Exception:
            pass
        
        await ctx.guild.ban(member, reason = reason)
        
        if reason:
            await ctx.send(f"**{member_str}** has been banned for **{reason}**.")
        else:
            await ctx.send(f"**{member_str}** has been banned.")

    @commands.command(name = "unban")
    @commands.has_guild_permissions(ban_members = True)
    @commands.guild_only()
    async def unban(self, ctx, member : typing.Union[discord.Member, int, str], *, reason = None):
    
        if isinstance(member, int):
            member_str = f"<@{member}>"
            member = discord.Object(id = member)
        else:
            member_str = member

        if isinstance(member, str):
            banned_members = await ctx.guild.bans()
            member_name, member_tag = member.split("#")

            banned_member = utils.get(banned_members,member_name = member_name, member_discriminator = member_tag)

            if banned_member is None:
                await ctx.send("This member is not banned!")
                return
            await ctx.guild.unban(banned_member.user)

        else:
            await ctx.guild.unban(member)

        await ctx.send(f"Unbanned **{member_str}**")

    @commands.command(name = "mute")
    @commands.has_guild_permissions(manage_messages = True)
    async def mute(self, ctx, member : discord.Member, *, reason = None):
        guild = ctx.guild
        mutedRole = discord.utils.get(guild.roles, name = "Muted")

        if not mutedRole:
            mutedRole = await guild.create_role(name = "Muted")
            await ctx.send("Muted role not found. Creating one now....")

            for channel in guild.channels:
                await channel.set_permissions(mutedRole, speak = False, send_messages = False)

        await member.add_roles(mutedRole, reason = None)
        if reason == None:
            await ctx.send(f"**{member}** has been muted.")
            await member.send(f"You have been muted in **{guild.name}**.")
            
        else:
            await ctx.send(f"**{member}** has been muted for Reason: **{reason}**")
            await member.send(f"You have been muted in **{guild.name}**.\nReason: **{reason}**")

    @commands.command(name = "unmute")
    async def unmute(self, ctx, member : discord.Member):
        guild = ctx.guild
        mutedRole = discord.utils.get(guild.roles, name = "Muted")

        await member.remove_roles(mutedRole)
        await ctx.send(f"**{member}** has been unmuted.")
        await member.send(f"You have been unmuted from **{guild}**.")

    
   


def setup(client):
    client.add_cog(Moderator(client))
