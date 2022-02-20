from discord.commands import (  # Importing the decorator that makes slash commands.
    slash_command,
)
from discord.ext import commands


class Example(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(guild_ids=[867597533458202644])  # Create a slash command for the supplied guilds.
    async def heloo(self, ctx):
        await ctx.respond("Hi, this is a slash command from a cog!")

def setup(bot):
    bot.add_cog(Example(bot))