import RPi.GPIO as GPIO
import time, urllib, urllib2

# get the GA property string
ga_string = open('prop.txt').read()

GPIO.setmode(GPIO.BCM)
sensor = 21
GPIO.setup(sensor, GPIO.IN)

import RPi.GPIO as GPIO2
import time

GPIO2.setmode(GPIO.BCM)
led = 5
GPIO2.setup(led, GPIO.OUT)


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


test = 0
while test != 1:
    if GPIO.input(sensor):
        print("I see you")
        tell_google()
        GPIO2.output(led, 1)
        time.sleep(2)
        GPIO2.output(led, 0)
        time.sleep(2)
        # test = 1
    else:
        # print("waiting")
        time.sleep(0.5)

GPIO.cleanup()
