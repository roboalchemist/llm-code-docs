---
rfc: 438
title: "FTP Server-Server Interaction"
date: January 1973
---
1. making the establishment of data connections symmetric, or;

2. providing a mechanism for instructing a server to establish its
end of a data connection as if it were a user.

The second alternative probably requires fewer changes to the
existing protocol.

The following proposed extension to FTP uses the second method.   It
involves the addition of a single new command (LSTN) and minor
modifications to several existing commands (SOCK, APPE, RETR, STOR):

a. The LSTN (Listen) command requests the FTP server to allocate a
socket for use as a data connection.  To establish the
corresponding data connection the server is to "listen" on the
socket allocated when an appropriate transfer command is given.

syntax: LSTN <direction> CRLF

where <direction> is either "S" for send or "R" for receive.

The server responds to LSTN by:

1. refusing to allocate such a socket, or:

2. sending the user the number of the socket allocated (the 255
FTP server data socket reply could be used for this
purpose).

b. Receipt of an appropriate STOR, RETR or APPE command following a
successful LSTN command causes the server to "listen" for an RFC
for the socket allocated.   Data transfer may proceed after the
server receives an RFC for the socket and responds with a matching
RFC.   Once established, a data connection corresponding to a
successful LSTN command has the same duration as one established
in the usual way.

c. The user may insure the security of his data transfer by using the
SOCK command to instruct the server to accept an RFC for the
listening socket only if it is from a specified host and socket.

d. The SOCK command is modified in two ways:

1. On success the reply must be the 255 FTP server data socket
reply; that is, the 255 reply can not be deferred until receipt
of a data transfer command.  (This is to allow the user to
transmit the server's response to the program at the third
site; see the example below.)

2. After a LSTN command the SOCK command is to be interpreted by
the server as specification of the acceptable RFC for
subsequent data transfer command that use the allocated socket.

With this extension to FTP, the RSEXEC program could accomplish the
APPEND in the example above as follows:

to SITE1:                       to SITE2:

.                                .
.                                .
.                                .

1.                                   LSTN R CRLF
(let X = socket
allocated)

2.   SOCK SITE2,X CRLF
(let Y = socket in 255
reply from SITE1)

3.                                   SOCK SITE1,Y CRLF

4.  RETR PROG1.PL1                   APPE PROG2.Pl1 CRLF

.                                 .
.                                 .
.                                 .

In closing it is appropriate to note that an experimental RSEXEC
program of the sort suggested above has been operational on TENEXs
for about 8 months.  It currently uses a private, resource sharing
protocol (RSP) that includes file transfer operations.  RSP supports
server-server cooperation; in RSP data connections are established in
a symmetric way (alternative 1 above).

[ This RFC was put into machine readable form for entry ]
[ into the online RFC archives by Mirsad Todorovac 5/98 ]
