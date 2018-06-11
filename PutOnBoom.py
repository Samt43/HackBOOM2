#!/bin/python
# This script build and execute this : 
#-------------------->YOUR_BOOM_MAC     -----------------------------> YOUR_BTMAC(no ":")+01 
# gatttool -i hci0 -b XX:XX:XX:XX:XX:XX --char-write-req -a 0x0003 -n XXXXXXXXXXXX01
# This command was found by Mathieu Tournier by reverse engineering BOOM2 bluetooth ATT traffic
from __future__ import print_function
from builtins import input
import subprocess
import re

print("Bluetooth devices : \n")
commandRet = subprocess.check_output(['hciconfig'])

print(commandRet)

## Get bluetooth adapter address (BD Adress).
matches = re.findall("([0-9A-F]{2}:[0-9A-F]{2}:[0-9a-fA-F]{2}:[0-9A-F]{2}:[0-9A-F]{2}:[0-9A-F]{2})", commandRet)

if (matches) : 
    btAdress = matches[0].translate(None,':')
    print ('using ' + matches[0] + ' as BT Adress adaptor')
    boomAddr = input("Please Write BOOM MAC Adress :\n")
    boomAddr = re.findall("([0-9A-F]{2}:[0-9A-F]{2}:[0-9a-fA-F]{2}:[0-9A-F]{2}:[0-9A-F]{2}:[0-9A-F]{2})", boomAddr)
    if (boomAddr) :
        commandRet = subprocess.check_output(['gatttool', '-i', 'hci0', '-b', str(boomAddr[0]), '--char-write-req', '-a', '0x0003', '-n', btAdress + '01'])
    else :
        print("Invalid Bt Adress")
else :
    print("No BT Adaptator Found")

