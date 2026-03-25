Package org.jsoup.nodes

# Class Document

java.lang.Object
org.jsoup.nodes.Node
org.jsoup.nodes.Element
org.jsoup.nodes.Document

All Implemented Interfaces:
`Cloneable`, `Iterable<Element>`

---

public class Document
extends Element
A HTML Document.

Author:
Jonathan Hedley, [email protected]

- 

## Nested Class Summary

Nested Classes

Modifier and Type
Class
Description
`static class `
`Document.OutputSettings`

A Document's output settings control the form of the text() and html() methods.

`static enum `
`Document.QuirksMode`
 

- 

## Constructor Summary

Constructors

Constructor
Description
`Document(String baseUri)`

Create a new, empty Document, in the HTML namespace.

`Document(String namespace,
 String baseUri)`

Create a new, empty Document, in the specified namespace.

- 

## Method Summary

Modifier and Type
Method
Description
`Element`
`body()`

Get this document's `<body>` or `<frameset>` element.

`Charset`
`charset()`

Get the output character set of this Document.

`void`
`charset(Charset charset)`

Set the output character set of this Document.

`Document`
`clone()`

Create a stand-alone, deep copy of this node, and all of its children.

`Connection`
`connection()`

Returns the Connection (Request/Response) object that was used to fetch this document, if any; otherwise, a new
     default Connection object.

`Document`
`connection(Connection connection)`

Set the Connection used to fetch this document.

`Element`
`createElement(String tagName)`

Create a new Element, with this document's base uri.

`static Document`
`createShell(String baseUri)`

Create a valid, empty shell of an HTML document, suitable for adding more elements to.

`@Nullable DocumentType`
`documentType()`

Returns this Document's doctype.

`FormElement`
`expectForm(String cssQuery)`

Selects the first `FormElement` in this document that matches the query.

`List<FormElement>`
`forms()`

Get each of the `<form>` elements contained in this document.

`Element`
`head()`

Get this document's `head` element.

`String`
`location()`

Get the URL this Document was parsed from.

`String`
`nodeName()`

Get the node name of this node.

`String`
`outerHtml()`

Get the outer HTML of this node.

`Document.OutputSettings`
`outputSettings()`

Get the document's current output settings.

`Document`
`outputSettings(Document.OutputSettings outputSettings)`

Set the document's output settings.

`Parser`
`parser()`

Get the parser that was used to parse this document.

`Document`
`parser(Parser parser)`

Set the parser used to create this document.

`Document.QuirksMode`
`quirksMode()`
 
`Document`
`quirksMode(Document.QuirksMode quirksMode)`
 
`Document`
`shallowClone()`

Create a stand-alone, shallow copy of this node.

`Element`
`text(String text)`

Set the text of the `body` of this document.

`String`
`title()`

Get the string contents of the document's `title` element.

`void`
`title(String title)`

Set the document's `title` element.

### Methods inherited from class org.jsoup.nodes.Element

`addClass, after, after, append, appendChild, appendChildren, appendElement, appendElement, appendText, appendTo, attr, attr, attribute, attributes, baseUri, before, before, child, childNodeSize, children, childrenSize, className, classNames, classNames, clearAttributes, closest, closest, cssSelector, data, dataNodes, dataset, doClone, doSetBaseUri, elementIs, elementSiblingIndex, empty, endSourceRange, ensureChildNodes, expectFirst, expectFirstNode, filter, firstElementChild, firstElementSibling, forEach, forEachNode, getAllElements, getElementById, getElementsByAttribute, getElementsByAttributeStarting, getElementsByAttributeValue, getElementsByAttributeValueContaining, getElementsByAttributeValueEnding, getElementsByAttributeValueMatching, getElementsByAttributeValueMatching, getElementsByAttributeValueNot, getElementsByAttributeValueStarting, getElementsByClass, getElementsByIndexEquals, getElementsByIndexGreaterThan, getElementsByIndexLessThan, getElementsByTag, getElementsContainingOwnText, getElementsContainingText, getElementsMatchingOwnText, getElementsMatchingOwnText, getElementsMatchingText, getElementsMatchingText, hasAttributes, hasChildNodes, hasClass, hasText, html, html, html, id, id, insertChildren, insertChildren, is, is, isBlock, iterator, lastElementChild, lastElementSibling, nextElementSiblings, nodeValue, normalName, ownText, parent, parents, prepend, prependChild, prependChildren, prependElement, prependElement, prependText, previousElementSiblings, removeAttr, removeClass, root, select, select, selectFirst, selectFirst, selectFirstNode, selectFirstNode, selectNodes, selectNodes, selectNodes, selectNodes, selectStream, selectStream, selectXpath, selectXpath, siblingElements, stream, tag, tag, tagName, tagName, tagName, text, textNodes, toggleClass, traverse, val, val, wholeOwnText, wholeText, wrap`

### Methods inherited from class org.jsoup.nodes.Node

`absUrl, addChildren, addChildren, attr, attributesSize, childNode, childNodes, childNodesAsArray, childNodesCopy, equals, firstChild, firstSibling, hasAttr, hashCode, hasParent, hasSameValue, indent, lastChild, lastSibling, nameIs, nextElementSibling, nextSibling, nodeStream, nodeStream, outerHtml, outerHtml, ownerDocument, parentElement, parentElementIs, parentNameIs, parentNode, previousElementSibling, previousSibling, remove, removeChild, reparentChild, replaceChild, replaceWith, setBaseUri, setParentNode, setSiblingIndex, siblingIndex, siblingNodes, sourceRange, toString, unwrap`

### Methods inherited from class java.lang.Object

`finalize, getClass, notify, notifyAll, wait, wait, wait`

### Methods inherited from interface java.lang.Iterable

`spliterator`

- 

## Constructor Details

  - 

### Document

public Document(String namespace,
 String baseUri)
Create a new, empty Document, in the specified namespace.

Parameters:
`namespace` - the namespace of this Document's root node.
`baseUri` - base URI of document
See Also:

    - `Jsoup.parse(java.lang.String, java.lang.String)`

    - `createShell(java.lang.String)`

  - 

### Document

public Document(String baseUri)
Create a new, empty Document, in the HTML namespace.

Parameters:
`baseUri` - base URI of document
See Also:

    - `Jsoup.parse(java.lang.String, java.lang.String)`

    - `Document(String namespace, String baseUri)`

- 

## Method Details

  - 

### createShell

public static Document createShell(String baseUri)
Create a valid, empty shell of an HTML document, suitable for adding more elements to.

Parameters:
`baseUri` - baseUri of document
Returns:
document with html, head, and body elements.

  - 

### location

public String location()
Get the URL this Document was parsed from. If the starting URL is a redirect,
 this will return the final URL from which the document was served from.
 

Will return an empty string if the location is unknown (e.g. if parsed from a String).

Returns:
location

  - 

### connection

public Connection connection()
Returns the Connection (Request/Response) object that was used to fetch this document, if any; otherwise, a new
     default Connection object. This can be used to continue a session, preserving settings and cookies, etc.

Returns:
the Connection (session) associated with this Document, or an empty one otherwise.
See Also:

    - `Connection.newRequest()`

  - 

### documentType

public @Nullable DocumentType documentType()
Returns this Document's doctype.

Returns:
document type, or null if not set

  - 

### head

public Element head()
Get this document's `head` element.
     

     As a side effect, if this Document does not already have an HTML structure, it will be created. If you do not want
     that, use `#selectFirst("head")` instead.

Returns:
`head` element.

  - 

### body

public Element body()
Get this document's `<body>` or `<frameset>` element.
     

     As a **side-effect**, if this Document does not already have an HTML structure, it will be created with a `
    <body>` element. If you do not want that, use `#selectFirst("body")` instead.

Returns:
`body` element for documents with a `<body>`, a new `<body>` element if the document
     had no contents, or the outermost `<frameset> element` for frameset documents.

  - 

### forms

public List<FormElement> forms()
Get each of the `<form>` elements contained in this document.

Returns:
a List of FormElement objects, which will be empty if there are none.
Since:
1.15.4
See Also:

    - `Elements.forms()`

    - `FormElement.elements()`

  - 

### expectForm

public FormElement expectForm(String cssQuery)
Selects the first `FormElement` in this document that matches the query. If none match, throws an
     `IllegalArgumentException`.

Parameters:
`cssQuery` - a `Selector` CSS query
Returns:
the first matching `<form>` element
Throws:
`IllegalArgumentException` - if no match is found
Since:
1.15.4

  - 

### title

public String title()
Get the string contents of the document's `title` element.

Returns:
Trimmed title, or empty string if none set.

  - 

### title

public void title(String title)
Set the document's `title` element. Updates the existing element, or adds `title` to `head` if
     not present

Parameters:
`title` - string to set as title

  - 

### createElement

public Element createElement(String tagName)
Create a new Element, with this document's base uri. Does not make the new element a child of this document.

Parameters:
`tagName` - element tag name (e.g. `a`)
Returns:
new element

  - 

### outerHtml

public String outerHtml()
Description copied from class: `Node`
Get the outer HTML of this node. For example, on a `p` element, may return `<p>Para</p>`.

Overrides:
`outerHtml` in class `Node`
Returns:
outer HTML
See Also:

    - `Element.html()`

    - `Element.text()`

  - 

### text

public Element text(String text)
Set the text of the `body` of this document. Any existing nodes within the body will be cleared.

Overrides:
`text` in class `Element`
Parameters:
`text` - un-encoded text
Returns:
this document

  - 

### nodeName

public String nodeName()
Description copied from class: `Node`
Get the node name of this node. Use for debugging purposes and not logic switching (for that, use instanceof).

Overrides:
`nodeName` in class `Element`
Returns:
node name

  - 

### charset

public void charset(Charset charset)
Set the output character set of this Document. This method is equivalent to
     `OutputSettings.charset(Charset)`, but additionally adds or
     updates the charset / encoding element within the Document.

     

If there's no existing element with charset / encoding information yet, one will
     be created. Obsolete charset / encoding definitions are removed.

     

**Elements used:**

     

     
    - **HTML:** *<meta charset="CHARSET">*
     
    - **XML:** *<?xml version="1.0" encoding="CHARSET">*
     

Parameters:
`charset` - Charset
See Also:

    - `Document.OutputSettings.charset(java.nio.charset.Charset)`

  - 

### charset

public Charset charset()
Get the output character set of this Document. This method is equivalent to `Document.OutputSettings.charset()`.

Returns:
the current Charset
See Also:

    - `Document.OutputSettings.charset()`

  - 

### clone

public Document clone()
Description copied from class: `Node`
Create a stand-alone, deep copy of this node, and all of its children. The cloned node will have no siblings.
     

     
    - If this node is a `LeafNode`, the clone will have no parent.
     
    - If this node is an `Element`, the clone will have a simple owning `Document` to retain the
     configured output settings and parser.
     

     

The cloned node may be adopted into another Document or node structure using
     `Element.appendChild(Node)`.

Overrides:
`clone` in class `Element`
Returns:
a stand-alone cloned node, including clones of any children
See Also:

    - `Node.shallowClone()`

  - 

### shallowClone

public Document shallowClone()
Description copied from class: `Node`
Create a stand-alone, shallow copy of this node. None of its children (if any) will be cloned, and it will have
 no parent or sibling nodes.

Overrides:
`shallowClone` in class `Element`
Returns:
a single independent copy of this node
See Also:

    - `Node.clone()`

  - 

### outputSettings

public Document.OutputSettings outputSettings()
Get the document's current output settings.

Returns:
the document's current output settings.

  - 

### outputSettings

public Document outputSettings(Document.OutputSettings outputSettings)
Set the document's output settings.

Parameters:
`outputSettings` - new output settings.
Returns:
this document, for chaining.

  - 

### quirksMode

public Document.QuirksMode quirksMode()

  - 

### quirksMode

public Document quirksMode(Document.QuirksMode quirksMode)

  - 

### parser

public Parser parser()
Get the parser that was used to parse this document.

Returns:
the parser

  - 

### parser

public Document parser(Parser parser)
Set the parser used to create this document. This parser is then used when further parsing within this document
 is required.

Parameters:
`parser` - the configured parser to use when further parsing is required for this document.
Returns:
this document, for chaining.

  - 

### connection

public Document connection(Connection connection)
Set the Connection used to fetch this document. This Connection is used as a session object when further requests are
     made (e.g. when a form is submitted).

Parameters:
`connection` - to set
Returns:
this document, for chaining
Since:
1.14.1
See Also:

    - `Connection.newRequest()`