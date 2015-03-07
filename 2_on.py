#!/usr/bin/python
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()
GPIO.setwarnings(True) # for debugging
GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
print "Lights on"
GPIO.output(17,GPIO.HIGH)
GPIO.output(27,GPIO.HIGH)
