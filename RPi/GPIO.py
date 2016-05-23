# GPIO stuf for testing TelePi.

BCM = 'bcm'
OUT = 'out'

def cleanup():
	print('GPIO cleaned up.')

def setmode(mode):
	print('GPIO mode set to: ' + str(mode))

def setwarnings(warn):
	print('GPIO warnings set to: ' + str(warn))

def setup(pin, mode):
	print('GPIO pin ' + str(pin) + ' mode set to: ' + str(mode))

def output(pin, state):
	print('GPIO pin ' + str(pin) + ' state set to ' + str(state))


