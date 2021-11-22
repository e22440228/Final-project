import discord
from discord.ext import commands
bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print('>> Bot is online<<')
@bot.event
async def on_member_join(member):
    channel = bot.get_channel(912124958958817361)
    await channel.send(f'{member} join!')
@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(912125467677577277)
    await channel.send(f'{member} left!')
@bot.command()
async def 圖片(ctx):
    await ctx.send("HI")
@bot.command()
async def Games(ctx):
    await ctx.send('Which one?')
    await ctx.send('BlackJack, DND')
    

@bot.event
#當有訊息時
async def on_message(message):
    #排除自己的訊息，避免陷入無限循環
    if message.author == bot.user:
        return
    #如果包含 ping，機器人回傳 pong
    if message.content == 'ping':
        await message.channel.send('pong')
    if message.content == '!Game':
        await message.channel.send('Which one?')
        await message.channel.send('BlackJack, DND')
    if message.content == 'BlackJack':
        await message.channel.send('Not yet deployment')


bot.run('***') #TOKEN 在剛剛 Discord Developer 那邊「BOT」頁面裡面
