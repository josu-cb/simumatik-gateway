# Simumatik Gateway - Simumatik 3rd party integration tool
# Copyright (C) 2021 Simumatik AB
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import sys
from os import path
import time
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from drivers.fanuc_roboguide.fanuc_roboguide import fanuc_roboguide
from drivers.driver import VariableOperation, VariableDatatype

# Define your I/O variables here
VARIABLES = {
    'DI1':{'datatype': VariableDatatype.BOOL, 'size': 1, 'operation': VariableOperation.WRITE},
    'DO1':{'datatype': VariableDatatype.BOOL, 'size': 1, 'operation': VariableOperation.READ},
    'GI1':{'datatype': VariableDatatype.BYTE, 'size': 1, 'operation': VariableOperation.WRITE},
    'GO1':{'datatype': VariableDatatype.BYTE, 'size': 1, 'operation': VariableOperation.READ},
    'AI1':{'datatype': VariableDatatype.WORD, 'size': 1, 'operation': VariableOperation.WRITE},
    'AO1':{'datatype': VariableDatatype.WORD, 'size': 1, 'operation': VariableOperation.READ},
    'RI1':{'datatype': VariableDatatype.BOOL, 'size': 1, 'operation': VariableOperation.WRITE},
    'RO1':{'datatype': VariableDatatype.BOOL, 'size': 1, 'operation': VariableOperation.READ},
    }

# Add your custom logic in this test.
d = fanuc_roboguide(None, 'test')
if d.connect():
    d.addVariables(VARIABLES)

    counter = 0
    start = time.perf_counter()
    while (time.perf_counter()-start < 5):
        res = d.writeVariables([('DI1', counter%2), ('GI1', counter), ('AI1', counter), ('RI1', counter%2)])
        print(res)
        print(d.readVariables(['DO1','GO1','AO1','RO1']))
        #time.sleep(0.05)
        counter += 1

    d.disconnect()
else:
    print("Connection failed!")