---
rfc: 5133
title: "Terminal Endpoint Identifier (TEI) Query Request Number Change"
date: December 2007
category: Standards
updates: [4233]
---

# Abstract

The Integrated Services Digital Network (ISDN) Q.921-User Adaptation
Layer (IUA) Protocol, described in RFC 4233, defines the message type
of Terminal Endpoint Identifier (TEI) Query Request messages as 5.
However, this number is already being used by the Digital Private
Network Signaling System (DPNSS)/Digital Access Signaling System 2
(DASS 2) Extensions (DUA) to the IUA Protocol described in RFC 4129.
This document updates RFC 4233 such that the message type of TEI
Query Request messages is 8.

# Table of Contents

  - [1.  Introduction](#1-introduction)
  - [2.  Conventions Used in This Document](#2-conventions-used-in-this-document)
  - [3.  New Message Type of the TEI Query Message](#3-new-message-type-of-the-tei-query-message)
  - [4.  IANA Considerations](#4-iana-considerations)
  - [5.  Security Considerations](#5-security-considerations)
  - [6.  Acknowledgments](#6-acknowledgments)
  - [7.  Normative References](#7-normative-references)

# 1. Introduction

The Integrated Services Digital Network (ISDN) Q.921-User Adaptation
Layer (IUA) protocol, described in [RFC3057], does not define a
Terminal Endpoint Identifier (TEI) Query Request message.  The
Digital Private Network Signaling System (DPNSS)/Digital Access
Signaling System 2 (DASS 2) Extensions (DUA) to the IUA Protocol,
described in [RFC4129], introduces Data Link Connection (DLC) Status
messages of type 5, 6, and 7.  Then, [RFC4233] was published, which
updates [RFC3057].  [RFC4233] also introduces the TEI Query Request
message and uses the message type of 5 for it.  This makes it
impossible to differentiate the DLC Status request from a TEI Query
Request.

This document updates [RFC4233].

# 2. Conventions Used in This Document

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT",
"SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this
document are to be interpreted as described in [RFC2119].

# 3. New Message Type of the TEI Query Message

This document updates [RFC4233] by introducing the following change:

Terminal Endpoint Identifier (TEI) Query messages MUST be encoded
with a message type of 8 instead of 5 as described in [RFC4233].

# 4. IANA Considerations

In the "Message Types" section of the "Signaling User Adaptation
Layer Assignments" registry, IANA has reserved the message type 8 of
Management Messages for Terminal Endpoint Identifier (TEI) Query
Request messages.

# 5. Security Considerations

This document does not require any security considerations in
addition to the ones given in [RFC4233].

# 6. Acknowledgments

The authors wish to thank Jon Peterson and Christian Vogt for their
invaluable comments.

# 7. Normative References

[RFC2119]  Bradner, S., "Key words for use in RFCs to Indicate
Requirement Levels", BCP 14, RFC 2119, March 1997.

[RFC3057]  Morneault, K., Rengasami, S., Kalla, M., and G.
Sidebottom, "ISDN Q.921-User Adaptation Layer", RFC 3057,
February 2001.

[RFC4129]  Mukundan, R., Morneault, K., and N. Mangalpally, "Digital
Private Network Signaling System (DPNSS)/Digital Access
Signaling System 2 (DASS 2) Extensions to the IUA
Protocol", RFC 4129, September 2005.

[RFC4233]  Morneault, K., Rengasami, S., Kalla, M., and G.
Sidebottom, "Integrated Services Digital Network (ISDN)
Q.921-User Adaptation Layer", RFC 4233, January 2006.

# Authors' Addresses

Michael Tuexen
Muenster Univ. of Applied Sciences
Stegerwaldstr. 39
48565 Steinfurt
Germany

EMail: tuexen@fh-muenster.de

Ken Morneault
Cisco Systems, Inc.
13615 Dulles Technology Drive
Herndon, VA  20171
US

Phone: +1-703-484-3323
EMail: kmorneau@cisco.com

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
