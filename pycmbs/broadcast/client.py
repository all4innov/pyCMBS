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

import couchdb

import zmq

CouchDB_DB_Name = pycmbs_config.CouchDB_DB_Name

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.setsockopt(zmq.LINGER, 0)    # discard unsent messages on close

try:
    server = couchdb.Server('http://' + str(pycmbs_config.CouchDB_IP) + ':' + str(pycmbs_config.CouchDB_PORT))
except Exception:
    logger.error("The CouchDB database is unreachable")

try:
    server[CouchDB_DB_Name]
    db = server[CouchDB_DB_Name]
except couchdb.http.ResourceNotFound:
    logger.debug("The CouchDB database named: '" + CouchDB_DB_Name + "' doesnt exist.")


logger.debug("extracting all know broadcast socket's CP from DB")
s = "ocni.cp.dcp_broadcast_socket"
map_fun = 'function(doc) { emit(doc["attributes"]["' + s + '"], null);  }'
results = db.query(map_fun)
res = set()
print 'the results.total_rows: ' + str(results.total_rows)
if results.total_rows > 0:
    for q in results.rows:
        print q.key
        socket.connect(q.key)

msg = raw_input('> ')
socket.send(msg)
socket.close()
