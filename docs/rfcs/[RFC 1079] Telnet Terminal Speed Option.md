---
rfc: 1079
title: "Telnet Terminal Speed Option"
date: December 1988
---

# 1. Command Name and Code

TERMINAL-SPEED

Code = 32

# 2. Command Meanings

IAC WILL TERMINAL-SPEED

Sender is willing to send terminal speed information in a
subsequent sub-negotiation.

IAC WON'T TERMINAL-SPEED

Sender refuses to send terminal speed information.

IAC DO TERMINAL-SPEED

Sender is willing to receive terminal speed information in a
subsequent sub-negotiation.

IAC DON'T TERMINAL-SPEED

Sender refuses to accept terminal speed information.

IAC SB TERMINAL-SPEED SEND IAC SE

Sender requests receiver to transmit his (the receiver's)
terminal speed. The code for SEND is 1. (See below.)

IAC SB TERMINAL-SPEED IS ... IAC SE

Sender is stating his terminal speed. The code for IS is 0.
(See below.)

# 3. Default

WON'T TERMINAL-SPEED

Terminal speed information will not be exchanged.

DON'T TERMINAL-SPEED

Terminal speed information will not be exchanged.

# 4. Description of the Option

WILL and DO are used only to obtain and grant permission for future
discussion. The actual exchange of status information occurs within
option subcommands (IAC SB TERMINAL-SPEED...).

Once the two hosts have exchanged a WILL and a DO, the sender of the
DO TERMINAL-SPEED is free to request speed information.  Only the
sender of the DO may send requests (IAC SB TERMINAL-SPEED SEND IAC
SE) and only the sender of the WILL may transmit actual speed
information (within an IAC SB TERMINAL-SPEED IS ... IAC SE command).
Terminal speed information may not be sent spontaneously, but only in
response to a request.

The terminal speed information is an NVT ASCII string.  This string
contains the decimal representation of the transmit and receive
speeds of the terminal, separated by a comma, e.g.,

No leading zeros may be included.  No extraneous characters such as
spaces may be included.

The following is an example of use of the option:

Host1: IAC DO TERMINAL-SPEED

Host2: IAC WILL TERMINAL-SPEED

(Host1 is now free to request status information at any time.)

Host1: IAC SB TERMINAL-SPEED SEND IAC SE

Host2: IAC SB TERMINAL-SPEED IS "1200,1200" IAC SE

(This command is 15 octets.)

# 5. Implementation Suggestions

Many systems allow only certain discrete terminal speeds.  In such
cases it is possible that a speed may be received that does not match
one of the allowed values.  We suggest that you pick the nearest
speed that is allowed, rounding in a "safe" direction.  Safety will
depend upon the use of the speed information.  If it is being used
for padding, it is best to round up, since too much padding is better
than too little.

Reference

[1]  Solomon, M., and Wimmers, E., "Telnet Terminal Type Option",
RFC 930, January, 1985

[AAuthor's Address:

Charles Hedrick
Rutgers University
Center for Computer and Information Services
Hill Center, Busch Campus
P.O. Box 879
Piscataway, NJ 08855-0879

Phone: (201) 932-3088

Email: HEDRICK@ARAMIS.RUTGERS.EDU
