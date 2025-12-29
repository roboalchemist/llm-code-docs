---
title: "Comments on a Proferred Official ICP"
date: October 1969
---

# 1. In RFC 123 (bottom of Page 2) it is suggested that the byte size for the

connection to the server socket L is 32. However, in the modifications
to second level protocol (RDC 107) it is specified that it is up to the
sending process to chose the byte size. According to the Host-Host
protocol, NCPs should be prepared to accept messages in any byte size
(1<= size <=255);  therefore there is no need to impose a size of 32 in
this case.  Furthermore, since it is up to the sender to choose the byte
size, some Hosts may choose a particular byte size (for simplicity and
convenience) and their NCP may not be geared to transmit in an imposed
byte size.

# 2. In RFCs 66 and 80, an ALL is expected on the connection to the server

socket before data can be sent. In RFCs 123 and 127 the ALL requirement
disappeared.  But the ALL is a Host-Host protocol requirement and not
requiring it creates special case. A particular NCP implementation may
cause the ALL to be sent internally when a connection is created,
without the user process having control of it. Relaxing this requirement
will create a special case for the receiving NCP not to send the ALL and
for the sending NCP to send the data = S without first receiving an ALL.

# 3. In RFC 127, I disagree with the comment "send 32 bits of data in one

message" because it is a second level protocol decision that a message
can be sent in any size pieces and the size is to be specified through
the ALL mechanism. In particular, there may be hosts which are not
prepared to accept more than few bytes at a time (TIPs).

In general we should not make second level decisions in a third level
protocol.

[ This RFC was put into machine readable form for entry ]

```
        [ into the online RFC archives by BBN Corp. under the   ]
        [ direction of Alex McKenzie.                   12/96   ]

```