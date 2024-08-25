import discord
separtor = "●▬▬▬▬▬▬▬▬▬▬▬▬●"
separtor_2 = "`●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●`"

async def how_to_play_game(interaction, url):
  try:
    embed = discord.Embed(
      title=f"Reed this Article",
      description=f"[URL -> Click to open]({url})",
      color=0xb2c863,
    )
    
    embed.set_image(
      url=f"https://cusoft.tech/wp-content/uploads/2024/08/image-removebg-preview-24.jpg"
    )
  
    await interaction.followup.send(embed=embed, ephemeral=True)
    
  except Exception as e: 
    print(e)
    return(e)
  