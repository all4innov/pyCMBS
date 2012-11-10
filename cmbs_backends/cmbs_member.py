#  Copyright 2010-2012 Institut Mines-Telecom
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

"""
Created on Sep 01, 2011

@author: Houssem Medhioub
@contact: houssem.medhioub@it-sudparis.eu
@organization: Institut Mines-Telecom - Telecom SudParis
@license: Apache License, Version 2.0
"""

#import pyocni.backend.backend as backend
#from  backend import backend_interface
import pyocni.pyocni_tools.config as config
# getting the Logger
logger = config.logger
import cmbs_backends.backend as backend
import pycurl
import StringIO
import cmbs_backends.f_entities as f_entities
import logging
try:
    import simplejson as json
except ImportError:
    import json

from multiprocessing import Process
import time
import cStringIO
import jsonpickle
import couchdb

import zmq

import threading
from threading import Thread

# getting the Logger
#logger = config.logger

receiver_l1_state = True
receiver_l2_state = True
receiver_l31_state = True
receiver_l32_state = True
receiver_l4_state = True

class receiver_l1(threading.Thread):
    def __init__(self, name = 'l1_receiver', l1_socket='tcp://127.0.0.1:5010'):
        threading.Thread.__init__(self)
        self.name = name
        self.l1_socket = l1_socket
        global receiver_l1_state
        receiver_l1_state = True
    def run(self):

        context = zmq.Context()
        socket = context.socket(zmq.REP)
        socket.bind(self.l1_socket)

        global receiver_l1_state
        while True:
            msg = socket.recv_json()
            # to avoid receiving a message after
            if not receiver_l1_state:
                break
            print type(msg)
            print "Got", msg

            socket.send_json("{'d':'f'}")

    def stop(self):
        global receiver_l1_state
        receiver_l1_state = False

class receiver_l2(threading.Thread):
    def __init__(self, name = 'l2_receiver', l2_socket='tcp://127.0.0.1:5020'):
        threading.Thread.__init__(self)
        self.name = name
        self.l2_socket = l2_socket
        global receiver_l2_state
        receiver_l2_state = True
    def run(self):
        pass

    def stop(self):
        global receiver_l2_state
        receiver_l2_state = False

class receiver_l31(threading.Thread):
    def __init__(self, name = 'l31_receiver', l31_socket='tcp://127.0.0.1:5031'):
        threading.Thread.__init__(self)
        self.name = name
        self.l31_socket = l31_socket
        global receiver_l31_state
        receiver_l31_state = True
    def run(self):
        pass

    def stop(self):
        global receiver_l31_state
        receiver_l31_state = False

class receiver_l32(threading.Thread):
    def __init__(self, name = 'l32_receiver', l32_socket='tcp://127.0.0.1:5032'):
        threading.Thread.__init__(self)
        self.name = name
        self.l32_socket = l32_socket
        global receiver_l32_state
        receiver_l32_state = True
    def run(self):
        pass

    def stop(self):
        global receiver_l32_state
        receiver_l32_state = False

class receiver_l4(threading.Thread):
    def __init__(self, name = 'l4_receiver', l4_socket='tcp://127.0.0.1:5040'):
        threading.Thread.__init__(self)
        self.name = name
        self.l4_socket = l4_socket
        global receiver_l4_state
        receiver_l4_state = True
    def run(self):
        pass

    def stop(self):
        global receiver_l4_state
        receiver_l4_state = False

def check_neighbors(neighbors_socket):
    while len(neighbors_socket) > 0:
        socket = neighbors_socket[0]

        if check_socket(socket) > 0:
            logger.debug("The member with the socket: " + str(socket) + " is already known.")
        else:
            logger.debug("The member with the socket: " + str(socket) + " is unknown. A discoverty request will be sent.")
        del neighbors_socket[0]


def check_socket(socket):
    c = pycurl.Curl()

    storage = StringIO.StringIO()
    c.setopt(c.URL, str(config.PyOCNI_Server_Address + "/cmbs/member/"))
    c.setopt(c.HTTPHEADER, ['Content-type: application/occi+json', 'Accept: application/occi+json'])
    c.setopt(c.VERBOSE, True)
    c.setopt(c.CUSTOMREQUEST, 'GET')
    c.setopt(c.WRITEFUNCTION, storage.write)
    c.setopt(c.POSTFIELDS,f_entities.j_cmbs_member_l1_socket_att(socket))
    c.perform()
    content = storage.getvalue()
    json_result = json.loads(content)
    # return the number of the result: 0 if no result
    return len(json_result["X-OCCI-Location"])

class backend(backend.backend_interface):
    receiver_l1_ins = receiver_l1(name='l1_receiver')
    receiver_l1_ins.daemon = True
    receiver_l2_ins = receiver_l2(name='l2_receiver')
    receiver_l2_ins.daemon = True
    receiver_l31_ins = receiver_l31(name='l31_receiver')
    receiver_l31_ins.daemon = True
    receiver_l32_ins = receiver_l32(name='l32_receiver')
    receiver_l32_ins.daemon = True
    receiver_l4_ins = receiver_l4(name='l4_receiver')
    receiver_l4_ins.daemon = True

    def create(self, entity):
        '''

        Create an entity (Resource or Link)

        '''

    #        logger.debug('The create operation of the cmbs_member_backend')

    def read(self, entity):
        '''

        Get the Entity's information

        '''
    #        logger.debug('The read operation of the cmbs_member_backend')

    def update(self, old_entity, new_entity):
        '''

        Update an Entity's information

        '''
    #        logger.debug('The update operation of the cmbs_member_backend')

    def delete(self, entity):
        '''

        Delete an Entity

        '''
    #        logger.debug('The delete operation of the cmbs_member_backend')

    def action(self, entity, action, attributes):
        '''

        Perform an action on an Entity

        '''

        if action == 'check_neighbors':
            neighbors_socket = entity['attributes']['cmbs']['member']['neighbors_socket']
            #check_neighbors(neighbors_socket)
            t = Thread(target=check_neighbors, args=(neighbors_socket,))
            t.start()
        elif action == 'start_l1':
            self.receiver_l1_ins.start()
        elif action == 'start_l2':
            self.receiver_l2_ins.start()
        elif action == 'start_l31':
            self.receiver_l31_ins.start()
        elif action == 'start_l32':
            self.receiver_l32_ins.start()
        elif action == 'start_l4':
            self.receiver_l4_ins.start()
        elif action == 'stop_l1':
            self.receiver_l1_ins.stop()
        elif action == 'stop_l2':
            self.receiver_l2_ins.stop()
        elif action == 'stop_l31':
            self.receiver_l31_ins.stop()
        elif action == 'stop_l32':
            self.receiver_l32_ins.stop()
        elif action == 'stop_l4':
            self.receiver_l4_ins.stop()
#        logger.debug('The Entity\'s action operation of the cmbs_member_backend')


if __name__ == "__main__":
    import atexit
    a = atexit
    a.register(backend)
    print "ddddd" + str(a.register(backend))
    check_socket("tcp://127.0.0.1:5010")
