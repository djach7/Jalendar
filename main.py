# bot.py
import os
import discord
from dotenv import load_dotenv
from discord.ext import commands, tasks
from datetime import datetime
from jate import Jate

load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='?', intents=intents)

current_time = datetime.now()

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    updateTime.start()

@tasks.loop(seconds = 30)
async def updateTime():
    current_time = datetime.now()

@bot.command()
async def jate(ctx):
    jate = Jate()
    current_time = datetime.now()
    await ctx.send("Today's jate is " + jate.getJate(current_time))



bot.run(DISCORD_TOKEN)