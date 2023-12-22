import discord
from discord.ext import commands

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)
slash = SlashCommand(bot, sync_commands=True)


@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")
    await bot.change_presence(activity=discord.Game(name="Hello World!"))


@bot.slash_command(
    name="hello",
    description="Greet with Hello!"
)
async def hello(ctx):
    await ctx.send("Hello!")


bot.run("YOUR_BOT_TOKEN")

