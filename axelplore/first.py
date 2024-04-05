# erster Python Code von Axelplore für die Max7219
# https://luma-led-matrix.readthedocs.io/en/latest/python-usage.html

from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.led_matrix.device import max7219
from PIL import ImageFont 
from luma.core.legacy import text
from luma.core.legacy.font import proportional, CP437_FONT, LCD_FONT

# create device
serial = spi(port=0, device=0, gpio=noop())
device = max7219(serial)
print("Created device")

font = ImageFont.truetype("examples/pixelmix.ttf", 8)

with canvas(device) as draw:
    draw.rectangle(device.bounding_box, outline="white", fill="black")
print("rectangle drawed")