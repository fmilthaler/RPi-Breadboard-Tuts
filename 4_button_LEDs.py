#!/usr/bin/python
import os
import time
import RPi.GPIO as GPIO

def led(colorgpio, status):
   if (status):
      GPIO.output(colorgpio, GPIO.HIGH)
   else:
      GPIO.output(colorgpio, GPIO.LOW)

GPIO.setmode(GPIO.BCM)

sleeptime=2
red=17; blue=27

GPIO.setwarnings(False)
# setup channels:
GPIO.setup(10, GPIO.IN)
GPIO.setup(red,GPIO.OUT)
GPIO.setup(blue,GPIO.OUT)

print("------------------")
print(" Button + GPIO ")
print("------------------")

# print current button status:
print GPIO.input(10)
try:
   while True:
      if ( GPIO.input(10) == False ):
         print("Button Pressed")
         os.system('date')
         print GPIO.input(10)
         led(red, True)
         led(blue, True)
         time.sleep(sleeptime)
      else:
         os.system('clear')
         print ("Waiting for you to press a button")
         print GPIO.input(10)
         led(red, False)
         led(blue, False)
         time.sleep(sleeptime)
except:
   led(red, False)
   led(blue, False)
