# MakiBot
import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import random
from discord import Client
import redis
import urbandictionary as ud
r = redis.Redis(host='localhost', port=6379, db=0)
bot = commands.Bot(command_prefix='$')
dadjokes=["Can february march? No, but april may","I won't buy anything velcro. They are such a rip-off"]
eightball_responses=["Hell yea.","The future is uncertain.","Fuhggetaboutit."]

@bot.event
async def on_ready():
    print ("Maki is here.")
    print ("I am running on " + bot.user.name)
    print ("With the ID: " + str(bot.user.id))

@bot.command(pass_context=True)
async def ping(ctx):
    embed=discord.Embed(description="Pong! :ping_pong:",color=0xE19BFF)
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
    embed = discord.Embed(title="{}\'s info".format(user.display_name),description="Hi",color=0xE19BFF)
    embed.add_field(name="User ID",value="{}".format(user.id),inline=True)
    embed.add_field(name="Status",value="{}".format(user.status),inline=True)
    embed.add_field(name="User's highest role",value="{}".format(user.top_role),inline=True)
    embed.add_field(name="Date of joining the server",value="{}".format(user.joined_at))
    embed.set_thumbnail(url=user.avatar_url)
    await bot.say(embed=embed)
    print("User has requested the info of {}.".format(user.name))

@bot.command(pass_context=True)
async def serverinfo(ctx):
    embed = discord.Embed(name="{}'s info".format(ctx.message.server.name), description="Here's what I could find.", color=0xE19BFF)
    embed.set_author(name="Maki")
    embed.add_field(name="Name", value=ctx.message.server.name, inline=True)
    embed.add_field(name="ID", value=ctx.message.server.id, inline=True)
    embed.add_field(name="Roles", value=len(ctx.message.server.roles), inline=True)
    embed.add_field(name="Members", value=len(ctx.message.server.members))
    embed.set_thumbnail(url=ctx.message.server.icon_url)
    await bot.say(embed=embed)
    print("User has requested server info.")

@bot.command(pass_context=True)
async def kick(ctx, user: discord.Member):
    await bot.say(":boot: Cya, {}. Ya loser!".format(user.name))
    await bot.kick(user)

@bot.command(pass_context=True)
async def dice(ctx):
    embed=discord.Embed(description="You have rolled: "+str(random.randint(1,6)),color=0xE19BFF)
    await bot.say(embed=embed)
    print("User has requested dice rolling.")

@bot.command(pass_context=True)
async def say(ctx,*,args):
    embed=discord.Embed(description=args,color=0xe198ff)
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def math(ctx, arg1, arg2, arg3):
    if arg1=="add" or "+":
        embed=discord.Embed(description=int(arg2+arg3),color=0xe198ff)
        await bot.say(embed=embed)
    elif arg1=="subtract" or "-":
        embed=discord.Embed(description=int(arg2-arg3),color=0xe198ff)
        await bot.say(embed=embed)
    elif arg1=="multiply" or "*":
        embed=discord.Embed(description=int(arg2*arg3),color=0xe198ff)
        await bot.say(embed=embed)
    elif arg1=="divide" or "/":
        embed=discord.Embed(description=int(arg2/arg3),color=0xe198ff)
    else:
        embed=discord.Embed(description="Sorry, I don't know how to math these two numbers.",color=0xe198ff)
        await bot.say(embed=embed)
    print("math math math.")

@bot.command(pass_context=True)
async def invite(ctx):
    embed=discord.Embed(title="Invite Me",color=0xe198ff)
    embed.add_field(name="Invite me to your guild",value="https://discordapp.com/api/oauth2/authorize?client_id=444718926472019968&permissions=0&scope=bot",inline=True)
    embed.add_field(name="Support Server",value="This is the server where you can chat along, recieve support, and support development! :hotsprings:\n https://discord.gg/bA9ry43",inline=True)
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def dadjoke(ctx):
    embed=discord.Embed(description=str(random.choice(dadjokes)),color=0xe198ff)
    await bot.say(embed=embed)
#needs work
@bot.command(pass_context=True)
async def ud(ctx,*,args):
    defs = ud.define(args)
    embed=discord.Embed(title="Definition of {}".format(args),description=str(defs.definition),color=0xe198ff)
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def wikipedia(ctx,*,args):
    if args=="help":
        embed=discord.Embed(title="the Wikipedia Function",color=0xe198ff)
        embed=add_field(name="How to wiki",value="Just type the word you want to search after $wikipedia.",inline=True)
        await bot.say(embed=embed)
    else:
        await bot.say("http://wikipedia.org/wiki/"+args.replace(" ","_"))

@bot.command(pass_context=True)
async def linux(ctx,arg1,arg2):
    embed=discord.Embed(description="I'd just like to interject for a moment. What you're referring to as "+arg2+", is in fact, "+arg1+"/"+arg2+", or as I've recently taken to calling it, "+arg1+" plus "+arg2+". "+arg2+" is not an operating system unto itself, but rather another free component of a fully functioning "+arg1+" system made useful by the "+arg1+" corelibs, shell utilities and vital system components comprising a full OS as defined by POSIX.\nMany computer users run a modified version of the "+arg1+" system every day, without realizing it. Through a peculiar turn of events, the version of "+arg1+" which is widely used today is often called \""+arg2+"\", and many of its users are not aware that it is basically the "+arg1+" system, developed by the "+arg1+" Project. There really is a "+arg2+", and these people are using it, but it is just a part of the system they use. "+arg2+" is the kernel: the program in the system that allocates the machine's resources to the other programs that you run. The kernel is an essential part of an operating system, but useless by itself; it can only function in the context of a complete operating system. "+arg2+" is normally used in combination with the "+arg1+" operating system: the whole system is basically GNU with Linux added, or "+arg1+"/"+arg2+". All the so-called \""+arg2+"\" distributions are really distributions of "+arg1+"/"+arg2+".")
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def eightball(ctx):
    embed=discord.Embed(description=str(random.choice(eightball_responses))
    await bot.say(embed=embed)

bot.run(TOKEN)
