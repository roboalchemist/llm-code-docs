---
rfc: 8067
title: "Updating When Standards Track Documents May Refer Normatively to"
date: January 2017
category: Best
updates: [3967]
---

# Abstract

RFC 3967 specifies a process for allowing normative references to
documents at lower maturity levels ("downrefs"), which involves
calling out the downref explicitly in the Last Call notice.  That
requirement has proven to be unnecessarily strict, and this document
updates RFC 3967, allowing the IESG more flexibility in accepting
downrefs in Standards Track documents.

# Status of This Memo

This memo documents an Internet Best Current Practice.

This document is a product of the Internet Engineering Task Force
(IETF).  It has been approved for publication by the Internet
Engineering Steering Group (IESG).  Further information on BCPs is
available in Section 2 of RFC 7841.

Information about the current status of this document, any errata,
and how to provide feedback on it may be obtained at
http://www.rfc-editor.org/info/rfc8067.

# Copyright Notice

Copyright (c) 2017 IETF Trust and the persons identified as the
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

  - [1.  Introduction](#1-introduction)
  - [2.  The IESG's Responsibility with Respect to Downrefs](#2-the-iesgs-responsibility-with-respect-to-downrefs)
  - [3.  Security Considerations](#3-security-considerations)
  - [4.  Normative References](#4-normative-references)
  - [Author's Address](#authors-address)

Call, with the corresponding delay and with no real benefit.

# 2. The IESG's Responsibility with Respect to Downrefs

The process in RFC 3967 is hereby updated to specify that explicitly
documenting the downward references in the Last Call message is
strongly recommended but not required.  The responsible AD should
still check for downrefs before sending out the Last Call notice, but
if an undetected downref is noticed during Last Call or IESG review,
any need to repeat the Last Call is at the discretion of the IESG.
However, the process in RFC 3967 is not fundamentally altered: If the
IESG decides not to repeat the Last Call, the status of the affected
downrefs is not changed, and the process in RFC 3967 will still apply
if those downrefs are used in the future.

This gives the IESG the responsibility to determine the actual
maturity level of the downward reference with respect to the document
at hand, and to decide whether or not it is necessary to explicitly
ask the IETF community for comments on the downref on a case-by-case
basis.  In making that decision, the IESG should take into account
the general discussion in RFC 3967.  The responsible AD should make
sure that the omission is recorded as a comment in the datatracker.

# 3. Security Considerations

Referencing immature protocols can have security and stability
implications, and the IESG should take that into account when
deciding whether re-consulting the community is useful.

# 4. Normative References

[RFC3967]  Bush, R. and T. Narten, "Clarifying when Standards Track
Documents may Refer Normatively to Documents at a Lower
Level", BCP 97, RFC 3967, DOI 10.17487/RFC3967, December
2004, <http://www.rfc-editor.org/info/rfc3967>.

# Author's Address

Barry Leiba
Huawei Technologies

Phone: +1 646 827 0648
Email: barryleiba@computer.org
URI:   http://internetmessagingtechnology.org/
