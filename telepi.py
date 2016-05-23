# TelePi, by Treyzania

import RPi.GPIO as GPIO
import time

# Configured values
buttonPins = []
hookPin = -1

# Delays
keyDownTime = 0.25
keyUpTime = 0.25
hookUpTime = 1
hookDownTime = 1

# State
inCall = False

# Sets up the library, using a <KEY>:<PIN> dictionary, and a pin for the "hook"
# of the phone.  When the hook pin recieves power, the phone should think that
# the handset is being picked up.
def init(buttonDic, hook):
	
	# Cleans up any settings 
	GPIO.cleanup()
	
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
	
	buttonPins = buttonDic
	
	# Set all the pins to outputs
	for pin in buttonDic.values():
		GPIO.setup(pin, GPIO.OUT)
	
	# Set the hook as an output
	hookPin = hook

# Takes a single character and dials it.
def pushKey(key):
	
	if key in buttonPins:
		GPIO.output(buttonPins[key], 1)
		time.sleep(keyDownTime)
		GPIO.output(buttonPins[key], 0)
		time.sleep(keyAfterUpTime)
	else:
		print('Invalid key dialed')

def dial(number):
	
	chars = list(number)
	
	# Iterate through the pushable keys.
	for k in chars:
		if k in buttonPins:
			pushKey(k)

def pickup():
	GPIO.output(hookPin, 1)
	time.sleep(hookUpTime)

def rehook():
	GPIO.output(hookPin, 0)
	time.sleep(hookDownTime)

def beginCall(number)
	
	if !inCall:
		inCall = True
		pickup()
		dial(number)
	else:
		print("ALREADY IN CALL!")

def endCall():
	
	if inCall:
		rehook()
		inCall = False
		time.sleep(hookDownTime)
	else:
		print("CALL ALREADY OVER!")
		
