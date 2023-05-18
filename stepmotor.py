import RPi.GPIO as GPIO
import time

def setupStepmotor(stepPins):
	GPIO.setmode(GPIO.BCM)
	GPIO.cleanup()
	for pin in stepPins:
		GPIO.setup(pin,GPIO.OUT)
		GPIO.output(pin, False)


def rotateStepmotor(stepPins):
	stepCounter = 0
	stepCount = 4
	
	seq = [[0,0,0,1],
			[0,0,1,0],
			[0,1,0,0],
			[1,0,0,0]]
			
	for pin in range(0,4):
		xpin =  stepPins[pin]
		if seq[stepCounter][pin] != 0:
			GPIO.output(xpin, True)
		else:
			GPIO.output(xpin, False)
			
		stepCounter += 1
			
				
	time.sleep(0.01)


	
setupStepmotor([12, 16, 20, 21])
rotateStepmotor([12, 16, 20, 21])
