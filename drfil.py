import discord
from discord.ext import commands

TOKEN = 'Njc1NzA4MDQ0OTE4OTE1MDk0.Xj7PxQ.9S8YUMI_IR6w_G-NFQmE21my-F4'

client = commands.Bot(command_prefix = '!')


@client.event
async def on_ready():
    print('klar')


client.run(TOKEN)
