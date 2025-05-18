# bot.py

import discord
from discord.ext import commands, tasks
from config import DISCORD_TOKEN, CHANNEL_ID, TARGET_URL, CHECK_INTERVAL
from checker import check_sales

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    sale_alert.start()

@tasks.loop(minutes=CHECK_INTERVAL)
async def sale_alert():
    channel = bot.get_channel(CHANNEL_ID)
    if not channel:
        print("Channel not found.")
        return

    sales = check_sales(TARGET_URL)
    if sales:
        await channel.send("🛍️ New Sale Items:\n" + "\n".join(sales))
    else:
        print("No sale items found.")

bot.run(DISCORD_TOKEN)
