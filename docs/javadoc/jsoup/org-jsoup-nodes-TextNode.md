Package org.jsoup.nodes

# Class TextNode

java.lang.Object
org.jsoup.nodes.Node
org.jsoup.nodes.LeafNode
org.jsoup.nodes.TextNode

All Implemented Interfaces:
`Cloneable`

Direct Known Subclasses:
`CDataNode`

---

public class TextNode
extends LeafNode
A text node.

Author:
Jonathan Hedley, [email protected]

- 

## Constructor Summary

Constructors

Constructor
Description
`TextNode(String text)`

Create a new TextNode representing the supplied (unencoded) text).

- 

## Method Summary

Modifier and Type
Method
Description
`TextNode`
`clone()`

Create a stand-alone, deep copy of this node, and all of its children.

`static TextNode`
`createFromEncoded(String encodedText)`

Create a new TextNode from HTML encoded (aka escaped) data.

`String`
`getWholeText()`

Get the (unencoded) text of this text node, including any newlines and spaces present in the original.

`boolean`
`isBlank()`

Test if this text node is blank -- that is, empty or only whitespace (including newlines).

`String`
`nodeName()`

Get the node name of this node.

`TextNode`
`splitText(int offset)`

Split this text node into two nodes at the specified string offset.

`String`
`text()`

Get the text content of this text node.

`TextNode`
`text(String text)`

Set the text content of this text node.

`String`
`toString()`

Gets this node's outer HTML.

### Methods inherited from class org.jsoup.nodes.LeafNode

`absUrl, attr, attr, attributes, baseUri, childNodeSize, doClone, doSetBaseUri, empty, ensureChildNodes, hasAttr, hasAttributes, nodeValue, parent, removeAttr`

### Methods inherited from class org.jsoup.nodes.Node

`addChildren, addChildren, after, after, attributesSize, before, before, childNode, childNodes, childNodesAsArray, childNodesCopy, clearAttributes, equals, filter, firstChild, firstSibling, forEachNode, hashCode, hasParent, hasSameValue, html, indent, lastChild, lastSibling, nameIs, nextElementSibling, nextSibling, nodeStream, nodeStream, normalName, outerHtml, outerHtml, outerHtml, ownerDocument, parentElement, parentElementIs, parentNameIs, parentNode, previousElementSibling, previousSibling, remove, removeChild, reparentChild, replaceChild, replaceWith, root, setBaseUri, setParentNode, setSiblingIndex, shallowClone, siblingIndex, siblingNodes, sourceRange, traverse, unwrap, wrap`

### Methods inherited from class java.lang.Object

`finalize, getClass, notify, notifyAll, wait, wait, wait`

- 

## Constructor Details

  - 

### TextNode

public TextNode(String text)
Create a new TextNode representing the supplied (unencoded) text).

Parameters:
`text` - raw text
See Also:

    - `createFromEncoded(String)`

- 

## Method Details

  - 

### nodeName

public String nodeName()
Description copied from class: `Node`
Get the node name of this node. Use for debugging purposes and not logic switching (for that, use instanceof).

Specified by:
`nodeName` in class `Node`
Returns:
node name

  - 

### text

public String text()
Get the text content of this text node.

Returns:
Unencoded, normalised text.
See Also:

    - `getWholeText()`

  - 

### text

public TextNode text(String text)
Set the text content of this text node.

Parameters:
`text` - unencoded text
Returns:
this, for chaining

  - 

### getWholeText

public String getWholeText()
Get the (unencoded) text of this text node, including any newlines and spaces present in the original.

Returns:
text

  - 

### isBlank

public boolean isBlank()
Test if this text node is blank -- that is, empty or only whitespace (including newlines).

Returns:
true if this document is empty or only whitespace, false if it contains any text content.

  - 

### splitText

public TextNode splitText(int offset)
Split this text node into two nodes at the specified string offset. After splitting, this node will contain the
 original text up to the offset, and will have a new text node sibling containing the text after the offset.

Parameters:
`offset` - string offset point to split node at.
Returns:
the newly created text node containing the text after the offset.

  - 

### toString

public String toString()
Description copied from class: `Node`
Gets this node's outer HTML.

Overrides:
`toString` in class `Node`
Returns:
outer HTML.
See Also:

    - `Node.outerHtml()`

  - 

### clone

public TextNode clone()
Description copied from class: `Node`
Create a stand-alone, deep copy of this node, and all of its children. The cloned node will have no siblings.
     

     
    - If this node is a `LeafNode`, the clone will have no parent.
     
    - If this node is an `Element`, the clone will have a simple owning `Document` to retain the
     configured output settings and parser.
     

     

The cloned node may be adopted into another Document or node structure using
     `Element.appendChild(Node)`.

Overrides:
`clone` in class `Node`
Returns:
a stand-alone cloned node, including clones of any children
See Also:

    - `Node.shallowClone()`

  - 

### createFromEncoded

public static TextNode createFromEncoded(String encodedText)
Create a new TextNode from HTML encoded (aka escaped) data.

Parameters:
`encodedText` - Text containing encoded HTML (e.g. `<`)
Returns:
TextNode containing unencoded data (e.g. `<`)