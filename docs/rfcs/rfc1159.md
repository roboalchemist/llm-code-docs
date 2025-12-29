---
rfc: 1159
title: "Message Send Protocol"
date: June 1990
---
18.  When a datagram is received by the server, an answering datagram

is sent back to the client containing exactly the same data.

Message Syntax

The message should consist of several parts.  The first part is a
single octet indicating the protocol revision, currently decimal 65,
'A'.  The second part is the name of the user that the message is
directed to.  This and the remaining parts are null-terminated, and
consist of eight-bit characters.  Do not strip the eighth bit of the
characters.  The third part is the name of the terminal.  The fourth
part is the actual message.

The total length of the message shall be less than 512 octets.  This
includes all four parts, and any terminating nulls.

If the terminal part is empty, then "the right" terminal is chosen.
If the user part is empty, then the message is written on the
console.

If this protocol is changed, the revision number will be changed.  In
no case will any of the four parts be removed.

Advisories

It is advisable for servers to strip escape sequences before sending
them to actual terminals.  Some terminals can do nasty things when
you send them certain escape sequence.

In both the TCP and UDP versions of the service, checksums are always
used.

# Security Considerations

Security issues are not addressed in this memo.

# Author's Address

Russell Nelson
Educational Computing System
Clarkson University
Potsdam, NY 13699-5730

Phone:  (315) 268-6455

EMail:  nelson@sun.soe.clarkson.edu
