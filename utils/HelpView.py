import discord

polaris_discord_url = "https://discord.com/invite/YgQgEHqPyd"
discord_url = "https://discord.com/invite/q3P5hjqsuE"
website_url = "https://lumiterra.net"
docs_url = "https://docs.lumiterra.net/docs"


class HelpView(discord.ui.View):
    def __init__(self, *, timeout=180):
        super().__init__(timeout=timeout)
        self.add_item(
            discord.ui.Button(label="Discord Help",
                              url=polaris_discord_url,
                              style=discord.ButtonStyle.success))
        self.add_item(
            discord.ui.Button(label="Website",
                              url=website_url,
                              style=discord.ButtonStyle.url))
        self.add_item(
            discord.ui.Button(label="Documentation",
                              url=docs_url,
                              style=discord.ButtonStyle.url))

    @discord.ui.select(
        placeholder="Choose a command to get more information...",
        options=[
            discord.SelectOption(
                label="Help",
                description="Get detailed information about the bot"),
            
            discord.SelectOption(
                label="Guide",
                description="Get information on how to play the game"),
            
            discord.SelectOption(
                label="Download",
                description="Get information on how to download the game"),
            
            discord.SelectOption(
                label="Collection",
                description="Get information on the collection of the game"),
            
            discord.SelectOption(
                label="Analytics",
                description="Get information on analytics of the game"),
            
            #discord.SelectOption(
            #    label="Activity",
            #    description="Obtain information on gaming activity in the Marketplace."),
            
            discord.SelectOption(
                label="Searsh by name",
                description="Search for NFTs in Mavis Market by name."),
            
            discord.SelectOption(
                label="Searsh by type",
                description="Search for NFTs in Mavis Market by type."),
            
        ],
    )
    async def select_callback(self, interaction: discord.Interaction,
                              select: discord.ui.Select):
            
        if select.values[0] == "Help":
            embed = discord.Embed(
                title="🆘 Help",
                description=
                "Get detailed information about the bot.\n\n **Example of use: ** `{command}`\n\n**(** || `/help` || **)** ",
                color=discord.Color.green())
            embed.set_image(
                url=
                "https://dao.thlm.com/assets/img/game/Lumiterra-b.jpg"
            )

        elif select.values[0] == "Guide":
            embed = discord.Embed(
                title="📖 Guide",
                description=
                "Discover the three guides currently available in our bot. Gathering, Agriculture, Combat.\n\n**Example of use: ** `{command}`\n\n **(** || `/guide` || **)** ",
                color=discord.Color.blue())
            embed.set_image(
                url=
                "https://images.ctfassets.net/the2mlmvkyaw/2fO6oifvNBNUGbu83JfzYD/c0b9b0ffcb02de090a1799ee31e1e7fc/lumittera-poster.webp"
            )

        elif select.values[0] == "Download":
            embed = discord.Embed(
                title="📖 Download",
                description=
                "Find out what is the best way to download Lumiterra from your device.\n\n**Example of use: ** `{command}`\n\n **(** || `/download [platform]` || **)** ",
                color=discord.Color.blue())
            embed.set_image(
                url=
                "https://media.moddb.com/images/articles/1/318/317871/20230629-181044-oo.jpg"
            )

        elif select.values[0] == "Collection":
            embed = discord.Embed(
                title="📖 Collection",
                description=
                "Get updated on the latest statistics of the Lumiterra collection.\n\n**Example of use: ** `{command}`\n\n **(** || `/collection` || **)** ",
                color=discord.Color.blue())
            embed.set_image(
                url=
                "https://framerusercontent.com/images/2plT6RJkZqzBYdkruHtVlcRmUTY.png"
            )

        elif select.values[0] == "Analytics":
            embed = discord.Embed(
                title="📖 Analytics",
                description=
                "Enter the latest Analytics available.\n\n**Example of use: ** `{command} {type} {temporality}`\n\n **(** || `/analytics | type: Average price | temp: Last 24h` || **)** ",
                color=discord.Color.blue())
            embed.set_image(
                url=
                "https://img.freepik.com/vector-gratis/ilustracion-concepto-informe-datos_114360-864.jpg?size=626&ext=jpg"
            )
            
        #elif select.values[0] == "Activity":
        #    embed = discord.Embed(
        #        title="📖 News",
        #        description=
        #        "Discover the latest news about the world crypto.\n\n**Example of use: ** `{command}`\n\n **(** || `/news` || **)** ",
        #        color=discord.Color.blue())
        #    embed.set_image(
        #        url=
        #        "https://cusoft.tech/wp-content/uploads/2024/07/6f0b4fd6de0be2aa424373863d6c630e.jpeg"
        #    )
        #    
        elif select.values[0] == "Searsh by name":
            embed = discord.Embed(
                title="📖 Search by name",
                description=
                "Searsh any NFT by name in Mavis Market. \n\n**Example of use: ** `{command} {name}`\n\n **(** || `/searsh_by_name | name: slime ` || **)** ",
                color=discord.Color.blue())
            embed.set_image(
                url=
                "https://nfthorizon.io/wp-content/uploads/2023/05/20-05-news-file-1.jpg"
            )
            
        elif select.values[0] == "Searsh by type":
            embed = discord.Embed(
                title="📖 Search by type",
                description=
                "Searsh any NFT by type in Mavis Market. .\n\n**Example of use: ** `{command} {type}`\n\n **(** || `/searsh_by_type | type: consumable` || **)** ",
                color=discord.Color.blue())
            embed.set_image(
                url=
                "https://nfthorizon.io/wp-content/uploads/2023/05/20-05-news-file-1.jpg"
            )

        await interaction.response.send_message(embed=embed, ephemeral=True)