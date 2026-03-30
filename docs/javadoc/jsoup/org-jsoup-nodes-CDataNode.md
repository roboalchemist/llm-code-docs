Package org.jsoup.nodes

# Class CDataNode

java.lang.Object
org.jsoup.nodes.Node
org.jsoup.nodes.LeafNode
org.jsoup.nodes.TextNode
org.jsoup.nodes.CDataNode

All Implemented Interfaces:
`Cloneable`

---

public class CDataNode
extends TextNode
A Character Data node, to support CDATA sections.

- 

## Constructor Summary

Constructors

Constructor
Description
`CDataNode(String text)`
 

- 

## Method Summary

Modifier and Type
Method
Description
`CDataNode`
`clone()`

Create a stand-alone, deep copy of this node, and all of its children.

`String`
`nodeName()`

Get the node name of this node.

`String`
`text()`

Get the un-encoded, **non-normalized** text content of this CDataNode.

### Methods inherited from class org.jsoup.nodes.TextNode

`createFromEncoded, getWholeText, isBlank, splitText, text, toString`

### Methods inherited from class org.jsoup.nodes.LeafNode

`absUrl, attr, attr, attributes, baseUri, childNodeSize, doClone, doSetBaseUri, empty, ensureChildNodes, hasAttr, hasAttributes, nodeValue, parent, removeAttr`

### Methods inherited from class org.jsoup.nodes.Node

`addChildren, addChildren, after, after, attributesSize, before, before, childNode, childNodes, childNodesAsArray, childNodesCopy, clearAttributes, equals, filter, firstChild, firstSibling, forEachNode, hashCode, hasParent, hasSameValue, html, indent, lastChild, lastSibling, nameIs, nextElementSibling, nextSibling, nodeStream, nodeStream, normalName, outerHtml, outerHtml, outerHtml, ownerDocument, parentElement, parentElementIs, parentNameIs, parentNode, previousElementSibling, previousSibling, remove, removeChild, reparentChild, replaceChild, replaceWith, root, setBaseUri, setParentNode, setSiblingIndex, shallowClone, siblingIndex, siblingNodes, sourceRange, traverse, unwrap, wrap`

### Methods inherited from class java.lang.Object

`finalize, getClass, notify, notifyAll, wait, wait, wait`

- 

## Constructor Details

  - 

### CDataNode

public CDataNode(String text)

- 

## Method Details

  - 

### nodeName

public String nodeName()
Description copied from class: `Node`
Get the node name of this node. Use for debugging purposes and not logic switching (for that, use instanceof).

Overrides:
`nodeName` in class `TextNode`
Returns:
node name

  - 

### text

public String text()
Get the un-encoded, **non-normalized** text content of this CDataNode.

Overrides:
`text` in class `TextNode`
Returns:
un-encoded, non-normalized text
See Also:

    - `TextNode.getWholeText()`

  - 

### clone

public CDataNode clone()
Description copied from class: `Node`
Create a stand-alone, deep copy of this node, and all of its children. The cloned node will have no siblings.
     

     
    - If this node is a `LeafNode`, the clone will have no parent.
     
    - If this node is an `Element`, the clone will have a simple owning `Document` to retain the
     configured output settings and parser.
     

     

The cloned node may be adopted into another Document or node structure using
     `Element.appendChild(Node)`.

Overrides:
`clone` in class `TextNode`
Returns:
a stand-alone cloned node, including clones of any children
See Also:

    - `Node.shallowClone()`