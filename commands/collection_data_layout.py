import discord
from discord.ext import commands

# functions
from functions.get_collection_data import get_collection_data
from functions.get_erc1155_token_list import get_erc1155_token_list

#utils
from utils.ButtonsHelp import ButtonsHelp
separtor = "●▬▬▬▬▬▬▬⛏️🚧🗡️▬▬▬▬▬▬▬●"

#command
async def collection_data_layout(interaction):
  try:
    await interaction.response.defer()
    
    data = get_collection_data("0xcc451977a4be9adee892f7e610fe3e3b3927b5a1")
    token_list = get_erc1155_token_list("0xcc451977a4be9adee892f7e610fe3e3b3927b5a1")
    top_5_tokens = token_list["data"]["erc1155Tokens"]["results"][:5]
    
    embed = discord.Embed(
      title=f"{data["data"]["tokenData"]["collectionMetadata"]["collection_name"]}",
      description=separtor,
      color=0xb2c863,
    )
    
    
    embed.add_field(
      name="📜 Description",
      value=f"\nMultiplayer, open-world survival crafting game where you can battle, farm with your friends or mysterious collected creatures in a vast world! \n\n {separtor}",
      inline=False
    )
    
    embed.add_field(
      name="🛒 Market Data",
      value="",
      inline=False
    )
    
    embed.add_field(
      name="TOTAL VOLUME",
      value=f"`{float(data['data']['tokenData']['volumeAllTime']):.2f}` *RON*",
      inline=True
    )
    
    embed.add_field(
      name="TOTAL SUPPLY",
      value=f"`{data['data']['tokenData']['totalItems']}` *Items*",
      inline=True
    )
    
    embed.add_field(
      name="FLOOR PRICE",
      value=f"`{int(data['data']['tokenData']['minPrice']) / 10 ** 18}` *RON*",
      inline=True
    )
    
    embed.add_field(
      name=" ",
      value=f"{separtor}",
      inline=False
    )
    
    embed.add_field(
      name="📉 Top 5 Cheapest Tokens on the Market",
      value=f"",
      inline=False
    )
    
    for i in range(5):
      embed.add_field(
        name=f"{top_5_tokens[i]['name']}",
        value=f"**Price:**  || - ` {int(top_5_tokens[i]['minPrice']) / 10 ** 18} `  *RON* - ||",
        inline=False
      )
    
    embed.set_image(
      url=data["data"]["tokenData"]["collectionMetadata"]["banner"]
    )
    
    await interaction.followup.send(embed=embed, view=ButtonsHelp())
  except Exception as e:
    print(e)
    return e

