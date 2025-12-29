---
title: "Basically, the proposed set of changes in RFC 687 seems reasonable, as"
date: June 1975
---
1.  The last 8 bits are never used to convey information.

2.  The network is not required to pass them from source to
destination, or to return them to the source.

3.  When sending messages of types other than zero, (irregular
messages), the IMP is allowed to send either 96, 104 or 112 bits
of data, the choice being at the IMP's convenience.

4.  Also, if desired, either 96 or 112 could be used as the new
leader length for irregular messages.

It must be faster (and cheaper) to just change the IMP program to handle
a 104 bit leader, than to force additional changes in all hosts using
the standard protocol.

Another suggested extension to the protocol would add a new type of IMP
to Host message.  This message has a table of Host names (people type
character strings) and Host network addresses.  Send this message(s) to
the Host after each interface reset, or alternatively, it could be a
response to a new Host to IMP request for this information.

[ This RFC was put into machine readable form for entry ]
[ into the online RFC archives by Alex McKenzie with    ]

```
       [ support from GTE, formerly BBN Corp.            10/99 ]

```