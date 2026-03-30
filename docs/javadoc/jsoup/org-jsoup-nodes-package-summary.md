# Package org.jsoup.nodes

---

@NullMarked
package org.jsoup.nodes

HTML document structure nodes.

- 

Related Packages

Package
Description
org.jsoup

Contains the main `Jsoup` class, which provides convenient static access to the jsoup functionality.

org.jsoup.helper

Package containing classes supporting the core jsoup code.

org.jsoup.parser

Contains the HTML parser, tag specifications, and HTML tokeniser.

org.jsoup.safety

Contains the jsoup HTML cleaner, and safelist definitions.

org.jsoup.select

Packages to support the CSS-style element selector.

- 

Class
Description
Attribute

A single key + value attribute.

Attributes

The attributes of an Element.

CDataNode

A Character Data node, to support CDATA sections.

Comment

A comment node.

DataNode

A data node, for contents of style, script tags etc, where contents should not show in text().

Document

A HTML Document.

Document.OutputSettings

A Document's output settings control the form of the text() and html() methods.

Document.OutputSettings.Syntax

The output serialization syntax.

Document.QuirksMode
 
DocumentType

A `<!DOCTYPE>` node.

Element

An HTML Element consists of a tag name, attributes, and child nodes (including text nodes and other elements).

Entities

HTML entities, and escape routines.

Entities.EscapeMode
 
FormElement

An HTML Form Element provides ready access to the form fields/controls that are associated with it.

LeafNode

A node that does not hold any children.

Node

The base, abstract Node model.

NodeIterator<T extends Node>

Iterate through a Node and its tree of descendants, in document order, and returns nodes of the specified type.

PseudoTextElement
Deprecated.
use `Element.selectNodes(String, Class)` instead, with selector of `::textnode` and class `TextNode`;
 will be removed in jsoup 1.24.1.

Range

A Range object tracks the character positions in the original input source where a Node starts or ends.

Range.AttributeRange
 
Range.Position

A Position object tracks the character position in the original input source where a Node starts or ends.

TextNode

A text node.

XmlDeclaration

An XML Declaration.