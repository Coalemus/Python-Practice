import discord
import random # For 8ball command replies.
from discord.ext import commands

client = commands.Bot(command_prefix = '.') # client variable def. # 

@client.event
async def on_ready(): # When the bot has all the information it needs on Discord.
    print("Bot is ready.")

@client.command()
async def kick(ctx, member : discord.Member, *, reason=None): # defined the member parameter as the member object of discord lib. # * says all the parameters passed in after ctx and member goes to reason.
    await member.kick(reason=reason)

@client.command()
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'Banned {member.mention}')
    
client.run('NzcwMzE1MTUxMjU3NjMyNzg4.X5bx4w.YyRDac0rBKK827drRpbaLMXQY2c') # Use Bot token in Parameter / Bot token is a code that links your code to an app so that the code can manipulate the application.
