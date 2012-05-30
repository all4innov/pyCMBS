# http://code.saghul.net/implementing-a-pubsub-based-application-with

# consumer

import zmq

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.bind('tcp://127.0.0.1:5001')
socket.setsockopt(zmq.SUBSCRIBE, 'test')
socket.setsockopt(zmq.SUBSCRIBE, 'topic_1')

while True:
    data = socket.recv()
    print data
