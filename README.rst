==========================================================
 pyCMBS - Python Cloud Message Brokering Service
==========================================================

:Version: 0.2
:Source: https://github.com/jordan-developer/pyCMBS
:Keywords: CMBS, Message Brokering, Message pattern, OCCI, REST, Interface, HTTP, JSON, CouchDB, Eventlet, Webob, Cloud Computing

Developers
==========

Copyright (C) Houssem Medhioub <houssem.medhioub@it-sudparis.eu>

Redistribution of this software is permitted under the terms of the Apache License, Version 2.0

Table of Contents
=================

::

  0. What is it?
  1. The Latest Version
  2. API Documentation
  3. Installation
    3.1. Requirements
    3.2. Install
    3.3. Configuration
    3.4. Server running
  4. HowTo use (examples)
  5. For developers
  6. Licensing
  7. Contacts
  8. Acknowledgment
  9. Todo


0. What is it?
==============

pyCMBS (Python Cloud Message Brokering Service): A Python implementation of CMBS.


1. The Latest Version
=====================

version 0.2


2. API Documentation
====================
the api documentation are available through this html file:
pyCMBS/pyocni/doc/index.html

3. Installation
===============

3.1. Requirements
-----------------
This software needs this packages to run:

* python <= 2.7
* python-all-dev (for eventlet/greenlet install/make)
* python-setuptools (to execute the setup.py file)
* pyOCNI >= 0.4
* couchdb >= 1.2.0:
Example of installing couchdb using build-couchdb on Ubuntu (more details on: https://github.com/iriscouch/build-couchdb)
::

    sudo apt-get install help2man make gcc zlib1g-dev libssl-dev rake help2man
    git clone git://github.com/iriscouch/build-couchdb
    cd build-couchdb
    git submodule init
    git submodule update
    rake
    build/bin/couchdb

To test CouchDB:       http://127.0.0.1:5984

To test CouchDB GUI:   http://127.0.0.1:5984/_utils/


3.2. Install
------------
::

   sudo python setup.py install

3.3. Configuration
------------------

* Logger configuration:  OCCILogging.conf
* Server configuration:  occi_server.conf
* CouchDB configuration: couchdb_server.conf

3.4. Server running
-------------------
::

   sudo python start.py

4. HowTo use (examples. The json files are at the end of this README)
=====================================================================

4.1. Member category
--------------------

Creation of the 'member' kind::

    curl -X POST -d@post_category_cmbs_member.json -H 'content-type: application/occi+json' -H 'accept: application/occi+json' --user user_1:pass -v http://127.0.0.1:8090/-/

post_category_cmbs_member.json::

    {
            "actions": [
                {
                    "term": "start_l1",
                    "scheme": "http://houssem.org/cmbs/member/action#",
                    "title": "start the L1 of the member instance",
                    "attributes": {}
                },
                {
                    "term": "start_l2",
                    "scheme": "http://houssem.org/cmbs/member/action#",
                    "title": "start the L2 of the member instance",
                    "attributes": {}
                },
                {
                    "term": "start_l3.1",
                    "scheme": "http://houssem.org/cmbs/member/action#",
                    "title": "start the L3.1 of the member instance",
                    "attributes": {}
                },
                {
                    "term": "start_l3.2",
                    "scheme": "http://houssem.org/cmbs/member/action#",
                    "title": "start the L3.2 of the member instance",
                    "attributes": {}
                },
                {
                    "term": "start_l4",
                    "scheme": "http://houssem.org/cmbs/member/action#",
                    "title": "start the L4 of the member instance",
                    "attributes": {}
                },
                {
                    "term": "check_neighbors",
                    "scheme": "http://houssem.org/cmbs/member/action#",
                    "title": "check the neighbors member and try to get their description",
                    "attributes": {}
                }
            ],
            "kinds": [
                {
                    "term": "member",
                    "scheme": "http://houssem.org/cmbs#",
                    "title": "member of CMBS",
                    "attributes": {
                        "cmbs": {
                            "member": {
                                "state": {
                                    "mutable": true,
                                    "required": false,
                                    "type": "String",
                                    "pattern": "active|inactive|suspended|failed",
                                    "default": "inactive"
                                },
                                "l1_socket": {
                                    "mutable": true,
                                    "required": false,
                                    "type": "String",
                                    "pattern": "(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\\\\-]*[a-zA-Z0-9])\\\\.)*",
                                    "default": "tcp://127.0.0.1:5010"

                                },
                                "l2_socket": {
                                    "mutable": true,
                                    "required": false,
                                    "type": "String",
                                    "pattern": "(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\\\\-]*[a-zA-Z0-9])\\\\.)*",
                                    "default": "tcp://127.0.0.1:5020"

                                },
                                "l3.1_socket": {
                                    "mutable": true,
                                    "required": false,
                                    "type": "String",
                                    "pattern": "(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\\\\-]*[a-zA-Z0-9])\\\\.)*",
                                    "default": "tcp://127.0.0.1:5031"

                                },
                                "l3.2_socket": {
                                    "mutable": true,
                                    "required": false,
                                    "type": "String",
                                    "pattern": "(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\\\\-]*[a-zA-Z0-9])\\\\.)*",
                                    "default": "tcp://127.0.0.1:5032"

                                },
                                "l4_socket": {
                                    "mutable": true,
                                    "required": false,
                                    "type": "String",
                                    "pattern": "(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\\\\-]*[a-zA-Z0-9])\\\\.)*",
                                    "default": "tcp://127.0.0.1:5040"

                                },
                                "neighbors_socket": {
                                    "mutable": true,
                                    "required": false,
                                    "type": "Array",
                                    "pattern": "(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\\\\-]*[a-zA-Z0-9])\\\\.)*",
                                    "default": ""
                                },
                                "topics": {
                                    "mutable": true,
                                    "required": false,
                                    "type": "Array",
                                    "pattern": "(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\\\\-]*[a-zA-Z0-9])\\\\.)*",
                                    "default": ""

                                }
                            }
                        }
                    },
                    "actions": [
                        "http://houssem.org/cmbs/member/action#start_l1",
                        "http://houssem.org/cmbs/member/action#start_l2",
                        "http://houssem.org/cmbs/member/action#start_l3.1",
                        "http://houssem.org/cmbs/member/action#start_l3.2",
                        "http://houssem.org/cmbs/member/action#start_l4",
                        "http://houssem.org/cmbs/member/action#check_neighbors"
                    ],
                    "location": "/cmbs/member/"
                }
            ],
            "mixins": []
     }

Update the provider of the 'member' kind::

    curl -X PUT -d@put_provider_cmbs_member.json -H 'content-type: application/occi+json' -H 'accept: application/occi+json' --user user_1:pass -v http://127.0.0.1:8090/-/

put_provider_cmbs_member.json::

    {
        "providers": [
            {
                "Provider": {
                    "local": [
                        "cmbs_member"
                    ],
                    "remote": [

                    ]
                },
                "OCCI_ID": "http://houssem.org/cmbs#member"
            }
        ]
    }

4.2. Message category
---------------------

Creation of the 'message' kind::

    curl -X POST -d@post_category_cmbs_message.json -H 'content-type: application/occi+json' -H 'accept: application/occi+json' -v http://127.0.0.1:8090/-/

post_category_cmbs_message.json::

  {
      "actions": [
          {
              "term": "execute",
              "scheme": "http://houssem.org/cmbs/message/action#",
              "title": "execute locally the message",
              "attributes": {}
          },
          {
              "term": "send_l1",
              "scheme": "http://houssem.org/cmbs/message/action#",
              "title": "Send a L1 message",
              "attributes": {}
          },
          {
              "term": "send_l2",
              "scheme": "http://houssem.org/cmbs/message/action#",
              "title": "Send a L2 message",
              "attributes": {}
          },
          {
              "term": "send_l31",
              "scheme": "http://houssem.org/cmbs/message/action#",
              "title": "Send a L31 message",
              "attributes": {}
          },
          {
              "term": "send_l32",
              "scheme": "http://houssem.org/cmbs/message/action#",
              "title": "Send a L32 message",
              "attributes": {}
          },
          {
              "term": "send_l4",
              "scheme": "http://houssem.org/cmbs/message/action#",
              "title": "Send a L4 message",
              "attributes": {}
          }
      ],
      "kinds": [
          {
              "term": "message",
              "scheme": "http://houssem.org/cmbs#",
              "title": "CMBS message",
              "attributes": {
                  "cmbs": {
                      "message": {
                          "cmbs_layer": {
                              "mutable": true,
                              "required": false,
                              "type": "String",
                              "pattern": "l1|l2|l31|l32|l4",
                              "default": "true"
                          },
                          "executable": {
                              "mutable": true,
                              "required": false,
                              "type": "String",
                              "pattern": "true|false",
                              "default": "true"
                          },
                          "sendable": {
                              "mutable": true,
                              "required": false,
                              "type": "String",
                              "pattern": "true|false",
                              "default": "true"
                          },
                          "storable": {
                              "mutable": true,
                              "required": false,
                              "type": "String",
                              "pattern": "true|false",
                              "default": "true"
                          },
                          "path_history": {
                              "mutable": true,
                              "required": false,
                              "type": "Array",
                              "pattern": "(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\\\\-]*[a-zA-Z0-9])\\\\.)*",
                              "default": ""
                          },
                          "message_content": {
                              "mutable": true,
                              "required": false,
                              "type": "Object",
                              "pattern": "(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\\\\-]*[a-zA-Z0-9])\\\\.)*",
                              "default": ""
                          },
                          "result": {
                              "mutable": true,
                              "required": false,
                              "type": "Object",
                              "pattern": "(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\\\\-]*[a-zA-Z0-9])\\\\.)*",
                              "default": ""
                          }
                      }
                  }
              },
              "actions": [
                  "http://houssem.org/cmbs/message/action#execute"
              ],
              "location": "/cmbs/message/"
          }
      ],
      "mixins": [
          {
              "term": "l1",
              "scheme": "http://houssem.org/cmbs#",
              "title": "L1 CMBS message",
              "related": [],
              "attributes": {
                  "cmbs": {
                      "message": {
                          "l1_socket_receiver_member": {
                              "mutable": true,
                              "required": false,
                              "type": "String",
                              "pattern": "(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\\\\-]*[a-zA-Z0-9])\\\\.)*",
                              "default": ""
                          }
                      }
                  }
              },
              "actions": [
                  "http://houssem.org/cmbs/message/action#send_l1"
              ],
              "location": "/cmbs/message/l1/"
          },
          {
              "term": "l2",
              "scheme": "http://houssem.org/cmbs#",
              "title": "L2 CMBS message",
              "related": [],
              "attributes": {},
              "actions": [
                  "http://houssem.org/cmbs/message/action#send_l2"
              ],
              "location": "/cmbs/message/l2/"
          },
          {
              "term": "l31",
              "scheme": "http://houssem.org/cmbs#",
              "title": "L31 CMBS message",
              "related": [],
              "attributes": {
                  "cmbs": {
                      "message": {
                          "providers": {
                              "mutable": true,
                              "required": false,
                              "type": "Array",
                              "pattern": "(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\\\\-]*[a-zA-Z0-9])\\\\.)*",
                              "default": ""
                          }
                      }
                  }
              },
              "actions": [
                  "http://houssem.org/cmbs/message/action#send_l31"
              ],
              "location": "/cmbs/message/l31/"
          },
          {
              "term": "l32",
              "scheme": "http://houssem.org/cmbs#",
              "title": "L32 CMBS message",
              "related": [],
              "attributes": {
                  "cmbs": {
                      "message": {
                          "topics": {
                              "mutable": true,
                              "required": false,
                              "type": "Array",
                              "pattern": "(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\\\\-]*[a-zA-Z0-9])\\\\.)*",
                              "default": ""
                          }
                      }
                  }
              },
              "actions": [
                  "http://houssem.org/cmbs/message/action#send_l32"
              ],
              "location": "/cmbs/message/l32/"
          },
          {
              "term": "l4",
              "scheme": "http://houssem.org/cmbs#",
              "title": "L4 CMBS message",
              "related": [],
              "attributes": {
                  "cmbs": {
                      "message": {
                          "providers": {
                              "mutable": true,
                              "required": false,
                              "type": "Array",
                              "pattern": "(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\\\\-]*[a-zA-Z0-9])\\\\.)*",
                              "default": ""
                          },
                          "topics": {
                              "mutable": true,
                              "required": false,
                              "type": "Array",
                              "pattern": "(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\\\\-]*[a-zA-Z0-9])\\\\.)*",
                              "default": ""
                          }
                      }
                  }
              },
              "actions": [
                  "http://houssem.org/cmbs/message/action#send_l4"
              ],
              "location": "/cmbs/message/l4/"
          }
  
      ]
  }
Update the provider of the 'message' kind::
  
    curl -X PUT -d@put_provider_cmbs_message.json -H 'content-type: application/occi+json' -H 'accept: application/occi+json' -v http://127.0.0.1:8090/-/

put_provider_cmbs_message.json::

  {
    "providers": [
        {
            "Provider": {
                "local": [
                    "cmbs_message"
                ],
                "remote": [

                ]
            },
            "OCCI_ID": "http://houssem.org/cmbs#message"
        }
    ]
  }


4.3. Member instance
--------------------

Create a member::

    curl -X POST -d@post_member.json -H 'content-type: application/occi+json' -H 'accept: application/occi+json' --user user_1:pass -v http://127.0.0.1:8090/cmbs/member/

return::

    {"Location": ["http://127.0.0.1:8090/cmbs/member/996ad860-2a9a-504f-8861-aeafd0b2ae29"]}


post_member.json::

    {
           "resources": [
               {
                   "kind": "http://houssem.org/cmbs#member",
                   "mixins": [],
                   "attributes": {
                       "cmbs": {
                           "member": {
                               "state": "active",
                               "l1_socket": "tcp://127.0.0.1:5010",
                               "l2_socket": "tcp://127.0.0.1:5020",
                               "l3.1_socket": "tcp://127.0.0.1:5031",
                               "l3.2_socket": "tcp://127.0.0.1:5032",
                               "l4_socket": "tcp://127.0.0.1:5040",
                               "neighbors_socket": [],
                               "topics": []

                           }
                       }
                   },
                   "actions": [],
                   "id": "996ad860-2a9a-504f-8861-aeafd0b2ae29",
                   "title": "member of CMBS",
                   "summary": "This is a member of CMBS",
                   "links": []
               }
           ]
       }

discovery request::

   curl -X POST -d@action_check_neighbors_member.json -H 'content-type: application/occi+json' -H 'accept: application/occi+json' -v http://127.0.0.1:8090/cmbs/member/016ad860-2a9a-504f-8861-aeafd0b2ae29?action=check_neighbors

starting the l1 receiver::

   curl -X POST -d@action_start_l1_member.json -H 'content-type: application/occi+json' -H 'accept: application/occi+json' -v http://127.0.0.1:8090/cmbs/member/016ad860-2a9a-504f-8861-aeafd0b2ae29?action=start_l1

stopping the l1 receiver::

   curl -X POST -d@action_stop_l1_member.json -H 'content-type: application/occi+json' -H 'accept: application/occi+json' -v http://127.0.0.1:8090/cmbs/member/016ad860-2a9a-504f-8861-aeafd0b2ae29?action=stop_l1

starting the l2 receiver::

   curl -X POST -d@action_start_l2_member.json -H 'content-type: application/occi+json' -H 'accept: application/occi+json' -v http://127.0.0.1:8090/cmbs/member/016ad860-2a9a-504f-8861-aeafd0b2ae29?action=start_l2

stopping the l2 receiver::

   curl -X POST -d@action_stop_l2_member.json -H 'content-type: application/occi+json' -H 'accept: application/occi+json' -v http://127.0.0.1:8090/cmbs/member/016ad860-2a9a-504f-8861-aeafd0b2ae29?action=stop_l2

4.4. Message l1 instance
------------------------

Create a message::

   curl -X POST -d@post_message_l1.json -H 'content-type: application/occi+json' -H 'accept: application/occi+json' -v http://127.0.0.1:8090/cmbs/message/

post_message_l1.json::

   {
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
                           "l1_socket_receiver_member": "tcp://127.0.0.1:5010",
                           "result": ""
                       }
                   }
               },
               "actions": [],
               "id": "0101d860-2a9a-504f-8861-aeafd0b20101",
               "title": "l1 CMBS message",
               "summary": "This is a L1 CMBS message",
               "links": []
           }
       ]
   }


sending the message l1::

   curl -X POST -d@action_send_l1_message.json -H 'content-type: application/occi+json' -H 'accept: application/occi+json' -v http://127.0.0.1:8090/cmbs/message/0101d860-2a9a-504f-8861-aeafd0b20101?action=send_l1


5. For developers
=================



6. Licensing
============

::

  Copyright 2010-2012 Institut Mines-Telecom

  Licensed under the Apache License, Version 2.0 (the "License");
  you may not use this file except in compliance with the License.
  You may obtain a copy of the License at

  http://www.apache.org/licenses/LICENSE-2.0

  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License.


7. Contacts
===========

Houssem Medhioub: houssem.medhioub@it-sudparis.eu

Djamal Zeghlache: djamal.zeghlache@it-sudparis.eu

8. Acknowledgment
=================
This work has been supported by:

* SAIL project (IST 7th Framework Programme Integrated Project) [http://sail-project.eu/]


9. Todo
=======

Some of pyCMBS's needs might be:

*

