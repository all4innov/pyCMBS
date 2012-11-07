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
#import pyocni.pyocni_tools.config as config
import cmbs_backends.backend as backend

try:
    import simplejson as json
except ImportError:
    import json

import cStringIO
import jsonpickle
import couchdb

import zmq

from threading import Thread

# getting the Logger
#logger = config.logger

class backend(backend.backend_interface):
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
            print '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'
            print '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'
            print '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'
            print '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'
            print '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'
            check_neighbors()
        elif action == 'start_l1':
            start_l1()
        elif action == 'start_l2':
            start_l2()
        elif action == 'start_l31':
            start_l31()
        elif action == 'start_l32':
            start_l32()
        elif action == 'start_l4':
            start_l4()

#        logger.debug('The Entity\'s action operation of the cmbs_member_backend')

def check_neighbors():
    pass

def start_l1(l1_socket='tcp://127.0.0.1:5010'):
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind(l1_socket)

    while True:
        msg = socket.recv_json()
        print type(msg)
        print "Got", msg
        l1_socket = msg['attributes']['cmbs']['member']["l1_socket"]

        s = "l1_socket"
        map_fun = 'function(doc) { emit(doc["OCCI_Description"]["attributes"]["cmbs"]["member"]["' + s + '"], null);  }'
        results = db.query(map_fun, key=l1_socket)


        if len(results) > 0:
            logger.debug("The CMBS member with socket: " + l1_socket + ' is already know.')
        else:
            logger.debug("adding the received CP description to the DB")
            db.save(msg)

        logger.debug("extracting all knowed CP from DB")
        s = "ocni.cp.dcp_discovery_socket"
        map_fun = 'function(doc) { emit(doc["attributes"]["' + s + '"], null);  }'
        results = db.query(map_fun)
        res = set()
        print 'the results.total_rows: ' + str(results.total_rows)
        if results.total_rows > 0:
            for q in results.rows:
                print q
                res.add(q.key)

        h = {"description_provider": initialisation_data, "values": list(res)}
        #result_dump = cStringIO.StringIO()
        #json.dump(h, result_dump, indent=4 * ' ')
        #print 'OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO'
        print type(h)
        print h

        #print 'YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYyYYYYYYYYYYYYYYYYYYYYYyy'
        #print type(result_dump.getvalue())
        #print result_dump.getvalue()
        logger.debug("sending this result to the client: ")
        #socket.send_json(result_dump.getvalue())
        socket.send_json(h)


def start_l2():
    pass

def start_l31():
    pass

def start_l32():
    pass

def start_l4():
    pass

