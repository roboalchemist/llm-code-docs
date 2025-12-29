---
rfc: 9844
title: "Entering IPv6 Zone Identifiers in User Interfaces"
date: August 2025
category: Standards
obsoletes: [6874]
updates: [4007, 7622, 8089]
---

# Abstract

This document describes how the zone identifier of an IPv6 scoped
address, defined in the IPv6 Scoped Address Architecture
specification (RFC 4007), should be entered into a user interface.
This document obsoletes RFC 6874 and updates RFCs 4007, 7622, and
8089.

# Status of This Memo

This is an Internet Standards Track document.

This document is a product of the Internet Engineering Task Force
(IETF).  It represents the consensus of the IETF community.  It has
received public review and has been approved for publication by the
Internet Engineering Steering Group (IESG).  Further information on
Internet Standards is available in Section 2 of RFC 7841.

Information about the current status of this document, any errata,
and how to provide feedback on it may be obtained at
https://www.rfc-editor.org/info/rfc9844.

# Copyright Notice

Copyright (c) 2025 IETF Trust and the persons identified as the
document authors.  All rights reserved.

This document is subject to BCP 78 and the IETF Trust's Legal
Provisions Relating to IETF Documents
(https://trustee.ietf.org/license-info) in effect on the date of
publication of this document.  Please review these documents
carefully, as they describe your rights and restrictions with respect
to this document.  Code Components extracted from this document must
include Revised BSD License text as described in Section 4.e of the
Trust Legal Provisions and are provided without warranty as described
in the Revised BSD License.

# Table of Contents

  - [1.  Introduction](#1-introduction)
  - [2.  Use Cases](#2-use-cases)
  - [3.  Relationship to Other Documents](#3-relationship-to-other-documents)
  - [4.  Requirements Language](#4-requirements-language)
  - [5.  Specification](#5-specification)
  - [6.  Security Considerations](#6-security-considerations)
  - [7.  IANA Considerations](#7-iana-considerations)
  - [8.  References](#8-references)
  - [8.1.  Normative References](#81-normative-references)
  - [8.2.  Informative References](#82-informative-references)
  - [Acknowledgements](#acknowledgements)
- [1.  Introduction](#1-introduction)
- [2.  Use Cases](#2-use-cases)
  - [1.  A software tool may be used for simple debugging actions](#1-a-software-tool-may-be-used-for-simple-debugging-actions)
  - [2.  A software tool must sometimes be used to configure or](#2-a-software-tool-must-sometimes-be-used-to-configure-or)
  - [3.  Using a monitoring tool such as a network sniffer, the user may](#3-using-a-monitoring-tool-such-as-a-network-sniffer-the-user-may)
  - [4.  The Microsoft Web Services for Devices (WSD) virtual printer port](#4-the-microsoft-web-services-for-devices-wsd-virtual-printer-port)
  - [5.  The National Marine Electronics Association (NMEA) has defined](#5-the-national-marine-electronics-association-nmea-has-defined)

For all such use cases, it is highly desirable that a complete IPv6
link-local address can be cut and pasted from one UI (such as the
output from a system command) to another.  Since such addresses may
include quite long hexadecimal strings, for example,
"fe80::8d0f:7f26:f5c8:780b%enx525400d5e0fb", any solution except cut-
and-paste is highly error prone.

# 3. Relationship to Other Documents

The use cases listed above apply to relatively simple actions on end
systems.  The zone identifiers that can be used are limited by the
host operating system, since [RFC4007] only specifies that they are
text strings, without specifying a maximum length or syntax.  As
[RFC4007] explains, each zone identifier corresponds to a numerical
zone index that qualifies a link-local address.

It should be noted that whereas some operating systems and network
APIs support a default zone identifier as recommended by [RFC4007],
others, including Linux, do not, and for them a solution is
particularly important, since a link-local address without a zone
index cannot be used in the Linux socket API.

The model in [RFC4007] assumes that the human-readable zone
identifier is mapped by the operating system into a numeric interface
index.  Typically, this mapping is performed by the socket API, e.g.,
by "getaddrinfo()".  The mapping between the human-readable zone
identifier string and the numeric value is a host-specific function
that varies between operating systems.  The present document is
concerned only with the human-readable string that is typically
displayed in an operating system's user interface.  However, in most
operating systems, it is possible to use the underlying interface
number, represented as a decimal integer, as an equivalent to the
human-readable string.  This is recommended by Section 11.2 of
[RFC4007], but it is not required.  This possibility does not affect
the UI requirement given in this document.

As IPv6 deployment becomes more widespread, the lack of a solution
for handling complete link-local addresses in all tools is becoming
an acute problem for increasing numbers of operational and support
personnel.  It will become critical as IPv6-only or IPv6-mostly
networks [RFC8925] [IPv6-MOSTLY], with nodes lacking native IPv4
support, appear.  For example, the NMEA use case mentioned above is
an immediate requirement.  This is the principal reason for
documenting this requirement now.

This document completely obsoletes [RFC6874], which implementors of
web browsers have determined is impracticable to support
[LINK-LOCAL-URI], and replaces it with a generic UI requirement.
Note that obsoleting [RFC6874] reverts the change that it made to the
URI syntax defined by [RFC3986], so [RFC3986] is no longer updated by
[RFC6874].  As far as is known, this change will have no significant
impact on non-browser deployments of URIs.

This document also updates [RFC7622] and [RFC8089] by deleting their
references to [RFC6874].

It also updates [RFC4007] by adding a new requirement that user
interfaces support the zone identifier as described in Section 5.

# 4. Requirements Language

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT",
"SHOULD", "SHOULD NOT", "RECOMMENDED", "NOT RECOMMENDED", "MAY", and
"OPTIONAL" in this document are to be interpreted as described in
BCP 14 [RFC2119] [RFC8174] when, and only when, they appear in all
capitals, as shown here.

# 5. Specification

A user interface (UI) that allows or requires the user to enter an
IPv6 address other than a global unicast address MUST provide a means
for entering a link-local address or a scoped multicast address and
selecting a zone identifier as specified by [RFC4007] (typically, an
interface identifier as defined by the operating system).

In this case, the UI SHOULD support the complete format specified by
[RFC4007] (e.g., "fe80::1%eth0").

If this is impossible for practical reasons, the UI MAY support an
alternative delimiter in place of "%".  The hyphen ("-") is suggested
(e.g., "fe80::1-eth0").

If this too is impossible for practical reasons, the UI MAY provide
two separate input fields (e.g., "fe80::1" in one box and "eth0" in
another), selection from a list of active zone identifiers, or a
separate command-line parameter for the zone identifier.

The program providing the UI will then store the address and the zone
identifier, converting the latter to an interface index (typically
via the socket API).  A faulty zone identifier will be detected when
attempting to convert it, and this should be reported to the user as
an error.  The resulting interface index will be used for any
subsequent socket calls using the link-local address.

Note that an address string such as "fe80::1%eth0" cannot be
converted to binary by the POSIX socket API function "inet_pton()"
[POSIX].  It must be converted either by using "getaddrinfo()" or by
splitting it into two strings and using "inet_pton()" and
"if_nametoindex()" successively, in order to obtain the required
interface index value.

In this model, the zone identifier is considered independently of the
IPv6 address itself.  However, this does not in itself resolve the
difficulties in considering the zone identifier as part of the HTTP
origin model [RFC6454].  Therefore, this approach does not resolve
the issue of how browsers should support link-local addresses, which
is discussed further in [LINK-LOCAL-URI].  Because of this, the
recommendations and normative statements in this document do not
apply to URIs fetched by web browsers.

# 6. Security Considerations

As explained in [RFC4007], zone identifiers are of local significance
only and must not be sent on the wire.  In particular, see the final
security consideration of [RFC4007], which indicates that software
should not trust packets that contain textual non-global addresses as
data.  Therefore, software that obtains a zone identifier through a
UI should not transmit it further.

There is no formal limit on the length of the zone identifier string
in [RFC4007].  A UI implementation should apply an appropriate length
limit when inputting a zone identifier, in order to minimize the risk
of a buffer overrun.  Typically, this limit would be the same as the
host operating system's limit on interface names.

[RFC4007] does not specify or restrict the character set allowed in a
zone identifier.  Therefore, each implementation processing zone
identifiers needs to make checks appropriate for the environment it
is used in.  For example, a UI implementation should not allow ASCII
NUL characters in a zone identifier string as this could cause
inconsistencies in subsequent string processing.

# 7. IANA Considerations

This document has no IANA actions.

# 8. References

## 8.1. Normative References

[RFC2119]  Bradner, S., "Key words for use in RFCs to Indicate
Requirement Levels", BCP 14, RFC 2119,
DOI 10.17487/RFC2119, March 1997,
<https://www.rfc-editor.org/info/rfc2119>.

[RFC4007]  Deering, S., Haberman, B., Jinmei, T., Nordmark, E., and
B. Zill, "IPv6 Scoped Address Architecture", RFC 4007,
DOI 10.17487/RFC4007, March 2005,
<https://www.rfc-editor.org/info/rfc4007>.

[RFC4291]  Hinden, R. and S. Deering, "IP Version 6 Addressing
Architecture", RFC 4291, DOI 10.17487/RFC4291, February
2006, <https://www.rfc-editor.org/info/rfc4291>.

[RFC5952]  Kawamura, S. and M. Kawashima, "A Recommendation for IPv6
Address Text Representation", RFC 5952,
DOI 10.17487/RFC5952, August 2010,
<https://www.rfc-editor.org/info/rfc5952>.

[RFC8174]  Leiba, B., "Ambiguity of Uppercase vs Lowercase in RFC
2119 Key Words", BCP 14, RFC 8174, DOI 10.17487/RFC8174,
May 2017, <https://www.rfc-editor.org/info/rfc8174>.

## 8.2. Informative References

[IPv6-MOSTLY]
Buraglio, N., Caletka, O., and J. Linkova, "IPv6-Mostly
Networks: Deployment and Operations Considerations", Work
in Progress, Internet-Draft, draft-ietf-v6ops-6mops-01, 3
March 2025, <https://datatracker.ietf.org/doc/html/draft-
ietf-v6ops-6mops-01>.

[LINK-LOCAL-URI]
Schinazi, D., "Best Practices for Link-Local Connectivity
in URI-Based Protocols", Work in Progress, Internet-Draft,
draft-schinazi-httpbis-link-local-uri-bcp-03, 22 February
2024, <https://datatracker.ietf.org/doc/html/draft-
schinazi-httpbis-link-local-uri-bcp-03>.

[LL-HACK]  Jin, P., "Snippets: IPv6 link-local connect hack", 2021,
<https://web.archive.org/web/20210725030713/
https://website.peterjin.org/wiki/
Snippets:IPv6_link_local_connect_hack>.

[ONE-NET]  NMEA, "OneNet Marine IPv6 Ethernet Networking Standard",
2025, <https://www.nmea.org/nmea-onenet.html>.

[POSIX]    IEEE, "IEEE/Open Group Standard for Information
Technology--Portable Operating System Interface
(POSIX(TM)) Base Specifications, Issue 8", IEEE
Std 1003.1-2024, DOI 10.1109/IEEESTD.2024.10555529, June
2024, <https://doi.org/10.1109/IEEESTD.2024.10555529>.

[RFC1918]  Rekhter, Y., Moskowitz, B., Karrenberg, D., de Groot, G.
J., and E. Lear, "Address Allocation for Private
Internets", BCP 5, RFC 1918, DOI 10.17487/RFC1918,
February 1996, <https://www.rfc-editor.org/info/rfc1918>.

[RFC3493]  Gilligan, R., Thomson, S., Bound, J., McCann, J., and W.
Stevens, "Basic Socket Interface Extensions for IPv6",
RFC 3493, DOI 10.17487/RFC3493, February 2003,
<https://www.rfc-editor.org/info/rfc3493>.

[RFC3986]  Berners-Lee, T., Fielding, R., and L. Masinter, "Uniform
Resource Identifier (URI): Generic Syntax", STD 66,
RFC 3986, DOI 10.17487/RFC3986, January 2005,
<https://www.rfc-editor.org/info/rfc3986>.

[RFC6454]  Barth, A., "The Web Origin Concept", RFC 6454,
DOI 10.17487/RFC6454, December 2011,
<https://www.rfc-editor.org/info/rfc6454>.

[RFC6874]  Carpenter, B., Cheshire, S., and R. Hinden, "Representing
IPv6 Zone Identifiers in Address Literals and Uniform
Resource Identifiers", RFC 6874, DOI 10.17487/RFC6874,
February 2013, <https://www.rfc-editor.org/info/rfc6874>.

[RFC6874bis]
Carpenter, B., Cheshire, S., and R. Hinden, "Representing
IPv6 Zone Identifiers in Address Literals and Uniform
Resource Identifiers", Work in Progress, Internet-Draft,
draft-ietf-6man-rfc6874bis-09, 2 July 2023,
<https://datatracker.ietf.org/doc/html/draft-ietf-6man-
rfc6874bis-09>.

[RFC6991]  Schoenwaelder, J., Ed., "Common YANG Data Types",
RFC 6991, DOI 10.17487/RFC6991, July 2013,
<https://www.rfc-editor.org/info/rfc6991>.

[RFC7622]  Saint-Andre, P., "Extensible Messaging and Presence
Protocol (XMPP): Address Format", RFC 7622,
DOI 10.17487/RFC7622, September 2015,
<https://www.rfc-editor.org/info/rfc7622>.

[RFC8089]  Kerwin, M., "The "file" URI Scheme", RFC 8089,
DOI 10.17487/RFC8089, February 2017,
<https://www.rfc-editor.org/info/rfc8089>.

[RFC8925]  Colitti, L., Linkova, J., Richardson, M., and T.
Mrugalski, "IPv6-Only Preferred Option for DHCPv4",
RFC 8925, DOI 10.17487/RFC8925, October 2020,
<https://www.rfc-editor.org/info/rfc8925>.

# Acknowledgements

This document owes a lot to the previous discussions that led to
[RFC6874] and to the expired Internet-Draft [RFC6874bis].

Useful comments were received from Erik Auerswald, Nick Buraglio,
Martin J. Dürst, Toerless Eckert, David Farmer, Brian Haberman, Nate
Karstens, Tero Kivinen, Erik Kline, Jen Linkova, Eduard Metz, Gyan
Mishra, David Schinazi, Jürgen Schönwälder, Michael Sweet, Martin
Thomson, Ole Troan, Éric Vyncke, Magnus Westerlund, and other
participants in the 6MAN WG.

# Authors' Addresses

Brian Carpenter
School of Computer Science
University of Auckland
PB 92019
Auckland 1142
New Zealand
Email: brian.e.carpenter@gmail.com

Robert M. Hinden
Check Point Software
959 Skyway Road
San Carlos, CA 94070
United States of America
Email: bob.hinden@gmail.com
