---
rfc: 7913
title: "P-Access-Network-Info ABNF Update"
date: June 2016
category: Informational
updates: [7315]
---

# Abstract

This document updates RFC 7315, by modifying the extension-access-
info part of the P-Access-Network-Info header field Augmented Backus-
Naur Form (ABNF), and by adding the following 'access-info' header
field parameter values to the list of 'access-info' header field
parameter values in the ABNF: 'operator-specific-GI' and
'utran-sai-3gpp'.  The values are defined in the ABNF but are not
included in the list.

# Status of This Memo

This document is not an Internet Standards Track specification; it is
published for informational purposes.

This document is a product of the Internet Engineering Task Force
(IETF).  It represents the consensus of the IETF community.  It has
received public review and has been approved for publication by the
Internet Engineering Steering Group (IESG).  Not all documents
approved by the IESG are a candidate for any level of Internet
Standard; see Section 2 of RFC 7841.

Information about the current status of this document, any errata,
and how to provide feedback on it may be obtained at
http://www.rfc-editor.org/info/rfc7913.

# Copyright Notice

Copyright (c) 2016 IETF Trust and the persons identified as the
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
  - [2.  Update to RFC 7315](#2-update-to-rfc-7315)
  - [3.  Security Considerations](#3-security-considerations)
  - [4.  Normative References](#4-normative-references)
  - [Acknowledgments](#acknowledgments)
  - [Author's Address](#authors-address)

However, the values are not included in the list of 'access-info'
values.

This document updates Section 5.4 of [RFC7315], by modifying the
extension-access-info part of the P-Access-Network-Info header field
ABNF.

As the P-Access-Network-Info header field is mainly used in networks
defined by the 3rd-Generation Partnership Project (3GPP), where new
values following the 'generic-param' rule have been defined

```
   [TS.3GPP.24.229], the update is not considered to cause issues with
   backward compatibility.

```

# 2. Update to RFC 7315

This section updates the ABNF defined in Section 5.4 of RFC 7315, as
described below:

Old syntax:

access-info            = cgi-3gpp / utran-cell-id-3gpp /
dsl-location / i-wlan-node-id /
ci-3gpp2 / eth-location /
ci-3gpp2-femto / fiber-location /
np / gstn-location /local-time-zone /
dvb-rcs2-node-id / extension-access-info
np                     = "network-provided"
extension-access-info  = gen-value

New syntax:

access-info            = cgi-3gpp / utran-cell-id-3gpp /
dsl-location / i-wlan-node-id /
ci-3gpp2 / eth-location /
ci-3gpp2-femto / fiber-location /
np / gstn-location /local-time-zone /
dvb-rcs2-node-id / operator-specific-GI /
utran-sai-3gpp / extension-access-info
np                     = "network-provided"
extension-access-info  = generic-param

# 3. Security Considerations

The security considerations for the P-Access-Network-Info header
field are defined in [RFC7315].  The ABNF update defined in this
document does not impact the security considerations.

# 4. Normative References

[RFC3261]  Rosenberg, J., Schulzrinne, H., Camarillo, G., Johnston,
A., Peterson, J., Sparks, R., Handley, M., and E.
Schooler, "SIP: Session Initiation Protocol", RFC 3261,
DOI 10.17487/RFC3261, June 2002,
<http://www.rfc-editor.org/info/rfc3261>.

[RFC5234]  Crocker, D., Ed. and P. Overell, "Augmented BNF for Syntax
Specifications: ABNF", STD 68, RFC 5234,
DOI 10.17487/RFC5234, January 2008,
<http://www.rfc-editor.org/info/rfc5234>.

[RFC7315]  Jesske, R., Drage, K., and C. Holmberg, "Private Header
(P-Header) Extensions to the Session Initiation Protocol
(SIP) for the 3GPP", RFC 7315, DOI 10.17487/RFC7315, July
2014, <http://www.rfc-editor.org/info/rfc7315>.

```
   [TS.3GPP.24.229]
              3GPP, "IP multimedia call control protocol based on
              Session Initiation Protocol (SIP) and Session Description
```

Protocol (SDP); Stage 3", 3GPP TS 24.229 13.5.1, March
2016, <http://www.3gpp.org/ftp/Specs/html-info/24229.htm>.

# Acknowledgments

Thanks to Ben Campbell, Cullen Jennings, Gonzalo Salgueiro, Jean
Mahoney, Menachem Dodge, Olafur Gudmundsson, Paul Kyzivat, and the
3GPP community for providing guidance, input, and comments on the
document.

# Author's Address

Christer Holmberg
Ericsson
Hirsalantie 11
Jorvas  02420
Finland

Email: christer.holmberg@ericsson.com
