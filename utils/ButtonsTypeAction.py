import discord
from functions.searsh_by_type import searsh_by_type

class ButtonsTypeAction(discord.ui.View):
    def __init__(self, interaction, criteria, embed):
        super().__init__()
        self.original_interaction = interaction 
        self.criteria = criteria
        self.embed = embed
        
    @discord.ui.button(label="Refresh", emoji="🔄", style=discord.ButtonStyle.blurple)
    async def refresh_button_callback(self, interaction: discord.Interaction, button: discord.ui.Button):

        await interaction.response.defer()

        token_address = "0xcc451977a4be9adee892f7e610fe3e3b3927b5a1"
        data = searsh_by_type(token_address, criteria=self.criteria)
        top_20_tokens = data["data"]["erc1155Tokens"]["results"][:5]

        # Limpia los campos actuales del embed
        self.embed.clear_fields()

        # Actualiza el embed con los nuevos datos
        for i in range(len(top_20_tokens)):
            token = top_20_tokens[i]
            min_price = int(token['minPrice']) / 10**18 if token['minPrice'] else "N/A"
            total_items = token['totalItems']
            price_str = f"{min_price:.2f} *RON*" if isinstance(min_price, (int, float)) else min_price
            self.embed.add_field(
                name=f"{token['name']}",
                value=(
                    f"Price: {price_str}\n"
                    f"Actual Supply: {total_items}\n"
                    f"Purchase of tokens on the [Market](https://marketplace.skymavis.com/collections/lumiterra/{token['tokenId']})\n\n `●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●`"
                ),
                inline=False
            )

        try: 
          await interaction.edit_original_response(embed=self.embed, view=ButtonsTypeAction(interaction, self.criteria, self.embed))
        except Exception as e:
          print(e)