#Basic UserBot used to respond when im offline
#Feel free to use, make sure you give credit. :)
#Created by Sanjay
#Discord.py Library

import discord
from discord.ext import commands
import random
import logging
logging.basicConfig(level=logging.INFO) #Logs command prompt


#Basic Bot Info
description = '''NAME OF BOT'''
prefix = '''PREFIX'''
bot = False
bot = commands.Bot(command_prefix='PREFIX', description=description)


#Non-Categoric Commands
@bot.command(description='ping')
async def ping():
    """Ping"""
    await bot.say(embed=discord.Embed(title='Ping Result',description='pong', colour=discord.Colour.blue()))

@bot.command(description='shutdown',pass_context=False)
async def shutdown():
    """Shutdown"""
    await bot.logout()















#General Information module
@bot.group(pass_context=True)
async def about(ctx):
    """General Info"""
    if ctx.invoked_subcommand is None:
        await bot.say(embed=discord.Embed(title='Invoked',description='About Section', colour=discord.Colour.green()))

@about.command(description='info')
async def info():
    """General information"""
    await bot.say(embed=discord.Embed(title='Information',description='Developed by Sanjay#2382 [Support Server](https://discordapp.com/invite/8xmtspU) [Repository](https://sanjay-b.github.io/Sanjay-DiscordBot/)', colour=discord.Colour.teal()))


@about.command(description='prefix')
async def prefix():
    """Bot's Prefix"""
    await bot.say(embed=discord.Embed(title='Invoked',description='The prefix is " + "``" + prefix1 + "``', colour=discord.Colour.blue()))


















#math module
@bot.group(pass_context=True)
async def math(ctx):
    """Set of Math Commands"""
    if ctx.invoked_subcommand is None:
        await bot.say(embed=discord.Embed(title='Invoked',description='Math Section', colour=discord.Colour.blue()))

@math.command(description='add')
async def add(number1 : int, number2 : int):
    """Adds numbers"""
    await bot.say(number1 + number2)

@math.command(description='subtract')
async def subtract(number1 : int, number2 : int):
    """Subtracts numbers"""
    await bot.say(number1 - number2)

@math.command(description='multiply')
async def multiply(number1 : int, number2 : int):
    """Multiplies numbers"""
    await bot.say(number1 * number2)

@math.command(description='divide')
async def divide(number1 : int, number2 : int):
    """Divides numbers"""
    await bot.say(number1 / number2)









bot.run("YOUR TOKEN HERE")
