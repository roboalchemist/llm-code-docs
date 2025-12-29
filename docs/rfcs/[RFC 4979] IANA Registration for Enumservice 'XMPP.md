---
rfc: 4979
title: "IANA Registration for Enumservice 'XMPP'"
date: August 2007
category: Standards
---

# Abstract

This document requests IANA registration of an Enumservice for XMPP,
the Extensible Messaging and Presence Protocol.  This Enumservice
specifically allows the use of 'xmpp' Uniform Resource Identifiers
(URIs) in the context of E.164 Number Mapping (ENUM).

# Table of Contents

  - [1.  Introduction](#1-introduction)
  - [2.  Terminology](#2-terminology)
  - [3.  Enumservice Registration - XMPP](#3-enumservice-registration-xmpp)
  - [4.  XMPP IRI/URI Considerations for ENUM](#4-xmpp-iriuri-considerations-for-enum)
  - [4.1.  Authority Component](#41-authority-component)
  - [4.2.  IRI-to-URI mapping](#42-iri-to-uri-mapping)
  - [5.  Example](#5-example)
  - [6.  Security and Privacy Considerations](#6-security-and-privacy-considerations)
  - [7.  IANA Considerations](#7-iana-considerations)
  - [8.  Acknowledgements](#8-acknowledgements)
  - [9.  References](#9-references)
  - [9.1.  Normative References](#91-normative-references)
  - [9.2.  Informative References](#92-informative-references)

# 1. Introduction

E.164 Number Mapping (ENUM) [1] uses the Domain Name System (DNS) [6]
to refer from E.164 numbers [7] to Uniform Resource Identifiers
(URIs) [3].  Specific services to be used with ENUM must be
registered with IANA.  Section 3 of RFC 3761 describes the process of
such an Enumservice registration.

The Extensible Messaging and Presence Protocol (XMPP) [9] provides
means for streaming Extensible Markup Language (XML) [8] elements
between endpoints in close to real time.  The XMPP framework is
mainly used to provide instant messaging, presence, and streaming
media services.

RFC 4622 [5] registers a Uniform Resource Identifier (URI) scheme for
identifying an XMPP entity as a URI or as an Internationalized
Resource Identifier (IRI) [4].  The Enumservice specified in this
document allows the provisioning of such "xmpp" URIs (and the URI
representations of "xmpp" IRIs) in ENUM.

# 2. Terminology

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT",
"SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this
document are to be interpreted as described in RFC 2119 [2].

# 3. Enumservice Registration - XMPP

The following template contains information required for the IANA
registrations of the 'XMPP' Enumservice, according to Section 3 of
RFC 3761:

Enumservice Name: "XMPP"

Enumservice Type: "xmpp"

Enumservice Subtype: n/a

URI Schemes: "xmpp"

Functional Specification:

This Enumservice indicates that the resource identified is an XMPP
entity.

Security Considerations: see Section 6

Intended Usage: COMMON

Author: Alexander Mayrhofer <alexander.mayrhofer@enum.at>

# 4. XMPP IRI/URI Considerations for ENUM

## 4.1. Authority Component

XMPP IRIs/URIs optionally contain an "Authority Component" (see
Section 2.3 of RFC 4622).  The presence of such an Authority
Component in an IRI/URI signals the processing application to
authenticate as the user indicated in the URI/IRI rather than using
the preconfigured identity.

In the context of this Enumservice, arbitrary clients may discover
and use the XMPP URIs/IRIs associated to an E.164 number.  Hence, in
most cases, those clients will not be able to authenticate as
requested in the Authority Component.

Therefore, URIs/IRIs that result from processing an XMPP Enumservice
record SHOULD NOT contain an Authority Component.

## 4.2. IRI-to-URI mapping

While XMPP supports IRIs as well as 'plain' URIs, ENUM itself
supports only the use of URIs for Enumservices.

Therefore, XMPP IRIs MUST be mapped to URIs for use in an XMPP
Enumservice record.  The mapping MUST follow the procedures outlined
in Section 3.1 of RFC 3987.

# 5. Example

An example ENUM entry referencing to a XMPP URI could look like:

```
             $ORIGIN 6.9.4.0.6.9.4.5.1.1.4.4.e164.arpa.
             @  IN NAPTR  ( 100 10 "u"
                            "E2U+xmpp"
                            "!^.*$!xmpp:some-user@example.com!" .
                          )

```

# 6. Security and Privacy Considerations

General security considerations of the protocols on which this
Enumservice registration is based are addressed in Sections 3.1.3 and
6 of RFC 3761 (ENUM) and Section 14 of RFC 3920 (XMPP).

Since ENUM uses DNS -- a publicly available database -- any
information contained in records provisioned in ENUM domains must be
considered public as well.  Even after revoking the DNS entry and
removing the referred resource, copies of the information could still
be available.

Information published in ENUM records could reveal associations
between E.164 numbers and their owners -- especially if IRIs/URIs
contain personal identifiers or domain names for which ownership
information can be obtained easily.

However, it is important to note that the ENUM record itself does not
need to contain any personal information.  It just points to a
location where access to personal information could be granted.

ENUM records pointing to third-party resources can easily be
provisioned on purpose by the ENUM domain owner -- so any assumption
about the association between a number and an entity could therefore
be completely bogus unless some kind of identity verification is in
place.  This verification is out of scope for this memo.

# 7. IANA Considerations

This memo requests IANA to add a new "XMPP" Enumservice to the
'Enumservice Registrations' registry, according to the definitions in
this document and RFC 3761 [1].

The required template is contained in Section 3.

# 8. Acknowledgements

Some text from RFC 4622 was used in the Introduction of this
document.  Charles Clancy, Miguel Garcia, Andrew Newton, Jon
Peterson, and Peter Saint-Andre provided extensive reviews and
valuable feedback.

# 9. References

## 9.1. Normative References

[1]  Faltstrom, P. and M. Mealling, "The E.164 to Uniform Resource
Identifiers (URI) Dynamic Delegation Discovery System (DDDS)
Application (ENUM)", RFC 3761, April 2004.

[2]  Bradner, S., "Key words for use in RFCs to Indicate Requirement
Levels", BCP 14, RFC 2119, March 1997.

[3]  Berners-Lee, T., Fielding, R., and L. Masinter, "Uniform
Resource Identifier (URI): Generic Syntax", STD 66, RFC 3986,
January 2005.

[4]  Duerst, M. and M. Suignard, "Internationalized Resource
Identifiers (IRIs)", RFC 3987, January 2005.

[5]  Saint-Andre, P., "Internationalized Resource Identifiers (IRIs)
and Uniform Resource Identifiers (URIs) for the Extensible
Messaging and Presence Protocol (XMPP)", RFC 4622, July 2006.

## 9.2. Informative References

[6]  Mockapetris, P., "Domain names - implementation and
specification", STD 13, RFC 1035, November 1987.

[7]  ITU-T, "The international public telecommunication numbering
plan", Recommendation E.164 (02/05), Feb. 2005.

[8]  Maler, E., Paoli, J., Bray, T., Yergeau, F., and C. Sperberg-
McQueen, "Extensible Markup Language (XML) 1.0 (Third Edition)",
World Wide Web Consortium FirstEdition REC-xml-20040204,
February 2004, <http://www.w3.org/TR/2004/REC-xml-20040204>.

[9]  Saint-Andre, P., Ed., "Extensible Messaging and Presence
Protocol (XMPP): Core", RFC 3920, October 2004.

# Author's Address

Alexander Mayrhofer
enum.at GmbH
Karlsplatz 1/2/9
Wien  A-1010
Austria

Phone: +43 1 5056416 34
EMail: alexander.mayrhofer@enum.at
URI:   http://www.enum.at/

Full Copyright Statement

Copyright (C) The IETF Trust (2007).

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

Acknowledgement

Funding for the RFC Editor function is currently provided by the
Internet Society.
