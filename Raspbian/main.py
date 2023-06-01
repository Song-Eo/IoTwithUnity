import serial
import socketio

ser1 = serial.Serial(port='/dev/ttyACM0', baudrate=9600, timeout=1)
ser2 = serial.Serial(port='/dev/ttyUSB0', baudrate=9600, timeout=1)

sio = socketio.Client()
sio.connect("http://20.214.250.33:8080")

dat = None
changed_data = True
count = 0
count2 = 0

@sio.on('response_data')
def response_data(data):
	global dat
	dat = data
	changed_data = True
	
def change_state():
	global dat
	for d in dat:
		if(d['name'] == 'gas_level'):
			s = str(d['state'])
			ser1.write(bytes(s.encode()))
				
	changed_data - False
			
			
sio.emit('request_data')
print('request_data')

while(True):
	if(ser2.readable() and not count == 3):
		message = ser2.readline().decode()
		print(message)
		if(message == "rain"):
			sio.emit("update", {"name":"rain", "state":"1"})
			count += 1
		elif(message == 'mois'):
			sio.emit("update", {"name":"mois", "state":"1"})
			count += 1
		elif(message == 'undetect'):
			sio.emit("update", {"name":"detect", "state":"1"})
			count += 1
			
	if(ser1.readable() and not count2 == 1):
		message = ser1.readline().decode()
		if(message == "rfid"):
			sio.emit("update", {"name":"detect", "state":"1"})
			count2 += 1
	
	if(changed_data):
		change_state()
		
	
	
	if KeyboardInterrupt:
		ser1.write("0".encode())
