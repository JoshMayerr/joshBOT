import os
import discord
import random

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):

    sayings = ['I love pancakes!', 'Go Warriors!',
               'Spark! is the best place to work on campus.', 'West coast best coast.', 'The Mandalorian is the best Disney+']

    if message.author == client.user:
        return

#     enter you commands here


client.run(INSERT_TOKEN_HERE)
