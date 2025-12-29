---
rfc: 5526
title: "The E.164 to Uniform Resource Identifiers (URI)"
date: April 2009
category: Informational
---

# Abstract

This document defines the use case for Infrastructure ENUM and
proposes its implementation as a parallel namespace to "e164.arpa",
as defined in RFC 3761, as the long-term solution to the problem of
allowing carriers to provision DNS records for telephone numbers
independently of those provisioned by end users (number assignees).

# Table of Contents

  - [1. Introduction](#1-introduction)
  - [2. Terminology](#2-terminology)
  - [3. Zone Apex for Infrastructure ENUM](#3-zone-apex-for-infrastructure-enum)
  - [4. IANA Considerations](#4-iana-considerations)
  - [5. Security and Privacy Considerations](#5-security-and-privacy-considerations)
  - [6. Acknowledgements](#6-acknowledgements)
  - [7. Normative References](#7-normative-references)

# 1. Introduction

ENUM (E.164 Number Mapping [1]) is a system that transforms E.164
numbers [2] into domain names and then uses the DNS (Domain Name
Service) [3] to discover NAPTR records that specify what services are
available for a specific domain name.

ENUM as originally defined was based on the end-user opt-in
principle.  While this has great potential to foster new services and
end-user choices in the long term, the current requirements for
IP-based interconnection of Voice over IP (VoIP) domains require the
provisioning of large numbers of allocated or served (hosted) numbers
of a participating service provider, without the need for individual
users to opt-in.  This way, service providers can provision their own
ENUM information that is separate, distinct, and likely to be
different from what an end-user may provision.  This is particularly
important if Infrastructure ENUM is used for number-portability
applications, for example, which an end-user would be unlikely
interested in provisioning but which a service provider would likely
find essential.

In addition, while it is possible that service providers could
mandate that their users opt-into e164.arpa through end-user contract
terms and conditions, there are substantial downsides to such an
approach.  Thus, for all these reasons and many others, ENUM for
end-user provisioning is ill-suited for use by service providers for
the interconnection of VoIP domains.

As VoIP evolves and becomes pervasive, E.164-addressed telephone
calls need not necessarily traverse the Public Switched Telephone
Network (PSTN).  Therefore, VoIP service providers have an interest
in using ENUM on a so-called "Infrastructure" basis in order to keep
VoIP traffic on IP networks on an end-to-end basis, both within and
between service provider domains.  This requires a means of
identifying a VoIP point of interconnection to which calls addressed
to a given E.164 number may be delivered; Infrastructure ENUM
provides this means.  Calls that can originate and terminate on IP
networks, and do not have to traverse the PSTN, will require fewer or
no points of transcoding, and can also involve additional IP network
services that are not possible on the PSTN, among other benefits.

Requirements for Infrastructure ENUM are provided in [4].

# 2. Terminology

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT",
"SHOULD", "SHOULD NOT", "RECOMMENDED",  "MAY", and "OPTIONAL" in this
document are to be interpreted as described in BCP 14, RFC 2119 [5].

# 3. Zone Apex for Infrastructure ENUM

This document proposes that Infrastructure ENUM be implemented by
means of a parallel namespace to e164.arpa dedicated to
Infrastructure ENUM, in a domain that is yet to be determined.  Use
of a parallel namespace allows carriers and end-users to control
their ENUM registrations independently, without forcing one to work
through the other.

Infrastructure ENUM Tier 2 resource records in the Infrastructure
ENUM tree will be controlled by the service provider that is
providing services to a given E.164 number, generally referred to in
various countries as the "carrier-of-record" (see [4]).  The
definition of a carrier-of-record for a given E.164 number is a
national matter or is defined by the entity controlling the numbering
space.

See also Section 3, "Requirements for Infrastructure ENUM", of [4].

# 4. IANA Considerations

IANA has created a registry for Enumservices as originally specified
in RFC 2916 and revised in RFC 3761.  Enumservices registered with
IANA are valid for Infrastructure ENUM as well as end-user ENUM.

# 5. Security and Privacy Considerations

This document proposes a new zone apex for ENUM to meet the
requirements of Infrastructure ENUM.  The over-the-network protocol
of ENUM is unchanged by the addition of an apex and, as such, the
Security Considerations of RFC 3761 [1] still apply.  Specific
considerations related to the security of an Infrastructure ENUM apex
are given in more detail in Section 4, "Security Considerations", of
[4].

Infrastructure ENUM registrations proposed by this document should
resolve to service provider points-of-interconnection rather than to
end-user equipment.  Service providers need to take appropriate
measures to protect their end-user customers from unwanted
communications as with other types of interconnections.

# 6. Acknowledgements

The authors wish to thank Lawrence Conroy, Patrik Faltstrom, Michael
Haberler, Otmar Lendl, Steve Lind, Alexander Mayrhofer, Jim Reid, and
Richard Shockey for their helpful discussions of this document and
the concept of Infrastructure ENUM.

# 7. Normative References

[1] Faltstrom, P. and M. Mealling, "The E.164 to Uniform Resource
Identifiers (URI) Dynamic Delegation Discovery System (DDDS)
Application (ENUM)", RFC 3761, April 2004.

[2] ITU-T, "The International Public Telecommunication Number Plan",
Recommendation E.164, February 2005.

[3] Mockapetris, P., "Domain names - concepts and facilities", STD
13, RFC 1034, November 1987.

[4] Lind, S. and P. Pfautz, "Infrastructure ENUM Requirements", RFC
5067, November 2007.

[5] Bradner, S., "Key words for use in RFCs to Indicate Requirement
Levels", BCP 14, RFC 2119, March 1997.

# Authors' Addresses

Jason Livingood
Comcast Cable Communications
1500 Market Street
Philadelphia, PA 19102
USA

Phone: +1-215-981-7813
EMail: jason_livingood@cable.comcast.com

Penn Pfautz
AT&T
200 S. Laurel Ave
Middletown, NJ  07748
USA

Phone: +1-732-420-4962
EMail: ppfautz@att.com

Richard Stastny
Anzbachgasse 43
1140 Vienna
Austria

Phone: +43-664-420-4100
EMail: richard.stastny@gmail.com
