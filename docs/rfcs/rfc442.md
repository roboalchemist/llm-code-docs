---
rfc: 442
title: "The Current Flow-Control Scheme for IMPSYS"
date: January 1973
---
1. Priority Packets (as marked by HOST)

2. Non-Priority Packet

3. Unacknowledged packets (on I,O state channels)

4. Others

It was pointed out that a heavy load of type (1) and (2) traffic
might prevent retransmissions from occurring at all, and W. Crowther
responded that the bug would be fixed by a 125 ms time-out which
forces retransmission of old packets in class (3).

Note that each packet must carry a "pseudo-channel" number to
identify the POE-to-channel association, and 8 ACK bits (which are
positionally associated with the pseudo-channels).  Thus a single
packet can ACK up to 8 packets at once.

[This RFC was put into machine readable form for entry]

```
     [into the online RFC archives by Helene Morin, Via Genie, 12/99]

```