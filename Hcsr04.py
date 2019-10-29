import time
import neopixel
import board
from adafruit_hcsr04 import HCSR04
trig = board.D2
echo = board.D3
sonar = HCSR04(trig, echo)
pixel_pin = board.NEOPIXEL
num_pixels = 1
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.3)

RED = (255, 0, 0)
PINK = (255, 0, 180)
PURPLE = (180, 0, 255)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
GREEN = (0, 255, 0)

while True:
    try:
        distance = sonar.distance
        print((distance))

        if distance > 0 and distance <= 7:
            pixels.fill(RED)
            pixels.show()
        if distance > 7 and distance <= 15:
            pixels.fill(PURPLE)
            pixels.show()
        if distance > 15 and distance <= 23:
            pixels.fill(BLUE)
            pixels.show()
        if distance > 23 and distance <= 29:
            pixels.fill(CYAN)
            pixels.show()
        if distance > 29 and distance <= 35:
            pixels.fill(GREEN)
            pixels.show()
    except RuntimeError:
        print("Retrying!")
        pass
        time.sleep(.2)