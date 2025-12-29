---
title: "IANA Allocations for Mobile Ad Hoc Network (MANET) Protocols"
rfc: 5498
date: March 2009
category: Standards---


# Abstract

This document enumerates several common IANA allocations for use by
Mobile Ad hoc NETwork (MANET) protocols.  The following well-known
numbers are required: a UDP port number, an IP protocol number, and a
link-local multicast group address.

# Table of Contents

  - [1. Introduction](#1-introduction)
  - [2. Conventions Used in This Document](#2-conventions-used-in-this-document)
  - [3. UDP Port Number](#3-udp-port-number)
  - [4. IP Protocol Number](#4-ip-protocol-number)
  - [5. Link-Local Multicast Group for MANET Routers](#5-link-local-multicast-group-for-manet-routers)
  - [6. IANA Considerations](#6-iana-considerations)
  - [7. Security Considerations](#7-security-considerations)
  - [8. Acknowledgements](#8-acknowledgements)
  - [9. References](#9-references)
    - [9.1. Normative References](#91-normative-references)
    - [9.2. Informative References](#92-informative-references)

# 1. Introduction

This document enumerates several common IANA allocations for use by
one or more protocols that conform to [RFC5444].  The following
well-known numbers are required: a UDP port number, an IP protocol
number, and a link-local multicast group address.  All interoperable
protocols running on these well-known IANA allocations MUST conform
to [RFC5444].  [RFC5444] provides a common format that enables one or
more protocols to share the IANA allocations defined in this document
unambiguously.

# 2. Conventions Used in This Document

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT",
"SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this
document are to be interpreted as described in RFC 2119 [RFC2119].

# 3. UDP Port Number

MANET routers require a well-known UDP port number [IANA] to send and
receive MANET routing protocol packets.  The title of this UDP port
is "manet".  The value of this UDP port is 269.

# 4. IP Protocol Number

MANET routers require a well-known IP protocol number [IANA] to send
and receive MANET routing protocol packets.  The title of this IP
protocol number is "manet".  The value of this IP protocol number is
138.

# 5. Link-Local Multicast Group for MANET Routers

MANET routers require a well-known, link-local multicast address
[RFC4291] to send and receive MANET routing protocol packets.  The
name of the multicast address to reach link-local (LL) MANET routers
is "LL-MANET-Routers".

For IPv4, a well-known, link-local scope multicast address is
required.  The address for LL-MANET-Routers is 224.0.0.109.

For IPv6, a well-known, link-local scope multicast address is
required.  The address for LL-MANET-Routers is FF02:0:0:0:0:0:0:6D.

# 6. IANA Considerations

This document enumerates several common IANA allocations for use by
one or more protocols that conform to [RFC5444].  Specifically, the
following well-known numbers have been assigned: a UDP port
(Section 3), an IP protocol number (Section 4), and a link-local
multicast group address (Section 5).

Action 1:

IANA has made the following assignments in the "PORT NUMBERS"
registry:

sub-registry "WELL KNOWN PORT NUMBERS"

Keyword Decimal Description     References
------- ------- -----------     ----------
manet   269/udp MANET Protocols [RFC5498]

Action 2:

IANA has made the following assignments in the "PROTOCOL NUMBERS"
registry:

sub-registry "WELL KNOWN PORT NUMBERS"

Keyword Decimal Description     References
------- ------- -----------     ----------
manet   138     MANET Protocols [RFC5498]

Action 3:

IANA has made the following assignments in the "Internet Multicast
Addresses" registry:

sub-registry "224.0.0.0 - 224.0.0.255 (224.0.0/24) Local Network
Control Block"

224.0.0.109 LL-MANET-Routers   [RFC5498]

Action 4:

IANA has made the following assignments in the "INTERNET PROTOCOL
VERSION 6 MULTICAST ADDRESSES" registry:

sub-registry "Fixed Scope Multicast Addresses"

sub-sub-registry "Link-Local Scope"

FF02:0:0:0:0:0:0:6D LL-MANET-Routers [RFC5498]

# 7. Security Considerations

This document specifies only well-known numbers for protocols that
conform to [RFC5444], and it not does not specify the protocols that
carry the information across the network.  Each protocol using these
well-known numbers may have its own set of security issues, but those
issues are not affected by using the IANA allocations specified
herein.

The security issues associated with possibly operating multiple
cooperating protocols using the same IANA assignments (e.g., UDP
port) MUST be addressed in each protocol's specification.

# 8. Acknowledgements

Fred Templin, Bill Fenner, Alexandru Petrescu, Sam Weiler, Ross
Callon, and Lars Eggert provided valuable input to this document.

# 9. References

## 9.1. Normative References

[RFC2119]  Bradner, S., "Key words for use in RFCs to Indicate
Requirement Levels", BCP 14, RFC 2119, March 1997.

[RFC4291]  Hinden, R. and S. Deering, "IP Version 6 Addressing
Architecture", RFC 4291, February 2006.

[RFC5444]  Clausen, T., Dearlove, C., Dean, J., and C. Adjih,
"Generalized Mobile Ad Hoc Network (MANET) Packet/Message
Format", RFC 5444, February 2009.

## 9.2. Informative References

[IANA]     http://www.iana.org/

# Author's Address

Ian D Chakeres
CenGen
9250 Bendix Road North
Columbia MD 21045  USA

EMail: ian.chakeres@gmail.com
URI:   http://www.ianchak.com/
