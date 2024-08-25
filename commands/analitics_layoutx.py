import discord
from discord.ext import commands

# functions
from functions.get_analytics import get_analytics
from commands.analitics_layout.layout import layout

separtor = "●▬▬▬⛏️🚧🗡️▬▬▬●"
separtor_2 = "`●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●`"

#command
async def analitics_layout(interaction, type, temp):
  try:
    await interaction.response.defer()
    data = get_analytics("0xcc451977a4be9adee892f7e610fe3e3b3927b5a1")
    await layout(data, type, temp, interaction)
  except Exception as e:
    print(f"Error in command analitics_layout:")
    print(e)
    return e

