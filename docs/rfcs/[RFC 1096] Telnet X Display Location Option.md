---
rfc: 1096
title: "Telnet X Display Location Option"
date: March 1989
---

# 1. Command Name and Code

X-DISPLAY-LOCATION (XDISPLOC)

Code = 35

# 2. Command Meanings

IAC WILL X-DISPLAY-LOCATION

Sender is willing to send the X display location in a
subsequent sub-negotiation.

IAC WON'T X-DISPLAY-LOCATION

Sender refuses to send the X display location.

IAC DO X-DISPLAY-LOCATION

Sender is willing to receive the X display location in a
subsequent sub-negotiation.

IAC DON'T X-DISPLAY-LOCATION

Sender refuses to accept the X display location.

IAC SB X-DISPLAY-LOCATION SEND IAC SE

Sender requests receiver to transmit his (the receiver's) X
display location.  The code for SEND is 1.  (See below.)

IAC SB X-DISPLAY-LOCATION IS ... IAC SE

Sender is stating his X display location.  The code for IS is
0.  (See below.)

# 3. Default

WON'T X-DISPLAY-LOCATION

The X display location will not be exchanged.

DON'T X-DISPLAY-LOCATION

The X display location will not be exchanged.

# 4. Description of the Option

WILL and DO are used only to obtain and grant permission for future
discussion.  The actual exchange of status information occurs within
option subcommands (IAC SB X-DISPLAY-LOCATION...).

Once the two hosts have exchanged a WILL and a DO, the sender of the
DO X-DISPLAY-LOCATION is free to request the X display location.
Only the sender of the DO may send requests (IAC SB X-DISPLAY-
LOCATION SEND IAC SE) and only the sender of the WILL may transmit
actual X display location (within an IAC SB X-DISPLAY-LOCATION IS ...
IAC SE command).  The X display location may not be sent
spontaneously, but only in response to a request.

The X display location is an NVT ASCII string.  This string follows
the normal Unix convention used for the DISPLAY environment variable,
e.g.,

```
         <host>:<dispnum>[.<screennum>]

```

No extraneous characters such as spaces may be included.

The following is an example of use of the option:

Host1: IAC DO X-DISPLAY-LOCATION

Host2: IAC WILL X-DISPLAY-LOCATION

(Host1 is now free to request status information at any time.)

Host1: IAC SB X-DISPLAY-LOCATION SEND IAC SE

Host2: IAC SB X-DISPLAY-LOCATION IS "SRI-NIC.ARPA:0.0" IAC SE

(This command is 22 octets.)

# 5. Implementation Suggestions

Since the X display location may not contain a hostname on the client
host, i.e., ":0" or "unix:0.0", the Telnet client will need to modify
the location appropriately before sending it on to the remote Telnet.

Reference

[1]  Hedrick, C., "Telnet Terminal Speed Option", RFC 1079,
Rutgers University, December, 1988.

Author's Address:

Glenn A. Marcy
Carnegie Mellon University
School of Computer Science
Pittsburgh, PA 15213-3890

Phone: (412) 268-7669

Email: Glenn.Marcy@CS.CMU.EDU
