---
rfc: 1397
title: "Default Route Advertisement In"
date: January 1993
---

# Abstract

This document specifies the recommendation of the BGP Working Group
on default route advertisement support in BGP2 [1] and BGP3 [2]
versions of the Border Gateway Protocol.

This recommendation only applies to BGP2 and BGP3 versions of the
Border Gateway Protocol since starting with the BGP4 [3] version a
default route advertisement capability is built in the protocol.

# 1. Overview

The purpose of the default route advertisement capability is to
advertise the IP address of a border gateway which can be used as the
default next hop to destinations that are not listed explicitly in
the BGP peer's routing table.

This capability will allow routers, that are unable to maintain a
complete routing table (e.g., due to its size) to learn a border
gateway that is ready to handle the default traffic.  Also, in
contrast to static defaults, if there is more than one default
gateway, this would make it possible for a BGP speaker to express a
preference for one over the other.  It also reduces the need to
configure default routes in routers.

# 2. Default Route Advertisement

A default route is advertised in an UPDATE message that carries
reachability information for network 0.0.0.0.  A Network field of
such an UPDATE message must contain the IP address 0.0.0.0 as the
indication that it carries a default route.  The NEXT_HOP path
attribute of such a message provides the IP address of a border

gateway that can be used as a default next hop to destinations that
are not listed in the BGP peer's routing table.  The value of the
ORIGIN attribute should be 2 (INCOMPLETE).  The AS_PATH attribute
should be constructed according to the same rules that apply to a
conventional network advertisement.

If multiple default routes are advertised by a BGP speaker,  the
INTER-AS-METRIC path attribute can be included in the corresponding
UPDATE messages to express  preference levels for entry points to the
same AS.

The UNREACHABLE path attribute is used to indicate that a previously
advertised default route has become unreachable.

UPDATE messages containing the default route advertisements should be
handled according to the rules that apply to all other UPDATE
messages.  If multiple default route are acquired by a BGP speaker, a
route is selected according to the local policies adopted by this BGP
speaker.

# References

[1] Lougheed, K., and Y. Rekhter, "A Border Gateway Protocol (BGP)",
RFC 1163, cisco Systems, T.J. Watson Research Center, IBM Corp.,
June 1990.

[2] Lougheed, K., and Y. Rekhter, "A Border Gateway Protocol 3 (BGP-
3)", RFC 1267, cisco Systems, T.J. Watson Research Center, IBM
Corp., October 1991.

[3] Rekhter, Y., and T. Li, "A Border Gateway Protocol 4 (BGP-4)",
Work in Progress, T.J. Watson Research Center, IBM Corp., cisco
Systems, December 1992.

# Security Considerations

Security issues are not discussed in this memo.

# Author's Address

Dimitry Haskin
Bolt, Beranek & Newman
150 Cambridge Park Drive
Cambridge, MA 02140

Phone: 617-873-8609
Email: dhaskin@bbn.com
