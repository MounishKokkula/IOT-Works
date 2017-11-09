import sys

import Adafruit_DHT

# Parse command line parameters.

target = open('DHT11Inv.txt', 'w')

sensor_args = {'11': Adafruit_DHT.DHT11,
            '22': Adafruit_DHT.DHT22,
            '2302': Adafruit_DHT.AM2302 }
if len(sys.argv) == 3 and sys.argv[1] in sensor_args:
    sensor = sensor_args[sys.argv[1]]
    pin = sys.argv[2]
else:
    print('usage: sudo python Adafruit_DHT.py [11|22|2302] GPIOpin#')
    print('example: sudo python Adafruit_DHT.py 2302 4 - Read from an AM2302 connected to GPIO #4')
    sys.exit(1)
n = 0
while( n < 10 ):

    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

# Un-comment the line below to convert the temperature to Fahrenheit.
    temperature = temperature * 9/5.0 + 32

    n += 1
    if humidity is not None and temperature is not None:
        target.write('Temp={0:0.1f}*  Humidity={1:0.1f}%\n'.format(temperature, humidity))
        print('Temp={0:0.1f}*  Humidity={1:0.1f}%\n'.format(temperature, humidity))
    else:
        target.write('Failed to get reading. Try again!\n')
        print('Failed to get reading. Try again!')
        sys.exit(1)
