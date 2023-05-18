import serial

ser = serial.Serial(port='/dev/ttyACM2', baudrate=9600, timeout=1)

while 1:
	s = (input("what want you say : "))
	ser.write(bytes(s.encode()))
	
