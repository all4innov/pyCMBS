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

import pycurl
import cmbs_backends.f_entities as f_entities

import StringIO

try:
    import simplejson as json
except ImportError:
    import json

def check_socket(socket):
    c = pycurl.Curl()

    storage = StringIO.StringIO()
    c.setopt(c.URL, str(config.PyOCNI_Server_Address + "/cmbs/member/"))
    c.setopt(c.HTTPHEADER, ['Content-type: application/occi+json', 'Accept: application/occi+json'])
    c.setopt(c.VERBOSE, True)
    c.setopt(c.CUSTOMREQUEST, 'GET')
    c.setopt(c.WRITEFUNCTION, storage.write)
    c.setopt(c.POSTFIELDS, f_entities.j_cmbs_member_l1_socket_att(socket))
    c.perform()
    content = storage.getvalue()
    json_result = json.loads(content)
    # return the number of the result: 0 if no result
    return len(json_result["X-OCCI-Location"])


def check_member(id):
    c = pycurl.Curl()

    storage_header = StringIO.StringIO()
    storage_body = StringIO.StringIO()

    c.setopt(c.URL, str(config.PyOCNI_Server_Address + "/cmbs/member/" + id))
    c.setopt(c.HTTPHEADER, ['Content-type: application/occi+json', 'Accept: application/occi+json'])
    c.setopt(c.VERBOSE, True)
    c.setopt(pycurl.POSTFIELDS, "{}")
    c.setopt(c.CUSTOMREQUEST, 'GET')
    c.setopt(c.HEADERFUNCTION, storage_header.write)
    c.setopt(c.WRITEFUNCTION, storage_body.write)
    c.perform()

    if c.getinfo(pycurl.HTTP_CODE) == 404:
        return 0
    elif c.getinfo(pycurl.HTTP_CODE) == 200:
        return 1
        #json_result = json.loads(content)
        # return the number of the result: 0 if no result
        #return len(json_result["resources"])


def add_member(member_description):
    storage = StringIO.StringIO()
    c = pycurl.Curl()
    c.setopt(c.URL, config.PyOCNI_Server_Address + '/cmbs/member/')
    c.setopt(c.HTTPHEADER, ['Accept:application/occi+json', 'Content-Type: application/occi+json'])
    c.setopt(c.VERBOSE, True)

    h = {"resources": [member_description]}

    c.setopt(pycurl.POSTFIELDS, json.dumps(h))
    c.setopt(c.CUSTOMREQUEST, 'POST')
    c.setopt(c.WRITEFUNCTION, storage.write)
    c.perform()
    content = storage.getvalue()
    print " ========== Body content ==========\n " + content + " \n ==========\n"


def get_members():
    storage = StringIO.StringIO()
    c = pycurl.Curl()
    c.setopt(c.URL, config.PyOCNI_Server_Address + '/cmbs/member/')
    c.setopt(c.HTTPHEADER, ['Accept:application/occi+json', 'Content-Type: application/occi+json'])
    c.setopt(c.VERBOSE, True)
    # surtout rien dans le body car sinon ca devient un filtre
    # Nope c.setopt(pycurl.POSTFIELDS, "{}")
    c.setopt(c.CUSTOMREQUEST, 'GET')
    c.setopt(c.WRITEFUNCTION, storage.write)
    c.perform()
    content = storage.getvalue()
    # content format: {"X-OCCI-Location": ["http://127.0.0.1:8090/cmbs/member/996ad860-2a9a-504f-8861-aeafd0b2ae29"]}
    print  (config.PyOCNI_Server_Address + '/cmbs/member/')
    print " ========== Body content ==========\n " + content + " \n ==========\n"
    json_result = json.loads(content)
    return json_result["X-OCCI-Location"]


def get_members_l1_socket():
    result = []
    locations = get_members()
    for a in locations:
        storage = StringIO.StringIO()
        c = pycurl.Curl()
        c.setopt(c.URL, a)
        c.setopt(c.HTTPHEADER, ['Accept:application/occi+json', 'Content-Type: application/occi+json'])
        c.setopt(c.VERBOSE, True)
        c.setopt(pycurl.POSTFIELDS, "{}")
        c.setopt(c.CUSTOMREQUEST, 'GET')
        c.setopt(c.WRITEFUNCTION, storage.write)
        c.perform()
        content = storage.getvalue()
        # content format: {"X-OCCI-Location": ["http://127.0.0.1:8090/cmbs/member/996ad860-2a9a-504f-8861-aeafd0b2ae29"]}
        print " ========== Body content ==========\n " + content + " \n ==========\n"
        result.append(json.loads(content)['attributes']['cmbs']['member']['l1_socket'])
    return  result


def get_local_member_uri():
    c = pycurl.Curl()

    storage = StringIO.StringIO()
    c.setopt(c.URL, str(config.PyOCNI_Server_Address + "/cmbs/member/"))
    c.setopt(c.HTTPHEADER, ['Content-type: application/occi+json', 'Accept: application/occi+json'])
    c.setopt(c.VERBOSE, True)
    c.setopt(pycurl.POSTFIELDS, "{}")
    c.setopt(c.CUSTOMREQUEST, 'GET')
    c.setopt(c.WRITEFUNCTION, storage.write)
    c.setopt(c.POSTFIELDS, f_entities.j_cmbs_member_member_local_att())
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
    # should be like that but...
    #return json_result["resources"][0]
    return json_result


def get_local_member_description_for_sending(uri):
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
    # should be like that but...
    #json_result["resources"][0]["attributes"]['cmbs']['member']['local'] = 'false'
    json_result["attributes"]['cmbs']['member']['local'] = 'false'
    # should be like that but...
    #return json_result["resources"][0]
    return json_result

