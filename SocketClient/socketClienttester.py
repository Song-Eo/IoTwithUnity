import socketio

sio = socketio.Client()
sio.connect('http://20.214.250.33:8080')


@sio.event
def response_data(data):
    print('I received a message!')
    print(data)


sio.emit('request_data')

