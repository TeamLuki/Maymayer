from discord.ext import commands
import discord.utils
import sys

def is_owner_check(message):
    return message.author.id == 'Replace this with the bot owners id'

def is_owner():
    return commands.check(is_owner_check)

