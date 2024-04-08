# erster Python Code von Axelplore für die Max7219
# https://luma-led-matrix.readthedocs.io/en/latest/python-usage.html

import time

from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.led_matrix.device import max7219
from luma.core.legacy import text
from luma.core.legacy.font import proportional, CP437_FONT, LCD_FONT

# create device
serial = spi(port=0, device=0, gpio=noop())
device = max7219(serial)
print("Created device")

msg = "Hallo Lisa"
msg_length= len(msg)

for i in range(msg_length):
    with canvas(device) as draw:
        text(draw, (0, 0), msg[i], fill="white")
        print("draw", msg[i])
        time.sleep(1)