---
rfc: 6232
title: "Cisco Systems, Inc."
date: May 2011
category: Standards
updates: [5301, 5304, 5310]
---

# Abstract

At present, an IS-IS purge does not contain any information
identifying the Intermediate System (IS) that generates the purge.
This makes it difficult to locate the source IS.

To address this issue, this document defines a TLV to be added to
purges to record the system ID of the IS generating it.  Since normal
Link State Protocol Data Unit (LSP) flooding does not change LSP
contents, this TLV should propagate with the purge.

This document updates RFC 5301, RFC 5304, and RFC 5310.

# Status of This Memo

This is an Internet Standards Track document.

This document is a product of the Internet Engineering Task Force
(IETF).  It represents the consensus of the IETF community.  It has
received public review and has been approved for publication by the
Internet Engineering Steering Group (IESG).  Further information on
Internet Standards is available in Section 2 of RFC 5741.

Information about the current status of this document, any errata,
and how to provide feedback on it may be obtained at
http://www.rfc-editor.org/info/rfc6232.

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
  - [2. Requirements Language](#2-requirements-language)
  - [3. The Purge Originator Identification (POI) TLV](#3-the-purge-originator-identification-poi-tlv)
  - [4. Using the Dynamic Hostname TLV in Purges](#4-using-the-dynamic-hostname-tlv-in-purges)
  - [5. Security Considerations](#5-security-considerations)
  - [6. IANA Considerations](#6-iana-considerations)
  - [7. Acknowledgments](#7-acknowledgments)
  - [8. Normative References](#8-normative-references)

# 1. Introduction

The IS-IS [ISO-10589] routing protocol has been widely used in large-
scale IP networks because of its strong scalability and fast
convergence.

The IS-IS protocol floods purges throughout an area, regardless of
which IS initiated the purge.  If a network operator would like to
investigate the cause of the purge, it is difficult to determine the
origin of the purge.  At present, the IS-IS protocol has no mechanism
to locate the originator of a purge.  To address this problem, this
document defines a TLV to be added to purges to record the system ID
of the IS generating the purge.

Field experience has shown several circumstances where an IS can
improperly generate a purge.  These are all due to implementation
deficiencies or implementations that predate [ISO-TC1] and generate a
purge when they receive a corrupted Link State Protocol Data Unit
(LSP).

# 2. Requirements Language

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT",
"SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this
document are to be interpreted as described in [RFC2119].

# 3. The Purge Originator Identification (POI) TLV

This document defines a TLV to be included in purges.  If an IS
generates a purge, it SHOULD include this TLV in the purge with its
own system ID.  If an IS receives a purge that does not include this
TLV, then it SHOULD add this TLV with both its own system ID and the
system ID of the IS from which it received the purge.  This allows
ISs receiving purges to log the system ID of the originator, or the
upstream source of the purge.  This makes it much easier for the
network administrator to locate the origin of the purge and thus the
cause of the purge.  Similarly, this TLV is helpful to developers in
lab situations.

The POI TLV is defined as:

CODE - 13

LENGTH - total length of the value field.

VALUE -

Number of system IDs carried in this TLV (1 octet) -- only the
values 1 and 2 are defined.

System ID of the Intermediate System that inserted this TLV.

System ID of the Intermediate System from which the purge was
received (optional).

The POI TLV SHOULD be found in all purges and MUST NOT be found in
LSPs with a non-zero Remaining Lifetime.

# 4. Using the Dynamic Hostname TLV in Purges

This document also extends the use of the Dynamic hostname TLV
(type 137) [RFC5301] to further aid in the rapid identification of
the system that generated the purge.  This TLV MAY be included in
purges.  Implementations SHOULD include one instance of the Dynamic
hostname TLV if the POI TLV is included.  Only the local hostname
should be inserted.

# 5. Security Considerations

Use of the extensions defined here, with authentication as defined in
[RFC5304] or [RFC5310], will result in the discarding of purges by
legacy systems that are in strict conformance with either of those
RFCs.  This may compromise the correctness/consistency of the routing
database unless all ISs in the network support these extensions.
Therefore, all implementations in a domain implementing
authentication MUST be upgraded to receive the POI TLV before any IS
is allowed to generate a purge with the POI TLV.

More interactions between the POI TLV, the Dynamic hostname TLV, and
the Authentication TLV are described in [RFC6233].

# 6. IANA Considerations

IANA has assigned code point 13 for the 'Purge Originator
Identification' TLV from the IS-IS 'TLV Codepoints' registry.  The
additional values for this TLV should be IIH:n, LSP:y, SNP:n, and
Purge:y.

# 7. Acknowledgments

Many thanks to Adrian Farrel and Daniel King for their comments to
improve this document and move it forward.

The first version of this document was mainly composed by
Lianyuan Li.

Acknowledgments are given to the discussion in the mailing list.
Some improvements to this document are based on the discussion.

# 8. Normative References

[ISO-10589]  ISO, "Intermediate system to Intermediate system
intra-domain routeing information exchange protocol for
use in conjunction with the protocol for providing the
connectionless-mode Network Service (ISO 8473)",
ISO/IEC 10589:2002.

[ISO-TC1]    ISO, "Intermediate system to Intermediate system
intra-domain routeing information exchange protocol for
use in conjunction with the protocol for providing the
connectionless-mode Network Service (ISO 8473) --
Technical Corrigendum 1", ISO/IEC 10589:1992/
Cor.1:1993.

[RFC2119]    Bradner, S., "Key words for use in RFCs to Indicate
Requirement Levels", BCP 14, RFC 2119, March 1997.

[RFC5301]    McPherson, D. and N. Shen, "Dynamic Hostname Exchange
Mechanism for IS-IS", RFC 5301, October 2008.

[RFC5304]    Li, T. and R. Atkinson, "IS-IS Cryptographic
Authentication", RFC 5304, October 2008.

[RFC5310]    Bhatia, M., Manral, V., Li, T., Atkinson, R., White, R.,
and M. Fanto, "IS-IS Generic Cryptographic
Authentication", RFC 5310, February 2009.

[RFC6233]    Li, T. and L. Ginsberg, "IS-IS Registry Extension for
Purges", RFC 6233, May 2011.

# Authors' Addresses

Fang Wei
China Mobile
No. 29, Financial Street, Xicheng District
Beijing  100032
P.R. China

EMail: weifang@chinamobile.com

Yue Qin
China Mobile
No. 29, Financial Street, Xicheng District
Beijing  100032
P.R. China

EMail: qinyue@chinamobile.com

Zhenqiang Li
China Mobile
Unit2, Dacheng Plaza, No. 28 Xuanwumenxi Ave., Xuanwu District
Beijing  100053
P.R. China

EMail: lizhenqiang@chinamobile.com

Tony Li
Cisco Systems, Inc.
170 W. Tasman Dr.
San Jose, CA  95134
USA

EMail: tony.li@tony.li

Jie Dong
Huawei Technologies
KuiKe Building, No. 9 Xinxi Rd., Haidian District
Beijing  100085
P.R. China

EMail: dongjie_dj@huawei.com
