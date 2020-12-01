import discord
import os # For cog loading pre start
import random # For 8ball command replies.
from discord.ext import commands, tasks
from itertools import cycle # for cycling through statuses


client = commands.Bot(command_prefix = '.') # client variable def. # 
status = cycle(['Status 1', 'Status 2'])


@client.event
async def on_ready(): # When the bot has all the information it needs on Discord.
    change_status.start() # to run status change cycle
    print("Bot is ready.")

@tasks.loop(seconds=10) # For tasks # Parameters are for duration
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))



#@client.command()
#async def

client.run('NzcwMzE1MTUxMjU3NjMyNzg4.X5bx4w.YyRDac0rBKK827drRpbaLMXQY2c') # Use Bot token in Parameter / Bot token is a code that links your code to an app so that the code can manipulate the application.
