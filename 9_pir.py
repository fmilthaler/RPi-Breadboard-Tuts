#!/usr/bin/python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO_PIR=7
RLED_IO=17
BLED_IO=27
BUZZER_IO=22
sleeptime=1.0

def ledstatus(channel):
  return 1==GPIO.input(channel)

def led(channel, status):
  if (status):
    GPIO.output(channel, GPIO.HIGH)
  else:
    GPIO.output(channel, GPIO.LOW)

def ledswitch(channel):
  #outmsg = "Channel "+str(channel)+" currently switched "+str(ledstatus(channel))
  #outmsg = outmsg.replace('False', 'off').replace('True', 'on')
  #print outmsg
  #print "Switching its status..."
  if ledstatus(channel):
    GPIO.output(channel, GPIO.LOW)
  else:
    GPIO.output(channel, GPIO.HIGH)

def buzz(channel, sleeptime):
  GPIO.output(channel, GPIO.HIGH)
  time.sleep(sleeptime)
  GPIO.output(channel, GPIO.LOW)
  time.sleep(sleeptime)

def motionalert(alerttime):
  ledswitch(RLED_IO)
  ledswitch(BLED_IO)
  buzz(BUZZER_IO,0.3*alerttime)
  time.sleep(0.7*alerttime)
  ledswitch(RLED_IO)
  ledswitch(BLED_IO)


print "PIR Module Test (CTRL-C to exit)"
# Set PIR pin as input
GPIO.setup(GPIO_PIR,GPIO.IN)

# Set led pins as output:
GPIO.setup(RLED_IO,GPIO.OUT)
GPIO.setup(BLED_IO,GPIO.OUT)
ledswitch(BLED_IO)

# Set buzzer as output:
GPIO.setup(BUZZER_IO,GPIO.OUT)
GPIO.output(BUZZER_IO,GPIO.LOW)

Current_State  = 0
Previous_State = 0

try:
  print "Waiting for PIR to settle ..."
  # Loop until PIR output is 0
  while GPIO.input(GPIO_PIR)==1:
    Current_State = 0
  print "  Ready"
  # Loop until users quits with CTRL-C
  while True :
    # Read PIR state
    Current_State = GPIO.input(GPIO_PIR)
    if Current_State==1 and Previous_State==0:
      # PIR is triggered
      print "  Motion detected!"
      # Record previous state
      motionalert(sleeptime)
      Previous_State=1
    elif Current_State==0 and Previous_State==1:
      # PIR has returned to ready state
      print "  Ready"
      Previous_State=0
    # Wait for 10 milliseconds
    time.sleep(0.01)

except KeyboardInterrupt:
  print "  Quit"
  # Reset GPIO settings
  GPIO.output(RLED_IO,GPIO.LOW)
  GPIO.output(BLED_IO,GPIO.LOW)
  GPIO.output(BUZZER_IO,GPIO.LOW)
  GPIO.cleanup()

