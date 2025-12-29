---
rfc: 4508
title: "Conveying Feature Tags with the"
date: May 2006
category: Standards
---

# Abstract

The SIP "Caller Preferences" extension defined in RFC 3840 provides a
mechanism that allows a SIP request to convey information relating to
the originator's capabilities and preferences for handling of that
request.  The SIP REFER method defined in RFC 3515 provides a
mechanism that allows one party to induce another to initiate a SIP
request.  This document extends the REFER method to use the mechanism
of RFC 3840.  By doing so, the originator of a REFER may inform the
recipient as to the characteristics of the target that the induced
request is expected to reach.

# Table of Contents

  - [1. Introduction](#1-introduction)
  - [2. Terminology](#2-terminology)
  - [3. Definitions](#3-definitions)
  - [4. Examples](#4-examples)
    - [4.1. isfocus Feature Tag Usage](#41-isfocus-feature-tag-usage)
    - [4.2. Voice and Video Feature Tags Usage](#42-voice-and-video-feature-tags-usage)
    - [4.3. Example with URI parameters and multiple feature tags](#43-example-with-uri-parameters-and-multiple-feature-tags)
  - [5. Security Considerations](#5-security-considerations)
  - [6. Acknowledgements](#6-acknowledgements)
  - [7. Normative References](#7-normative-references)

# 1. Introduction

This document extends the SIP [2] REFER method defined in RFC 3515
[3] to be used with feature parameters defined in RFC 3840 [4].

Feature tags are used by a UA to convey to another UA information
about capabilities and features.  This information can be shared by a
UA using a number of mechanisms, including REGISTER requests and
responses and OPTIONS responses.  This information can also be shared
in the context of a dialog by inclusion with a remote target URI
(Contact URI).

Feature tag information can be very useful to another UA.  It is
especially useful prior to the establishment of a session.  For
example, if a UA knows (through an OPTIONS query, for example) that
the remote UA supports both video and audio, the calling UA might
call, offering video in the SDP.  Another example is when a UA knows
that a remote UA is acting as a focus and hosting a conference.  In
this case, the UA might first subscribe to the conference URI and
find out details about the conference prior to sending an INVITE to
join.

This extension to the REFER method provides a mechanism by which the
REFER-Issuer can provide this useful information about the REFER-
Target capabilities and functionality to the REFER-Recipient by
including feature tags in the Refer-To header field in a REFER
request.

# 2. Terminology

In this document, the key words "MUST", "MUST NOT", "REQUIRED",
"SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY",
and "OPTIONAL" are to be interpreted as described in RFC 2119 [1].

To simplify discussions of the REFER method and its extensions, three
new terms are used throughout the document:

o  REFER-Issuer: the UA issuing the REFER request
o  REFER-Recipient: the UA receiving the REFER request
o  REFER-Target: the UA designated in the Refer-To URI

# 3. Definitions

The Refer-To BNF from RFC 3515:

Refer-To = ("Refer-To" / "r") HCOLON ( name-addr / addr-spec )
*(SEMI generic-param)

is extended to:

Refer-To = ("Refer-To" / "r") HCOLON ( name-addr / addr-spec )
*(SEMI refer-param)
refer-param = generic-param / feature-param

where feature-param is defined in Section 9 of RFC 3840 [4].

Note that if any URI parameters are present, the entire URI must be
enclosed in "<" and ">".  If the "<" and ">" are not present, all
parameters after the URI are header parameters, not URI parameters.

# 4. Examples

## 4.1. isfocus Feature Tag Usage

The example below shows how the "isfocus" feature tag can be used by
REFER-Issuer to tell the REFER-Recipient that the REFER-Target is a
conference focus and, consequently, that sending an INVITE will bring
the REFER-Recipient into the conference:

Refer-To: sip:conf44@example.com;isfocus

## 4.2. Voice and Video Feature Tags Usage

The example below shows how a REFER-Issuer can tell the REFER-
Recipient that the REFER-Target supports audio and video and,
consequently, that a video and audio session can be established by
sending an INVITE to the REFER-Target:

Refer-To: "Alice's Videophone" <sip:alice@videophone.example.com>
;audio;video

## 4.3. Example with URI parameters and multiple feature tags

The example below shows how the REFER-Issuer can tell the REFER-
Recipient that the REFER-Target is a voicemail server.  Note that the
transport URI parameter is enclosed within the "<" and ">" so that it
is not interpreted as a header parameter.

Refer-To: <sip:alice-vm@example.com;transport=tcp>
;actor="msg-taker";automata;audio

# 5. Security Considerations

Feature tags can provide sensitive information about a user or a UA.
As such, RFC 3840 cautions against providing sensitive information to
another party.  Once this information is given out, any use may be
made of it, including relaying to a third party as in this
specification.

A REFER-Issuer MUST NOT create or guess feature tags. Instead, a
feature tag included in a REFER SHOULD be discovered in an
authenticated and secure method (such as an OPTIONS response or from
a remote target URI in a dialog) directly from the REFER-Target.

It is RECOMMENDED that the REFER-Issuer includes in the Refer-To
header field all feature tags that were listed in the most recent
Contact header field of the REFER-Target.

A feature tag provided by a REFER-Issuer cannot be authenticated or
certified directly from the REFER request.  As such, the REFER-
Recipient MUST treat the information as a hint.  If the REFER-
Recipient application logic or user's action depends on the presence
of the expressed feature, the feature tag can be verified.  For
example, in order to do so, the REFER-Recipient can directly send an
OPTIONS query to the REFER-Target over a secure (e.g., mutually
authenticated and integrity-protected) connection.  This protects the
REFER-Recipient against the sending of incorrect or malicious feature
tags.

# 6. Acknowledgements

The authors would like to thank Jonathan Rosenberg for providing
helpful guidance to this work.

# 7. Normative References

[1]  Bradner, S., "Key words for use in RFCs to Indicate Requirement
Levels", BCP 14, RFC 2119, March 1997.

[2]  Rosenberg, J., Schulzrinne, H., Camarillo, G., Johnston, A.,
Peterson, J., Sparks, R., Handley, M., and E. Schooler, "SIP:
Session Initiation Protocol", RFC 3261, June 2002.

[3]  Sparks, R., "The Session Initiation Protocol (SIP) Refer
Method", RFC 3515, April 2003.

[4]  Rosenberg, J., Schulzrinne, H., and P. Kyzivat, "Indicating User
Agent Capabilities in the Session Initiation Protocol (SIP)",
RFC 3840, August 2004.

# Authors' Addresses

Orit Levin
Microsoft Corporation
One Microsoft Way
Redmond, WA  98052
USA

Phone: 425-722-2225
EMail: oritl@microsoft.com

Alan Johnston
Avaya
St. Louis, MO 63124

EMail: ajohnston@ipstation.com

Full Copyright Statement

Copyright (C) The Internet Society (2006).

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

Funding for the RFC Editor function is provided by the IETF
Administrative Support Activity (IASA).
