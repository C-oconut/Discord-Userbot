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

@bot.group(pass_context=True)
async def about(ctx):
    """General Info"""
    if ctx.invoked_subcommand is None:
        await bot.say("Invoked About Sub-Command")

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
