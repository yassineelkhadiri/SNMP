from pysnmp.hlapi import *
def show_item() :
    g=getCmd(SnmpEngine()
            ,CommunityData('ciscolab',mpModel=1)
            ,UdpTransportTarget(('192.168.1.1',161))
            ,ContextData()
            ,ObjectType(ObjectIdentity('SNMPv2-MIB','sysORDescr',1)))
    errorIndication,errorStatus,errorIndex,varBinds=next(g)
    for varBind in varBinds:
        print(' = '.join([x.prettyPrint()for x in varBind]))
# Show initial value
show_item()
# Setting new value
g=setCmd(SnmpEngine()
         ,UsmUserData("USER1"
                      ,authProtocol=usmHMACSHAAuthProtocol
                      ,authKey="cisco12345"
                      ,privProtocol=usmDESPrivProtocol
                      ,privKey="cisco54321")
         ,UdpTransportTarget(('192.168.1.1',161))
         ,ContextData()
         ,ObjectType(ObjectIdentity('SNMPv2-MIB','sysORDescr',1),'Hello from Lannion using Kalray processor on Linux'))

errorIndication,errorStatus,errorIndex,varBinds=next(g)
print(errorIndication,varBinds)
show_item()