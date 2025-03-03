


from http import client
from re import IGNORECASE
from discord.ext import commands
import discord
import random #Used for random greeting
import sys
import time
import os
import pygame
from colorama import init
init(strip=not sys.stdout.isatty())  # Strip colors if stdout is redirected
from termcolor import cprint
from pyfiglet import figlet_format #used for ASCII
from discord import Client, Intents


GIF_FOLDER = r"PATH TO YOUR GIF FOLDER"






BOT_TOKEN = "REPLACE ME WITH YOUR BOT TOKEN" #Unique token for this bot
#Everytime the bot code runs, it will use a random start up phrase in this channel
CHANNEL_ID = REPLACE ME WITH YOUR DISCORD TEXT CHANNEL ID #Discord channel ID



bot = commands.Bot(command_prefix="!", intents=discord.Intents.all()) 




@bot.event
async def on_ready():
    print("Im booting up ahah!!(;")                                     
    channel = bot.get_channel(CHANNEL_ID)  #Makes sure bot talks in the right channel                                                                             


    #CONSOLE MESSAGE
    art = figlet_format('LAUNCHING', font='larry3d') #use larry3d to start  # Generate the ASCII art
    cprint(art, 'red', 'on_black', attrs=['bold'])   # Print the ASCII art to the console with color



    channelIntroList = [
        
        "im fresh to death fr", "dw ill be humble aha",
        "if i spend my whole bankroll ill affect the DOW", "sponsored by the shadow government",
        "the king is back", "did you miss me aha?",
        
        ]
    
    if channel:
        await channel.send(random.choice(channelIntroList))
    
        await nopicturesplease(channel)   # Send a random GIF after the intro message







@bot.command()
async def nopicturesplease(ctx):
    # Get all files in the 'gifs' folder (check .gif, .png, .jpg)
    media_files = [f for f in os.listdir(GIF_FOLDER) if f.endswith(('.gif', '.png', '.jpg'))]

    # If the folder is empty, inform the user
    if not media_files:
        await ctx.send("No media files found in the folder!")
        return
    
    # Pick a random file (GIF, PNG, or JPG)
    chosen_file = random.choice(media_files)
    
    # Create a path to the chosen file
    file_path = os.path.join(GIF_FOLDER, chosen_file)
    
    # Send the media file to the channel
    await ctx.send(file=discord.File(file_path))




@bot.event
async def on_message(message):                      #Prevents the bot from sending the same message a bunch of times

    #if bot.user.mentioned_in(message):                   #Use this code to get bot to reply to you with something
        #await message.channel.send('You mentioned me!')

    # Ignore messages from the bot itself
    if message.author == bot.user:
        return

    # Process commands
    await bot.process_commands(message)





    



complimentIntro = [
    
    #ADD MORE INTROS HERE
    
    ]
complimentAdj = [
    
    #Add more adjectives here
    
    ]
complimentNoun = [
    
    #Add more nouns here
    
    ]
@bot.command()                                      
async def rizzme(ctx):
    await ctx.send(random.choice(complimentIntro) + " " + random.choice(complimentAdj) + " " + random.choice(complimentNoun))



insultIntroList = [
    "down bad"
    ]
insultAdjList = [

    #Add more adjectives here

    ]
insultNounList = [

    ]                               #Command !insult
insultNounList2 = [
    
    ]
@bot.command()                                      
async def roastme(ctx):
    await ctx.send("You're a " + random.choice(insultIntroList) + " " + random.choice(insultAdjList) + " " + random.choice(insultNounList) + " " + random.choice(insultNounList2))


helloList = [
    "ah h e eeeeey ", "hey(; ", "Sup dawg ", "Aye ", "What it do ahaha", "who are you hahah ",
    "no pictures please ", "whats up big dog ", "whats good aaahah ", "h e y ", "h e y y ", "h e y y y ",
    "ahaha heeyy whats up ", "aha, yo ", "yo yo     (; ", "where you been aha ", "i missed you ;( ", "(; "
    ]
@bot.command()                                      #Command !hello makes Joeyy say a random greeting in response to the user #add more hey, hi, etc commands
async def hello(ctx):
    await ctx.send(random.choice(helloList) + ctx.author.mention)

@bot.command()                                      #Command !commands makes Joeyy respond with a list of current commands
async def commands(ctx):
    await ctx.send("""
    Commands:

    !hello ------------------------------> random greeting

    !art(number) *insert word(s)* --------> ASCII art of word(s)

            !art   -----> larry3d ASCII    (Default)
            !art1  -----> smisome1 ASCII 
            !art2  -----> graffiti ASCII 
            !art3  -----> eftiwater ASCII 
            !art4  -----> ogre ASCII 
            !art5  -----> smkeyboard ASCII 
            !art6  -----> block ASCII 
            !art7  -----> bulbhead ASCII
            !art8  -----> poison ASCII
            !art9  -----> serifcap ASCII
            !art10 -----> cybersmall ASCII
            !art11 -----> slant ASCII

    !roastme -----------------------------> BOT roasts you

    !rizzme -----------------------------> BOT rizz

    !nopicturesplease -------------------> Sends a random gif, jpg, or png

    """)

FONT_MAP = {
    'art': 'larry3d',
    'art1': 'smisome1',
    'art2': 'graffiti',
    'art3': 'eftiwater',
    'art4': 'ogre',
    'art5': 'smkeyboard',
    'art6': 'block',
    'art7': 'bulbhead',
    'art8': 'poison',
    'art9': 'serifcap',
    'art10': 'cybersmall',
    'art11': 'slant',
}

@bot.command(name='art')  # Main command
async def art(ctx, *, text: str):
    command_name = ctx.invoked_with  # Get the command used
    font = FONT_MAP.get(command_name, 'larry3d')  # Get the corresponding font

    # Generate the ASCII art
    ascii_art = figlet_format(text, font=font)

    # Print the ASCII art
    await ctx.send(f"```\n{ascii_art}```")
# Create individual commands for each alias
for command_name in FONT_MAP.keys():
    if command_name != 'art':  # Skip the main command
        @bot.command(name=command_name)
        async def alias_art(ctx, *, text: str, font=FONT_MAP[command_name]):
            ascii_art = figlet_format(text, font=font)
            await ctx.send(f"```\n{ascii_art}```")


bot.run(BOT_TOKEN) #Run bot
