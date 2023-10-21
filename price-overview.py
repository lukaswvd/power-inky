import json
from inky.auto import auto
from PIL import Image, ImageFont, ImageDraw
from font_fredoka_one import FredokaOne
from datetime import datetime

try:
    import requests
except ImportError:
    exit("This script requires the requests module\nInstall with: sudo pip install requests")

inky_display = auto()
inky_display.set_border(inky_display.BLACK)

currentDateAndTime = datetime.now()
price = ""

res = requests.get("https://www.hvakosterstrommen.no/api/v1/prices/{}/{}-{}_NO1.json".format(currentDateAndTime.year, currentDateAndTime.month, currentDateAndTime.day))

if res.status_code == 200:
    j = json.loads(res.text)
    price = "{:.3f} øre/kWh".format(j[currentDateAndTime.hour]["NOK_per_kWh"])
else:
    price = "Kunne ikke hente pris"

img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))
draw = ImageDraw.Draw(img)

font = ImageFont.truetype(FredokaOne, 22)

w, h = font.getsize(price)
x = (inky_display.WIDTH / 2) - (w / 2)
y = (inky_display.HEIGHT / 2) - (h / 2)

draw.text((x, y), price, inky_display.RED, font)
inky_display.set_image(Image.open("./resources/NO1.png").convert('P'))
inky_display.show()
