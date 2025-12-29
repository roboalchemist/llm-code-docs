---
rfc: 6308
title: "Overview of the Internet Multicast Addressing Architecture"
date: June 2011
category: Informational
obsoletes: [2908]
---

# Abstract

The lack of up-to-date documentation on IP multicast address
allocation and assignment procedures has caused a great deal of
confusion.  To clarify the situation, this memo describes the
allocation and assignment techniques and mechanisms currently (as of
this writing) in use.

# Status of This Memo

This document is not an Internet Standards Track specification; it is
published for informational purposes.

This document is a product of the Internet Engineering Task Force
(IETF).  It represents the consensus of the IETF community.  It has
received public review and has been approved for publication by the
Internet Engineering Steering Group (IESG).  Not all documents
approved by the IESG are a candidate for any level of Internet
Standard; see Section 2 of RFC 5741.

Information about the current status of this document, any errata,
and how to provide feedback on it may be obtained at
http://www.rfc-editor.org/info/rfc6308.

# Copyright Notice

Copyright (c) 2011 IETF Trust and the persons identified as the
document authors.  All rights reserved.

This document is subject to BCP 78 and the IETF Trust's Legal
Provisions Relating to IETF Documents
(http://trustee.ietf.org/license-info) in effect on the date of
publication of this document.  Please review these documents
carefully, as they describe your rights and restrictions with respect
to this document.  Code Components extracted from this document must
include Simplified BSD License text as described in Section 4.e of
the Trust Legal Provisions and are provided without warranty as
described in the Simplified BSD License.

# Table of Contents

  - [1. Introduction](#1-introduction)
    - [1.1. Terminology: Allocation or Assignment](#11-terminology-allocation-or-assignment)
  - [2. Multicast Address Allocation](#2-multicast-address-allocation)
    - [2.1. Derived Allocation](#21-derived-allocation)
      - [2.1.1. GLOP Allocation](#211-glop-allocation)
      - [2.1.2. Unicast-Prefix-Based Allocation](#212-unicast-prefix-based-allocation)
    - [2.2. Administratively Scoped Allocation](#22-administratively-scoped-allocation)
    - [2.3. Static IANA Allocation](#23-static-iana-allocation)
    - [2.4. Dynamic Allocation](#24-dynamic-allocation)
  - [3. Multicast Address Assignment](#3-multicast-address-assignment)
    - [3.1. Derived Assignment](#31-derived-assignment)
    - [3.2. SSM Assignment inside the Node](#32-ssm-assignment-inside-the-node)
    - [3.3. Manually Configured Assignment](#33-manually-configured-assignment)
    - [3.4. Static IANA Assignment](#34-static-iana-assignment)
      - [3.4.1. Global IANA Assignment](#341-global-iana-assignment)
      - [3.4.2. Scope-Relative IANA Assignment](#342-scope-relative-iana-assignment)
    - [3.5. Dynamic Assignments](#35-dynamic-assignments)
  - [4. Summary and Future Directions](#4-summary-and-future-directions)
    - [4.1. Prefix Allocation](#41-prefix-allocation)
    - [4.2. Address Assignment](#42-address-assignment)
    - [4.3. Future Actions](#43-future-actions)
  - [5. Acknowledgements](#5-acknowledgements)
  - [6. IANA Considerations](#6-iana-considerations)
  - [7. Security Considerations](#7-security-considerations)
  - [8. References](#8-references)
    - [8.1. Normative References](#81-normative-references)
    - [8.2. Informative References](#82-informative-references)

# 1. Introduction

Good, up-to-date documentation of IP multicast is close to
non-existent.  Particularly, this is an issue with multicast address
allocations (to networks and sites) and assignments (to hosts and
applications).  This problem is stressed by the fact that there
exists confusing or misleading documentation on the subject
[RFC2908].  The consequence is that those who wish to learn about IP
multicast and how the addressing works do not get a clear view of the
current situation.

The aim of this document is to provide a brief overview of multicast
addressing and allocation techniques.  The term "addressing
architecture" refers to the set of addressing mechanisms and methods
in an informal manner.

It is important to note that Source-Specific Multicast (SSM)
[RFC4607] does not have these addressing problems because SSM group
addresses have only local significance; hence, this document focuses
on the Any Source Multicast (ASM) model.

This memo obsoletes and re-classifies RFC 2908 to Historic, and
re-classifies RFCs 2776 and 2909 to Historic.

## 1.1. Terminology: Allocation or Assignment

Almost all multicast documents and many other RFCs (such as DHCPv4
[RFC2131] and DHCPv6 [RFC3315]) have used the terms "address
allocation" and "address assignment" interchangeably.  However, the
operator and address management communities use these terms for two
conceptually different processes.

In unicast operations, address allocations refer to leasing a large
block of addresses from the Internet Assigned Numbers Authority
(IANA) to a Regional Internet Registry (RIR), or from an RIR to a
Local Internet Registry (LIR), possibly through a National Internet
Registry (NIR).  Address assignments, on the other hand, are the
leases of smaller address blocks or even single addresses to the end-
user sites or end-users themselves.

Therefore, in this memo, we will separate the two different
functions: "allocation" describes how larger blocks of addresses are
obtained by the network operators, and "assignment" describes how
applications, nodes, or sets of nodes obtain a multicast address for
their use.

# 2. Multicast Address Allocation

Multicast address allocation, i.e., how a network operator might be
able to obtain a larger block of addresses, can be handled in a
number of ways, as described below.

Note that these are all only pertinent to ASM -- SSM requires no
address block allocation because the group address has only local
significance (however, we discuss the address assignment inside the
node in Section 3.2).

## 2.1. Derived Allocation

Derived allocations take the unicast prefix or some other properties
of the network (e.g., an autonomous system (AS) number) to determine
unique multicast address allocations.

### 2.1.1. GLOP Allocation

GLOP address allocation [RFC3180] inserts the 16-bit public AS number
in the middle of the IPv4 multicast prefix 233.0.0.0/8, so that each
AS number can get a /24 worth of multicast addresses.  While this is
sufficient for multicast testing or small-scale use, it might not be
sufficient in all cases for extensive multicast use.

A minor operational debugging issue with GLOP addresses is that the
connection between the AS and the prefix is not apparent from the
prefix when the AS number is greater than 255, but has to be
calculated (e.g., as described in [RFC3180], AS 5662 maps to
233.22.30.0/24).  A usage issue is that GLOP addresses are not tied
to any prefix but to routing domains, so they cannot be used or
calculated automatically.

GLOP mapping is not available with 4-byte AS numbers [RFC4893].
Unicast-prefix-based allocation or an IANA allocation from "AD-HOC
Block III" (the previous so-called "EGLOP" (Extended GLOP) block)
could be used instead, as needed.

The GLOP allocation algorithm has not been defined for IPv6 multicast
because the unicast-prefix-based allocation (described below)
addresses the same need in a simpler fashion.

### 2.1.2. Unicast-Prefix-Based Allocation

RFC 3306 [RFC3306] describes a mechanism that embeds up to 64 high-
order bits of an IPv6 unicast address in the prefix part of the IPv6
multicast address, leaving at least 32 bits of group-id space
available after the prefix mapping.

A similar IPv4 mapping is described in [RFC6034], but it provides a
limited number of addresses (e.g., 1 per IPv4 /24 block).

The IPv6 unicast-prefix-based allocations are an extremely useful way
to allow each network operator, even each subnet, to obtain multicast
addresses easily, through an easy computation.  Further, as the IPv6
multicast header also includes the scope value [RFC4291], multicast
groups of smaller scope can also be used with the same mapping.

The IPv6 Embedded Rendezvous Point (RP) technique [RFC3956], used
with Protocol Independent Multicast - Sparse Mode (PIM-SM), further
leverages the unicast-prefix-based allocations, by embedding the
unicast prefix and interface identifier of the PIM-SM RP in the
prefix.  This provides all the necessary information needed to the
routing systems to run the group in either inter- or intra-domain
operation.  A difference from RFC 3306 is, however, that the hosts

cannot calculate their "multicast prefix" automatically (as the
prefix depends on the decisions of the operator setting up the RP),
but instead require an assignment method.

All the IPv6 unicast-prefix-based allocation techniques provide a
sufficient amount of multicast address space for network operators.

## 2.2. Administratively Scoped Allocation

Administratively scoped multicast address allocation [RFC2365] is
provided by two different means: under 239.0.0.0/8 in IPv4 or by
4-bit encoding in the IPv6 multicast address prefix [RFC4291].

Since IPv6 administratively scoped allocations can be handled with
unicast-prefix-based multicast addressing as described in
Section 2.1.2, we'll only discuss IPv4 in this section.

The IPv4 administratively scoped prefix 239.0.0.0/8 is further
divided into Local Scope (239.255.0.0/16) and Organization Local
Scope (239.192.0.0/14); other parts of the administrative scopes are
either reserved for expansion or undefined [RFC2365].  However,
RFC 2365 is ambiguous as to whether the enterprises or the IETF are
allowed to expand the space.

Topologies that act under a single administration can easily use the
scoped multicast addresses for their internal groups.  Groups that
need to be shared between multiple routing domains (even if not
propagated through the Internet) are more problematic and typically
need an assignment of a global multicast address because their scope
is undefined.

There are a large number of multicast applications (such as "Norton
Ghost") that are restricted either to a link or a site, and it is
extremely undesirable to propagate them further (beyond the link or
the site).  Typically, many such applications have been given or have
hijacked a static IANA address assignment.  Given the fact that
assignments to typically locally used applications come from the same
range as global applications, implementing proper propagation
limiting is challenging.  Filtering would be easier if a separate,
identifiable range would be used for such assignments in the future;
this is an area of further future work.

There has also been work on a protocol to automatically discover
multicast scope zones [RFC2776], but it has never been widely
implemented or deployed.

## 2.3. Static IANA Allocation

In some rare cases, organizations may have been able to obtain static
multicast address allocations (of up to 256 addresses) directly from
IANA.  Typically, these have been meant as a block of static
assignments to multicast applications, as described in Section 3.4.1.
If another means of obtaining addresses is available, that approach
is preferable.

Especially for those operators that only have a 32-bit AS number and
need IPv4 addresses, an IANA allocation from "AD-HOC Block III" (the
previous so-called "EGLOP" block) is an option [RFC5771].

## 2.4. Dynamic Allocation

RFC 2908 [RFC2908] proposed three different layers of multicast
address allocation and assignment, where layer 3 (inter-domain
allocation) and layer 2 (intra-domain allocation) could be applicable
here.  The Multicast Address-Set Claim Protocol (MASC) [RFC2909] is
an example of the former, and the Multicast Address Allocation
Protocol (AAP) [MALLOC-AAP] (abandoned in 2000 due to lack of
interest and technical problems) is an example of the latter.

Both of the proposed allocation protocols were quite complex, and
have never been deployed or seriously implemented.

It can be concluded that dynamic multicast address allocation
protocols provide no benefit beyond GLOP/unicast-prefix-based
mechanisms and have been abandoned.

# 3. Multicast Address Assignment

There are a number of possible ways for an application, node, or set
of nodes to learn a multicast address, as described below.

Any IPv6 address assignment method should be aware of the guidelines
for the assignment of group-IDs for IPv6 multicast addresses
[RFC3307].

## 3.1. Derived Assignment

There are significantly fewer options for derived address assignment
compared to derived allocation.  Derived multicast assignment has
only been specified for IPv6 link-scoped multicast [RFC4489], where
the EUI64 is embedded in the multicast address, providing a node with
unique multicast addresses for link-local ASM communications.

## 3.2. SSM Assignment inside the Node

While SSM multicast addresses have only local (to the node)
significance, there is still a minor issue on how to assign the
addresses between the applications running on the same IP address.

This assignment is not considered to be a problem, because typically
the addresses for these applications are selected manually or
statically, but if done using an Application Programming Interface
(API), the API could check that the addresses do not conflict prior
to assigning one.

## 3.3. Manually Configured Assignment

With manually configured assignment, a network operator who has a
multicast address prefix assigns the multicast group addresses to the
requesting nodes using a manual process.

Typically, the user or administrator that wants to use a multicast
address for a particular application requests an address from the
network operator using phone, email, or similar means, and the
network operator provides the user with a multicast address.  Then
the user/administrator of the node or application manually configures
the application to use the assigned multicast address.

This is a relatively simple process; it has been sufficient for
certain applications that require manual configuration in any case,
or that cannot or do not want to justify a static IANA assignment.
The manual assignment works when the number of participants in a
group is small, as each participant has to be manually configured.

This is the most commonly used technique when the multicast
application does not have a static IANA assignment.

## 3.4. Static IANA Assignment

In contrast to manually configured assignment, as described above,
static IANA assignment refers to getting an assignment for the
particular application directly from IANA.  There are two main forms
of IANA assignment: global and scope-relative.  Guidelines for IANA
are described in [RFC5771].

### 3.4.1. Global IANA Assignment

Globally unique address assignment is seen as lucrative because it's
the simplest approach for application developers, since they can then
hard-code the multicast address.  Hard-coding requires no lease of
the usable multicast address, and likewise the client applications do

not need to perform any kind of service discovery (but depend on
hard-coded addresses).  However, there is an architectural scaling
problem with this approach, as it encourages a "land-grab" of the
limited multicast address space.

### 3.4.2. Scope-Relative IANA Assignment

IANA also assigns numbers as an integer offset from the highest
address in each IPv4 administrative scope, as described in [RFC2365].
For example, the SLPv2 discovery scope-relative offset is "2", so the
SLPv2 discovery address within IPv4 Local-Scope (239.255.0.0/16) is
"239.255.255.253"; within the IPv4 Organization Local-Scope
(239.192.0.0/14), it is "239.195.255.253"; and so on.

Similar scope-relative assignments also exist with IPv6 [RFC2375].
As IPv6 multicast addresses have much more flexible scoping, scope-
relative assignments are also applicable to global scopes.  The
assignment policies are described in [RFC3307].

## 3.5. Dynamic Assignments

Layer 1 as defined in RFC 2908 [RFC2908] described dynamic assignment
from Multicast Address Allocation Servers (MAAS) to applications and
nodes, with the Multicast Address Dynamic Client Allocation Protocol
(MADCAP) [RFC2730] as an example.  Since then, other mechanisms have
also been proposed (e.g., DHCPv6 assignment
[MCAST-DHCPv6]), but these have not gained traction.

It would be rather straightforward to deploy a dynamic assignment
protocol that would lease group addresses based on a multicast prefix
to applications wishing to use multicast.  However, only few have
implemented MADCAP (i.e., it is not significantly deployed).  It is
not clear if the sparse deployment is due to a lack of need for the
protocol.  Moreover, it is not clear how widely, for example, the
APIs for communication between the multicast application and the
MADCAP client operating at the host have been implemented [RFC2771].

An entirely different approach is the Session Announcement Protocol
(SAP) [RFC2974].  In addition to advertising global multicast
sessions, the protocol also has associated ranges of addresses for
both IPv4 and IPv6 that can be used by SAP-aware applications to
create new groups and new group addresses.  Creating a session (and
obtaining an address) is a rather tedious process, which is why it
isn't done all that often.  It is also worth noting that the IPv6 SAP
address is unroutable in the inter-domain multicast.

Conclusions about dynamic assignment protocols are that:

1.  multicast is not significantly attractive in the first place,

2.  most applications have a static IANA assignment and thus require
no dynamic or manual assignment,

3.  those applications that cannot be easily satisfied with IANA or
manual assignment (i.e., where dynamic assignment would be
desirable) are rather marginal, or

4.  there are other reasons why dynamic assignments are not seen as a
useful approach (for example, issues related to service
discovery/rendezvous).

In consequence, more work on rendezvous/service discovery would be
needed to make dynamic assignments more useful.

# 4. Summary and Future Directions

This section summarizes the mechanisms and analysis discussed in this
memo, and presents some potential future directions.

## 4.1. Prefix Allocation

A summary of prefix allocation methods for ASM is shown in Figure 1.

+-------+--------------------------------+--------+--------+
| Sect. | Prefix allocation method       | IPv4   | IPv6   |
+-------+--------------------------------+--------+--------+
| 2.1.1 | Derived: GLOP                  |  Yes   | NoNeed*|
| 2.1.2 | Derived: Unicast-prefix-based  |   No   |  Yes   |
|  2.2  | Administratively scoped        |  Yes   | NoNeed*|
|  2.3  | Static IANA allocation         |  Yes** |   No   |
|  2.4  | Dynamic allocation protocols   |   No   |   No   |
+-------+--------------------------------+--------+--------+
*  = the need satisfied by IPv6 unicast-prefix-based allocation
** = mainly using the AD-HOC block III (formerly called "EGLOP")

Figure 1

o  Only ASM is affected by the assignment/allocation issues.

o  With IPv4, GLOP allocations provide a sufficient IPv4 multicast
allocation mechanism for those that have a 16-bit AS number.  IPv4
unicast-prefix-based allocation offers some addresses.  IANA is
also allocating from the AD-HOC block III (formerly called
"EGLOP"), especially with 32-bit AS number holders in mind.
Administratively scoped allocations provide the opportunity for
internal IPv4 allocations.

o  With IPv6, unicast-prefix-based addresses and the derivatives
provide a good allocation strategy, and this also works for scoped
multicast addresses.

o  Dynamic allocations are too complex and unnecessary a mechanism.

## 4.2. Address Assignment

A summary of address assignment methods is shown in Figure 2.

+--------+--------------------------------+----------+----------+
| Sect.  | Address assignment method      | IPv4     | IPv6     |
+--------+--------------------------------+----------+----------+
|  3.1   | Derived: link-scope addresses  |  No      |   Yes    |
|  3.2   | SSM (inside the node)          |  Yes     |   Yes    |
|  3.3   | Manual assignment              |  Yes     |   Yes    |
|  3.4.1 | Global IANA/RIR assignment     |LastResort|LastResort|
|  3.4.2 | Scope-relative IANA assignment |  Yes     |   Yes    |
|  3.5   | Dynamic assignment protocols   |  Yes     |   Yes    |
+--------+--------------------------------+----------+----------+

Figure 2

o  Manually configured assignment is typical today, and works to a
sufficient degree in smaller scale.

o  Global IANA assignment has been done extensively in the past.
Scope-relative IANA assignment is acceptable, but the size of the
pool is not very high.  Inter-domain routing of IPv6 IANA-assigned
prefixes is likely going to be challenging, and as a result that
approach is not very appealing.

o  Dynamic assignment, e.g., MADCAP, has been implemented, but there
is no wide deployment.  Therefore, either there are other gaps in
the multicast architecture, or there is no sufficient demand for
it in the first place when manual and static IANA assignments are
available.  Assignments using SAP also exist but are not common;
global SAP assignment is infeasible with IPv6.

o  Derived assignments are only applicable in a fringe case of link-
scoped multicast.

## 4.3. Future Actions

o  Multicast address discovery/"rendezvous" needs to be analyzed at
more length, and an adequate solution provided.  See
[ADDRDISC-PROB] and [MSA-REQ] for more information.

o  The IETF should consider whether to specify more ranges of the
IPv4 administratively scoped address space for static allocation
for applications that should not be routed over the Internet (such
as backup software, etc. -- so that these wouldn't need to use
global addresses, which should never leak in any case).

o  The IETF should consider its static IANA allocations policy, e.g.,
"locking it down" to a stricter policy (like "IETF Consensus") and
looking at developing the discovery/rendezvous functions, if
necessary.

# 5. Acknowledgements

Tutoring a couple of multicast-related papers, the latest by Kaarle
Ritvanen [RITVANEN], convinced the author that updated multicast
address assignment/allocation documentation is needed.

Multicast address allocations/assignments were discussed at the
MBONED WG session at IETF 59 [MBONED-IETF59].

Dave Thaler, James Lingard, and Beau Williamson provided useful
feedback for the preliminary version of this memo.  Myung-Ki Shin,
Jerome Durand, John Kristoff, Dave Price, Spencer Dawkins, and Alfred
Hoenes also suggested improvements.

# 6. IANA Considerations

IANA considerations in Sections 4.1.1 and 4.1.2 of obsoleted and now
Historic [RFC2908] were never implemented in the IANA registry.

# 7. Security Considerations

This memo only describes different approaches to allocating and
assigning multicast addresses, and this has no security
considerations; the security analysis of the mentioned protocols is
out of scope of this memo.

Obviously, the dynamic assignment protocols in particular are
inherently vulnerable to resource exhaustion attacks, as discussed,
e.g., in [RFC2730].

# 8. References

## 8.1. Normative References

[RFC2365]   Meyer, D., "Administratively Scoped IP Multicast",
BCP 23, RFC 2365, July 1998.

[RFC3180]   Meyer, D. and P. Lothberg, "GLOP Addressing in 233/8",
BCP 53, RFC 3180, September 2001.

[RFC3306]   Haberman, B. and D. Thaler, "Unicast-Prefix-based IPv6
Multicast Addresses", RFC 3306, August 2002.

[RFC3307]   Haberman, B., "Allocation Guidelines for IPv6 Multicast
Addresses", RFC 3307, August 2002.

[RFC3956]   Savola, P. and B. Haberman, "Embedding the Rendezvous
Point (RP) Address in an IPv6 Multicast Address",
RFC 3956, November 2004.

[RFC4291]   Hinden, R. and S. Deering, "IP Version 6 Addressing
Architecture", RFC 4291, February 2006.

[RFC4489]   Park, J-S., Shin, M-K., and H-J. Kim, "A Method for
Generating Link-Scoped IPv6 Multicast Addresses",
RFC 4489, April 2006.

[RFC4607]   Holbrook, H. and B. Cain, "Source-Specific Multicast for
IP", RFC 4607, August 2006.

[RFC5771]   Cotton, M., Vegoda, L., and D. Meyer, "IANA Guidelines
for IPv4 Multicast Address Assignments", BCP 51,
RFC 5771, March 2010.

[RFC6034]   Thaler, D., "Unicast-Prefix-Based IPv4 Multicast
Addresses", RFC 6034, October 2010.

## 8.2. Informative References

[ADDRDISC-PROB]
Savola, P., "Lightweight Multicast Address Discovery
Problem Space", Work in Progress, March 2006.

[MALLOC-AAP]
Handley, M. and S. Hanna, "Multicast Address Allocation
Protocol (AAP)", Work in Progress, June 2000.

[MBONED-IETF59]
"MBONED WG session at IETF59",
<http://www.ietf.org/proceedings/04mar/172.htm>.

[MCAST-DHCPv6]
Durand, J., "IPv6 multicast address assignment with
DHCPv6", Work in Progress, February 2005.

[MSA-REQ]   Asaeda, H. and V. Roca, "Requirements for IP Multicast
Session Announcement", Work in Progress, March 2010.

[RFC2131]   Droms, R., "Dynamic Host Configuration Protocol",
RFC 2131, March 1997.

[RFC2375]   Hinden, R. and S. Deering, "IPv6 Multicast Address
Assignments", RFC 2375, July 1998.

[RFC2730]   Hanna, S., Patel, B., and M. Shah, "Multicast Address
Dynamic Client Allocation Protocol (MADCAP)", RFC 2730,
December 1999.

[RFC2771]   Finlayson, R., "An Abstract API for Multicast Address
Allocation", RFC 2771, February 2000.

[RFC2776]   Handley, M., Thaler, D., and R. Kermode, "Multicast-Scope
Zone Announcement Protocol (MZAP)", RFC 2776, February
2000.

[RFC2908]   Thaler, D., Handley, M., and D. Estrin, "The Internet
Multicast Address Allocation Architecture", RFC 2908,
September 2000.

[RFC2909]   Radoslavov, P., Estrin, D., Govindan, R., Handley, M.,
Kumar, S., and D. Thaler, "The Multicast Address-Set
Claim (MASC) Protocol", RFC 2909, September 2000.

[RFC2974]   Handley, M., Perkins, C., and E. Whelan, "Session
Announcement Protocol", RFC 2974, October 2000.

[RFC3315]   Droms, R., Ed., Bound, J., Volz, B., Lemon, T., Perkins,
C., and M. Carney, "Dynamic Host Configuration Protocol
for IPv6 (DHCPv6)", RFC 3315, July 2003.

[RFC4893]   Vohra, Q. and E. Chen, "BGP Support for Four-octet AS
Number Space", RFC 4893, May 2007.

[RITVANEN]  Ritvanen, K., "Multicast Routing and Addressing", HUT
Report, Seminar on Internetworking, May 2004,
<http://www.tml.hut.fi/Studies/T-110.551/2004/papers/>.

# Author's Address

Pekka Savola
CSC - Scientific Computing Ltd.
Espoo
Finland

EMail: psavola@funet.fi
