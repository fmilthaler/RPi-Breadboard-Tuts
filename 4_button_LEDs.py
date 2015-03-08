#!/usr/bin/python
import os
import time
import RPi.GPIO as GPIO

def ledstatus(channel):
   return 1==GPIO.input(channel)

def led(channel, status):
   if (status):
      GPIO.output(channel, GPIO.HIGH)
   else:
      GPIO.output(channel, GPIO.LOW)

def ledswitch(channel):
   outmsg = "Channel "+str(channel)+" currently switched "+str(ledstatus(channel))
   outmsg = outmsg.replace('False', 'off').replace('True', 'on')
   print outmsg
   print "Switching its status..."
   if ledstatus(channel):
      GPIO.output(channel, GPIO.LOW)
   else:
      GPIO.output(channel, GPIO.HIGH)

GPIO.setmode(GPIO.BCM)

sleeptime=2
red=17; blue=27

GPIO.setwarnings(False)
# setup channels:
GPIO.setup(10, GPIO.IN)
GPIO.setup(red,GPIO.OUT)
GPIO.setup(blue,GPIO.OUT)

# starting with blue being on:
ledswitch(blue)

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
         ledswitch(red)
         ledswitch(blue)
      else:
         os.system('clear')
         print ("Waiting for you to press a button")
         #print GPIO.input(10)
      time.sleep(sleeptime)
except:
   led(red, False)
   led(blue, False)
