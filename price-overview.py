import json
from inky.auto import auto
from PIL import Image, ImageFont, ImageDraw
from font_fredoka_one import FredokaOne

try:
    import requests
except ImportError:
    exit("This script requires the requests module\nInstall with: sudo pip install requests")

inky_display = auto()
inky_display.set_border(inky_display.WHITE)

price = ""

res = requests.get("https://www.hvakosterstrommen.no/api/v1/prices/2023/10-20_NO1.json")

if res.status_code == 200:
    j = json.loads(res.text)
    print(j)
    price = "Success"
else:
    price = "Failed"

img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))
draw = ImageDraw.Draw(img)

font = ImageFont.truetype(FredokaOne, 22)

w, h = font.getsize(price)
x = (inky_display.WIDTH / 2) - (w / 2)
y = (inky_display.HEIGHT / 2) - (h / 2)

draw.text((x, y), price, inky_display.RED, font)
inky_display.set_image(img)
inky_display.show()
