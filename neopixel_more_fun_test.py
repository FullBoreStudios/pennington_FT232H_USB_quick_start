import time
import board
import neopixel_spi as neopixel

num_pixels = 30
PIXEL_ORDER = neopixel.GRB
spi = board.SPI()

pixels = neopixel.NeoPixel_SPI(spi,
                               num_pixels,
                               pixel_order=PIXEL_ORDER,
                               auto_write=False)

RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)
WHITE = (255, 200, 0)
ORANGE = (255, 100, 0)

def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        return (0, 0, 0)
    if pos < 85:
        return (255 - pos * 3, pos * 3, 0)
    if pos < 170:
        pos -= 85
        return (0, 255 - pos * 3, pos * 3)
    pos -= 170
    return (pos * 3, 0, 255 - pos * 3)

def set_pixel(color, pixel_number):
    pixels[pixel_number] = WHITE
    pixels.show()
    time.sleep(0.04)
    pixels[pixel_number] = color
    pixels.show()
    time.sleep(0.09)


def color_chase(color, wait):
    for i in range(num_pixels):
        pixels[i] = color
        time.sleep(wait)
        pixels.show()
        time.sleep(0.01)

while True:
    color_chase(RED, 0.0001)
    # Vial 1
    set_pixel(GREEN, 0)
    set_pixel(GREEN, 1)
    set_pixel(GREEN, 2)
    # Vial 2
    set_pixel(BLUE, 3)
    set_pixel(BLUE, 4)
    set_pixel(BLUE, 5)
    # Vial 3
    set_pixel(PURPLE, 6)
    set_pixel(PURPLE, 7)
    set_pixel(PURPLE, 8)
    # Vial 4
    set_pixel(RED, 9)
    set_pixel(RED, 10)
    set_pixel(RED, 11)
    # Vial 5
    set_pixel(ORANGE, 12)
    set_pixel(ORANGE, 13)
    set_pixel(ORANGE, 14)
    # Vial 6
    set_pixel(GREEN, 15)
    set_pixel(GREEN, 16)
    set_pixel(GREEN, 17)
    # Vial 7
    set_pixel(BLUE, 18)
    set_pixel(BLUE, 19)
    set_pixel(BLUE, 20)
    # Vial 8
    set_pixel(PURPLE, 21)
    set_pixel(PURPLE, 22)
    set_pixel(PURPLE, 23)
    # Vial 9
    set_pixel(RED, 24)
    set_pixel(RED, 25)
    set_pixel(RED, 26)
    # Vial 10
    set_pixel(ORANGE, 27)
    set_pixel(ORANGE, 28)
    set_pixel(ORANGE, 29)
    time.sleep(10)

