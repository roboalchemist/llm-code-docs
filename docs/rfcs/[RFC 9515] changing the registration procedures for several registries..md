---
rfc: 9515
title: "changing the registration procedures for several registries."
date: December 2023
category: Standards
updates: [7854]
---

# Abstract

This document updates RFC 7854, "BGP Monitoring Protocol (BMP)", by
changing the registration procedures for several registries.
Specifically, any BMP registry with a range of 32768-65530 designated
"Specification Required" has that range redesignated as "First Come
First Served".

# Status of This Memo

This is an Internet Standards Track document.

This document is a product of the Internet Engineering Task Force
(IETF).  It represents the consensus of the IETF community.  It has
received public review and has been approved for publication by the
Internet Engineering Steering Group (IESG).  Further information on
Internet Standards is available in Section 2 of RFC 7841.

Information about the current status of this document, any errata,
and how to provide feedback on it may be obtained at
https://www.rfc-editor.org/info/rfc9515.

# Copyright Notice

Copyright (c) 2023 IETF Trust and the persons identified as the
document authors.  All rights reserved.

This document is subject to BCP 78 and the IETF Trust's Legal
Provisions Relating to IETF Documents
(https://trustee.ietf.org/license-info) in effect on the date of
publication of this document.  Please review these documents
carefully, as they describe your rights and restrictions with respect
to this document.  Code Components extracted from this document must
include Revised BSD License text as described in Section 4.e of the
Trust Legal Provisions and are provided without warranty as described
in the Revised BSD License.

# Table of Contents

  - [1.  Introduction](#1-introduction)
  - [2.  IANA Considerations](#2-iana-considerations)
  - [3.  Security Considerations](#3-security-considerations)
  - [4.  Normative References](#4-normative-references)
  - [Acknowledgements](#acknowledgements)
- [1.  Introduction](#1-introduction)

Accordingly, this document revises the registration procedures, as
given in Section 2.

# 2. IANA Considerations

IANA has revised the following registries within the BMP group:

*  BMP Statistics Types
*  BMP Initiation and Peer Up Information TLVs
*  BMP Termination Message TLVs
*  BMP Termination Message Reason Codes
*  BMP Route Mirroring TLVs
*  BMP Route Mirroring Information Codes

For each of these registries, the ranges 32768-65530 whose
registration procedures were "Specification Required" are revised to
have the registration procedures "First Come First Served".

# 3. Security Considerations

This revision to registration procedures does not change the
underlying security issues inherent in [RFC7854].

# 4. Normative References

[RFC7854]  Scudder, J., Ed., Fernando, R., and S. Stuart, "BGP
Monitoring Protocol (BMP)", RFC 7854,
DOI 10.17487/RFC7854, June 2016,
<https://www.rfc-editor.org/info/rfc7854>.

[RFC8126]  Cotton, M., Leiba, B., and T. Narten, "Guidelines for
Writing an IANA Considerations Section in RFCs", BCP 26,
RFC 8126, DOI 10.17487/RFC8126, June 2017,
<https://www.rfc-editor.org/info/rfc8126>.

# Acknowledgements

Thanks to Jeff Haas for review and encouragement, and to Tom Petch
for review.

# Author's Address

John Scudder
Juniper Networks
1194 N. Mathilda Ave
Sunnyvale, CA 94089
United States of America
Email: jgs@juniper.net
