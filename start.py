# -*- Mode: python; py-indent-offset: 4; indent-tabs-mode: nil; coding: utf-8; -*-

# Copyright (C) 2011 Houssem Medhioub - Institut Telecom
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
Created on Feb 25, 2011

@author: Houssem Medhioub
@contact: houssem.medhioub@it-sudparis.eu
@organization: Institut Telecom - Telecom SudParis
@version: 0.1
@license: LGPL - Lesser General Public License
"""

print '''
    1 - cmbs_discovery server
    2 - cmbs_broadcast server
    3 - cmbs_broadcast client
    4 - cmbs_provider server
    5 - cmbs_provider client
    6 - cmbs_topic server
    7 - cmbs_topic client
    8 - cmbs_provider_topic server
    9 - cmbs_provider_topic client
'''

msg = raw_input('> ')
if msg == '1':
    import pycmbs.discovery as pycmbs_discovery
    pycmbs_discovery.__init__
elif msg == '2':
    import pycmbs.broadcast.server as pycmbs_broadcast_server
    pycmbs_broadcast_server.__init__
elif msg == '3':
    import pycmbs.broadcast.client as pycmbs_broadcast_client
    pycmbs_broadcast_client.__init__
elif msg == '4':
    import pycmbs.for_provider.server as pycmbs_provider_server
    pycmbs_provider_server.__init__
elif msg == '5':
    import pycmbs.for_provider.client as pycmbs_provider_client
    pycmbs_provider_client.__init__
elif msg == '6':
    print 'still under implementation'
elif msg == '7':
    print 'still under implementation'
elif msg == '8':
    print 'still under implementation'
elif msg == '9':
    print 'still under implementation'