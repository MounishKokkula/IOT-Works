import RPi.GPIO as GPIO
import time ## Import 'time' library. Allows us to use 'sleep'

GPIO.setmode(GPIO.BCM) ## Use board pin numbering
GPIO.setwarnings(False)
GPIO.setup(17, GPIO.OUT) ## Setup GPIO Pin 17 to OUT
GPIO.setup(22,GPIO.OUT) ## Setup GPIO Pin 27 OUT

while 1==1:

	# Turn LEDs ON
	GPIO.output(17,GPIO.HIGH)
	GPIO.output(22,GPIO.HIGH)
	time.sleep(2)

# Turn off LEDs

	GPIO.output(17,GPIO.LOW)
	GPIO.output(22,GPIO.LOW)
	time.sleep(2)







##Define a function named Blink()
#def Blink(numTimes,speed):

 #   for i in range(0,numTimes):
  #      ## Run loop numTimes
   #     print("Iteration " + str(i+1))## Print current loop
   #     GPIO.output(7,True)## Switch on pin 7
   #     time.sleep(speed)## Wait
   #     GPIO.output(7,False)## Switch off pin 7
   #     time.sleep(speed)## Wait
#print ("Done" )## When loop is complete, print "Done"
#GPIO.cleanup()

## Ask user for total number of blinks and length of each blink
#iterations = input("Enter total number of times to blink: ")
#speed = input("Enter length of each blink(seconds): ")

## Start Blink() function. Convert user input from strings to numeric data types and pass to Blink() as parameters
#Blink(int(iterations),float(speed))
