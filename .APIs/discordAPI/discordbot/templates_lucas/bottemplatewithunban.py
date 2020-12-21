import discord
import random # For 8ball command replies.
from discord.ext import commands

client = commands.Bot(command_prefix = '.') # client variable def. # 

@client.event
async def on_ready(): # When the bot has all the information it needs on Discord.
    print("Bot is ready.")

@client.command()
async def unban(ctx, *, member): # * enables bot to read member with spaces.
    banned_users = await ctx.guild.bans() # Generates a list of banned users.
    member_name, member_discriminator = member.split('#') # To make the bot properly read the name and discriminator

    for banned_entry in banned_users:
        user = banned_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')
            return


client.run('NzcwMzE1MTUxMjU3NjMyNzg4.X5bx4w.IEwe36wSOyvJtCy9hSf97hu_wck') # Use Bot token in Parameter / Bot token is a code that links your code to an app so that the code can manipulate the application.
