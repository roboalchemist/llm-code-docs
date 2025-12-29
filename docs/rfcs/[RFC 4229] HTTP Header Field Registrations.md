---
rfc: 4229
title: "HTTP Header Field Registrations"
date: December 2005
category: Informational
---

# Abstract

This document defines the initial contents of a permanent IANA
registry for HTTP header fields and a provisional repository for HTTP
header fields, per RFC 3864.

# Table of Contents

  - [1. Introduction](#1-introduction)
  - [2. Registration Templates](#2-registration-templates)
    - [2.1. Permanent HTTP Header Field Registrations](#21-permanent-http-header-field-registrations)
      - [2.1.1. Header field: A-IM](#211-header-field-a-im)
      - [2.1.2. Header field: Accept](#212-header-field-accept)
      - [2.1.3. Header field: Accept-Additions](#213-header-field-accept-additions)
      - [2.1.4. Header field: Accept-Charset](#214-header-field-accept-charset)
      - [2.1.5. Header field: Accept-Encoding](#215-header-field-accept-encoding)
      - [2.1.6. Header field: Accept-Features](#216-header-field-accept-features)
      - [2.1.7. Header field: Accept-Language](#217-header-field-accept-language)
      - [2.1.8. Header field: Accept-Ranges](#218-header-field-accept-ranges)
      - [2.1.9. Header field: Age](#219-header-field-age)
      - [2.1.10. Header field: Allow](#2110-header-field-allow)
      - [2.1.11. Header field: Alternates](#2111-header-field-alternates)
      - [2.1.12. Header field: Authentication-Info](#2112-header-field-authentication-info)
      - [2.1.13. Header field: Authorization](#2113-header-field-authorization)
      - [2.1.14. Header field: C-Ext](#2114-header-field-c-ext)
      - [2.1.15. Header field: C-Man](#2115-header-field-c-man)
      - [2.1.16. Header field: C-Opt](#2116-header-field-c-opt)
      - [2.1.17. Header field: C-PEP](#2117-header-field-c-pep)
      - [2.1.18. Header field: C-PEP-Info](#2118-header-field-c-pep-info)
      - [2.1.19. Header field: Cache-Control](#2119-header-field-cache-control)
      - [2.1.20. Header field: Connection](#2120-header-field-connection)
      - [2.1.21. Header field: Content-Base](#2121-header-field-content-base)
      - [2.1.22. Header field: Content-Disposition](#2122-header-field-content-disposition)
      - [2.1.23. Header field: Content-Encoding](#2123-header-field-content-encoding)
      - [2.1.24. Header field: Content-ID](#2124-header-field-content-id)
      - [2.1.25. Header field: Content-Language](#2125-header-field-content-language)
      - [2.1.26. Header field: Content-Length](#2126-header-field-content-length)
      - [2.1.27. Header field: Content-Location](#2127-header-field-content-location)
      - [2.1.28. Header field: Content-MD5](#2128-header-field-content-md5)
      - [2.1.29. Header field: Content-Range](#2129-header-field-content-range)
      - [2.1.30. Header field: Content-Script-Type](#2130-header-field-content-script-type)
      - [2.1.31. Header field: Content-Style-Type](#2131-header-field-content-style-type)
      - [2.1.32. Header field: Content-Type](#2132-header-field-content-type)
      - [2.1.33. Header field: Content-Version](#2133-header-field-content-version)
      - [2.1.34. Header field: Cookie](#2134-header-field-cookie)
      - [2.1.35. Header field: Cookie2](#2135-header-field-cookie2)
      - [2.1.36. Header field: DAV](#2136-header-field-dav)
      - [2.1.37. Header field: Date](#2137-header-field-date)
      - [2.1.38. Header field: Default-Style](#2138-header-field-default-style)
      - [2.1.39. Header field: Delta-Base](#2139-header-field-delta-base)
      - [2.1.40. Header field: Depth](#2140-header-field-depth)
      - [2.1.41. Header field: Derived-From](#2141-header-field-derived-from)
      - [2.1.42. Header field: Destination](#2142-header-field-destination)
      - [2.1.43. Header field: Differential-ID](#2143-header-field-differential-id)
      - [2.1.44. Header field: Digest](#2144-header-field-digest)
      - [2.1.45. Header field: ETag](#2145-header-field-etag)
      - [2.1.46. Header field: Expect](#2146-header-field-expect)
      - [2.1.47. Header field: Expires](#2147-header-field-expires)
      - [2.1.48. Header field: Ext](#2148-header-field-ext)
      - [2.1.49. Header field: From](#2149-header-field-from)
      - [2.1.50. Header field: GetProfile](#2150-header-field-getprofile)
      - [2.1.51. Header field: Host](#2151-header-field-host)
      - [2.1.52. Header field: IM](#2152-header-field-im)
      - [2.1.53. Header field: If](#2153-header-field-if)
      - [2.1.54. Header field: If-Match](#2154-header-field-if-match)
      - [2.1.55. Header field: If-Modified-Since](#2155-header-field-if-modified-since)
      - [2.1.56. Header field: If-None-Match](#2156-header-field-if-none-match)
      - [2.1.57. Header field: If-Range](#2157-header-field-if-range)
      - [2.1.58. Header field: If-Unmodified-Since](#2158-header-field-if-unmodified-since)
      - [2.1.59. Header field: Keep-Alive](#2159-header-field-keep-alive)
      - [2.1.60. Header field: Label](#2160-header-field-label)
      - [2.1.61. Header field: Last-Modified](#2161-header-field-last-modified)
      - [2.1.62. Header field: Link](#2162-header-field-link)
      - [2.1.63. Header field: Location](#2163-header-field-location)
      - [2.1.64. Header field: Lock-Token](#2164-header-field-lock-token)
      - [2.1.65. Header field: MIME-Version](#2165-header-field-mime-version)
      - [2.1.66. Header field: Man](#2166-header-field-man)
      - [2.1.67. Header field: Max-Forwards](#2167-header-field-max-forwards)
      - [2.1.68. Header field: Meter](#2168-header-field-meter)
      - [2.1.69. Header field: Negotiate](#2169-header-field-negotiate)
      - [2.1.70. Header field: Opt](#2170-header-field-opt)
      - [2.1.71. Header field: Ordering-Type](#2171-header-field-ordering-type)
      - [2.1.72. Header field: Overwrite](#2172-header-field-overwrite)
      - [2.1.73. Header field: P3P](#2173-header-field-p3p)
      - [2.1.74. Header field: PEP](#2174-header-field-pep)
      - [2.1.75. Header field: PICS-Label](#2175-header-field-pics-label)
      - [2.1.76. Header field: Pep-Info](#2176-header-field-pep-info)
      - [2.1.77. Header field: Position](#2177-header-field-position)
      - [2.1.78. Header field: Pragma](#2178-header-field-pragma)
      - [2.1.79. Header field: ProfileObject](#2179-header-field-profileobject)
      - [2.1.80. Header field: Protocol](#2180-header-field-protocol)
      - [2.1.81. Header field: Protocol-Info](#2181-header-field-protocol-info)
      - [2.1.82. Header field: Protocol-Query](#2182-header-field-protocol-query)
      - [2.1.83. Header field: Protocol-Request](#2183-header-field-protocol-request)
      - [2.1.84. Header field: Proxy-Authenticate](#2184-header-field-proxy-authenticate)
      - [2.1.85. Header field: Proxy-Authentication-Info](#2185-header-field-proxy-authentication-info)
      - [2.1.86. Header field: Proxy-Authorization](#2186-header-field-proxy-authorization)
      - [2.1.87. Header field: Proxy-Features](#2187-header-field-proxy-features)
      - [2.1.88. Header field: Proxy-Instruction](#2188-header-field-proxy-instruction)
      - [2.1.89. Header field: Public](#2189-header-field-public)
      - [2.1.90. Header field: Range](#2190-header-field-range)
      - [2.1.91. Header field: Referer](#2191-header-field-referer)
      - [2.1.92. Header field: Retry-After](#2192-header-field-retry-after)
      - [2.1.93. Header field: Safe](#2193-header-field-safe)
      - [2.1.94. Header field: Security-Scheme](#2194-header-field-security-scheme)
      - [2.1.95. Header field: Server](#2195-header-field-server)
      - [2.1.96. Header field: Set-Cookie](#2196-header-field-set-cookie)
      - [2.1.97. Header field: Set-Cookie2](#2197-header-field-set-cookie2)
      - [2.1.98. Header field: SetProfile](#2198-header-field-setprofile)
      - [2.1.99. Header field: SoapAction](#2199-header-field-soapaction)
      - [2.1.100. Header field: Status-URI](#21100-header-field-status-uri)
      - [2.1.101. Header field: Surrogate-Capability](#21101-header-field-surrogate-capability)
      - [2.1.102. Header field: Surrogate-Control](#21102-header-field-surrogate-control)
      - [2.1.103. Header field: TCN](#21103-header-field-tcn)
      - [2.1.104. Header field: TE](#21104-header-field-te)
      - [2.1.105. Header field: Timeout](#21105-header-field-timeout)
      - [2.1.106. Header field: Trailer](#21106-header-field-trailer)
      - [2.1.107. Header field: Transfer-Encoding](#21107-header-field-transfer-encoding)
      - [2.1.108. Header field: URI](#21108-header-field-uri)
      - [2.1.109. Header field: Upgrade](#21109-header-field-upgrade)
      - [2.1.110. Header field: User-Agent](#21110-header-field-user-agent)
      - [2.1.111. Header field: Variant-Vary](#21111-header-field-variant-vary)
      - [2.1.112. Header field: Vary](#21112-header-field-vary)
      - [2.1.113. Header field: Via](#21113-header-field-via)
      - [2.1.114. Header field: WWW-Authenticate](#21114-header-field-www-authenticate)
      - [2.1.115. Header field: Want-Digest](#21115-header-field-want-digest)
      - [2.1.116. Header field: Warning](#21116-header-field-warning)
    - [2.2. Provisional HTTP Header Field Submissions](#22-provisional-http-header-field-submissions)
      - [2.2.1. Header field: Compliance](#221-header-field-compliance)
      - [2.2.2. Header field: Content-Transfer-Encoding](#222-header-field-content-transfer-encoding)
      - [2.2.3. Header field: Cost](#223-header-field-cost)
      - [2.2.4. Header field: Message-ID](#224-header-field-message-id)
      - [2.2.5. Header field: Non-Compliance](#225-header-field-non-compliance)
      - [2.2.6. Header field: Optional](#226-header-field-optional)
      - [2.2.7. Header field: Resolution-Hint](#227-header-field-resolution-hint)
      - [2.2.8. Header field: Resolver-Location](#228-header-field-resolver-location)
      - [2.2.9. Header field: SubOK](#229-header-field-subok)
      - [2.2.10. Header field: Subst](#2210-header-field-subst)
      - [2.2.11. Header field: Title](#2211-header-field-title)
      - [2.2.12. Header field: UA-Color](#2212-header-field-ua-color)
      - [2.2.13. Header field: UA-Media](#2213-header-field-ua-media)
      - [2.2.14. Header field: UA-Pixels](#2214-header-field-ua-pixels)
      - [2.2.15. Header field: UA-Resolution](#2215-header-field-ua-resolution)
      - [2.2.16. Header field: UA-Windowpixels](#2216-header-field-ua-windowpixels)
      - [2.2.17. Header field: Version](#2217-header-field-version)
  - [3. IANA Considerations](#3-iana-considerations)
  - [4. Security Considerations](#4-security-considerations)
  - [5. Acknowledgements](#5-acknowledgements)
  - [6. Informative References](#6-informative-references)

# 1. Introduction

HTTP/1.0 [3] and HTTP/1.1 [11] define protocol constructs
(respectively, the HTTP-header and message-header BNF rules) that are
used as message headers.  These specifications also define a number
of HTTP headers themselves, and they provide for extension through
the use of new field-names.

This document defines the initial contents of an IANA registry that
catalogs permanent HTTP header field-names, and of an IANA repository
that catalogs provisional HTTP header field-names.  Both are operated
according to Registration Procedures for Message Header Fields [1].

Note that neither tracks the syntax or semantics of field-values.
Also, while some HTTP headers have different semantics depending on
their context (e.g., Cache-Control in requests and responses), both
registries consider the HTTP header field-name name space singular.

Also, some contact details listed may no longer be correct.

# 2. Registration Templates

Header field entries are summarized in tabular form for convenience
of reference and presented in full in the following sections.

## 2.1. Permanent HTTP Header Field Registrations

Header name             Protocol
-----------             --------
A-IM                      http
Accept                    http
Accept-Additions          http
Accept-Charset            http
Accept-Encoding           http
Accept-Features           http
Accept-Language           http
Accept-Ranges             http
Age                       http
Allow                     http
Alternates                http
Authentication-Info       http
Authorization             http
C-Ext                     http
C-Man                     http
C-Opt                     http
C-PEP                     http
C-PEP-Info                http
Cache-Control             http
Connection                http
Content-Base              http
Content-Disposition       http
Content-Encoding          http
Content-ID                http
Content-Language          http
Content-Length            http
Content-Location          http
Content-MD5               http
Content-Range             http
Content-Script-Type       http
Content-Style-Type        http
Content-Type              http
Content-Version           http
Cookie                    http
Cookie2                   http
DAV                       http
Date                      http
Default-Style             http
Delta-Base                http
Depth                     http
Derived-From              http
Destination               http
Differential-ID           http
Digest                    http

ETag                      http
Expect                    http
Expires                   http
Ext                       http
From                      http
GetProfile                http
Host                      http
IM                        http
If                        http
If-Match                  http
If-Modified-Since         http
If-None-Match             http
If-Range                  http
If-Unmodified-Since       http
Keep-Alive                http
Label                     http
Last-Modified             http
Link                      http
Location                  http
Lock-Token                http
MIME-Version              http
Man                       http
Max-Forwards              http
Meter                     http
Negotiate                 http
Opt                       http
Ordering-Type             http
Overwrite                 http
P3P                       http
PEP                       http
PICS-Label                http
Pep-Info                  http
Position                  http
Pragma                    http
ProfileObject             http
Protocol                  http
Protocol-Info             http
Protocol-Query            http
Protocol-Request          http
Proxy-Authenticate        http
Proxy-Authentication-Info http
Proxy-Authorization       http
Proxy-Features            http
Proxy-Instruction         http
Public                    http
Range                     http
Referer                   http
Retry-After               http

Safe                      http
Security-Scheme           http
Server                    http
Set-Cookie                http
Set-Cookie2               http
SetProfile                http
SoapAction                http
Status-URI                http
Surrogate-Capability      http
Surrogate-Control         http
TCN                       http
TE                        http
Timeout                   http
Trailer                   http
Transfer-Encoding         http
URI                       http
Upgrade                   http
User-Agent                http
Variant-Vary              http
Vary                      http
Via                       http
WWW-Authenticate          http
Want-Digest               http
Warning                   http

### 2.1.1. Header field: A-IM

Applicable protocol:     http [11]

Status: standard

Author/change controller:
IETF  (iesg@ietf.org)
Internet Engineering Task Force

Specification document(s):
RFC3229 [16]

### 2.1.2. Header field: Accept

Applicable protocol: http [11]

Status: standard

Author/change controller:
IETF  (iesg@ietf.org)
Internet Engineering Task Force

Specification document(s):
RFC2616 [11]

### 2.1.3. Header field: Accept-Additions

Applicable protocol: http [11]

Status: informational

Author/change controller:
IETF  (iesg@ietf.org)
Internet Engineering Task Force

Specification document(s):
RFC2324 [9]

Related information: spoof

### 2.1.4. Header field: Accept-Charset

Applicable protocol: http [11]

Status: standard

Author/change controller:
IETF  (iesg@ietf.org)
Internet Engineering Task Force

Specification document(s):
RFC2616 [11]

### 2.1.5. Header field: Accept-Encoding

Applicable protocol: http [11]

Status: standard

Author/change controller:
IETF  (iesg@ietf.org)
Internet Engineering Task Force

Specification document(s):
RFC2616 [11]

### 2.1.6. Header field: Accept-Features

Applicable protocol: http [11]

Status: experimental

Author/change controller:
Andrew H. Mutz  (mutz@hpl.hp.com)
Koen Holtman  (koen@win.tue.nl)

Specification document(s):
RFC2295 [7]

### 2.1.7. Header field: Accept-Language

Applicable protocol: http [11]

Status: standard

Author/change controller:
IETF  (iesg@ietf.org)
Internet Engineering Task Force

Specification document(s):
RFC2616 [11]

### 2.1.8. Header field: Accept-Ranges

Applicable protocol: http [11]

Status: standard

Author/change controller:
IETF  (iesg@ietf.org)
Internet Engineering Task Force

Specification document(s):
RFC2616 [11]

### 2.1.9. Header field: Age

Applicable protocol: http [11]

Status: standard

Author/change controller:
IETF  (iesg@ietf.org)
Internet Engineering Task Force

Specification document(s):
RFC2616 [11]

### 2.1.10. Header field: Allow

Applicable protocol: http [11]

Status: standard

Author/change controller:
IETF  (iesg@ietf.org)
Internet Engineering Task Force

Specification document(s):
RFC2616 [11]

### 2.1.11. Header field: Alternates

Applicable protocol: http [11]

Status: experimental

Author/change controller:
Andrew H. Mutz  (mutz@hpl.hp.com)
Koen Holtman  (koen@win.tue.nl)

Specification document(s):
RFC2295 [7]

### 2.1.12. Header field: Authentication-Info

Applicable protocol: http [11]

Status: standard

Author/change controller:
IETF  (iesg@ietf.org)
Internet Engineering Task Force

Specification document(s):
RFC2617 [12]

### 2.1.13. Header field: Authorization

Applicable protocol: http [11]

Status: standard

Author/change controller:
IETF  (iesg@ietf.org)
Internet Engineering Task Force

Specification document(s):
RFC2616 [11]

### 2.1.14. Header field: C-Ext

Applicable protocol: http [11]

Status: experimental

Author/change controller:
Henrik Frystyk Nielsen  (frystyk@microsoft.com)
Paul J. Leach  (paulle@microsoft.com)
Scott Lawrence  (lawrence@agranat.com)

Specification document(s):
RFC2774 [14]

### 2.1.15. Header field: C-Man

Applicable protocol: http [11]

Status: experimental

Author/change controller:
Henrik Frystyk Nielsen  (frystyk@microsoft.com)
Paul J. Leach  (paulle@microsoft.com)
Scott Lawrence  (lawrence@agranat.com)

Specification document(s):
RFC2774 [14]

### 2.1.16. Header field: C-Opt

Applicable protocol: http [11]

Status: experimental

Author/change controller:
Henrik Frystyk Nielsen  (frystyk@microsoft.com)
Paul J. Leach  (paulle@microsoft.com)
Scott Lawrence  (lawrence@agranat.com)

Specification document(s):
RFC2774 [14]

### 2.1.17. Header field: C-PEP

Applicable protocol: http [11]

Status: deprecated

Author/change controller:
Henrik Frystyk Nielsen  (frystyk@w3.org)
World Wide Web Consortium, MIT Laboratory for Computer Science
Dan Connolly  (connolly@w3.org)
World Wide Web Consortium, MIT Laboratory for Computer Science
Rohit Khare  (khare@w3.org)
World Wide Web Consortium, MIT Laboratory for Computer Science
Eric Prud'hommeaux  (eric@w3.org)
World Wide Web Consortium, MIT Laboratory for Computer Science

Specification document(s):
PEP [29]

### 2.1.18. Header field: C-PEP-Info

Applicable protocol: http [11]

Status: deprecated

Author/change controller:
Henrik Frystyk Nielsen  (frystyk@w3.org)
World Wide Web Consortium, MIT Laboratory for Computer Science
Dan Connolly  (connolly@w3.org)
World Wide Web Consortium, MIT Laboratory for Computer Science
Rohit Khare  (khare@w3.org)
World Wide Web Consortium, MIT Laboratory for Computer Science
Eric Prud'hommeaux  (eric@w3.org)
World Wide Web Consortium, MIT Laboratory for Computer Science

Specification document(s):
PEP [29]

### 2.1.19. Header field: Cache-Control

Applicable protocol: http [11]

Status: standard

Author/change controller:
IETF  (iesg@ietf.org)
Internet Engineering Task Force

Specification document(s):
RFC2616 [11]

### 2.1.20. Header field: Connection

Applicable protocol: http [11]

Status: standard

Author/change controller:
IETF  (iesg@ietf.org)
Internet Engineering Task Force

Specification document(s):
RFC2616 [11]

### 2.1.21. Header field: Content-Base

Applicable protocol: http [11]

Status: standard

Author/change controller:
IETF  (iesg@ietf.org)
Internet Engineering Task Force

Specification document(s):
RFC2068 [4]

### 2.1.22. Header field: Content-Disposition

Applicable protocol: http [11]

Status: standard

Author/change controller:
IETF  (iesg@ietf.org)
Internet Engineering Task Force

Specification document(s):
RFC2616 [11]

### 2.1.23. Header field: Content-Encoding

Applicable protocol: http [11]

Status: standard

Author/change controller:
IETF  (iesg@ietf.org)
Internet Engineering Task Force

Specification document(s):
RFC2616 [11]

### 2.1.24. Header field: Content-ID

Applicable protocol: http [11]

Status: informational

Author/change controller:
Arthur van Hoff  (avh@marimba.com)
Marimba Inc.
John Giannandrea  (jg@netscape.com)
Netscape Inc.
Mark Hapner  (mark.hapner@sun.com)
Sun Microsystems Inc.
Steve Carter  (srcarter@novell.com)
Novell Inc.
Milo Medin  (medin@home.net)
At Home Corp

Specification document(s):
DRP [20]

### 2.1.25. Header field: Content-Language

Applicable protocol: http [11]

Status: standard

Author/change controller:
IETF  (iesg@ietf.org)
Internet Engineering Task Force

Specification document(s):
RFC2616 [11]

### 2.1.26. Header field: Content-Length

Applicable protocol: http [11]

Status: standard

Author/change controller:
IETF  (iesg@ietf.org)
Internet Engineering Task Force

Specification document(s):
RFC2616 [11]

### 2.1.27. Header field: Content-Location

Applicable protocol: http [11]

Status: standard

Author/change controller:
IETF  (iesg@ietf.org)
Internet Engineering Task Force

Specification document(s):
RFC2616 [11]

### 2.1.28. Header field: Content-MD5

Applicable protocol: http [11]

Status: standard

Author/change controller:
IETF  (iesg@ietf.org)
Internet Engineering Task Force

Specification document(s):
RFC2616 [11]

### 2.1.29. Header field: Content-Range

Applicable protocol: http [11]

Status: standard

Author/change controller:
IETF  (iesg@ietf.org)
Internet Engineering Task Force

Specification document(s):
RFC2616 [11]

### 2.1.30. Header field: Content-Script-Type

Applicable protocol: http [11]

Status: standard

Author/change controller:
W3C  (web-human@w3.org)
World Wide Web Consortium

Specification document(s):
HTML 4 [21]

### 2.1.31. Header field: Content-Style-Type

Applicable protocol: http [11]

Status: standard

Author/change controller:
W3C  (web-human@w3.org)
World Wide Web Consortium

Specification document(s):
HTML 4 [21]

### 2.1.32. Header field: Content-Type

Applicable protocol: http [11]

Status: standard

Author/change controller:
IETF  (iesg@ietf.org)
Internet Engineering Task Force

Specification document(s):
RFC2616 [11]

### 2.1.33. Header field: Content-Version

Applicable protocol: http [11]

Status: standard

Author/change controller:
IETF  (iesg@ietf.org)
Internet Engineering Task Force

Specification document(s):
RFC2068 [4]

### 2.1.34. Header field: Cookie

Applicable protocol: http [11]

Status: standard

Author/change controller:
IETF  (iesg@ietf.org)
Internet Engineering Task Force

Specification document(s):
RFC2965 [15]

### 2.1.35. Header field: Cookie2

Applicable protocol: http [11]

Status: standard

Author/change controller:
IETF  (iesg@ietf.org)
Internet Engineering Task Force

Specification document(s):
RFC2965 [15]

### 2.1.36. Header field: DAV

Applicable protocol: http [11]

Status: standard

Author/change controller:
IETF  (iesg@ietf.org)
Internet Engineering Task Force

Specification document(s):
RFC2518 [10]

### 2.1.37. Header field: Date

Applicable protocol: http [11]

Status: standard

Author/change controller:
IETF  (iesg@ietf.org)
Internet Engineering Task Force

Specification document(s):
RFC2616 [11]

### 2.1.38. Header field: Default-Style

Applicable protocol: http [11]

Status: standard

Author/change controller:
W3C  (web-human@w3.org)
World Wide Web Consortium

Specification document(s):
HTML 4 [21]

### 2.1.39. Header field: Delta-Base

Applicable protocol: http [11]

Status: standard

Author/change controller:
IETF  (iesg@ietf.org)
Internet Engineering Task Force

Specification document(s):
RFC3229 [16]

### 2.1.40. Header field: Depth

Applicable protocol: http [11]

Status: standard

Author/change controller:
IETF  (iesg@ietf.org)
Internet Engineering Task Force

Specification document(s):
RFC2518 [10]

### 2.1.41. Header field: Derived-From

Applicable protocol: http [11]

Status: standard

Author/change controller:
IETF  (iesg@ietf.org)
Internet Engineering Task Force

Specification document(s):
RFC2068 [4]

### 2.1.42. Header field: Destination

Applicable protocol: http [11]

Status: standard

Author/change controller:
IETF  (iesg@ietf.org)
Internet Engineering Task Force

Specification document(s):
RFC2518 [10]

### 2.1.43. Header field: Differential-ID

Applicable protocol: http [11]

Status: informational

Author/change controller:
Arthur van Hoff  (avh@marimba.com)
Marimba Inc.
John Giannandrea  (jg@netscape.com)
Netscape Inc.
Mark Hapner  (mark.hapner@sun.com)
Sun Microsystems Inc.
Steve Carter  (srcarter@novell.com)
Novell Inc.
Milo Medin  (medin@home.net)
At Home Corp

Specification document(s):
DRP [20]

### 2.1.44. Header field: Digest

Applicable protocol: http [11]

Status: standard

Author/change controller:
IETF  (iesg@ietf.org)
Internet Engineering Task Force

Specification document(s):
RFC3230 [17]

### 2.1.45. Header field: ETag

Applicable protocol: http [11]

Status: standard

Author/change controller:
IETF  (iesg@ietf.org)
Internet Engineering Task Force

Specification document(s):
RFC2616 [11]

### 2.1.46. Header field: Expect

Applicable protocol: http [11]

Status: standard

Author/change controller:
IETF  (iesg@ietf.org)
Internet Engineering Task Force

Specification document(s):
RFC2616 [11]

### 2.1.47. Header field: Expires

Applicable protocol: http [11]

Status: standard

Author/change controller:
IETF  (iesg@ietf.org)
Internet Engineering Task Force

Specification document(s):
RFC2616 [11]

### 2.1.48. Header field: Ext

Applicable protocol: http [11]

Status: experimental

Author/change controller:
Henrik Frystyk Nielsen  (frystyk@microsoft.com)
Paul J. Leach  (paulle@microsoft.com)
Scott Lawrence  (lawrence@agranat.com)

Specification document(s):
RFC2774 [14]

### 2.1.49. Header field: From

Applicable protocol: http [11]

Status: standard

Author/change controller:
IETF  (iesg@ietf.org)
Internet Engineering Task Force

Specification document(s):
RFC2616 [11]

### 2.1.50. Header field: GetProfile

Applicable protocol: http [11]

Status: informational

Author/change controller:
Pat Hensley  (hensley@firefly.net)
FireFly Network, Inc.
Max Metral  (max@firefly.net)
FireFly Network, Inc.
Upendra Shardanand  (shard@firefly.net)
FireFly Network, Inc.
Donna Converse  (converse@netscape.com)
Netscape Communications
Mike Myers  (mmyers@verisign.com)
Verisign, Inc.

Specification document(s):
OPS over HTTP [22]

### 2.1.51. Header field: Host

Applicable protocol: http [11]

Status: standard

Author/change controller:
IETF  (iesg@ietf.org)
Internet Engineering Task Force

Specification document(s):
RFC2616 [11]

### 2.1.52. Header field: IM

Applicable protocol: http [11]

Status: standard

Author/change controller:
IETF  (iesg@ietf.org)
Internet Engineering Task Force

Specification document(s):
RFC3229 [16]

### 2.1.53. Header field: If

Applicable protocol: http [11]

Status: standard

Author/change controller:
IETF  (iesg@ietf.org)
Internet Engineering Task Force

Specification document(s):
RFC2518 [10]

### 2.1.54. Header field: If-Match

Applicable protocol: http [11]

Status: standard

Author/change controller:
IETF  (iesg@ietf.org)
Internet Engineering Task Force

Specification document(s):
RFC2616 [11]

### 2.1.55. Header field: If-Modified-Since

Applicable protocol: http [11]

Status: standard

Author/change controller:
IETF  (iesg@ietf.org)
Internet Engineering Task Force

Specification document(s):
RFC2616 [11]

### 2.1.56. Header field: If-None-Match

Applicable protocol: http [11]

Status: standard

Author/change controller:
IETF  (iesg@ietf.org)
Internet Engineering Task Force

Specification document(s):
RFC2616 [11]

### 2.1.57. Header field: If-Range

Applicable protocol: http [11]

Status: standard

Author/change controller:
IETF  (iesg@ietf.org)
Internet Engineering Task Force

Specification document(s):
RFC2616 [11]

### 2.1.58. Header field: If-Unmodified-Since

Applicable protocol: http [11]

Status: standard

Author/change controller:
IETF  (iesg@ietf.org)
Internet Engineering Task Force

Specification document(s):
RFC2616 [11]

### 2.1.59. Header field: Keep-Alive

Applicable protocol: http [11]

Status: standard

Author/change controller:
IETF  (iesg@ietf.org)
Internet Engineering Task Force

Specification document(s):
RFC2068 [4]

### 2.1.60. Header field: Label

Applicable protocol: http [11]

Status: standard

Author/change controller:
IETF  (iesg@ietf.org)
Internet Engineering Task Force

Specification document(s):
RFC3253 [18]

### 2.1.61. Header field: Last-Modified

Applicable protocol: http [11]

Status: standard

Author/change controller:
IETF  (iesg@ietf.org)
Internet Engineering Task Force

Specification document(s):
RFC2616 [11]

### 2.1.62. Header field: Link

Applicable protocol: http [11]

Status: standard

Author/change controller:
IETF  (iesg@ietf.org)
Internet Engineering Task Force

Specification document(s):
RFC2068 [4]

### 2.1.63. Header field: Location

Applicable protocol: http [11]

Status: standard

Author/change controller:
IETF  (iesg@ietf.org)
Internet Engineering Task Force

Specification document(s):
RFC2616 [11]

### 2.1.64. Header field: Lock-Token

Applicable protocol: http [11]

Status: standard

Author/change controller:
IETF  (iesg@ietf.org)
Internet Engineering Task Force

Specification document(s):
RFC2518 [10]

### 2.1.65. Header field: MIME-Version

Applicable protocol: http [11]

Status: standard

Author/change controller:
IETF  (iesg@ietf.org)
Internet Engineering Task Force

Specification document(s):
RFC2616 [11]

### 2.1.66. Header field: Man

Applicable protocol: http [11]

Status: experimental

Author/change controller:
Henrik Frystyk Nielsen  (frystyk@microsoft.com)
Paul J. Leach  (paulle@microsoft.com)
Scott Lawrence  (lawrence@agranat.com)

Specification document(s):
RFC2774 [14]

### 2.1.67. Header field: Max-Forwards

Applicable protocol: http [11]

Status: standard

Author/change controller:
IETF  (iesg@ietf.org)
Internet Engineering Task Force

Specification document(s):
RFC2616 [11]

### 2.1.68. Header field: Meter

Applicable protocol: http [11]

Status: standard

Author/change controller:
IETF  (iesg@ietf.org)
Internet Engineering Task Force

Specification document(s):
RFC2227 [6]

### 2.1.69. Header field: Negotiate

Applicable protocol: http [11]

Status: experimental

Author/change controller:
Andrew H. Mutz  (mutz@hpl.hp.com)
Koen Holtman  (koen@win.tue.nl)

Specification document(s):
RFC2295 [7]

### 2.1.70. Header field: Opt

Applicable protocol: http [11]

Status: experimental

Author/change controller:
Henrik Frystyk Nielsen  (frystyk@microsoft.com)
Paul J. Leach  (paulle@microsoft.com)
Scott Lawrence  (lawrence@agranat.com)

Specification document(s):
RFC2774 [14]

### 2.1.71. Header field: Ordering-Type

Applicable protocol: http [11]

Status: standard

Author/change controller:
IETF  (iesg@ietf.org)
Internet Engineering Task Force

Specification document(s):
RFC3648 [19]

### 2.1.72. Header field: Overwrite

Applicable protocol: http [11]

Status: standard

Author/change controller:
IETF  (iesg@ietf.org)
Internet Engineering Task Force

Specification document(s):
RFC2518 [10]

### 2.1.73. Header field: P3P

Applicable protocol: http [11]

Status: standard

Author/change controller:
W3C  (web-human@w3.org)
World Wide Web Consortium

Specification document(s):
P3P [23]

### 2.1.74. Header field: PEP

Applicable protocol: http [11]

Status: deprecated

Author/change controller:
Henrik Frystyk Nielsen  (frystyk@w3.org)
World Wide Web Consortium, MIT Laboratory for Computer Science
Dan Connolly  (connolly@w3.org)
World Wide Web Consortium, MIT Laboratory for Computer Science
Rohit Khare  (khare@w3.org)
World Wide Web Consortium, MIT Laboratory for Computer Science
Eric Prud'hommeaux  (eric@w3.org)
World Wide Web Consortium, MIT Laboratory for Computer Science

Specification document(s):
PEP [29]

### 2.1.75. Header field: PICS-Label

Applicable protocol: http [11]

Status: standard

Author/change controller:
W3C  (web-human@w3.org)
World Wide Web Consortium

Specification document(s):
PICSLabels [24]

### 2.1.76. Header field: Pep-Info

Applicable protocol: http [11]

Status: deprecated

Author/change controller:
Henrik Frystyk Nielsen  (frystyk@w3.org)
World Wide Web Consortium, MIT Laboratory for Computer Science
Dan Connolly  (connolly@w3.org)
World Wide Web Consortium, MIT Laboratory for Computer Science
Rohit Khare  (khare@w3.org)
World Wide Web Consortium, MIT Laboratory for Computer Science
Eric Prud'hommeaux  (eric@w3.org)
World Wide Web Consortium, MIT Laboratory for Computer Science

Specification document(s):  PEP [29]

### 2.1.77. Header field: Position

Applicable protocol: http [11]

Status: standard

Author/change controller:
IETF  (iesg@ietf.org)
Internet Engineering Task Force

Specification document(s):
RFC3648 [19]

### 2.1.78. Header field: Pragma

Applicable protocol: http [11]

Status: standard

Author/change controller:
IETF  (iesg@ietf.org)
Internet Engineering Task Force

Specification document(s):
RFC2616 [11]

### 2.1.79. Header field: ProfileObject

Applicable protocol: http [11]

Status: informational

Author/change controller:
Pat Hensley  (hensley@firefly.net)
FireFly Network, Inc.
Max Metral  (max@firefly.net)
FireFly Network, Inc.
Upendra Shardanand  (shard@firefly.net)
FireFly Network, Inc.
Donna Converse  (converse@netscape.com)
Netscape Communications
Mike Myers  (mmyers@verisign.com)
Verisign, Inc.

Specification document(s):
OPS over HTTP [22]

### 2.1.80. Header field: Protocol

Applicable protocol: http [11]

Status: standard

Author/change controller:
W3C  (web-human@w3.org)
World Wide Web Consortium

Specification document(s):
PICSLabels [24]

### 2.1.81. Header field: Protocol-Info

Applicable protocol: http [11]

Status: deprecated

Author/change controller:
Don Eastlake  (dee@cybercash.com)
Rohit Khare  (khare@w3.org)
Jim Miller  (jmiller@w3.org)

Specification document(s):
Selecting Payment Mechanisms [26]

### 2.1.82. Header field: Protocol-Query

Applicable protocol: http [11]

Status: deprecated

Author/change controller:
Don Eastlake  (dee@cybercash.com)
Rohit Khare  (khare@w3.org)
Jim Miller  (jmiller@w3.org)

Specification document(s):
Selecting Payment Mechanisms [26]

### 2.1.83. Header field: Protocol-Request

Applicable protocol: http [11]

Status: standard

Author/change controller:
W3C  (web-human@w3.org)
World Wide Web Consortium

Specification document(s):
PICSLabels [24]

### 2.1.84. Header field: Proxy-Authenticate

Applicable protocol: http [11]

Status: standard

Author/change controller:
IETF  (iesg@ietf.org)
Internet Engineering Task Force

Specification document(s):
RFC2616 [11]

### 2.1.85. Header field: Proxy-Authentication-Info

Applicable protocol: http [11]

Status: standard

Author/change controller:
IETF  (iesg@ietf.org)
Internet Engineering Task Force

Specification document(s):
RFC2617 [12]

### 2.1.86. Header field: Proxy-Authorization

Applicable protocol: http [11]

Status: standard

Author/change controller:
IETF  (iesg@ietf.org)
Internet Engineering Task Force

Specification document(s):
RFC2616 [11]

### 2.1.87. Header field: Proxy-Features

Applicable protocol: http [11]

Status: informational

Author/change controller:
Phillip M. Hallam-Baker  (hallam@w3.org)
W3C

Specification document(s):
Proxy Notification [27]

### 2.1.88. Header field: Proxy-Instruction

Applicable protocol: http [11]

Status: informational

Author/change controller:
Phillip M. Hallam-Baker  (hallam@w3.org)
W3C

Specification document(s):
Proxy Notification [27]

### 2.1.89. Header field: Public

Applicable protocol: http [11]

Status: standard

Author/change controller:
IETF  (iesg@ietf.org)
Internet Engineering Task Force

Specification document(s):
RFC2068 [4]

### 2.1.90. Header field: Range

Applicable protocol: http [11]

Status: standard

Author/change controller:
IETF  (iesg@ietf.org)
Internet Engineering Task Force

Specification document(s):
RFC2616 [11]

### 2.1.91. Header field: Referer

Applicable protocol: http [11]

Status: standard

Author/change controller:
IETF  (iesg@ietf.org)
Internet Engineering Task Force

Specification document(s):
RFC2616 [11]

### 2.1.92. Header field: Retry-After

Applicable protocol: http [11]

Status: standard

Author/change controller:
IETF  (iesg@ietf.org)
Internet Engineering Task Force

Specification document(s):
RFC2616 [11]

### 2.1.93. Header field: Safe

Applicable protocol: http [11]

Status: experimental

Author/change controller:
Koen Holtman  (koen@win.tue.nl)

Specification document(s):
RFC2310 [8]

### 2.1.94. Header field: Security-Scheme

Applicable protocol: http [11]

Status: experimental

Author/change controller:
Eric Rescorla  (ekr@rtfm.com)
A. Schiffman  (ams@terisa.com)

Specification document(s):
RFC2660 [13]

### 2.1.95. Header field: Server

Applicable protocol: http [11]

Status: standard

Author/change controller:
IETF  (iesg@ietf.org)
Internet Engineering Task Force

Specification document(s):
RFC2616 [11]

### 2.1.96. Header field: Set-Cookie

Applicable protocol: http [11]

Status: standard

Author/change controller:
IETF  (iesg@ietf.org)
Internet Engineering Task Force

Specification document(s):
RFC2109 [5]

### 2.1.97. Header field: Set-Cookie2

Applicable protocol: http [11]

Status: standard

Author/change controller:
IETF  (iesg@ietf.org)
Internet Engineering Task Force

Specification document(s):
RFC2965 [15]

### 2.1.98. Header field: SetProfile

Applicable protocol: http [11]

Status: informational

Author/change controller:
Pat Hensley  (hensley@firefly.net)
FireFly Network, Inc.
Max Metral  (max@firefly.net)
FireFly Network, Inc.
Upendra Shardanand  (shard@firefly.net)
FireFly Network, Inc.
Donna Converse  (converse@netscape.com)
Netscape Communications
Mike Myers  (mmyers@verisign.com)
Verisign, Inc.

Specification document(s):
OPS over HTTP [22]

### 2.1.99. Header field: SoapAction

Applicable protocol: http [11]

Status: informational

Author/change controller:
Don Box  (dbox@develop.com)
DevelopMentor
David Ehnebuske  (davide@us.ibm.com)
IBM
Gopal Kakivaya  (gopalk@microsoft.com)
Microsoft
Andrew Layman  (andrewl@microsoft.com)
Microsoft
Noah Mendelsohn  (Noah_Mendelsohn@lotus.com)
Lotus Development Corp.
Hernik Frystyk Nielsen  (frystyk@microsoft.com)
Microsoft
Satish Thatte  (satisht@microsoft.com)
Microsoft
Dave Winer  (dave@userland.com)
UserLand Software, Inc.

Specification document(s):
SOAP [28]

### 2.1.100. Header field: Status-URI

Applicable protocol: http [11]

Status: standard

Author/change controller:
IETF  (iesg@ietf.org)
Internet Engineering Task Force

Specification document(s):
RFC2518 [10]

### 2.1.101. Header field: Surrogate-Capability

Applicable protocol: http [11]

Status: informational

Author/change controller:
Mark Nottingham  (mnot@akamai.com)
Akamai
Xiang Liu  (xiang.liu@oracle.com)
Oracle

Specification document(s):
edge-arch [25]

### 2.1.102. Header field: Surrogate-Control

Applicable protocol: http [11]

Status: informational

Author/change controller:
Mark Nottingham  (mnot@akamai.com)
Akamai
Xiang Liu  (xiang.liu@oracle.com)
Oracle

Specification document(s):
edge-arch [25]

### 2.1.103. Header field: TCN

Applicable protocol: http [11]

Status: experimental

Author/change controller:
Andrew H. Mutz  (mutz@hpl.hp.com)
Koen Holtman  (koen@win.tue.nl)

Specification document(s):
RFC2295 [7]

### 2.1.104. Header field: TE

Applicable protocol: http [11]

Status: standard

Author/change controller:
IETF  (iesg@ietf.org)
Internet Engineering Task Force

Specification document(s):
RFC2616 [11]

### 2.1.105. Header field: Timeout

Applicable protocol: http [11]

Status: standard

Author/change controller:
IETF  (iesg@ietf.org)
Internet Engineering Task Force

Specification document(s):
RFC2518 [10]

### 2.1.106. Header field: Trailer

Applicable protocol: http [11]

Status: standard

Author/change controller:
IETF  (iesg@ietf.org)
Internet Engineering Task Force

Specification document(s):
RFC2616 [11]

### 2.1.107. Header field: Transfer-Encoding

Applicable protocol: http [11]

Status: standard

Author/change controller:
IETF  (iesg@ietf.org)
Internet Engineering Task Force

Specification document(s):
RFC2616 [11]

### 2.1.108. Header field: URI

Applicable protocol: http [11]

Status: standard

Author/change controller:
IETF  (iesg@ietf.org)
Internet Engineering Task Force

Specification document(s):
RFC2068 [4]

### 2.1.109. Header field: Upgrade

Applicable protocol: http [11]

Status: standard

Author/change controller:
IETF  (iesg@ietf.org)
Internet Engineering Task Force

Specification document(s):
RFC2616 [11]

### 2.1.110. Header field: User-Agent

Applicable protocol: http [11]

Status: standard

Author/change controller:
IETF  (iesg@ietf.org)
Internet Engineering Task Force

Specification document(s):
RFC2616 [11]

### 2.1.111. Header field: Variant-Vary

Applicable protocol: http [11]

Status: experimental

Author/change controller:
Andrew H. Mutz  (mutz@hpl.hp.com)
Koen Holtman  (koen@win.tue.nl)

Specification document(s):
RFC2295 [7]

### 2.1.112. Header field: Vary

Applicable protocol: http [11]

Status: standard

Author/change controller:
IETF  (iesg@ietf.org)
Internet Engineering Task Force

Specification document(s):
RFC2616 [11]

### 2.1.113. Header field: Via

Applicable protocol: http [11]

Status: standard

Author/change controller:
IETF  (iesg@ietf.org)
Internet Engineering Task Force

Specification document(s):
RFC2616 [11]

### 2.1.114. Header field: WWW-Authenticate

Applicable protocol: http [11]

Status: standard

Author/change controller:
IETF  (iesg@ietf.org)
Internet Engineering Task Force

Specification document(s):
RFC2616 [11]

### 2.1.115. Header field: Want-Digest

Applicable protocol: http [11]

Status: standard

Author/change controller:
IETF  (iesg@ietf.org)
Internet Engineering Task Force

Specification document(s):
RFC3230 [17]

### 2.1.116. Header field: Warning

Applicable protocol: http [11]

Status: standard

Author/change controller:
IETF  (iesg@ietf.org)
Internet Engineering Task Force

Specification document(s):
RFC2616 [11]

## 2.2. Provisional HTTP Header Field Submissions

Header name             Protocol
-----------             --------
Compliance                http
Content-Transfer-Encoding http
Cost                      http
Message-ID                http
Non-Compliance            http
Optional                  http
Resolution-Hint           http
Resolver-Location         http
SubOK                     http
Subst                     http
Title                     http
UA-Color                  http
UA-Media                  http
UA-Pixels                 http
UA-Resolution             http
UA-Windowpixels           http
Version                   http

### 2.2.1. Header field: Compliance

Applicable protocol: http [11]

Status: provisional

Author/change controller:  Jeffrey C. Mogul  (mogul@wrl.dec.com)
Western Research Laboratory, Digital Equipment Corporation Josh
Cohen  (josh@netscape.com) Netscape Communications Corporation
Scott Lawrence  (lawrence@agranat.com) Agranat Systems, Inc.

Specification document(s):
OPTIONS messages [31]

### 2.2.2. Header field: Content-Transfer-Encoding

Applicable protocol: http [11]

Status: provisional

Author/change controller:
Tim Berners-Lee  (timbl@w3.org)
MIT Laboratory for Computer Science

Specification document(s):
Object Headers [2]

### 2.2.3. Header field: Cost

Applicable protocol: http [11]

Status: provisional

Author/change controller:
Tim Berners-Lee  (timbl@w3.org)
MIT Laboratory for Computer Science

Specification document(s):
Object Headers [2]

### 2.2.4. Header field: Message-ID

Applicable protocol: http [11]

Status: provisional

Author/change controller:
Tim Berners-Lee  (timbl@w3.org)
MIT Laboratory for Computer Science

Specification document(s):
Object Headers [2]

### 2.2.5. Header field: Non-Compliance

Applicable protocol: http [11]

Status: provisional

Author/change controller:  Jeffrey C. Mogul  (mogul@wrl.dec.com)
Western Research Laboratory, Digital Equipment Corporation Josh
Cohen  (josh@netscape.com) Netscape Communications Corporation
Scott Lawrence  (lawrence@agranat.com) Agranat Systems, Inc.

Specification document(s):
OPTIONS messages [31]

### 2.2.6. Header field: Optional

Applicable protocol: http [11]

Status: provisional

Author/change controller:
John Mallery  (jcma@ai.mit.edu)
MIT Artificial Intelligence Laboratory
Lewis Girod  (girod@lcs.mit.edu)
MIT Laboratory for Computer Science
Benjie Chen  (benjie@lcs.mit.edu)
MIT Laboratory for Computer Science
Henrik Frystyk Nielsen  (frystyk@w3.org)
World Wide Web Consortium

Specification document(s):
WIRE [32]

### 2.2.7. Header field: Resolution-Hint

Applicable protocol: http [11]

Status: provisional

Author/change controller:
John Mallery  (jcma@ai.mit.edu)
MIT Artificial Intelligence Laboratory
Lewis Girod  (girod@lcs.mit.edu)
MIT Laboratory for Computer Science
Benjie Chen  (benjie@lcs.mit.edu)
MIT Laboratory for Computer Science
Henrik Frystyk Nielsen  (frystyk@w3.org)
World Wide Web Consortium

Specification document(s):
WIRE [32]

### 2.2.8. Header field: Resolver-Location

Applicable protocol: http [11]

Status: provisional

Author/change controller:
John Mallery  (jcma@ai.mit.edu)
MIT Artificial Intelligence Laboratory
Lewis Girod  (girod@lcs.mit.edu)
MIT Laboratory for Computer Science
Benjie Chen  (benjie@lcs.mit.edu)
MIT Laboratory for Computer Science
Henrik Frystyk Nielsen  (frystyk@w3.org)
World Wide Web Consortium

Specification document(s):
WIRE [32]

### 2.2.9. Header field: SubOK

Applicable protocol: http [11]

Status: provisional

Author/change controller:  Jeffrey C. Mogul  (mogul@wrl.dec.com)
Western Research Laboratory, Digital Equipment Corporation Arthur
van Hoff  (avh@marimba.com) Marimba, Inc.

Specification document(s):
Duplicate Suppression [33]

### 2.2.10. Header field: Subst

Applicable protocol: http [11]

Status: provisional

Author/change controller:  Jeffrey C. Mogul  (mogul@wrl.dec.com)
Western Research Laboratory, Digital Equipment Corporation Arthur
van Hoff  (avh@marimba.com) Marimba, Inc.

Specification document(s):
Duplicate Suppression [33]

### 2.2.11. Header field: Title

Applicable protocol: http [11]

Status: provisional

Author/change controller:
Tim Berners-Lee  (timbl@w3.org)
MIT Laboratory for Computer Science

Specification document(s):
Object Headers [2]

### 2.2.12. Header field: UA-Color

Applicable protocol: http [11]

Status: provisional

Author/change controller:
Larry Masinter  (LMM@acm.org)
Adobe Systems
Lou Montulli  (montulli@netscape.com)
Netscape Communications Corp.
Andrew H. Mutz  (mutz@hpl.hp.com)
Hewlett-Packard Company

Specification document(s):
UA Attributes [30]

### 2.2.13. Header field: UA-Media

Applicable protocol: http [11]

Status: provisional

Author/change controller:
Larry Masinter  (LMM@acm.org)
Adobe Systems
Lou Montulli  (montulli@netscape.com)
Netscape Communications Corp.
Andrew H. Mutz  (mutz@hpl.hp.com)
Hewlett-Packard Company

Specification document(s):
UA Attributes [30]

### 2.2.14. Header field: UA-Pixels

Applicable protocol: http [11]

Status: provisional

Author/change controller:
Larry Masinter  (LMM@acm.org)
Adobe Systems
Lou Montulli  (montulli@netscape.com)
Netscape Communications Corp.
Andrew H. Mutz  (mutz@hpl.hp.com)
Hewlett-Packard Company

Specification document(s):
UA Attributes [31]

### 2.2.15. Header field: UA-Resolution

Applicable protocol: http [11]

Status: provisional

Author/change controller:
Larry Masinter  (LMM@acm.org)
Adobe Systems
Lou Montulli  (montulli@netscape.com)
Netscape Communications Corp.
Andrew H. Mutz  (mutz@hpl.hp.com)
Hewlett-Packard Company

Specification document(s):
UA Attributes [30]

### 2.2.16. Header field: UA-Windowpixels

Applicable protocol: http [11]

Status: provisional

Author/change controller:
Larry Masinter  (LMM@acm.org)
Adobe Systems
Lou Montulli  (montulli@netscape.com)
Netscape Communications Corp.
Andrew H. Mutz  (mutz@hpl.hp.com)
Hewlett-Packard Company

Specification document(s):
UA Attributes [30]

### 2.2.17. Header field: Version

Applicable protocol: http [11]

Status: provisional

Author/change controller:
Tim Berners-Lee  (timbl@w3.org)
MIT Laboratory for Computer Science

Specification document(s):
Object Headers [2]

# 3. IANA Considerations

This specification provides initial registrations of HTTP header
fields in the "Permanent Message Header Field Registry", defined by
Registration Procedures for Message Header Fields [1].

It also provides initial submissions of HTTP header fields in the
"Provisional Message Header Field Repository", defined by the same
document.

# 4. Security Considerations

No security considerations are introduced by this document beyond
those already inherent in use of the HTTP header fields referenced.

# 5. Acknowledgements

The authors would like to thank Graham Klyne for his work in defining
the message header registries, his input and help in preparing this
document, and the registry generation software.

# 6. Informative References

[1]   Klyne, G., Nottingham, M., and J. Mogul, "Registration
Procedures for Message Header Fields", BCP 90, RFC 3864,
September 2004.

[2]   Berners-Lee, T., "Object Header lines in HTTP", May 1994,
<http://www.w3.org/Protocols/HTTP/Object_Headers.html>.

[3]   Berners-Lee, T., Fielding, R., and H. Nielsen, "Hypertext
Transfer Protocol -- HTTP/1.0", RFC 1945, May 1996.

[4]   Fielding, R., Gettys, J., Mogul, J., Nielsen, H., and T.
Berners-Lee, "Hypertext Transfer Protocol -- HTTP/1.1", RFC
2068, January 1997.

[5]   Kristol, D. and L. Montulli, "HTTP State Management Mechanism",
RFC 2109, February 1997.

[6]   Mogul, J. and P. Leach, "Simple Hit-Metering and Usage-Limiting
for HTTP", RFC 2227, October 1997.

[7]   Holtman, K. and A. Mutz, "Transparent Content Negotiation in
HTTP", RFC 2295, March 1998.

[8]   Holtman, K., "The Safe Response Header Field", RFC 2310, April
1998.

[9]   Masinter, L., "Hyper Text Coffee Pot Control Protocol
(HTCPCP/1.0)", RFC 2324, April 1998.

[10]  Goland, Y., Whitehead, E., Faizi, A., Carter, S., and D.
Jensen, "HTTP Extensions for Distributed Authoring -- WEBDAV",
RFC 2518, February 1999.

[11]  Fielding, R., Gettys, J., Mogul, J., Frystyk, H., Masinter, L.,
Leach, P., and T. Berners-Lee, "Hypertext Transfer Protocol --
HTTP/1.1", RFC 2616, June 1999.

[12]  Franks, J., Hallam-Baker, P., Hostetler, J., Lawrence, S.,
Leach, P., Luotonen, A., and L. Stewart, "HTTP Authentication:
Basic and Digest Access Authentication", RFC 2617, June 1999.

[13]  Rescorla, E. and A. Schiffman, "The Secure HyperText Transfer
Protocol", RFC 2660, August 1999.

[14]  Nielsen, H., Leach, P., and S. Lawrence, "An HTTP Extension
Framework", RFC 2774, February 2000.

[15]  Kristol, D. and L. Montulli, "HTTP State Management Mechanism",
RFC 2965, October 2000.

[16]  Mogul, J., Krishnamurthy, B., Douglis, F., Feldmann, A.,
Goland, Y., van Hoff, A., and D. Hellerstein, "Delta encoding
in HTTP", RFC 3229, January 2002.

[17]  Mogul, J. and A. Van Hoff, "Instance Digests in HTTP", RFC
3230, January 2002.

[18]  Clemm, G., Amsden, J., Ellison, T., Kaler, C., and J.
Whitehead, "Versioning Extensions to WebDAV (Web Distributed
Authoring and Versioning)", RFC 3253, March 2002.

[19]  Whitehead, J. and J. Reschke, Ed., "Web Distributed Authoring
and Versioning (WebDAV) Ordered Collections Protocol", RFC
3648, December 2003.

[20]  Hoff, A., Payne, J., Hapner, M., Carter, S., and M. Medin, "The
HTTP Distribution and Replication Protocol", W3C NOTE NOTE-
drp-19970825, August 1997.

[21]  Raggett, D., Hors, A., and I. Jacobs, "HTML 4.01
Specification", W3C REC REC-html401-19991224, December 1999.

[22]  Hensley, P., Metral, M., Shardanand, U., Converse, D., and M.
Myers, "Implementation of OPS Over HTTP", W3C NOTE NOTE-OPS-
OverHTTP, June 1997.

[23]  Marchiori, M., "The Platform for Privacy Preferences 1.0
(P3P1.0) Specification", W3C REC REC-P3P-20020416, April 2002.

[24]  Krauskopf, T., Miller, J., Resnick, P., and W. Treese, "PICS
1.1 Label Distribution -- Label Syntax and Communication
Protocols", W3C REC REC-PICS-labels-961031, October 1996.

[25]  Nottingham, M. and X. Liu, "Edge Architecture Specification",
W3C NOTE NOTE-edge-arch-20010804, August 2001.

[26]  Chung, E. and D. Dardailler, "White Paper: Joint Electronic
Payment Initiative", W3C NOTE NOTE-jepi-970519, May 1997.

[27]  Hallam-Baker, P., "Notification for Proxy Caches", W3C NOTE WD-
proxy-960221, February 1996.

[28]  Box, D., Ehnebuske, D., Kakivaya, G., Layman, A., Mendelsohn,
N., Nielsen, H., Thatte, S., and D. Winer, "Simple Object
Access Protocol (SOAP) 1.1", W3C NOTE NOTE-SOAP-20000508, May
2000.

[29]  Connolly, D., Prod'hommeaux, E., Nielsen, H., and R. Khare,
"PEP Specification: an Extension Mechanism for HTTP", Nov 1998,
<http://www.w3.org/TR/WD-http-pep>.

[30]  Masinter, L., Montulli, L., and A. Mutz, "User-Agent Display
Attributes Headers", Work in Progress, November 1996.

[31]  Mogul, J., Cohen, J., and S. Lawrence, "Specification of
HTTP/1.1 OPTIONS messages", Work in Progress, August 1997.

[32]  Girod, L., Chen, B., Henrik, H., and J. Mallery, "WIRE - W3
Identifier Resolution Extensions", Work in Progress, March
1998.

[33]  Mogul, J. and A. van Hoff, "Duplicate Suppression in HTTP",
Work in Progress, April 1998.

# Authors' Addresses

Mark Nottingham

EMail: mnot@pobox.com
URI:   http://www.mnot.net/

Jeffrey C. Mogul
HP Labs
1501 Page Mill Road
Palo Alto, CA  94304
US

EMail: JeffMogul@acm.org

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
this standard.  Please address the information to the IETF at ietf-
ipr@ietf.org.

Acknowledgement

Funding for the RFC Editor function is currently provided by the
Internet Society.
