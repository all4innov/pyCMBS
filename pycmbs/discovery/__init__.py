# Copyright (C) 2012 Houssem Medhioub - Institut Mines-Telecom
#
# This library is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as
# published by the Free Software Foundation, either version 3 of
# the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this library.  If not, see <http://www.gnu.org/licenses/>.

"""
Created on March 13, 2012

@author: Houssem Medhioub
@contact: houssem.medhioub@it-sudparis.eu
@organization: Institut Mines-Telecom - Telecom SudParis
@version: 0.1
@license: LGPL - Lesser General Public License
"""

import pycmbs.pycmbs_config as pycmbs_config
# getting the Logger
logger = pycmbs_config.logger

from pprint import pprint

try:
    import simplejson as json
except ImportError:
    import json

import cStringIO

import jsonpickle

import couchdb

from pyocni.pyocni_tools import ask_user_details as shell_ask

import zmq

from threading import Thread

def discovery_request(zmq_server='tcp://127.0.0.1:5000', message=''):
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect(zmq_server)
    logger.debug("Sending the request to the server: ")
    socket.send_json(message)

    msg_in = socket.recv_json()
    logger.debug('Receiving the replay: ')
    #print 'SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSss'
    print type(msg_in)
    print msg_in
    return msg_in


def create_discovery_server(zmq_server='tcp://127.0.0.1:5000'):
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind(zmq_server)

    while True:
        msg = socket.recv_json()
        print type(msg)
        print "Got", msg
        a = msg['attributes']["ocni.cp.dcp_discovery_socket"]

        s = "ocni.cp.dcp_discovery_socket"
        map_fun = 'function(doc) { emit(doc["attributes"]["' + s + '"], null);  }'
        results = db.query(map_fun, key=a)
        if len(results) > 0:
            logger.debug("The cloud provider with socket: " + a + ' is already know.')
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


def create_broadcast_server(zmq_server='tcp://127.0.0.1:6000'):
    context = zmq.Context()
    socket = context.socket(zmq.SUB)
    socket.bind(zmq_server)

    while True:
        data = socket.recv()
    print data

CouchDB_DB_Name = pycmbs_config.CouchDB_DB_Name

logger.debug("reading the initialisation file")
json_data = open(pycmbs_config.get_absolute_path_from_relative_path('../initialization.json'))
initialisation_data = json.load(json_data)
json_data.close()

try:
    server = couchdb.Server('http://' + str(pycmbs_config.CouchDB_IP) + ':' + str(pycmbs_config.CouchDB_PORT))
except Exception:
    logger.error("The CouchDB database is unreachable")
# ======================================================================================
# Reinialization of the CouchDB PyCMBS database
# ======================================================================================
result = shell_ask.query_yes_no_quit(" \n_______________________________________________________________\n"
                                     "   Do you want to purge the PyCMBS Databases (DB  reinialization)?", "no")
if result == 'yes':
    try:
        del server[CouchDB_DB_Name]
        server.create(CouchDB_DB_Name)
    except Exception:
        logger.debug("No DB names: '" + CouchDB_DB_Name + "' to delete.")
        server.create(CouchDB_DB_Name)
else:
    try:
        server[CouchDB_DB_Name]
    except couchdb.http.ResourceNotFound:
        logger.debug("The CouchDB database named: '" + CouchDB_DB_Name + "' doesnt exist.")
        server.create(CouchDB_DB_Name)

logger.debug("adding the cp description to the DB")
db = server[CouchDB_DB_Name]
try:
    db.save(initialisation_data)
except Exception:
    logger.debug("The Cloud Provider description already exist")

A = initialisation_data['attributes']["ocni.cp.dcp_discovery_neighbors_socket"]

print type(A)

while len(A) > 0:
    a = A[0]
    s = "ocni.cp.dcp_discovery_socket"
    map_fun = 'function(doc) { emit(doc["attributes"]["' + s + '"], null);  }'
    results = db.query(map_fun, key=a)
    if len(results) > 0:
        logger.debug("The cloud provider with socket: " + a + ' is already know.')
    else:
        logger.debug("The cloud provider with socket: " + a + ' is unknown -> A discovery request will be sent.')
        # the discovery requests can be sent in // via thread (just check that no more thread running when doing the while len(A) > 0
        result = discovery_request(zmq_server=a, message=initialisation_data)
        db.save(result['description_provider'])
        for u in result['values']:
            print type(u)
            print u
            k = "ocni.cp.dcp_discovery_socket"
            map_fun2 = 'function(doc) { emit(doc["attributes"]["' + k + '"], null);  }'
            results2 = db.query(map_fun2, key=k)
            if len(results2) > 0:
                logger.debug("The cloud provider with socket: " + u + ' is already know.')
            elif u in A:
                logger.debug(
                    "The cloud provider with socket: " + u + ' is unknown but in the list of servers to discover.')
            else:
                logger.debug(
                    "Add the cloud provider with this socket: " + u + ' to the list of CP that will be discovered')
                A.append(u)

    del A[0]


create_discovery_server(zmq_server=initialisation_data['attributes']["ocni.cp.dcp_discovery_socket"])
