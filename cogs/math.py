import discord
from discord.ext import commands

class Math():
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def add(self, left : int, right : int):
        '''Adds 2 numbers together.'''
        await self.bot.say(left + right)

    @commands.command()
    async def subtract(self, left : int, right : int):
        '''Subtracts a number by another number.'''
        await self.bot.say(left - right)

    @commands.command()
    async def multiply(self, left : int, right : int):
        '''Multiplies a number by another number.'''
        await self.bot.say(left * right)

    @commands.command()
    async def divide(self, left : int, right : int):
        '''Divides a number by another number.'''
        await self.bot.say(left/right)

def setup(bot):
    bot.add_cog(Math(bot))
