import discord
from discord.ext import commands

# functions
from functions.searsh_by_type import searsh_by_type

# utils
from utils.ButtonsTypeAction import ButtonsTypeAction
separtor = "●▬▬▬⛏️🚧🗡️▬▬▬●"
separtor_2 = "`●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●`"

# command
async def searsh_by_type_layout(interaction, type):
    try:
        await interaction.response.defer(ephemeral=True)

        token_address = "0xcc451977a4be9adee892f7e610fe3e3b3927b5a1"
        criteria = [
            {
                "name": "type",
                "values": [type]  # type es un string
            }
        ]

        data = searsh_by_type(token_address, criteria=criteria)
        top_20_tokens = data["data"]["erc1155Tokens"]["results"]

        embed = discord.Embed(
            title=f"🔎 Results for {type}",
            description=separtor,
            color=0xb2c863,
        )

        for i in range(10):
            token = top_20_tokens[i]
            min_price = int(token['minPrice']) / 10**18 if token['minPrice'] else "N/A"
            total_items = token['totalItems']

            price_str = f"{min_price:.2f} *RON*" if isinstance(min_price, (int, float)) else min_price
            embed.add_field(
                name=f"{token['name']}",
                value=(
                    f"Price: {price_str}\n"
                    f"Actual Supply: {total_items}\n Purchase of tokens on the [Market](https://marketplace.skymavis.com/collections/lumiterra/{token['tokenId']})\n\n {separtor_2}"
                ),
                inline=False
            )

        embed.set_thumbnail(url=top_20_tokens[0]["image"])

        await interaction.followup.send(embed=embed, ephemeral=True, view=ButtonsTypeAction(interaction, criteria, embed))
    except Exception as e:
        print(f"Error in command searsh_by_type_layout:")
        print(e)
        return e
