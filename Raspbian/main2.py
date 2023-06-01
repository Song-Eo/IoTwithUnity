import serial
import socketio

ser1 = serial.Serial(port='/dev/ttyACM0', baudrate=9600, timeout=1)

sio = socketio.Client()
sio.connect("http://20.214.250.33:8080")

dat = None
changed_data = True
count = 0

@sio.on('response_data')
def response_data(data):
	global changed_data
	global dat
	dat = data
	changed_data = True
	
def change_state():
	print("changed")
	global dat
	global changed_data
	for d in dat:
		if(d['name'] == 'gas_level'):
			print(d['state'])
			s = str(d['state'])
			ser1.write((s.encode()))
	changed_data = False
			
			
sio.emit('request_data')
print('request_data')

while(True):
	print("change_data : ", changed_data, "  count : ", count)
	
	if(ser1.readable()):
		message = ser1.readline().decode()
		print(message)
		if(message == "rain"):
			sio.emit("update", {"name":"rain", "state":"1"})
			print(message)
		elif(message == 'mois'):
			sio.emit("update", {"name":"mois", "state":"1"})
			print(message)
		elif(message == 'undetect'):
			sio.emit("update", {"name":"detect", "state":"1"})
			print(message)
		elif(message == "rfid_first"):
			sio.emit("update", {"name":"rfid", "state":"1"})
			print(message)

	
	if(changed_data == True):
		change_state()
		
	
	
