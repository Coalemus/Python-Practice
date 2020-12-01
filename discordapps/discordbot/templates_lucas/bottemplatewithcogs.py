import discord
import os # For cog loading pre start 
import random # For 8ball command replies.
from discord.ext import commands

# Cogs are codes that you load into your main code, it assists by sorting.

client = commands.Bot(command_prefix = '.') # client variable def. # 

@client.event
async def on_ready(): # When the bot has all the information it needs on Discord.
    print("Bot is ready.")

@client.command()
async def load(ctx, extension): # extension will be the cog that you want to load.
    client.load_extension(f'cogs.{extension}') # cogs is the folder in the same directory as this code, extension is the python file called.

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

@client.command()
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')

# Recommended practice for preloading the cog extensions.

for filename in os.listdir('./cogs'): # List out all files in a given directory # ./ means current directory this is in. # ./filename look in dir this is in and give all files inside the filename folder.
    if filename.endswith('.py'): # Loop through the files within the file in parameter and checks out files with given parameter.
        client.load_extension(f'cogs.{filename[:-3]}') # [:-3] cuts out the last 3 chars in a file so that only the file name is given not the file type.  It is 3 because we specified filetype .py

client.run('NzcwMzE1MTUxMjU3NjMyNzg4.X5bx4w.YyRDac0rBKK827drRpbaLMXQY2c') # Use Bot token in Parameter / Bot token is a code that links your code to an app so that the code can manipulate the application.
