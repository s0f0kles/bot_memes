import discord
from discord.ext import commands
from config_images import TOKEN
import random

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send('Привет! Я бот!')
    else:
        await message.channel.send("Я не понимаю такую команду!")
    await bot.tree.process_interaction(message)


@bot.command()
async def mem(ctx):
    image_files_rarity = {
        'mem1.jpg': 5, 
        'mem2.jpg': 3, 
        'mem3.jpg': 4,
        'mem4.jpg': 2,
    }    

    chosen_file = random.choice(list(image_files_rarity.keys)), 
    weights=list(image_files_rarity.values())[0]

    picture = discord.File(f'images/{chosen_file}')
    await ctx.send(file=picture)

    
bot.run(TOKEN)