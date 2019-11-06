import board
import time
from digitalio import DigitalInOut, Direction, Pull


counter = 0
interrups = 0
lasttime = 0
photo = DigitalInOut(board.D13)
photo.direction = Direction.INPUT
photo.pull = Pull.UP
initial = time.monotonic()
print("working")
while True:
    #print(photo.value)
    now = time.monotonic() # sets up the time
    if time.monotonic() % 4 == 0:
        print("the number of interrupts is ",counter )#prints out phrase
    if photo.value and interrups==0 :
         interrups=1
         initial = now
         counter = counter + 1 # adds the interrups


    elif not photo.value:

        interrups = 0