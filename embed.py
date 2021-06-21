from re import search
import re
import aiohttp
from attr import dataclass
import discord
from discord import channel
from discord import message
from discord.flags import Intents
from dotenv import load_dotenv
import os
import os.path
import random as rnd
from discord.ext import commands
from yarl import URL

bot = commands.Bot(command_prefix='€')

load_dotenv()
TOKEN = os.getenv("TOKEN_DS")
GUILD = int(os.getenv("GUILD_DS"))
api_key = os.getenv("GIPHY_API_KEY")



async def random_gif(tag):
    api_giphy = (
        f"https://api.giphy.com/v1/gifs/random?api_key=2GDNydq1IMOCd86RihgZ15AQnl78nz31&tag={tag}&rating=g")
    async with aiohttp.ClientSession() as session:
        async with session.get(api_giphy) as response:
            if response.status == 200:
                js = await response.json()
                return js["data"]
        return None



@bot.command()
async def random(ctx , tag : str = ""):
    data = await random_gif(tag)
    await ctx.send(data["images"]["downsized"]["url"])


@bot.command()
async def embed(ctx , tag : str = ""):
    data = await random_gif(tag)
    embed = discord.Embed()
    embed.set_image(url=data["images"]["downsized"]["url"])
    embed.add_field (name="bit.ly URL", value=data["bitly_url"], inline=True)
    description = f"@{ctx.author.name} requested this {tag if tag!='' else 'random'} gif"
    url = (data["url"])
    title = (data["username"])
    embed.description = description
    embed.url = url
    embed.title = title
    await ctx.send(embed=embed)
    
bot.run(TOKEN)