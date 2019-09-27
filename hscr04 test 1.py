import time
#import neopixel
import board
from adafruit_hcsr04 import HCSR04
trig = board.D2
echo = board.D3
sonar = HCSR04(trig, echo)
#pin_pixel = board.NEOPIXEL
#num_pixels = 1

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

while True:
    try:
        print((sonar.distance,))
    except RuntimeError:
        print("Retrying!")
    pass
    time.sleep(.2)