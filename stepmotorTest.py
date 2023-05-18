import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
stepPins = [19, 16, 20, 21]

for pin in stepPins:
	GPIO.setup(pin,GPIO.OUT)
	GPIO.output(pin, False)
	
stepCounter = 0
stepCount = 4

seq = [[1,0,0,0],
		[0,1,0,0],
		[0,0,1,0],
		[0,0,0,1]]
			
try:
	while 1:
		for pin in range(0,4):
			xpin = stepPins[pin]
			if seq[stepCounter][pin] != 0:
				GPIO.output(xpin, True)
			else:
				GPIO.output(xpin, False)
			
		stepCounter += 1
			
		if(stepCounter == stepCount):
			stepCounter = 0
		if(stepCounter<0):
			stepCounter = stepCount
		time.sleep(0.01)
		
except KeyboardInterrupt:
	GPIO.cleanup()
