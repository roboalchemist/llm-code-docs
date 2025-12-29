---
rfc: 133
title: "FILE TRANSFER AND ERROR RECOVERY"
date: April 1971
---
...                     (waiting)
<-><0>      ==>                     Error, timeout
<==     <-><0>          Sorry, forget it
<R><...>    ==>                     Send the file (third time)
<==     <rs>            Got it
<rr>        ==>                     Ready
<==     <*><...>        There it is
<rr>        ==>                     Got it
<==     <+>             Done (finally>

Note that the server always gets the last word in error situations
as well as normal transmission.

2C   Although the above examples are given in terms of Bhushan's
transaction codes, this form of error recovery is implementable in
any protocol which uses flagged blocking and duplex connections.

2D   If errors cannot be recovered as above, then some means must be
available to clear the link completely and resynchronize.  I
suggest that an 8-bit argument be appended to the interrupt-on-link
NCP message (INR, INS).  The receiver would send <INR><error> to
indicate that the block boundaries were lost and all incoming data
is being discarded.  The sender, upon receiving the INR, would
flush all queued output and wait for the link to clear.  The NCP
would then send a <INS><newsync> message and, when it was received
(RFNM returned), a negative termination would be sent on the link.
The receiver begins accepting data again when the INS is received.
This assumes that any process can flush untransmitted data and
detect a clear link.  Note that this method is useable on any
simplex connection.

2E  If all else fails, one can resort to closing the faulty socket.

# 3. NCP VERSION NUMBERS

3A  I suggest that the NCP be given a version number and the next
version include two new message types: <WRU> ('Who aRe yoU?')
requests a version number from the receiving host and <IAM><version>
('I AM') supplies that number.

3B  The messages would probably be initially used in a 'can I talk to
you?' sense or not at all.  Eventually, it would take on a 'what
can you do?' meaning.  Accordingly, the <version> field should be
large (32 bits?) for expansion.

[ This RFC was put into machine readable form for entry ]
[ into the online RFC archives by Jose Tamayo 4/97 ]
