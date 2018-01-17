from discord.ext import commands
import discord.utils
import sys

owners = [replace this text with your ID]

def is_owner_check(ctx):
    return ctx.message.author.id in owners

def is_owner():
    return commands.check(is_owner_check)
