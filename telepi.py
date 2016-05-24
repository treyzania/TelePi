# TelePi, by Treyzania

import RPi.GPIO as GPIO
import time

# Configured values
__buttonPins = []
__hookPin = -1

# State
__inCall = False

# Delays
_keyDownTime = 0.25
_keyUpTime = 0.25
_hookUpTime = 1
_hookDownTime = 1

# Sets up the library, using a <KEY>:<PIN> dictionary, and a pin for the "hook" of the phone.  When the hook pin recieves power, the phone should think that the handset is being picked up.
def init(buttonDic, hook):
	
	# Cleans up any settings 
	GPIO.cleanup()
	
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
	
	global __buttonPins
	__buttonPins = buttonDic
	
	# Set all the pins to outputs
	for pin in __buttonPins.values():
		GPIO.setup(pin, GPIO.OUT)
	
	# Set the hook as an output
	global __hookPin
	__hookPin = hook
	GPIO.setup(__hookPin, GPIO.OUT)

# Takes a single character and dials it.
def pushKey(key):
	
	global __buttonPins
	global _keyDowTime
	global _keyUpTime
	
	if key in __buttonPins:
		GPIO.output(__buttonPins[key], 1)
		time.sleep(_keyDownTime)
		GPIO.output(__buttonPins[key], 0)
		time.sleep(_keyUpTime)
	else:
		raise Exception('Invalid key: ' + str(key))

# Dials the number specified, regardless of the call state.
def dial(number):
	
	# Split up the string into the parts.
	chars = list(number)
	
	global __buttonPins
	
	# Iterate through the pushable keys.
	for k in chars:
		if k in __buttonPins:
			pushKey(k)

# Picks up the handset, which should trigger a dial tone.
def _pickup():
	
	global __hookPin
	global _hookUpTime
	
	GPIO.output(__hookPin, 1)
	time.sleep(_hookUpTime)

# Replaces the handset, usually ending a call.
def _rehook():
	
	global __hookPin
	global _hookDownTime
	
	GPIO.output(__hookPin, 0)
	time.sleep(_hookDownTime)

# Begins a call, dialing the number.
def beginCall(number):
	
	global __inCall
	
	if not __inCall:
		__inCall = True
		_pickup()
		dial(number)
	else:
		raise Exception('Can\'t begin call when in call.')

# Ends a call, putting the handset in the cradle.
def endCall():
	
	global __inCall
	
	if __inCall:
		_rehook()
		__inCall = False
		time.sleep(_hookDownTime)
	else:
		raise Exception('Need to be in call to end one.')

