
from __future__ import print_function
import sys,os
from time import sleep
def typewr(s,t,sep):
    for x in t:
        print(x,end=sep)
        sys.stdout.flush()
        sleep(s)
os.system("title LOGIN")
os.system("cls")
os.system("COLOR A")
print("\n\n\t\t----WELCOME SUMAN MANNA----")
p = int(input("\n\t\tENTER YOUR PASSWORD PLEASE -- "))
os.system("cls")
if(p==1024):
    os.system("title LAUNCHPAD")
    print("\n")
    message_1 = "[ WECOME TO DARK CYBER ]"
    des = ""
    typewr(0.1,message_1,des)
    print("\n")
    message_2 = "[ LAUNCH PAD CREATING "
    des = "_"
    typewr(0.1,message_2,des)
    beep = "..."
    des=''
    for i in range(0,10):
        typewr(0.5,beep,des)
    print("\n")
    message_3="[ CREATING HOSTED PLATFORM "
    des=""
    typewr(0.1,message_3,des)
    des=''
    for i in range(0,10):
        typewr(0.5,beep,des)
    print("\n\n\n")
    ssid = str(input("\n\nSSID : "))
    print("\n[SSID CREATED : ",ssid)
    password = str(input("\nPASSWORD : "))
    command = "netsh wlan set hostednetwork mode=allow ssid="+ssid+" key="+password
    os.system("cd C:\Windows\System32")
    os.system(command)
    os.system("netsh wlan start hostednetwork")
else:
    os.system("COLOR C")
    os.system("cls")
    os.system("title ACCESS DENIED")
    typewr(0.1,"\nALERT! WRONG ATTEMPT MUST BE COUNTED!")
    typewr(0.1, "\nYOU ARE SURVILENCE BY MICRO CAMERA!")





