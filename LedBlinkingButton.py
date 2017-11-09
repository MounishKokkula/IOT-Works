import RPi.GPIO as GPIO
import time ## Import 'time' library. Allows us to use 'sleep'
import os
GPIO.setmode(GPIO.BCM) ## Use board pin numbering
GPIO.setwarnings(False)

LEDPin = 17
buttonPin = 10


GPIO.setup(LEDPin, GPIO.OUT) ## Setup the button

GPIO.setup(buttonPin, GPIO.IN, pull_up_down = GPIO.PUD_UP)

GPIO.output(LEDPin, False)

count = 0
buttonPress = True
ledState = False

try:
    while True:
        
        os.system('clear')
        print("Press a button!")
        time.sleep(1)
        buttonPress=GPIO.input(buttonPin)
        print(buttonPress)
        if buttonPress != True:
            count += 1
        elif count == 1   :    
            GPIO.output(LEDPin,True)
            time.sleep(0.2)
            print('LED ON')
            GPIO.output(LEDPin,False)
            time.sleep(0.2)
            print('LED off')
        elif count > 1:
            GPIO.output(LEDPin,False)
            count=0 
        #time.sleep(0.2)
finally:
    GPIO.output(LEDPin, False)
    GPIO.cleanup()
