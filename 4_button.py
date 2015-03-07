#!/usr/bin/python
import os
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)
GPIO.setup(10, GPIO.IN)

sleeptime=2

print("------------------")
print(" Button + GPIO ")
print("------------------")

# print current button status:
print GPIO.input(10)
while True:
   if ( GPIO.input(10) == False ):
      print("Button Pressed")
      os.system('date')
      print GPIO.input(10)
      time.sleep(sleeptime)
   else:
      os.system('clear')
      print ("Waiting for you to press a button")
      print GPIO.input(10)
      time.sleep(sleeptime)
