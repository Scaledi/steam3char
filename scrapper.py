from requests import api
import config
import random
import requests
import time
import os
import winsound


# from string (https://github.com/python/cpython/blob/master/Lib/string.py)
# see https://wiki.teamfortress.com/wiki/WebAPI/ResolveVanityURL for how we use the API

# region: string
whitespace = ' \t\n\r\v\f'
ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ascii_letters = ascii_lowercase + ascii_uppercase
digits = '0123456789'
hexdigits = digits + 'abcdef' + 'ABCDEF'
octdigits = '01234567'
punctuation = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
printable = digits + ascii_letters + punctuation + whitespace
# endregion

steam_valid = ascii_uppercase + digits + "-" + "_"

file = open("userurls.txt","a")

while True:
    vantity = ''.join((random.choice(steam_valid) for i in range(3)))
    #vantity = "_"

    APIcall = requests.get("https://api.steampowered.com/ISteamUser/ResolveVanityURL/v0001/?key=" + str(config.key) + "&vanityurl=" + str(vantity))
    data = APIcall.text

    isvalid = data.find(":1")

    if str(isvalid) == "-1":
        os.system('cls' if os.name == 'nt' else 'clear')
        file.write(vantity + "\n")
        print(vantity)
        frequency = 5000  # Set Frequency To 2500 Hertz
        duration = 10000  # Set Duration To 1000 ms == 1 second
        winsound.Beep(frequency, duration)
        time.sleep(60)
    else:
        print(str(vantity) + " was already taken!")