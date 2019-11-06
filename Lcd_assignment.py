import board
import time
from digitalio import DigitalInOut, Direction, Pull
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
from lcd.lcd import CursorMode


button = DigitalInOut(board.D2)
button.direction = Direction.INPUT
button.pull = Pull.DOWN
switch = DigitalInOut(board.D3)
switch.direction = Direction.INPUT
switch.pull = Pull.DOWN

clicks = 0
clicks2 = 1
lcd = LCD(I2CPCF8574Interface(0x27), num_rows=2, num_cols=16)
#oldButton = False

while True:
     if not button.value:# and oldButton:
        lcd.set_cursor_pos(0,0)
        lcd.print("Switch")
        lcd.set_cursor_pos(1,0)
        lcd.print("presses")

        if switch.value:
            clicks2 =-1 # Make it go down 

            lcd.set_cursor_pos(0,7)
            lcd.print(" Down ")
            lcd.print("  ")
            lcd.set_cursor_pos(0,7)
        if switch.value and clicks2 == -1: # make it go up
            clicks2 = 1
            lcd.set_cursor_pos(0,7)
            lcd.print(" Up ")
            lcd.print("  ")
            lcd.set_cursor_pos(0,7)
        if button.value: #and oldButton:

            lcd.set_cursor_pos(1,8) #prints number
            clicks += clicks2
            lcd.print(str(clicks))
            lcd.print("  ")
            lcd.set_cursor_pos(1,8)
     #oldButton = button.value