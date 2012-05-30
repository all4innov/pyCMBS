import zmq

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("tcp://127.0.0.1:5000")
socket.setsockopt(zmq.SUBSCRIBE, "portugal")
#socket.setsockopt(zmq.SUBSCRIBE, "germany")
#socket.setsockopt(zmq.SUBSCRIBE, "portugal")

while True:
    print  "->", socket.recv()
