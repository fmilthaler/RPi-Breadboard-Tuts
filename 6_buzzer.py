#!/usr/bin/python
import os
import time
import RPi.GPIO as GPIO

loop_count = 0
shortsleep=.1
longsleep=.3
buzzer=22

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(buzzer,GPIO.OUT)

def buzz(channel, sleeptime):
	GPIO.output(channel, GPIO.HIGH)
	time.sleep(sleeptime)
	GPIO.output(channel, GPIO.LOW)
	time.sleep(sleeptime)

def dotdotdot(channel, sleeptime):
	#Dot Dot Dot
	for i in range(3):
		buzz(channel, sleeptime)

def dashdashdash(channel, sleeptime):
	#Dash Dash Dash
	for i in range(3):
		buzz(channel, sleeptime)

def morsecode ():
	#Dot Dot Dot
	dotdotdot(buzzer, shortsleep)
	time.sleep(longsleep)
	#Dash Dash Dah
	dashdashdash(buzzer, 2*shortsleep)
	time.sleep(longsleep)
	#Dot Dot Dot
	dotdotdot(buzzer, shortsleep)
	time.sleep(2*longsleep)

os.system('clear')
print "Morse Code"
loop_count = input("How many times would you like SOS to loop?: ")
for i in range(loop_count):
	morsecode()
