import discord
from discord.ext import commands

import json
import os

if os.path.exists(os.getcwd() + "/config.json"):
    with open("./config.json") as f:
        configData = json.load(f)

else:
    configTemplate = {"Token": "", "Prefix": "Z"}

    with open(os.getcwd() + "/config.json", "w+") as f:
        json.dump(configTemplate, f)

token = configData["Token"]
prefix = configData["Prefix"]

bot = commands.Bot(command_prefix="Z")

@bot.event
async def on_ready():
    print("ZAlpha ready!")
    await bot.change_presence(activity=discord.Game(name="League of Developers|Zhelp"))

@bot.command(name="ping")
async def ping(ctx):
    await ctx.send(f"Pong {round(bot.latency*1000, 1)} ms!")

bot.run(token)