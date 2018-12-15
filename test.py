
from __future__ import print_function
from time import sleep

import os,sys
import sys
text = "WELCOME TO DEPATRMENT OF CYBER CRIME"
beep = "..."
sepr="|"
def typewr(s,t,sep):
    for x in t:
        print(x,end=sep)
        sys.stdout.flush()
        sleep(s)

typewr(0.1,text,sepr)
ssid = input("\nSSID : ")
print("[SSID CREATED : ",ssid)
password = input("PASSWORD ")
os.system("cd C:\Windows\System32")
command = "netsh wlan set hostednetwork mode=allow ssid="+ssid+" key="+password
os.system(command)



