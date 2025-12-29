---
rfc: 593
title: "Telnet and FTP Implementation Schedule Change"
---
23.  It will also be useful for the user program to let the user
optionally select the server socket, as many user Telnet programs
currently do.  It will also be useful for implementers to consider a
server Telnet program capable of dealing with both protocols as MIT-
DMCG has done (RFC 559).  This will provide an opportunity for
testing and debugging the new programs in a way that does not
interfere with normal use.

During January we will survey the technical liaisons to determine the
status of the Telnet implementations.  As soon as we determine that
the Telnet implementations have reached a point where the changeover
can be made without disruption of user services the technical
liaisons will be notified.

In light of this change in the Telnet implementation schedule, the
FTP schedule is also modified.  New FTP implementations are to be
ready by 1 Feb 74 (as before), but will continue to use ICP socket 21
(decimal) until we can determine that a changeover is appropriate.

# References

Telnet Protocol NIC 18639

File Transfer Protocol NIC 17759

[This RFC was put into machine readable form for entry ]
[into the online RFC archives by Mirsad Todorovac 5/98 ]
