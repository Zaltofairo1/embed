from re import search
import re
import aiohttp
import discord
from discord import channel
from discord import message
from discord.flags import Intents
from dotenv import load_dotenv
import os
import os.path
import random as rnd
from discord.ext import commands

bot = commands.Bot(command_prefix='€')

api_giphy = "https://api.giphy.com/v1/gifs/random?api_key=2GDNydq1IMOCd86RihgZ15AQnl78nz31&tag=rating=g"
api_search_giphy = "https://api.giphy.com/v1/gifs/search?api_key=2GDNydq1IMOCd86RihgZ15AQnl78nz31&limit=25&offset=0&rating=g&lang=en&q="

load_dotenv()
TOKEN = os.getenv("TOKEN_DS")
GUILD = int(os.getenv("GUILD_DS"))




@bot.command()
async def random(ctx):
    async with aiohttp.ClientSession() as session:
        async with session.get(api_giphy) as response:
             if response.status == 200:
                js = await response.json()
                await ctx.send(js["data"]["images"]["original"]["url"])

@bot.command()
async def search(ctx, title):
    busqueda = api_search_giphy+title
    async with aiohttp.ClientSession() as session:
        async with session.get(busqueda) as response:
            if response.status == 200:
                js = await response.json()
                await ctx.send(rnd.choice(js["data"]) ["images"]["original"]["url"])


bot.run(TOKEN)