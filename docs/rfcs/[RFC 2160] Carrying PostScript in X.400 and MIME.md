---
rfc: 2160
title: "Carrying PostScript in X.400 and MIME"
date: January 1998
category: Standards
---

# Table of Contents

  - [1 Introduction](#1-introduction)
  - [2 The PostScript body part](#2-the-postscript-body-part)
  - [3 The PostScript FTBP](#3-the-postscript-ftbp)
  - [4 The Application/PostScript content-type](#4-the-applicationpostscript-content-type)
  - [5 MIXER conversion](#5-mixer-conversion)
  - [6 MIXER conversion](#6-mixer-conversion)
  - [7 OID Assignments](#7-oid-assignments)
  - [8 Security Issues](#8-security-issues)
  - [9 Trademark Issues](#9-trademark-issues)
  - [10 References](#10-references)
  - [11 Author's Address](#11-authors-address)
  - [12 Full Copyright Statement](#12-full-copyright-statement)

# 1. Introduction

This document describes methods for carrying PostScript information
in the two standard mail systems MIME and X.400, and the conversion
between them. It uses the notational conventions of [BODYMAP], and
the conversion is further described in [MIXER].

Two ways of carrying PostScript in X.400 are described.  One is using
the FTAM Body Part, and one uses the Extended Body Part originally
described in RFC 1494.

The FTAM method is recommended.

RFC 2160         Carrying PostScript in X.400 and MIME      January 1998

# 2. The PostScript body part

Carrying PostScript in X.400 as an Extended Body Part was originally
defined in RFC 1494.  This specification carries that work forward
now that RFC 1494 is obsoleted by [BODYMAP].

The following Extended Body Part is defined for PostScript data
streams.  It has no parameters.

postscript-body-part EXTENDED-BODY-PART-TYPE
DATA             OCTET STRING
::= mime-postscript-body

mime-postscript-body OBJECT IDENTIFIER ::=

```
                { mixer-bp-data 2 }

```

# 3. The PostScript FTBP

The PostScript FTBP is identified by having the
FileTransferParameters.environment.application-reference set to id-
mime-ftbp-postscript.

The definition is:

id-mime-ftbp-postscript OBJECT IDENTIFIER ::=

```
                       { mixer-bp-data 6 }

```

# 4. The Application/PostScript content-type

In MIME, PostScript is carried in the body part
"application/PostScript", which is defined in RFC 1521.

# 5. MIXER conversion

X.400 Body Part: Extended Body Part, OID mime-postscript-body MIME
Content-Type: application/postscript Conversion Type: No conversion

The two representations of PostScript both contain a single stream of
octets. This stream of octets can be copied with no problems between
the representations. No other data needs to be converted.

# 6. MIXER conversion

X.400 Body Part: FTBP, OID mime-ftbp-postscript-body MIME Content-
Type: application/postscript Conversion Type: No conversion

RFC 2160         Carrying PostScript in X.400 and MIME      January 1998

The two representations of PostScript both contain a single stream of
octets. This stream of octets can be copied with no problems between
the representations. No other data needs to be converted.

# 7. OID Assignments

The first OID is also defined in [BODYMAP].

POSTSCRIPT-MAPPINGS DEFINITIONS ::= BEGIN
EXPORTS -- everything --;

IMPORTS
mixer-bp-data
FROM MIXER-MAPPINGS

id-mime-postscript-body OBJECT IDENTIFIER ::=

```
            { mixer-bp-data 2 };
    id-mime-ftbp-postscript OBJECT IDENTIFIER ::=
            { mixer-bp-data 6 };

    END

```

# 8. Security Issues

The issues concerning PostScript and security are well discussed in
RFC 2046.  No additional security issues are identified by this memo.

# 9. Trademark Issues

PostScript is a trademark of Adobe Systems, Inc.

# 10. References

[MIXER]
Kille, S., "MIXER: Mapping between X.400
and RFC 822/MIME", RFC 2156, January 1998.

[BODYMAP]
Alvestrand, H., "Mapping between X.400 and RFC 822/MIME
Message Bodies", RFC 2157, January 1998.

RFC 2160         Carrying PostScript in X.400 and MIME      January 1998

# 11. Author's Address

Harald Tveit Alvestrand
UNINETT
Postboks 6883 Elgeseter
N-7002 TRONDHEIM

Phone: +47 73 59 70 94
EMail: Harald.T.Alvestrand@uninett.no

RFC 2160         Carrying PostScript in X.400 and MIME      January 1998

# 12. Full Copyright Statement

Copyright (C) The Internet Society (1998).  All Rights Reserved.

This document and translations of it may be copied and furnished to
others, and derivative works that comment on or otherwise explain it
or assist in its implementation may be prepared, copied, published
and distributed, in whole or in part, without restriction of any
kind, provided that the above copyright notice and this paragraph are
included on all such copies and derivative works.  However, this
document itself may not be modified in any way, such as by removing
the copyright notice or references to the Internet Society or other
Internet organizations, except as needed for the purpose of
developing Internet standards in which case the procedures for
copyrights defined in the Internet Standards process must be
followed, or as required to translate it into languages other than
English.

The limited permissions granted above are perpetual and will not be
revoked by the Internet Society or its successors or assigns.

This document and the information contained herein is provided on an
"AS IS" basis and THE INTERNET SOCIETY AND THE INTERNET ENGINEERING
TASK FORCE DISCLAIMS ALL WARRANTIES, EXPRESS OR IMPLIED, INCLUDING
BUT NOT LIMITED TO ANY WARRANTY THAT THE USE OF THE INFORMATION
HEREIN WILL NOT INFRINGE ANY RIGHTS OR ANY IMPLIED WARRANTIES OF
MERCHANTABILITY OR FITNESS FOR A PARTICULAR PURPOSE.
