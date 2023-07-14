import os
import discord
from discord.ext import commands

intents = discord.Intents.all()
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.command()
async def hellolyka(ctx):
  await ctx.send("Hello Rohan What's up?")

token = os.environ['TOKEN']
bot.run(token)