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

import pycmbs_config as pycmbs_config
# getting the Logger
logger = pycmbs_config.logger

try:
    import simplejson as json
except ImportError:
    import json

import zmq

CouchDB_DB_Name = pycmbs_config.CouchDB_DB_Name

logger.debug("reading the initialisation file")
json_data = open(pycmbs_config.get_absolute_path_from_relative_path('../initialization.json'))
initialisation_data = json.load(json_data)
json_data.close()

def create_broadcast_server(zmq_server='tcp://127.0.0.1:6000'):
    context = zmq.Context()
    socket = context.socket(zmq.SUB)
    socket.bind(zmq_server)
    socket.setsockopt(zmq.SUBSCRIBE, '')
    print zmq_server
    while True:
        data = socket.recv()
        logger.debug(data)

create_broadcast_server(zmq_server=initialisation_data['attributes']["ocni.cp.dcp_broadcast_socket"])