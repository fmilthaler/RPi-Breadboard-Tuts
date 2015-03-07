#!/usr/bin/python
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

endtime=10; pause=0.5
red=17; blue=27
GPIO.setup(red,GPIO.OUT)
GPIO.setup(blue,GPIO.OUT)
try:
	for i in range(int(round(float(endtime)/pause))):
		if (i%2==0):
			GPIO.output(red,GPIO.HIGH)
			GPIO.output(blue,GPIO.LOW)
		else:
			GPIO.output(red,GPIO.LOW)
			GPIO.output(blue,GPIO.HIGH)
		time.sleep(0.5)
finally:
	GPIO.output(red,GPIO.LOW)
	GPIO.output(blue,GPIO.LOW)
