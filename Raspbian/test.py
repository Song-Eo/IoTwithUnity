import Database as db
import stepmotor as sm
import RPi.GPIO as GPIO
import time

light1 = 17
switch = 23
baseDB = []
state = 0


GPIO.setmode(GPIO.BCM)
GPIO.setup(light1, GPIO.OUT)
GPIO.setup(switch, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


def btn_callback(channel):
	global state
	state = not state
	db.updateDB(state, "light1")

GPIO.add_event_detect(switch, GPIO.RISING, callback=btn_callback, bouncetime=300)

try:
	while(True):
		
		baseDB = db.loadDB(baseDB.clear())
		
		for i in baseDB:
			if(i[0] == "light1"):
				state = i[1]
				print(state)
				GPIO.output(light1, state)
				break
		
		time.sleep(3)

except KeyboardInterrupt:
	GPIO.cleanup()


