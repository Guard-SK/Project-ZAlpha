import discord
from discord.ext import commands

import json
import os
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from discord.ext.commands import Bot as BotBase
from discord.ext.commands.core import has_permissions

### Taking token from json file ###

# if os.path.exists(os.getcwd() + "/config.json"):
#     with open("./config.json") as f:
#         configData = json.load(f)

# else:
#     configTemplate = {"Token": "", "Prefix": "Z"}

#     with open(os.getcwd() + "/config.json", "w+") as f:
#         json.dump(configTemplate, f)

# token = configData["Token"]
# prefix = configData["Prefix"]

bot = commands.Bot(command_prefix="Z")

OWNER_IDS = [544573811899629568]
COGS = [path[:-3] for path in os.listdir('./cogs') if path[-3:] == '.py']

@bot.command()
async def load(ctx, extension):
    bot.load_extension(f"cogs.{extension}")
    await ctx.send("Cog(s) loaded.")

@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f"cogs.{extension}")
    await ctx.send("Cog(s) unloaded.")


for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f"cogs.{filename[:-3]}")


@bot.event
async def on_ready():
    print("ZAlpha ready!")
    await bot.change_presence(activity=discord.Game(name="League of Developers|Zhelp"))

bot.run("os.environ['DISCORD_TOKEN']") #taking token from Heroku os.environ['DISCORD_TOKEN']