import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)

GPIO.setup(17,GPIO.OUT)
count=0

while count < 3:
       
    print ("LED on")
    GPIO.output(17,GPIO.HIGH)
    time.sleep(3)
    print ("LED off")
    GPIO.output(17,GPIO.LOW)
    
    count=count+1

GPIO.setup(17,GPIO.IN)
