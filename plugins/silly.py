import discord
import random
import discord
from discord.ext import commands
from discord.ext.commands import Bot

@bot.command(pass_context=True)
async def joke(ctx,arg1):
    if arg1=="polanjoke":
        embed=discord.Embed(description=random.choice(polanjokes))
        await bot.say(embed=embed)
    else:
        embed=discord.Embed(description="Sorry, no such joke type found.")

@bot.command(pass_context=True)
async def eightball(ctx):
    embed=discord.Embed(description=str(random.choice(eightball_responses))
    await bot.say(embed=embed)