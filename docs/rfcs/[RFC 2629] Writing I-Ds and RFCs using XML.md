---
rfc: 2629
title: "Writing I-Ds and RFCs using XML"
date: June 1999
category: Informational
---

# Abstract

This memo presents a technique for using XML (Extensible Markup
Language) as a source format for documents in the Internet-Drafts
(I-Ds) and Request for Comments (RFC) series.

# Table of Contents

  - [1.      Introduction](#1-introduction)
  - [2.      Using the DTD to Write I-Ds and RFCs](#2-using-the-dtd-to-write-i-ds-and-rfcs)
  - [2.1     XML basics](#21-xml-basics)
  - [2.2     Front matter](#22-front-matter)
  - [2.2.1   The title Element](#221-the-title-element)
  - [2.2.2   The author Element](#222-the-author-element)
  - [2.2.3   The date Element](#223-the-date-element)
  - [2.2.4   Meta Data Elements](#224-meta-data-elements)
  - [2.2.5   The abstract Element](#225-the-abstract-element)
  - [2.2.6   The note Element](#226-the-note-element)
  - [2.2.7   Status, Copyright Notice, Table of Contents](#227-status-copyright-notice-table-of-contents)
  - [2.2.7.1 Conformance with RFC 2026](#2271-conformance-with-rfc-2026)
  - [2.2.8   Everything in the Front](#228-everything-in-the-front)
  - [2.3     The Middle](#23-the-middle)
  - [2.3.1   The section Element](#231-the-section-element)
  - [2.3.1.1 The t Element](#2311-the-t-element)
  - [2.3.1.2 The list Element](#2312-the-list-element)
  - [2.3.1.3 The figure Element](#2313-the-figure-element)
  - [2.3.1.4 The xref Element](#2314-the-xref-element)
  - [2.3.1.5 The eref Element](#2315-the-eref-element)
  - [2.3.1.6 The iref Element](#2316-the-iref-element)
  - [2.3.1.7 The vspace Element](#2317-the-vspace-element)
  - [2.4     Back matter](#24-back-matter)
  - [2.4.1   The references Element](#241-the-references-element)
  - [2.4.2   Appendices](#242-appendices)
  - [2.4.3   Copyright Status](#243-copyright-status)
  - [3.      Processing the XML Source File](#3-processing-the-xml-source-file)
  - [3.1     Editing](#31-editing)
  - [3.1.1   Checking](#311-checking)
  - [3.2     Converting to Text Format](#32-converting-to-text-format)
  - [3.3     Converting to HTML Format](#33-converting-to-html-format)
  - [3.4     Viewing](#34-viewing)
  - [3.5     Searching](#35-searching)
  - [4.      Security Considerations](#4-security-considerations)
      - [References](#references)
      - [Author's Address](#authors-address)
  - [A.      The rfc Element](#a-the-rfc-element)
  - [B.      The RFC DTD](#b-the-rfc-dtd)
  - [C.      Acknowledgements](#c-acknowledgements)
  - [Index](#index)
  - [Full Copyright Statement](#full-copyright-statement)

# 1. Introduction

This memo describes how to write a document for the I-D and RFC
series using the Extensible Markup Language [1] (XML). This memo has
three goals:

1.  To describe a simple XML Document Type Definition (DTD) that is
powerful enough to handle the simple formatting requirements of
RFC-like documents whilst allowing for meaningful markup of
descriptive qualities.

2.  To describe software that processes XML source files, including a
tool that produces documents conforming to RFC 2223 [2], HTML
format, and so on.

3.  To provide the proof-of-concept for the first two goals (this
memo was written using this DTD and produced using that
software).

It is beyond the scope of this memo to discuss the political
ramifications of using XML as a source format for RFC-like documents.
Rather, it is simply noted that adding minimal markup to plain text:

o  allows the traditional production of textual RFC-like documents
using familiar editors;

o  requires some, albeit minimal, additions to existing software
environments; and,

o  permits information to be organized, searched, and retrieved using
both unstructured and structured mechanisms.

# 2. Using the DTD to Write I-Ds and RFCs

We do not provide a formal or comprehensive description of XML.
Rather, this section discusses just enough XML to use a Document Type
Declaration (DTD) to write RFC-like documents.

If you're already familiar with XML, skip to Appendix B to look at
the DTD.

## 2.1. XML basics

There are very few rules when writing in XML, as the syntax is
simple. There are five terms you'll need to know:

1.  An "element" usually refers to a start tag, an end tag, and all
the characters in between, e.g., "<example>text and/or nested
elements</example>"

2.  An "empty element" combines the start tag and the end tag, e.g.,
"<empty/>". You don't find these in HTML.

3.  An "attribute" is part of an element. If present, they occur in
the start tag, e.g., "<example name='value'>". Of course, they
can also appear in empty elements, e.g., "<empty name='value'/>".

4.  An "entity" is a textual macro that starts with "&". Don't worry
about these, you'll only use them whenever you want to put a "&"
or a "<" in your text.

5.  A "token" is a string of characters. The first character is
either a letter or an underscore ("_"). Any characters that
follow are either letters, numbers, an underscore, or a period
(".").

First, start your source file with an XML declaration, a reference to
the DTD, and the "rfc" element:

<?xml version="1.0"?>
<!DOCTYPE rfc SYSTEM "rfc2629.dtd">

```
       <rfc>
           ...
       </rfc>

   Ignore the first two lines -- the declaration and the reference --
   and simply treat them as opaque strings. Nothing else should be
   present after the "</rfc>" tag.

```

Second, make sure that all elements are properly matched and nested.

A properly matched element that starts with "<example>" is eventually
followed with "</example>". (Empty elements are always matched.)
Elements are properly nested when they don't overlap.

For example,

```
       <outer>
           ...
           <inner>
               ...
           </inner>
           ...
       </outer>

   is properly nested.

```

However,

```
       <outer>
           ...
           <inner>
               ...
           </outer>
           ...
       </inner>

   overlaps, so the elements aren't properly nested.

```

Third, never use "<" or "&" in your text. Instead, use either "&lt;"
or "&amp;", respectively.

Fourth, there are two quoting characters in XML, 'apostrophe' and
"quotation". Make sure that all attributes values are quoted, e.g.,
"<example name='value'>", If the value contains one of the quoting
characters, then use the other to quote the value, e.g., "<example
name='"'>", If the value contains both quoting characters, then use
one of them to quote the value, and replace occurrances of that
character in the attribute value with either '&apos;' (apostrophe) or
"&quot;" (quotation), e.g., "<example name='"&apos;"'>".

If you want to put a comment in your source file, here's the syntax:

<!-- comments can be multiline,
if you wish -->

Finally, XML is case sensitive.

## 2.2. Front matter

Immediately following the "<rfc>" tag is the "front" element:

<?xml version="1.0"?>
<!DOCTYPE rfc SYSTEM "rfc2629.dtd">

```
       <rfc>
           <front>
               <title ...>
               <author ...>
               <author ...>
               <date ...>
               <area ...>
               <workgroup ...>
               <keyword ...>
               <keyword ...>
               <abstract ...>
               <note ...>
           </front>
           ...
       </rfc>

   (Note that in all examples, indentation is used only for expository
   purposes.)

```

The "front" element consists of a "title" element, one or more
"author" elements, a "date" element, one or more optional "area"
elements, one or more optional "workgroup" elements, one or more
optional "keyword" elements, an optional "abstract" element. and, one
or more optional "note" elements.

### 2.2.1. The title Element

The "title" element identifies the title of the document. Because the
title will be used in the headers of the document when formatted
according to [2], if the title is more than 42 characters, then an
abbreviation should also be provided, e.g.,

```
       <title abbrev="Much Ado about Nothing">
```

The IETF's Discussion on "Source Format of RFC Documents"
</title>

### 2.2.2. The author Element

Each "author" element identifies a document author. Since a document
may have more than one author, more than one "author" element may be
present. If the author is a person, then three attributes must be
present in the "<author>" tag, "initials", "surname", and
"fullname", e.g.,

```
       <author initials="M.T." surname="Rose"
               fullname="Marshall T. Rose">

```

The "author" element itself consists of an "organization" element,
and, an optional "address" element.

The "organization" element is similar to the "title" element, in that
an abbreviation may be paired with a long organization name using the
"abbrev" attribute, e.g.,

```
       <organization abbrev="ISI">
           USC/Information Sciences Institute
       </organization>

```

The "address" element consists of an optional "postal" element, an
optional "phone" element, an optional "facsimile" element, an
optional "email" element, and, an optional "uri" element.

The "postal" element contains one or more "street" elements, followed
by any combination of "city", "region" (state or province), "code"
(zipcode or postal code), and "country" elements, e.g.,

```
       <postal>
           <street>660 York Street</street>
           <street>M/S 40</street>
           <city>San Francisco</city> <region>CA</region>
           <code>94110</code>
           <country>US</country>
       </postal>

```

This flexibility is provided to allow for different national formats
for postal addresses. Note however, that although the order of the
"city", "region", "code", and "country" elements isn't specified, at
most one of each may be present. Regardless, these elements must not
be re-ordered during processing by an XML application (e.g., display
applications must preserve the ordering of the information contained
in these elements). Finally, the value of the "country" element
should be a two-letter code from ISO 3166.

The "phone", "facsimile", "email", and "uri" elements are simple,
e.g.,

```
       <phone>+1 415 695 3975</phone>
       <email>mrose@not.invisible.net</email>
       <uri>http://invisible.net/</uri>

```

### 2.2.3. The date Element

The "date" element identifies the publication date of the document.
It consists of a month and a year, e.g.,

```
       <date month="February" year="1999" />

```

The "date" element also has an optional day attribute.

### 2.2.4. Meta Data Elements

The "front" element may contain meta data -- the content of these
elements does not appear in printed versions of the document.

A document has one or more optional "area", "workgroup" and "keyword"
elements, e.g.,

```
       <area>General</area>
       <workgroup>RFC Beautification Working Group</workgroup>
       <keyword>RFC</keyword>
       <keyword>Request for Comments</keyword>
       <keyword>I-D</keyword>
       <keyword>Internet-Draft</keyword>
       <keyword>XML</keyword>
       <keyword>Extensible Markup Language</keyword>

```

The "area" elements identify a general category for the document
(e.g., one of "Applications", "General", "Internet", "Management",
"Operations", "Routing", "Security", "Transport", or "User"), while
the "workgroup" elements identify the IETF working groups that
produced the document, and the "keyword" elements identify useful
search terms.

### 2.2.5. The abstract Element

A document may have an "abstract" element, which contains one or more
"t" elements (Section 2.3.1.1). In general, only a single "t" element
is present, e.g.,

```
       <abstract>
           <t>This memo presents a technique for using XML
           (Extensible Markup Language) as a source format
           for documents in the Internet-Drafts (I-Ds) and
```

Request for Comments (RFC) series.</t>
</abstract>

### 2.2.6. The note Element

A document may have one or more "note" elements, each of which
contains one or more "t" elements (Section 2.3.1.1). There is a
mandatory "title" attribute. In general, the "note" element contains
text from the IESG, e.g.,

```
       <note title="IESG Note">
           <t>The IESG has something to say.</t>
       </note>

```

### 2.2.7. Status, Copyright Notice, Table of Contents

Note that text relating to the memo's status, copyright notice, or
table of contents is not included in the document's markup -- this is
automatically inserted by an XML application when it produces either
a text or HTML version of the document.

#### 2.2.7.1. Conformance with RFC 2026

If an Internet-Draft is being produced, then the "ipr" attribute
should be present in the "<rfc>" tag at the beginning of the file.
The value of the attribute should be one of:

full2026: indicating that the document is in full conformance with
all the provisions of Section 10 of RFC 2026;

noDerivativeWorks2026: indicating that the document is in full
conformance with all the provisions of Section 10 of RFC 2026
except that the right to produce derivative works is not granted;
or,

none: indicating that the document is NOT offered in accordance with
Section 10 of RFC 2026, and the author does not provide the IETF
with any rights other than to publish as an Internet-Draft.

In the latter case, a copyright notice will not be automatically
inserted during processing by an XML application.

Consult [3] for further details.

Finally, if the Internet-Draft is being submitted to an automated
process, then the "docName" attribute should be present in the
"<rfc>" tag at the beginning of the file. The value of this attribute
contains the document (not file) name associated with this Internet-
Draft, e.g.,

```
       <rfc ipr="full" docName="draft-mrose-writing-rfcs-01">
           ...
       </rfc>

```

### 2.2.8. Everything in the Front

So, putting it all together, we have, e.g.,

```
       <front>
           <title>Writing I-Ds and RFCs using XML</title>

           <author initials="M.T." surname="Rose"
                   fullname="Marshall T. Rose">
               <organization>Invisible Worlds, Inc.</organization>

               <address>
                   <postal>
                       <street>660 York Street</street>
                       <street>M/S 40</street>
                       <city>San Francisco</city> <region>CA</region>
                       <code>94110</code>
                       <country>US</country>
                   </postal>

                   <phone>+1 415 695 3975</phone>
                   <email>mrose@not.invisible.net</email>
                   <uri>http://invisible.net/</uri>
               </address>
           </author>

           <date month="February" year="1999" />

           <area>General</area>
           <workgroup>RFC Beautification Working Group</workgroup>
           <keyword>RFC</keyword>
           <keyword>Request for Comments</keyword>
           <keyword>I-D</keyword>

           <keyword>Internet-Draft</keyword>
           <keyword>XML</keyword>
           <keyword>Extensible Markup Language</keyword>
           <abstract>
               <t>This memo presents a technique for using XML
               (Extensible Markup Language) as a source format
               for documents in the Internet-Drafts (I-Ds) and
```

Request for Comments (RFC) series.</t>
</abstract>
</front>

## 2.3. The Middle

The "middle" element contains all the sections of the document except
for the bibliography and appendices:

...
</front>

```
       <middle>
           <section ...>
           <section ...>
           <section ...>
       </middle>
       <back>
       ...

```

The "middle" element consists of one or more "section" elements.

### 2.3.1. The section Element

Each "section" element contains a section of the document. There is a
mandatory attribute, "title", that identifies the title of the
section. There is also an optional attribute, "anchor", that is used
for cross-referencing with the "xref" element (Section 2.3.1.4),
e.g.,

```
       <section anchor="intro" title="Introduction">
           ...
       </section>

```

The "section" element is recursive -- each contains any number and
combination of "t", "figure", and "section" elements, e.g.,

```
       <section title="The Middle">
           ...
           <section title="The section Element">
               ...
               <section title="The t Element">...</section>
               <section title="The list Element">...</section>
               <section title="The figure Element">...</section>
               <section title="The xref Element">...</section>
               <section title="The eref Element">...</section>
               <section title="The iref Element">...</section>
           </section>
       </section>

```

#### 2.3.1.1. The t Element

The "t" element contains any number and combination of paragraphs,
lists, and figures. If a cross-reference is needed to a section,
figure, or reference, the "xref" element (Section 2.3.1.4) is used;
similarly, if an external-reference is needed, the "eref" element
(Section 2.3.1.5) is used. Indexing of text is provided by the the
"iref" element (Section 2.3.1.6).

#### 2.3.1.2. The list Element

The "list" element contains one or more items. Each item is a "t"
element, allowing for recursion, e.g.,

```
       <list style="numbers">
           <t>The pfirst item.</t>
           <t>The second item, which contains two bulleted sub-items:
               <list style="symbols">
                   <t>The first sub-item.</t>
                   <t>The second sub-item.</t>
               </list>
           </t>
       </list>

```

The "list" element has an optional attribute, "style", having the
value "numbers" (for numeric lists), "symbols" (for bulleted lists),
"hanging" (for hanging lists), or, "empty" (for indented text). If a
"list" element is nested, the default value is taken from its closest
parent; otherwise, the default value is "empty".

When nested within a "hanging list" element, the "t" element has an
optional attribute, "hangText" that specifies the text to be
inserted, e.g.,

```
       <list style="hanging">
           <t hangText="full2026:">indicating that the document is in
           full conformance with all the provisions of Section 10 of RFC
           2026;</t>

           <t hangText="noDerivativeWorks2026:">indicating that the
           document is in full conformance with all the provisions of
           Section 10 of RFC 2026 except that the right to produce
           derivative works is not granted; or,</t>

           <t hangText="none:">indicating that the document is NOT
           offered in accordance with Section 10 of RFC 2026, and the
           author does not provide the IETF with any rights other than
           to publish as an Internet-Draft.</t>
       </list>

```

#### 2.3.1.3. The figure Element

The "figure" element groups an optional "preamble" element, an
"artwork" element, and an optional "postamble" element together. The
"figure" element also has an optional "anchor" attribute that is used
for cross-referencing with the "xref" element (Section 2.3.1.4).
There is also an optional "title" attribute that identifies the title
of the figure.

The "preamble" and "postamble" elements, if present, are simply text.
If a cross-reference is needed to a section, figure, or reference,
the "xref" element (Section 2.3.1.4) is used; similarly, if an
external-reference is needed, the "eref" element (Section 2.3.1.5) is
used. Indexing of text is provided by the the "iref" element (Section
2.3.1.6).

The "artwork" element, which must be present, contains "ASCII
artwork". Unlike text contained in the "t", "preamble", or
"postamble" elements, both horizontal and vertical whitespace is
significant in the "artwork" element.

So, putting it all together, we have, e.g.,

```
       <figure anchor="figure_example">
           <preamble>So,
           putting it all together, we have, e.g.,</preamble>
           <artwork>
               ascii artwork goes here...

               be sure to use "&lt;" or "&amp;" instead of "<" and "&",
               respectively!
           </artwork>
           <postamble>which is a very simple example.</postamble>
       </figure>

   which is a very simple example.

```

If you have artwork with a lot of "<" characters, then there's an XML
trick you can use:

```
       <figure>
           <preamble>If you have artwork with a lot of "&lt;"
           characters, then there's an XML trick you can
           use:</preamble>
           <artwork><![CDATA[
               ascii artwork goes here...

               just don't use "]]" in your artwork!
           ]]></artwork>
           <postamble>The "&lt;![CDATA[ ... ]]>" construct is called
           a CDATA block -- everything between the innermost brackets
           is left alone by the XML application.</postamble>
       </figure>

```

The "<![CDATA[ ... ]]>" construct is called a CDATA block --
everything between the innermost brackets is left alone by the XML
application.

Because the "figure" element represents a logical grouping of text
and artwork, an XML application producing a text version of the
document should attempt to keep these elements on the same page.
Because RFC 2223 [2] allows no more than 69 characters by 49 lines of
content on each page, XML applications should be prepared to
prematurely introduce page breaks to allow for better visual
grouping.

Finally, the "artwork" element has two optional attributes: "name"
and "type". The former is used to suggest a filename to use when
storing the content of the "artwork" element, whilst the latter
contains a suggestive data-typing for the content.

#### 2.3.1.4. The xref Element

The "xref" element is used to cross-reference sections, figures, and
references. The mandatory "target" attribute is used to link back to
the "anchor" attribute of the "section", "figure", and "reference"
elements. The value of the "anchor" and "target" attributes should be
formatted according to the token syntax in Section 2.1.

If used as an empty element, e.g.,

according to the token syntax in <xref target="xml_basics" />.

then the XML application inserts an appropriate phrase during
processing, such as "Section 2.1" or "<a href="#xml_basics">XML
Basics</a>".

If used with content, e.g.,

conforming to <xref target="refs.RFC2223">RFC 2223</xref>.

then the XML application inserts an appropriate designation during
processing, such as "RFC 2223 [2]" or "<a href="#refs.RFC2223">RFC
2223</a>". Although the XML application decides what "an appropriate
designation" might be, its choice is consistent throughout the
processing of the document.

#### 2.3.1.5. The eref Element

The "eref" element is used to reference external documents. The
mandatory "target" attribute is a URI [4], e.g.,

```
       <eref target="http://metalab.unc.edu/xml/">Cafe con Leche</eref>

```

Note that while the "target" attribute is always present, the "eref"
element may be empty, e.g.,

```
       <eref target="http://invisible.net/" />

   and the XML application inserts an appropriate designation during
   processing such as "[9]" or "<a
   href="http://invisible.net/">http://invisible.net/</a>".

```

#### 2.3.1.6. The iref Element

The "iref" element is used to add information to an index. The
mandatory "item" attribute is the primary key the information is
stored under, whilst the optional "subitem" attribute is the
secondary key, e.g.,

```
       <iref item="indexing" subitem="how to" />

```

Finally, note that the "iref" element is always empty -- it never
contains any text.

#### 2.3.1.7. The vspace Element

The "vspace" element, which may occur only inside the "t" element, is
used by the author to provide formatting guidance to the XML
application. There is an attribute, "blankLines", that indicates the
number of blank lines that should be inserted. A physical linebreak
is specified by using the default value, "0".

In addition, the "vspace" element can be used to force a new physical
paragraph within a list item, e.g.,

```
       <list style="numbers">
           <t>This is list item.
              <vspace blankLines="1" />
```

This is part of the same list item,
although when displayed, it appears
as a separate physical paragraph.</t>
</list>

An XML application producing a text version of the document should
exercise care when encountering a value for "blankLines" that causes
a pagebreak -- in particular, if a "vspace" element causes a
pagebreak, then no further blank lines should be inserted. This
allows authors to "force" a pagebreak by using an arbitrarily large
value, e.g., "blankLines='100'".

Finally, note that the "vspace" element is always empty -- it never
contains any text.

## 2.4. Back matter

Finally, the "back" element is used for references and appendices:

...
</middle>

```
           <back>
               <references>
                   <reference ...>
                   <reference ...>
               </references>
               <section ...>
               <section ...>
           </back>
       </rfc>

```

The "back" element consists of an optional "references" element, and,
one or more optional "section" elements. The "back" element itself is
optional, if your document doesn't have any references or appendices,
you don't have to include it.

### 2.4.1. The references Element

The "references" element contains the document's bibliography. It
contains one or more "reference" elements.

Each "reference" element contains a "front" element and one or more
optional "seriesInfo" elements.

We've already discussed the "front" element back in Section 2.2.

The "seriesInfo" element has two attributes, "name" and "value" that
identify the document series and series entry, respectively.

The "reference" element has an optional "anchor" attribute that is
used for cross-referencing with the "xref" element (Section 2.3.1.4),
e.g.,

```
       <reference anchor="refs.RFC2200">
           <front>
               <title>Internet Official Protocol Standards</title>
               <author initials="J." surname="Postel"
                       fullname="Jon Postel">
                   <organization abbrev="ISI">
                   USC/Information Sciences Institute
                   </organization>
               </author>

               <date month="June" year="1997" />
           </front>
           <seriesInfo name="RFC" value="2200" />
           <seriesInfo name="STD" value="1" />
       </reference>

```

The "reference" element also has an optional "target" attribute that
is used for external references (c.f., Section 2.3.1.5). The XML
application, if producing an HTML version of the document will use
the "target" attribute accordingly; however, if the "name" attribute
of the "seriesInfo" element has the value "RFC", then the XML
application should automatically provide an appropriate default for
the "target" attribute (e.g., "http://example.com/rfcs/rfc2200.txt").

### 2.4.2. Appendices

To include appendices after the bibliography, simply add more
"section" elements. (For an example, look at the example at the
beginning of Section 2.4.)

### 2.4.3. Copyright Status

The copyright status for the document is not included in the
document's markup -- this is automatically inserted by an XML
application that produces either a text or HTML version of the
document.

# 3. Processing the XML Source File

This section concerns itself with applications that operate on an XML
source file. A lot of XML tools are available, as are many lists of
XML resources, e.g., Cafe con Leche [5].

There are two kinds of XML tools: validating and non-validating.
Both check that the source file conforms to the rules given in
Section 2.1. However, in addition to making sure that the source file
is well-formed, a validating tool also reads the DTD referenced by
the source file to make sure that they match. There are a number of
both validating and non-validating tools available.

## 3.1. Editing

There are several XML editors available. Ideally, you want an editor
that validates. This has two advantages:

o  the editor provides guidance in fleshing-out the document
structure; and,

o  the editor validates that the source file matches the rules in the
DTD.

There are two major modes in Emacs that support XML: tdtd [6] and
psgml [7]. The latter mode allows you to validate the source file (by
calling an external program). If you visit the source file in Emacs
and the major mode isn't "SGML" or "XML", then usually all it takes
is adding these lines to your ".emacs" file:

(setq auto-mode-alist
(cons (cons "\\.xml$" 'sgml-mode) auto-mode-alist))

and then restarting Emacs. If this doesn't work, try one of the
sources above.

The author uses both sgml-mode in Emacs, and a commercial validating
editor, Clip! version 1.5 [8], when editing source files.

### 3.1.1. Checking

If your editor doesn't validate, then you should run a program to
validate the source file.

The author uses the AlphaWorks XML parser [9] for this purpose. It
requires that your system have a Java virtual machine. In addition to
Java, there are validating parsers written in C, Perl, Python, and
Tcl.

## 3.2. Converting to Text Format

The author has written the xml2rfc tool [10], which reads the source
file and produces both a text and HTML version of the document.
(This memo was produced using the xml2rfc tool.) Note that xml2rfc
isn't a validating tool, so it's a good idea to use either a
validating editor or run a stand-alone validating parser prior to
using the tool.

## 3.3. Converting to HTML Format

The XML Style Language (XSL) is used to describe transformations from
the source file into some other structured file. So, ideally you
should use an XSL-capable formatter to convert an XML source file to
HTML.

However, as of this writing XSL is still in considerable flux.
(Hence, no reference was included in this memo, as by the time you
read this section, the reference would be outdated.) So, in the
interim, the author uses the xml2rfc tool for this purpose, even
though this tool doesn't provide much flexibility in its HTML layout.

## 3.4. Viewing

Browsers that support either XSL or Cascading Style Sheets (CSS) are
able to view the source file directly.

At present, the author doesn't use any of these browsers, instead
converting source files to either text or HTML.

## 3.5. Searching

As with text editors, any text-oriented search tool (e.g., grep) can
be used on the source file. However, there are search tools available
that understand structured source.

The author uses sgrep version 1.9 [11] for this purpose, e.g.

sgrep -g xml 'ELEMENTS("title") not in ELEMENTS("back")' \
writing-rfcs.xml

which extracts the title element from the source file.

# 4. Security Considerations

This memo raises no security issues; however, according to [2], your
document should contain a section near the end that discusses the
security considerations of the protocol or procedures that are the
main topic of your document, e.g.,

```
       <middle>
           ...
           <section title="Security Considerations">
               <t>This memo raises no security issues;
               however,
               according to <xref target="refs.RFC2223" />,
               your document should contain a section near the end
               that discusses the security considerations of the
               protocol or procedures that are the main topic of your
               document.</t>
           </section>
       </middle>

```

# References

[1]  World Wide Web Consortium, "Extensible Markup Language (XML)
1.0", W3C XML, February 1998.

[2]  Postel, J. and J. Reynolds, "Instructions to RFC Authors", RFC
2223, October 1997.

[3]  Bradner, S., "The Internet Standards Process -- Revision 3", BCP
9, RFC 2026, October 1996.

[4]  Berners-Lee, T., Fielding, R. and L. Masinter, "Uniform Resource
Identifiers (URI): Generic Syntax", RFC 2396, August 1998.

[5]  http://metalab.unc.edu/xml/

[6]  http://www.mulberrytech.com/tdtd/

[7]  http://www.inria.fr/koala/plh/sxml.html

[8]  http://www.t2000-usa.com/

[9]  http://www.alphaworks.ibm.com/formula/xml/

[10]  http://memory.palace.org/authoring/

[11]  http://www.cs.helsinki.fi/~jjaakkol/sgrep.html

# Author's Address

Marshall T. Rose
Invisible Worlds, Inc.
660 York Street
San Francisco, CA  94110
US

Phone: +1 415 695 3975
EMail: mrose@not.invisible.net
URI:   http://invisible.net/

# Appendix A. The rfc Element

The "<rfc>" tag at the beginning of the file, with only an "ipr"
attribute (Section 2.2.7.1), produces an Internet-Draft. However,
when other attributes are added to this tag by the RFC editor, an RFC
is produced, e.g.,

```
       <rfc number="2200"
            obsoletes="2000, 1920, 1880, 1800, ..."
            category="std"
            seriesNo="1">

```

At a minimum, the "number" attribute should be present.

The other attributes are:

o  "obsoletes", having a comma-separated list of RFC numbers, that
the document obsoletes;

o  "updates", having a comma-separated list of RFC numbers, that the
document updates;

o  "category", having one of these values:

1.  "std", for a Standards-Track document;

2.  "bcp", "for a Best Current Practices document;

3.  "exp", for an Experimental Protocol document;

4.  "historic", for a historic document; or,

5.  "info", the default, for an Informational document.

o  "seriesNo", having the corresponding number in the STD (std), BCP
(bcp), or FYI (info) series.

Finally, a special entity, "&rfc.number;", is available. Authors
preparing an RFC should use this entity whenever they want to
reference the number of the RFC within the document itself. In
printed versions of the document, the appropriate substitution (or
"XXXX") will occur.

# Appendix B. The RFC DTD

<!--
DTD for the RFC document series, draft of 99-01-30
-->

<!--

# Table of Contents

    - [DTD data types](#dtd-data-types)
    - [Front matter](#front-matter)
    - [Back matter](#back-matter)
      - [TEXT          character data](#text-character-data)
  - [Front matter](#front-matter)
  - [Back matter](#back-matter)

The author gratefully acknowledges the contributions of: Alan
Barrett, Brad Burdick, Brian Carpenter, Steve Deering, Patrik
Faltstrom, Jim Gettys, Carl Malamud, Chris Newman, Kurt Starsinic,
and, Frank Strauss.

I
indexing
how to  16

Full Copyright Statement

Copyright (C) The Internet Society (1999).  All Rights Reserved.

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

Acknowledgement

Funding for the RFC Editor function is currently provided by the
Internet Society.
