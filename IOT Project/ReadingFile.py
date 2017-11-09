import time

import Adafruit_Nokia_LCD as LCD
import Adafruit_GPIO.SPI as SPI

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import RPi.GPIO as GPIO
import time ## Import 'time' library. Allows us to use 'sleep'


# Raspberry Pi hardware SPI config:
DC = 23
RST = 24
SPI_PORT = 0
SPI_DEVICE = 0

GPIO.setmode(GPIO.BCM) ## Use board pin numbering
GPIO.setwarnings(False)
GPIO.setup(17, GPIO.OUT) ## Setup GPIO Pin 17 to OUT
GPIO.setup(22,GPIO.OUT) ## Setup GPIO Pin 27 OUT


# Hardware SPI usage:
disp = LCD.PCD8544(DC, RST, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE, max_speed_hz=4000000))

# Initialize library.
disp.begin(contrast=60)

# Clear display.
disp.clear()
disp.display()


target = open('test.txt', 'r')

while True:

    for t in target:
        print (t)
        time.sleep(2)
        if t > 0:
            # Create blank image for drawing.
            # Make sure to create image with mode '1' for 1-bit color.
            image = Image.new('1', (LCD.LCDWIDTH, LCD.LCDHEIGHT))

            # Get drawing object to draw on image.
            draw = ImageDraw.Draw(image)

            # Draw a white filled box to clear the image.
            draw.rectangle((0,0,LCD.LCDWIDTH,LCD.LCDHEIGHT), outline=255, fill=255)

            draw.polygon([(6,40), (43,3), (80,40)], outline=0, fill=255)
            print ('inside the loop')
            
            # Load default font.
            font = ImageFont.load_default()

            draw.text((27,20), 'ALERT!', font=font)

            disp.image(image)
            disp.display()
