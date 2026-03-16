Package org.jsoup.nodes

# Class Node

java.lang.Object
org.jsoup.nodes.Node

All Implemented Interfaces:
`Cloneable`

Direct Known Subclasses:
`Element`, `LeafNode`

---

public abstract class Node
extends Object
implements Cloneable
The base, abstract Node model. `Element`, `Document`, `Comment`, `TextNode`, et al.,
 are instances of Node.

Author:
Jonathan Hedley, [email protected]

- 

## Constructor Summary

Constructors

Modifier
Constructor
Description
`protected `
`Node()`

Default constructor.

- 

## Method Summary

Modifier and Type
Method
Description
`String`
`absUrl(String attributeKey)`

Get an absolute URL from a URL attribute that may be relative (such as an `<a href>` or
 `<img src>`).

`protected void`
`addChildren(int index,
 Node... children)`
 
`protected void`
`addChildren(Node... children)`
 
`Node`
`after(String html)`

Insert the specified HTML into the DOM after this node (as a following sibling).

`Node`
`after(Node node)`

Insert the specified node into the DOM after this node (as a following sibling).

`String`
`attr(String attributeKey)`

Get an attribute's value by its key.

`Node`
`attr(String attributeKey,
 String attributeValue)`

Set an attribute (key=value).

`abstract Attributes`
`attributes()`

Get each of the Element's attributes.

`int`
`attributesSize()`

Get the number of attributes that this Node has.

`abstract String`
`baseUri()`

Get the base URI that applies to this node.

`Node`
`before(String html)`

Insert the specified HTML into the DOM before this node (as a preceding sibling).

`Node`
`before(Node node)`

Insert the specified node into the DOM before this node (as a preceding sibling).

`Node`
`childNode(int index)`

Get a child node by its 0-based index.

`List<Node>`
`childNodes()`

Get this node's children.

`protected Node[]`
`childNodesAsArray()`
 
`List<Node>`
`childNodesCopy()`

Returns a deep copy of this node's children.

`abstract int`
`childNodeSize()`

Get the number of child nodes that this node holds.

`Node`
`clearAttributes()`

Clear (remove) each of the attributes in this node.

`Node`
`clone()`

Create a stand-alone, deep copy of this node, and all of its children.

`protected Node`
`doClone(@Nullable Node parent)`
 
`protected abstract void`
`doSetBaseUri(String baseUri)`

Set the baseUri for just this node (not its descendants), if this Node tracks base URIs.

`abstract Node`
`empty()`

Delete all this node's children.

`protected abstract List<Node>`
`ensureChildNodes()`
 
`boolean`
`equals(@Nullable Object o)`

Check if this node is the same instance of another (object identity test).

`Node`
`filter(NodeFilter nodeFilter)`

Perform a depth-first controllable traversal through this node and its descendants.

`@Nullable Node`
`firstChild()`

Gets the first child node of this node, or `null` if there is none.

`Node`
`firstSibling()`

Gets the first sibling of this node.

`Node`
`forEachNode(Consumer<? super Node> action)`

Perform the supplied action on this Node and each of its descendants, during a depth-first traversal.

`boolean`
`hasAttr(String attributeKey)`

Test if this Node has an attribute.

`protected abstract boolean`
`hasAttributes()`

Check if this Node has an actual Attributes object.

`int`
`hashCode()`

Provides a hashCode for this Node, based on its object identity.

`boolean`
`hasParent()`

Checks if this node has a parent.

`boolean`
`hasSameValue(@Nullable Object o)`

Check if this node has the same content as another node.

`<T extends Appendable>
T`
`html(T appendable)`

Write this node and its children to the given `Appendable`.

`protected void`
`indent(Appendable accum,
 int depth,
 Document.OutputSettings out)`

Deprecated.
internal method moved into Printer; will be removed in jsoup 1.24.1.

`@Nullable Node`
`lastChild()`

Gets the last child node of this node, or `null` if there is none.

`Node`
`lastSibling()`

Gets the last sibling of this node.

`boolean`
`nameIs(String normalName)`

Test if this node has the specified normalized name, in any namespace.

`@Nullable Element`
`nextElementSibling()`

Gets the next sibling Element of this node.

`@Nullable Node`
`nextSibling()`

Get this node's next sibling.

`abstract String`
`nodeName()`

Get the node name of this node.

`Stream<Node>`
`nodeStream()`

Returns a Stream of this Node and all of its descendant Nodes.

`<T extends Node>
Stream<T>`
`nodeStream(Class<T> type)`

Returns a Stream of this and descendant nodes, containing only nodes of the specified type.

`String`
`nodeValue()`

Get the node's value.

`String`
`normalName()`

Get the normalized name of this node.

`String`
`outerHtml()`

Get the outer HTML of this node.

`protected void`
`outerHtml(Appendable accum)`
 
`protected void`
`outerHtml(org.jsoup.internal.QuietAppendable accum)`
 
`@Nullable Document`
`ownerDocument()`

Gets the Document associated with this Node.

`@Nullable Node`
`parent()`

Gets this node's parent node.

`@Nullable Element`
`parentElement()`

Gets this node's parent Element.

`boolean`
`parentElementIs(String normalName,
 String namespace)`

Test if this node's parent is an Element with the specified normalized name and namespace.

`boolean`
`parentNameIs(String normalName)`

Test if this node's parent has the specified normalized name.

`final @Nullable Node`
`parentNode()`

Gets this node's parent node.

`@Nullable Element`
`previousElementSibling()`

Gets the previous Element sibling of this node.

`@Nullable Node`
`previousSibling()`

Get this node's previous sibling.

`void`
`remove()`

Remove (delete) this node from the DOM tree.

`Node`
`removeAttr(String attributeKey)`

Remove an attribute from this node.

`protected void`
`removeChild(Node out)`
 
`protected void`
`reparentChild(Node child)`
 
`protected void`
`replaceChild(Node out,
 Node in)`
 
`void`
`replaceWith(Node in)`

Replace this node in the DOM with the supplied node.

`Node`
`root()`

Get this node's root node; that is, its topmost ancestor.

`void`
`setBaseUri(String baseUri)`

Update the base URI of this node and all of its descendants.

`protected void`
`setParentNode(Node parentNode)`
 
`protected void`
`setSiblingIndex(int siblingIndex)`
 
`Node`
`shallowClone()`

Create a stand-alone, shallow copy of this node.

`int`
`siblingIndex()`

Get the list index of this node in its node sibling list.

`List<Node>`
`siblingNodes()`

Retrieves this node's sibling nodes.

`Range`
`sourceRange()`

Get the source range (start and end positions) in the original input source from which this node was parsed.

`String`
`toString()`

Gets this node's outer HTML.

`Node`
`traverse(NodeVisitor nodeVisitor)`

Perform a depth-first traversal through this node and its descendants.

`@Nullable Node`
`unwrap()`

Removes this node from the DOM, and moves its children up into the node's parent.

`Node`
`wrap(String html)`

Wrap the supplied HTML around this node.

### Methods inherited from class java.lang.Object

`finalize, getClass, notify, notifyAll, wait, wait, wait`

- 

## Constructor Details

  - 

### Node

protected Node()
Default constructor. Doesn't set up base uri, children, or attributes; use with caution.

- 

## Method Details

  - 

### nodeName

public abstract String nodeName()
Get the node name of this node. Use for debugging purposes and not logic switching (for that, use instanceof).

Returns:
node name

  - 

### normalName

public String normalName()
Get the normalized name of this node. For node types other than Element, this is the same as `nodeName()`.
     For an Element, will be the lower-cased tag name.

Returns:
normalized node name
Since:
1.15.4.

  - 

### nodeValue

public String nodeValue()
Get the node's value. For a TextNode, the whole text; for a Comment, the comment data; for an Element,
     wholeOwnText. Returns "" if there is no value.

Returns:
the node's value

  - 

### nameIs

public boolean nameIs(String normalName)
Test if this node has the specified normalized name, in any namespace.

Parameters:
`normalName` - a normalized element name (e.g. `div`).
Returns:
true if the element's normal name matches exactly
Since:
1.17.2

  - 

### parentNameIs

public boolean parentNameIs(String normalName)
Test if this node's parent has the specified normalized name.

Parameters:
`normalName` - a normalized name (e.g. `div`).
Returns:
true if the parent element's normal name matches exactly
Since:
1.17.2

  - 

### parentElementIs

public boolean parentElementIs(String normalName,
 String namespace)
Test if this node's parent is an Element with the specified normalized name and namespace.

Parameters:
`normalName` - a normalized element name (e.g. `div`).
`namespace` - the namespace
Returns:
true if the parent element's normal name matches exactly, and that element is in the specified namespace
Since:
1.17.2

  - 

### hasAttributes

protected abstract boolean hasAttributes()
Check if this Node has an actual Attributes object.

  - 

### hasParent

public boolean hasParent()
Checks if this node has a parent. Nodes won't have parents if (e.g.) they are newly created and not added as a child
     to an existing node, or if they are a `shallowClone()`. In such cases, `parent()` will return `null`.

Returns:
if this node has a parent.

  - 

### attr

public String attr(String attributeKey)
Get an attribute's value by its key. **Case insensitive**
 

 To get an absolute URL from an attribute that may be a relative URL, prefix the key with `**abs:**`,
 which is a shortcut to the `absUrl(java.lang.String)` method.
 
 E.g.:
 `String url = a.attr("abs:href");`

Parameters:
`attributeKey` - The attribute key.
Returns:
The attribute, or empty string if not present (to avoid nulls).
See Also:

    - `attributes()`

    - `hasAttr(String)`

    - `absUrl(String)`

  - 

### attributes

public abstract Attributes attributes()
Get each of the Element's attributes.

Returns:
attributes (which implements Iterable, with the same order as presented in the original HTML).

  - 

### attributesSize

public int attributesSize()
Get the number of attributes that this Node has.

Returns:
the number of attributes
Since:
1.14.2

  - 

### attr

public Node attr(String attributeKey,
 String attributeValue)
Set an attribute (key=value). If the attribute already exists, it is replaced. The attribute key comparison is
 **case insensitive**. The key will be set with case sensitivity as set in the parser settings.

Parameters:
`attributeKey` - The attribute key.
`attributeValue` - The attribute value.
Returns:
this (for chaining)

  - 

### hasAttr

public boolean hasAttr(String attributeKey)
Test if this Node has an attribute. **Case insensitive**.

Parameters:
`attributeKey` - The attribute key to check.
Returns:
true if the attribute exists, false if not.

  - 

### removeAttr

public Node removeAttr(String attributeKey)
Remove an attribute from this node.

Parameters:
`attributeKey` - The attribute to remove.
Returns:
this (for chaining)

  - 

### clearAttributes

public Node clearAttributes()
Clear (remove) each of the attributes in this node.

Returns:
this, for chaining

  - 

### baseUri

public abstract String baseUri()
Get the base URI that applies to this node. Will return an empty string if not defined. Used to make relative links
     absolute.

Returns:
base URI
See Also:

    - `absUrl(java.lang.String)`

  - 

### doSetBaseUri

protected abstract void doSetBaseUri(String baseUri)
Set the baseUri for just this node (not its descendants), if this Node tracks base URIs.

Parameters:
`baseUri` - new URI

  - 

### setBaseUri

public void setBaseUri(String baseUri)
Update the base URI of this node and all of its descendants.

Parameters:
`baseUri` - base URI to set

  - 

### absUrl

public String absUrl(String attributeKey)
Get an absolute URL from a URL attribute that may be relative (such as an `<a href>` or
 `<img src>`).
 

 E.g.: `String absUrl = linkEl.absUrl("href");`
 
 

 If the attribute value is already absolute (i.e. it starts with a protocol, like
 `http://` or `https://` etc), and it successfully parses as a URL, the attribute is
 returned directly. Otherwise, it is treated as a URL relative to the element's `baseUri()`, and made
 absolute using that.
 
 

 As an alternate, you can use the `attr(java.lang.String)` method with the `abs:` prefix, e.g.:
 `String absUrl = linkEl.attr("abs:href");`
 

Parameters:
`attributeKey` - The attribute key
Returns:
An absolute URL if one could be made, or an empty string (not null) if the attribute was missing or
 could not be made successfully into a URL.
See Also:

    - `attr(java.lang.String)`

    - `URL(java.net.URL, String)`

  - 

### ensureChildNodes

protected abstract List<Node> ensureChildNodes()

  - 

### childNode

public Node childNode(int index)
Get a child node by its 0-based index.

Parameters:
`index` - index of child node
Returns:
the child node at this index.
Throws:
`IndexOutOfBoundsException` - if the index is out of bounds.

  - 

### childNodes

public List<Node> childNodes()
Get this node's children. Presented as an unmodifiable list: new children can not be added, but the child nodes
     themselves can be manipulated.

Returns:
list of children. If no children, returns an empty list.

  - 

### childNodesCopy

public List<Node> childNodesCopy()
Returns a deep copy of this node's children. Changes made to these nodes will not be reflected in the original
 nodes

Returns:
a deep copy of this node's children

  - 

### childNodeSize

public abstract int childNodeSize()
Get the number of child nodes that this node holds.

Returns:
the number of child nodes that this node holds.

  - 

### childNodesAsArray

protected Node[] childNodesAsArray()

  - 

### empty

public abstract Node empty()
Delete all this node's children.

Returns:
this node, for chaining

  - 

### parent

public @Nullable Node parent()
Gets this node's parent node. This is always an Element.

Returns:
parent node; or null if no parent.
See Also:

    - `hasParent()`

  - 

### parentElement

public @Nullable Element parentElement()
Gets this node's parent Element.

Returns:
parent element; or null if this node has no parent.
Since:
1.21.1
See Also:

    - `hasParent()`

  - 

### parentNode

public final @Nullable Node parentNode()
Gets this node's parent node. Not overridable by extending classes, so useful if you really just need the Node type.

Returns:
parent node; or null if no parent.

  - 

### root

public Node root()
Get this node's root node; that is, its topmost ancestor. If this node is the top ancestor, returns `this`.

Returns:
topmost ancestor.

  - 

### ownerDocument

public @Nullable Document ownerDocument()
Gets the Document associated with this Node.

Returns:
the Document associated with this Node, or null if there is no such Document.

  - 

### remove

public void remove()
Remove (delete) this node from the DOM tree. If this node has children, they are also removed. If this node is
 an orphan, nothing happens.

  - 

### before

public Node before(String html)
Insert the specified HTML into the DOM before this node (as a preceding sibling).

Parameters:
`html` - HTML to add before this node
Returns:
this node, for chaining
See Also:

    - `after(String)`

  - 

### before

public Node before(Node node)
Insert the specified node into the DOM before this node (as a preceding sibling).

Parameters:
`node` - to add before this node
Returns:
this node, for chaining
See Also:

    - `after(Node)`

  - 

### after

public Node after(String html)
Insert the specified HTML into the DOM after this node (as a following sibling).

Parameters:
`html` - HTML to add after this node
Returns:
this node, for chaining
See Also:

    - `before(String)`

  - 

### after

public Node after(Node node)
Insert the specified node into the DOM after this node (as a following sibling).

Parameters:
`node` - to add after this node
Returns:
this node, for chaining
See Also:

    - `before(Node)`

  - 

### wrap

public Node wrap(String html)
Wrap the supplied HTML around this node.

Parameters:
`html` - HTML to wrap around this node, e.g. `<div class="head"></div>`. Can be arbitrarily deep. If
     the input HTML does not parse to a result starting with an Element, this will be a no-op.
Returns:
this node, for chaining.

  - 

### unwrap

public @Nullable Node unwrap()
Removes this node from the DOM, and moves its children up into the node's parent. This has the effect of dropping
 the node but keeping its children.
 

 For example, with the input html:
 
 

`<div>One <span>Two <b>Three</b></span></div>`
 Calling `element.unwrap()` on the `span` element will result in the html:
 

`<div>One Two <b>Three</b></div>`
 and the `"Two "` `TextNode` being returned.

Returns:
the first child of this node, after the node has been unwrapped. @{code Null} if the node had no children.
See Also:

    - `remove()`

    - `wrap(String)`

  - 

### replaceWith

public void replaceWith(Node in)
Replace this node in the DOM with the supplied node.

Parameters:
`in` - the node that will replace the existing node.

  - 

### setParentNode

protected void setParentNode(Node parentNode)

  - 

### replaceChild

protected void replaceChild(Node out,
 Node in)

  - 

### removeChild

protected void removeChild(Node out)

  - 

### addChildren

protected void addChildren(Node... children)

  - 

### addChildren

protected void addChildren(int index,
 Node... children)

  - 

### reparentChild

protected void reparentChild(Node child)

  - 

### siblingNodes

public List<Node> siblingNodes()
Retrieves this node's sibling nodes. Similar to `node.parent.childNodes()`, but does not
     include this node (a node is not a sibling of itself).

Returns:
node siblings. If the node has no parent, returns an empty list.

  - 

### nextSibling

public @Nullable Node nextSibling()
Get this node's next sibling.

Returns:
next sibling, or `null` if this is the last sibling

  - 

### previousSibling

public @Nullable Node previousSibling()
Get this node's previous sibling.

Returns:
the previous sibling, or @{code null} if this is the first sibling

  - 

### siblingIndex

public int siblingIndex()
Get the list index of this node in its node sibling list. E.g. if this is the first node
 sibling, returns 0.

Returns:
position in node sibling list
See Also:

    - `Element.elementSiblingIndex()`

  - 

### setSiblingIndex

protected void setSiblingIndex(int siblingIndex)

  - 

### firstChild

public @Nullable Node firstChild()
Gets the first child node of this node, or `null` if there is none. This could be any Node type, such as an
     Element, TextNode, Comment, etc. Use `Element.firstElementChild()` to get the first Element child.

Returns:
the first child node, or null if there are no children.
Since:
1.15.2
See Also:

    - `Element.firstElementChild()`

    - `lastChild()`

  - 

### lastChild

public @Nullable Node lastChild()
Gets the last child node of this node, or `null` if there is none.

Returns:
the last child node, or null if there are no children.
Since:
1.15.2
See Also:

    - `Element.lastElementChild()`

    - `firstChild()`

  - 

### firstSibling

public Node firstSibling()
Gets the first sibling of this node. That may be this node.

Returns:
the first sibling node
Since:
1.21.1

  - 

### lastSibling

public Node lastSibling()
Gets the last sibling of this node. That may be this node.

Returns:
the last sibling (aka the parent's last child)
Since:
1.21.1

  - 

### nextElementSibling

public @Nullable Element nextElementSibling()
Gets the next sibling Element of this node. E.g., if a `div` contains two `p`s, the
     `nextElementSibling` of the first `p` is the second `p`.
     

This is similar to `nextSibling()`, but specifically finds only Elements.

Returns:
the next element, or null if there is no next element
See Also:

    - `previousElementSibling()`

  - 

### previousElementSibling

public @Nullable Element previousElementSibling()
Gets the previous Element sibling of this node.

Returns:
the previous element, or null if there is no previous element
See Also:

    - `nextElementSibling()`

  - 

### traverse

public Node traverse(NodeVisitor nodeVisitor)
Perform a depth-first traversal through this node and its descendants.

Parameters:
`nodeVisitor` - the visitor callbacks to perform on each node
Returns:
this node, for chaining

  - 

### forEachNode

public Node forEachNode(Consumer<? super Node> action)
Perform the supplied action on this Node and each of its descendants, during a depth-first traversal. Nodes may be
     inspected, changed, added, replaced, or removed.

Parameters:
`action` - the function to perform on the node
Returns:
this Node, for chaining
See Also:

    - `Element.forEach(Consumer)`

  - 

### filter

public Node filter(NodeFilter nodeFilter)
Perform a depth-first controllable traversal through this node and its descendants.

Parameters:
`nodeFilter` - the filter callbacks to perform on each node
Returns:
this node, for chaining

  - 

### nodeStream

public Stream<Node> nodeStream()
Returns a Stream of this Node and all of its descendant Nodes. The stream has document order.

Returns:
a stream of all nodes.
Since:
1.17.1
See Also:

    - `Element.stream()`

  - 

### nodeStream

public <T extends Node> Stream<T> nodeStream(Class<T> type)
Returns a Stream of this and descendant nodes, containing only nodes of the specified type. The stream has document
     order.

Returns:
a stream of nodes filtered by type.
Since:
1.17.1
See Also:

    - `Element.stream()`

  - 

### outerHtml

public String outerHtml()
Get the outer HTML of this node. For example, on a `p` element, may return `<p>Para</p>`.

Returns:
outer HTML
See Also:

    - `Element.html()`

    - `Element.text()`

  - 

### outerHtml

protected void outerHtml(Appendable accum)

  - 

### outerHtml

protected void outerHtml(org.jsoup.internal.QuietAppendable accum)

  - 

### html

public <T extends Appendable> T html(T appendable)
Write this node and its children to the given `Appendable`.

Parameters:
`appendable` - the `Appendable` to write to.
Returns:
the supplied `Appendable`, for chaining.
Throws:
`SerializationException` - if the appendable throws an IOException.

  - 

### sourceRange

public Range sourceRange()
Get the source range (start and end positions) in the original input source from which this node was parsed.
     Position tracking must be enabled prior to parsing the content. For an Element, this will be the positions of the
     start tag.

Returns:
the range for the start of the node, or `untracked` if its range was not tracked.
Since:
1.15.2
See Also:

    - `Parser.setTrackPosition(boolean)`

    - `Range.isImplicit()`

    - `Element.endSourceRange()`

    - `Attributes.sourceRange(String name)`

  - 

### toString

public String toString()
Gets this node's outer HTML.

Overrides:
`toString` in class `Object`
Returns:
outer HTML.
See Also:

    - `outerHtml()`

  - 

### indent

@Deprecated
protected void indent(Appendable accum,
 int depth,
 Document.OutputSettings out)
               throws IOException
Deprecated.
internal method moved into Printer; will be removed in jsoup 1.24.1.

Throws:
`IOException`

  - 

### equals

public boolean equals(@Nullable Object o)
Check if this node is the same instance of another (object identity test).
 

For a node value equality check, see `hasSameValue(Object)`

Overrides:
`equals` in class `Object`
Parameters:
`o` - other object to compare to
Returns:
true if the content of this node is the same as the other
See Also:

    - `hasSameValue(Object)`

  - 

### hashCode

public int hashCode()
Provides a hashCode for this Node, based on its object identity. Changes to the Node's content will not impact the
     result.

Overrides:
`hashCode` in class `Object`
Returns:
an object identity based hashcode for this Node

  - 

### hasSameValue

public boolean hasSameValue(@Nullable Object o)
Check if this node has the same content as another node. A node is considered the same if its name, attributes and content match the
 other node; particularly its position in the tree does not influence its similarity.

Parameters:
`o` - other object to compare to
Returns:
true if the content of this node is the same as the other

  - 

### clone

public Node clone()
Create a stand-alone, deep copy of this node, and all of its children. The cloned node will have no siblings.
     

     
    - If this node is a `LeafNode`, the clone will have no parent.
     
    - If this node is an `Element`, the clone will have a simple owning `Document` to retain the
     configured output settings and parser.
     

     

The cloned node may be adopted into another Document or node structure using
     `Element.appendChild(Node)`.

Overrides:
`clone` in class `Object`
Returns:
a stand-alone cloned node, including clones of any children
See Also:

    - `shallowClone()`

  - 

### shallowClone

public Node shallowClone()
Create a stand-alone, shallow copy of this node. None of its children (if any) will be cloned, and it will have
 no parent or sibling nodes.

Returns:
a single independent copy of this node
See Also:

    - `clone()`

  - 

### doClone

protected Node doClone(@Nullable Node parent)