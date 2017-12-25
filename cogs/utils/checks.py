from discord.ext import commands
import discord.utils
import sys

def is_owner_check(message):
    return message.author.id == 'Replace this with the bot owners id' #add or 'bot owner id' to this, replacing bot owner id with the id of another bot owner if you would like multiple bot owners.

def is_owner():
    return commands.check(lambda ctx: is_owner_check(ctx.message))

