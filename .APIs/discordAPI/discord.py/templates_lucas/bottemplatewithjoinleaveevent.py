import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '.') # client variable def. # 

@client.event
async def on_ready(): # When the bot has all the information it needs on Discord.
    print("Bot is ready.")

@client.event # prompts a member has joined
async def on_member_join(member): # member is an object in discord lib
    print("f'{member} has joined a server.")

@client.event # prompts a member has left
async def on_member_remove(member):
    print("f'{member} has left the server.")


client.run('NzcwMzE1MTUxMjU3NjMyNzg4.X5bx4w.YyRDac0rBKK827drRpbaLMXQY2c') # Use Bot token in Parameter / Bot token is a code that links your code to an app so that the code can manipulate the application.
