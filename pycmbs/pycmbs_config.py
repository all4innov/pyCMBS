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


import logging.config
from configobj import ConfigObj

import os

def get_absolute_path_from_relative_path(filename):
    return os.path.abspath(os.path.join(os.path.dirname(__file__), filename))

# Loading the logging configuration file
logging.config.fileConfig(get_absolute_path_from_relative_path("../Logging.conf"))
logger = logging.getLogger("Logging")

# Loading the OCCI server configuration file
config = ConfigObj(get_absolute_path_from_relative_path("../pycmbs.conf"))
CouchDB_IP = config['CouchDB_IP']
CouchDB_PORT = config['CouchDB_PORT']
CouchDB_DB_Name = config['CouchDB_DB_Name']
