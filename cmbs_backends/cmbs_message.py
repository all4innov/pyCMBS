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
import cmbs_backends.backend as backend

#import pyocni.backend.backend as backend
#from pyocni.backends.backend import backend_interface
#import pyocni.pyocni_tools.config as config


# getting the Logger
#logger = config.logger


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

    def action(self, entity, action):
        '''

        Perform an action on an Entity

        '''
        if action == 'execute':
            cmbs_layer = entity['attributes']['cmbs']['message']['cmbs_layer']
            if cmbs_layer ==  'l1':
                execute_l1()
            elif cmbs_layer == 'l2':
                execute_l2()
            elif cmbs_layer == 'l31':
                execute_l31()
            elif cmbs_layer == 'l32':
                execute_l32()
            elif cmbs_layer == 'l4':
                execute_l4()
        elif action == 'send_l1':
            send_l1()
        elif action == 'send_l2':
            send_l2()
        elif action == 'send_l31':
            send_l31()
        elif action == 'send_l32':
            send_l32()
        elif action == 'send_l4':
            send_l4()

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

def send_l1():
    pass

def send_l2():
    pass

def send_l31():
    pass

def send_l32():
    pass

def send_l4():
    pass

