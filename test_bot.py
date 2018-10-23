# Work with Python 3.7
import discord

TOKEN = 'NTA0MDk3NjAwMjM3MDc2NTIw.DrAFRw.-oBjE-SMp1KuqcZ2e65aa_aTOqU'

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)