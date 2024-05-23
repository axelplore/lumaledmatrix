# Uhr im Format d.m. hh:mm:ss von Axelplore für die Max7219
# https://luma-led-matrix.readthedocs.io/en/latest/python-usage.html

import time
import argparse
from time import localtime, strftime
from threading import Timer

from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.led_matrix.device import max7219
from luma.core.legacy import text
from luma.core.legacy.font import proportional, CP437_FONT, LCD_FONT, TINY_FONT

def demo(n, block_orientation, rotate, inreverse):
    # create device
    serial = spi(port=0, device=0, gpio=noop())
    device = max7219(serial, cascaded=n or 7, block_orientation=block_orientation,
                     rotate=rotate or 0, blocks_arranged_in_reverse_order=inreverse)
    print("Created device")

    def print_current_time():
        current_time = strftime("%-d.%-m°%-H:%-M:%-S", localtime())
        with canvas(device) as draw:
            text(draw, (0, 0), current_time, fill="white", font=proportional(TINY_FONT))
            Timer(1, print_current_time).start()

    print_current_time()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='matrix_demo arguments',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('--cascaded', '-n', type=int, default=1, help='Number of cascaded MAX7219 LED matrices')
    parser.add_argument('--block-orientation', type=int, default=0, choices=[0, 90, -90], help='Corrects block orientation when wired vertically')
    parser.add_argument('--rotate', type=int, default=0, choices=[0, 1, 2, 3], help='Rotate display 0=0°, 1=90°, 2=180°, 3=270°')
    parser.add_argument('--reverse-order', type=bool, default=False, help='Set to true if blocks are in reverse order')

    args = parser.parse_args()

    try:
        demo(args.cascaded, args.block_orientation, args.rotate, args.reverse_order)
    except KeyboardInterrupt:
        pass
