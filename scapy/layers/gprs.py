
from scapy.fields import *
from scapy.packet import *
from scapy.layers.inet import IP

class GPRS(Packet):
    name = "GPRSdummy"
    fields_desc = [
        StrStopField("dummy","","\x65\x00\x00",1)
        ]


bind_layers( GPRS,          IP,            )