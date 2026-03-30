Package org.jsoup.nodes

# Class DocumentType

java.lang.Object
org.jsoup.nodes.Node
org.jsoup.nodes.LeafNode
org.jsoup.nodes.DocumentType

All Implemented Interfaces:
`Cloneable`

---

public class DocumentType
extends LeafNode
A `<!DOCTYPE>` node.

- 

## Field Summary

Fields

Modifier and Type
Field
Description
`static final String`
`PUBLIC_KEY`
 
`static final String`
`SYSTEM_KEY`
 

- 

## Constructor Summary

Constructors

Constructor
Description
`DocumentType(String name,
 String publicId,
 String systemId)`

Create a new doctype element.

- 

## Method Summary

Modifier and Type
Method
Description
`String`
`name()`

Get this doctype's name (when set, or empty string)

`String`
`nodeName()`

Get the node name of this node.

`String`
`publicId()`

Get this doctype's Public ID (when set, or empty string)

`void`
`setPubSysKey(@Nullable String value)`
 
`String`
`systemId()`

Get this doctype's System ID (when set, or empty string)

### Methods inherited from class org.jsoup.nodes.LeafNode

`absUrl, attr, attr, attributes, baseUri, childNodeSize, doClone, doSetBaseUri, empty, ensureChildNodes, hasAttr, hasAttributes, nodeValue, parent, removeAttr`

### Methods inherited from class org.jsoup.nodes.Node

`addChildren, addChildren, after, after, attributesSize, before, before, childNode, childNodes, childNodesAsArray, childNodesCopy, clearAttributes, clone, equals, filter, firstChild, firstSibling, forEachNode, hashCode, hasParent, hasSameValue, html, indent, lastChild, lastSibling, nameIs, nextElementSibling, nextSibling, nodeStream, nodeStream, normalName, outerHtml, outerHtml, outerHtml, ownerDocument, parentElement, parentElementIs, parentNameIs, parentNode, previousElementSibling, previousSibling, remove, removeChild, reparentChild, replaceChild, replaceWith, root, setBaseUri, setParentNode, setSiblingIndex, shallowClone, siblingIndex, siblingNodes, sourceRange, toString, traverse, unwrap, wrap`

### Methods inherited from class java.lang.Object

`finalize, getClass, notify, notifyAll, wait, wait, wait`

- 

## Field Details

  - 

### PUBLIC_KEY

public static final String PUBLIC_KEY

See Also:

    - Constant Field Values

  - 

### SYSTEM_KEY

public static final String SYSTEM_KEY

See Also:

    - Constant Field Values

- 

## Constructor Details

  - 

### DocumentType

public DocumentType(String name,
 String publicId,
 String systemId)
Create a new doctype element.

Parameters:
`name` - the doctype's name
`publicId` - the doctype's public ID
`systemId` - the doctype's system ID

- 

## Method Details

  - 

### setPubSysKey

public void setPubSysKey(@Nullable String value)

  - 

### name

public String name()
Get this doctype's name (when set, or empty string)

Returns:
doctype name

  - 

### publicId

public String publicId()
Get this doctype's Public ID (when set, or empty string)

Returns:
doctype Public ID

  - 

### systemId

public String systemId()
Get this doctype's System ID (when set, or empty string)

Returns:
doctype System ID

  - 

### nodeName

public String nodeName()
Description copied from class: `Node`
Get the node name of this node. Use for debugging purposes and not logic switching (for that, use instanceof).

Specified by:
`nodeName` in class `Node`
Returns:
node name