import discord
from discord.ext import commands
import time
import asyncio
import getinfo
import os
token = os.getenv('token')

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='!')


@bot.command(name="latest")
async def news(ctx):
    message='Son haberler şu şekildedir:\n'
    with open('fpb/newest1.txt','r') as d:
        message += "1-->" + d.readlines()[0]
        await ctx.send(message)
    with open('fpb/newest2.txt','r') as d:
        message = "2-->" + d.readlines()[0]
        await ctx.send(message)
    with open('fpb/newest3.txt','r') as d:
        message = "3-->" + d.readlines()[0]
        await ctx.send(message)
@bot.event
async def on_ready():
    #bot.wait_until_ready()
    channel=bot.get_channel(820785442961096714)
    while True:
        news1,news2,news3 = getinfo.get()
        messagee='Yeni bir haber vaar ! \n'
        with open('fpb/newest1.txt','r+') as d:
            news= d.readlines()[0]
            d.seek(0)
            if news != news1:
                d.truncate()
                d.write(news1)
                await channel.send(messagee+news1)
        with open('fpb/newest2.txt','r+') as d:
            news= d.readlines()[0]
            d.seek(0)
            if news != news2:
                d.truncate()
                d.write(news2)
                await channel.send(messagee+news2)
        with open('fpb/newest3.txt','r+') as d:
            news= d.readlines()[0]
            d.seek(0)
            if news != news3:
                d.truncate()
                d.write(news3)
                await channel.send(messagee+news3)
        await asyncio.sleep(3600)

bot.run(token)