import socketio

sio = socketio.Client()
sio.connect('http://20.214.250.33:8080')

@sio.event
def message(data):
    print('I received a message!');
    print(data);



s = input("메시지 적으세요")
sio.emit('message', s)

