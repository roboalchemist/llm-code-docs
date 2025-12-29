---
rfc: 7963
title: "Huawei Technologies"
date: August 2016
category: Informational
---

# Abstract

RFCs 4328 and 7139 provide signaling extensions in Resource
ReserVation Protocol - Traffic Engineering (RSVP-TE) to control the
full set of Optical Transport Network (OTN) features.  However, these
specifications do not cover the additional Optical channel Data Unit
(ODU) containers defined in G.Sup43 (ODU1e, ODU3e1, and ODU3e2).
This document defines new Signal Types for these additional
containers.

# Status of This Memo

This document is not an Internet Standards Track specification; it is
published for informational purposes.

This document is a product of the Internet Engineering Task Force
(IETF).  It represents the consensus of the IETF community.  It has
received public review and has been approved for publication by the
Internet Engineering Steering Group (IESG).  Not all documents
approved by the IESG are a candidate for any level of Internet
Standard; see Section 2 of RFC 7841.

Information about the current status of this document, any errata,
and how to provide feedback on it may be obtained at
http://www.rfc-editor.org/info/rfc7963.

RFC 7963       RSVP-TE Ext for Signal Types in G.709 OTNs    August 2016

# Copyright Notice

Copyright (c) 2016 IETF Trust and the persons identified as the
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

This document may contain material from IETF Documents or IETF
Contributions published or made publicly available before November
10, 2008.  The person(s) controlling the copyright in some of this
material may not have granted the IETF Trust the right to allow
modifications of such material outside the IETF Standards Process.
Without obtaining an adequate license from the person(s) controlling
the copyright in such materials, this document may not be modified
outside the IETF Standards Process, and derivative works of it may
not be created outside the IETF Standards Process, except to format
it for publication as an RFC or to translate it into languages other
than English.

# Table of Contents

  - [1. Introduction](#1-introduction)
  - [2. RSVP-TE Extension for Additional Signal Types](#2-rsvp-te-extension-for-additional-signal-types)
  - [3. Security Considerations](#3-security-considerations)
  - [4. IANA Considerations](#4-iana-considerations)
  - [5. References](#5-references)
  - [5.1. Normative References](#51-normative-references)
  - [5.2. Informative References](#52-informative-references)
  - [Acknowledgments](#acknowledgments)
  - [Authors' Addresses](#authors-addresses)

# 3. Security Considerations

This document does not introduce any additional security issues
beyond those identified in [RFC7139].

# 4. IANA Considerations

IANA maintains the "Generalized Multi-Protocol Label Switching
(GMPLS) Signaling Parameters" registry that contains the "OTN Signal
Type" subregistry.  IANA has added the following three allocations
for ODU1e, ODU3e1, and ODU3e2 in the subregistry via the
Specification Required policy [RFC5226]:

Value            Type
-----            ----
23               ODU1e  (10Gbps Ethernet [G.Sup43])
26               ODU3e1 (40Gbps Ethernet [G.Sup43])
27               ODU3e2 (40Gbps Ethernet [G.Sup43])

These Signal Types are carried in the Traffic Parameters in OTN-TDM
SENDER_TSPEC and OTN-TDM FLOWSPEC objects [RFC7139].

RFC 7963       RSVP-TE Ext for Signal Types in G.709 OTNs    August 2016

# 5. References

## 5.1. Normative References

[RFC4328]  Papadimitriou, D., Ed., "Generalized Multi-Protocol Label
Switching (GMPLS) Signaling Extensions for G.709 Optical
Transport Networks Control", RFC 4328,
DOI 10.17487/RFC4328, January 2006,
<http://www.rfc-editor.org/info/rfc4328>.

[RFC7139]  Zhang, F., Ed., Zhang, G., Belotti, S., Ceccarelli, D.,
and K. Pithewan, "GMPLS Signaling Extensions for Control
of Evolving G.709 Optical Transport Networks", RFC 7139,
DOI 10.17487/RFC7139, March 2014,
<http://www.rfc-editor.org/info/rfc7139>.

[RFC7892]  Ali, Z., Bonfanti, A., Hartley, M., and F. Zhang, "IANA
Allocation Procedures for the GMPLS OTN Signal Type
Registry", RFC 7892, DOI 10.17487/RFC7892, May 2016,
<http://www.rfc-editor.org/info/rfc7892>.

## 5.2. Informative References

```
   [G.709-v3] ITU-T, "Interfaces for the optical transport network",
```

Recommendation G.709/Y.1331, June 2016.

```
   [G.Sup43]  ITU-T, "Transport of IEEE 10GBASE-R in optical transport
              networks (OTN)", Recommendation G.Sup43, February 2011.

   [RFC5226]  Narten, T. and H. Alvestrand, "Guidelines for Writing an
              IANA Considerations Section in RFCs", BCP 26, RFC 5226,
              DOI 10.17487/RFC5226, May 2008,
              <http://www.rfc-editor.org/info/rfc5226>.

```

# Acknowledgments

The authors would like to thank Dieter Beller, Lou Berger, Deborah
Brungard, Daniele Ceccarelli, Adrian Farrel, and Sudip Shukla for
their comments.

RFC 7963       RSVP-TE Ext for Signal Types in G.709 OTNs    August 2016

# Authors' Addresses

Zafar Ali
Cisco Systems

Email: zali@cisco.com

Antonello Bonfanti
Cisco Systems

Email: abonfant@cisco.com

Matt Hartley
Cisco Systems

Email: mhartley@cisco.com

Fatai Zhang
Huawei Technologies

Email: zhangfatai@huawei.com
