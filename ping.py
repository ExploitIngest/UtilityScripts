#! /usr/bin/python
import os
for ip in range(1,254): 
    os.system('ping 10.11.1.%d -c 1 -w 1' % ip)
