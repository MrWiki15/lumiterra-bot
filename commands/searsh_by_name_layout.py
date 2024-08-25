import discord
from discord.ext import commands

# functions
from functions.searsh_by_name import searsh_by_name

#utils
from utils.ButtonsSearshAction import ButtonsSearshAction
separtor = "●▬▬▬⛏️🚧🗡️▬▬▬●"
separtor_2 = "`●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●`"

#command
async def searsh_by_name_layout(interaction, name):
  try:
    await interaction.response.defer(ephemeral=True)
    
    data = searsh_by_name(name)
    top_20_tokens = data["data"]["erc1155Tokens"]["results"]
    
    embed = discord.Embed(
      title=f"🔎 Results for {name}",
      description=separtor,
      color=0xb2c863,
    )
    
    for i in range(min(20, len(top_20_tokens))):
      token = top_20_tokens[i]
      min_price = int(token['minPrice']) / 10**18 if token['minPrice'] else "N/A"
      total_items = token['totalItems']
      
      price_str = f"{min_price:.2f} *RON*" if isinstance(min_price, (int, float)) else min_price
      embed.add_field(
          name=f"{token['name']}",
          value=(
              f"Price: {price_str}\n"
              f"Actual Supply: {total_items}\n Purchase of tokens on the [Market](https://marketplace.skymavis.com/collections/lumiterra/{token["tokenId"]})\n\n {separtor_2}"
          ),
          inline=False
      )
    
    embed.set_thumbnail(url=data["data"]["erc1155Tokens"]["results"][0]["image"])
    
    await interaction.followup.send(embed=embed, ephemeral=True, view=ButtonsSearshAction(interaction, name, embed))
  except Exception as e:
    print(f"Error in command searsh_by_name_layout:")
    print(e)
    return e

