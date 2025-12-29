---
rfc: 3969
title: "The Internet Assigned Number Authority (IANA)"
date: December 2004
category: Best
updates: [3427]
---

# Abstract

This document creates an Internet Assigned Number Authority (IANA)
registry for the Session Initiation Protocol (SIP) and SIPS Uniform
Resource Identifier (URI) parameters, and their values.  It also
lists the already existing parameters to be used as initial values
for that registry.

# Table of Contents

  - [1.  Introduction](#1-introduction)
  - [2.  Terminology](#2-terminology)
  - [3.  Use of the Registry](#3-use-of-the-registry)
  - [4.  IANA Considerations](#4-iana-considerations)
    - [4.1.  SIP and SIPS URI Parameters Sub-Registry](#41-sip-and-sips-uri-parameters-sub-registry)
    - [4.2.  Registration Policy for SIP and SIPS URI Parameters](#42-registration-policy-for-sip-and-sips-uri-parameters)
  - [5.  Security Considerations](#5-security-considerations)
  - [6.  Acknowledgements](#6-acknowledgements)
  - [7.  Normative References](#7-normative-references)
    - [Author's Address](#authors-address)
    - [Full Copyright Statement](#full-copyright-statement)

# 1. Introduction

RFC 3261 [1] allows new SIP URI and SIPS URI parameters, and new
parameter values to be defined.  However, RFC 3261 omitted an IANA
registry for them.  This document creates such a registry.

RFC 3427 [2] documents the process to extend SIP.  This document
updates RFC 3427 by specifying how to define and register new SIP and
SIP URI parameters and their values.

# 2. Terminology

In this document, the key words "MUST", "MUST NOT", "REQUIRED",
"SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY",
and "OPTIONAL" are to be interpreted as described in BCP 14, RFC 2119
[3] and indicate requirement levels for compliant SIP
implementations.

# 3. Use of the Registry

SIP and SIPS URI parameters and values for these parameters MUST be
documented in a standards-track RFC in order to be registered by
IANA.  This documentation MUST fully explain the syntax, intended
usage, and semantics of the parameter.  The intent of this
requirement is to assure interoperability between independent
implementations, and to prevent accidental namespace collisions
between implementations of dissimilar features.

Note that this registry, unlike other protocol registries, only
deals with parameters and parameter values defined in RFCs (i.e.,
it lacks a vendor-extension tree).  RFC 3427 [2] documents
concerns with regards to new SIP extensions which may damage
security, greatly increase the complexity of the protocol, or
both.  New parameters and parameter values need to be documented
in RFCs as a result of these concerns.

RFCs defining SIP URI, SIPS URI parameters, or parameter values MUST
register them with IANA as described below.

Registered SIP and SIPS URI parameters and their values are to be
considered "reserved words".  In order to preserve interoperability,
registered parameters MUST be used in a manner consistent with that
described in their defining RFC.  Implementations MUST NOT utilize
"private" or "locally defined" URI parameters that conflict with
registered parameters.

Note that although unregistered SIP and SIPS URI parameters may be
used in implementations, developers are cautioned that usage of
such parameters is risky.  New SIP and SIPS URI parameters and new
values for them may be registered at any time, and there is no
assurance that these new registered URI parameters will not
conflict with unregistered parameters currently in use.

Some SIP and SIPS URI parameters only accept a set of predefined
parameter values.  For example, a parameter indicating the transport
protocol in use may only accept the predefined tokens TCP, UDP, and
SCTP as valid values.  Registering all parameter values for all SIP
and SIPS URI parameters of this type would require a large number of
subregistries.  Instead, we have chosen to register URI parameter
values by reference.  That is, the entry in the URI parameter
registry for a given URI parameter contains references to the RFCs
defining new values of that parameter.  References to RFCs defining
parameter values appear in double brackets in the registry.

So, the SIP and SIPS URI parameter registry contains a column that
indicates whether or not each parameter only accepts a set of
predefined values.  Implementers of parameters with a "yes" in that
column need to find all the valid parameter values in the RFCs
provided as references.

# 4. IANA Considerations

Section 27 of RFC 3261 [1] creates an IANA registry for method names,
header field names, warning codes, status codes, and option tags.
This specification creates a new sub-registry under the SIP
Parameters registry.

o  SIP/SIPS URI Parameters

## 4.1. SIP and SIPS URI Parameters Sub-Registry

New SIP and SIPS URI parameters and new parameter values are
registered by the IANA.  When registering a new SIP or SIPS parameter
or a new value for a parameter, the following information MUST be
provided.

o  Name of the parameter.

o  Whether the parameter only accepts a set of predefined values.

o  Reference to the RFC defining the parameter and to any RFC that
defines new values for the parameter.  References to RFCs
defining parameter values appear in double brackets in the
registry.

Table 1 contains the initial values for this sub-registry.

Parameter Name  Predefined Values  Reference
____________________________________________
comp                   Yes        [RFC 3486]
lr                      No        [RFC 3261]
maddr                   No        [RFC 3261]
method                 Yes        [RFC 3261]
transport              Yes        [RFC 3261]
ttl                     No        [RFC 3261]
user                   Yes        [RFC 3261]

Table 1: IANA SIP and SIPS URI parameter sub-registry

Note that any given parameter name is registered both as a SIP and as
a SIPS URI parameter.  Still, some parameters may not apply to one of
the schemes.  We have chosen to register any parameter as both a SIP
and SIPS URI parameter anyway to avoid having two parameters with the
same name, one applicable to SIP URIs and one to SIPS URIs, but with
different semantics.  Implementors are urged to read the parameter
specifications for a detailed description of the semantics of any
parameter.

## 4.2. Registration Policy for SIP and SIPS URI Parameters

As per the terminology in RFC 2434 [4], the registration policy for
SIP and SIPS URI parameters shall be "Specification Required".

For the purposes of this registry, the parameter for which IANA
registration is requested MUST be defined by a standards-track RFC.

# 5. Security Considerations

The registry in this document does not in itself have security
considerations.  However, as mentioned in RFC 3427, an important
reason for the IETF to manage the extensions of SIP is to ensure that
all extensions and parameters are able to provide secure usage.  The
supporting RFC publications for parameter registrations described
this specification MUST provide detailed security considerations for
them.

# 6. Acknowledgements

Jonathan Rosenberg, Henning Schulzrinne, Rohan Mahy, Dean Willis, and
Allison Mankin provided useful comments on this document.

# 7. Normative References

[1] Rosenberg, J., Schulzrinne, H., Camarillo, G., Johnston, A.,
Peterson, J., Sparks, R., Handley, M., and E. Schooler, "SIP:
Session Initiation Protocol", RFC 3261, June 2002.

[2] Mankin, A., Bradner, S., Mahy, R., Willis, D., Ott, J., and B.
Rosen, "Change Process for the Session Initiation Protocol
(SIP)", BCP 67, RFC 3427, December 2002.

[3] Bradner, S., "Key words for use in RFCs to Indicate Requirement
Levels", BCP 14, RFC 2119, March 1997.

[4] Narten, T. and H. Alvestrand, "Guidelines for Writing an IANA
Considerations Section in RFCs", BCP 26, RFC 2434, October 1998.

# Author's Address

Gonzalo Camarillo
Ericsson
Advanced Signalling Research Lab.
FIN-02420 Jorvas
Finland

EMail:  Gonzalo.Camarillo@ericsson.com

Full Copyright Statement

Copyright (C) The Internet Society (2004).

This document is subject to the rights, licenses and restrictions
contained in BCP 78, and except as set forth therein, the authors
retain all their rights.

This document and the information contained herein are provided on an
"AS IS" basis and THE CONTRIBUTOR, THE ORGANIZATION HE/SHE REPRESENTS
OR IS SPONSORED BY (IF ANY), THE INTERNET SOCIETY AND THE INTERNET
ENGINEERING TASK FORCE DISCLAIM ALL WARRANTIES, EXPRESS OR IMPLIED,
INCLUDING BUT NOT LIMITED TO ANY WARRANTY THAT THE USE OF THE
INFORMATION HEREIN WILL NOT INFRINGE ANY RIGHTS OR ANY IMPLIED
WARRANTIES OF MERCHANTABILITY OR FITNESS FOR A PARTICULAR PURPOSE.

Intellectual Property

The IETF takes no position regarding the validity or scope of any
Intellectual Property Rights or other rights that might be claimed to
pertain to the implementation or use of the technology described in
this document or the extent to which any license under such rights
might or might not be available; nor does it represent that it has
made any independent effort to identify any such rights.  Information
on the IETF's procedures with respect to rights in IETF Documents can
be found in BCP 78 and BCP 79.

Copies of IPR disclosures made to the IETF Secretariat and any
assurances of licenses to be made available, or the result of an
attempt made to obtain a general license or permission for the use of
such proprietary rights by implementers or users of this
specification can be obtained from the IETF on-line IPR repository at
http://www.ietf.org/ipr.

The IETF invites any interested party to bring to its attention any
copyrights, patents or patent applications, or other proprietary
rights that may cover technology that may be required to implement
this standard.  Please address the information to the IETF at ietf-
ipr@ietf.org.

Acknowledgement

Funding for the RFC Editor function is currently provided by the
Internet Society.
