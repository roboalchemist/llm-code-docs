---
rfc: 6577
title: "Authentication-Results Registration Update for"
date: March 2012
category: Standards
updates: [5451]
---

# Abstract

This memo updates the registry of authentication method results in
Authentication-Results: message header fields, correcting a
discontinuity between the original registry creation and the Sender
Policy Framework (SPF) specification.

This memo updates RFC 5451.

# Status of This Memo

This is an Internet Standards Track document.

This document is a product of the Internet Engineering Task Force
(IETF).  It represents the consensus of the IETF community.  It has
received public review and has been approved for publication by the
Internet Engineering Steering Group (IESG).  Further information on
Internet Standards is available in Section 2 of RFC 5741.

Information about the current status of this document, any errata,
and how to provide feedback on it may be obtained at
http://www.rfc-editor.org/info/rfc6577.

# Copyright Notice

Copyright (c) 2012 IETF Trust and the persons identified as the
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

  - [1. Introduction](#1-introduction)
  - [2. Keywords](#2-keywords)
  - [3. New 'fail' Definition](#3-new-fail-definition)
  - [4. IANA Considerations](#4-iana-considerations)
    - [4.1. Addition of 'Status' Columns](#41-addition-of-status-columns)
    - [4.2. Update to Result Names](#42-update-to-result-names)
  - [5. Security Considerations](#5-security-considerations)
  - [6. References](#6-references)
    - [6.1. Normative References](#61-normative-references)
    - [6.2. Informative References](#62-informative-references)
  - [Appendix A. Examples in RFC 5451](#appendix-a-examples-in-rfc-5451)
  - [Appendix B. Acknowledgements](#appendix-b-acknowledgements)

# 2. Keywords

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT",
"SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this
document are to be interpreted as described in [KEYWORDS].

# 3. New 'fail' Definition

The new "fail" result, replacing the existing "hardfail" result for
[SPF] (and thus also for [SENDER-ID]) has the same definition for
"hardfail" that was used in Section 2.4.2 of [AUTHRES], namely:

This client is explicitly not authorized to inject or relay mail
using the sender's DNS domain.

# 4. IANA Considerations

This section enumerates requested actions of IANA, per [IANA].

## 4.1. Addition of 'Status' Columns

IANA has amended the Email Authentication Methods and Email
Authentication Result Names registries, both in the Email
Authentication Parameters group, by adding to each a column called
"Status" that will indicate for each entry its current status.  Legal
values for these columns are as follows:

active:  The entry is in current use.

deprecated:  The entry is no longer in current use.

New registrations to either table MUST specify one of these values.

All existing entries, except as specified below, are to be noted as
"active" as of publication of this memo.

## 4.2. Update to Result Names

[AUTHRES] listed "hardfail" as the result to be used when a message
fails an [SPF] evaluation.  However, this latter specification used
the string "fail" to denote such failures.

Therefore, IANA has marked "hardfail" in the Email Authentication
Result Names registry as "deprecated" and amended the "fail" entry as
follows:

Code:  fail

Defined:  [AUTHRES]

Auth Method:  spf, sender-id

Meaning:  [this memo] Section 3

Status:  active

# 5. Security Considerations

This memo corrects a registry error.  It is possible that older
implementations will not recognize or use the corrected entry.  Thus,
implementers are advised to support both result strings for some
period of time.  However, it is known that some implementations are
already using the SPF-defined result string.

# 6. References

## 6.1. Normative References

[AUTHRES]    Kucherawy, M., "Message Header Field for Indicating
Message Authentication Status", RFC 5451, April 2009.

[ERR2617]    "RFC Errata", Errata ID 2617, RFC 5451,
<http://www.rfc-editor.org>.

[KEYWORDS]   Bradner, S., "Key words for use in RFCs to Indicate
Requirement Levels", BCP 14, RFC 2119, March 1997.

## 6.2. Informative References

[ERR2818]    "RFC Errata", Errata ID 2818, RFC 5451,
<http://www.rfc-editor.org>.

[IANA]       Narten, T. and H. Alvestrand, "Guidelines for Writing an
IANA Considerations Section in RFCs", BCP 26, RFC 5226,
May 2008.

[SENDER-ID]  Lyon, J. and M. Wong, "Sender ID: Authenticating
E-Mail", RFC 4406, April 2006.

[SPF]        Wong, M. and W. Schlitt, "Sender Policy Framework (SPF)
for Authorizing Use of Domains in E-Mail, Version 1",
RFC 4408, April 2006.

# Appendix A. Examples in RFC 5451

It should be noted that this update also applies to the examples in
[AUTHRES], specifically the one in Appendix B.5.  The error there
[ERR2818] is not corrected by this update, which only deals with the
normative portions of that specification and the related IANA
registrations.  However, it is assumed one could easily see what
needs to be corrected there.

Corrected examples will be included in a full update to [AUTHRES] at
some future time.

# Appendix B. Acknowledgements

The author wishes to acknowledge the following for their review and
constructive criticism of this proposal: S. Moonesamy, Scott
Kitterman.

# Author's Address

Murray S. Kucherawy
Cloudmark, Inc.
128 King St., 2nd Floor
San Francisco, CA  94107
US

Phone: +1 415 946 3800
EMail: msk@cloudmark.com
