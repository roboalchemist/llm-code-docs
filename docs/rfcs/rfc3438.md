---
rfc: 3438
title: "Layer Two Tunneling Protocol (L2TP)"
date: December 2002
category: Best
---

# Abstract

This document describes updates to the Internet Assigned Numbers
Authority (IANA) considerations for the Layer Two Tunneling Protocol
(L2TP).

# Table of Contents

  - [1. Introduction](#1-introduction)
  - [1.1 Terminology](#11-terminology)
  - [2. IANA Considerations](#2-iana-considerations)
  - [2.1 Control Message AVPs](#21-control-message-avps)
  - [2.2 Message Type AVP Values](#22-message-type-avp-values)
  - [2.3 Result Code AVP Values](#23-result-code-avp-values)
  - [2.4 Remaining Values](#24-remaining-values)
  - [3. Normative References](#3-normative-references)
  - [4. Security Considerations](#4-security-considerations)
  - [5. Acknowledgements](#5-acknowledgements)
  - [6. Author's Address](#6-authors-address)
  - [7. Full Copyright Statement](#7-full-copyright-statement)

# 1. Introduction

This document provides guidance to the Internet Assigned Numbers
Authority (IANA) regarding the registration of values related to the
Layer Two Tunneling Protocol (L2TP), defined in [RFC2661], in
accordance with BCP 26, [RFC2434].

## 1.1. Terminology

The following terms are used here with the meanings defined in
BCP 26:  "name space", "assigned value", "registration".

The following policies are used here with the meanings defined in
BCP 26: "Private Use", "First Come First Served", "Expert Review",
"Specification Required", "IETF Consensus", "Standards Action".

# 2. IANA Considerations

L2TP [RFC2661] defines a number of "magic" numbers to be maintained
by the IANA.  This section updates the criteria to be used by the
IANA to assign additional numbers in each of these lists.

Each of the values identified in this document that require a
registration criteria update are currently maintained by IANA and
have a range of values from 0 to 65 535, of which a very small number
have been allocated (the maximum number allocated within any one
range is 46) [L2TP-IANA].  Given the nature of these values, it is
not expected that any will ever run into a resource allocation
problem if registration allocation requirements are relaxed from
their current state.

The recommended criteria changes for IANA registration are listed in
the following sections.  In one case, the registration criteria is
currently defined as First Come First Served and should be made more
strict, others are defined as IETF Consensus and need to be relaxed.
The relaxation from IETF Consensus is motivated by specific cases in
which values that were never intended to be vendor-specific have had
to enter early field trials or be released in generally available
products with vendor-specific values while awaiting documents to be
formalized.  In most cases, this results in products that have to
support both the vendor-specific value and IETF value indefinitely.

For registration requests where a Designated Expert should be
consulted, the responsible IESG Area Director should appoint the
Designated Expert.

For registration requests requiring Expert Review, the Designated
Expert should consult relevant WGs as appropriate (e.g., the l2tpext
WG at the time of this writing).

The basic guideline for the Expert Review process will be to approve
the assignment of a value only if there is a document being advanced
that clearly defines the values to be assigned, and there is active

implementation development (perhaps entering early field or
interoperability trails, requiring assigned values to proceed without
having to resort to a chosen vendor-specific method).

## 2.1. Control Message AVPs

IANA manages the "Control Message Attribute Value Pairs" [L2TP-IANA]
name space, of which 0 - 46 have been assigned.  The criteria for
assignment was originally IETF Consensus.  Further values should be
assigned upon Expert Review.

## 2.2. Message Type AVP Values

IANA manages the "Message Type AVP (Attribute Type 0) Values" [L2TP-
IANA] name space, of which 0 - 16 have been assigned.  The criteria
for assignment was originally IETF Consensus.  Further values should
be assigned upon Expert Review.

## 2.3. Result Code AVP Values

IANA maintains a list of "Result Code values for the StopCCN
message," "Result Code values for the CDN message," and "General
Error Codes" [L2TP-IANA].  The criteria for Error Code assignment was
originally First Come First Served, and the criteria for CDN and
StopCCN Result Codes were originally IETF Consensus.  Further values
for all Result and Error codes should be assigned upon Expert Review.

## 2.4. Remaining Values

All criteria for L2TP values maintained by IANA and not mentioned
specifically in this document remain unchanged.

# 3. Normative References

[RFC2119]   Bradner, S., "Key words for use in RFCs to Indicate
Requirement Levels", BCP 14, RFC 2119, March 1997.

[RFC2434]   Alvestrand, H. and T. Narten, "Guidelines for Writing an
IANA Considerations Section in RFCs", BCP 26, RFC 2434,
October 1998.

[RFC2661]   Townsley, W., Valencia, A., Rubens, A., Pall, G., Zorn,
G. and B. Palter, "Layer Two Tunneling Layer Two
Tunneling Protocol (L2TP)", RFC 2661, August 1999.

[L2TP-IANA] Internet Assigned Numbers Authority (IANA), "Layer Two
Tunneling Protocol 'L2TP' - RFC 2661",
http://www.iana.org/assignments/l2tp-parameters

# 4. Security Considerations

This focuses on IANA considerations, and does not have security
considerations.

# 5. Acknowledgements

Some of this text and much of the format of this document was taken
from an internet document on EAP IANA Considerations authored by
Bernard Aboba.

# 6. Author's Address

W. Mark Townsley
Cisco Systems
7025 Kit Creek Road
PO Box 14987
Research Triangle Park, NC 27709

EMail: mark@townsley.net

# 7. Full Copyright Statement

Copyright (C) The Internet Society (2002).  All Rights Reserved.

This document and translations of it may be copied and furnished to
others, and derivative works that comment on or otherwise explain it
or assist in its implementation may be prepared, copied, published
and distributed, in whole or in part, without restriction of any
kind, provided that the above copyright notice and this paragraph are
included on all such copies and derivative works.  However, this
document itself may not be modified in any way, such as by removing
the copyright notice or references to the Internet Society or other
Internet organizations, except as needed for the purpose of
developing Internet standards in which case the procedures for
copyrights defined in the Internet Standards process must be
followed, or as required to translate it into languages other than
English.

The limited permissions granted above are perpetual and will not be
revoked by the Internet Society or its successors or assigns.

This document and the information contained herein is provided on an
"AS IS" basis and THE INTERNET SOCIETY AND THE INTERNET ENGINEERING
TASK FORCE DISCLAIMS ALL WARRANTIES, EXPRESS OR IMPLIED, INCLUDING
BUT NOT LIMITED TO ANY WARRANTY THAT THE USE OF THE INFORMATION
HEREIN WILL NOT INFRINGE ANY RIGHTS OR ANY IMPLIED WARRANTIES OF
MERCHANTABILITY OR FITNESS FOR A PARTICULAR PURPOSE.

Acknowledgement

Funding for the RFC Editor function is currently provided by the
Internet Society.
