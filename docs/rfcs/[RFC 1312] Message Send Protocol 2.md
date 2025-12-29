---
rfc: 1312
title: "Message Send Protocol 2"
date: April 1992
---
18.  When a datagram is received by the server, an answering datagram
may be sent back to the client.  If the message was addressed to a
particular user (i.e., the RECIPIENT part was non-empty) and was
successfully delivered to that user, a positive acknowledgement
should be sent (as described above). If the message was directed at
any user (i.e., the RECIPIENT part is empty), or if the message could
not be delivered for some reason, no reply is sent.

The reason for this policy is that the UDP service may be used to
broadcast messages addressed to a particular user on an unknown
system or all users on all systems. In either case, it is
inappropriate for all servers to send replies. An alternative
approach might have been to require that a server only send a reply
if a message was addressed explicitly to that system and was not
broadcast. Unfortunately, the most popular network programming API
does not provide an easy way for an application to determine this;
furthermore such a policy would provide no feedback to the sender of
a broadcast message to a particular recipient. The approach adopted
here provides a reasonable compromise.

Example of Message Encoding

Consider a situation in which the user "sandy" is logged into the
console of system "alpha", and wishes to send a message to the user
"chris". "chris" is known to be logged in on the system "beta" but
the exact terminal is unknown. The message consists of two lines of
text, "Hi" followed by "How about lunch?".

The message would be encoded as follows:

+--------+---------+---------+---------+
0 |    B   |    c    |    h    |    r    |
+--------+---------+---------+---------+
4 |    i   |    s    |  <NULL> |  <NULL> |
+--------+---------+---------+---------+
8 |    H   |    i    |   <CR>  |   <LF>  |
+--------+---------+---------+---------+
12 |    H   |    o    |    w    |         |
+--------+---------+---------+---------+
16 |    a   |    b    |    o    |    u    |
+--------+---------+---------+---------+
20 |    t   |         |    l    |    u    |
+--------+---------+---------+---------+
24 |    n   |    c    |    h    |    ?    |
+--------+---------+---------+---------+
28 |  <NULL>|    s    |    a    |    n    |
+--------+---------+---------+---------+
32 |    d   |    y    |  <NULL> |    c    |
+--------+---------+---------+---------+
36 |    o   |    n    |    s    |    o    |
+--------+---------+---------+---------+
40 |    l   |    e    |  <NULL> |    9    |
+--------+---------+---------+---------+
44 |    1   |    0    |    8    |    0    |
+--------+---------+---------+---------+
48 |    6   |    1    |    2    |    1    |
+--------+---------+---------+---------+
52 |    3   |    2    |    5    |  <NULL> |
+--------+---------+---------+---------+
56 | <NULL> |
+--------+

Note that the RECIP-TERM  and SIGNATURE parts are empty. The COOKIE
is the string "910806121325", which in this implementation indicates
that the message was sent at 12:13:25 on the 6th of August, 1991.
The identity if the sending and receiving systems is not included in
the message; the server must obtain this information from the
transport service.

Advisories

Client and server implementations must follow the character set
restrictions noted in the MESSAGE part description. Failure to do so
may have undesirable effects on the operation of the receiver's
terminal; more seriously, it may open up a significant security

"hole". The checks must be made on any part of the message which may
be displayed, including the sender's name and terminal.  This is one
case where the admonition to "be liberal in what you accept" is not
applicable. A server may chose to apply additional checks to an
incoming message, and to reject any message which may pose a security
risk. For example, a system using a PostScript-based display may
reject a message which might be interpreted as an executable
PostScript program.

The underlying transport, whether TCP or UDP, is expected to provide
checksums for the message and any response.

The semantics of the various RECIPIENT and RECIP-TERM combinations
may be confusing. The introduction of the "*" wildcard designation in
the RECIP-TERM part makes it possible to send a message to all
terminals on the designated system (if RECIPIENT is empty), or to all
terminals at which a particular recipient has logged in.

A positive acknowledgement may indicate only that the Message Send
server was able to successfully invoke a local message delivery
service. It may not be possible for true end-to-end semantics to be
inferred.

For example, a Message Send server may employ a local delivery
mechanism which calls upon the services of a window system to display
the message in a pop-up window. This process may take some
significant time to complete, and it is unclear whether it is useful
for the server to wait for an indeterminate period before returning
an acknowledgement.  Therefore, this specification does not prescribe
whether the acknowledgement is associated with delivery of the
message to the local service, the display of the message, or
confirmation by the user that the message has been read by, e.g.,
dismissing the pop-up window.

# Security Considerations

Those who plan to implement this service must ensure that the
following issues are reflected in the documentation of their
products, and that their implementations include sufficient
configuration controls to allow systems and network administrators to
achieve the appropriate levels of usability and security.

First, this service may allow someone to write on a user's terminal
without the user giving his or her permission.  Where possible, users
should be provided with a mechanism for disabling this.

Second, it is extremely important for implementors to observe the
rules for filtering message text as discussed under Message Syntax

above. Failure to do this may introduce major security holes.

The third issue concerns the verification of the sender's identity.
If the recipient is fooled into believing that a message is from a
particular user, various security issues may arise. For example, the
recipient may send a reply containing confidential material.

This service is primarily intended for "open" environments:
controlled local area networks used by reasonably trusted
participants, in which security considerations may be relaxed in the
interests of ease of use and administration. In such an environment
it is appropriate to trust the user name and source IP address as
identifying the actual sender of the message.

Within more security-conscious environments, this assumption is
probably unacceptable. As has been widely noted, there is no way
within the current Internet architecture to ensure that the source
address of an IP datagram is correct. Hence it is entirely possible
for someone to spoof the IP address.

The obvious, and simplest, answer is to disallow the use of this
protocol in such situations.  However a more constructive approach is
to incorporate within the protocol some mechanism by which a server
can reliably identify the sender.

In this version of the protocol specification, we define a SIGNATURE
part within a message. If this part is empty, the identity of the
sender cannot be verified, and the server implementation may elect to
reject all such requests.  If the part is not empty, it is treated as
a case-insensitive text encoding of some security token. This RFC
does not define the encoding or interpretation of this token. We
expect that such matters will form part of future RFCs on security
and privacy issues; at an appropriate time, this RFC will be re-
issued to include references to these RFCs.

# Acknowledgements

PostScript is a trademark of Adobe Systems, Inc.

# Authors' Addresses

Russell Nelson
Crynwr Software
11 Grant St.
Potsdam, NY 13676

Phone:  (315) 268-1925
EMail:  nelson@crynwr.com

Geoff Arnold
Sun Microsystems, Inc.
2 Federal Street
Billerica, MA 01821

Phone:  (508) 671-0317
EMail:  geoff@east.sun.com
