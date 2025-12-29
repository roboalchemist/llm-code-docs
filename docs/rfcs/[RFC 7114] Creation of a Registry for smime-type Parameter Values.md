---
rfc: 7114
title: "Creation of a Registry for smime-type Parameter Values"
date: January 2014
category: Standards
---

# Abstract

Secure/Multipurpose Internet Mail Extensions (S/MIME) defined the
Content-Type parameter "smime-type".  As the list of defined values
for that parameter has increased, it has become clear that a registry
is needed to document these values.  This document creates the
registry, registers the current values, and specifies the policies
for registration of new values.

# Status of This Memo

This is an Internet Standards Track document.

This document is a product of the Internet Engineering Task Force
(IETF).  It represents the consensus of the IETF community.  It has
received public review and has been approved for publication by the
Internet Engineering Steering Group (IESG).  Further information on
Internet Standards is available in Section 2 of RFC 5741.

Information about the current status of this document, any errata,
and how to provide feedback on it may be obtained at
http://www.rfc-editor.org/info/rfc7114.

# Copyright Notice

Copyright (c) 2014 IETF Trust and the persons identified as the
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
  - [2.  IANA Considerations](#2-iana-considerations)
  - [3.  Security Considerations](#3-security-considerations)
  - [4.  References](#4-references)
  - [4.1.  Normative References](#41-normative-references)
  - [4.2.  Informative References](#42-informative-references)

# 1. Introduction

Secure/Multipurpose Internet Mail Extensions (S/MIME) defined the
Content-Type "application/pkcs7-mime" and the parameter "smime-type",
along with four valid values for the parameter [RFC3851].
Certificate Management over CMS (CMC) added two new parameter values
[RFC5273].  [RFC5751] replaced RFC 3851 and registered the
application/pkcs7-mime media type, but did not create a registry for
the smime-type values.

Enhanced Security Services for S/MIME [RFC2634] and Securing X.400
Content with S/MIME [RFC3854] also add smime-type values.

When Enrollment over Secure Transport [RFC7030] added another
parameter value, it became clear that a registry for smime-type
parameter values is necessary.  Section 2 creates this registry,
registers the current values that are defined in previously published
documents, and specifies the policies for registration of new values.

# 2. IANA Considerations

IANA has changed the reference field for the media type application/
pkcs7-mime to refer to [RFC5751] and this document.  This document
replaces the references to RFC 5273 and RFC 7030, which are no longer
needed.

IANA has created a new sub-registry under the "MIME Media Type Sub-
Parameter Registries" top-level registry.  The new registry is
"Parameter Values for the smime-type Parameter", and it references
this document and [RFC5751].  The initial values for the registry are
as follows:

+----------------------+-----------------------------------+
|  smime-type value    |  Reference                        |
+----------------------+-----------------------------------+
| certs-only           | [RFC5751], Section 3.2.2          |
| CMC-Request          | [RFC5273], Section 3              |
| CMC-Response         | [RFC5273], Section 3              |
| compressed-data      | [RFC5751], Section 3.2.2          |
| enveloped-data       | [RFC5751], Section 3.2.2          |
| enveloped-x400       | [RFC3854], Section 3.3.1          |
| server-generated-key | [RFC7030], Section 4.4.2          |
| signed-data          | [RFC5751], Section 3.2.2          |
| signed-receipt       | [RFC2634], Section 2.4, bullet 10 |
| signed-x400          | [RFC3854], Section 3.2.1          |
+----------------------+-----------------------------------+

New values can be registered using the Specification Required policy,
as defined in [RFC5226].  The S/MIME Message Specification [RFC5751],
Section 3.2.2, specifies guidelines for assigning new smime-type
parameter values, and those guidelines apply to the assignment of
values in this registry.

# 3. Security Considerations

This document is purely administrative and presents no security
issues.

# 4. References

## 4.1. Normative References

[RFC5226]  Narten, T. and H. Alvestrand, "Guidelines for Writing an
IANA Considerations Section in RFCs", BCP 26, RFC 5226,
May 2008.

[RFC5751]  Ramsdell, B. and S. Turner, "Secure/Multipurpose Internet
Mail Extensions (S/MIME) Version 3.2 Message
Specification", RFC 5751, January 2010.

## 4.2. Informative References

[RFC2634]  Hoffman, P., "Enhanced Security Services for S/MIME", RFC
2634, June 1999.

[RFC3851]  Ramsdell, B., "Secure/Multipurpose Internet Mail
Extensions (S/MIME) Version 3.1 Message Specification",
RFC 3851, July 2004.

[RFC3854]  Hoffman, P., Bonatti, C., and A. Eggen, "Securing X.400
Content with Secure/Multipurpose Internet Mail Extensions
(S/MIME)", RFC 3854, July 2004.

[RFC5273]  Schaad, J. and M. Myers, "Certificate Management over CMS
(CMC): Transport Protocols", RFC 5273, June 2008.

[RFC7030]  Pritikin, M., Yee, P., and D. Harkins, "Enrollment over
Secure Transport", RFC 7030, October 2013.

# Author's Address

Barry Leiba
Huawei Technologies

Phone: +1 646 827 0648
EMail: barryleiba@computer.org
URI:   http://internetmessagingtechnology.org/
