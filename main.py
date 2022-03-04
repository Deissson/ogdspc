import os
import time

import discord
import pyautogui
from discord.ext import commands

bot = commands.Bot(command_prefix='og!')
#этот бот затачивался для одного сервака, скоро сделаю чтобы можно было указать канал где будет работать и сделаю норм проверку

@bot.command()
async def screen(ctx):
    if ctx.channel == 949370517285126194:
        pyautogui.screenshot('screen.png')
        with open('screen.png', 'rb') as f:
            screen = discord.File(f)
        await ctx.channel.send(f'Позиция мыши{pyautogui.position()}', file=screen)


@bot.command()
async def start(ctx, arg):
    if ctx.channel == 949370517285126194:
        os.system(arg)
        time.sleep(0.5)
        await screen(ctx)


@bot.command()
async def hotkey(ctx, *args):
    if ctx.channel == 949370517285126194:
        pyautogui.hotkey(*args)
        time.sleep(0.5)
        await screen(ctx)


@bot.command()
async def moveto(ctx, arg1, arg2):
    if ctx.channel == 949370517285126194:
        pyautogui.moveTo(int(arg1), int(arg2))
        time.sleep(0.5)
        await screen(ctx)


@bot.command()
async def moveleft(ctx, arg1):
    if ctx.channel == 949370517285126194:
        pyautogui.move(abs(int(arg1)), 0)
        time.sleep(0.5)
        await screen(ctx)


@bot.command()
async def moveright(ctx, arg1):
    if ctx.channel == 949370517285126194:
        pyautogui.move(int(arg1), 0)
        time.sleep(0.5)
        await screen(ctx)


@bot.command()
async def moveup(ctx, arg1):
    if ctx.channel == 949370517285126194:
        pyautogui.move(0, int(arg1))
        time.sleep(0.5)
        await screen(ctx)


@bot.command()
async def movedown(ctx, arg1):
    if ctx.channel == 949370517285126194:
        pyautogui.move(0, abs(int(arg1)))
        time.sleep(0.5)
        await screen(ctx)


@bot.command()
async def move(ctx, arg1, arg2):
    if ctx.channel == 949370517285126194:
        pyautogui.move(int(arg1), int(arg2))
        time.sleep(0.5)
        await screen(ctx)

@bot.command()
async def help(ctx):
    if ctx.channel == 949370517285126194:
        await ctx.channel.send('og!screen - отправка скрина\nog!start "команда"(в кавычках)\nog!moveto x y - перемещает курсор на координаты монитора\nog!move{up down left rigth} pos - перемешает курсор в какое либо направление\nog!move x y перемещает курсор по координатам  ')

