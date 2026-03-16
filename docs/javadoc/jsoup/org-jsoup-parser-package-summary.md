# Package org.jsoup.parser

---

@NullMarked
package org.jsoup.parser

Contains the HTML parser, tag specifications, and HTML tokeniser.

- 

Related Packages

Package
Description
org.jsoup

Contains the main `Jsoup` class, which provides convenient static access to the jsoup functionality.

org.jsoup.helper

Package containing classes supporting the core jsoup code.

org.jsoup.nodes

HTML document structure nodes.

org.jsoup.safety

Contains the jsoup HTML cleaner, and safelist definitions.

org.jsoup.select

Packages to support the CSS-style element selector.

- 

Classes

Class
Description
CharacterReader

CharacterReader consumes tokens off a string.

HtmlTreeBuilder

HTML Tree Builder; creates a DOM from Tokens.

ParseError

A Parse Error records an error in the input HTML that occurs in either the tokenisation or the tree building phase.

ParseErrorList

A container for ParseErrors.

Parser

Parses HTML or XML into a `Document`.

ParseSettings

Controls parser case settings, to optionally preserve tag and/or attribute name case.

StreamParser

A StreamParser provides a progressive parse of its input.

Tag

A Tag represents an Element's name and configured options, common throughout the Document.

TagSet

A TagSet controls the `Tag` configuration for a Document's parse, and its serialization.

TokenQueue

A character reader with helpers focusing on parsing CSS selectors.

XmlTreeBuilder

Use the `XmlTreeBuilder` when you want to parse XML without any of the HTML DOM rules being applied to the
 document.