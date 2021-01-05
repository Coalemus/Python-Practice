import discord
import random # For 8ball command replies.
from discord.ext import commands

client = commands.Bot(command_prefix = '.') # client variable def. # 

@client.event
async def on_ready(): # When the bot has all the information it needs on Discord.
    print("Bot is ready.")

@client.command(aliases=['8ball']) # 8ball command aliases that can be called rather than acutal func.
async def _8ball(ctx, *, question):
    responses = ['It is certain.',
                'It is decidedly so.',
                'Without a doubt.',
                'Yes - definetly.',
                'You may rely on it',
                'As I see it, yes.',
                'most likely.',
                'Outlook good.',
                'Yes.',
                'Signs point to yes.',
                'Reply hazy, try again.',
                'Ask again later.',
                'Better not tell you now.',
                'Cannot predict now',
                'Concentrate and ask again.',
                'Don\'t count on it.',
                'my reply is no.',
                'my sources say no.',
                'Outlook not very good',
                'Very doubtful.']
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

client.run('NzcwMzE1MTUxMjU3NjMyNzg4.X5bx4w.IEwe36wSOyvJtCy9hSf97hu_wck') # Use Bot token in Parameter / Bot token is a code that links your code to an app so that the code can manipulate the application.
