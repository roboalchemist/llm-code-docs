---
title: "A FIRST CUT AT A PROPOSED TELNET PROTOCOL"
date: February 1971
---
.
.
.

user site <- NIC

ALL <q> <space>

.
.
.

NIC <- user site

ALL <r> <space>

2    Connection Breaking Protocol

A CLS trade is made between the NCPs for each of the two
connections as per Document #1 NIC (5143,).

We may decide to put a time-out into the NIC connections such
that no interaction for some (as yet unspecified) "reasonable"
length of time will result in a CLS-out of the connections being
initiated by NIC.

3    Third Level Protocol

The first 8 bits received by NIC thru socket ss should be the
message data type designating that an 8-bit ASCII stream follows, as
per NWG/RFC #63, NIC (4963,).

I.e., the first 8 bits are 00000001

The first 8 bits received by Telnet thru socket us will also
indicate a message data type of l.  Each network message should have
an integral multiple of 8 bits.  If a network standard is established
different from the suggestion of NWG/RFC #63, NIC (4963,), then we
would change this protocol to conform.

NIC will have NCP-generated interrupts disabled, i.e.,

INR will be ignored

INS will not be sent to the remote host

4    NLS(NIC) Character Conventions of Interest to Telnet

Echoing can either be under control of NIS(NIC) or under control
of the user site.  When we refer to echoing below, we mean under
control of NLS(NIC).  When echoing is handled by the user site we
would expect the user to set the NLS(NIC) output conventions to
conform to the echoing conventions at his site.  NLS(NIC) assumes
echoing is handled by the user site unless explicitly commanded
otherwise.

Format affecting control characters

horizontal tab

spaces to next (user definable) stop on both echoing
and output.

if during literal input, enters file as ASCII '11.

form feed

carriage return and (user definable) appropriate number
of line feeds on echo and output.

If during literal input, enters file as ASCII '14

vertical tab

carriage return and (user definable) appropriate number
of line feeds on echo and output

if during literal input, enters file as ASCII '13

carriage return

carriage return followed by line feed on echo and
output

if during literal input, enters file as EOL (see below)

line feed

line feed on echo and output

enters file as ASCII '12 on literal input

EOL (end of line)

presently ASCII code '37

carriage return followed by line feed on echo and
output

if during literal input, enters file as ASCII '37

If the user's system automatically appends a LF to a CR
before sending it to Telnet or converts CR to some EOL code
not ASCII '37, we would expect Telnet to send NLS(NIC) just
a CR or ASCII '37.  If we receive CRLF, then on output we
will send CRLFLF.

5 NLS(NIC) Interrupt Attention Convention

A (user definable) ASCII code in the text input stream is used to
abort the executing process and return control to the main NLS(NIC)
command processor.

This code is presently DEL (ASCII '177).

Escape to the NIC monitor:  No escape is required as all
operations needed for use of the NIC can be performed within
NLS(NIC).

Character Set:  We strongly recommend that the Telnet process
be able to generate by some set of keying conventions all 128
ASCII codes.  Use of NLS(NIC) will probably feel most comfortable
from a device with upper and lower case graphics, although we can
provide service to single case devices.  We can provide a useful
service if the full ASCII set cannot be sent, but would like to
minimize the special cases we have to handle.  Sites which cannot
provide the full ASCII set should contact us.

+----+                      |
|    |        Server        |
|    |        Program       |
|    |                      |
+----+                      |
^ |                        |
| v                        |
+----+        Terminal      |
|    |        control       |
|    |        software      |    SERVER
|    |        and           |     SITE
+----+        possibly      |
^ |          hardware      |
| v                        |

+----+                      |
|    |                      |
|    |        NCP           |
|    |                      |
+----+                      |
^ |                        |
| v                        |

. .
. .                                            Figure 1 -
. .
. .                                        Telnet Connection

^ |
| v
+----+                      |
|    |                      |
|    |        NCP           |
|    |                      |
+----+                      |
^ |                        |
| v                        |
+----+                      |
|    |                      |
|    |        Telnet        |
|    |                      |
+----+                      |
^ |                        |    USER
| v                        |    SITE
+----+        Terminal      |
|    |        control       |
|    |        hardware-     |
|    |        software      |
+----+                      |
^ |                        |
| v                        |
+----+                      |
|    |        User          |
\   |        terminal      |
\--+                      |

[ This RFC was put into machine readable form for entry ]
[   into the online RFC archives by Tony Hansen 08/08   ]
