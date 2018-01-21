import discord
from discord.ext import commands
from .utils import checks
import sys
import os.path
import inspect

class Admin():
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(name='eval', hidden=True)
    @checks.is_owner()
    async def _eval(self, ctx, *, code : str):
        """Evaluates code."""
        code = code.strip('` ')
        python = '```py\n{}\n```'
        result = None

        env = {
            'bot': self.bot,
            'ctx': ctx,
            'message': ctx.message,
            'guild': ctx.message.guild,
            'channel': ctx.message.channel,
            'author': ctx.message.author
        }

        env.update(globals())

        try:
            result = eval(code, env)
            if inspect.isawaitable(result):
                result = await result
        except Exception as e:
            await ctx.send(python.format(type(e).__name__ + ': ' + str(e)))
            return

        await ctx.send(python.format(result))
        
def setup(bot):
    bot.add_cog(Admin(bot))
