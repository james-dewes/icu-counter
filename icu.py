import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
sensor = 21
GPIO.setup(sensor,GPIO.IN)

import RPi.GPIO as GPIO2
import time
GPIO2.setmode(GPIO.BCM)
led = 5
GPIO2.setup(led,GPIO.OUT)

test = 0
while test != 1:
    if GPIO.input(sensor):
        print("I see you")
        GPIO2.output(led,1)
        time.sleep(2)
        GPIO2.output(led,0)
        time.sleep(2)
        #test = 1
    else:
        #print("waiting")
        time.sleep(0.5)


GPIO.cleanup()
