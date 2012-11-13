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

import time

import pycurl
import StringIO
import cmbs_backends.f_entities as f_entities

try:
    import simplejson as json
except ImportError:
    import json

import cmbs_backends.backend as backend

import zmq

import threading
from threading import Thread

#import pyocni.backend.backend as backend
#from pyocni.backends.backend import backend_interface
#import pyocni.pyocni_tools.config as config



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
        elif action == 'send_l1' and cmbs_layer == 'l1' and entity['attributes']['cmbs']['message']['sendable'] == 'True':
            sen_l1 = Thread(target=send_l1, args=(entity['attributes']['cmbs']['message']['l1_socket_receiver_member'], entity))
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
#    try:
        print "EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE"
        print type(entity)
        print entity
        print "EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE"
        #entity = json.loads(entity)
        print '***************************************************'
        Q = get_local_member_uri()
        print type(Q)
        print Q
        print "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
        H = get_local_member_description(Q)
        print type(H)
        print H
        print 'JJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJ'
        entity['attributes']['cmbs']['message']['message_content'] = H
        print "##################################################"
        print "##################################################"
        entity['attributes']['cmbs']['message']['path_history'].append(get_local_member_uri())
        context = zmq.Context()
        socket = context.socket(zmq.REQ)
        socket.connect(zmq_server)
        logger.debug("sending the request to the server.")
        print 'QWWQWQWQWQWQWQWQWQWQWQWQWQWQWQWQWQWQWQWQWQWQ'
        print 'QWWQWQWQWQWQWQWQWQWQWQWQWQWQWQWQWQWQWQWQWQWQ'
        print type(entity)
        print entity

        socket.send_json(entity)
        logger.debug('Receiving the replay:')
        msg_in = socket.recv_json()
        print 'COOOOOOOOOOOOOOOOOCMMMMMMMMMMMMMMMMMMMMMMMMM'
        print type(msg_in)
        print msg_in

        entity['attributes']['cmbs']['message']['result'] = msg_in
        update_message(entity)


        #return msg_in
#    except Exception as e:
#        logger.error("Error on the send_l1 request: " + str(e))


def send_l2():
    pass


def send_l31():
    pass


def send_l32():
    pass


def send_l4():
    pass

def get_local_member_uri():
    c = pycurl.Curl()

    storage = StringIO.StringIO()
    c.setopt(c.URL, str(config.PyOCNI_Server_Address + "/cmbs/member/"))
    c.setopt(c.HTTPHEADER, ['Content-type: application/occi+json', 'Accept: application/occi+json'])
    c.setopt(c.VERBOSE, True)
    c.setopt(c.CUSTOMREQUEST, 'GET')
    c.setopt(c.WRITEFUNCTION, storage.write)
    c.setopt(c.POSTFIELDS,f_entities.j_cmbs_member_member_local_att())
    c.perform()
    content = storage.getvalue()
    json_result = json.loads(content)
    return json_result["X-OCCI-Location"][0]

def get_local_member_description(uri):
    c = pycurl.Curl()

    storage = StringIO.StringIO()
    c.setopt(c.URL, str(uri))
    c.setopt(c.HTTPHEADER, ['Content-type: application/occi+json', 'Accept: application/occi+json'])
    c.setopt(c.VERBOSE, True)
    c.setopt(pycurl.POSTFIELDS, "{}")
    c.setopt(c.CUSTOMREQUEST, 'GET')
    c.setopt(c.WRITEFUNCTION, storage.write)
    c.perform()
    content = storage.getvalue()
    json_result = json.loads(content)
    print 'WSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSDDDDDDDDDDDDd'
    print json_result
    # should be like that but...
    #json_result["resources"][0]["attributes"]['cmbs']['member']['local'] = 'false'
    json_result["attributes"]['cmbs']['member']['local'] = 'false'
    # should be like that but...
    #return json_result["resources"][0]
    return json_result

def update_partial_message(uri, result):
    print '666666666666666666666666666666666666666666666666666666666666666666666666'
    print type(result)
    print result
    print '555555555555555555555555555555555555555555555555555555555555555555555555'
    print type(f_entities.j_cmbs_message_update_result(result))
    print (f_entities.j_cmbs_message_update_result(result))

    print '4444444444444444444444444444444444444444444444444444'
    print str(config.PyOCNI_Server_Address + "/cmbs/message/" + uri)

    c = pycurl.Curl()

    storage = StringIO.StringIO()
    c.setopt(c.URL, str(config.PyOCNI_Server_Address + "/cmbs/message/" + uri))
    c.setopt(c.HTTPHEADER, ['Content-type: application/occi+json', 'Accept: application/occi+json'])
    c.setopt(c.VERBOSE, True)
    c.setopt(c.CUSTOMREQUEST, 'POST')
    c.setopt(c.WRITEFUNCTION, storage.write)
    x = str(f_entities.j_cmbs_message_update_result(result))
    print 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx'
    print type(x)
    print x
    c.setopt(c.POSTFIELDS,x)
    c.perform()
    content = storage.getvalue()
    return content

def update_message(entity):
    c = pycurl.Curl()

    storage = StringIO.StringIO()
    c.setopt(c.URL, str(config.PyOCNI_Server_Address + "/cmbs/message/" + entity["id"]))
    c.setopt(c.HTTPHEADER, ['Content-type: application/occi+json', 'Accept: application/occi+json'])
    c.setopt(c.VERBOSE, True)
    c.setopt(c.CUSTOMREQUEST, 'PUT')
    c.setopt(c.WRITEFUNCTION, storage.write)
    H = { "resources": []}
    H["resources"].append(entity)

    print '==================================================================='
    print '==================================================================='
    print '==================================================================='
    print json.dumps(H)
    #print json.dumps(entity)
    c.setopt(c.POSTFIELDS,json.dumps(H))
    c.perform()
    content = storage.getvalue()
    print " ========== Body content of the update message ==========\n " + content + " \n ==========\n"
    time.sleep(5)

if __name__ == "__main__":
    #send_l1(zmq_server='tcp://127.0.0.1:6010', entity='{"a":"b"}')
    pass
