import discord
from discord.ext import commands
from discord import app_commands
import asyncio
import datetime
import requests

#data
from data.types import types
from data.platforms import platforms
from data.branches import branches
from data.analitics import analitics_autocomplete

#config
from config.constants import BOT_TOKEN

#utils
from utils.on_command_error import on_command_error
from utils.ButtonsHelp import ButtonsHelp
from utils.HelpView import HelpView

#commands
from commands.download_layout import download_layout
from commands.guide_layout import guide_layout
from commands.ping_layout import ping_layout
from commands.collection_data_layout import collection_data_layout
from commands.searsh_by_name_layout import searsh_by_name_layout
from commands.searsh_by_type_layout import searsh_by_type_layout
from commands.analitics_layoutx import analitics_layout

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.reactions = True
bot = commands.Bot(command_prefix='/', intents=intents)

#variables
footer_image_url = "https://cusoft.tech/wp-content/uploads/2024/07/imagen_2024-07-17_224059345-removebg-preview.png"
footer_text = "by: Qsoft Development Team"

@bot.event
async def on_ready():
    print("Bot is Up and Ready!")
    try:
        synced = await bot.tree.sync()
        print(f'{bot.user} se ha conectado a Discord!')
    except Exception as e:
        print(e)

# message error 
async def error_message(e, interaction, msg):
    try: 
        embed = discord.Embed(
            title="We had a problem ⚠️",
            description=f"An error occurred while executing the 😢 command. Don't worry, it's not your fault, we are working to fix the problem as soon as possible ⚒️."
        )
        
        embed.add_field(
            name=" ",
            value="●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●",
            inline=False)
        
        embed.add_field(
            name="Error description: ",
            value=f"{msg}",
            inline=False)
        
        embed.add_field(
            name=" ",
            value="●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●",
            inline=False)
        
        embed.set_image(
                url="https://nftplazas.com/wp-content/uploads/2024/06/lumittera-gameplay.png"
            )
        
        embed.color = 0x0fffff
        await interaction.response.send_message(embed=embed, ephemeral=True, view=ButtonsHelp())
        print(f"Este es el error: {str(e)}")
        
    except Exception as e:
        print(f"Ocurrio un error al enviar el mensaje de error: {str(e)}")















@bot.tree.command(name="ping", 
                  description="Ping the bot")
async def ping_command(interaction: discord.Interaction):
  try:
    await ping_layout(interaction, round(bot.latency * 1000))
  except Exception as e:
      await error_message(e,
                          interaction,
                          f"Command ping [{e}]")










@bot.tree.command(name="guide", 
                  description="Select a branch and become a master in Lumiterra.")
@app_commands.describe(type="Select the type of guide")
@app_commands.describe(section="Select a section of the guide.")
async def guide_command(interaction: discord.Interaction, type: str, section: str):
  try:
    await guide_layout(interaction, type, section)
  except Exception as e:
      await error_message(e,
                          interaction,
                          f"Command ping [{e}]")
      
@guide_command.autocomplete('type')
async def type_autocomplete(interaction: discord.Interaction, current: str):
    choices = [app_commands.Choice(name=branch, value=branch) for branch in branches.keys()]
    return choices[:25]  # Limit to 25 options

@guide_command.autocomplete('section')
async def section_autocomplete(interaction: discord.Interaction, current: str):

    selected_type = interaction.namespace.type
    if selected_type in branches:
        sections = branches[selected_type]
        choices = [
            app_commands.Choice(name=section, value=section) 
            for section in sections 
            if current.lower() in section.lower()
        ]
        return choices[:25]  # Limit to 25 options
    return []










@bot.tree.command(name="analitics", 
                  description="Real time graphics.")
@app_commands.describe(type="Select the type of analitics")
@app_commands.describe(temp="Select the temporality of the graph.")
async def analitics_command(interaction: discord.Interaction, type: str, temp: str):
  try:
    await analitics_layout(interaction, type, temp)
  except Exception as e:
      await error_message(e,
                          interaction,
                          f"Command ping [{e}]")
      
@analitics_command.autocomplete('type')
async def type_autocomplete(interaction: discord.Interaction, current: str):
    choices = [app_commands.Choice(name=branch, value=branch) for branch in analitics_autocomplete.keys()]
    return choices[:25]  # Limit to 25 options

@analitics_command.autocomplete('temp')
async def temp_autocomplete(interaction: discord.Interaction, current: str):

    selected_type = interaction.namespace.type
    if selected_type in analitics_autocomplete:
        temps = analitics_autocomplete[selected_type]
        choices = [
            app_commands.Choice(name=temp, value=temp)
            for temp in temps 
            if current.lower() in temp.lower()
        ]
        return choices[:25]  # Limit to 25 options
    return []















@bot.tree.command(name="download",
                  description="Download the Lumiterra game")
@app_commands.describe(platform="Select the platform of the game")
async def download_command(interaction: discord.Interaction, platform: str):
  try:
    await download_layout(interaction, platform)
  except Exception as e:
      await error_message(e,
                          interaction,
                          f"Command download [{e}]")

@download_command.autocomplete("platform")
async def platform_autocomplete(interaction: discord.Interaction, current: str):
    platforms_for = [
        app_commands.Choice(name=platform_name, value=platform_name) 
        for platform_name in platforms 
        if current.lower() in platform_name.lower() 
    ]
    return platforms_for[:25]









@bot.tree.command(name="collection",
                  description="Get the collection data")
async def collection_command(interaction: discord.Interaction):
  try:
    await collection_data_layout(interaction)
  except Exception as e:
      await error_message(e,
                          interaction,
                          f"Command collection [{e}]")
  
  
  
  
  
  
  
  
  
  
  
  
  
@bot.tree.command(name="search_by_name",
                  description="Search by name")
@app_commands.describe(name="The name of the token")
async def search_by_name_command(interaction: discord.Interaction, name: str):
  try:
    await searsh_by_name_layout(interaction, name)
  except Exception as e:
      await error_message(e,
                          interaction,
                          f"Command search_by_name [{e}]")
  
  
  
  
  
  
  
  
  
  
  
  
  
  
@bot.tree.command(name="search_by_type",
                  description="Search by type")
@app_commands.describe(type="The type of the token")
async def search_by_name_command(interaction: discord.Interaction, type: str):
  try:
    await searsh_by_type_layout(interaction, type)
  except Exception as e:
      await error_message(e,
                          interaction,
                          f"Command search_by_type [{e}]")     

@search_by_name_command.autocomplete("type")
async def token_autocomplete(interaction: discord.Interaction, current: str):
    types_for = [
        app_commands.Choice(name=type_name, value=type_name) 
        for type_name in types 
        if current.lower() in type_name.lower() 
    ]
    return types_for[:25]  
















@bot.tree.command(name="help",
    description="Get information about the current commands")
async def market(interaction: discord.Interaction):
    try:
        embed = discord.Embed(
            title="**Lumiterra Market** ( V1.0 )",
            description=
            f"Choose an option from the list to display information about the commands and features of the Lumiterra Market\n\n||Currently our bot is in the `V1.0` phase, if you find any error in the execution of the commands, we appreciate that you communicate the issue to the support channel within our server ||\n\n**Many thanks** for using the Polaris services  (ɔ◔‿◔)ɔ ♥ ",
            color=discord.Color.blue())
        embed.set_image(
            url=
            "https://pbs.twimg.com/media/GSHbkfUaEAApj0v.jpg"
        )
        embed.set_footer(
                text=footer_text,
                icon_url=footer_image_url
            )
        await interaction.response.send_message(embed=embed,
                                                view=HelpView(),
                                                ephemeral=True)
    except Exception as e:
        await error_message(e, 
                            interaction,
                            msg=f"Command help [{e}]")




bot.run(BOT_TOKEN)
