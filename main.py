import os
import time

import discord
import pyautogui
from discord.ext import commands

#переменые

TOKEN = "YOUR_TOKEN_GOES_HERE"
channel_id = "YOUR_CHANNEL_ID_GOES_HERE"
bot = commands.Bot(command_prefix='og!')

#этот бот затачивался для одного сервака, скоро сделаю чтобы можно было указать канал где будет работать и сделаю норм проверку

@bot.command()
async def screen(ctx):
    if ctx.channel == channel_id:
        pyautogui.screenshot('screen.png')
        with open('screen.png', 'rb') as f:
            screen = discord.File(f)
        await ctx.channel.send(f'Позиция мыши{pyautogui.position()}', file=screen)


@bot.command()
async def start(ctx, arg):
    if ctx.channel == channel_id:
        os.system(arg)
        time.sleep(0.5)
        await screen(ctx)


@bot.command()
async def hotkey(ctx, *args):
    if ctx.channel == channel_id:
        pyautogui.hotkey(*args)
        time.sleep(0.5)
        await screen(ctx)


@bot.command()
async def moveto(ctx, arg1, arg2):
    if ctx.channel == channel_id:
        pyautogui.moveTo(int(arg1), int(arg2))
        time.sleep(0.5)
        await screen(ctx)


@bot.command()
async def moveleft(ctx, arg1):
    if ctx.channel == channel_id:
        pyautogui.move(abs(int(arg1)), 0)
        time.sleep(0.5)
        await screen(ctx)


@bot.command()
async def moveright(ctx, arg1):
    if ctx.channel == channel_id:
        pyautogui.move(int(arg1), 0)
        time.sleep(0.5)
        await screen(ctx)


@bot.command()
async def moveup(ctx, arg1):
    if ctx.channel == channel_id:
        pyautogui.move(0, int(arg1))
        time.sleep(0.5)
        await screen(ctx)


@bot.command()
async def movedown(ctx, arg1):
    if ctx.channel == channel_id:
        pyautogui.move(0, abs(int(arg1)))
        time.sleep(0.5)
        await screen(ctx)


@bot.command()
async def move(ctx, arg1, arg2):
    if ctx.channel == channel_id:
        pyautogui.move(int(arg1), int(arg2))
        time.sleep(0.5)
        await screen(ctx)

@bot.command()
async def help(ctx):
    if ctx.channel == channel_id:
        await ctx.channel.send('og!screen - отправка скрина\nog!start "команда"(в кавычках)\nog!moveto x y - перемещает курсор на координаты монитора\nog!move{up down left rigth} pos - перемешает курсор в какое либо направление\nog!move x y перемещает курсор по координатам  ')

