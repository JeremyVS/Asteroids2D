# all of this is copied from adafruit guide
# from: https://learn.adafruit.com/character-lcds/python-circuitpython

import board
import digitalio
lcd_rs = digitalio.DigitalInOut(board.D7)
lcd_en = digitalio.DigitalInOut(board.D8)
lcd_d7 = digitalio.DigitalInOut(board.D12)
lcd_d6 = digitalio.DigitalInOut(board.D11)
lcd_d5 = digitalio.DigitalInOut(board.D10)
lcd_d4 = digitalio.DigitalInOut(board.D9)

lcd_columns = 16
lcd_rows = 2

import adafruit_character_lcd.character_lcd as characterlcd
lcd = characterlcd.Character_LCD_Mono(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows)

while True:
    # gratuitous hello world test! ...but tweaked for LCD display testing
    lcd.message = 'Hello\nCircuitPython!'
    for i in range(0:15))  
        sleep(1)
        lcd.move_left())
    for i in range(0:15)
        sleep(1)
        lcd.move_right()