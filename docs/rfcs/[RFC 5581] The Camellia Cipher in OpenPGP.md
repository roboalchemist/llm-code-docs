---
rfc: 5581
title: "The Camellia Cipher in OpenPGP"
date: June 2009
category: Informational
updates: [4880]
---

# Abstract

This document presents the necessary information to use the Camellia
symmetric block cipher in the OpenPGP protocol.

# Table of Contents

  - [1.  Introduction](#1-introduction)
  - [2.  Requirements Notation](#2-requirements-notation)
  - [3.  Camellia](#3-camellia)
  - [4.  Security Considerations](#4-security-considerations)
  - [5.  IANA Considerations](#5-iana-considerations)
  - [6.  Normative References](#6-normative-references)

# 1. Introduction

The OpenPGP protocol [RFC4880] can support many different symmetric
ciphers.  This document presents the necessary information to use the
Camellia [RFC3713] symmetric cipher in the OpenPGP protocol.

# 2. Requirements Notation

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT",
"SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this
document are to be interpreted as described in [RFC2119].

# 3. Camellia

Camellia is specified in [RFC3713].  It is a 128-bit symmetric block
cipher (as are AES and Twofish in OpenPGP) that supports 128-bit,
192-bit, and 256-bit keys.  This document defines the use of Camellia
in OpenPGP.

+---------------------+----------------------------------------+
| Camellia Key Length | OpenPGP Symmetric-Key Algorithm Number |
+---------------------+----------------------------------------+
|         128         |                   11                   |
|         192         |                   12                   |
|         256         |                   13                   |
+---------------------+----------------------------------------+

OpenPGP applications MAY implement Camellia.  If implemented,
Camellia may be used in any place in OpenPGP where a symmetric cipher
is usable, and it is subject to the same usage requirements (such as
its presence in the Preferred Symmetric Algorithms signature
subpacket) as the other symmetric ciphers in OpenPGP.

While the OpenPGP algorithm preferences system prevents
interoperability problems with public key encrypted messages, if
Camellia (or any other optional cipher) is used for encrypting
private keys, there could be interoperability problems when migrating
a private key from one system to another.  A similar issue can arise
when using an optional cipher for symmetrically encrypted messages,
as this OpenPGP message type does not use the algorithm preferences
system.  Those using optional ciphers in this manner should take care
they are using a cipher that their intended recipient can decrypt.

# 4. Security Considerations

At publication time, there are no known weak keys for Camellia, and
the Camellia algorithm is believed to be strong.  However, as with
any technology involving cryptography, implementers should check the

current literature, as well as the Camellia home page at
http://info.isl.ntt.co.jp/camellia/ to determine if Camellia has been
found to be vulnerable to attack.

# 5. IANA Considerations

IANA assigned three algorithm numbers from the registry of OpenPGP
Symmetric-Key Algorithms that was created by [RFC4880].

# 6. Normative References

[RFC2119]  Bradner, S., "Key words for use in RFCs to Indicate
Requirement Levels", BCP 14, RFC 2119, March 1997.

[RFC3713]  Matsui, M., Nakajima, J., and S. Moriai, "A Description of
the Camellia Encryption Algorithm", RFC 3713, April 2004.

[RFC4880]  Callas, J., Donnerhacke, L., Finney, H., Shaw, D., and R.
Thayer, "OpenPGP Message Format", RFC 4880, November 2007.

# Author's Address

David Shaw

EMail: dshaw@jabberwocky.com
