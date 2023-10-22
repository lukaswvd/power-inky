import os
from inky import InkyPHAT
from PIL import Image, ImageFont, ImageDraw
from font_fredoka_one import FredokaOne

PATH = os.path.dirname(__file__)

inky_display = InkyPHAT("red")
inky_display.set_border(inky_display.WHITE)

img = Image.open(os.path.join(PATH, "resources/NO1.png"))
draw = ImageDraw.Draw(img)

font = ImageFont.truetype(FredokaOne, 22)

draw.text((72,(104-22)/2), "62 øre/kWh", inky_display.BLACK, font=font)

inky_display.set_image(img)
inky_display.show()