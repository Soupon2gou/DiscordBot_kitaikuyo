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

#channel_id = "816220744471412748"

# ボットの設定
DISCORD_BOT_TOKEN = getenv("token")
intents = discord.Intents.all()
client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='!', intents=intents)

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

# yt_dlp
YTDL_FORMAT_OPTIONS = {
    "format": "bestaudio/best*[acodec=aac]",
    "outtmpl": "%(extractor)s-%(id)s-%(title)s.%(ext)s",
    "restrictfilenames": True,
    "noplaylist": True,
    "nocheckcertificate": True,
    "ignoreerrors": False,
    "logtostderr": False,
    "quiet": True,
    "no_warnings": True,
    "default_search": "auto",
    "source_address": "0.0.0.0"  # bind to ipv4 since ipv6 addresses cause issues sometimes
}

# https://stackoverflow.com/questions/58892635/discord-py-and-youtube-dl-read-error-and-the-session-has-been-invalidated-fo
FFMPEG_OPTIONS = {
    "before_options": "-reconnect 1 -reconnect_streamed 1 -reconnect_at_eof 1 -reconnect_delay_max 5",
    "options": "-vn"
}

# https://qiita.com/sizumita/items/cafd00fe3e114d834ce3
# Suppress noise about console usage from errors
yt_dlp.utils.bug_reports_message = lambda: ""

ytdl = yt_dlp.YoutubeDL(YTDL_FORMAT_OPTIONS)

#マンボウ鯖のID
MANBOU_GUILD_ID = 814777045841084416
#ソウポン鯖のID
SOUPON_GUILD_ID = 816220744010301453

#ソウポン鯖ステッカー・スタンプのチャンネルID
STAMP_CHANNEL_ID = 880790745747959838

#マンボウ鯖ぼざろのチャンネルID
BOZARO_CHANNEL_ID = 814777045841084416

#bot起動時に実行される関数
#@bot.event
#async def on_ready():
#    print(f"We have logged in as {bot.user}")
#    await bot.change_presence(activity=discord.Game(name="結束バンド"))
# Bot起動時に実行される関数
@bot.event
async def on_ready():
    now_time = datetime.datetime.utcnow() + datetime.timedelta(hours=9)
    await bot.change_presence(activity=discord.Game(name="結束バンド"))

    time.sleep(5)

    await bot.change_presence(activity=discord.Game(name=f'{now_time.strftime("%H:%M:%S")}にいくよ～！'))




@bot.command()
async def manbou(ctx):
    for _ in range(message_count):
       await ctx.send('まんぼうはきもい')
       await asyncio.sleep(1)  # メッセージ間の遅延（秒）
       
@bot.command()
async def wahaya(ctx):
    for _ in range(message_count):
       await ctx.send('マンボウさん気持ち悪いのね～！')
       await asyncio.sleep(1)  # メッセージ間の遅延（秒）

message_content = "キタキタ～ン！"
message_count = 1 # 送信するメッセージの数
@bot.command()
async def kita(ctx):
    # 指定されたチャンネルを取得
    #channel = client.get_channel(int(channel_id))
    # メッセージを送信する
    for _ in range(message_count):
        await ctx.send(message_content)
        await asyncio.sleep(1)  # メッセージ間の遅延（秒）

# チーバくんの、なのはな体操
@bot.command()
async def yare(ctx):
    await ctx.channel.send("https://www.youtube.com/watch?v=JV3KOJ_Z4Vs")

# おもしろ画像を送信
@bot.command(aliases=["omosiro", "www"])
async def stamp(ctx):
    guild = bot.get_guild(SOUPON_GUILD_ID)

    channel = guild.get_channel(STAMP_CHANNEL_ID)

    stamp_channel_messages = [message async for message in channel.history(limit=None)]

    random_stamp = random.choice(stamp_channel_messages)

    content = random_stamp.attachments[0].url if random_stamp.content == "" else random_stamp.content

    # メッセージが送られてきたチャンネルに送る
    await ctx.channel.send(content)

#ぼざろ画像を送信
@bot.command(aliases=["bozaro"])
async def bozaro_stamp(ctx):
    guild = bot.get_guild(MANBOU_GUILD_ID)

    channel = guild.get_channel(BOZARO_CHANNEL_ID)

    bozaro_channel_messages = [message async for message in channel.history(limit=None)]

    random_bozaro = random.choice(bozaro_channel_messages)

    content = random_bozaro.attachments[0].url if random_bozaro.content == "" else random_bozaro.content

    # メッセージが送られてきたチャンネルに送る
    await ctx.channel.send(content)

# ゆるゆりを送信
@bot.command()
async def yuruyuri(ctx):
    tweets = twapi.search_tweets(q="from:@Generative_Ex", count=1)
    #print(tweets)
    for tweet in tweets:
        media = tweet.entities["urls"]
        #print(media)
        for m in media:
            origin = m["url"]
            print(origin)
            await ctx.channel.send(origin)

# ボットを実行
bot.run(DISCORD_BOT_TOKEN)

