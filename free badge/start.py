import discord
from discord.ext import commands
from discord import app_commands
from discord.ui import Button, View
import os


print("-------------- Active developer badge bot -----------------")
print("[1] | create badge bot")
print("[2] | help")
i1 = input()
if i1 == "1":
    print("paste bot token here")
    token = input()

if i1 == "2":
    print("To get badge paste your bot token from discord developer portal open discord and use command /givemebadge on your serwer.")
    token = input()

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.messages = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print("[badge bot] : ok your bot is ready now you only must open discord and use bot command: '/givemebadge' ")
    await bot.change_presence(activity=discord.Game(name="active developer badge bot!"))
    await bot.change_presence(status=discord.Status.idle)

@bot.tree.command(name="givemebadge")
async def givemebadge(interaction: discord.Interaction):
    button = Button(label="help",style=discord.ButtonStyle.green,emoji="🏓")
    async def button_po(interaction2):
        channel = interaction.channel
        await channel.send(f"to get badge wait 24 hours and get it on discord developer portal")
    button.callback = button_po
    view = View()
    view.add_item(button)
    embed = discord.Embed(title="badge", description=f"all is ready, to get badge wait 24 hours and get it on discord developer portal ",colour=discord.Colour.random())
    await interaction.response.send_message(embed=embed,view=view)

@bot.tree.command(name="givebadge")
async def givebadge(interaction: discord.Interaction):
    button = Button(label="help",style=discord.ButtonStyle.green,emoji="🏓")
    async def button_po(interaction2):
        channel = interaction.channel
        await channel.send(f"to get badge wait 24 hours and get it on discord developer portal")
    button.callback = button_po
    view = View()
    view.add_item(button)
    embed = discord.Embed(title="badge", description=f"to get badge wait 24 hours and get it on discord developer portal",colour=discord.Colour.random())
    await interaction.response.send_message(embed=embed,view=view)

bot.run(token)
