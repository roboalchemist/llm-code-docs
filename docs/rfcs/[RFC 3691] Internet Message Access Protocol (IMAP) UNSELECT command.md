---
title: "Internet Message Access Protocol (IMAP) UNSELECT command"
rfc: 3691
date: February 2004
category: Standards---


# Abstract

This document defines an UNSELECT command that can be used to close
the current mailbox in an Internet Message Access Protocol - version
4 (IMAP4) session without expunging it.  Certain types of IMAP
clients need to release resources associated with the selected
mailbox without selecting a different mailbox.  While IMAP4 provides
this functionality (via a SELECT command with a nonexistent mailbox
name or reselecting the same mailbox with EXAMINE command), a more
clean solution is desirable.

# Table of Contents

  - [1.  Introduction](#1-introduction)
  - [2.  UNSELECT command](#2-unselect-command)
  - [3.  Security Considerations](#3-security-considerations)
  - [4.  Formal Syntax](#4-formal-syntax)
  - [5.  IANA Considerations](#5-iana-considerations)
  - [6.  Acknowledgments](#6-acknowledgments)
  - [7.  Normative References](#7-normative-references)
  - [8.  Author's Address](#8-authors-address)
  - [9.  Full Copyright Statement](#9-full-copyright-statement)

# 1. Introduction

Certain types of IMAP clients need to release resources associated
with the selected mailbox without selecting a different mailbox.
While [IMAP4] provides this functionality (via a SELECT command with
a nonexistent mailbox name or reselecting the same mailbox with
EXAMINE command), a more clean solution is desirable.

[IMAP4] defines the CLOSE command that closes the selected mailbox as
well as permanently removes all messages with the \Deleted flag set.

However [IMAP4] lacks a command that simply closes the mailbox
without expunging it.  This document defines the UNSELECT command for
this purpose.

A server which supports this extension indicates this with a
capability name of "UNSELECT".

"C:" and "S:" in examples show lines sent by the client and server
respectively.

The keywords "MUST", "MUST NOT", "SHOULD", "SHOULD NOT", and "MAY" in
this document when typed in uppercase are to be interpreted as
defined in "Key words for use in RFCs to Indicate Requirement Levels"
[KEYWORDS].

# 2. UNSELECT Command

Arguments:  none

Responses:  no specific responses for this command

Result:     OK - unselect completed, now in authenticated state
BAD - no mailbox selected, or argument supplied but
none permitted

The UNSELECT command frees server's resources associated with the
selected mailbox and returns the server to the authenticated
state.  This command performs the same actions as CLOSE, except
that no messages are permanently removed from the currently
selected mailbox.

Example:    C: A341 UNSELECT
S: A341 OK Unselect completed

# 3. Security Considerations

It is believed that this extension doesn't raise any additional
security concerns not already discussed in [IMAP4].

# 4. Formal Syntax

The following syntax specification uses the Augmented Backus-Naur
Form (ABNF) notation as specified in [ABNF].  Non-terminals
referenced but not defined below are as defined by [IMAP4].

Except as noted otherwise, all alphabetic characters are case-
insensitive.  The use of upper or lower case characters to define
token strings is for editorial clarity only.  Implementations MUST
accept these strings in a case-insensitive fashion.

command-select  /= "UNSELECT"

# 5. IANA Considerations

IMAP4 capabilities are registered by publishing a standards track or
IESG approved experimental RFC.  The registry is currently located
at:

http://www.iana.org/assignments/imap4-capabilities

This document defines the UNSELECT IMAP capabilities.  IANA has added
this capability to the registry.

# 6. Acknowledgments

UNSELECT command was originally implemented by Tim Showalter in Cyrus
IMAP server.

Also, the author of the document would like to thank Vladimir Butenko
and Mark Crispin for reminding that UNSELECT has to be documented.
Also thanks to Simon Josefsson for pointing out that there are
multiple ways to implement UNSELECT.

# 7. Normative References

[KEYWORDS] Bradner, S., "Key words for use in RFCs to Indicate
Requirement Levels", BCP 14, RFC 2119, March 1997.

[IMAP4]    Crispin, M., "Internet Message Access Protocol - Version
4rev1", RFC 3501, March 2003.

[ABNF]     Crocker, D., Ed. and P. Overell, "Augmented BNF for Syntax
Specifications: ABNF", RFC 2234, November 1997.

# 8. Author's Address

Alexey Melnikov
Isode Limited
5 Castle Business Village
Hampton, Middlesex TW12 2BX

EMail: Alexey.Melnikov@isode.com
URI: http://www.melnikov.ca/

# 9. Full Copyright Statement

Copyright (C) The Internet Society (2004).  This document is subject
to the rights, licenses and restrictions contained in BCP 78 and
except as set forth therein, the authors retain all their rights.

This document and the information contained herein are provided on an
"AS IS" basis and THE CONTRIBUTOR, THE ORGANIZATION HE/SHE
REPRESENTS OR IS SPONSORED BY (IF ANY), THE INTERNET SOCIETY AND THE
INTERNET ENGINEERING TASK FORCE DISCLAIM ALL WARRANTIES, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO ANY WARRANTY THAT THE USE OF
THE INFORMATION HEREIN WILL NOT INFRINGE ANY RIGHTS OR ANY IMPLIED
WARRANTIES OF MERCHANTABILITY OR FITNESS FOR A PARTICULAR PURPOSE.

Intellectual Property

The IETF takes no position regarding the validity or scope of any
Intellectual Property Rights or other rights that might be claimed
to pertain to the implementation or use of the technology
described in this document or the extent to which any license
under such rights might or might not be available; nor does it
represent that it has made any independent effort to identify any
such rights.  Information on the procedures with respect to
rights in RFC documents can be found in BCP 78 and BCP 79.

Copies of IPR disclosures made to the IETF Secretariat and any
assurances of licenses to be made available, or the result of an
attempt made to obtain a general license or permission for the use
of such proprietary rights by implementers or users of this
specification can be obtained from the IETF on-line IPR repository
at http://www.ietf.org/ipr.

The IETF invites any interested party to bring to its attention
any copyrights, patents or patent applications, or other
proprietary rights that may cover technology that may be required
to implement this standard.  Please address the information to the
IETF at ietf-ipr@ietf.org.

Acknowledgement

Funding for the RFC Editor function is currently provided by the
Internet Society.
