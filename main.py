import os
import discord
from dotenv import load_dotenv
from discord.ext import commands, tasks
from datetime import datetime
from jate import Jate
import pandas as pd

load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='?', intents=intents)

jateObj = Jate()

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.command()
async def jate(ctx):
    current_time = datetime.now()
    curJate = jateObj.getJate(current_time)
    await ctx.send("Today's jate is " + curJate[0] + "/" + curJate[1] + " " + curJate[2] + ":" + curJate[3] + " IJ")

@bot.command()
async def futureJate(ctx, *, fDate: str):
    fJate = jateObj.getJate(pd.to_datetime(fDate))
    await ctx.send("The date " + fDate + " is " + fJate[0] + "/" + fJate[1] + " " + fJate[2] + ":00 IJ on the Jalendar")


bot.run(DISCORD_TOKEN)