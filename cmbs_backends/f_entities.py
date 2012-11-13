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

try:
    import simplejson as json
except ImportError:
    import json

def j_cmbs_member_l1_socket_att(socket):
    return """
    {
        "resources": [
            {
                "attributes": {
                    "cmbs": {
                        "member": {
                            "l1_socket": \""""  + str(socket) +  """\"
                        }
                    }
                }
            }
        ]
    }
    """

def j_cmbs_member_member_local_att():
    return """
    {
        "resources": [
            {
                "attributes": {
                    "cmbs": {
                        "member": {
                            "local": "true"
                        }
                    }
                }
            }
        ]
    }
    """

def j_cmbs_message(l1_socket_receiver_member, id):
    return """{
    "resources": [
        {
            "kind": "http://houssem.org/cmbs#message",
            "mixins": [
                "http://houssem.org/cmbs#l1"
            ],
            "attributes": {
                "cmbs": {
                    "message": {
                        "cmbs_layer": "l1",
                        "executable": "True",
                        "sendable": "True",
                        "storable": "True",
                        "path_history": [],
                        "message_content": "",
                        "l1_socket_receiver_member": \"""" + l1_socket_receiver_member + """\",
                        "result": ""
                    }
                }
            },
            "actions": [],
            "id": \"""" + id + """\",
            "title": "l1 CMBS message",
            "summary": "This is a L1 CMBS message",
            "links": []
        }
    ]
}
"""
def j_cmbs_message_update_result(result):
    return """{
    "resources": [
        {
            "attributes": {
                "cmbs": {
                    "message": {
                        "result": """ + result + """
                    }
                }
            }
        }
    ]
}
"""
if __name__ == '__main__':
    #print (j_cmbs_member_l1_socket_att("a"))
    print j_cmbs_message_update_result({"a":"b"})