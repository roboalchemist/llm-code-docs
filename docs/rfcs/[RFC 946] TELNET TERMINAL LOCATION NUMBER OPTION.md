---
rfc: 946
title: "TELNET TERMINAL LOCATION NUMBER OPTION"
date: May 1985
---

# 1. Command Name and Option Code

TTYLOC  28

# 2. Command Meanings

IAC WILL TTYLOC

The sender offers to send the TTYLOC information or confirms that
it can send the TTYLOC information.

IAC WON'T TTYLOC

The sender refuses to send the TTYLOC information.

IAC DO TTYLOC

The sender requests to receive the TTYLOC information or confirms
that it will receive the TTYLOC information.

IAC DON'T TTYLOC

The sender refuses to receive the TTYLOC information.

IAC SB TTYLOC <format> <TTYLOC number with IAC doubling> IAC SE

The sender is transmitting the TTYLOC information. The 64-bit
TTYLOC number has format 0. The first 32-bits is the Internet host
number and the second 32-bits is the line on the specified
Internet host. The bytes are in most significant 8-bit byte to
least significant byte order.

# 3. Default Specification

WON'T TTYLOC

TTYLOC information will not be sent.

DON'T TTYLOC

TTYLOC information will not be received.

# 4. Motivation

Many systems provide a mechanism for finding out where a user is
logged in from usually including information about telephone
extension and office occupants names. The information is useful for
physically locating people and/or calling them on the phone.

For incoming network connections to a host, only the remote host's
name is available. This option and the Telnet Terminal Location
option (RFC-779) provide the information to the system so it in turn
can provide the information to the various mechanisms (FINGER, WHOIS,
etc.).

# 5. Description of the Option

When the user Telnet connects to a remote host, it can attempt to
send the terminal location number information by doing a
IAC WILL TTYLOC command. If the Telnet server can use the
information, it replies with a IAC DO TTYLOC command. The user Telnet
then sends the TTYLOC number in the subnegotiation.

It is recommended that if sending the TTYLOC number is refused then
the Telnet Terminal Location (SEND-LOCATION in RFC-779) should be
attempted.

The following are two example usage scenarios:

User Side First:

(User) Host1: IAC WILL TTYLOC

Host1 is asking if it can send the 64-bit terminal location
number (I will send...).

(Server) Host2: IAC DO TTYLOC

Host2 indicates to Host1 that it will accept the 64-bit
terminal location number in a subnegotiation (You please do
...).

(User) Host1: IAC SB TTYLOC 0 <64-bit number> IAC SE

Host1 is sending the location number to Host2 which can
communicate the number to the operating system or other
system components.

Server Side First:

(Server) HostA: IAC DO TTYLOC

HostA indicates to HostB that it would like to know the
64-bit terminal location number (You please do ...).

(User) HostB: IAC WILL TTYLOC

HostB agrees to send the 64-bit terminal location number to
HostA in a subnegotiation (I will send...).

(User) HostB: IAC SB TTYLOC 0 <64-bit number> IAC SE

HostB is sending the location number to HostA which can
communicate the number to the operating system or other
system components.
