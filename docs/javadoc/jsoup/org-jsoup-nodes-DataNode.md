Package org.jsoup.nodes

# Class DataNode

java.lang.Object
org.jsoup.nodes.Node
org.jsoup.nodes.LeafNode
org.jsoup.nodes.DataNode

All Implemented Interfaces:
`Cloneable`

---

public class DataNode
extends LeafNode
A data node, for contents of style, script tags etc, where contents should not show in text().

Author:
Jonathan Hedley, [email protected]

- 

## Constructor Summary

Constructors

Constructor
Description
`DataNode(String data)`

Create a new DataNode.

- 

## Method Summary

Modifier and Type
Method
Description
`DataNode`
`clone()`

Create a stand-alone, deep copy of this node, and all of its children.

`String`
`getWholeData()`

Get the data contents of this node.

`String`
`nodeName()`

Get the node name of this node.

`DataNode`
`setWholeData(String data)`

Set the data contents of this node.

### Methods inherited from class org.jsoup.nodes.LeafNode

`absUrl, attr, attr, attributes, baseUri, childNodeSize, doClone, doSetBaseUri, empty, ensureChildNodes, hasAttr, hasAttributes, nodeValue, parent, removeAttr`

### Methods inherited from class org.jsoup.nodes.Node

`addChildren, addChildren, after, after, attributesSize, before, before, childNode, childNodes, childNodesAsArray, childNodesCopy, clearAttributes, equals, filter, firstChild, firstSibling, forEachNode, hashCode, hasParent, hasSameValue, html, indent, lastChild, lastSibling, nameIs, nextElementSibling, nextSibling, nodeStream, nodeStream, normalName, outerHtml, outerHtml, outerHtml, ownerDocument, parentElement, parentElementIs, parentNameIs, parentNode, previousElementSibling, previousSibling, remove, removeChild, reparentChild, replaceChild, replaceWith, root, setBaseUri, setParentNode, setSiblingIndex, shallowClone, siblingIndex, siblingNodes, sourceRange, toString, traverse, unwrap, wrap`

### Methods inherited from class java.lang.Object

`finalize, getClass, notify, notifyAll, wait, wait, wait`

- 

## Constructor Details

  - 

### DataNode

public DataNode(String data)
Create a new DataNode.

Parameters:
`data` - data contents

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

### getWholeData

public String getWholeData()
Get the data contents of this node. Will be unescaped and with original new lines, space etc.

Returns:
data

  - 

### setWholeData

public DataNode setWholeData(String data)
Set the data contents of this node.

Parameters:
`data` - un-encoded data
Returns:
this node, for chaining

  - 

### clone

public DataNode clone()
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