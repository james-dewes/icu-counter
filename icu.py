import RPi.GPIO as GPIO, RPi.GPIO as GPIO2, time, urllib, urllib2
from msvcrt import getch

# get the GA property string
ga_string = open('prop.txt').read()

# set the GPIO pin the sensor is attached to
GPIO.setmode(GPIO.BCM)
sensor = 21
GPIO.setup(sensor, GPIO.IN)

# setup an output for the blinking LED
GPIO2.setmode(GPIO.BCM)
led = 5
GPIO2.setup(led, GPIO.OUT)


# TODO add a local log file function

def tell_google(ga_string):
    """
    string->
    :rtype : bool
    :return: true
    takes the GA property ID i.e. UA-XXXX-Y and makes a POST request to Google to log activity against
    that property under the category icu-counter
    """
    values = urllib.urlencode(dict(v='1', tid=ga_string, cid='12345', t='Sevent', ec='icu-counter', ea='person'))
    url = 'http://www.google-analytics.com/collect'
    headers = {'Content-type': 'application/x-www-form-urlencoded',
               'Accept': 'text/plain'}
    headers = ('User-agent':'ICU people counter', 'From:':'test@somedomain.com')
    req = urllib2.Request(url, values, headers)
    response = urllib2.urlopen(req)
    print(response.geturl())
    print(response.info())
    return true


def blink_led():
    """
    null
    :return: null
    Cause the attached LED to blink when the sensor is triggered
    """
    for i in range(0, 3):
        GPIO2.output(led, 1)
        time.sleep(0.5)
        GPIO2.output(led, 0)


# infinate loop of main operation
while True:
    # check for escape key
    key = ord(getch())
    if key == 27:  # ESC
        break
    elif GPIO.input(sensor):
        tell_google(ga_string)
        blink_led()
        time.sleep(2)
    else:
        time.sleep(0.5)

#cleanup
GPIO.cleanup()
GPIO2.cleanup()
