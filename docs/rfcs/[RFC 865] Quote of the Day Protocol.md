---
rfc: 865
title: "Quote of the Day Protocol"
date: May 1983
---
17.  Once a connection is established a short message is sent out the
connection (and any data received is thrown away).  The service
closes the connection after sending the quote.

UDP Based Character Generator Service

Another quote of the day service is defined as a datagram based
application on UDP.  A server listens for UDP datagrams on UDP port
17.  When a datagram is received, an answering datagram is sent
containing a quote (the data in the received datagram is ignored).

Quote Syntax

There is no specific syntax for the quote.  It is recommended that it
be limited to the ASCII printing characters, space, carriage return,
and line feed.  The quote may be just one or up to several lines, but
it should be less than 512 characters.
