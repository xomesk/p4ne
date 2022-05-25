from pysnmp.hlapi import *


snmp_engene = SnmpEngine()
community_data = CommunityData("public", mpModel=0)
transport = UdpTransportTarget(("10.31.70.107",161))
snmp_object_version = ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0)
snmp_objetc_interface = ObjectIdentity('1.3.6.1.2.1.2.2.1.2')


resultGet = getCmd(SnmpEngine(),
           community_data,
           transport,
           ContextData(),
           ObjectType(snmp_object_version))

resultNext  = nextCmd(snmp_engene,
            community_data,
            transport,
            ContextData(),
            ObjectType(snmp_objetc_interface),
            lexicographicMode=False)


for x in resultGet:
    for j in x[3]:
     print(j)

for x in resultNext:
    for j in x[3]:
        print(j)





