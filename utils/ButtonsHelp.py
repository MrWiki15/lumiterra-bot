import discord

discord_url = "https://discord.com/invite/q3P5hjqsuE"
website_url = "https://lumiterra.net"
twitter_url = "https://x.com/lumiterragame"

class ButtonsHelp(discord.ui.View):

    def __init__(self):
        super().__init__()
        self.add_item(
            discord.ui.Button(label="Oficial Discord",
                              url=discord_url,
                              style=discord.ButtonStyle.url))
        self.add_item(
            discord.ui.Button(label="Oficial Twitter",
                              url=twitter_url,
                              style=discord.ButtonStyle.url))
        self.add_item(
            discord.ui.Button(label="Oficial Web",
                              url=website_url,
                              style=discord.ButtonStyle.url))
      