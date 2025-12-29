---
rfc: 5279
title: "A Uniform Resource Name (URN) Namespace"
date: July 2008
category: Informational
---

# Abstract

This document describes the Namespace Identifier (NID) for Uniform
Resource Namespace (URN) resources published by the 3rd Generation
Partnership Project (3GPP). 3GPP defines and manages resources that
utilize this URN name model.  Management activities for these and
other resource types are provided by the 3GPP Support Team.

# Table of Contents

  - [1.  Introduction](#1-introduction)
  - [2.  URN Specification for the 3GPP Namespace Identifier (NID)](#2-urn-specification-for-the-3gpp-namespace-identifier-nid)
  - [3.  Examples](#3-examples)
  - [4.  Namespace Considerations](#4-namespace-considerations)
  - [5.  Community Considerations](#5-community-considerations)
  - [6.  Security Considerations](#6-security-considerations)
  - [7.  IANA Considerations](#7-iana-considerations)
  - [8.  Normative References](#8-normative-references)

2.  Registration of values or sub-trees to other entities

3.  Name models for use in experimental purposes

New Namespace Identifier (NID) labels

The Entries in the registration table will be the following:

3gpp-urn:    the registered value;
Description: description of the registered value;
Reference:   3GPP spec that defines the value;
Contact:     person requesting the URN assignment.

Process for identifier resolution:

The namespace is not listed with a Resolution Discovery System
(RDS), as this is not relevant.

Rules for Lexical Equivalence:

No special considerations; the rules for lexical equivalence of
RFC 2141 [RFC2141] apply.

Conformance with URN Syntax:

No special considerations.

Validation mechanism:

None specified.  URN assignment will be handled by procedures
supported and maintained by 3GPP.

Scope:

Global

# 3. Examples

The following examples are representative URNs that could be assigned
by 3GPP.  They are not actual strings that are assigned.

urn:3gpp:featurephones

Defines the "3gpp-urn" to be used for "featurephones".

urn:3gpp:acme.foo-serv

Defines the URN associated with the operator identified by the
"3gpp-urn" value "acme", which has decided to register and provide
information about its service identified by value "foo-serv".

# 4. Namespace Considerations

The 3rd Generation Partnership Project is developing a variety of
enablers and applications.  Some of these require information to be
fully specified.

For proper operation, descriptions of the needed information must
exist for the URNs and be available in a unique, reliable, and
persistent manner.

As 3GPP is ongoing and covers many technical areas, the possibility
of binding to various other namespace repositories has been deemed
impractical.  Each object or description, as defined in 3GPP, could
possibly be related to multiple different other namespaces, so
further conflicts of association could occur.  Thus, the intent is to
utilize the 3GPP specifications manager as the naming authority for
3GPP-defined URNs and its descriptions.

# 5. Community Considerations

The objects and descriptions required for enablers produced by 3GPP
are generally available for use by other organizations.  The 3rd
Generation Partnership Project Support Office will provide access and
support for name requests by these organizations.  This support can
be enabled in a timely and responsive fashion as new objects and
descriptions are produced.

# 6. Security Considerations

There are no security considerations other than those normally
associated with the use and resolution of URNs in general.

# 7. IANA Considerations

This section registers a new URN NID with the registration provided
in Section 2.

"3gpp-urn" strings are identified by label managed by 3GPP.  Thus,
creating a new label does not require any IANA action.

# 8. Normative References

[RFC3406]  Daigle, L., van Gulik, D., Iannella, R., and P. Faltstrom,
"Uniform Resource Names (URN) Namespace Definition
Mechanisms", BCP 66, RFC 3406, October 2002.

[RFC2141]  Moats, R., "URN Syntax", RFC 2141, May 1997.

# Authors' Addresses

Atle Monrad
Ericsson
Televeien 1
Grimstad  4898
Norway

EMail: atle.monrad@ericsson.com

Salvatore Loreto
Ericsson
Hirsalantie 11
Jorvas  02420
Finland

EMail: Salvatore.Loreto@ericsson.com

Full Copyright Statement

Copyright (C) The IETF Trust (2008).

This document is subject to the rights, licenses and restrictions
contained in BCP 78, and except as set forth therein, the authors
retain all their rights.

This document and the information contained herein are provided on an
"AS IS" basis and THE CONTRIBUTOR, THE ORGANIZATION HE/SHE REPRESENTS
OR IS SPONSORED BY (IF ANY), THE INTERNET SOCIETY, THE IETF TRUST AND
THE INTERNET ENGINEERING TASK FORCE DISCLAIM ALL WARRANTIES, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO ANY WARRANTY THAT THE USE OF
THE INFORMATION HEREIN WILL NOT INFRINGE ANY RIGHTS OR ANY IMPLIED
WARRANTIES OF MERCHANTABILITY OR FITNESS FOR A PARTICULAR PURPOSE.

Intellectual Property

The IETF takes no position regarding the validity or scope of any
Intellectual Property Rights or other rights that might be claimed to
pertain to the implementation or use of the technology described in
this document or the extent to which any license under such rights
might or might not be available; nor does it represent that it has
made any independent effort to identify any such rights.  Information
on the procedures with respect to rights in RFC documents can be
found in BCP 78 and BCP 79.

Copies of IPR disclosures made to the IETF Secretariat and any
assurances of licenses to be made available, or the result of an
attempt made to obtain a general license or permission for the use of
such proprietary rights by implementers or users of this
specification can be obtained from the IETF on-line IPR repository at
http://www.ietf.org/ipr.

The IETF invites any interested party to bring to its attention any
copyrights, patents or patent applications, or other proprietary
rights that may cover technology that may be required to implement
this standard.  Please address the information to the IETF at
ietf-ipr@ietf.org.
