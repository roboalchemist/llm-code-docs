---
rfc: 867
title: "Daytime Protocol"
date: May 1983
---
13.  When a datagram is received, an answering datagram is sent
containing the current date and time as a ASCII character string (the
data in the received datagram is ignored).

Daytime Syntax

There is no specific syntax for the daytime.  It is recommended that
it be limited to the ASCII printing characters, space, carriage
return, and line feed.  The daytime should be just one line.

One popular syntax is:

Weekday, Month Day, Year Time-Zone

Example:

Tuesday, February 22, 1982 17:37:43-PST

Another popular syntax is that used in SMTP:

dd mmm yy hh:mm:ss zzz

Example:

02 FEB 82 07:59:01 PST

NOTE:  For machine useful time use the Time Protocol (RFC-868).
