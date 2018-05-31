#!/bin/python
# This script build and execute this : 
#-------------------->YOUR_BOOM_MAC     -----------------------------> YOUR_BTMAC(no ":")+01 
# gatttool -i hci0 -b XX:XX:XX:XX:XX:XX --char-write-req -a 0x0003 -n XXXXXXXXXXXX01
# This command was found by Mathieu Tournier by reverse engineering BOOM2 bluetooth ATT traffic

import subprocess
import re

print("Please Write BOOM MAC Adress :")
commandRet = subprocess.check_output(['hciconfig'])

print(commandRet)

matches = re.findall("([0-9A-F]{2}:[0-9A-F]{2}:[0-9a-fA-F]{2}:[0-9A-F]{2}:[0-9A-F]{2}:[0-9A-F]{2})", commandRet)
btAdress = matches[0].translate(None,':')

if (matches) : 
    print ('using ' + matches[0] + ' as BT Adress adaptor')
    boomAddr = raw_input("BOOM Mac Adress ?")
    boomAddr = re.findall("([0-9A-F]{2}:[0-9A-F]{2}:[0-9a-fA-F]{2}:[0-9A-F]{2}:[0-9A-F]{2}:[0-9A-F]{2})", boomAddr)
    if (boomAddr) :
        commandRet = subprocess.check_output(['gatttool', '-i', 'hci0', '-b', str(boomAddr[0]), '--char-write-req', '-a', '0x0003', '-n', btAdress + '01'])
    else :
        print("Invalid Bt Adress")
    
else :
    print("No Adaptator Found")

