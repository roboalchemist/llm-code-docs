---
rfc: 128
title: "It is somewhat unclear what to do with the Byte size parameter now"
date: April 1971
category: C.2,
---
I.  The first is that the connection is illegal.

II.  The second is that the NCP must parse the data stream on receipt
from the network and into a buffer according to be byte size of
the sender, and subsequently parse the data stream on transfer
from the buffer to the receiver.  In this second case there are
two sub cases.

A. One is to consider bits as the basic unit.

For example, if the sender specified byte size = 5 and the
receiver specified byte size = 3 then

Receiver                   NCP                    Sender
-+---+---+---+---+      +--------+      +-----+-----+---
|000|001|010|011| <--- | Buffer | <--- |00000|10100|11
-+---+---+---+---+      +--------+      +-----+-----+---

B. The other is to consider bytes as the significant unit and pad
(on the right or left?) or truncate to make things fit, or
other transformation.

At UCLA-Computer Science we are contemplating allowing sender and
receiver to specify different byte sizes and consider bits as the
basic unit (Case II.A.).  This does not rule out our considering the
second subcase (Case II.B.).  We may allow 3rd level programs to
specify a library or user supplied routine to perform the

transformation between sender and receiver bytes.  Perhaps these
transformation routines would be written in the Data Reconfiguration
Language.

[ This RFC was put into machine readable form for entry ]
[ into the online RFC archives by Duncan de Waal 03/98 ]
