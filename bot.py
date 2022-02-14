# test bot
import os

import discord

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents().all()
intents.members = True

bot = commands.Bot(command_prefix='-', intents=intents)


@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))


@bot.command()
async def ping(ctx):
    await ctx.send("pong")

token = os.getenv('discord_token')
bot.run(token)