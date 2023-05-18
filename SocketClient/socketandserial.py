import serial
import socketio


ser = serial.Serial(port='/dev/ttyACM3', baudrate=9600, timeout=1)

sio = socketio.Client()
sio.connect('http://20.214.250.33:8080')

global dat


@sio.on('response_data')
def response_data(data):
    dat = data
    for i in dat:
        if(i['name'] == 'gas_level'):
            print(i['state'])
            s = str(i['state'])
            ser.write(s.encode())

            

