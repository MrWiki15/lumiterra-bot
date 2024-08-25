import discord
from functions.searsh_by_name import searsh_by_name

class ButtonsSearshAction(discord.ui.View):
    def __init__(self, interaction, name, embed):
        super().__init__()
        self.original_interaction = interaction 
        self.name = name
        self.embed = embed
        
    @discord.ui.button(label="Refresh", emoji="🔄", style=discord.ButtonStyle.blurple)
    async def refresh_button_callback(self, interaction: discord.Interaction, button: discord.ui.Button):

        await interaction.response.defer()

        # Llama a la función para obtener los nuevos datos
        data = searsh_by_name(self.name)
        top_20_tokens = data["data"]["erc1155Tokens"]["results"][:5]

        # Limpia los campos actuales del embed
        self.embed.clear_fields()

        # Actualiza el embed con los nuevos datos
        for i in range(min(20, len(top_20_tokens))):
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
          await interaction.edit_original_response(embed=self.embed, view=ButtonsSearshAction(interaction, self.name, self.embed))
        except Exception as e:
          print(e)