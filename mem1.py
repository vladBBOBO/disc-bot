#from settings import settings
import discord
from discord.ext import commands
import os
import random
# Переменная intents - хранит привилегии бота
intents = discord.Intents.default()
# Включаем привелегию на чтение сообщений
intents.message_content = True
# Создаем бота в переменной client и передаем все привелегии
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
   
@bot.command()
async def mem(ctx):
   with open("images/mem2/jpg","rb") as f:
     picture -discord.file(f)
     await ctx.send(file-picture)
bot.run("")
