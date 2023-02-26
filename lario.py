import os
import random

import discord
from discord.ext import tasks
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

    channel = await client.fetch_channel("your channel here") 
    @tasks.loop(minutes=5)

    async def sendmessage():
        await channel.send("Wheezy outta here")

        post = random.choice(os.listdir("./posts/"))
        await channel.send(file=discord.File('./posts/' + post))
        
    await sendmessage.start()


client.run(TOKEN)
