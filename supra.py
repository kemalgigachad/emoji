import discord
from sifre import  gen_pass



# ayricaliklar (intents) değişkeni botun ayrıcalıklarını depolayacak
intents = discord.Intents.default()
# Mesajları okuma ayrıcalığını etkinleştirelim
intents.message_content = True
# client (istemci) değişkeniyle bir bot oluşturalım ve ayrıcalıkları ona aktaralım
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):   
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send("Hi!")   
    if message.content.startswith('$pass'):
        await message.channel.send(gen_pass(7))     
    elif message.content.startswith('$gulen yuz'):
        await message.channel.send("\U0001f642")
    elif message.content.startswith('$siritan yuz'):
        await message.channel.send("\U0001f600") 
    elif message.content.startswith('$gulmekten olen yuz'):
        await message.channel.send("\U0001F923")   
    else:
        await message.channel.send(message.content)

client.run("")
