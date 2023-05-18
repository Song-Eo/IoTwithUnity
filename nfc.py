import serial

ser = serial.Serial(port='/dev/ttyACM0', baudrate=9600, timeout=1)

while 1:
	s = ser.readline()
	print(s)
