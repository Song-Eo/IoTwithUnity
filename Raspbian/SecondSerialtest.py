import serial

ser = serial.Serial(port='/dev/ttyUSB0', baudrate=9600, timeout=1)

while(True):
	if(ser.readable()):
		message = ser.readline().decode()
		print(message)
