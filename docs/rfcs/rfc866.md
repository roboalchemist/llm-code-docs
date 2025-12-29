---
rfc: 866
title: "Active Users"
date: May 1983
---
11.  When a datagram is received, an answering datagram is sent
containing a list of the currently active users (the data in the
received datagram is ignored).

If the list does not fit in one datagram then send a sequence of
datagrams but don't break the information for a user (a line) across
a datagram.  The user side should wait for a timeout for all
datagrams to arrive.  Note that they are not necessarily in order.

User List Syntax

There is no specific syntax for the user list.  It is recommended
that it be limited to the ASCII printing characters, space, carriage
return, and line feed.  Each user should be listed on a separate
line.
