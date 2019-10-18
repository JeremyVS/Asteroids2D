# LCD setup code copied from adafruit guide, 
# located at: https://learn.adafruit.com/character-lcds/python-circuitpython
# char lcd library: https://github.com/adafruit/Adafruit_CircuitPython_CharLCD
# nunchuck library: https://github.com/adafruit/Adafruit_CircuitPython_Nunchuk

import board
import digitalio
import adafruit_character_lcd.character_lcd as characterlcd
import time
import adafruit_nunchuk

# setup for LCD character screen (16x2)
lcd_rs = digitalio.DigitalInOut(board.D7)
lcd_en = digitalio.DigitalInOut(board.D8)
lcd_d7 = digitalio.DigitalInOut(board.D12)
lcd_d6 = digitalio.DigitalInOut(board.D11)
lcd_d5 = digitalio.DigitalInOut(board.D10)
lcd_d4 = digitalio.DigitalInOut(board.D9)

lcd_columns = 16
lcd_rows = 2

lcd = characterlcd.Character_LCD_Mono(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows)
lcd.clear()

# setup for wii nunchuck
nc = adafruit_nunchuk.Nunchuk(board.I2C())


while True:
    # gratuitous hello world test! ...but tweaked for LCD display testing
    lcd.message = 'Hello\nCircuitPython!'
    for i in range(0:15))  
        time.sleep(1)
        lcd.move_left())
    for i in range(0:15)
        time.sleep(1)
        lcd.move_right()

# notes: char_lcd library only seems to allow printing via "message",
# not specifically printing to a given location (x/y, etc)
# this might require careful manipulation of stored string(s) to keep the state of the playing field
# Note 1: looking at the library itself, I also see a "cursor_position(self, column, row)" function,
#    which says it only works for the next message, then goes back to 0,0 - this could be helpful?
#    (perhaps with a wrapper function of my own) 
# Note 2: does writting a 'message' (of any size) erase the old one?  if so, have to write entire
#    "game screen" at once anyway...