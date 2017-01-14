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


@bot.event
async def on_ready():
    print('------ Logged in as -----')
    print('Username: ' + bot.user.name)
    print('UserID: ' + bot.user.id)
    print('Prefix: ' + prefix)
    print('----- Output -----')



@bot.command(description='ping')
async def ping():
    """Ping"""
    await bot.say('Pong')













#General Information module
@bot.group(pass_context=True)
async def about(ctx):
    """General Info"""
    if ctx.invoked_subcommand is None:
        await bot.say("Invoked Information Sub-Command")

@about.command(description='info')
async def info():
	"""General information"""
	await bot.say(
    "This bot-kit was developed by Sanjay#2382.\n",
    "However, please contribute if you can!\n",
    "The bot was writtin in python using the\n",
    "discord.py library.\n",
    "[Support Server](https://discordapp.com/invite/8xmtspU)\n",
    "[Repository](https://sanjay-b.github.io/Sanjay-DiscordBot/)\n",
    )

@about.command(description='prefix')
async def prefix():
    """Bot's Prefix"""
    await bot.say("The prefix is " + prefix)

















#math module
@bot.group(pass_context=True)
async def math(ctx):
    """General Info"""
    if ctx.invoked_subcommand is None:
        await bot.say("Invoked Math Sub-Command")

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
