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

import time
import pycurl
import cmbs_backends.f_entities as f_entities

import StringIO

try:
    import simplejson as json
except ImportError:
    import json

import pyocni.pyocni_tools.config as config
# getting the Logger
logger = config.logger

def update_partial_message(uri, result):
    c = pycurl.Curl()

    storage = StringIO.StringIO()
    c.setopt(c.URL, str(config.PyOCNI_Server_Address + "/cmbs/message/" + uri))
    c.setopt(c.HTTPHEADER, ['Content-type: application/occi+json', 'Accept: application/occi+json'])
    c.setopt(c.VERBOSE, True)
    c.setopt(c.CUSTOMREQUEST, 'POST')
    c.setopt(c.WRITEFUNCTION, storage.write)
    x = str(f_entities.j_cmbs_message_update_result(result))
    c.setopt(c.POSTFIELDS, x)
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
    H = {"resources": []}
    H["resources"].append(entity)

    c.setopt(c.POSTFIELDS, json.dumps(H))
    c.perform()
    content = storage.getvalue()
    print " ========== Body content of the update message ==========\n " + content + " \n ==========\n"

def add_message(message_description):
    storage = StringIO.StringIO()
    c = pycurl.Curl()
    c.setopt(c.URL, config.PyOCNI_Server_Address + "/cmbs/message/")
    c.setopt(c.HTTPHEADER, ['Accept:application/occi+json', 'Content-Type: application/occi+json'])
    c.setopt(c.VERBOSE, True)
    c.setopt(pycurl.POSTFIELDS, message_description)
    c.setopt(c.CUSTOMREQUEST, 'POST')
    c.setopt(c.WRITEFUNCTION, storage.write)
    c.perform()
    content = storage.getvalue()
    json_result = json.loads(content)
    print " ========== Body content ==========\n " + content + " \n ==========\n"
    return json_result["Location"][0]


def send_l1_message(location):
    storage = StringIO.StringIO()
    c = pycurl.Curl()
    print location
    c.setopt(c.URL, location + "?action=send_l1")
    c.setopt(c.HTTPHEADER, ['Accept:application/occi+json', 'Content-Type: application/occi+json'])
    c.setopt(c.VERBOSE, True)
    c.setopt(pycurl.POSTFIELDS, "{}")
    c.setopt(c.CUSTOMREQUEST, 'POST')
    c.setopt(c.WRITEFUNCTION, storage.write)

    c.perform()
    content = storage.getvalue()
    print " ========== Body content ==========\n " + content + " \n ==========\n"


def get_result_from_message(location):
    c = pycurl.Curl()

    storage = StringIO.StringIO()
    c.setopt(c.URL, str(location))
    c.setopt(c.HTTPHEADER, ['Content-type: application/occi+json', 'Accept: application/occi+json'])
    c.setopt(c.VERBOSE, True)
    c.setopt(pycurl.POSTFIELDS, "{}")
    c.setopt(c.CUSTOMREQUEST, 'GET')
    c.setopt(c.WRITEFUNCTION, storage.write)
    c.perform()
    content = storage.getvalue()
    json_result = json.loads(content)
    # should be like that but...
    #return json_result["resources"][0]
    a = json_result['attributes']['cmbs']['message']['result']
    return a

def send_l1_message_get_result(location):
    send_l1_message(location)

    result_received = False
    res = ''
    while not result_received:
        res = get_result_from_message(location)
        if len(res) < 0.5:
            time.sleep(0.5)
        else:
            result_received = True
    return res