import os
import discord
from dotenv import load_dotenv
from discord.ext import commands, tasks
from datetime import datetime
from jate import Jate
import pandas as pd

###
### Welcome to the Jalendar Bot. This bot converts normal dates and times into
### their corresponding Jates and Jimes according to the Jon Calendar (Jalender).
### Please use responsibly, enjoy!
###

load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='?', intents=intents)

jateObj = Jate()

# On bot run, log connection to discord
@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

# On jate command, bot prints current jate and jime in discord channel of command
# Example discord input: ?jate
@bot.command()
async def jate(ctx):
    current_time = datetime.now()
    curJate = jateObj.getJate(current_time)
    await ctx.send("Today's jate is " + curJate[0] + "/" + curJate[1] + " " + curJate[2] + ":" + curJate[3] + " IJ")

# On futureJate command, bot prints irl date specified and the corresponding jate and jime
# Time is optionally specified on input
# Example discord input: ?futureJate 6/7/24 18:30
# Example discord input: ?futureJate 6/7/2024
# Example discord input: ?futureJate 6/7/24
@bot.command()
async def futureJate(ctx, *, fDate: str):
    fJate = jateObj.getJate(pd.to_datetime(fDate))
    await ctx.send("The date " + fDate + " is " + fJate[0] + "/" + fJate[1] + " " + fJate[2] + ":00 IJ on the Jalendar")


bot.run(DISCORD_TOKEN)