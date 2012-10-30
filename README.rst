==========================================================
 pyCMBS - Python Cloud Message Brokering Service
==========================================================

:Version: 0.1
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
  10. json files to execute the HowTo use examples


0. What is it?
==============

pyCMBS (Python Cloud Message Brokering Service): A Python implementation of CMBS.


1. The Latest Version
=====================

version 0.1


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

10. json files to execute the HowTo use examples (available under client/request_examples folder)
=======================================================================
