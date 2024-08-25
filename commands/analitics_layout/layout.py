import discord

# functions
from functions.generate_graph import generate_graph

async def layout(data, chart_type, temp_key, interaction):
    try:
        # Generar el gráfico basado en los datos
        chart_buf = generate_graph(data, chart_type, temp_key)

        # Crear el embed
        embed = discord.Embed(title=f'{chart_type} Analysis', description=f'Temporality: {temp_key}', color=0x00ff00)
        embed.set_image(url="attachment://chart.png")

        # Enviar el embed con el gráfico
        file = discord.File(fp=chart_buf, filename="chart.png")
        await interaction.followup.send(embed=embed, file=file)
    except KeyError as e:
        raise ValueError(f"Error accessing data for {chart_type} and temporality {temp_key}: {e}")
    except Exception as e:
        print(f"Unexpected error in layout: {e}")
        raise e

