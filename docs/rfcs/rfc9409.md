---
rfc: 9409
title: "The 'sip-trunking-capability' Link Relation Type"
date: July 2023
category: Informational
---

# Abstract

This Informational document defines the 'sip-trunking-capability'
link relation type that may be used by an enterprise telephony
Session Initiation Protocol (SIP) network to retrieve a SIP trunking
capability set document, which contains the capabilities and
configuration requirements of an Internet Telephony Service Provider
(ITSP).  These technical requirements allow for seamless peering
between SIP-based enterprise telephony networks and the ITSP.

# Status of This Memo

This document is not an Internet Standards Track specification; it is
published for informational purposes.

This document is a product of the Internet Engineering Task Force
(IETF).  It represents the consensus of the IETF community.  It has
received public review and has been approved for publication by the
Internet Engineering Steering Group (IESG).  Not all documents
approved by the IESG are candidates for any level of Internet
Standard; see Section 2 of RFC 7841.

Information about the current status of this document, any errata,
and how to provide feedback on it may be obtained at
https://www.rfc-editor.org/info/rfc9409.

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
  - [2.  The 'sip-trunking-capability' Link Relation Type](#2-the-sip-trunking-capability-link-relation-type)
  - [3.  Example Usage](#3-example-usage)
  - [4.  IANA Considerations](#4-iana-considerations)
  - [5.  Security Considerations](#5-security-considerations)
  - [6.  References](#6-references)
  - [6.1.  Normative References](#61-normative-references)
  - [6.2.  Informative References](#62-informative-references)
  - [Acknowledgements](#acknowledgements)
- [1.  Introduction](#1-introduction)
- [2.  The 'sip-trunking-capability' Link Relation Type](#2-the-sip-trunking-capability-link-relation-type)
- [3.  Example Usage](#3-example-usage)

The ITSP may use an authentication framework such as OAuth 2.0
[RFC6749] to determine the identity of the enterprise telephony
network to provide the appropriate capability set document.

# 4. IANA Considerations

IANA has registered the 'sip-trunking-capability' link relation under
the "Link Relation Types" registry as follows:

Relation Name:  sip-trunking-capability

Description:  Refers to a capability set document that defines
parameters or configuration requirements for automated peering and
communication-channel negotiation of the Session Initiation
Protocol (SIP).

Reference:  RFC 9409

# 5. Security Considerations

The 'sip-trunking-capability' relation type is not known to introduce
any new security issues not already discussed in RFC 8288 for generic
use of web-linking mechanisms.  However, it is recommended to
exercise caution when publishing potentially sensitive capability
information over unencrypted or unauthenticated channels.  Additional
security recommendations are outlined in the capability set document
definition.  See the Security Considerations section in "Automatic
Peering for SIP Trunks" [SIP-AUTO-PEER].

# 6. References

## 6.1. Normative References

[RFC8288]  Nottingham, M., "Web Linking", RFC 8288,
DOI 10.17487/RFC8288, October 2017,
<https://www.rfc-editor.org/info/rfc8288>.

## 6.2. Informative References

[RFC3261]  Rosenberg, J., Schulzrinne, H., Camarillo, G., Johnston,
A., Peterson, J., Sparks, R., Handley, M., and E.
Schooler, "SIP: Session Initiation Protocol", RFC 3261,
DOI 10.17487/RFC3261, June 2002,
<https://www.rfc-editor.org/info/rfc3261>.

[RFC3986]  Berners-Lee, T., Fielding, R., and L. Masinter, "Uniform
Resource Identifier (URI): Generic Syntax", STD 66,
RFC 3986, DOI 10.17487/RFC3986, January 2005,
<https://www.rfc-editor.org/info/rfc3986>.

[RFC6749]  Hardt, D., Ed., "The OAuth 2.0 Authorization Framework",
RFC 6749, DOI 10.17487/RFC6749, October 2012,
<https://www.rfc-editor.org/info/rfc6749>.

[RFC7033]  Jones, P., Salgueiro, G., Jones, M., and J. Smarr,
"WebFinger", RFC 7033, DOI 10.17487/RFC7033, September
2013, <https://www.rfc-editor.org/info/rfc7033>.

[SIP-AUTO-PEER]
Inamdar, K., Narayanan, S., and C. F. Jennings, "Automatic
Peering for SIP Trunks", Work in Progress, Internet-Draft,
draft-ietf-asap-sip-auto-peer-07, 13 January 2023,
<https://datatracker.ietf.org/doc/html/draft-ietf-asap-
sip-auto-peer-07>.

# Acknowledgements

This document resulted from the discussions in the ASAP Working
Group, especially the detailed and thoughtful comments of Paul Jones,
Marc Petit-Huguenin, Mark Nottingham, Cullen Jennings, Jonathan
Rosenberg, Jon Peterson, Chris Wendt, Jean Mahoney, and Murray
Kucherawy.  Additional thanks to Joe Clarke, Tim Bray, Christopher
Wood, Dan Romascanu, David Dong, Éric Vyncke, Robert Wilton, and Lars
Eggert for their reviews and feedback.

# Authors' Addresses

Kaustubh Inamdar
Unaffiliated
Email: kaustubh.ietf@gmail.com

Sreekanth Narayanan
Cisco
Email: sreenara@cisco.com

Derek Engi
Cisco
Ann Arbor, MI
United States of America
Phone: +1 919 392 7966
Email: deengi@cisco.com

Gonzalo Salgueiro
Cisco
7200-12 Kit Creek Rd.
Research Triangle Park, NC 27709
United States of America
Phone: +1 919 392 3266
Email: gsalguei@cisco.com
