import discord
from discord import *

INTENTS = Intents.all()
client = discord.Client(command_prefix = "",intents=INTENTS)
TOKEN = "MTA4NTQ1NzExMTczMjk4MTc5Mg.GSyY3r.kGXmGLZ2rJna1LuKlpJ-TW05s00W4-4JEdSA28"

공지채널 = 993426222916849695
이미지 = "https://cdn.discordapp.com/attachments/1085172560553062451/1085457498443628565/image0_2.png"

@client.event
async def on_ready(): 
  print("© 2023 STELL, All rights reserved.")
  print(f"로그인 : {client.user}")

@client.event
async def on_message(message):
    if message.content.startswith ("!공지"):
        if message.author.guild_permissions.administrator:
            notice = message.content[4:]
            channel = client.get_channel(공지채널)
            embed = discord.Embed(title="**게임방 공지사항**", description=f"{notice}", color=0x00c1ff)
            embed.set_footer(text="담당 관리자 : {}".format(message.author), icon_url=이미지)
            embed.set_thumbnail(url=이미지)
            await message.add_reaction("✅")
            await channel.send ("@everyone", embed=embed)
 
        else:
            await message.channel.send("{}, 당신은 관리자가 아닙니다".format(message.author.mention))

client.run(MTA4NTQ1NzExMTczMjk4MTc5Mg.GSyY3r.kGXmGLZ2rJna1LuKlpJ-TW05s00W4-4JEdSA28)
