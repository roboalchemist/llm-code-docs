---
rfc: 5396
title: "Textual Representation of Autonomous System (AS) Numbers"
date: December 2008
category: Standards
---

# Abstract

A textual representation for Autonomous System (AS) numbers is
defined as the decimal value of the AS number.  This textual
representation is to be used by all documents, systems, and user
interfaces referring to AS numbers.

# Table of Contents

  - [1.  Introduction](#1-introduction)
  - [2.  Taxonomy of Representation Formats](#2-taxonomy-of-representation-formats)
  - [3.  Representation of AS Number Values](#3-representation-of-as-number-values)
  - [4.  IANA Considerations](#4-iana-considerations)
  - [5.  Security Considerations](#5-security-considerations)
  - [6.  Acknowledgments](#6-acknowledgments)
  - [7.  Informative References](#7-informative-references)

# 1. Introduction

A textual representation for Autonomous System (AS) numbers is
defined as the decimal value of the AS number.  This textual
representation is to be used by all documents, systems, and user
interfaces referring to AS numbers.

This document notes a number of potential representation formats and
proposes the adoption of a decimal value notation for AS numbers, or
"asplain" according to the representation taxonomy described here.

# 2. Taxonomy of Representation Formats

A taxonomy of representation for AS numbers is as follows:

asplain
refers to a syntax scheme of representing all AS numbers using
decimal integer notation.  Using asplain notation, an AS number of
value 65526 would be represented as the string "65526" and an AS
number of value 65546 would be represented as the string "65546".

asdot+
refers to a syntax scheme of representing all AS numbers using a
notation of two integer values joined by a period character: <high
order 16-bit value in decimal>.<low order 16-bit value in
decimal>.  Using asdot+ notation, an AS number of value 65526
would be represented as the string "0.65526" and an AS number of
value 65546 would be represented as the string "1.10".

asdot
refers to a syntax scheme of representing AS number values less
than 65536 using asplain notation and representing AS number
values equal to or greater than 65536 using asdot+ notation.
Using asdot notation, an AS number of value 65526 would be
represented as the string "65526" and an AS number of value 65546
would be represented as the string "1.10".

# 3. Representation of AS Number Values

To avoid confusion, a single textual notation is useful for
documentation, configuration systems, reports, and external tools and
information repositories.  The decimal value representation, or
"asplain" is proposed as the textual notation to use for AS numbers.

The "asplain" representation represents the number as its decimal
value, without any field delimiter, corresponding to the lack of any
internal structure required by the use of AS numbers in the inter-
domain routing context.

# 4. IANA Considerations

IANA Registries should use decimal representation ("asplain") for AS
numbers.

# 5. Security Considerations

This document does not refer to matters associated with security of
routing systems.

# 6. Acknowledgments

The terminology of "asplain", "asdot", and "asdot+" was originally
devised and described by Juergen Kammer in January 2007 [KAMMER2007].

# 7. Informative References

[KAMMER2007]  Kammer, J., "AS Number Formats", Jan 2007,
<http://quagga.ncc.eurodata.de/asnumformat.html>.

# Authors' Addresses

Geoff Huston
Asia Pacific Network Information Centre

EMail: gih@apnic.net

George Michaelson
Asia Pacific Network Information Centre

EMail: ggm@apnic.net
