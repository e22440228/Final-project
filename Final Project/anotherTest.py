from gc import enable
import random
import discord
import random
from discord import player
from discord import channel
from discord.abc import User

from discord.embeds import Embed
from discord.enums import SpeakingState
from discord.ext.commands.converter import PartialMessageConverter
import Game
from discord import message
from discord.ext import commands
from discord.utils import get
from discord.ext.commands import context
bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print('>>bot is online<<')

@bot.event
async def on_message(message):
    data = []
    
    #async for content in message.channel.history(limit = 1):
    
    if message.author == bot.user:
            await message.add_reaction('\U0001F44D')
            await message.add_reaction('\U0001F44E')
    await bot.process_commands(message)

def randomnumber():
    numbers =random.randint(1,13)
    return numbers

example = {'player_number':'','dealer_number':''}
value = {'player_value':0,'dealer_value':0}



@bot.command()
async def test(ctx):
    special = {11:'J',12:'Q',13:"K"}
    player_card = ''
    dealer_card = ''

    numbers = randomnumber()
    dealer_number = randomnumber()
    if numbers == 1:
        if value['player_value'] + 10 > 21:
            numbers = 1
            value['player_value'] = value['player_value'] + numbers
        elif value['player_value'] + 10 < 21:
            numbers = 10
            value['player_value'] = value['player_value'] + numbers
        if len(player_card) == 2 and value['player_value'] == 10:
            value['player_value'] = 21


    if dealer_number == 1:
        if value['dealer_value'] + 10 > 21:
            dealer_number = 1
            value['dealer_value'] = value['dealer_value'] + dealer_number
        elif value['dealer_value'] + 10 < 21:
            dealer_number = 10
            value['dealer_value'] = value['dealer_value'] + dealer_number

    if numbers in (11,12,13):
        value['player_value'] = value['player_value'] + 10
    else:
        value['player_value'] = value['player_value'] + numbers
    if dealer_number in (11,12,13):
        value['dealer_value'] = value['dealer_value'] + 10
    else:
        value['dealer_value'] = value['dealer_value'] + dealer_number

    
    Color_Shape = random.choice(['\U00002664','\U00002661','\U00002667','\U00002662']) 

    if numbers in special:
        numbers = special[numbers]
    if dealer_number in special:
        dealer_number = special[dealer_number]


    player_card = Color_Shape + str(numbers)
    dealer_card = Color_Shape + str(dealer_number)
    embed=discord.Embed(title= ctx.message.author, description='BlackJack', color=0xf40b0b)
    embed.set_author(name='Player',icon_url=ctx.message.author.avatar_url)
    embed.add_field(name='You', value= player_card, inline=True)
    embed.add_field(name='Current Value',value = value['player_value'],inline=False)
    embed.add_field(name='Dealer', value=dealer_card, inline=True)
    embed.add_field(name='Current Value',value = value['dealer_value'],inline=False)

    await ctx.message.channel.send(embed=embed)
    example['player_number'] = example['player_number'] + player_card
    example['dealer_number'] = example['dealer_number'] + dealer_card

    return example,value


@bot.event
async def on_reaction_add(reaction, user):
    emoji = reaction.emoji
    count = 0
    channel = bot.get_channel(791205845588377600)
    change = 0
    if user.bot:
        return

    if emoji == "\U0001F44D":
        count += 1
    elif emoji == "\U0001F44E":
        count -= 1
    else:
        return
    if count >= 1:
       
        special = {11:'J',12:'Q',13:"K"}
        player_card = ''
        dealer_card = ''
        numbers = randomnumber()
        dealer_number = randomnumber()
        
        if numbers == 1:
            if len(player_card) <=3 and value['player_value'] == 10:
                value['player_value'] = 21
            if value['player_value'] + 10 > 21:
                numbers = 1
                value['player_value'] = value['player_value'] + numbers
            elif value['player_value'] + 10 < 21:
                numbers = 10
                value['player_value'] = value['player_value'] + numbers


        elif numbers in (11,12,13):
            if len(player_card) <=2 and value['player_value'] == 1:
                value['player_value'] = 21
            else:
                value['player_value'] = value['player_value'] + 10
        else:
            value['player_value'] = value['player_value'] + numbers

            
        Color_Shape = random.choice(['\U00002664','\U00002661','\U00002667','\U00002662'])
        if numbers in special:
            numbers = special[numbers]

        player_card = Color_Shape + str(numbers)

        example['player_number'] = example['player_number'] + player_card

        embed=discord.Embed(title=user, description='BlackJack', color=0xf40b0b)
        embed.set_author(name='Player',icon_url=user.avatar_url)
        embed.add_field(name='You', value= example['player_number'], inline=False)
        embed.add_field(name='Current Value',value = value['player_value'],inline=False)
        embed.add_field(name='Dealer', value=example['dealer_number'], inline=False)
        embed.add_field(name='Current Value',value = value['dealer_value'],inline=False)

        await channel.send(embed=embed)        

        return example,value
        #print(test(reaction)[1])
        
    elif count <= -1:
        # set while loop, until the dealer numers >, =, < player number
        while value['dealer_value'] < 17:
            if value['dealer_value'] >= 17:
                change = 1
            special = {11:'J',12:'Q',13:"K"}
            player_card = ''
            dealer_card = ''
            numbers = randomnumber()
            dealer_number = randomnumber()
            if value['dealer_value'] >= 17:
                decision = True

            if dealer_number == 1:
                if len(dealer_card) <3 and value['dealer_value'] == 10:
                    value['dealer_value'] = 21
                if value['dealer_value'] + 10 > 21:
                    dealer_number = 1
                    value['dealer_value'] = value['dealer_value'] + dealer_number
                elif value['dealer_value'] + 10 < 21:
                    dealer_number = 10
                    value['dealer_value'] = value['dealer_value'] + dealer_number


            elif dealer_number in (11,12,13):
                if len(dealer_card) <=2 and value['dealer_value'] == 1:
                    value['dealer_value'] = 21
                else:
                    value['dealer_value'] = value['dealer_value'] + 10
            else:
                value['dealer_value'] = value['dealer_value'] + dealer_number


                
            Color_Shape = random.choice(['\U00002664','\U00002661','\U00002667','\U00002662'])

            if dealer_number in special:
                dealer_number = special[dealer_number]

            dealer_card = Color_Shape + str(dealer_number)

            example['dealer_number'] = example['dealer_number'] + dealer_card

        embed=discord.Embed(title=user, description='BlackJack', color=0xf40b0b)
        embed.add_field(name='You', value= example['player_number'], inline=False)
        embed.add_field(name='Current Value',value = value['player_value'],inline=False)
        embed.add_field(name='Dealer', value=example['dealer_number'], inline=False)
        embed.add_field(name='Current Value',value = value['dealer_value'],inline=False)
        await channel.send(embed=embed)

        return example,value
    if change == 1:

        if value['player_value'] == 21:
            await channel.send('win')
            example['player_number'] = ''
            example['dealer_number'] = ''
            value['player_value'] = 0
            value['dealer_value'] = 0

        elif value['dealer_value'] == 21:
            await channel.send('lose')
            example['player_number'] = ''
            example['dealer_number'] = ''
            value['player_value'] = 0
            value['dealer_value'] = 0
        elif value['dealer_value'] >21:
            await channel.send('win')
            example['player_number'] = ''
            example['dealer_number'] = ''
            value['player_value'] = 0
            value['dealer_value'] = 0
                    
        elif value['player_value'] > 21:
            await channel.send('lose')
            example['player_number'] = ''
            example['dealer_number'] = ''
            value['player_value'] = 0
            value['dealer_value'] = 0
        elif value['dealer_value'] > value['player_value']:
            await channel.send('lose')
            example['player_number'] = ''
            example['dealer_number'] = ''
            value['player_value'] = 0
            value['dealer_value'] = 0
        elif value['dealer_value'] < value['player_value']:
            await channel.send('win')
            example['player_number'] = ''
            example['dealer_number'] = ''
            value['player_value'] = 0
            value['dealer_value'] = 0
        elif value['dealer_value'] == value['player_value']:
            await channel.send('draw')
            example['player_number'] = ''
            example['dealer_number'] = ''
            value['player_value'] = 0
            value['dealer_value'] = 0

bot.run('***')