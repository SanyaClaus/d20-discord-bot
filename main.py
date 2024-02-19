import random
import discord
from discord.ext import commands
from config import settings


bot = commands.Bot(command_prefix=settings['prefix'])


@bot.command()
async def hi(ctx):
    # Объявляем переменную author и записываем туда информацию об авторе.
    author = ctx.message.author  
    # Выводим сообщение с упоминанием автора, обращаясь к переменной author.
    await ctx.send(
        f'Привет, {author.mention}!')


@bot.command(pass_context=True)
async def d1000(ctx):
    author = ctx.message.author
    dice = random.randint(1, 1000)
    await ctx.send(f'{author.mention} бросил(а) кубик d1000 и выпало {dice}!')
    if dice == 1:
        await ctx.send(file=discord.File('.\\img\\cake1.png'))


@bot.command(pass_context=True)
async def d100(ctx):
    author = ctx.message.author
    dice = random.randint(1, 100)
    await ctx.send(f'{author.mention} бросил(а) кубик d100 и выпало {dice}!')
    if dice == 1:
        await ctx.send(file=discord.File('.\\img\\cake1.png'))


@bot.command(pass_context=True)
async def d20(ctx):
    author = ctx.message.author
    dice = random.randint(1, 20)
    await ctx.send(f'{author.mention} бросил(а) кубик d20 и выпало {dice}!')
    if dice == 1:
        await ctx.send(file=discord.File('.\\img\\cake1.png'))


@bot.command(pass_context=True)
async def d10(ctx):
    author = ctx.message.author
    dice = random.randint(1, 10)
    await ctx.send(f'{author.mention} бросил(а) кубик d10 и выпало {dice}!')


@bot.command(pass_context=True)
async def d6(ctx):
    author = ctx.message.author
    dice = random.randint(1, 6)
    await ctx.send(f'{author.mention} бросил(а) кубик d6 и выпало {dice}!')


@bot.command(pass_context=True)
async def d3(ctx):
    author = ctx.message.author
    dice = random.randint(1, 3)
    await ctx.send(f'{author.mention} бросил кубик d3 и выпало {dice}!')


@bot.command(pass_context=True)
async def info(ctx):
    info_text = '!d100, !d20, !d10, !d6, !d3 - бросок кубика с этим числом граней.'
    await ctx.send(info_text)


bot.run(settings['token'])  # Обращаемся к словарю settings с ключом token, для получения токена
