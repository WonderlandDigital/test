import discord, json, os, colorama, ctypes
from discord.ext import commands, tasks
from discord import app_commands
from itertools import cycle
from colorama import Fore

with open('config.json') as f:
  config = json.load(f)
  token = config['token']
  wonderlanddigital = config['name?']

alice = commands.Bot(command_prefix="!", intents=discord.Intents.all())
alice_status = cycle([
  "Developer badge!", "Hi its Rudy :)", "Wait 24 hours",
  "After running command"
])
clear = lambda: os.system('cls')


@tasks.loop(seconds=2)
async def change_status():
  await alice.change_presence(activity=discord.Game(next(alice_status)))


@alice.event
async def on_ready():
  clear()
  ctypes.windll.kernel32.SetConsoleTitleW(
    f'Developer Badge | Logged in as {alice.user} | Authenticated as {wonderlanddigital}'
  )
  print(f"""
{Fore.GREEN}  ____________36936936936936936
____________36936936936936936
____________369369369369369369
___________36936936936936933693
__________3693693693693693693693
_________369369369369369369369369
_________3693693693693693693693699
________3693693693693693693693699369
_______36936939693693693693693693693693
_____3693693693693693693693693693693636936
___36936936936936936936936936936___369369369
__36936___369336936369369369369________36936
_36936___36936_369369336936936{Fore.RED}__¶¶__¶¶{Fore.GREEN}
36933___36936__36936___3693636_{Fore.RED}¶¶¶¶¶¶¶¶{Fore.GREEN}
693____36936__36936_____369363_{Fore.RED}¶¶¶¶¶¶¶¶{Fore.GREEN}
______36936__36936______369369__{Fore.RED}¶¶¶¶¶¶{Fore.GREEN}
_____36936___36936_______36936___{Fore.RED}¶¶¶¶{Fore.GREEN}
_____36936___36936________36936___{Fore.RED}¶¶{Fore.GREEN}
_____36936___36936_________36936___11,
______369____36936__________369___11,
______________369________________11,
_______________________________11,
_____________________________11,
______________________________11,
________________________________11,
___________________________{Fore.RED}¶¶__¶¶                   {Fore.WHITE}𝐀𝐜𝐭𝐢𝐯𝐞 𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐫 𝐁𝐚𝐝𝐠𝐞{Fore.GREEN}
__________________________{Fore.RED}¶¶¶¶¶¶¶¶{Fore.GREEN}				
__________________________{Fore.RED}¶¶¶¶¶¶¶¶		    {Fore.GREEN}Logged in {Fore.WHITE}as {Fore.RED}{alice.user.name}{Fore.GREEN}
___________________________{Fore.RED}¶¶¶¶¶¶                   {Fore.WHITE}Use {Fore.GREEN}/badge {Fore.WHITE}to become eligble,{Fore.GREEN}
____________________________ {Fore.RED}¶¶¶                    {Fore.WHITE}then wait 24-hours to claim.{Fore.GREEN}
_____________________________{Fore.RED} ¶                     {Fore.WHITE}If you encounter error's type{Fore.GREEN}
____________________________11,                     {Fore.GREEN}restart {Fore.WHITE}in the console.{Fore.GREEN}
_______________________________11,                  {Fore.WHITE}Credits to: {Fore.RED}@akwh{Fore.GREEN}
_______________________________11,  
______________369_________________11,
______369____36936__________369_____11,              
_____36936___36936_________36936___11,
_____36936___36936________36936___11,
_____36936___36936_______36936___11,
______36936__36936______369369 _{Fore.RED}¶¶_¶¶{Fore.GREEN}
693____36936__36936_____369363 {Fore.RED}¶¶¶¶¶¶¶{Fore.GREEN}
36933___36936__36936___3693636 {Fore.RED}¶¶¶¶¶¶¶{Fore.GREEN}
_36936___36936_369369336936936 _{Fore.RED}¶¶¶¶¶{Fore.GREEN}
__36936___369336936369369369369 _{Fore.RED}¶¶¶{Fore.GREEN}__3696
___36936936936936936936936936936 _{Fore.RED}¶{Fore.GREEN}_336939
_____36936936936936936936936936936936936
_______369369396936936936936936693693
________36936936936936936936999369
_________36936936936936936933699
_________3693693693693693369369
__________36936936936936993693
___________369369369369333693
____________3693693693699369
____________369369369366936
____________36936936936693
  """)
  print(f'{Fore.RED}╔[{Fore.WHITE}{wonderlanddigital}{Fore.RED}@{Fore.WHITE}WonderDev]{Fore.RED}')
  try:
    synced = await alice.tree.sync()
    change_status.start()
    print(f"╚═════➤ {Fore.WHITE}")
  except Exception as e:
    print(e)



@alice.tree.command(description="Makes you eligble toward the badge.")
async def badge(interaction: discord.Interaction):
  await interaction.response.send_message(
    "**This is a command to get the Active Developer Badge!**\nYou will be able to claim your Active Developer Badge within 24 hours\n**Make sure to follow @akwh for making this method!**\nhttps://support-dev.discord.com/hc/en-us/articles/10113997751447-Active-Developer-Badge",
    ephemeral=True)
  print(f"Command Log: \n{interaction.user} used /badge!")


alice.run(token)
