import time
import board
import neopixel_spi as neopixel



RED = (255, 0, 0)
ORANGE = (255, 34, 0)
YELLOW = (255, 170, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
VIOLET = (153, 0, 255)
MAGENTA = (255, 0, 51)
PINK = (255, 51, 119)
AQUA = (85, 125, 255)


NUM_PIXELS = 30
PIXEL_ORDER = neopixel.GRB
COLORS = (RED, ORANGE, CYAN, MAGENTA, BLUE, GREEN, PINK, AQUA)
DELAY = 0.005

spi = board.SPI()

pixels = neopixel.NeoPixel_SPI(spi,
                               NUM_PIXELS,
                               pixel_order=PIXEL_ORDER,
                               auto_write=False)

while True:
    for color in COLORS:
        for i in range(NUM_PIXELS):
            pixels[i] = color
            pixels.show()
            time.sleep(DELAY)
            pixels.fill(0)