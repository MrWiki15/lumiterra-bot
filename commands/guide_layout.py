import discord
from discord.ext import commands
separtor = "●▬▬▬▬▬▬▬▬▬▬▬▬●"
separtor_2 = "`●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●`"

from commands.guid_layout.how_to_play_game import how_to_play_game 

async def guide_layout(interaction, type, section):
  try:
    await interaction.response.defer(ephemeral=True)
    
    if type == "Game Tutorial":
      if section == "How to Play the Game?":
        await how_to_play_game(interaction=interaction, url="https://lumiterra.notion.site/LumiTerra-Game-Guide-ff7923da552242139c9e44bbec4df8e4?p=41330faf5a014f4988d0778efee58d13&pm=s")
      
      if section == "Beginner's Village":
        await how_to_play_game(interaction=interaction, url="https://lumiterra.notion.site/LumiTerra-Game-Guide-ff7923da552242139c9e44bbec4df8e4?p=963f054eb3b54e6d8c19a286cc80e94d&pm=s#85619eb64f5944c59d810748131f506b")
      
      if section == "Talent Profession NPC":
        await how_to_play_game(interaction=interaction, url="https://lumiterra.notion.site/LumiTerra-Game-Guide-ff7923da552242139c9e44bbec4df8e4?p=f54f8ade049e42709df8aef66a955a53&pm=s")
      
      if section == "Energy System":
        await how_to_play_game(interaction=interaction, url="https://lumiterra.notion.site/LumiTerra-Game-Guide-ff7923da552242139c9e44bbec4df8e4?p=29fc9982123c4352a95fc8badecf1919&pm=s")
      
      if section == "Ability Level":
        await how_to_play_game(interaction=interaction, url="https://lumiterra.notion.site/LumiTerra-Game-Guide-ff7923da552242139c9e44bbec4df8e4?p=e8cd8a7309bd4f588bcb6657d057455e&pm=s")
      
      if section == "Drop rate":
        await how_to_play_game(interaction=interaction, url="https://lumiterra.notion.site/LumiTerra-Game-Guide-ff7923da552242139c9e44bbec4df8e4?p=665bce78a37047208b867bedaf06feee&pm=s")
      
      if section == "Backpack":
        await how_to_play_game(interaction=interaction, url="https://lumiterra.notion.site/LumiTerra-Game-Guide-ff7923da552242139c9e44bbec4df8e4?p=ad0284afd016413d8a69306af7208697&pm=s")
      
      if section == "Packaging boxes":
        await how_to_play_game(interaction=interaction, url="https://lumiterra.notion.site/LumiTerra-Game-Guide-ff7923da552242139c9e44bbec4df8e4?p=de4c9146d3a14509a1324e36a50080e4&pm=s")
      
      if section == "Equipment Disassembling":
        await how_to_play_game(interaction=interaction, url="https://lumiterra.notion.site/LumiTerra-Game-Guide-ff7923da552242139c9e44bbec4df8e4?p=394d6be8849848f590b2024d59bef8ff&pm=s")
      
      if section == "Pet system":
        await how_to_play_game(interaction=interaction, url="https://lumiterra.notion.site/LumiTerra-Game-Guide-ff7923da552242139c9e44bbec4df8e4?p=239980a8a0f44c60b44debf6b7f85889&pm=s")
      
      if section == "PVP":
        await how_to_play_game(interaction=interaction, url="https://lumiterra.notion.site/LumiTerra-Game-Guide-ff7923da552242139c9e44bbec4df8e4?p=afc9df4320ea4a16bde20aaaeff1d0ed&pm=s")
      
      if section == "Team":
        await how_to_play_game(interaction=interaction, url="https://lumiterra.notion.site/LumiTerra-Game-Guide-ff7923da552242139c9e44bbec4df8e4?p=ea58894814eb45f190b280d1c5fc9c19&pm=s")
      
      if section == "HomeLand":
        await how_to_play_game(interaction=interaction, url="https://lumiterra.notion.site/LumiTerra-Game-Guide-ff7923da552242139c9e44bbec4df8e4?p=0e757aec872a478f9265aff3229e3a7c&pm=s")
      
      if section == "How to return quickly?":
        await how_to_play_game(interaction=interaction, url="https://lumiterra.notion.site/LumiTerra-Game-Guide-ff7923da552242139c9e44bbec4df8e4?p=f1876bbd66084cc1ab246d82f535bc31&pm=s")
      
      if section == "Planting":
        await how_to_play_game(interaction=interaction, url="https://lumiterra.notion.site/LumiTerra-Game-Guide-ff7923da552242139c9e44bbec4df8e4?p=20d8b239fd8e4a64b70812062843175e&pm=s")
    
    elif type == "Task / Token Task":
      if section == "Task System":
        await how_to_play_game(interaction=interaction, url="https://lumiterra.notion.site/Task-System-aea940ee235149c5843b05c15cfdf2a0")
      
      if section == "Token Task":
        await how_to_play_game(interaction=interaction, url="https://lumiterra.notion.site/Token-Task-819c1c8ef9354cc192705d010d2b8b20")
      
      if section == "Material Loterry":
        await how_to_play_game(interaction=interaction, url="https://lumiterra.notion.site/Material-Loterry-125b3a9ac0d84c7dbc5013ef71d871d9")

      if section == "LeaderBoard":
        await how_to_play_game(interaction=interaction, url="https://lumiterra.notion.site/LeaderBoard-ee4b7e30a1a94de58f00dcdc056e3181")
        
    elif type == "Game profession":
      if section == "Combat Talent Profession":
        await how_to_play_game(interaction=interaction, url="https://lumiterra.notion.site/Combat-Talent-Profession-cd47977e0d9c4bfc9e0082f25404b476")
      
      if section == "Gathering Talent Profession":
        await how_to_play_game(interaction=interaction, url="https://lumiterra.notion.site/Gathering-Talent-Profession-3994251d40b14ad19f0a013e1de8b632")
      
      if section == "Farming Talent Profession":
        await how_to_play_game(interaction=interaction, url="https://lumiterra.notion.site/Farming-Talent-Profession-352fcd032f5b4d49abc431f6113c1849")
    
  except Exception as e:
    return e
  