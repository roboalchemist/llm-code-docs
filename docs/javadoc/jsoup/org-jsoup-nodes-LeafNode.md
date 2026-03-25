Package org.jsoup.nodes

# Class LeafNode

java.lang.Object
org.jsoup.nodes.Node
org.jsoup.nodes.LeafNode

All Implemented Interfaces:
`Cloneable`

Direct Known Subclasses:
`Comment`, `DataNode`, `DocumentType`, `TextNode`, `XmlDeclaration`

---

public abstract class LeafNode
extends Node
A node that does not hold any children. E.g.: `TextNode`, `DataNode`, `Comment`.

- 

## Constructor Summary

Constructors

Modifier
Constructor
Description
` `
`LeafNode()`
 
`protected `
`LeafNode(String coreValue)`
 

- 

## Method Summary

Modifier and Type
Method
Description
`String`
`absUrl(String key)`

Get an absolute URL from a URL attribute that may be relative (such as an `<a href>` or
 `<img src>`).

`String`
`attr(String key)`

Get an attribute's value by its key.

`Node`
`attr(String key,
 String value)`

Set an attribute (key=value).

`final Attributes`
`attributes()`

Get each of the Element's attributes.

`String`
`baseUri()`

Get the base URI that applies to this node.

`int`
`childNodeSize()`

Get the number of child nodes that this node holds.

`protected LeafNode`
`doClone(Node parent)`
 
`protected void`
`doSetBaseUri(String baseUri)`

Set the baseUri for just this node (not its descendants), if this Node tracks base URIs.

`Node`
`empty()`

Delete all this node's children.

`protected List<Node>`
`ensureChildNodes()`
 
`boolean`
`hasAttr(String key)`

Test if this Node has an attribute.

`protected final boolean`
`hasAttributes()`

Check if this Node has an actual Attributes object.

`String`
`nodeValue()`

Get the node's value.

`@Nullable Element`
`parent()`

Gets this node's parent node.

`Node`
`removeAttr(String key)`

Remove an attribute from this node.

### Methods inherited from class org.jsoup.nodes.Node

`addChildren, addChildren, after, after, attributesSize, before, before, childNode, childNodes, childNodesAsArray, childNodesCopy, clearAttributes, clone, equals, filter, firstChild, firstSibling, forEachNode, hashCode, hasParent, hasSameValue, html, indent, lastChild, lastSibling, nameIs, nextElementSibling, nextSibling, nodeName, nodeStream, nodeStream, normalName, outerHtml, outerHtml, outerHtml, ownerDocument, parentElement, parentElementIs, parentNameIs, parentNode, previousElementSibling, previousSibling, remove, removeChild, reparentChild, replaceChild, replaceWith, root, setBaseUri, setParentNode, setSiblingIndex, shallowClone, siblingIndex, siblingNodes, sourceRange, toString, traverse, unwrap, wrap`

### Methods inherited from class java.lang.Object

`finalize, getClass, notify, notifyAll, wait, wait, wait`

- 

## Constructor Details

  - 

### LeafNode

public LeafNode()

  - 

### LeafNode

protected LeafNode(String coreValue)

- 

## Method Details

  - 

### hasAttributes

protected final boolean hasAttributes()
Description copied from class: `Node`
Check if this Node has an actual Attributes object.

Specified by:
`hasAttributes` in class `Node`

  - 

### attributes

public final Attributes attributes()
Description copied from class: `Node`
Get each of the Element's attributes.

Specified by:
`attributes` in class `Node`
Returns:
attributes (which implements Iterable, with the same order as presented in the original HTML).

  - 

### parent

public @Nullable Element parent()
Description copied from class: `Node`
Gets this node's parent node. This is always an Element.

Overrides:
`parent` in class `Node`
Returns:
parent node; or null if no parent.
See Also:

    - `Node.hasParent()`

  - 

### nodeValue

public String nodeValue()
Description copied from class: `Node`
Get the node's value. For a TextNode, the whole text; for a Comment, the comment data; for an Element,
     wholeOwnText. Returns "" if there is no value.

Overrides:
`nodeValue` in class `Node`
Returns:
the node's value

  - 

### attr

public String attr(String key)
Description copied from class: `Node`
Get an attribute's value by its key. **Case insensitive**
 

 To get an absolute URL from an attribute that may be a relative URL, prefix the key with `**abs:**`,
 which is a shortcut to the `Node.absUrl(java.lang.String)` method.
 
 E.g.:
 `String url = a.attr("abs:href");`

Overrides:
`attr` in class `Node`
Parameters:
`key` - The attribute key.
Returns:
The attribute, or empty string if not present (to avoid nulls).
See Also:

    - `Node.attributes()`

    - `Node.hasAttr(String)`

    - `Node.absUrl(String)`

  - 

### attr

public Node attr(String key,
 String value)
Description copied from class: `Node`
Set an attribute (key=value). If the attribute already exists, it is replaced. The attribute key comparison is
 **case insensitive**. The key will be set with case sensitivity as set in the parser settings.

Overrides:
`attr` in class `Node`
Parameters:
`key` - The attribute key.
`value` - The attribute value.
Returns:
this (for chaining)

  - 

### hasAttr

public boolean hasAttr(String key)
Description copied from class: `Node`
Test if this Node has an attribute. **Case insensitive**.

Overrides:
`hasAttr` in class `Node`
Parameters:
`key` - The attribute key to check.
Returns:
true if the attribute exists, false if not.

  - 

### removeAttr

public Node removeAttr(String key)
Description copied from class: `Node`
Remove an attribute from this node.

Overrides:
`removeAttr` in class `Node`
Parameters:
`key` - The attribute to remove.
Returns:
this (for chaining)

  - 

### absUrl

public String absUrl(String key)
Description copied from class: `Node`
Get an absolute URL from a URL attribute that may be relative (such as an `<a href>` or
 `<img src>`).
 

 E.g.: `String absUrl = linkEl.absUrl("href");`
 
 

 If the attribute value is already absolute (i.e. it starts with a protocol, like
 `http://` or `https://` etc), and it successfully parses as a URL, the attribute is
 returned directly. Otherwise, it is treated as a URL relative to the element's `Node.baseUri()`, and made
 absolute using that.
 
 

 As an alternate, you can use the `Node.attr(java.lang.String)` method with the `abs:` prefix, e.g.:
 `String absUrl = linkEl.attr("abs:href");`
 

Overrides:
`absUrl` in class `Node`
Parameters:
`key` - The attribute key
Returns:
An absolute URL if one could be made, or an empty string (not null) if the attribute was missing or
 could not be made successfully into a URL.
See Also:

    - `Node.attr(java.lang.String)`

    - `URL(java.net.URL, String)`

  - 

### baseUri

public String baseUri()
Description copied from class: `Node`
Get the base URI that applies to this node. Will return an empty string if not defined. Used to make relative links
     absolute.

Specified by:
`baseUri` in class `Node`
Returns:
base URI
See Also:

    - `Node.absUrl(java.lang.String)`

  - 

### doSetBaseUri

protected void doSetBaseUri(String baseUri)
Description copied from class: `Node`
Set the baseUri for just this node (not its descendants), if this Node tracks base URIs.

Specified by:
`doSetBaseUri` in class `Node`
Parameters:
`baseUri` - new URI

  - 

### childNodeSize

public int childNodeSize()
Description copied from class: `Node`
Get the number of child nodes that this node holds.

Specified by:
`childNodeSize` in class `Node`
Returns:
the number of child nodes that this node holds.

  - 

### empty

public Node empty()
Description copied from class: `Node`
Delete all this node's children.

Specified by:
`empty` in class `Node`
Returns:
this node, for chaining

  - 

### ensureChildNodes

protected List<Node> ensureChildNodes()

Specified by:
`ensureChildNodes` in class `Node`

  - 

### doClone

protected LeafNode doClone(Node parent)

Overrides:
`doClone` in class `Node`