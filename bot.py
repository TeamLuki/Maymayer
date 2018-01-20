###################################################################
# Maymayer - A Discord bot made by DreamLive Inc. (mostly Kaniel) #
# I have no life. I have no life. I have no life. I have no life. #
###################################################################

from discord.ext import commands
import discord
import asyncio
import datetime
#get rid of the following 6 lines if you don't want stuff to be logged
import logging
import sys
import os
import aiohttp
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

with open("token.txt","r") as tokenfile:
    token = tokenfile.read().replace('\n','')
description = '''Maymayer - Hip with the kiddest discord bot created by Luki and maintained by TheLBall.'''
startup_extensions = ["cogs.general", "cogs.fun", "cogs.mod", "cogs.math"]
bot = commands.AutoShardedBot(command_prefix=['meme ', 'm!'], description=description)

if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Oops, I lost extension {}\n{}. But I had an antivirus!'.format(extension, exc))

@bot.event
async def on_ready():
    await bot.change_presence(game=discord.Game(name='m!help • https://discord.gg/GzNH2sB'.format(len(bot.guilds))))
    print('Maymayer has successfully logged in.')
    
bot.run(token, bot=True, reconnect=True)
