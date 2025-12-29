---
rfc: 3953
title: "Telephone Number Mapping (ENUM) Service"
date: January 2005
category: Standards
---

# Abstract

This document registers a Telephone Number Mapping (ENUM) service for
presence.  Specifically, this document focuses on provisioning pres
URIs in ENUM.

# Table of Contents

  - [1. Introduction](#1-introduction)
  - [2. ENUM Service Registration](#2-enum-service-registration)
  - [3. Presence for E.164 Numbers](#3-presence-for-e164-numbers)
  - [4. The 'E2U+pres' Enumservice](#4-the-e2upres-enumservice)
  - [5. Example of E2U+pres Enumservice](#5-example-of-e2upres-enumservice)
  - [6. Security Considerations](#6-security-considerations)
  - [7. IANA Considerations](#7-iana-considerations)
  - [8. References](#8-references)
    - [8.1.  Normative References](#81-normative-references)
    - [8.2.  Informative References](#82-informative-references)
  - [Author's Address](#authors-address)
  - [Full Copyright Statement](#full-copyright-statement)

# 1. Introduction

ENUM (E.164 Number Mapping, RFC 3761 [1]) is a system that uses DNS
(Domain Name Service, RFC 1034 [8]) to translate telephone numbers,
such as +12025332600, into URIs (Uniform Resource Identifiers, RFC
2396 [9]), such as pres:user@host.com.  ENUM exists primarily to
facilitate the interconnection of systems that rely on telephone
numbers with those that use URIs to identify resources.

Presence is a service defined in RFC 2778 [2] that allows users of a
communications service to monitor one another's availability and
disposition in order to make decisions about communicating.  Presence
information is highly dynamic and generally characterizes whether a
user is online or offline, busy or idle, away from communications
devices or nearby, and the like.

The IETF has defined a generic URI used to identify a presence
service for a particular resource: the 'pres' URI scheme (defined in
CPP [4]).  This document describes an enumservice for advertising
presence information associated with an E.164 number.

# 2. ENUM Service Registration

As defined in [1], the following is a template covering information
needed for the registration of the enumservice specified in this
document:

Service name: "E2U+pres"

URI scheme(s): "pres:"

Functional Specification: See section 4.

Security considerations: See section 6.

Intended usage: COMMON

Author: Jon Peterson (jon.peterson@neustar.biz)

Any other information that the author deems interesting: See
section 3.

# 3. Presence for E.164 Numbers

This document specifies an enumservice field that allows presence
information to be provided for an E.164 number.  This may include
presence states associated with telephones, or presence of non-
telephony communications services advertised by ENUM.

RFC 3953        ENUM Registration for Presence Services     January 2005

Endpoints that participate in a presence architecture are known
(following the framework in RFC 2778 [2]) as watchers and
presentities.  Watchers subscribe to the presence of presentities and
are notified when the presence of a presentity changes.  Watchers
generally monitor the presence of a group of presentities with whom
they have an ongoing association.  As an example, consider how this
might apply to a telephony service.  Most cellular telephones today
have an address book-like feature, a small database of names and
telephone numbers.  Such a telephone might act as a watcher,
subscribing to the presence of some or all of the telephone numbers
in its address book.  The display of the telephone might then show
its user, when a presence-enabled telephone number is selected, the
availability of the destination.  With this information, the user
might change their calling habits to correspond better to the
availability of his or her associates.

The presence information that is shared varies by communications
service.  The IETF has defined a Presence Information Data Format (or
PIDF [6]) for describing the presence data associated with a
presentity.  The baseline PIDF specification declares only two
presence states: OPEN and CLOSED (these terms are defined in RFC 2778
[2]); the former suggests that the destination resource is able to
accept communication requests, the latter that it is not.  These two
states provide useful but rudimentary insight into the communications
status of a presentity.  For that reason, PIDF is an extensible
format, and new sorts of statuses can be defined for specific
communications services.  For example, a telephony-based presence
service might define a status corresponding to 'busy'.  Extending
PIDF for telephony services is, however, outside the scope of this
document.

# 4. The 'E2U+pres' Enumservice

Traditionally, the services field of an NAPTR record (as defined in
[10]) contains a string composed of two subfields: a 'protocol'
subfield and a 'resolution service' subfield.  ENUM in particular
defines an 'E2U' (E.164 to URI) resolution service.  This document
defines an 'E2U+pres' enumservice for presence.

The scheme of the URI that will appear in the regexp field of an
NAPTR record using the 'E2U+pres' enumservice SHOULD be the 'pres'
URI scheme.  Other URI schemes appropriate to presence services MAY
be used; however, the use of the 'pres' URI scheme ensures a greater
level of compatibility than would the use of any URI specific to a
particular presence protocol.  The purpose of a pres URI is to
provide a generic way to locate a presence service.  Techniques for
dereferencing the pres URI to locate a presence service are given in
[5].

RFC 3953        ENUM Registration for Presence Services     January 2005

The 'pres' URI scheme does not identify any particular protocol that
will be used to handle presence operations (such as subscriptions and
notifications).  Rather, the mechanism in [5] details a way to
discover whether the presence protocol(s) supported by the watcher
is/are also supported by the presentity.  SIP [7] is one protocol
that can be used to convey presence information and manage
subscriptions/notifications.

# 5. Example of E2U+pres enumservice

The following is an example of the use of the enumservice registered
by this document in an NAPTR resource record.

$ORIGIN 3.8.0.0.6.9.2.3.6.1.4.4.e164.arpa.
IN NAPTR 100 10 "u" "E2U+pres" "!^.*$!pres:jon.peterson@example.net!"

# 6. Security Considerations

DNS does not make policy decisions about the records it shares with
an inquirer.  All DNS records must be assumed to be available to all
inquirers at all times.  The information provided within an ENUM
record set must therefore be considered open to the public -- which
is a cause for some privacy considerations.

Revealing a pres URI in and of itself is unlikely to introduce many
privacy concerns, although, depending on the structure of the URI, it
might reveal the full name or employer of the target.  The use of
anonymous URIs mitigates this risk.  More serious privacy concerns
are associated with the unauthorized distribution of presence
information.  For this reason, presence protocols have a number of
security requirements (detailed in RFC 2779 [3]) that call for
authentication of watchers, integrity and confidentiality properties,
and similar measures to prevent abuse of presence information.  Any
presence protocol used in conjunction with the 'pres' URI scheme is
required to meet these requirements.

Unlike a traditional telephone number, the resource identified by a
pres URI may require that callers provide cryptographic credentials
for authentication and authorization before presence information is
returned.  In concert with presence protocols, ENUM can actually
provide far greater protection from unwanted callers than does the
existing PSTN, despite the public availability of ENUM records.

RFC 3953        ENUM Registration for Presence Services     January 2005

# 7. IANA Considerations

This document registers the 'E2U+pres' enumservice under the
enumservice registry described in the IANA considerations in RFC
3761.  Details of the registration are given in section 2.

# 8. References

## 8.1. Normative References

[1]  Faltstrom, P. and M. Mealling, "The E.164 to Uniform Resource
Identifiers (URI) Dynamic Delegation Discovery System (DDDS)
Application", RFC 3761, April 2004.

[2]  Day, M., Rosenberg, J., and H. Sugano, "A Model for Presence and
Instant Messaging", RFC 2778, February 2000.

[3]  Day, M., Aggarwal, S., Mohr, G., and J. Vincent, "Instant
Messaging / Presence Protocol Requirements", RFC 2779, February
2000.

[4]  Peterson, J., "Common Profile for Presence (CPP)", RFC 3859,
August 2004.

[5]  Peterson, J., "Address Resolution for Instant Messaging and
Presence", RFC 3861, August 2004.

## 8.2. Informative References

[6]  Sugano, H., Fujimoto, S., Klyne, G., Bateman, A., Carr, W., and
J. Peterson, "Presence Information Data Format (PIDF)", RFC
3863, August 2004.

[7]  Rosenberg, J., Schulzrinne, H., Camarillo, G., Johnston, A.,
Peterson, J., Sparks, R., Handley, M., and E. Schooler, "SIP:
Session Initiation Protocol", RFC 3261, June 2002.

[8]  Mockapetris, P., "Domain Names - Concepts and Facilities", STD
13, RFC 1034, November 1987.

[9]  Berners-Lee, T., Fielding, R., and L. Masinter, "Uniform
Resource Identifiers (URI): Generic Syntax", RFC 2396, August
1998.

[10] Mealling, M., "Dynamic Delegation Discovery System (DDDS) Part
Three: The Domain Name System (DNS) Database", RFC 3403, October
2002.

RFC 3953        ENUM Registration for Presence Services     January 2005

# Author's Address

Jon Peterson
NeuStar, Inc.
1800 Sutter St.
Suite 570
Concord, CA  94520
USA

Phone: +1 925/363-8720
EMail: jon.peterson@neustar.biz
URI:   http://www.neustar.biz/

RFC 3953        ENUM Registration for Presence Services     January 2005

Full Copyright Statement

Copyright (C) The Internet Society (2005).

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
