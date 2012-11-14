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
import cmbs_backends.member_rest as member_rest
import cmbs_backends.message_rest as message_rest


try:
    import simplejson as json
except ImportError:
    import json

import zmq

from threading import Thread

def execute_l1():
    pass


def execute_l2():
    pass


def execute_l31():
    pass


def execute_l32():
    pass


def execute_l4():
    pass


def send_l1(zmq_server, entity):
    try:
        Q = member_rest.get_local_member_uri()
        H = member_rest.get_local_member_description_for_sending(Q)
        entity['attributes']['cmbs']['message']['message_content'] = H
        entity['attributes']['cmbs']['message']['path_history'].append(member_rest.get_local_member_uri())
        context = zmq.Context()
        socket = context.socket(zmq.REQ)
        socket.connect(zmq_server)
        logger.debug("sending the request to the server.")

        socket.send_json(entity)
        logger.debug('Receiving the replay:')
        msg_in = socket.recv_json()

        entity['attributes']['cmbs']['message']['result'] = msg_in
        message_rest.update_message(entity)

    except Exception as e:
        logger.warning("Error on the send_l1 request: " + str(e))


def send_l2():
    pass


def send_l31():
    pass


def send_l32():
    pass


def send_l4():
    pass


class backend(backend.backend_interface):
    def create(self, entity):
        '''

        Create an entity (Resource or Link)

        '''

    #        logger.debug('The create operation of the cmbs_message_backend')

    def read(self, entity):
        '''

        Get the Entity's information

        '''

    #        logger.debug('The read operation of the cmbs_message_backend')

    def update(self, old_entity, new_entity):
        '''

        Update an Entity's information

        '''

    #        logger.debug('The update operation of the cmbs_message_backend')

    def delete(self, entity):
        '''

        Delete an Entity

        '''

    #        logger.debug('The delete operation of the cmbs_message_backend')

    def action(self, entity, action, attributes):
        '''

        Perform an action on an Entity

        '''
        cmbs_layer = entity['attributes']['cmbs']['message']['cmbs_layer']
        if action == 'execute':
            if cmbs_layer == 'l1':
                exe_l1 = Thread(target=execute_l1, args=())
                exe_l1.start()
            elif cmbs_layer == 'l2':
                exe_l2 = Thread(target=execute_l2, args=())
                exe_l2.start()
            elif cmbs_layer == 'l31':
                exe_l31 = Thread(target=execute_l31, args=())
                exe_l31.start()
            elif cmbs_layer == 'l32':
                exe_l32 = Thread(target=execute_l32, args=())
                exe_l32.start()
            elif cmbs_layer == 'l4':
                exe_l4 = Thread(target=execute_l4, args=())
                exe_l4.start()
        elif action == 'send_l1' and cmbs_layer == 'l1' and\
             entity['attributes']['cmbs']['message']['sendable'] == 'True':
            sen_l1 = Thread(target=send_l1,
                args=(entity['attributes']['cmbs']['message']['l1_socket_receiver_member'], entity))
            sen_l1.start()
        elif action == 'send_l2' and cmbs_layer == 'l2':
            sen_l2 = Thread(target=send_l2, args=())
            sen_l2.start()
        elif action == 'send_l31' and cmbs_layer == 'l31':
            sen_l31 = Thread(target=send_l31, args=())
            sen_l31.start()
        elif action == 'send_l32' and cmbs_layer == 'l32':
            sen_l32 = Thread(target=send_l32, args=())
            sen_l32.start()
        elif action == 'send_l4' and cmbs_layer == 'l4':
            sen_l4 = Thread(target=send_l4, args=())
            sen_l4.start()

#        logger.debug('The Entity\'s action operation of the cmbs_message_backend')


if __name__ == "__main__":
    pass
