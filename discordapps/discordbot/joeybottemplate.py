import discord
import os # For cog loading pre start
import random # For 8ball command replies.
from discord.ext import commands

client = commands.Bot(command_prefix = '.') # client variable def. # 

@client.event
async def on_ready(): # When the bot has all the information it needs on Discord.
    await client.change_presence(status=discord.Status.idle, activity=discord.Game('with myself')) 
    print("Bot is ready.")
    print('We have logged in as {0.user}'.format(client))

#@client.command()
#async def

client.run('NzcwMzE1MTUxMjU3NjMyNzg4.X5bx4w.YyRDac0rBKK827drRpbaLMXQY2c') # Use Bot token in Parameter / Bot token is a code that links your code to an app so that the code can manipulate the application.
