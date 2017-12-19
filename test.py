
import discord
from discord.ext import commands



bot = commands.Bot(command_prefix='?')

@bot.event
async def on_ready():
    print('Sisse logitud kui')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


@bot.command()
async def joined(member : discord.Member):
    """Kasutaja liitumise kuupäev."""
    await bot.say('{0.name} joined in {0.joined_at}'.format(member))


bot.run('token')