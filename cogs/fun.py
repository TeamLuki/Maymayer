import discord
from discord.ext import commands
import random
import urllib
import urllib.request

#credits to NanoBot for the dog and cat commands

class Fun():
    def __init__(self, bot):
        self.bot = bot

    def getdog():
        dog = urllib.request.urlopen('https://random.dog/woof')
        dog = str(dog.read())
        dog = dog[2:]
        dog = dog[:len(dog) - 1]
        return dog

    def getcat():
        cat = urllib.request.urlopen('https://random.cat/meow')
        cat = str(cat.read())
        cat = cat[11:]
        cat = cat[:len(cat) - 3]
        cat = cat.replace("\\", "")
        return cat

    @commands.command()
    async def dog(self, ctx):
        """Gets a random dog from http://random.dog"""
        color = discord.Color.default()
        if ctx.message.guild is not None:
            color = ctx.message.guild.me.color
        embed = discord.Embed(color=color)
        embed.title = "Random Dog"

        dog = "null"
        while 1:
            dog = Fun.getdog()
            if not dog.endswith(".mp4"):
                break
        embed.set_footer(text="{}".format("http://random.dog/" + str(dog)))
        embed.set_image(url="http://random.dog/" + str(dog))
        await ctx.send(embed=embed)

    @commands.command()
    async def cat(self, ctx):
        """Gets a random cat from http://random.cat"""
        color = discord.Color.default()
        if ctx.message.guild is not None:
            color = ctx.message.guild.me.color
        embed = discord.Embed(color=color)
        embed.title = "Random Cat"
        cat = "null"
        while 1:
            cat = Fun.getcat()
            if not cat.endswith(".mp4"):
                break
        embed.set_footer(text="{}".format(str(cat)))
        embed.set_image(url=str(cat))
        await ctx.send(embed=embed)

    @commands.command()
    async def bestconsole(self, ctx):
        '''Tells you the best console.'''
        await ctx.send("**The PS Triple is the best console.**")

    @commands.command()
    async def kill(self, ctx, username: discord.User):
        '''Don't tell the government.'''
        await ctx.send("**I have successfully murdered " + str(username) + ".**")


def setup(bot):
    bot.add_cog(Fun(bot))
