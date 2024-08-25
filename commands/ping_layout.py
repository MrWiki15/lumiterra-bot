import discord
from discord.ext import commands

async def ping_layout(interaction, latency):
  try:
    await interaction.response.send_message(f"{interaction.user.mention} {latency} ms / Pong!")
  except Exception as e:
    return e