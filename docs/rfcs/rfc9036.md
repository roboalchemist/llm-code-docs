---
rfc: 9036
title: "Registry Policy"
date: June 2021
category: Standards
updates: [5222]
---

# Abstract

This document changes the policy of the "Location-to-Service
Translation (LoST) Location Profiles" IANA registry established by
RFC 5222 from Standards Action to Specification Required.  This
allows standards development organizations (SDOs) other than the IETF
to add new values.

# Status of This Memo

This is an Internet Standards Track document.

This document is a product of the Internet Engineering Task Force
(IETF).  It represents the consensus of the IETF community.  It has
received public review and has been approved for publication by the
Internet Engineering Steering Group (IESG).  Further information on
Internet Standards is available in Section 2 of RFC 7841.

Information about the current status of this document, any errata,
and how to provide feedback on it may be obtained at
https://www.rfc-editor.org/info/rfc9036.

# Copyright Notice

Copyright (c) 2021 IETF Trust and the persons identified as the
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
  - [2.  Document Scope](#2-document-scope)
  - [3.  Security Considerations](#3-security-considerations)
  - [4.  IANA Considerations](#4-iana-considerations)
  - [5.  References](#5-references)
  - [5.1.  Normative References](#51-normative-references)
  - [5.2.  Informative References](#52-informative-references)
  - [Acknowledgements](#acknowledgements)
- [1.  Introduction](#1-introduction)

Standards Action.  This requires a Standards Track RFC for any new
registry values.  The National Emergency Number Association (NENA) is
a standards development organization (SDO) that makes significant use
of LoST in its emergency call specifications (e.g., [NENA-i3]) and
has identified a need for additional location profiles.  This
document changes the registry policy to Specification Required,
allowing other SDOs such as NENA to add values.

# 2. Document Scope

This document changes the policy of the "Location-to-Service
Translation (LoST) Location Profiles" IANA registry [reg] established
by [RFC5222] from Standards Action to Specification Required (as
defined in [RFC8126]).  This allows SDOs other than the IETF to add
new values.

# 3. Security Considerations

No new security considerations are identified by this change in
registry policy.

# 4. IANA Considerations

IANA has changed the policy of the "Location-to-Service Translation
(LoST) Location Profiles" registry (established by [RFC5222]) to
Specification Required.  IANA has also added this document as a
reference for the registry.  The Expert Reviewer is designated per
[RFC8126].  The reviewer should verify that:

*  the proposed new value is specified by the IETF, NENA, or a
similar SDO in which location profiles are in scope;

*  the proposed new value has a clear need (which includes there not
being an existing profile that meets the need); and

*  the profile specification is unambiguous and interoperable.

# 5. References

## 5.1. Normative References

[reg]      IANA, "Location-to-Service Translation (LoST) Location
Profiles",
<https://www.iana.org/assignments/lost-location-profiles>.

[RFC5222]  Hardie, T., Newton, A., Schulzrinne, H., and H.
Tschofenig, "LoST: A Location-to-Service Translation
Protocol", RFC 5222, DOI 10.17487/RFC5222, August 2008,
<https://www.rfc-editor.org/info/rfc5222>.

[RFC8126]  Cotton, M., Leiba, B., and T. Narten, "Guidelines for
Writing an IANA Considerations Section in RFCs", BCP 26,
RFC 8126, DOI 10.17487/RFC8126, June 2017,
<https://www.rfc-editor.org/info/rfc8126>.

## 5.2. Informative References

[NENA-i3]  National Emergency Number Association (NENA), "Detailed
Functional and Interface Standards for the NENA i3
Solution", NENA i3 Solution - Stage 3, NENA-STA-
010.2-2016, September 2016,
<https://www.nena.org/page/i3_Stage3>.

# Acknowledgements

Many thanks to Ted Hardie for his helpful review and suggestions and
to Guy Caron for his suggestion to clarify that "clear need" includes
there not being an existing profile.

# Author's Address

Randall Gellens
Core Technology Consulting
United States of America

Email: rg+ietf@coretechnologyconsulting.com
URI:   http://www.coretechnologyconsulting.com
