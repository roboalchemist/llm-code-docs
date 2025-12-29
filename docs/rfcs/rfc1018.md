---
rfc: 1018
title: "Some Comments on SQuID"
date: August 1987
---
1. How should a gateway differentiate between Funneling and
mismatch congestion?  Perhaps whenever there are more than q"
items on an output queue to a slower subnet which have been
received from a faster subnet, then look to see if any h" of them
have the same source.  It so assume Mismatch and send an SQ to
that source.  The "q" test might be implemented by a small set of
counters which are incremented when a packet is placed on an
output queue and decremented when a packet is sent.  The search
for a common source might require more cycles but be performed
less often.  The value of "q" would have to be small enough to
give an early warning, but bigger than a small multiple of "h".
The value of "h" would have to be big enough to avoid triggering

on common cases of source datagram fragmentation by an
intermediate gateway.

2. How can a gateway determine which subnets are "slower" and
faster", as well as appropriate inter-arrival times?  There may be
lots of clever ways for a gateway to measure the dynamic bandwidth
of its directly-connected subnets.  However, I'm more in favor of
starting with configuration parameters related to the known (at
installation time) general characteristics of subnet types (e.g.
Ethernet is 10Mbps, ARPANET is 50 Kbps, SATNET is 100 Kbps, etc).
This sort of approximation is quite adequate for determining which
subnet is faster, or what inter-arrival time is appropriate for
packets being routed to a slower subnet.

Summary

Funneling congestion and Mismatch congestion are qualitatively
different, and it would not be surprising if different SQ-sending
strategies were best for dealing with them.  RFC- 1016 suggests a
specific SQ-sending strategy which may be inappropriate for dealing
with Mismatch congestion.  This RFC suggests guidelines for an
additional SQ-sending strategy for dealing with Mismatch.  Hosts
implementing the SQuID algorithm of RFC-1016 should be expected to
achieve better performance if they received SQ's sent according to
either or both of these strategies.  However, all these ideas are
still only in half-baked form; real engineering is clearly needed.
