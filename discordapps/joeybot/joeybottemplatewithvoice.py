import discord
from discord.ext import commands
from discord.utils import get 
import youtube_dl
import os

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game('with myself')) 
    print("Bot is ready.")
    print('We have logged in as {0.user}'.format(client))


@client.command(pass_context=True, aliases=['j','joi'])
async def join(ctx):
    global voice
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild=ctx.guild)

    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()

    await voice.disconnect()

    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
        print(f'The bot has connected to {channel}\n')

    await ctx.send(f'joined {channel}')    


@client.command(pass_context=True, aliases=['l','lea'])
async def leave(ctx):
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild=ctx.guild)

    if voice and voice.is_connected():
        await voice.disconnect()
        print(f'The bot has left {channel}')
        await ctx.send(f'Left {channel}')   
    else:
        print('Bot was told to leave voice channel, but was not in one.')
        await ctx.send('Dont think I am in a voice channel.')

@client.command(pass_context=True, aliases=['p','pla'])
async def play(ctx, url: str):
    song_there = os.path.isfile('song.mp3')
    try:
        if song_there:
            os.remove("song.mp3")
            print('Removed old song file')
    except PermissionError:
        print('Trying to delete song file, but its being played.')
        await ctx.send('ERROR: music playing')
        return

    await ctx.send('Getting everything ready now.')

    voice = get(client.voice_clients, guild=ctx.guild) 

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }   

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        print('Downloading audio now.\n')
        ydl.download([url])
    
    for file in os.listdir('./'):
        if file.endswith('.mp3'):
            name = file
            print(f'Renamed file: {file}\n')
            os.rename(file, 'song.mp3')

    voice.play(discord.FFmpegPCMAudio('song.mp3'), after=lambda e: print(f'{name} has finished playing.'))
    voice.source = discord.PCMVolumeTransformer(voice.source)
    voice.source.volume = 0.07

    nname = name.rsplit('-', 2)
    await ctx.send(f'Playing: {nname[0]}')
    print('Playing\n')



client.run('NzcwMzE1MTUxMjU3NjMyNzg4.X5bx4w.IEwe36wSOyvJtCy9hSf97hu_wck')
