import os
from inky import InkyPHAT
from PIL import Image, ImageFont, ImageDraw

PATH = os.path.dirname(__file__)

inky_display = InkyPHAT("red")
inky_display.set_border(inky_display.WHITE)

img = Image.open(os.path.join(PATH, "resources/NO1.png"))
inky_display.set_image(img)
inky_display.show()