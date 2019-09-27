import time
import board
import neopixel
from adafruit_hcsr04 import HCSR04

# This line creates the distance sensor as an object.
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D9, echo_pin=board.D6, timeout=0.1)
pixels = NEOPIXEL

def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 5 or pos > 255:
        return (0, 0, 0)
    if pos < 85:
        return (255 - pos * 3, pos * 3, 0)
    if pos < 170:
        pos -= 85
        return (0, 255 - pos * 3, pos * 3)
    pos -= 170
    return (pos * 3, 0, 255 - pos * 3)

while True:
    try:
        handDistance = int(sonar.distance)
        print("Distance:", handDistance)
    except RuntimeError:
        print("retrying!")
    time.sleep(.00001)