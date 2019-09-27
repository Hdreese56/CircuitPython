import board
import time
from digitalio import DigitalInOut, Direction, Pull
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574InterFace
from lcd.lcd import Cursemode

button = DigitalInOut(board.D2)
button.direction = Direction.INPUT
button.pull = Pull.DOWN
button2 = DigitalInOut(board.D3)
button.direction = Direction.INPUT
button.pull = Pull.DOWN

clicks = 0
lcd = LCD(I2CPCF8574InterFace(0x27), num_rows=2, num_cols=16)

while True :
    lcd.set_cursor_pos(0,0)
    lcd.print("switch")