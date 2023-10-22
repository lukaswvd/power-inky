import os
import json
from inky import InkyPHAT
from PIL import Image, ImageFont, ImageDraw
from font_fredoka_one import FredokaOne
from datetime import datetime

try:
    import requests
except ImportError:
    exit("This script requires the requests module\nInstall with: sudo pip install requests")

PATH = os.path.dirname(__file__)

inky_display = InkyPHAT("red")
inky_display.set_border(inky_display.WHITE)

img = Image.open(os.path.join(PATH, "resources/NO1.png"))
draw = ImageDraw.Draw(img)

currentDateAndTime = datetime.now()
price = ""

res = requests.get("https://www.hvakosterstrommen.no/api/v1/prices/{}/{}-{}_NO1.json".format(currentDateAndTime.year, currentDateAndTime.month, currentDateAndTime.day))

if res.status_code == 200:
    j = json.loads(res.text)
    print(j[currentDateAndTime.hour]["NOK_per_kWh"])
    price = "{:.0f} øre/kWh".format(j[currentDateAndTime.hour]["NOK_per_kWh"])
else:
    price = "Kunne ikke hente pris"


font = ImageFont.truetype(FredokaOne, 22)

w, h = font.getsize(price)
y = (inky_display.HEIGHT / 2) - (h / 2)

draw.text((72, y), price, inky_display.BLACK, font=font)

inky_display.set_image(img)
inky_display.show()