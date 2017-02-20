import RPi.GPIO as GPIO
import time ## Import 'time' library. Allows us to use 'sleep'

GPIO.setmode(GPIO.BCM) ## Use board pin numbering
GPIO.setwarnings(False)
#GPIO.setup(17, GPIO.OUT) ## Setup GPIO Pin 17 to OUT
GPIO.setup(22,GPIO.OUT) ## Setup GPIO Pin 27 OUT

while True:

	# Turn LEDs ON
#	GPIO.output(17,GPIO.HIGH)
	GPIO.output(22,GPIO.HIGH)
	time.sleep(2)

# Turn off LEDs

#	GPIO.output(17,GPIO.LOW)
	GPIO.output(22,GPIO.LOW)
	time.sleep(2)
