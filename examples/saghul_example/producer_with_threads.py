# http://code.saghul.net/implementing-a-pubsub-based-application-with

# producer

import os
import random
import threading
import time
import zmq


context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.setsockopt(zmq.LINGER, 0)    # discard unsent messages on close
socket.connect('tcp://127.0.0.1:5000')

stop_event = threading.Event()

def run():
    while not stop_event.is_set():
        msg = 'test Hello from process %s and thread %s' % (os.getpid(), threading.current_thread())
        socket.send(msg)
        time.sleep(random.randint(1, 5))

threads = []
for i in xrange(1, 11):
    t = threading.Thread(target=run)
    t.start()
    threads.append(t)

while True:
    msg = raw_input('> ')
    if msg == 'quit':
        break

stop_event.set()
[t.join() for t in threads]
socket.close()
