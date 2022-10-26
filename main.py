#!/usr/bin/env python3
#-*- coding: utf-8 -*-
import shutil
import colorama
import os
import json
import re
import secrets
import string
import datetime

x = datetime.datetime.now()

os.system("clear")

colorama.init()

def Header():
    print(colorama.Fore.RED+"""
\033[1;31m
██████╗░░█████╗░░██████╗░██████╗░█████╗░░██████╗
██╔══██╗██╔══██╗██╔════╝██╔════╝██╔══██╗██╔════╝
██████╔╝███████║╚█████╗░╚█████╗░██║░░██║╚█████╗░
██╔═══╝░██╔══██║░╚═══██╗░╚═══██╗██║░░██║░╚═══██╗
██║░░░░░██║░░██║██████╔╝██████╔╝╚█████╔╝██████╔╝
╚═╝░░░░░╚═╝░░╚═╝╚═════╝░╚═════╝░░╚════╝░╚═════╝░
                            \033[1;39mDeveloper by Eratonos
                                                Ibrahim\033[1;31m
""".center(shutil.get_terminal_size().columns))

Header()

print(colorama.Back.RED+colorama.Fore.WHITE+"[1]"+colorama.Back.RESET+colorama.Fore.RED+" Random Generator")
print(colorama.Back.RED+colorama.Fore.WHITE+"[2]"+colorama.Back.RESET+colorama.Fore.RED+" Soz Generator")

var = input(colorama.Fore.LIGHTRED_EX+"\n· Bir reqem daxil edin > "+colorama.Style.RESET_ALL)
os.system("clear")
Header()
if int(var) == 1:
    leng = input(colorama.Fore.LIGHTRED_EX+"· Uzunluq daxil edin > "+colorama.Style.RESET_ALL)
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation
    alphabet = letters + digits + special_chars
    pwd = ''
    for i in range(int(leng)):
        pwd += ''.join(secrets.choice(alphabet))

    f = open("passwords.txt", "a")
    f.write(f"{x.strftime('%x')} {x.strftime('%X')}: {pwd}\n")

    print(colorama.Fore.RED+"  └ Senin sifren → "+colorama.Back.RED+colorama.Fore.WHITE+pwd)
elif int(var) == 2:
    word = input(colorama.Fore.LIGHTRED_EX + "· Soz & Cumle daxil edin > " + colorama.Style.RESET_ALL)
    pwd = word\
        .replace(" ", "_")\
        .replace("a", "4")\
        .replace("A", "@")\
        .replace("e", "3")\
        .replace("E", "_3")\
        .replace("g", "9")\
        .replace("G", "_9")\
        .replace("i", "1")\
        .replace("I", "_1")\
        .replace("o", "0")\
        .replace("O", "_0")\
        .replace("u", "7")\
        .replace("U", "_7")
    f = open("passwords.txt", "a")
    f.write(f"{x.strftime('%x')} {x.strftime('%X')}: {pwd}\n")
    print(colorama.Fore.RED + "  └ Senin sifren → " + colorama.Back.RED + colorama.Fore.WHITE + pwd)