import discord
from discord.ext import commands
separtor = "●▬▬▬⛏️🚧🗡️▬▬▬●"
separtor_2 = "`●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●`"

async def download_layout(interaction, platform):
  try:
    await interaction.response.defer(ephemeral=True)
    
    if platform == "How to play in WINDOWS":
      embed = discord.Embed(
        title=f"{platform} Lumiterra", 
        description=f"Below you will find a list of detailed steps to play Lumiterra on Windows computers without any problems."
      )
      
      embed.add_field(
        name=" ",
        value=f"{separtor_2}",
        inline=False
      )
      
      embed.add_field(
        name="Step 1",
        value=f"Go to your browser and go to the [itch.io](https://itch.io/).",
        inline=False
      )
      
      embed.add_field(name="", value=f"{separtor_2}", inline=False)
      
      embed.add_field(
        name="Step 2",
        value=f"Enter `Lumiterra` in the navigation bar above || - (You can find it by looking for the following emoji 🔍) - ||",
        inline=False
      )
      
      embed.add_field(name="", value=f"{separtor_2}", inline=False)
      
      embed.add_field(
        name="Step 3",
        value=f"Enter *Double click on the first search result*, make sure the category of the result that appears is `Adventure` and has more than **160 reviews.**",
        inline=False
      )
      
      embed.add_field(name="", value=f"{separtor_2}", inline=False)
      
      embed.add_field(
        name="Step 4",
        value=f"This will redirect you to [lumiterra.itch.io](https://lumiterra.itch.io/game), once you are there look for the download button, in red at the bottom of the page and press it.",
        inline=False
      )
      
      embed.add_field(name="", value=f"{separtor_2}", inline=False)
      
      embed.add_field(
        name="Step 5",
        value=f"Once the download is complete, run the file and you will be prompted to download approximately 1GB of content. Once the download is complete, run the file and  **Welcome to Lumiterra.**",
        inline=False
      )
      
      embed.set_image(
        url="https://cusoft.tech/wp-content/uploads/2024/08/image-removebg-preview-23.jpg"
      )
      
      embed.color = 0xb2c863
    
      await interaction.followup.send(embed=embed, ephemeral=True)
  
    if platform == "How to play in LINUX":
      embed = discord.Embed(
        title=f"{platform} Lumiterra", 
        description=f"Below you will find a list of detailed steps to play Lumiterra on Linux computers without any problems."
      )
      
      embed.add_field(
        name=" ",
        value=f"{separtor_2}",
        inline=False
      )
      
      embed.add_field(
        name=f"Step 1", 
        value=f"Go to [itch.io](https://itch.io) and download the executable .exe file."
      )
      
      embed.add_field(
        name=" ",
        value=f"{separtor_2}",
        inline=False
      )
      
      embed.add_field(
        name=f"Step 2", 
        value=f"Once you have downloaded the executable, you must install Wine, which is a compatibility layer that allows you to run Windows applications on Linux. To do so, run the following command: \n\n ` sudo apt install wine `"
      )
      
      embed.add_field(
        name=" ",
        value=f"{separtor_2}",
        inline=False
      )
      
      embed.add_field(
        name=f"Step 3", 
        value=f"Run the game .exe file with Wine: \n\n ` wine lumiterra.exe `"
      )
      
      embed.set_image(
        url="https://cusoft.tech/wp-content/uploads/2024/08/image-removebg-preview-23.jpg"
      )
      
      embed.color = 0xb2c863
      await interaction.followup.send(embed=embed, ephemeral=True)
  
    if platform == "How to play in MAC":
      embed = discord.Embed(
        title=f"{platform} Lumiterra", 
        description=f"Below you will find a list of detailed steps to play Lumiterra on Mac computers without any problems."
      )
      
      embed.add_field(
        name=" ",
        value=f"{separtor_2}",
        inline=False
      )
      
      embed.add_field(
        name="Step 1",
        value=f"Go to your browser and go to the [itch.io](https://itch.io/).",
        inline=False
      )
      
      embed.add_field(name="", value=f"{separtor_2}", inline=False)
      
      embed.add_field(
        name="Step 2",
        value=f"Enter `Lumiterra` in the navigation bar above || - (You can find it by looking for the following emoji 🔍) - ||",
        inline=False
      )
      
      embed.add_field(name="", value=f"{separtor_2}", inline=False)
      
      embed.add_field(
        name="Step 3",
        value=f"Enter *Double click on the first search result*, make sure the category of the result that appears is `Adventure` and has more than **160 reviews.**",
        inline=False
      )
      
      embed.add_field(name="", value=f"{separtor_2}", inline=False)
      
      embed.add_field(
        name="Step 4",
        value=f"This will redirect you to [lumiterra.itch.io](https://lumiterra.itch.io/game), once you are there look for the download button, in red at the bottom of the page and press it.",
        inline=False
      )
      
      embed.add_field(name="", value=f"{separtor_2}", inline=False)
      
      embed.add_field(
        name="Step 5",
        value=f"Once the download is complete, run the file and you will be prompted to download approximately 1GB of content. Once the download is complete, run the file and  **Welcome to Lumiterra.**",
        inline=False
      )
      
      embed.set_image(
        url="https://cusoft.tech/wp-content/uploads/2024/08/image-removebg-preview-23.jpg"
      )
      embed.color = 0xb2c863
      await interaction.followup.send(embed=embed, ephemeral=True)
  
    if platform == "How to play in ANDROID":
      embed = discord.Embed(
        title=f"{platform} Lumiterra", 
        description=f"Below you will find a list of detailed steps to play Lumiterra on Android computers without any problems."
      )
      
      embed.add_field(
        name=" ",
        value=f"{separtor_2}",
        inline=False
      )
      
      embed.add_field(
        name="Step 1",
        value=f"Go to your browser and go to the [itch.io](https://itch.io/).",
        inline=False
      )
      
      embed.add_field(name="", value=f"{separtor_2}", inline=False)
      
      embed.add_field(
        name="Step 2",
        value=f"Enter `Lumiterra` in the navigation bar above || - (You can find it by looking for the following emoji 🔍) - ||",
        inline=False
      )
      
      embed.add_field(name="", value=f"{separtor_2}", inline=False)
      
      embed.add_field(
        name="Step 3",
        value=f"Enter *Double click on the first search result*, make sure the category of the result that appears is `Adventure` and has more than **160 reviews.**",
        inline=False
      )
      
      embed.add_field(name="", value=f"{separtor_2}", inline=False)
      
      embed.add_field(
        name="Step 4",
        value=f"This will redirect you to [lumiterra.itch.io](https://lumiterra.itch.io/game), once you are there look for the download button, in red at the bottom of the page and press it.",
        inline=False
      )
      
      embed.add_field(name="", value=f"{separtor_2}", inline=False)
      
      embed.add_field(
        name="Step 5",
        value=f"Once the download is complete, run the file and you will be prompted to download approximately 1GB of content. Once the download is complete, run the file and  **Welcome to Lumiterra.**",
        inline=False
      )
      
      embed.set_image(
        url="https://cusoft.tech/wp-content/uploads/2024/08/image-removebg-preview-24.jpg"
      )
      embed.color = 0xb2c863
      await interaction.followup.send(embed=embed, ephemeral=True)
  
  except Exception as e:
    return e