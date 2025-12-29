---
rfc: 478
title: "FTP Server-Server Interaction-II"
date: March 1973
---
1. After the PASV command has been acknowledged, the two data
transfer commands can be sent in either order, since the
LISTENING action takes place with the PASV command

2. The user knows the socket numbers Sc and Sb to be the data
sockets as specified by the protocol.

3. Note that it is not essential for a SOCK command to be sent to
the same Host to whom a PASV will be sent.  Sending one to him
provides security in that the incoming RFC can be checked.

RB/nlg

[This RFC was put into machine readable form for entry]

```
     [into the online RFC archives by Helene Morin, Via Genie 12/1999]

```