import discord
from discord.ext import commands
import asyncio

#credits to NanoBot for the prune command

class Moderation():
    def __init__(self, bot):
        self.bot = bot

    async def process_deletion(self, messages, channel):
        while messages:
            if len(messages) > 1:
                await channel.delete_messages(messages[:100])
                messages = messages[100:]
            else:
                await messages.delete()
                messages = []
            await asyncio.sleep(1.5)

    @commands.command()
    @commands.has_permissions(manage_messages = True)
    async def prune(self, ctx, number: int):
        """Deletes the specified number of messages."""

        if ctx.invoked_subcommand is None:
            channel = ctx.message.channel
            author = ctx.message.author
            server = author.guild
            is_bot = self.bot.user.bot
            has_permissions = channel.permissions_for(server.me).manage_messages

            to_delete = []

            if not has_permissions:
                await ctx.send("I am not able to delete messages.")
                return

            async for message in channel.history(limit=number+1):
                to_delete.append(message)

            await self.process_deletion(to_delete, ctx.message.channel)
            if number == 1:
                await ctx.send("**Successfully pruned 1 message.**")
                return
            else:
                await ctx.send("**Successfully pruned {} messages.**".format(number))
                return

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, username: discord.User):
        """Kicks a user."""
        await ctx.message.guild.kick(username)
        await ctx.send("**Successfully kicked " + str(username) + ".**")

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, username: discord.User):
        """Bans a user."""
        await ctx.message.guild.ban(username)
        await ctx.send("**Successfully banned " + str(username) + ".**")

def setup(bot):
    bot.add_cog(Moderation(bot))
