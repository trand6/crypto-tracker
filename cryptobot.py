import os

import discord
import pandas as pd

from discord.ext import commands
from pycoingecko import CoinGeckoAPI
from dotenv import load_dotenv

load_dotenv()
cg = CoinGeckoAPI()
intents = discord.Intents().all()
intents.members = True

bot = commands.Bot(command_prefix='-', intents=intents)


@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))


@bot.command()
async def ping(ctx):
    
    data =cg.get_exchanges_list()
    df =pd.DataFrame(data, columns=['name', 'trust_score','trust_score_rank'])
    df.set_index('name',inplace=True)
    ranking = df.head(25)
    await ctx.send(ranking)


token = os.getenv('discord_token')
bot.run(token)