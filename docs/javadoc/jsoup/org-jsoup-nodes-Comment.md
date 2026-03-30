Package org.jsoup.nodes

# Class Comment

java.lang.Object
org.jsoup.nodes.Node
org.jsoup.nodes.LeafNode
org.jsoup.nodes.Comment

All Implemented Interfaces:
`Cloneable`

---

public class Comment
extends LeafNode
A comment node.

Author:
Jonathan Hedley, [email protected]

- 

## Constructor Summary

Constructors

Constructor
Description
`Comment(String data)`

Create a new comment node.

- 

## Method Summary

Modifier and Type
Method
Description
`@Nullable XmlDeclaration`
`asXmlDeclaration()`

Attempt to cast this comment to an XML Declaration node.

`Comment`
`clone()`

Create a stand-alone, deep copy of this node, and all of its children.

`String`
`getData()`

Get the contents of the comment.

`boolean`
`isXmlDeclaration()`

Check if this comment looks like an XML Declaration.

`String`
`nodeName()`

Get the node name of this node.

`Comment`
`setData(String data)`
 

### Methods inherited from class org.jsoup.nodes.LeafNode

`absUrl, attr, attr, attributes, baseUri, childNodeSize, doClone, doSetBaseUri, empty, ensureChildNodes, hasAttr, hasAttributes, nodeValue, parent, removeAttr`

### Methods inherited from class org.jsoup.nodes.Node

`addChildren, addChildren, after, after, attributesSize, before, before, childNode, childNodes, childNodesAsArray, childNodesCopy, clearAttributes, equals, filter, firstChild, firstSibling, forEachNode, hashCode, hasParent, hasSameValue, html, indent, lastChild, lastSibling, nameIs, nextElementSibling, nextSibling, nodeStream, nodeStream, normalName, outerHtml, outerHtml, outerHtml, ownerDocument, parentElement, parentElementIs, parentNameIs, parentNode, previousElementSibling, previousSibling, remove, removeChild, reparentChild, replaceChild, replaceWith, root, setBaseUri, setParentNode, setSiblingIndex, shallowClone, siblingIndex, siblingNodes, sourceRange, toString, traverse, unwrap, wrap`

### Methods inherited from class java.lang.Object

`finalize, getClass, notify, notifyAll, wait, wait, wait`

- 

## Constructor Details

  - 

### Comment

public Comment(String data)
Create a new comment node.

Parameters:
`data` - The contents of the comment

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

### getData

public String getData()
Get the contents of the comment.

Returns:
comment content

  - 

### setData

public Comment setData(String data)

  - 

### clone

public Comment clone()
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

### isXmlDeclaration

public boolean isXmlDeclaration()
Check if this comment looks like an XML Declaration. This is the case when the HTML parser sees an XML
 declaration or processing instruction. Other than doctypes, those aren't part of HTML, and will be parsed as a
 bogus comment.

Returns:
true if it looks like, maybe, it's an XML Declaration.
See Also:

    - `asXmlDeclaration()`

  - 

### asXmlDeclaration

public @Nullable XmlDeclaration asXmlDeclaration()
Attempt to cast this comment to an XML Declaration node.

Returns:
an XML declaration if it could be parsed as one, null otherwise.
See Also:

    - `isXmlDeclaration()`