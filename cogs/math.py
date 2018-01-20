import discord
from discord.ext import commands

class Math():
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def add(self, ctx, left : int, right : int):
        '''Adds 2 numbers together.'''
        await ctx.send(left + right)

    @commands.command()
    async def subtract(self, ctx, left : int, right : int):
        '''Subtracts a number by another number.'''
        await ctx.send(left - right)

    @commands.command()
    async def multiply(self, ctx, left : int, right : int):
        '''Multiplies a number by another number.'''
        await ctx.send(left * right)

    @commands.command()
    async def divide(self, ctx, left : int, right : int):
        '''Divides a number by another number.'''
        await ctx.send(left/right)

def setup(bot):
    bot.add_cog(Math(bot))
