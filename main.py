import os
import random
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
bot.remove_command('help')

jateObj = Jate()

# On bot run, log connection to discord
@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

# On jate command, bot prints current jate and jime in discord channel of command
# Example discord input: ?jate
@bot.command()
async def jate(ctx):
    jonny = isItJonny(ctx.author.name)
    if jonny[0]:
        await ctx.send(jonny[1])
    current_time = datetime.now()
    curJate = jateObj.getJate(current_time)
    # curJate is returned as [curJWeekday, curJWeek, curJDay, curJYear, curJMin, curJSec]
    await ctx.send("Today is " + curJate[0] + ", " + curJate[1] + "/" + curJate[2] + "/" + curJate[3] + " " + curJate[4] + ":" + curJate[5] + " IJ")

# On futureJate command, bot prints irl date specified and the corresponding jate and jime
# Time is optionally specified on input
# Example discord input: ?futureJate 6/7/24 18:30
# Example discord input: ?futureJate 6/7/2024
# Example discord input: ?futureJate 6/7/24
@bot.command()
async def futureJate(ctx, *, fDate: str):
    jonny = isItJonny(ctx.author.name)
    if jonny[0]:
        await ctx.send(jonny[1])
    fJate = jateObj.getJate(pd.to_datetime(fDate))
    # fJate is returned as [curJWeekday, curJWeek, curJDay, curJYear, curJMin, curJSec]
    await ctx.send("The date " + fDate + " is " + fJate[0] + ", " + fJate[1] + "/" + fJate[2] + "/" + fJate[3] + " " + fJate[4] + ":" + fJate[5] + " IJ on the Jalendar")

# Standard help command. Prints out all available commands
@bot.command()
async def help(ctx):
    jonny = isItJonny(ctx.author.name)
    if jonny[0]:
        await ctx.send(jonny[1])
    await ctx.send("""Welcome to the Jalendar! Valid commands include: 
    To print the current jate: `?jate`
    To print a specified jate: `?futureJate 11/6/24 11:15`
    To print this help message again: `?help`
                   """)

# Silly copy of help command. Prints a slightly different message
@bot.command()
async def jelp(ctx):
    jonny = isItJonny(ctx.author.name)
    if jonny[0]:
        await ctx.send(jonny[1])
    await ctx.send("""Welcome to the Jalendar! You found the hidden help message! Valid commands include: 
    To print the current jate: `?jate`
    To print a specified jate: `?futureJate 11/6/24 11:15`
    To print this help message again: `?help`
                   """)
    
# Checks if the author of a message is Jon. If it is, returns a random
# message lauding him
# Return: Array of [boolean, string]
def isItJonny(user):
    isJonny = False
    if user == "jflatley22":
        isJonny = True

    messageOptions = [
        "Hello benevolent overlord! \n",
        "Thank you for gracing us with your presence. \n",
        "It is a pleasure to interact with you today, Sir. \n",
        "It is an honor to serve you."
    ]

    retMessage = ""
    if isJonny:
        retMessage = random.choice (messageOptions)

    return [isJonny, retMessage]


bot.run(DISCORD_TOKEN)