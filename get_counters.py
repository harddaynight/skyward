#!/usr/bin/python2.6

from __future__ import print_function, unicode_literals
from __future__ import absolute_import, division

import os, sys

try:
    node = str(sys.argv[1])
    condition = str(sys.argv[2])
    address = '207.188.79.162:9000'
    timeout = '3'

    try:
        divider = str(sys.argv[3])
    except IndexError:
        divider = 1

except IndexError:
    print('Missed parameter(s)!')

#strg = open('system.conf', 'r')
#pd = strg.read()
#strg.close()
#config = {}
#config = dict(item.split("=") for item in pd.split("\n"))
#address = config['primary_address']+':'+config['primary_port']

output = os.popen('echo "select * from \\"'+node+'.*.counters\\" where name = \''+condition+'\'"|/usr/bin/mvts3g-sqlclient -a '+address+' -t '+timeout)
response = output.read()

pd2 = response.split('"')
idx = []
start = 0
total = 0

for i in pd2:
    if i == condition:
        idx.append(pd2.index(i, start))
        #print(pd2.index(i, start))
        start = pd2.index(i, start) + 1

for i in idx:
    total = total + int(pd2[i+2])

print(total//int(divider))
