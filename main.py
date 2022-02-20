import discord
from discord.ext import commands
from discord.ext import tasks
from discord.commands import Option
from dotenv import load_dotenv
import os
import random

# Gravity Destroyers secret security bot

bot = commands.Bot(command_prefix="a!")

load_dotenv()
BOT_TOKEN = os.getenv("A_TOKEN")

@bot.event
async def on_ready():
    print("I'm ready")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Rowan"))


@bot.command()
async def halp(ctx, mod=None):
    if mod == None:
        await ctx.send("myhelpcmd")
    if mod == "mod":
        await ctx.send("Wow, now you've found out about my secrety security functions")

@bot.slash_command(guild_ids=[867597533458202644])  # create a slash command for the supplied guilds
async def hello(ctx):
    """Say hello to the bot"""  # the command description can be supplied as the docstring
    await ctx.respond(f"Hello {ctx.author}! :blush:")

bot.load_extension('cog')