---
rfc: 6452
title: "The Unicode Code Points and"
date: November 2011
category: Standards
---

# Abstract

This memo documents IETF consensus for Internationalized Domain Names
for Applications (IDNA) derived character properties related to the
three code points, existing in Unicode 5.2, that changed property
values when version 6.0 was released.  The consensus is that no
update is needed to RFC 5892 based on the changes made in Unicode
6.0.

# Status of This Memo

This is an Internet Standards Track document.

This document is a product of the Internet Engineering Task Force
(IETF).  It represents the consensus of the IETF community.  It has
received public review and has been approved for publication by the
Internet Engineering Steering Group (IESG).  Further information on
Internet Standards is available in Section 2 of RFC 5741.

Information about the current status of this document, any errata,
and how to provide feedback on it may be obtained at
http://www.rfc-editor.org/info/rfc6452.

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
    - [1.1. U+0CF1 KANNADA SIGN JIHVAMULIYA](#11-u0cf1-kannada-sign-jihvamuliya)
    - [1.2. U+0CF2 KANNADA SIGN UPADHMANIYA](#12-u0cf2-kannada-sign-upadhmaniya)
    - [1.3. U+19DA NEW TAI LUE THAM DIGIT ONE](#13-u19da-new-tai-lue-tham-digit-one)
  - [2. IETF Consensus](#2-ietf-consensus)
  - [3. IANA Considerations](#3-iana-considerations)
  - [4. Security Considerations](#4-security-considerations)
  - [5. Acknowledgements](#5-acknowledgements)
  - [6. Normative References](#6-normative-references)

# 1. Introduction

RFC 5892 [RFC5892] specifies an algorithm that was defined when
version 5.0 (later updated to version 5.2) [Unicode5.2] was the
current version of Unicode, and it also defines a derived property
value based on that algorithm.  Unicode 6.0 [Unicode6] has changed
GeneralCategory of three code points that were allocated in
Unicode 5.2 or earlier.  This implies that the derived property value
differs depending on whether the property definitions used are from
Unicode 5.2 or 6.0.  These are non-backward-compatible changes as
described in Section 5.1 of RFC 5892.

The three code points are:

## 1.1. U+0CF1 KANNADA SIGN JIHVAMULIYA

The GeneralCategory for this character changes from So to Lo.  This
implies that the derived property value changes from DISALLOWED to
PVALID.

## 1.2. U+0CF2 KANNADA SIGN UPADHMANIYA

The GeneralCategory for this character changes from So to Lo.  This
implies that the derived property value changes from DISALLOWED to
PVALID.

## 1.3. U+19DA NEW TAI LUE THAM DIGIT ONE

The GeneralCategory for this character changes from Nd to No.  This
implies that the derived property value changes from PVALID to
DISALLOWED.

# 2. IETF Consensus

No change to RFC 5892 is needed based on the changes made in
Unicode 6.0.

This consensus does not imply that no changes will be made to
RFC 5892 for all future updates of The Unicode Standard.

This RFC has been produced because 6.0 is the first version of
Unicode to be released since IDNA2008 was published.

# 3. IANA Considerations

IANA has updated the derived property value registry according to
RFC 5892 and the property values defined in The Unicode Standard
version 6.0.

# 4. Security Considerations

When the algorithm presented in RFC 5892 is applied using the
property definitions of Unicode Standard version 6.0, the result will
be different from when it is applied using the property definitions
of Unicode 5.2 for the three code points discussed in this document.
The three code points are unlikely to occur in internationalized
domain names, however, so the security implications of the changes
are minor.

# 5. Acknowledgements

The main contributors are (in alphabetical order) Eric Brunner-
Williams, Vint Cerf, Tina Dam, Mark Davis, Martin Duerst, John
Klensin, Pete Resnick, Markus Scherer, Andrew Sullivan, Kenneth
Whistler, and Nicholas Williams.

Not all contributors believe that the solution for the issues
discussed in this document is optimal.

# 6. Normative References

[RFC5892]     Faltstrom, P., Ed., "The Unicode Code Points and
Internationalized Domain Names for Applications
(IDNA)", RFC 5892, August 2010.

```
   [Unicode5.2]  The Unicode Consortium, "The Unicode Standard,
```

Version 5.2.0", Unicode 5.0.0, Boston, MA,
Addison-Wesley ISBN 0-321-48091-0, as amended
by Unicode 5.2.0, October 2009,
<http://www.unicode.org/versions/Unicode5.2.0/>.

[Unicode6]    The Unicode Consortium, "The Unicode Standard,
Version 6.0.0", October 2010,
<http://www.unicode.org/versions/Unicode6.0.0/>.

# Authors' Addresses

Patrik Faltstrom (editor)
Cisco

EMail: paf@cisco.com

Paul Hoffman (editor)
VPN Consortium

EMail: paul.hoffman@vpnc.org
