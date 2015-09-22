#!/usr/bin/python2.6

from __future__ import print_function, unicode_literals
from __future__ import absolute_import, division

import os, sys

try:
    node = str(sys.argv[1])
    condition = str(sys.argv[2])
    address = '192.168.222.35:9000'
    timeout = '3'

    try:
        divider = str(sys.argv[3])
    except IndexError:
        divider = 1

except IndexError:
    print('Missed parameter(s)!')

strg = open('/home/test/gc_storage', 'r')
lastVal = strg.read()
#print('data from storage ', lastVal)
strg.close()

output = os.popen('echo "select * from \\"'+node+'.*.counters\\" where name = \''+condition+'\'"|/usr/bin/mvts3g-sqlclient -a '+address+' -t '+timeout)
response = output.read()

pd2 = response.split('"')
#print(pd2)
idx = []
start = 0
total = 0

for i in pd2:
    if i == condition:
        idx.append(pd2.index(i, start))
        #print(idx)
	#print(pd2.index(i, start))
        start = pd2.index(i, start) + 1
	#print(start)
for i in idx:
    total = total + int(pd2[i+2])

strg = open('gc_storage', 'w')
strg.write(str(total))
strg.close()

print(abs(total//int(divider)-int(lastVal)))
