---
rfc: 8425
title: "IANA Considerations for IPv6 Neighbor Discovery"
date: July 2018
category: Standards
updates: [4861]
---

# Abstract

The Prefix Information Option (PIO) in the IPv6 Neighbor Discovery
Router Advertisement message defines an 8-bit flag field; this field
has two flags defined, and the remaining 6 bits are reserved
(Reserved1).  RFC 6275 defines a flag from this field without
creating an IANA registry or updating RFC 4861.  The purpose of this
document is to create an IANA registry for the PIO flags.  This
document updates RFC 4861.

# Status of This Memo

This is an Internet Standards Track document.

This document is a product of the Internet Engineering Task Force
(IETF).  It represents the consensus of the IETF community.  It has
received public review and has been approved for publication by the
Internet Engineering Steering Group (IESG).  Further information on
Internet Standards is available in Section 2 of RFC 7841.

Information about the current status of this document, any errata,
and how to provide feedback on it may be obtained at
https://www.rfc-editor.org/info/rfc8425.

# Copyright Notice

Copyright (c) 2018 IETF Trust and the persons identified as the
document authors.  All rights reserved.

This document is subject to BCP 78 and the IETF Trust's Legal
Provisions Relating to IETF Documents
(https://trustee.ietf.org/license-info) in effect on the date of
publication of this document.  Please review these documents
carefully, as they describe your rights and restrictions with respect
to this document.  Code Components extracted from this document must
include Simplified BSD License text as described in Section 4.e of
the Trust Legal Provisions and are provided without warranty as
described in the Simplified BSD License.

# Table of Contents

  - [1.  Introduction](#1-introduction)
  - [2.  Current Prefix Information Option Flags](#2-current-prefix-information-option-flags)
  - [3.  Updates to RFC 4861](#3-updates-to-rfc-4861)
  - [4.  IANA Considerations](#4-iana-considerations)
  - [5.  Security Considerations](#5-security-considerations)
  - [6.  Normative References](#6-normative-references)
  - [Author's Address](#authors-address)

# 1. Introduction

The Prefix Information Option (PIO) in the IPv6 Neighbor Discovery
Router Advertisement message defines an 8-bit flag field; this field
has two flags defined and the remaining 6 bits are reserved
(Reserved1).  RFC 6275 defines a flag from this field without
creating an IANA registry or updating RFC 4861.  The purpose of this
document is to create a new registry for the PIO flags.

# 2. Current Prefix Information Option Flags

Currently, the Neighbor Discovery Protocol Prefix Information Option
[RFC4861] contains the following one-bit flags defined in published
RFCs:

+-+-+-+-+-+-+-+-+
|L|A|R|Reserved1|
+-+-+-+-+-+-+-+-+

Figure 1: PIO Flags

L - On-link Flag [RFC4861]

A - Autonomous Address Configuration Flag [RFC4861]

R - Router Address Flag [RFC6275]

Reserved1 - Reserved

# 3. Updates to RFC 4861

This document updates Section 4.6.2 "Prefix Information" of [RFC4861]
to point to the IANA registry that is created in this document (see
Section 4).

Specifically, the current list of flags in the Prefix Information
Option can be found in the "IPv6 Neighbor Discovery Prefix
Information Option Flags" registry.

# 4. IANA Considerations

IANA has created a new registry for IPv6 Neighbor Discovery Prefix
Information Option flags.  This registry includes the current flags
in the PIO.  The initial contents of the registry are as follows:

+----------------+---------------------------------+-----------+
| PIO Option Bit | Description                     | Reference |
+----------------+---------------------------------+-----------+
| 0              | L - On-link Flag                | [RFC4861] |
| 1              | A - Autonomous Address          | [RFC4861] |
|                |     Configuration Flag          |           |
| 2              | R - Router Address Flag         | [RFC6275] |
| 3-7            | Reserved                        |           |
+----------------+---------------------------------+-----------+

Figure 2: IPv6 Neighbor Discovery Prefix Information Option Flags

The assignment of new flags in the PIO option header requires
Standards Action [RFC8126].

The registry for these flags is available at
<http://www.iana.org/assignments/icmpv6-parameters>.

# 5. Security Considerations

This document has no security considerations.

# 6. Normative References

[RFC4861]  Narten, T., Nordmark, E., Simpson, W., and H. Soliman,
"Neighbor Discovery for IP version 6 (IPv6)", RFC 4861,
DOI 10.17487/RFC4861, September 2007,
<https://www.rfc-editor.org/info/rfc4861>.

[RFC6275]  Perkins, C., Ed., Johnson, D., and J. Arkko, "Mobility
Support in IPv6", RFC 6275, DOI 10.17487/RFC6275, July
2011, <https://www.rfc-editor.org/info/rfc6275>.

[RFC8126]  Cotton, M., Leiba, B., and T. Narten, "Guidelines for
Writing an IANA Considerations Section in RFCs", BCP 26,
RFC 8126, DOI 10.17487/RFC8126, June 2017,
<https://www.rfc-editor.org/info/rfc8126>.

# Author's Address

Ole Troan
Cisco Systems
Philip Pedersens vei 1
Lysaker  1366
Norway

Email: ot@cisco.com
