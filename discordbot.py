import discord
from discord.ext import commands
import asyncio
from time import sleep
import random as randm

abi = """Käskluste seletused. Commands help"""
bot = commands.Bot(command_prefix='!', description = abi)
client = discord.Client()


@bot.event
async def on_ready():
    print('Bot töötab')
    await bot.change_presence(game=discord.Game(name="esitlus"))
    

@bot.command()
async def add(vasak : int, parem : int):
    """Adds two numbers"""
    await bot.say(vasak + parem)
       
@bot.command()
async def subtract(vasak : int, parem : int):
    """Subtracts two numbers"""
    await bot.say(vasak - parem)
    
@bot.command()
async def multiply(vasak : int, parem : int):
    """Multiplies two numbers"""
    await bot.say(vasak * parem)
    
@bot.command()
async def divide(vasak : int, parem : int):
    """Divides two numbers"""
    await bot.say(vasak / parem)
 
 
@bot.command()
async def liida(vasak : int, parem : int):
    """Liidab kaks numbrit"""
    await bot.say(vasak + parem)
       
@bot.command()
async def lahuta(vasak : int, parem : int):
    """Lahutab kaks numbrit"""
    await bot.say(vasak - parem)
    
@bot.command()
async def korruta(vasak : int, parem : int):
    """Korrutab kaks numbrit"""
    await bot.say(vasak * parem)
    
@bot.command()
async def jaga(vasak : int, parem : int):
    """Jagab kaks numbrit"""
    await bot.say(vasak / parem)
    
      
@bot.command()
async def mündivise():
    """Viska münti"""
    number = randm.randint(1,2)
    if number == 1:
        await bot.say("Kiri")
    else:
        await bot.say("Kull")
        
@bot.command()
async def coinflip():
    """Does a coinlip"""
    number = randm.randint(1,2)
    if number == 1:
        await bot.say("Heads")
    else:
        await bot.say("Tails")
        
         
@bot.command()
async def korda(mitukorda : int, * , sisu='Kordan...'):
    """Korrutab sõnumit nii mitu kui korda kui tahad"""
    for i in range(mitukorda):
        await bot.say(sisu)
        
@bot.command()
async def repeat(mitukorda : int, * , sisu='repeating...'):
    """Repeats your message."""
    for i in range(mitukorda):
        await bot.say(sisu)   
              
        
@bot.command()
async def suvaline(esimene : int, viimane : int):
    """Suvaline number valitud vahemikus"""
    await bot.say(randm.randint(esimene,viimane))
    
@bot.command()
async def random(esimene : int, viimane : int):
    """Returns a random number in your selected range"""
    await bot.say(randm.randint(esimene,viimane))


@bot.command(pass_context=True)
async def kick(ctx, kasutaja: discord.Member):
    """Viska kasutaja grupist välja. Kick an user from the group"""
    await bot.say("Head teed, {}".format(kasutaja.name))
    await bot.say("Bye bye, {}".format(kasutaja.name))
    await bot.kick(kasutaja)
    
@bot.command(pass_context=True)
async def ban(ctx, kasutaja: discord.Member):
    """Viska kasutaja igaveseks grupist välja. Ban an user from the group"""
    await bot.say("{} visati grupist välja".format(kasutaja.name))
    await bot.say("{} was thrown out of the group".format(kasutaja.name))
    await bot.ban(kasutaja)
  
    
@bot.command(pass_context=True)
async def serverinfo(ctx):
    """Kuvab info serveri kohta"""
    embed = discord.Embed(name="{}'s info".format(ctx.message.server.name), description="Serveri info", color=0x00ff00)
    embed.add_field(name="Nimi", value=ctx.message.server.name, inline=True)
    embed.add_field(name="ID", value=ctx.message.server.id, inline=True)
    embed.add_field(name="Rollid", value=len(ctx.message.server.roles), inline=True)
    embed.add_field(name="Liikmed", value=len(ctx.message.server.members))
    embed.add_field(name="Loodud", value=ctx.message.server.created_at)
    embed.set_thumbnail(url=ctx.message.server.icon_url)
    await bot.say(embed=embed)
        
@bot.command(pass_context=True)
async def info(ctx, kasutaja: discord.Member):
    """Kuvab info serveri liikme kohta"""
    await bot.say("Kasutajanimi: {}".format(kasutaja.name))
    await bot.say("Kasutaja ID: {}".format(kasutaja.id))
    await bot.say("Kasutaja staatus: {}".format(kasutaja.status))
    await bot.say("Kasutaja kõrgeim staatus: {}".format(kasutaja.top_role))
    await bot.say("Kasutaja liitus: {}".format(kasutaja.joined_at))
    

@bot.command(pass_context=True)
async def say(ctx, *, sõnum):
    """Make the bot say something"""
    await bot.say(sõnum)
    await asyncio.sleep(1)
    await bot.delete_message(ctx.message)
    
@bot.command(pass_context=True)
async def ütle(ctx, *, sõnum):
    """Pane bot midagi ütlema"""
    await bot.say(sõnum)
    await asyncio.sleep(1)
    await bot.delete_message(ctx.message)    


@bot.command(pass_context = True)
async def kustuta(ctx, number):
    """Kustuta sõnumid"""
    sõnumid = []
    number = int(number)
    await bot.say("Kustutan "+ str(number) + " sõnumit.")
    async for x in bot.logs_from(ctx.message.channel, limit = number+2):
        sõnumid.append(x)
    await asyncio.sleep(1)
    await bot.delete_messages(sõnumid)
    
@bot.command(pass_context = True)
async def delete(ctx, number):
    """Delete messages"""
    sõnumid = []
    number = int(number)
    await bot.say("Deleting "+ str(number) + " messages.")
    async for x in bot.logs_from(ctx.message.channel, limit = number+2):
        sõnumid.append(x)
    await asyncio.sleep(1)
    await bot.delete_messages(sõnumid)

@bot.event
async def on_member_join(member):
    asi = member.server.channel
    msg = "Tere tulemast {0} {1}-sse".format(member.mention, member.server.name)
    await client.send_message(asi, msg)
    
     
    
bot.run("Mzg2MDkzMzcyOTAyNzM1ODcy.DQK5HA.rTuuPARdouAbF-ktidVBZ8QBQFY")