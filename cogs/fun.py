from bot import bot
from random import choice
import discord
from discord.ext.commands import Cog
from discord.ext.commands import command
from discord.ext import commands

class Fun(Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="ping")
    async def fun(self, ctx):
        await ctx.send(f"Pong {round(bot.latency*1000, 1)} ms!")   

    @commands.command(name="hi", aliases=["hello", "sup"])
    async def hi(self, ctx):
        await ctx.send(f"{choice(('Hello', 'Hi', 'Hey', 'Hiya', 'Sup', 'Ciao', '<:peepohey:806962515152994406>'))} {ctx.author.mention}!")

    @commands.Cog.listener()
    async def on_ready(self):
        print("ZAlpha initiated.")

def setup(bot):
    bot.add_cog(Fun(bot))