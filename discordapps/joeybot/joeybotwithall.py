import discord
import os 
import random 
from discord.ext import commands
from discord.utils import get 
import youtube_dl
import shutil
from os import system

client = commands.Bot(command_prefix = '.') 

@client.event
async def on_ready(): 
    await client.change_presence(status=discord.Status.idle, activity=discord.Game('learning how to sing')) 
    print("Bot is ready.")
    print('We have logged in as {0.user}'.format(client))

@client.command()
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('.hello'):
        await message.channel.send('Hello!')

@client.event 
async def on_member_join(member):
    print("f'{member} has joined a server.")

@client.event 
async def on_member_remove(member):
    print("f'{member} has left the server.")

@client.command()
async def clear(ctx, amount=0):
    if (ctx.message.author.permissions_in(ctx.message.channel).manage_messages):
        await ctx.channel.purge(limit=amount+1)

@client.command()
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send('Sorry you are not allowed to use this command.')

@client.command()
async def kick(ctx, member : discord.Member, *, reason=None): 
    await member.kick(reason=reason)

@client.command()
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'Banned {member.mention}')

@client.command()
async def unban(ctx, *, member): 
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for banned_entry in banned_users:
        user = banned_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')
            return

@client.command(aliases=['unsaynet'])
async def ping(ctx): 
    await ctx.send(f'Pong! {client.latency * 1000}ms') 

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
    
    def check_queue():
        Queue_infile = os.path.isdir("./Queue")
        if Queue_infile is True:
            DIR = os.path.abspath(os.path.realpath("Queue"))
            length = len(os.listdir(DIR))
            still_q = length - 1
            try:
                first_file = os.listdir(DIR)[0]
            except:
                print("No more queued song(s)\n")
                queues.clear()
                return
            main_location = os.path.dirname(os.path.realpath(__file__))
            song_path = os.path.abspath(os.path.realpath("Queue") + "\\" + first_file)
            if length != 0:
                print("Song done, playing next queued\n")
                print(f"Songs still in queue: {still_q}")
                song_there = os.path.isfile("song.mp3")
                if song_there:
                    os.remove("song.mp3")
                shutil.move(song_path, main_location)
                for file in os.listdir("./"):
                    if file.endswith("mp3"):
                        os.rename(file, "song.mp3")

                voice.play(discord.FFmpegPCMAudio('song.mp3'), after=lambda e: check_queue())
                voice.source = discord.PCMVolumeTransformer(voice.source)
                voice.source.volume = 0.07
    
            else:
                queues.clear()
                return

        else:
            queues.clear()
            print("No songs were queued before the ending of the last song.\n")    
    
    song_there = os.path.isfile('song.mp3')
    try:
        if song_there:
            os.remove("song.mp3")
            queues.clear()
            print('Removed old song file')
    except PermissionError:
        print('Trying to delete song file, but its being played.')
        await ctx.send('ERROR: music playing')
        return

    Queue_infile = os.path.isdir("./Queue")
    try:
        Queue_folder = "./Queue"
        if Queue_infile is True:
            print("Removed old Queue folder")
            shutil.rmtree(Queue_folder)
    except:
        print("No old Queue folder")

    await ctx.send('Getting everything ready now.')

    voice = get(client.voice_clients, guild=ctx.guild) 

    ydl_opts = {
        'format': 'bestaudio/best',
        'quiet': True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }   
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            print('Downloading audio now.\n')
            ydl.download([url])
    except:
        print("FALLBACK: youtube-dl does not support this URL, using Spotify (This is normal if Spotify URL)")
        c_path = os.path.dirname(os.path.realpath(__file__))
        system("spotdl -f " + '"' + c_path + '"' + " -s " + url)

    for file in os.listdir('./'):
        if file.endswith('.mp3'):
            name = file
            print(f'Renamed file: {file}\n')
            os.rename(file, 'song.mp3')

    voice.play(discord.FFmpegPCMAudio('song.mp3'), after=lambda e: check_queue())
    voice.source = discord.PCMVolumeTransformer(voice.source)
    voice.source.volume = 0.07

    nname = name.rsplit('-', 2)
    await ctx.send(f'Playing: {nname[0]}')
    print('Playing\n')

@client.command(pass_context=True, aliases=['pa','pau'])
async def pause(ctx):

    voice = get(client.voice_clients, guild=ctx.guild)

    if voice and voice.is_playing():
        print("music paused")
        voice.pause()
        await ctx.send("music paused")
    else:
        print("music not playing failed pause")
        await ctx.send("music not playing failed pause")

@client.command(pass_context=True, aliases=['r','res'])
async def resume(ctx):

    voice = get(client.voice_clients, guild=ctx.guild)

    if voice and voice.is_paused():
        print("Resumed music")
        voice.resume()
        await ctx.send("Resumed music")
    else:
        print("music is not paused")
        await ctx.send("music is not paused")

@client.command(pass_context=True, aliases=['s','sto'])
async def stop(ctx):

    voice = get(client.voice_clients, guild=ctx.guild)

    queues.clear()

    if voice and voice.is_playing():
        print("music stopped")
        voice.stop()
        await ctx.send("music stopped")
    else:
        print("No music playing failed to stop")
        await ctx.send("No music playing failed to stop")

queues = {}

@client.command(pass_context=True, aliases=['q','que'])
async def queue(ctx, url: str):
    Queue_infile = os.path.isdir("./Queue")
    if Queue_infile is False:
        os.mkdir("Queue")
    DIR = os.path.abspath(os.path.realpath("Queue"))
    q_num = len(os.listdir(DIR))
    q_num += 1
    add_queue = True
    while add_queue:
        if q_num in queues:
            q_num += 1
        else:
            add_queue = False
            queues[q_num] = q_num

    queue_path = os.path.abspath(os.path.realpath("Queue") + f"\\song{q_num}.%(ext)s")

    ydl_opts = {
        'format': 'bestaudio/best',
        'quiet': True,
        'outtmpl': queue_path,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }   
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            print('Downloading audio now.\n')
            ydl.download([url])
    except:
        print("FALLBACK: youtube-dl does not support this URL, using Spotify (This is normal if Spotify URL)")
        q_path = os.path.abspath(os.path.realpath("Queue"))
        system(f"spotdl -ff sng{q_num} -f " + '"' + q_path + '"' + " -s " + url)

    await ctx.send("Adding song " + str(q_num) + " to the queue.")    

    print("Song added to queue\n")

@client.command(aliases=['8ball'])
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

@client.command(aliases=['joe'])
async def joey(ctx, *, question):
    responses = ['Unsa man?', # custom responses
                'Tama man.', # Yes answers
                'mao may nasabutan.',
                'Walay duda ana.',
                'Oo - syempre.',
                'Salig lang.',
                'Salig lang lagi.',
                'Sa akong panan.aw, Oo.',
                'Taas ang posibilidad.',
                'Payts ra tanan.',
                'Oo.',
                'Padung sa Oo ra ang tubag nako ana.',
                'Wala ko kasabot, usbi daw.', # maybe answers
                'Pangutana ra unya.',
                'Nindot noh kung unya nalang ni.',
                'Di ko sure ana', # No answers
                'Hunahuna sa unya pangutana.',
                'Ayaw og salig nako.',
                'Dili akong matubag ana.',
                'Base sa akong mga natun.an kay dili.',
                'Di maayo ang panan.aw nako ani',
                'Duda jud ko ana.',
                'Dili gud.',
                'Buang.',
                'Ambot.',
                'Bye ka.',
                'Gani.', # most common words
                'Unsa man?',
                'Gani.',
                'murag.',
                'Gani.',
                'Unsa man?',
                'Gani.',
                'murag.',
                'Gani.',
                'Unsa man?',
                'Gani.',
                'murag.',
                
                ]           
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

@client.command()
async def load(ctx, extension): 
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

@client.command()
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')
 
client.run('NzcwMzE1MTUxMjU3NjMyNzg4.X5bx4w.IEwe36wSOyvJtCy9hSf97hu_wck')
