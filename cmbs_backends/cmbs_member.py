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

import pyocni.pyocni_tools.config as config
# getting the Logger
logger = config.logger

import cmbs_backends.backend as backend
import cmbs_backends.f_entities as f_entities
import cmbs_backends.member_rest as member_rest
import cmbs_backends.message_rest as message_rest

try:
    import simplejson as json
except ImportError:
    import json

import zmq

import threading
from threading import Thread

import uuid

if not ('receiver_l1_state' in globals()):  receiver_l1_state = True
if not ('receiver_l2_state' in globals()):  receiver_l2_state = True
if not ('receiver_l31_state' in globals()): receiver_l31_state = True
if not ('receiver_l32_state' in globals()): receiver_l32_state = True
if not ('receiver_l4_state' in globals()):  receiver_l4_state = True

if not ('receiver_l1_socket' in globals()):  receiver_l1_socket = ''
if not ('receiver_l2_socket' in globals()):  receiver_l2_socket = ''
if not ('receiver_l31_socket' in globals()): receiver_l31_socket = ''
if not ('receiver_l32_socket' in globals()): receiver_l32_socket = ''
if not ('receiver_l4_socket' in globals()):  receiver_l4_socket = ''

def get_UUID():
    _uuid = str(uuid.uuid1())
    #_uuid = str(uuid.uuid4())
    return _uuid


class receiver_l1(threading.Thread):
    def __init__(self, name='', l1_socket=''):
        threading.Thread.__init__(self)
        self.name = name
        self.l1_socket = l1_socket
        global receiver_l1_state
        receiver_l1_state = True

    def run(self):
        context = zmq.Context()
        socket = context.socket(zmq.REP)
        global receiver_l1_socket
        socket.bind(receiver_l1_socket)

        global receiver_l1_state
        while True:
            msg = socket.recv_json()
            # an if to avoid executing a message after stopping the receiver
            if not receiver_l1_state:  break

            if member_rest.check_member(msg['attributes']['cmbs']['message']['message_content']['id']) > 0:
                logger.debug("This provider is already know.")
            else:
                logger.debug("Adding the received member description to the DB.")
                member_rest.add_member(msg['attributes']['cmbs']['message']['message_content'])


            response = {"member_description": member_rest.get_local_member_description_for_sending(member_rest.get_local_member_uri()),
                        "sockets_l1": member_rest.get_members_l1_socket()}

            socket.send_json(response)

    def stop(self):
        global receiver_l1_state
        receiver_l1_state = False


class receiver_l2(threading.Thread):
    def __init__(self, name='l2_receiver', l2_socket='tcp://127.0.0.1:5020'):
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
    def __init__(self, name='l31_receiver', l31_socket='tcp://127.0.0.1:5031'):
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
    def __init__(self, name='l32_receiver', l32_socket='tcp://127.0.0.1:5032'):
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
    def __init__(self, name='l4_receiver', l4_socket='tcp://127.0.0.1:5040'):
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

        if member_rest.check_socket(socket) > 0:
            logger.debug("The member with the socket: " + str(socket) + " is already known.")
        else:
            logger.debug(
                "The member with the socket: " + str(socket) + " is unknown. A discovery request will be sent.")

            mes_id = get_UUID()
            mes = f_entities.j_cmbs_message(socket, mes_id)
            location = message_rest.add_message(mes)

            content = message_rest.send_l1_message_get_result(location)

            member_rest.add_member(content["member_description"])
            for soc in content["sockets_l1"]:
                if member_rest.check_socket(soc) > 0:
                    logger.debug("The member with the socket: " + str(socket) + " is already known.")
                else:
                    logger.debug("adding the cloud provider with the : " + str(
                        socket) + " to the list of neighbors_socket that will be discovered.")
                    neighbors_socket.append(soc)

        del neighbors_socket[0]

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

    def __init__(self):
        pass

    def create(self, entity):
        '''

        Create an entity (Resource or Link)

        '''

        # if this member is the local and first member
        if entity['attributes']['cmbs']['member']['local'] == 'true':
            global receiver_l1_socket
            receiver_l1_socket = entity['attributes']['cmbs']['member']['l1_socket']
            global receiver_l2_socket
            receiver_l2_socket = entity['attributes']['cmbs']['member']['l2_socket']
            global receiver_l31_socket
            receiver_l31_socket = entity['attributes']['cmbs']['member']['l31_socket']
            global receiver_l32_socket
            receiver_l32_socket = entity['attributes']['cmbs']['member']['l32_socket']
            global receiver_l4_socket
            receiver_l4_socket = entity['attributes']['cmbs']['member']['l4_socket']


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
    #check_socket("tcp://127.0.0.1:5010")
    #check_member("996ad860-2a9a-504f-8861-aeafd0b2ae29")
    #get_members()
    #print get_UUID()
    #add_message(f_entities.j_cmbs_message("",get_UUID()))
    #print get_members()
    #print get_members_l1_socket()
    pass