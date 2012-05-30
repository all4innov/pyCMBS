
import zmq



def create_broadcast_server(zmq_server='tcp://127.0.0.1:6000'):
    context = zmq.Context()
    socket = context.socket(zmq.SUB)
    socket.bind(zmq_server)
    socket.setsockopt(zmq.SUBSCRIBE, '')
    print zmq_server
    while True:
        data = socket.recv()
        print data

create_broadcast_server(zmq_server='tcp://127.0.0.1:6000')