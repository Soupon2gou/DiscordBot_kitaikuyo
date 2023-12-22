# -*- coding: utf-8 -*-
import asyncio
import datetime
import glob
# import MeCab
from ntpath import join
import os
import random
# import sys
import time
import typing
from os import getenv

import discord
import requests
import tweepy
import yt_dlp
from PIL import Image, ImageFont, ImageDraw
from discord.ext import commands
from googleapiclient.discovery import build
from niconico import NicoNico
from spotdl import Spotdl


token = "MTExNTE3ODg3NjIzOTM0Nzc0NA.GWXlm-.7oapHLYww1UH2i6nJVi2ic3I9Pr8gI9jLAQADc"
message_content = "キタキタ～ン"
#channel_id = "816220744471412748"
message_count = 1 # 送信するメッセージの数

intents = discord.Intents.all()
client = discord.Client(intents=intents)

# Tweepy
#print(os.getenv("CONSUMER_KEY"))
os.environ['CONSUMER_KEY'] = 'OG9fUU5aQVRmanBDOFU0UC1tdkE6MTpjaQ'
os.environ['CONSUMER_SECRET'] = 'qTMBfsCew5S6DqhH9JmcDY9p97VnWkZS917r6T3aktZ7VAXS8f'
os.environ['ACCESS_TOKEN_KEY'] = '1051379902098812928-0Eav7gi4dc9XmAuQefiBJlF1t0l9Gu'
os.environ['ACCESS_TOKEN_SECRET'] = '8rsaq7hOcnpobfuX4GX6AVWT0tcyHowQbjPaaUw2g8cj3'
TWITTER_CONSUMER_KEY = getenv("CONSUMER_KEY")
TWITTER_CONSUMER_SECRET = getenv("CONSUMER_SECRET")
TWITTER_ACCESS_TOKEN_KEY = getenv("ACCESS_TOKEN_KEY")
TWITTER_ACCESS_TOKEN_SECRET = getenv("ACCESS_TOKEN_SECRET")

key = os.getenv("CONSUMER_KEY")
if key:
    print("環境変数が見つかった場合の処理")
if not key:
    print("環境変数が見つからない場合の処理")

twauth = tweepy.OAuthHandler(TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET)
twauth.set_access_token(TWITTER_ACCESS_TOKEN_KEY, TWITTER_ACCESS_TOKEN_SECRET)
twapi = tweepy.API(twauth)


# ボットの設定
bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")
    await bot.change_presence(activity=discord.Game(name="結束バンド"))




@bot.command()
async def manbou(ctx):
    for _ in range(message_count):
       await ctx.send('まんぼうはきもい')
       await asyncio.sleep(1)  # メッセージ間の遅延（秒）

@bot.command()
async def kita(ctx):
    # 指定されたチャンネルを取得
    #channel = client.get_channel(int(channel_id))
    # メッセージを送信する
    for _ in range(message_count):
        await ctx.send(message_content)
        await asyncio.sleep(1)  # メッセージ間の遅延（秒）

# ゆるゆりを送信
@bot.command()
async def yuruyuri(ctx):
    tweets = twapi.search_tweets(q="from:@YuruYuriBot1", tweet_mode="extended", include_entities=True, count=1)
    for tweet in tweets:
        media = tweet.entities["media"]
        for m in media:
            origin = m["media_url"]
            await ctx.channel.send(origin)



# ボットを実行
bot.run(token)

