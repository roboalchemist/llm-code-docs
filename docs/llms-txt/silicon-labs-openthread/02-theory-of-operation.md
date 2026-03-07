# Source: https://docs.silabs.com/openthread/3.0.0/using-co-processor-communication-daemon/02-theory-of-operation.md

# Theory of Operation

CPCd uses Unix sockets configured as sequential packets to transfer data with the Linux host applications. Data is then forwarded to the co-processor over a serial link. The Unix sockets, used to transfer data with applications that use the CPC Library (libcpc.so), are instantiated in the /tmp/cpcd folder. A description of the CPC library usage is out of scope for this application note.

![Co-Processor Communication Overview](/using-co-processor-communication-daemon/0.1/images/sld804-image1.png)
