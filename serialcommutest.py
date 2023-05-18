import serial
import socketio

ser = serial.Serial(port='/dev/ttyACM0', baudrate=9600, timeout=1)

sio = socketio.Client()
sio.connect("http://20.214.250.33:8080")

global dat

@sio.on('response_data')
def response_data(data):
	dat = data
	for i in dat:
		if(i['name'] == 'gas_level'):
			s = str(i['state'])
			ser.write(bytes(s.encode()))
			print(i['state'])
if(ser.read()):
	print(ser.readline())

'''@sio.event
def message(data):
	dat = data
	for i in dat:
		if(i['name'] == 'gas_level'):
			print(i['state'])'''
			
if KeyboardInterrupt:
	ser.write("0".encode()  )



