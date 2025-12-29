---
rfc: 7892
title: "Huawei Technologies"
date: May 2016
category: Standards
updates: [7139]
---

# Abstract

IANA defined the "OTN Signal Type" subregistry of the "Generalized
Multi-Protocol Label Switching (GMPLS) Signaling Parameters" registry
in RFC 7139.  This document updates the "OTN Signal Type" subregistry
to allow registration via Specification Required.

# Status of This Memo

This is an Internet Standards Track document.

This document is a product of the Internet Engineering Task Force
(IETF).  It represents the consensus of the IETF community.  It has
received public review and has been approved for publication by the
Internet Engineering Steering Group (IESG).  Further information on
Internet Standards is available in Section 2 of RFC 7841.

Information about the current status of this document, any errata,
and how to provide feedback on it may be obtained at
http://www.rfc-editor.org/info/rfc7892.

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
  - [2. Security Considerations](#2-security-considerations)
  - [3. IANA Considerations](#3-iana-considerations)
  - [4. References](#4-references)
    - [4.1. Normative References](#41-normative-references)
    - [4.2. Informative References](#42-informative-references)
  - [Acknowledgments](#acknowledgments)
  - [Authors' Addresses](#authors-addresses)

# 1. Introduction

IANA maintains "OTN Signal Type" subregistry of the "Generalized
Multi-Protocol Label Switching (GMPLS) Signaling Parameters" registry
for OTN signal types (as defined in [RFC4328] and updated by
[RFC7139]).  This subregistry is defined to use only the Standards
Action registration policy as defined by [RFC5226].  This document
updates [RFC7139] to allow the "OTN Signal Type" subregistry to also
use the Specification Required policy as defined in [RFC5226].

# 2. Security Considerations

This document does not introduce any new security considerations to
the existing GMPLS signaling protocols.  Refer to [RFC7139] for
further details of the specific security measures.  Additionally,
[RFC5920] provides an overview of security vulnerabilities and
protection mechanisms for the GMPLS control plane.

# 3. IANA Considerations

IANA maintains the "OTN Signal Type" subregistry of the "Generalized
Multi-Protocol Label Switching (GMPLS) Signaling Parameters"
registry.  The registry currently is defined to use the Standards
Action registration policy as defined by [RFC5226].

Per this document, IANA has updated the registration policies for the
"OTN Signal Type" subregistry to be "Standards Action" for Standards
Track documents and "Specification Required" for other documents.

# 4. References

## 4.1. Normative References

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

[RFC5226]  Narten, T. and H. Alvestrand, "Guidelines for Writing an
IANA Considerations Section in RFCs", BCP 26, RFC 5226,
DOI 10.17487/RFC5226, May 2008,
<http://www.rfc-editor.org/info/rfc5226>.

## 4.2. Informative References

[RFC5920]  Fang, L., Ed., "Security Framework for MPLS and GMPLS
Networks", RFC 5920, DOI 10.17487/RFC5920, July 2010,
<http://www.rfc-editor.org/info/rfc5920>.

# Acknowledgments

The authors would like to thank Lou Berger, Deborah Brungard, Daniele
Ceccarelli, Adrian Farrel, Vijay Gurbani, Huub van Helvoort, Barry
Leiba, and Robert Sparks for comments.

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
