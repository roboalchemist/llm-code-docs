# RDF 1.1 N-Quads - Extending N-Triples with context

**Source**: https://www.w3.org/TR/n-quads/

**Description**: Specification for N-Quads, an extension of N-Triples that adds the ability to represent RDF datasets with named graphs.

---

RDF 1.1 N-Quads

[![W3C](https://www.w3.org/Icons/w3c_home)](https://www.w3.org/)

## RDF 1.1 N-Quads

A line-based syntax for RDF datasets

## W3C Recommendation 25 February 2014

This version:
:   [http://www.w3.org/TR/2014/REC-n-quads-20140225/](https://www.w3.org/TR/2014/REC-n-quads-20140225/)

Latest published version:
:   [http://www.w3.org/TR/n-quads/](https://www.w3.org/TR/n-quads/)

Test suite:
:   [http://www.w3.org/TR/2014/NOTE-rdf11-testcases-20140225/](https://www.w3.org/TR/2014/NOTE-rdf11-testcases-20140225/)

Implementation report:
:   [http://www.w3.org/2013/N-QuadsReports/index.html](https://www.w3.org/2013/N-QuadsReports/index.html)

Previous version:
:   [http://www.w3.org/TR/2014/PR-n-quads-20140109/](https://www.w3.org/TR/2014/PR-n-quads-20140109/)

Editor:
:   Gavin Carothers, [Lex Machina, Inc](https://lexmachina.com/)

Please check the [**errata**](https://www.w3.org/2014/rdf1.1-errata) for any errors or issues
reported since publication.

The English version of this specification is the only normative version. Non-normative
[translations](https://www.w3.org/Consortium/Translation/) may also be available.

[Copyright](https://www.w3.org/Consortium/Legal/ipr-notice#Copyright) ©
2012-2014
[W3C](https://www.w3.org/)®
([MIT](http://www.csail.mit.edu/),
[ERCIM](http://www.ercim.eu/),
[Keio](http://www.keio.ac.jp/), [Beihang](http://ev.buaa.edu.cn/)),
All Rights Reserved.
W3C [liability](https://www.w3.org/Consortium/Legal/ipr-notice#Legal_Disclaimer),
[trademark](https://www.w3.org/Consortium/Legal/ipr-notice#W3C_Trademarks) and
[document use](https://www.w3.org/Consortium/Legal/copyright-documents)
rules apply.

---

## Abstract

N-Quads is a line-based, plain text format for encoding an RDF dataset.

## Status of This Document

*This section describes the status of this document at the time of its publication.
Other documents may supersede this document. A list of current W3C publications and the
latest revision of this technical report can be found in the [W3C technical reports index](https://www.w3.org/TR/) at
http://www.w3.org/TR/.*

This document is part of the RDF 1.1 document suit.
The N-Quads format is a line-based RDF syntax with a similar flavor as N-Triples
[[N-TRIPLES](#bib-N-TRIPLES)]. The main distinction is that N-Quads allows encoding
multiple graphs.

This document was published by the [RDF Working Group](https://www.w3.org/2011/rdf-wg/) as a Recommendation.
If you wish to make comments regarding this document, please send them to
[public-rdf-comments@w3.org](mailto:public-rdf-comments@w3.org)
([subscribe](mailto:public-rdf-comments-request@w3.org?subject=subscribe),
[archives](http://lists.w3.org/Archives/Public/public-rdf-comments/)).
All comments are welcome.

Please see the Working Group's [implementation
report](https://www.w3.org/2013/N-QuadsReports/index.html).

This document has been reviewed by W3C Members, by software developers, and by other W3C
groups and interested parties, and is endorsed by the Director as a W3C Recommendation.
It is a stable document and may be used as reference material or cited from another
document. W3C's role in making the Recommendation is to draw attention to the
specification and to promote its widespread deployment. This enhances the functionality
and interoperability of the Web.

This document was produced by a group operating under the
[5 February 2004 W3C Patent
Policy](https://www.w3.org/Consortium/Patent-Policy-20040205/).
W3C maintains a [public list of any patent
disclosures](https://www.w3.org/2004/01/pp-impl/46168/status)
made in connection with the deliverables of the group; that page also includes
instructions for disclosing a patent. An individual who has actual knowledge of a patent
which the individual believes contains
[Essential
Claim(s)](https://www.w3.org/Consortium/Patent-Policy-20040205/#def-essential) must disclose the information in accordance with
[section
6 of the W3C Patent Policy](https://www.w3.org/Consortium/Patent-Policy-20040205/#sec-Disclosure).

## Table of Contents

* [1. Introduction](#sec-intro)
* [2. N-Quads Language](#n-quads-language)
  * [2.1 Simple Statements](#simple-triples)
  * [2.2 IRIs](#sec-iri)
  * [2.3 RDF Literals](#sec-literals)
  * [2.4 RDF Blank Nodes](#BNodes)
* [3. Conformance](#conformance)
  * [3.1 Media Type and Content Encoding](#sec-mediatype)
    * [3.1.1 Other Media Types](#sec-other-media-types)
* [4. Grammar](#sec-grammar)
* [5. Parsing](#sec-parsing)
  * [5.1 RDF Term Constructors](#sec-parsing-terms)
  * [5.2 RDF Dataset Construction](#rdf-dataset-construction)
* [6. Acknowledgements](#section-ack)
* [A. Change Log](#sec-changes)
  * [A.1 Changes between Proposed Recommendation and Recommendation](#changes-between-proposed-recommendation-and-recommendation)
  * [A.2 Changes between Candidate Recommendation and Proposed Recommendation](#changes-between-candidate-recommendation-and-proposed-recommendation)
  * [A.3 Changes between Last Call Working Draft and Candidate Recommendation](#changes-between-last-call-working-draft-and-candidate-recommendation)
  * [A.4 Changes between publication as Note and Last Call Working Draft](#changes-between-publication-as-note-and-last-call-working-draft)
* [B. N-Quads Internet Media Type, File Extension and Macintosh File Type](#sec-mediaReg)
* [C. References](#references)
  * [C.1 Normative references](#normative-references)
  * [C.2 Informative references](#informative-references)

## 1. Introduction

This document defines N-Quads, an easy to parse, line-based,
concrete syntax for
[RDF Datasets](https://www.w3.org/TR/rdf11-concepts/#section-dataset)
[[RDF11-CONCEPTS](#bib-RDF11-CONCEPTS)].

N-quads statements are a sequence of RDF terms representing the subject, predicate, object and graph label of an RDF Triple and the graph it is part of in a dataset. These may be separated by white space (spaces `#x20` or tabs `#x9`). This sequence is terminated by a '`.`' and a new line (optional at the end of a document).

Example 1

1. N-Quads Language

-------------------

### 2.1 Simple Statements

The simplest statement is a sequence of (subject, predicate, object) terms forming an RDF triple and an optional blank node label or IRI labeling what graph in a dataset the triple belongs to, all are separated by whitespace and terminated by '`.`' after each statement.

Example 2

The graph label IRI can be omitted, in which case the triples are considered part of the default graph of the RDF dataset.

### 2.2 IRIs

[IRIs](https://www.w3.org/TR/rdf11-concepts/#dfn-iri) may be written only as absolute IRIs.
IRIs are enclosed in '<' and '>' and may contain numeric escape sequences (described below). For example `<http://example.org/#green-goblin>`.

### 2.3 RDF Literals

[Literals](https://www.w3.org/TR/rdf11-concepts/#dfn-literal) are used to identify values such as strings, numbers, dates.

Literals (Grammar production [Literal](#grammar-production-literal)) have a lexical form followed by a language tag, a datatype IRI, or neither.
The representation of the lexical form consists of an initial delimiter `"` (U+0022), a sequence of permitted characters or numeric escape sequence or string escape sequence, and a final delimiter. Literals may not contain the characters `"`, `LF`, or `CR`. In addition '`\`' (U+005C) may not appear in any quoted literal except as part of an escape sequence.
The corresponding [RDF lexical form](https://www.w3.org/TR/rdf11-concepts/#dfn-lexical-form) is the characters between the delimiters, after processing any escape sequences.
If present, the [language tag](https://www.w3.org/TR/rdf11-concepts/#dfn-language-tagged-string) is preceded by a '`@`' (U+0040).
If there is no language tag, there may be a [datatype IRI](https://www.w3.org/TR/rdf11-concepts/#dfn-datatype-iri), preceded by '`^^`' (U+005E U+005E). If there is no datatype IRI and no language tag, the datatype is `xsd:string`.

### 2.4 RDF Blank Nodes

[RDF blank nodes](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node) in N-Quads are expressed as `_:` followed by a blank node label which is a series of name characters.
The characters in the label are built upon [PN\_CHARS\_BASE](#grammar-production-PN_CHARS_BASE), liberalized as follows:

* The characters `_` and digits may appear anywhere in a blank node label.
* The character `.` may appear anywhere except the first or last character.
* The characters `-`, `U+00B7`, `U+0300` to `U+036F` and `U+203F` to `U+2040` are permitted anywhere except the first character.

A fresh RDF blank node is allocated for each unique blank node label in a document.
Repeated use of the same blank node label identifies the same RDF blank node.

Example 3

## 3. Conformance

As well as sections marked as non-normative, all authoring guidelines, diagrams, examples,
and notes in this specification are non-normative. Everything else in this specification is
normative.

The key words *MUST*, *MUST NOT*, *REQUIRED*, *SHOULD*, *SHOULD NOT*, *RECOMMENDED*, *MAY*,
and *OPTIONAL* in this specification are to be interpreted as described in [[RFC2119](#bib-RFC2119)].

This specification defines conformance criteria for:

* N-Quads documents
* N-Quads parsers

A conforming **N-Quads document** is a Unicode string that conforms to the grammar and additional constraints defined in [section 4. Grammar](#sec-grammar), starting with the [`nquadsDoc` production](#grammar-production-nquadsDoc). An N-Quad document serializes an RDF dataset.

Note

N-Quads documents do not provide a way of serializing empty graphs that may be part of an RDF dataset.

A conforming **N-Quads parser** is a system capable of reading N-Quads documents on behalf of an application. It makes the serialized RDF graph, as defined in [section 5. Parsing](#sec-parsing), available to the application, usually through some form of API.

The IRI that identifies the N-Quads language is: `http://www.w3.org/ns/formats/N-Quads`

### 3.1 Media Type and Content Encoding

The media type of N-Quads is `application/n-quads`.
The content encoding of N-Quads is always UTF-8.
See [N-Quads Media Type](#sec-mediaReg) for the media type
registration form.

#### 3.1.1 Other Media Types

The original specification,
[N-Quads: Extending N-Triples with Context](http://sw.deri.org/2008/07/n-quads/),
proposed the use of media type `text/x-nquads` with an encoding
using 7-bit US-ASCII.

## 4. Grammar

An N-Quads document is a Unicode[[UNICODE](#bib-UNICODE)] character string encoded in UTF-8.
Unicode code points only in the range U+0 to U+10FFFF inclusive are allowed.

White space (tab `U+0009` or space `U+0020`) is used to separate two terminals which would otherwise be (mis-)recognized as one terminal. White space is significant in the production [STRING\_LITERAL\_QUOTE](#grammar-production-STRING_LITERAL_QUOTE).

Comments in N-Quads take the form of '`#`', outside an `IRIREF` or `STRING_LITERAL_QUOTE`, and continue to the end of line (`EOL`) or end of file if there is no end of line after the comment marker. Comments are treated as white space.

The EBNF used here is defined in XML 1.0
[[EBNF-NOTATION](#bib-EBNF-NOTATION)].

Escape sequence rules are the same as Turtle
[[TURTLE](#bib-TURTLE)]. However, as only the [`STRING_LITERAL_QUOTE`](#grammar-production-STRING_LITERAL_QUOTE) production is allowed new lines in literals *MUST* be escaped.

|  |  |  |  |
| --- | --- | --- | --- |
| [1] | `nquadsDoc` | ::= | [statement](#grammar-production-statement)? ([EOL](#grammar-production-EOL) [statement](#grammar-production-statement))`*` [EOL](#grammar-production-EOL)? |
| [2] | `statement` | ::= | [subject](#grammar-production-subject) [predicate](#grammar-production-predicate) [object](#grammar-production-object) [graphLabel](#grammar-production-graphLabel)? '`.`' |
| [3] | `subject` | ::= | [IRIREF](#grammar-production-IRIREF) `|`  [BLANK\_NODE\_LABEL](#grammar-production-BLANK_NODE_LABEL) |
| [4] | `predicate` | ::= | [IRIREF](#grammar-production-IRIREF) |
| [5] | `object` | ::= | [IRIREF](#grammar-production-IRIREF) `|` [BLANK\_NODE\_LABEL](#grammar-production-BLANK_NODE_LABEL) `|`  [literal](#grammar-production-literal) |
| [6] | `graphLabel` | ::= | [IRIREF](#grammar-production-IRIREF) `|`  [BLANK\_NODE\_LABEL](#grammar-production-BLANK_NODE_LABEL) |
| [7] | `literal` | ::= | [STRING\_LITERAL\_QUOTE](#grammar-production-STRING_LITERAL_QUOTE) ('`^^`' [IRIREF](#grammar-production-IRIREF) `|`  [LANGTAG](#grammar-production-LANGTAG))? |
| Productions for terminals | | | |
| [144s] | `LANGTAG` | ::= | '`@`' [`a-zA-Z`]`+` ('`-`' [`a-zA-Z0-9`]`+`)`*` |
| [8] | `EOL` | ::= | [`#xD#xA`]`+` |
| [10] | `IRIREF` | ::= | '`<`' ([`` ^#x00-#x20<>"{}|^`\ ``]`|`[UCHAR](#grammar-production-UCHAR))`*`'`>`' |
| [11] | `STRING_LITERAL_QUOTE` | ::= | '`"`' ([`^#x22#x5C#xA#xD`] `|` [ECHAR](#grammar-production-ECHAR) `|`[UCHAR](#grammar-production-UCHAR))`*`'`"`' |
| [141s] | `BLANK_NODE_LABEL` | ::= | '`_:`' ([PN\_CHARS\_U](#grammar-production-PN_CHARS_U) `|`[`0-9`]) (([PN\_CHARS](#grammar-production-PN_CHARS)`|`'`.`')`*` [PN\_CHARS](#grammar-production-PN_CHARS))? |
| [12] | `UCHAR` | ::= | '`\u`' [HEX](#grammar-production-HEX) [HEX](#grammar-production-HEX) [HEX](#grammar-production-HEX) [HEX](#grammar-production-HEX) `|`'`\U`' [HEX](#grammar-production-HEX) [HEX](#grammar-production-HEX) [HEX](#grammar-production-HEX) [HEX](#grammar-production-HEX) [HEX](#grammar-production-HEX) [HEX](#grammar-production-HEX) [HEX](#grammar-production-HEX) [HEX](#grammar-production-HEX) |
| [153s] | `ECHAR` | ::= | '`\`' [`tbnrf"'\`] |
| [157s] | `PN_CHARS_BASE` | ::= | [`A-Z`] `|`[`a-z`]`|`[`#x00C0-#x00D6`]`|`[`#x00D8-#x00F6`]`|`[`#x00F8-#x02FF`]`|`[`#x0370-#x037D`]`|`[`#x037F-#x1FFF`]`|`[`#x200C-#x200D`]`|`[`#x2070-#x218F`]`|`[`#x2C00-#x2FEF`]`|`[`#x3001-#xD7FF`]`|`[`#xF900-#xFDCF`]`|`[`#xFDF0-#xFFFD`]`|`[`#x10000-#xEFFFF`] |
| [158s] | `PN_CHARS_U` | ::= | [PN\_CHARS\_BASE](#grammar-production-PN_CHARS_BASE) `|`'`_`'`|`'`:`' |
| [160s] | `PN_CHARS` | ::= | [PN\_CHARS\_U](#grammar-production-PN_CHARS_U) `|`'`-`'`|`[`0-9`]`|`  `#x00B7` `|`[`#x0300-#x036F`]`|`[`#x203F-#x2040`] |
| [162s] | `HEX` | ::= | [`0-9`] `|`[`A-F`]`|`[`a-f`] |

## 5. Parsing

Parsing N-Quads requires a state of one item:

* Map[string -> [blank node](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node)] `bnodeLabels` — A mapping from string to blank node.

### 5.1 RDF Term Constructors

This table maps productions and lexical tokens to `RDF terms` or components of `RDF terms` listed in [section 5. Parsing](#sec-parsing):

| production | type | procedure |
| --- | --- | --- |
| [IRIREF](#grammar-production-IRIREF) | [IRI](https://www.w3.org/TR/rdf11-concepts/#dfn-iri) | The characters between "<" and ">" are taken, with the escape sequences unescaped, to form the unicode string of the IRI. |
| [STRING\_LITERAL\_QUOTE](#grammar-production-STRING_LITERAL_QUOTE) | [lexical form](https://www.w3.org/TR/rdf11-concepts/#dfn-lexical-form) | The characters between the outermost '"'s are taken, with escape sequences unescaped, to form the unicode string of a lexical form. |
| [LANGTAG](#grammar-production-LANGTAG) | [language tag](https://www.w3.org/TR/rdf11-concepts/#dfn-language-tag) | The characters following the `@` form the unicode string of the language tag. |
| [literal](#grammar-production-literal) | [literal](https://www.w3.org/TR/rdf11-concepts/#dfn-literal) | The literal has a lexical form of the first rule argument,  `STRING_LITERAL_QUOTE`, and either a language tag of `LANGTAG` or a datatype IRI of `iri`, depending on which rule matched the input. If the `LANGTAG` rule matched, the datatype is `rdf:langString` and the language tag is `LANGTAG`. If neither a language tag nor a datatype IRI is provided, the literal has a datatype of `xsd:string`. |
| [BLANK\_NODE\_LABEL](#grammar-production-BLANK_NODE_LABEL) | [blank node](https://www.w3.org/TR/rdf11-concepts/#dfn-blank-node) | The string matching the second argument, `PN_LOCAL`, is a key in [bnodeLabels](#bnodeLabels). If there is no corresponding blank node in the map, one is allocated. |

### 5.2 RDF Dataset Construction

An N-Quads document defines an RDF dataset composed of RDF graphs composed of a set of RDF triples. The `statement` production produces a triple defined by the terms constructed for `subject`, `predicate` and `object`. This RDF triple is added to the graph labeled by the production `graphLabel`, if no `graphLabel` is present the triple is added to the RDF datasets default graph.

## 6. Acknowledgements

*This section is non-normative.*

The editor of the RDF 1.1 edition acknowledges valuable
contributions from Gregg Kellogg, Andy Seaborne, Eric
Prud'hommeaux, Dave Beckett, David Robillard, Gregory Williams,
Antoine Zimmermann, Sandro Hawke, Richard Cyganiak, Pat Hayes,
Henry S. Thompson, Bob Ferris, Henry Story, Andreas Harth, Lee
Feigenbaum, Peter Ansell, Evan Patton and David Booth.

This specification is a product of extensive deliberations by the
members of the RDF Working Group chaired by Guus Schreiber and David Wood. It draws upon the eariler specification in *[N-Quads: Extending N-Triples with Context](http://sw.deri.org/2008/07/n-quads/)*, edited by Richard Cyganiak, Andreas Harth, and Aidan Hogan.

## A. Change Log

### A.1 Changes between Proposed Recommendation and Recommendation

* [Bug in grammar rule [7]](http://lists.w3.org/Archives/Public/public-rdf-comments/2014Feb/0009.html) concerning language-typed literals fixed.
* Link to original N-Quads proposal included.

### A.2 Changes between Candidate Recommendation and Proposed Recommendation

* A normative reference to RDF Concepts was added.
* Informative note about `text/x-nquads` historical media type added.

### A.3 Changes between Last Call Working Draft and Candidate Recommendation

No substitutive changes.

### A.4 Changes between publication as Note and Last Call Working Draft

* White space rules defined outside of grammar, as in Turtle.
* Comment processing defined.
* Parsing is defined.
* Recommendation track, not a working group Note.

## B. N-Quads Internet Media Type, File Extension and Macintosh File Type

Contact:
:   Eric Prud'hommeaux

See also:
:   [How to Register a Media Type for a W3C Specification](https://www.w3.org/2002/06/registering-mediatype)
:   [Internet Media Type registration, consistency of use](https://www.w3.org/2001/tag/2002/0129-mime)  
    TAG Finding 3 June 2002 (Revised 4 September 2002)

The Internet Media Type / MIME Type for N-Quads is "application/n-quads".

It is recommended that N-Quads files have the extension ".nq" (all lowercase) on all platforms.

It is recommended that N-Quads files stored on Macintosh HFS file systems be given a file type of "TEXT".

This information that follows will be submitted to the IESG for review, approval, and registration with IANA.

Type name:
:   application

Subtype name:
:   n-quads

Required parameters:
:   None

Optional parameters:
:   None

Encoding considerations:
:   The syntax of N-Quads is expressed over code points in Unicode [[UNICODE](#bib-UNICODE)]. The encoding is always UTF-8 [[UTF-8](#bib-UTF-8)].
:   Unicode code points may also be expressed using an \uXXXX (U+0 to U+FFFF) or \UXXXXXXXX syntax (for U+10000 onwards) where X is a hexadecimal digit [0-9A-F]

Security considerations:
:   N-Quads is a general-purpose assertion language; applications may evaluate given data to infer more assertions or to dereference IRIs, invoking the security considerations of the scheme for that IRI. Note in particular, the privacy issues in [[RFC3023](#bib-RFC3023)] section 10 for HTTP IRIs. Data obtained from an inaccurate or malicious data source may lead to inaccurate or misleading conclusions, as well as the dereferencing of unintended IRIs. Care must be taken to align the trust in consulted resources with the sensitivity of the intended use of the data; inferences of potential medical treatments would likely require different trust than inferences for trip planning.
:   N-Quads is used to express arbitrary application data; security considerations will vary by domain of use. Security tools and protocols applicable to text (e.g. PGP encryption, MD5 sum validation, password-protected compression) may also be used on N-Quads documents. Security/privacy protocols must be imposed which reflect the sensitivity of the embedded information.
:   N-Quads can express data which is presented to the user, for example, RDF Schema labels. Application rendering strings retrieved from untrusted N-Quads documents must ensure that malignant strings may not be used to mislead the reader. The security considerations in the media type registration for XML ([[RFC3023](#bib-RFC3023)] section 10) provide additional guidance around the expression of arbitrary data and markup.
:   N-Quads uses IRIs as term identifiers. Applications interpreting data expressed in N-Quads should address the security issues of
    [Internationalized Resource Identifiers (IRIs)](http://www.ietf.org/rfc/rfc3987.txt) [[RFC3987](#bib-RFC3987)] Section 8, as well as
    [Uniform Resource Identifier (URI): Generic Syntax](http://www.ietf.org/rfc/rfc3986.txt) [[RFC3986](#bib-RFC3986)] Section 7.
:   Multiple IRIs may have the same appearance. Characters in different scripts may
    look similar (a Cyrillic "о" may appear similar to a Latin "o"). A character followed
    by combining characters may have the same visual representation as another character
    (LATIN SMALL LETTER E followed by COMBINING ACUTE ACCENT has the same visual representation
    as LATIN SMALL LETTER E WITH ACUTE).
    Any person or application that is writing or interpreting data in Turtle must take care to use the IRI that matches the intended semantics, and avoid IRIs that make look similar.
    Further information about matching of similar characters can be found
    in [Unicode Security
    Considerations](http://www.unicode.org/reports/tr36/) [[UNICODE-SECURITY](#bib-UNICODE-SECURITY)] and
    [Internationalized Resource
    Identifiers (IRIs)](http://www.ietf.org/rfc/rfc3987.txt) [[RFC3987](#bib-RFC3987)] Section 8.

Interoperability considerations:
:   There are no known interoperability issues.

Published specification:
:   This specification.

Applications which use this media type:
:   No widely deployed applications are known to use this media type. It may be used by some web services and clients consuming their data.

Additional information:

Magic number(s):
:   None.

File extension(s):
:   ".nq"

Macintosh file type code(s):
:   "TEXT"

Person & email address to contact for further information:
:   Eric Prud'hommeaux <eric@w3.org>

Intended usage:
:   COMMON

Restrictions on usage:
:   None

Author/Change controller:
:   The N-Quads specification is the product of the RDF WG. The W3C reserves change control over this specifications.

## C. References

### C.1 Normative references

[EBNF-NOTATION]
:   Tim Bray; Jean Paoli; C. M. Sperberg-McQueen; Eve Maler; François Yergeau. [EBNF Notation](https://www.w3.org/TR/REC-xml/#sec-notation) 26 November 2008. W3C Recommendation. URL: [http://www.w3.org/TR/REC-xml/#sec-notation](https://www.w3.org/TR/REC-xml/#sec-notation)

[RDF11-CONCEPTS]
:   Richard Cyganiak, David Wood, Markus Lanthaler. [RDF 1.1 Concepts and Abstract Syntax.](https://www.w3.org/TR/2014/REC-rdf11-concepts-20140225/) W3C Recommendation, 25 February 2014. URL: [http://www.w3.org/TR/2014/REC-rdf11-concepts-20140225/](https://www.w3.org/TR/2014/REC-rdf11-concepts-20140225/). The latest edition is available at [http://www.w3.org/TR/rdf11-concepts/](https://www.w3.org/TR/rdf11-concepts/)

[RFC2119]
:   S. Bradner. [Key words for use in RFCs to Indicate Requirement Levels.](http://www.ietf.org/rfc/rfc2119.txt) March 1997. Internet RFC 2119. URL: <http://www.ietf.org/rfc/rfc2119.txt>

[RFC3023]
:   M. Murata; S. St.Laurent; D. Kohn. [XML Media Types (RFC 3023)](http://www.ietf.org/rfc/rfc3023.txt). January 2001. RFC. URL: <http://www.ietf.org/rfc/rfc3023.txt>

[RFC3986]
:   T. Berners-Lee; R. Fielding; L. Masinter. [Uniform Resource Identifier (URI): Generic Syntax (RFC 3986)](http://www.ietf.org/rfc/rfc3986.txt). January 2005. RFC. URL: <http://www.ietf.org/rfc/rfc3986.txt>

[RFC3987]
:   M. Dürst; M. Suignard. [Internationalized Resource Identifiers (IRIs)](http://www.ietf.org/rfc/rfc3987.txt). January 2005. RFC. URL: <http://www.ietf.org/rfc/rfc3987.txt>

[UNICODE]
:   [The Unicode Standard](http://www.unicode.org/versions/latest/). URL: <http://www.unicode.org/versions/latest/>

[UTF-8]
:   F. Yergeau. [UTF-8, a transformation format of ISO 10646](http://www.ietf.org/rfc/rfc3629.txt). IETF RFC 3629. November 2003. URL: <http://www.ietf.org/rfc/rfc3629.txt>

### C.2 Informative references

[N-TRIPLES]
:   Gavin Carothers, Andy Seabourne. [RDF 1.1 N-Triples](https://www.w3.org/TR/2014/REC-n-triples-20140225/). W3C Recommendation, 25 February 2014. URL: [http://www.w3.org/TR/2014/REC-n-triples-20140225/](https://www.w3.org/TR/2014/REC-n-triples-20140225/). The latest edition is available at [http://www.w3.org/TR/n-triples/](https://www.w3.org/TR/n-triples/)

[TURTLE]
:   Eric Prud'hommeaux, Gavin Carothers. [RDF 1.1 Turtle: Terse RDF Triple Language.](https://www.w3.org/TR/2014/REC-turtle-20140225/) W3C Recommendation, 25 February 2014. URL: [http://www.w3.org/TR/2014/REC-turtle-20140225/](https://www.w3.org/TR/2014/REC-turtle-20140225/). The latest edition is available at [http://www.w3.org/TR/turtle/](https://www.w3.org/TR/turtle/)

[UNICODE-SECURITY]
:   Mark Davis; Michel Suignard. [Unicode Security Considerations](http://www.unicode.org/reports/tr36/). URL: <http://www.unicode.org/reports/tr36/>
