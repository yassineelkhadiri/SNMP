from pysnmp.hlapi import *
import time

data = (
    ObjectType(ObjectIdentity('.1.3.6.1.2.1.2.2.1.10.3'))
)

while True :
    g = getCmd(SnmpEngine() ,
            CommunityData('ciscolab', mpModel=1) ,
            UdpTransportTarget(('192.168.1.1', 161)) ,
            ContextData() ,
            data
        )
    errorIndication, errorStatus, errorIndex, varBinds = next(g)
    if errorIndication:
        print(errorIndication)
    elif errorStatus:
        print('%s at %s' % (errorStatus.prettyPrint() ,
            errorIndex and varBinds[int(errorIndex) - 1][0] or '?' ) )
    else :
        print(varBinds[0][1])
        with open("debit.txt", "a+") as f : 
            f.write(str(varBinds[0][1]))
            f.write("\n")
    
    time.sleep(5)