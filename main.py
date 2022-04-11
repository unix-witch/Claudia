#!/bin/python3 -B
import os
import random
import discord
import gpt_2_simple as gpt2
from discord.ext import commands
from keep_alive import keep_alive
from collections import defaultdict

client = commands.Bot(command_prefix='ꙮ')
sess = gpt2.start_tf_sess()
gpt2.load_gpt2(sess, run_name='run1')
#gpt2.generate(sess)


channel_message_amounts = defaultdict(int)




@client.event
async def on_ready():
    print("Bot is running!")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    channel_id = message.channel.id
    channel_message_amounts[channel_id] += 1

    if channel_message_amounts[channel_id] > 3:
        print("sending message")

        
        bot_message = gpt2.generate(sess, return_as_list=True)[0]
        bot_message = bot_message.split('\n')

        #with open("message.txt", "w+") as f:
        #    f.write(bot_message)

        await message.channel.send(random.choice(bot_message))


keep_alive()
client.run('put your token here')
