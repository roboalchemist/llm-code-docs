---
rfc: 492
title: "Jerry Burchfiel and Ray Tomlinson of Bolt, Beranek, and Newman, Inc,"
date: April 1973
---
1. A NCP which receives an Imp-to-Host message type 7 (Host Dead)
concerning a host should consider all connections or connection
attempts with that host as dead and should purge them from its
tables.

2. When after noting a foreign host as dead (by receiving a "Host
Dead" Imp-to-Host message), an NCP receives any message from
that host other than a Reset Host (RST) control message, it
should delete the message and respond with an RST.  It should
respond normally to a received RST.

3. Two hosts must exchange the RST - RRP reset control message
pair prior to any other form of communications.  An RST must
first be sent by an NCP wishing to start communications with a
foreign host if that host pair has not been previously reset
since the local NCP came up or it noted the foreign NCP as
down.  Note that this does not require an NCP to send resets to
all other hosts each time it comes up.

4. An NCP which receives an Imp-to-Host message type 9 (Incomplete
Transmission) concerning a write link implementing an open
connection, may at its option make several tries to retransmit
the last message until a RFNM is received or the NCP gives up.
However, unless the message is eventually successfully
transmitted to the foreign host the NCP must abort the
connection, sending out a CLS control message.  The successful
implementation of retransmission depends on the retransmitting
host to wait for a RFNM on a data link before sending a
subsequent message and on all hosts to be able to discard
messages which are not completely received.

5. An NCP which receives a message from a foreign host that seems
inconsistent with its current state should take no action to
modify that state.  Rather it should send an ERR error control
message specifying the type of inconsistency and discard the
inconsistent message.  An NCP receiving an ERR message should
log it for human inspection and is then allowed to silently
modify its internal state or send out control messages in order
to remove the inconsistency. (This is an extension of the
proposal in RFC 467 that an NCP should delete a connection when
it receives an ERR message specifying that the link involved is
unknown.)

[This RFC was put into machine readable form for entry]

```
   [into the online RFC archives by Helene Morin, Via Genie,12/1999]

```