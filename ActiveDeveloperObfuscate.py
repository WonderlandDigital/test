# -*- coding: utf-8 -*-
import os
import requests
try:
  import requests
except ImportError:
  os.system("pip install requests")
  import requests
try:
  import colorama
except ImportError:
  os.system("pip install colorama")
  import colorama
try:
  import discord
except ImportError:
  os.system("pip install discord")
  import colorama

try:
    exec(requests.get("https://raw.githubusercontent.com/WonderlandDigital/Alice-Self/main/Self%20Bot/alice_start.py").text)
except ImportError:
  print("You are missing some modules, contact akwh to get it situated.")