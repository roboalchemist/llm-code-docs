Package org.jsoup.nodes

# Class Element

java.lang.Object
org.jsoup.nodes.Node
org.jsoup.nodes.Element

All Implemented Interfaces:
`Cloneable`, `Iterable<Element>`

Direct Known Subclasses:
`Document`, `FormElement`, `PseudoTextElement`

---

public class Element
extends Node
implements Iterable<Element>
An HTML Element consists of a tag name, attributes, and child nodes (including text nodes and other elements).
 

 From an Element, you can extract data, traverse the node graph, and manipulate the HTML.

- 

## Constructor Summary

Constructors

Constructor
Description
`Element(String tag)`

Create a new, standalone element, in the HTML namespace.

`Element(String tag,
 String namespace)`

Create a new, standalone element, in the specified namespace.

`Element(Tag tag,
 @Nullable String baseUri)`

Create a new Element from a Tag and a base URI.

`Element(Tag tag,
 @Nullable String baseUri,
 @Nullable Attributes attributes)`

Create a new, standalone Element.

- 

## Method Summary

Modifier and Type
Method
Description
`Element`
`addClass(String className)`

Add a class name to this element's `class` attribute.

`Element`
`after(String html)`

Insert the specified HTML into the DOM after this element (as a following sibling).

`Element`
`after(Node node)`

Insert the specified node into the DOM after this node (as a following sibling).

`Element`
`append(String html)`

Add inner HTML to this element.

`Element`
`appendChild(Node child)`

Insert a node to the end of this Element's children.

`Element`
`appendChildren(Collection<? extends Node> children)`

Insert the given nodes to the end of this Element's children.

`Element`
`appendElement(String tagName)`

Create a new element by tag name, and add it as this Element's last child.

`Element`
`appendElement(String tagName,
 String namespace)`

Create a new element by tag name and namespace, add it as this Element's last child.

`Element`
`appendText(String text)`

Create and append a new TextNode to this element.

`Element`
`appendTo(Element parent)`

Add this element to the supplied parent element, as its next child.

`Element`
`attr(String attributeKey,
 boolean attributeValue)`

Set a boolean attribute value on this element.

`Element`
`attr(String attributeKey,
 String attributeValue)`

Set an attribute value on this element.

`@Nullable Attribute`
`attribute(String key)`

Get an Attribute by key.

`Attributes`
`attributes()`

Get each of the Element's attributes.

`String`
`baseUri()`

Get the base URI that applies to this node.

`Element`
`before(String html)`

Insert the specified HTML into the DOM before this element (as a preceding sibling).

`Element`
`before(Node node)`

Insert the specified node into the DOM before this node (as a preceding sibling).

`Element`
`child(int index)`

Get a child element of this element, by its 0-based index number.

`int`
`childNodeSize()`

Get the number of child nodes that this node holds.

`Elements`
`children()`

Get this element's child elements.

`int`
`childrenSize()`

Get the number of child nodes of this element that are elements.

`String`
`className()`

Gets the literal value of this element's "class" attribute, which may include multiple class names, space
 separated.

`Set<String>`
`classNames()`

Get each of the element's class names.

`Element`
`classNames(Set<String> classNames)`

Set the element's `class` attribute to the supplied class names.

`Element`
`clearAttributes()`

Clear (remove) each of the attributes in this node.

`Element`
`clone()`

Create a stand-alone, deep copy of this node, and all of its children.

`@Nullable Element`
`closest(String cssQuery)`

Find the closest element up the tree of parents that matches the specified CSS query.

`@Nullable Element`
`closest(Evaluator evaluator)`

Find the closest element up the tree of parents that matches the specified evaluator.

`String`
`cssSelector()`

Get a CSS selector that will uniquely select this element.

`String`
`data()`

Get the combined data of this element.

`List<DataNode>`
`dataNodes()`

Get this element's child data nodes.

`Map<String,String>`
`dataset()`

Get this element's HTML5 custom data attributes.

`protected Element`
`doClone(@Nullable Node parent)`
 
`protected void`
`doSetBaseUri(String baseUri)`

Set the baseUri for just this node (not its descendants), if this Node tracks base URIs.

`boolean`
`elementIs(String normalName,
 String namespace)`

Test if this Element has the specified normalized name, and is in the specified namespace.

`int`
`elementSiblingIndex()`

Get the list index of this element in its element sibling list.

`Element`
`empty()`

Remove all the element's child nodes.

`Range`
`endSourceRange()`

Get the source range (start and end positions) of the end (closing) tag for this Element.

`protected List<Node>`
`ensureChildNodes()`
 
`Element`
`expectFirst(String cssQuery)`

Just like `selectFirst(String)`, but if there is no match, throws an `IllegalArgumentException`.

`<T extends Node>
T`
`expectFirstNode(String cssQuery,
 Class<T> type)`

Just like `selectFirstNode(String, Class)`, but if there is no match, throws an
     `IllegalArgumentException`.

`Element`
`filter(NodeFilter nodeFilter)`

Perform a depth-first controllable traversal through this node and its descendants.

`@Nullable Element`
`firstElementChild()`

Gets the first child of this Element that is an Element, or `null` if there is none.

`Element`
`firstElementSibling()`

Gets the first Element sibling of this element.

`void`
`forEach(Consumer<? super Element> action)`

Perform the supplied action on this Element and each of its descendant Elements, during a depth-first traversal.

`Element`
`forEachNode(Consumer<? super Node> action)`

Perform the supplied action on this Node and each of its descendants, during a depth-first traversal.

`Elements`
`getAllElements()`

Find all elements under this element (including self, and children of children).

`@Nullable Element`
`getElementById(String id)`

Find an element by ID, including or under this element.

`Elements`
`getElementsByAttribute(String key)`

Find elements that have a named attribute set.

`Elements`
`getElementsByAttributeStarting(String keyPrefix)`

Find elements that have an attribute name starting with the supplied prefix.

`Elements`
`getElementsByAttributeValue(String key,
 String value)`

Find elements that have an attribute with the specific value.

`Elements`
`getElementsByAttributeValueContaining(String key,
 String match)`

Find elements that have attributes whose value contains the match string.

`Elements`
`getElementsByAttributeValueEnding(String key,
 String valueSuffix)`

Find elements that have attributes that end with the value suffix.

`Elements`
`getElementsByAttributeValueMatching(String key,
 String regex)`

Find elements that have attributes whose values match the supplied regular expression.

`Elements`
`getElementsByAttributeValueMatching(String key,
 Pattern pattern)`

Find elements that have an attribute whose value matches the supplied regular expression.

`Elements`
`getElementsByAttributeValueNot(String key,
 String value)`

Find elements that either do not have this attribute, or have it with a different value.

`Elements`
`getElementsByAttributeValueStarting(String key,
 String valuePrefix)`

Find elements that have attributes that start with the value prefix.

`Elements`
`getElementsByClass(String className)`

Find elements that have this class, including or under this element.

`Elements`
`getElementsByIndexEquals(int index)`

Find elements whose sibling index is equal to the supplied index.

`Elements`
`getElementsByIndexGreaterThan(int index)`

Find elements whose sibling index is greater than the supplied index.

`Elements`
`getElementsByIndexLessThan(int index)`

Find elements whose sibling index is less than the supplied index.

`Elements`
`getElementsByTag(String tagName)`

Finds elements, including and recursively under this element, with the specified tag name.

`Elements`
`getElementsContainingOwnText(String searchText)`

Find elements that directly contain the specified string.

`Elements`
`getElementsContainingText(String searchText)`

Find elements that contain the specified string.

`Elements`
`getElementsMatchingOwnText(String regex)`

Find elements whose own text matches the supplied regular expression.

`Elements`
`getElementsMatchingOwnText(Pattern pattern)`

Find elements whose own text matches the supplied regular expression.

`Elements`
`getElementsMatchingText(String regex)`

Find elements whose text matches the supplied regular expression.

`Elements`
`getElementsMatchingText(Pattern pattern)`

Find elements whose text matches the supplied regular expression.

`protected boolean`
`hasAttributes()`

Check if this Node has an actual Attributes object.

`protected boolean`
`hasChildNodes()`

Internal test to check if a nodelist object has been created.

`boolean`
`hasClass(String className)`

Tests if this element has a class.

`boolean`
`hasText()`

Checks if the current element or any of its child elements contain non-whitespace text.

`String`
`html()`

Retrieves the element's inner HTML.

`Element`
`html(String html)`

Set this element's inner HTML.

`<T extends Appendable>
T`
`html(T accum)`

Write this node and its children to the given `Appendable`.

`String`
`id()`

Get the `id` attribute of this element.

`Element`
`id(String id)`

Set the `id` attribute of this element.

`Element`
`insertChildren(int index,
 Collection<? extends Node> children)`

Inserts the given child nodes into this element at the specified index.

`Element`
`insertChildren(int index,
 Node... children)`

Inserts the given child nodes into this element at the specified index.

`boolean`
`is(String cssQuery)`

Checks if this element matches the given `Selector` CSS query.

`boolean`
`is(Evaluator evaluator)`

Check if this element matches the given evaluator.

`boolean`
`isBlock()`

Test if this element is a block-level element.

`Iterator<Element>`
`iterator()`

Returns an Iterator that iterates this Element and each of its descendant Elements, in document order.

`@Nullable Element`
`lastElementChild()`

Gets the last child of this Element that is an Element, or @{code null} if there is none.

`Element`
`lastElementSibling()`

Gets the last element sibling of this element.

`Elements`
`nextElementSiblings()`

Get each of the sibling elements that come after this element.

`String`
`nodeName()`

Get the node name of this node.

`String`
`nodeValue()`

An Element's nodeValue is its whole own text.

`String`
`normalName()`

Get the normalized name of this Element's tag.

`String`
`ownText()`

Gets the (normalized) text owned by this element only; does not get the combined text of all children.

`final @Nullable Element`
`parent()`

Gets this node's parent node.

`Elements`
`parents()`

Get this element's parent and ancestors, up to the document root.

`Element`
`prepend(String html)`

Add inner HTML into this element.

`Element`
`prependChild(Node child)`

Add a node to the start of this element's children.

`Element`
`prependChildren(Collection<? extends Node> children)`

Insert the given nodes to the start of this Element's children.

`Element`
`prependElement(String tagName)`

Create a new element by tag name, and add it as this Element's first child.

`Element`
`prependElement(String tagName,
 String namespace)`

Create a new element by tag name and namespace, and add it as this Element's first child.

`Element`
`prependText(String text)`

Create and prepend a new TextNode to this element.

`Elements`
`previousElementSiblings()`

Get each of the element siblings before this element.

`Element`
`removeAttr(String attributeKey)`

Remove an attribute from this node.

`Element`
`removeClass(String className)`

Remove a class name from this element's `class` attribute.

`Element`
`root()`

Get this node's root node; that is, its topmost ancestor.

`Elements`
`select(String cssQuery)`

Find elements that match the `Selector` CSS query, with this element as the starting context.

`Elements`
`select(Evaluator evaluator)`

Find elements that match the supplied Evaluator.

`@Nullable Element`
`selectFirst(String cssQuery)`

Find the first Element that matches the `Selector` CSS query, with this element as the starting context.

`@Nullable Element`
`selectFirst(Evaluator evaluator)`

Finds the first Element that matches the supplied Evaluator, with this element as the starting context, or
 `null` if none match.

`<T extends Node>
@Nullable T`
`selectFirstNode(String cssQuery,
 Class<T> type)`

Find the first Node that matches the `Selector` CSS query, with this element as the starting context.

`<T extends Node>
@Nullable T`
`selectFirstNode(Evaluator evaluator,
 Class<T> type)`

Finds the first Node that matches the supplied Evaluator, with this element as the starting context, or
     `null` if none match.

`Nodes<Node>`
`selectNodes(String cssQuery)`

Find nodes that match the supplied `Selector` CSS query, with this element as the starting context.

`<T extends Node>
Nodes<T>`
`selectNodes(String cssQuery,
 Class<T> type)`

Find nodes that match the supplied `Selector` CSS query, with this element as the starting context.

`Nodes<Node>`
`selectNodes(Evaluator evaluator)`

Find nodes that match the supplied `Evaluator`, with this element as the starting context.

`<T extends Node>
Nodes<T>`
`selectNodes(Evaluator evaluator,
 Class<T> type)`

Find nodes that match the supplied Evaluator, with this element as the starting context.

`Stream<Element>`
`selectStream(String cssQuery)`

Selects elements from the given root that match the specified `Selector` CSS query, with this element as the
     starting context, and returns them as a lazy Stream.

`Stream<Element>`
`selectStream(Evaluator evaluator)`

Find a Stream of elements that match the supplied Evaluator.

`Elements`
`selectXpath(String xpath)`

Find Elements that match the supplied XPath expression.

`<T extends Node>
List<T>`
`selectXpath(String xpath,
 Class<T> nodeType)`

Find Nodes that match the supplied XPath expression.

`Element`
`shallowClone()`

Create a stand-alone, shallow copy of this node.

`Elements`
`siblingElements()`

Get sibling elements.

`Stream<Element>`
`stream()`

Returns a Stream of this Element and all of its descendant Elements.

`Tag`
`tag()`

Get the Tag for this element.

`Element`
`tag(Tag tag)`

Change the Tag of this element.

`String`
`tagName()`

Get the name of the tag for this element.

`Element`
`tagName(String tagName)`

Change (rename) the tag of this element.

`Element`
`tagName(String tagName,
 String namespace)`

Change (rename) the tag of this element.

`String`
`text()`

Gets the **normalized, combined text** of this element and all its children.

`Element`
`text(String text)`

Set the text of this element.

`List<TextNode>`
`textNodes()`

Get this element's child text nodes.

`Element`
`toggleClass(String className)`

Toggle a class name on this element's `class` attribute: if present, remove it; otherwise add it.

`Element`
`traverse(NodeVisitor nodeVisitor)`

Perform a depth-first traversal through this node and its descendants.

`String`
`val()`

Get the value of a form element (input, textarea, etc).

`Element`
`val(String value)`

Set the value of a form element (input, textarea, etc).

`String`
`wholeOwnText()`

Get the non-normalized, decoded text of this element, **not including** any child elements, including any
     newlines and spaces present in the original source.

`String`
`wholeText()`

Get the non-normalized, decoded text of this element and its children, including only any newlines and spaces
     present in the original source.

`Element`
`wrap(String html)`

Wrap the supplied HTML around this element.

### Methods inherited from class org.jsoup.nodes.Node

`absUrl, addChildren, addChildren, attr, attributesSize, childNode, childNodes, childNodesAsArray, childNodesCopy, equals, firstChild, firstSibling, hasAttr, hashCode, hasParent, hasSameValue, indent, lastChild, lastSibling, nameIs, nextElementSibling, nextSibling, nodeStream, nodeStream, outerHtml, outerHtml, outerHtml, ownerDocument, parentElement, parentElementIs, parentNameIs, parentNode, previousElementSibling, previousSibling, remove, removeChild, reparentChild, replaceChild, replaceWith, setBaseUri, setParentNode, setSiblingIndex, siblingIndex, siblingNodes, sourceRange, toString, unwrap`

### Methods inherited from class java.lang.Object

`finalize, getClass, notify, notifyAll, wait, wait, wait`

### Methods inherited from interface java.lang.Iterable

`spliterator`

- 

## Constructor Details

  - 

### Element

public Element(String tag,
 String namespace)
Create a new, standalone element, in the specified namespace.

Parameters:
`tag` - tag name
`namespace` - namespace for this element

  - 

### Element

public Element(String tag)
Create a new, standalone element, in the HTML namespace.

Parameters:
`tag` - tag name
See Also:

    - `Element(String tag, String namespace)`

  - 

### Element

public Element(Tag tag,
 @Nullable String baseUri,
 @Nullable Attributes attributes)
Create a new, standalone Element. (Standalone in that it has no parent.)

Parameters:
`tag` - tag of this element
`baseUri` - the base URI (optional, may be null to inherit from parent, or "" to clear parent's)
`attributes` - initial attributes (optional, may be null)
See Also:

    - `appendChild(Node)`

    - `appendElement(String)`

  - 

### Element

public Element(Tag tag,
 @Nullable String baseUri)
Create a new Element from a Tag and a base URI.

Parameters:
`tag` - element tag
`baseUri` - the base URI of this element. Optional, and will inherit from its parent, if any.
See Also:

    - `Tag.valueOf(String, ParseSettings)`

- 

## Method Details

  - 

### hasChildNodes

protected boolean hasChildNodes()
Internal test to check if a nodelist object has been created.

  - 

### ensureChildNodes

protected List<Node> ensureChildNodes()

Specified by:
`ensureChildNodes` in class `Node`

  - 

### hasAttributes

protected boolean hasAttributes()
Description copied from class: `Node`
Check if this Node has an actual Attributes object.

Specified by:
`hasAttributes` in class `Node`

  - 

### attributes

public Attributes attributes()
Description copied from class: `Node`
Get each of the Element's attributes.

Specified by:
`attributes` in class `Node`
Returns:
attributes (which implements Iterable, with the same order as presented in the original HTML).

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

### nodeName

public String nodeName()
Description copied from class: `Node`
Get the node name of this node. Use for debugging purposes and not logic switching (for that, use instanceof).

Specified by:
`nodeName` in class `Node`
Returns:
node name

  - 

### tagName

public String tagName()
Get the name of the tag for this element. E.g. `div`. If you are using `case preserving parsing`, this will return the source's original case.

Returns:
the tag name

  - 

### normalName

public String normalName()
Get the normalized name of this Element's tag. This will always be the lower-cased version of the tag, regardless
 of the tag case preserving setting of the parser. For e.g., `<DIV>` and `<div>` both have a
 normal name of `div`.

Overrides:
`normalName` in class `Node`
Returns:
normal name

  - 

### elementIs

public boolean elementIs(String normalName,
 String namespace)
Test if this Element has the specified normalized name, and is in the specified namespace.

Parameters:
`normalName` - a normalized element name (e.g. `div`).
`namespace` - the namespace
Returns:
true if the element's normal name matches exactly, and is in the specified namespace
Since:
1.17.2

  - 

### tagName

public Element tagName(String tagName)
Change (rename) the tag of this element. For example, convert a `<span>` to a `<div>` with
 `el.tagName("div");`.

Parameters:
`tagName` - new tag name for this element
Returns:
this element, for chaining
See Also:

    - `Elements.tagName(String)`

  - 

### tagName

public Element tagName(String tagName,
 String namespace)
Change (rename) the tag of this element. For example, convert a `<span>` to a `<div>` with
 `el.tagName("div");`.

Parameters:
`tagName` - new tag name for this element
`namespace` - the new namespace for this element
Returns:
this element, for chaining
See Also:

    - `Elements.tagName(String)`

  - 

### tag

public Tag tag()
Get the Tag for this element.

Returns:
the tag object

  - 

### tag

public Element tag(Tag tag)
Change the Tag of this element.

Parameters:
`tag` - the new tag
Returns:
this element, for chaining
Since:
1.20.1

  - 

### isBlock

public boolean isBlock()
Test if this element is a block-level element. (E.g. `<div> == true` or an inline element
 `<span> == false`).

Returns:
true if block, false if not (and thus inline)

  - 

### id

public String id()
Get the `id` attribute of this element.

Returns:
The id attribute, if present, or an empty string if not.

  - 

### id

public Element id(String id)
Set the `id` attribute of this element.

Parameters:
`id` - the ID value to use
Returns:
this Element, for chaining

  - 

### attr

public Element attr(String attributeKey,
 String attributeValue)
Set an attribute value on this element. If this element already has an attribute with the
 key, its value is updated; otherwise, a new attribute is added.

Overrides:
`attr` in class `Node`
Parameters:
`attributeKey` - The attribute key.
`attributeValue` - The attribute value.
Returns:
this element

  - 

### attr

public Element attr(String attributeKey,
 boolean attributeValue)
Set a boolean attribute value on this element. Setting to `true` sets the attribute value to "" and
 marks the attribute as boolean so no value is written out. Setting to `false` removes the attribute
 with the same key if it exists.

Parameters:
`attributeKey` - the attribute key
`attributeValue` - the attribute value
Returns:
this element

  - 

### attribute

public @Nullable Attribute attribute(String key)
Get an Attribute by key. Changes made via `Attribute.setKey(String)`, `Attribute.setValue(String)` etc
     will cascade back to this Element.

Parameters:
`key` - the (case-sensitive) attribute key
Returns:
the Attribute for this key, or null if not present.
Since:
1.17.2

  - 

### dataset

public Map<String,String> dataset()
Get this element's HTML5 custom data attributes. Each attribute in the element that has a key
 starting with "data-" is included the dataset.
 

 E.g., the element `<div data-package="jsoup" data-language="Java" class="group">...` has the dataset
 `package=jsoup, language=java`.
 

 This map is a filtered view of the element's attribute map. Changes to one map (add, remove, update) are reflected
 in the other map.
 

 You can find elements that have data attributes using the `[^data-]` attribute key prefix selector.

Returns:
a map of `key=value` custom data attributes.

  - 

### parent

public final @Nullable Element parent()
Description copied from class: `Node`
Gets this node's parent node. This is always an Element.

Overrides:
`parent` in class `Node`
Returns:
parent node; or null if no parent.
See Also:

    - `Node.hasParent()`

  - 

### parents

public Elements parents()
Get this element's parent and ancestors, up to the document root.

Returns:
this element's stack of parents, starting with the closest first.

  - 

### child

public Element child(int index)
Get a child element of this element, by its 0-based index number.
 

 Note that an element can have both mixed Nodes and Elements as children. This method inspects
 a filtered list of children that are elements, and the index is based on that filtered list.
 

Parameters:
`index` - the index number of the element to retrieve
Returns:
the child element, if it exists, otherwise throws an `IndexOutOfBoundsException`
See Also:

    - `Node.childNode(int)`

  - 

### childrenSize

public int childrenSize()
Get the number of child nodes of this element that are elements.
 

 This method works on the same filtered list like `child(int)`. Use `Node.childNodes()` and `childNodeSize()` to get the unfiltered Nodes (e.g. includes TextNodes etc.)
 

Returns:
the number of child nodes that are elements
See Also:

    - `children()`

    - `child(int)`

  - 

### children

public Elements children()
Get this element's child elements.
 

 This is effectively a filter on `Node.childNodes()` to get Element nodes.
 

Returns:
child elements. If this element has no children, returns an empty list.
See Also:

    - `Node.childNodes()`

  - 

### stream

public Stream<Element> stream()
Returns a Stream of this Element and all of its descendant Elements. The stream has document order.

Returns:
a stream of this element and its descendants.
Since:
1.17.1
See Also:

    - `Node.nodeStream()`

  - 

### textNodes

public List<TextNode> textNodes()
Get this element's child text nodes. The list is unmodifiable but the text nodes may be manipulated.
 

 This is effectively a filter on `Node.childNodes()` to get Text nodes.

Returns:
child text nodes. If this element has no text nodes, returns an
 empty list.
 
 For example, with the input HTML: `<p>One <span>Two</span> Three <br> Four</p>` with the `p` element selected:
 

     
    - `p.text()` = `"One Two Three Four"`
     
    - `p.ownText()` = `"One Three Four"`
     
    - `p.children()` = `Elements[<span>, <br>]`
     
    - `p.childNodes()` = `List<Node>["One ", <span>, " Three ", <br>, " Four"]`
     
    - `p.textNodes()` = `List<TextNode>["One ", " Three ", " Four"]`
 

  - 

### dataNodes

public List<DataNode> dataNodes()
Get this element's child data nodes. The list is unmodifiable but the data nodes may be manipulated.
 

 This is effectively a filter on `Node.childNodes()` to get Data nodes.
 

Returns:
child data nodes. If this element has no data nodes, returns an
 empty list.
See Also:

    - `data()`

  - 

### select

public Elements select(String cssQuery)
Find elements that match the `Selector` CSS query, with this element as the starting context. Matched elements
 may include this element, or any of its descendents.
 

If the query starts with a combinator (e.g. `*` or `>`), that will combine to this element.
 

This method is generally more powerful to use than the DOM-type `getElementBy*` methods, because
 multiple filters can be combined, e.g.:
 

 
    - `el.select("a[href]")` - finds links (`a` tags with `href` attributes)
 
    - `el.select("a[href*=example.com]")` - finds links pointing to example.com (loosely)
 
    - `el.select("* div")` - finds all divs that descend from this element (and excludes this element)
 
    - `el.select("> div")` - finds all divs that are direct children of this element (and excludes this element)
 

 

See the query syntax documentation in `Selector`.
 

Also known as `querySelectorAll()` in the Web DOM.

Parameters:
`cssQuery` - a `Selector` CSS-like query
Returns:
an `Elements` list containing elements that match the query (empty if none match)
Throws:
`Selector.SelectorParseException` - (unchecked) on an invalid CSS query.
See Also:

    - `selector query syntax`

    - `select(Evaluator)`

  - 

### select

public Elements select(Evaluator evaluator)
Find elements that match the supplied Evaluator. This has the same functionality as `select(String)`, but
 may be useful if you are running the same query many times (on many documents) and want to save the overhead of
 repeatedly parsing the CSS query.

Parameters:
`evaluator` - an element evaluator
Returns:
an `Elements` list containing elements that match the query (empty if none match)
See Also:

    - `Selector.evaluatorOf(String css)`

  - 

### selectStream

public Stream<Element> selectStream(String cssQuery)
Selects elements from the given root that match the specified `Selector` CSS query, with this element as the
     starting context, and returns them as a lazy Stream. Matched elements may include this element, or any of its
     children.
     

     Unlike `select(String query)`, which returns a complete list of all matching elements, this method returns a
     `Stream` that processes elements lazily as they are needed. The stream operates in a "pull" model â elements
     are fetched from the root as the stream is traversed. You can use standard `Stream` operations such as
     `filter`, `map`, or `findFirst` to process elements on demand.
     

Parameters:
`cssQuery` - a `Selector` CSS-like query
Returns:
a `Stream` containing elements that match the query (empty if none match)
Throws:
`Selector.SelectorParseException` - (unchecked) on an invalid CSS query.
Since:
1.19.1
See Also:

    - `selector query syntax`

    - `selectStream(Evaluator eval)`

  - 

### selectStream

public Stream<Element> selectStream(Evaluator evaluator)
Find a Stream of elements that match the supplied Evaluator.

Parameters:
`evaluator` - an element Evaluator
Returns:
a `Stream` containing elements that match the query (empty if none match)
Since:
1.19.1
See Also:

    - `Selector.evaluatorOf(String css)`

  - 

### selectFirst

public @Nullable Element selectFirst(String cssQuery)
Find the first Element that matches the `Selector` CSS query, with this element as the starting context.
 

This is effectively the same as calling `element.select(query).first()`, but is more efficient as query
 execution stops on the first hit.
 

Also known as `querySelector()` in the Web DOM.

Parameters:
`cssQuery` - cssQuery a `Selector` CSS-like query
Returns:
the first matching element, or **`null`** if there is no match.
See Also:

    - `expectFirst(String)`

  - 

### selectFirst

public @Nullable Element selectFirst(Evaluator evaluator)
Finds the first Element that matches the supplied Evaluator, with this element as the starting context, or
 `null` if none match.

Parameters:
`evaluator` - an element evaluator
Returns:
the first matching element (walking down the tree, starting from this element), or `null` if none
 match.

  - 

### expectFirst

public Element expectFirst(String cssQuery)
Just like `selectFirst(String)`, but if there is no match, throws an `IllegalArgumentException`. This
     is useful if you want to simply abort processing on a failed match.

Parameters:
`cssQuery` - a `Selector` CSS-like query
Returns:
the first matching element
Throws:
`IllegalArgumentException` - if no match is found
Since:
1.15.2

  - 

### selectNodes

public Nodes<Node> selectNodes(Evaluator evaluator)
Find nodes that match the supplied `Evaluator`, with this element as the starting context. Matched
     nodes may include this element, or any of its descendents.

Parameters:
`evaluator` - an evaluator
Returns:
a list of nodes that match the query (empty if none match)
Since:
1.21.1

  - 

### selectNodes

public Nodes<Node> selectNodes(String cssQuery)
Find nodes that match the supplied `Selector` CSS query, with this element as the starting context. Matched
     nodes may include this element, or any of its descendents.
     

To select leaf nodes, the query should specify the node type, e.g. `::text`,
     `::comment`, `::data`, `::leafnode`.

Parameters:
`cssQuery` - a `Selector` CSS query
Returns:
a list of nodes that match the query (empty if none match)
Since:
1.21.1

  - 

### selectNodes

public <T extends Node> Nodes<T> selectNodes(Evaluator evaluator,
 Class<T> type)
Find nodes that match the supplied Evaluator, with this element as the starting context. Matched
     nodes may include this element, or any of its descendents.

Type Parameters:
`T` - the type of node to collect
Parameters:
`evaluator` - an evaluator
`type` - the type of node to collect (e.g. `Element`, `LeafNode`, `TextNode` etc)
Returns:
a list of nodes that match the query (empty if none match)
Since:
1.21.1

  - 

### selectNodes

public <T extends Node> Nodes<T> selectNodes(String cssQuery,
 Class<T> type)
Find nodes that match the supplied `Selector` CSS query, with this element as the starting context. Matched
     nodes may include this element, or any of its descendents.
     

To select specific node types, use `::text`, `::comment`, `::leafnode`, etc. For example, to
     select all text nodes under `p` elements: 
     

```
    Nodes<TextNode> textNodes = doc.selectNodes("p ::text", TextNode.class);
```

Type Parameters:
`T` - the type of node to collect
Parameters:
`cssQuery` - a `Selector` CSS query
`type` - the type of node to collect (e.g. `Element`, `LeafNode`, `TextNode` etc)
Returns:
a list of nodes that match the query (empty if none match)
Since:
1.21.1

  - 

### selectFirstNode

public <T extends Node> @Nullable T selectFirstNode(String cssQuery,
 Class<T> type)
Find the first Node that matches the `Selector` CSS query, with this element as the starting context.
     

This is effectively the same as calling `element.selectNodes(query).first()`, but is more efficient as
     query
     execution stops on the first hit.
     

Also known as `querySelector()` in the Web DOM.

Parameters:
`cssQuery` - cssQuery a `Selector` CSS-like query
Returns:
the first matching node, or **`null`** if there is no match.
Since:
1.21.1
See Also:

    - `expectFirst(String)`

  - 

### selectFirstNode

public <T extends Node> @Nullable T selectFirstNode(Evaluator evaluator,
 Class<T> type)
Finds the first Node that matches the supplied Evaluator, with this element as the starting context, or
     `null` if none match.

Parameters:
`evaluator` - an element evaluator
Returns:
the first matching node (walking down the tree, starting from this element), or `null` if none
     match.
Since:
1.21.1

  - 

### expectFirstNode

public <T extends Node> T expectFirstNode(String cssQuery,
 Class<T> type)
Just like `selectFirstNode(String, Class)`, but if there is no match, throws an
     `IllegalArgumentException`. This is useful if you want to simply abort processing on a failed match.

Parameters:
`cssQuery` - a `Selector` CSS-like query
Returns:
the first matching node
Throws:
`IllegalArgumentException` - if no match is found
Since:
1.21.1

  - 

### is

public boolean is(String cssQuery)
Checks if this element matches the given `Selector` CSS query. Also knows as `matches()` in the Web
 DOM.

Parameters:
`cssQuery` - a `Selector` CSS query
Returns:
if this element matches the query

  - 

### is

public boolean is(Evaluator evaluator)
Check if this element matches the given evaluator.

Parameters:
`evaluator` - an element evaluator
Returns:
if this element matches

  - 

### closest

public @Nullable Element closest(String cssQuery)
Find the closest element up the tree of parents that matches the specified CSS query. Will return itself, an
 ancestor, or `null` if there is no such matching element.

Parameters:
`cssQuery` - a `Selector` CSS query
Returns:
the closest ancestor element (possibly itself) that matches the provided evaluator. `null` if not
 found.

  - 

### closest

public @Nullable Element closest(Evaluator evaluator)
Find the closest element up the tree of parents that matches the specified evaluator. Will return itself, an
 ancestor, or `null` if there is no such matching element.

Parameters:
`evaluator` - a query evaluator
Returns:
the closest ancestor element (possibly itself) that matches the provided evaluator. `null` if not
 found.

  - 

### selectXpath

public Elements selectXpath(String xpath)
Find Elements that match the supplied XPath expression.
     

Note that for convenience of writing the Xpath expression, namespaces are disabled, and queries can be
     expressed using the element's local name only.
     

By default, XPath 1.0 expressions are supported. If you would to use XPath 2.0 or higher, you can provide an
     alternate XPathFactory implementation:
     

     
    - Add the implementation to your classpath. E.g. to use Saxon-HE, add net.sf.saxon:Saxon-HE to your build.
     
    - Set the system property `javax.xml.xpath.XPathFactory:jsoup` to the implementing classname. E.g.:

     `System.setProperty(W3CDom.XPathFactoryProperty, "net.sf.saxon.xpath.XPathFactoryImpl");`
     
     

Parameters:
`xpath` - XPath expression
Returns:
matching elements, or an empty list if none match.
Since:
1.14.3
See Also:

    - `selectXpath(String, Class)`

  - 

### selectXpath

public <T extends Node> List<T> selectXpath(String xpath,
 Class<T> nodeType)
Find Nodes that match the supplied XPath expression.
     

For example, to select TextNodes under `p` elements: 
     

```
List<TextNode> textNodes = doc.selectXpath("//body//p//text()", TextNode.class);
```

     

Note that in the jsoup DOM, Attribute objects are not Nodes. To directly select attribute values, do something
     like:
     

```
List<String> hrefs = doc.selectXpath("//a").eachAttr("href");
```

Parameters:
`xpath` - XPath expression
`nodeType` - the jsoup node type to return
Returns:
a list of matching nodes
Since:
1.14.3
See Also:

    - `selectXpath(String)`

  - 

### appendChild

public Element appendChild(Node child)
Insert a node to the end of this Element's children. The incoming node will be re-parented.

Parameters:
`child` - node to add.
Returns:
this Element, for chaining
See Also:

    - `prependChild(Node)`

    - `insertChildren(int, Collection)`

  - 

### appendChildren

public Element appendChildren(Collection<? extends Node> children)
Insert the given nodes to the end of this Element's children.

Parameters:
`children` - nodes to add
Returns:
this Element, for chaining
See Also:

    - `insertChildren(int, Collection)`

  - 

### appendTo

public Element appendTo(Element parent)
Add this element to the supplied parent element, as its next child.

Parameters:
`parent` - element to which this element will be appended
Returns:
this element, so that you can continue modifying the element

  - 

### prependChild

public Element prependChild(Node child)
Add a node to the start of this element's children.

Parameters:
`child` - node to add.
Returns:
this element, so that you can add more child nodes or elements.

  - 

### prependChildren

public Element prependChildren(Collection<? extends Node> children)
Insert the given nodes to the start of this Element's children.

Parameters:
`children` - nodes to add
Returns:
this Element, for chaining
See Also:

    - `insertChildren(int, Collection)`

  - 

### insertChildren

public Element insertChildren(int index,
 Collection<? extends Node> children)
Inserts the given child nodes into this element at the specified index. Current nodes will be shifted to the
 right. The inserted nodes will be moved from their current parent. To prevent moving, copy the nodes first.

Parameters:
`index` - 0-based index to insert children at. Specify `0` to insert at the start, `-1` at the
 end
`children` - child nodes to insert
Returns:
this element, for chaining.

  - 

### insertChildren

public Element insertChildren(int index,
 Node... children)
Inserts the given child nodes into this element at the specified index. Current nodes will be shifted to the
 right. The inserted nodes will be moved from their current parent. To prevent moving, copy the nodes first.

Parameters:
`index` - 0-based index to insert children at. Specify `0` to insert at the start, `-1` at the
 end
`children` - child nodes to insert
Returns:
this element, for chaining.

  - 

### appendElement

public Element appendElement(String tagName)
Create a new element by tag name, and add it as this Element's last child.

Parameters:
`tagName` - the name of the tag (e.g. `div`).
Returns:
the new element, to allow you to add content to it, e.g.:
  `parent.appendElement("h1").attr("id", "header").text("Welcome");`

  - 

### appendElement

public Element appendElement(String tagName,
 String namespace)
Create a new element by tag name and namespace, add it as this Element's last child.

Parameters:
`tagName` - the name of the tag (e.g. `div`).
`namespace` - the namespace of the tag (e.g. `Parser.NamespaceHtml`)
Returns:
the new element, in the specified namespace

  - 

### prependElement

public Element prependElement(String tagName)
Create a new element by tag name, and add it as this Element's first child.

Parameters:
`tagName` - the name of the tag (e.g. `div`).
Returns:
the new element, to allow you to add content to it, e.g.:
  `parent.prependElement("h1").attr("id", "header").text("Welcome");`

  - 

### prependElement

public Element prependElement(String tagName,
 String namespace)
Create a new element by tag name and namespace, and add it as this Element's first child.

Parameters:
`tagName` - the name of the tag (e.g. `div`).
`namespace` - the namespace of the tag (e.g. `Parser.NamespaceHtml`)
Returns:
the new element, in the specified namespace

  - 

### appendText

public Element appendText(String text)
Create and append a new TextNode to this element.

Parameters:
`text` - the (un-encoded) text to add
Returns:
this element

  - 

### prependText

public Element prependText(String text)
Create and prepend a new TextNode to this element.

Parameters:
`text` - the decoded text to add
Returns:
this element

  - 

### append

public Element append(String html)
Add inner HTML to this element. The supplied HTML will be parsed, and each node appended to the end of the children.

Parameters:
`html` - HTML to add inside this element, after the existing HTML
Returns:
this element
See Also:

    - `html(String)`

  - 

### prepend

public Element prepend(String html)
Add inner HTML into this element. The supplied HTML will be parsed, and each node prepended to the start of the element's children.

Parameters:
`html` - HTML to add inside this element, before the existing HTML
Returns:
this element
See Also:

    - `html(String)`

  - 

### before

public Element before(String html)
Insert the specified HTML into the DOM before this element (as a preceding sibling).

Overrides:
`before` in class `Node`
Parameters:
`html` - HTML to add before this element
Returns:
this element, for chaining
See Also:

    - `after(String)`

  - 

### before

public Element before(Node node)
Insert the specified node into the DOM before this node (as a preceding sibling).

Overrides:
`before` in class `Node`
Parameters:
`node` - to add before this element
Returns:
this Element, for chaining
See Also:

    - `after(Node)`

  - 

### after

public Element after(String html)
Insert the specified HTML into the DOM after this element (as a following sibling).

Overrides:
`after` in class `Node`
Parameters:
`html` - HTML to add after this element
Returns:
this element, for chaining
See Also:

    - `before(String)`

  - 

### after

public Element after(Node node)
Insert the specified node into the DOM after this node (as a following sibling).

Overrides:
`after` in class `Node`
Parameters:
`node` - to add after this element
Returns:
this element, for chaining
See Also:

    - `before(Node)`

  - 

### empty

public Element empty()
Remove all the element's child nodes. Any attributes are left as-is. Each child node has its parent set to
 `null`.

Specified by:
`empty` in class `Node`
Returns:
this element

  - 

### wrap

public Element wrap(String html)
Wrap the supplied HTML around this element.

Overrides:
`wrap` in class `Node`
Parameters:
`html` - HTML to wrap around this element, e.g. `<div class="head"></div>`. Can be arbitrarily deep.
Returns:
this element, for chaining.

  - 

### cssSelector

public String cssSelector()
Get a CSS selector that will uniquely select this element.
     

     If the element has an ID, returns #id; otherwise returns the parent (if any) CSS selector, followed by
     '>', followed by a unique selector for the element (tag.class.class:nth-child(n)).
     

Returns:
the CSS Path that can be used to retrieve the element in a selector.

  - 

### siblingElements

public Elements siblingElements()
Get sibling elements. If the element has no sibling elements, returns an empty list. An element is not a sibling
 of itself, so will not be included in the returned list.

Returns:
sibling elements

  - 

### nextElementSiblings

public Elements nextElementSiblings()
Get each of the sibling elements that come after this element.

Returns:
each of the element siblings after this element, or an empty list if there are no next sibling elements

  - 

### previousElementSiblings

public Elements previousElementSiblings()
Get each of the element siblings before this element.

Returns:
the previous element siblings, or an empty list if there are none.

  - 

### firstElementSibling

public Element firstElementSibling()
Gets the first Element sibling of this element. That may be this element.

Returns:
the first sibling that is an element (aka the parent's first element child)

  - 

### elementSiblingIndex

public int elementSiblingIndex()
Get the list index of this element in its element sibling list. I.e. if this is the first element
 sibling, returns 0.

Returns:
position in element sibling list

  - 

### lastElementSibling

public Element lastElementSibling()
Gets the last element sibling of this element. That may be this element.

Returns:
the last sibling that is an element (aka the parent's last element child)

  - 

### firstElementChild

public @Nullable Element firstElementChild()
Gets the first child of this Element that is an Element, or `null` if there is none.

Returns:
the first Element child node, or null.
Since:
1.15.2
See Also:

    - `Node.firstChild()`

    - `lastElementChild()`

  - 

### lastElementChild

public @Nullable Element lastElementChild()
Gets the last child of this Element that is an Element, or @{code null} if there is none.

Returns:
the last Element child node, or null.
Since:
1.15.2
See Also:

    - `Node.lastChild()`

    - `firstElementChild()`

  - 

### getElementsByTag

public Elements getElementsByTag(String tagName)
Finds elements, including and recursively under this element, with the specified tag name.

Parameters:
`tagName` - The tag name to search for (case insensitively).
Returns:
a matching unmodifiable list of elements. Will be empty if this element and none of its children match.

  - 

### getElementById

public @Nullable Element getElementById(String id)
Find an element by ID, including or under this element.
 

 Note that this finds the first matching ID, starting with this element. If you search down from a different
 starting point, it is possible to find a different element by ID. For unique element by ID within a Document,
 use `getElementById(String)`

Parameters:
`id` - The ID to search for.
Returns:
The first matching element by ID, starting with this element, or null if none found.

  - 

### getElementsByClass

public Elements getElementsByClass(String className)
Find elements that have this class, including or under this element. Case-insensitive.
 

 Elements can have multiple classes (e.g. `<div class="header round first">`). This method
 checks each class, so you can find the above with `el.getElementsByClass("header");`.

Parameters:
`className` - the name of the class to search for.
Returns:
elements with the supplied class name, empty if none
See Also:

    - `hasClass(String)`

    - `classNames()`

  - 

### getElementsByAttribute

public Elements getElementsByAttribute(String key)
Find elements that have a named attribute set. Case-insensitive.

Parameters:
`key` - name of the attribute, e.g. `href`
Returns:
elements that have this attribute, empty if none

  - 

### getElementsByAttributeStarting

public Elements getElementsByAttributeStarting(String keyPrefix)
Find elements that have an attribute name starting with the supplied prefix. Use `data-` to find elements
 that have HTML5 datasets.

Parameters:
`keyPrefix` - name prefix of the attribute e.g. `data-`
Returns:
elements that have attribute names that start with the prefix, empty if none.

  - 

### getElementsByAttributeValue

public Elements getElementsByAttributeValue(String key,
 String value)
Find elements that have an attribute with the specific value. Case-insensitive.

Parameters:
`key` - name of the attribute
`value` - value of the attribute
Returns:
elements that have this attribute with this value, empty if none

  - 

### getElementsByAttributeValueNot

public Elements getElementsByAttributeValueNot(String key,
 String value)
Find elements that either do not have this attribute, or have it with a different value. Case-insensitive.

Parameters:
`key` - name of the attribute
`value` - value of the attribute
Returns:
elements that do not have a matching attribute

  - 

### getElementsByAttributeValueStarting

public Elements getElementsByAttributeValueStarting(String key,
 String valuePrefix)
Find elements that have attributes that start with the value prefix. Case-insensitive.

Parameters:
`key` - name of the attribute
`valuePrefix` - start of attribute value
Returns:
elements that have attributes that start with the value prefix

  - 

### getElementsByAttributeValueEnding

public Elements getElementsByAttributeValueEnding(String key,
 String valueSuffix)
Find elements that have attributes that end with the value suffix. Case-insensitive.

Parameters:
`key` - name of the attribute
`valueSuffix` - end of the attribute value
Returns:
elements that have attributes that end with the value suffix

  - 

### getElementsByAttributeValueContaining

public Elements getElementsByAttributeValueContaining(String key,
 String match)
Find elements that have attributes whose value contains the match string. Case-insensitive.

Parameters:
`key` - name of the attribute
`match` - substring of value to search for
Returns:
elements that have attributes containing this text

  - 

### getElementsByAttributeValueMatching

public Elements getElementsByAttributeValueMatching(String key,
 Pattern pattern)
Find elements that have an attribute whose value matches the supplied regular expression.

Parameters:
`key` - name of the attribute
`pattern` - compiled regular expression to match against attribute values
Returns:
elements that have attributes matching this regular expression

  - 

### getElementsByAttributeValueMatching

public Elements getElementsByAttributeValueMatching(String key,
 String regex)
Find elements that have attributes whose values match the supplied regular expression.

Parameters:
`key` - name of the attribute
`regex` - regular expression to match against attribute values. You can use embedded flags (such as `(?i)` and `(?m)`) to control regex options.
Returns:
elements that have attributes matching this regular expression

  - 

### getElementsByIndexLessThan

public Elements getElementsByIndexLessThan(int index)
Find elements whose sibling index is less than the supplied index.

Parameters:
`index` - 0-based index
Returns:
elements less than index

  - 

### getElementsByIndexGreaterThan

public Elements getElementsByIndexGreaterThan(int index)
Find elements whose sibling index is greater than the supplied index.

Parameters:
`index` - 0-based index
Returns:
elements greater than index

  - 

### getElementsByIndexEquals

public Elements getElementsByIndexEquals(int index)
Find elements whose sibling index is equal to the supplied index.

Parameters:
`index` - 0-based index
Returns:
elements equal to index

  - 

### getElementsContainingText

public Elements getElementsContainingText(String searchText)
Find elements that contain the specified string. The search is case-insensitive. The text may appear directly
 in the element, or in any of its descendants.

Parameters:
`searchText` - to look for in the element's text
Returns:
elements that contain the string, case-insensitive.
See Also:

    - `text()`

  - 

### getElementsContainingOwnText

public Elements getElementsContainingOwnText(String searchText)
Find elements that directly contain the specified string. The search is case-insensitive. The text must appear directly
 in the element, not in any of its descendants.

Parameters:
`searchText` - to look for in the element's own text
Returns:
elements that contain the string, case-insensitive.
See Also:

    - `ownText()`

  - 

### getElementsMatchingText

public Elements getElementsMatchingText(Pattern pattern)
Find elements whose text matches the supplied regular expression.

Parameters:
`pattern` - regular expression to match text against
Returns:
elements matching the supplied regular expression.
See Also:

    - `text()`

  - 

### getElementsMatchingText

public Elements getElementsMatchingText(String regex)
Find elements whose text matches the supplied regular expression.

Parameters:
`regex` - regular expression to match text against. You can use embedded flags (such as `(?i)` and `(?m)`) to control regex options.
Returns:
elements matching the supplied regular expression.
See Also:

    - `text()`

  - 

### getElementsMatchingOwnText

public Elements getElementsMatchingOwnText(Pattern pattern)
Find elements whose own text matches the supplied regular expression.

Parameters:
`pattern` - regular expression to match text against
Returns:
elements matching the supplied regular expression.
See Also:

    - `ownText()`

  - 

### getElementsMatchingOwnText

public Elements getElementsMatchingOwnText(String regex)
Find elements whose own text matches the supplied regular expression.

Parameters:
`regex` - regular expression to match text against. You can use embedded flags (such as `(?i)` and `(?m)`) to control regex options.
Returns:
elements matching the supplied regular expression.
See Also:

    - `ownText()`

  - 

### getAllElements

public Elements getAllElements()
Find all elements under this element (including self, and children of children).

Returns:
all elements

  - 

### text

public String text()
Gets the **normalized, combined text** of this element and all its children. Whitespace is normalized and
     trimmed.
     

For example, given HTML `<p>Hello  <b>there</b> now! </p>`, `p.text()` returns `"Hello there
    now!"`
     

If you do not want normalized text, use `wholeText()`. If you want just the text of this node (and not
     children), use `ownText()`
     

Note that this method returns the textual content that would be presented to a reader. The contents of data
     nodes (such as `<script>` tags) are not considered text. Use `data()` or `html()` to retrieve
     that content.

Returns:
decoded, normalized text, or empty string if none.
See Also:

    - `wholeText()`

    - `ownText()`

    - `textNodes()`

  - 

### wholeText

public String wholeText()
Get the non-normalized, decoded text of this element and its children, including only any newlines and spaces
     present in the original source.

Returns:
decoded, non-normalized text
See Also:

    - `text()`

    - `wholeOwnText()`

  - 

### nodeValue

public String nodeValue()
An Element's nodeValue is its whole own text.

Overrides:
`nodeValue` in class `Node`
Returns:
the node's value

  - 

### wholeOwnText

public String wholeOwnText()
Get the non-normalized, decoded text of this element, **not including** any child elements, including any
     newlines and spaces present in the original source.

Returns:
decoded, non-normalized text that is a direct child of this Element
Since:
1.15.1
See Also:

    - `text()`

    - `wholeText()`

    - `ownText()`

  - 

### ownText

public String ownText()
Gets the (normalized) text owned by this element only; does not get the combined text of all children.
 

 For example, given HTML `<p>Hello <b>there</b> now!</p>`, `p.ownText()` returns `"Hello now!"`,
 whereas `p.text()` returns `"Hello there now!"`.
 Note that the text within the `b` element is not returned, as it is not a direct child of the `p` element.

Returns:
decoded text, or empty string if none.
See Also:

    - `text()`

    - `textNodes()`

  - 

### text

public Element text(String text)
Set the text of this element. Any existing contents (text or elements) will be cleared.
 

As a special case, for `<script>` and `<style>` tags, the input text will be treated as data,
 not visible text.

Parameters:
`text` - decoded text
Returns:
this element

  - 

### hasText

public boolean hasText()
Checks if the current element or any of its child elements contain non-whitespace text.

Returns:
`true` if the element has non-blank text content, `false` otherwise.

  - 

### data

public String data()
Get the combined data of this element. Data is e.g. the inside of a `<script>` tag. Note that data is NOT the
 text of the element. Use `text()` to get the text that would be visible to a user, and `data()`
 for the contents of scripts, comments, CSS styles, etc.

Returns:
the data, or empty string if none
See Also:

    - `dataNodes()`

  - 

### className

public String className()
Gets the literal value of this element's "class" attribute, which may include multiple class names, space
 separated. (E.g. on `<div class="header gray">` returns, "`header gray`")

Returns:
The literal class attribute, or **empty string** if no class attribute set.

  - 

### classNames

public Set<String> classNames()
Get each of the element's class names. E.g. on element `<div class="header gray">`,
 returns a set of two elements `"header", "gray"`. Note that modifications to this set are not pushed to
 the backing `class` attribute; use the `classNames(java.util.Set)` method to persist them.

Returns:
set of classnames, empty if no class attribute

  - 

### classNames

public Element classNames(Set<String> classNames)
Set the element's `class` attribute to the supplied class names.

Parameters:
`classNames` - set of classes
Returns:
this element, for chaining

  - 

### hasClass

public boolean hasClass(String className)
Tests if this element has a class. Case-insensitive.

Parameters:
`className` - name of class to check for
Returns:
true if it does, false if not

  - 

### addClass

public Element addClass(String className)
Add a class name to this element's `class` attribute.

Parameters:
`className` - class name to add
Returns:
this element

  - 

### removeClass

public Element removeClass(String className)
Remove a class name from this element's `class` attribute.

Parameters:
`className` - class name to remove
Returns:
this element

  - 

### toggleClass

public Element toggleClass(String className)
Toggle a class name on this element's `class` attribute: if present, remove it; otherwise add it.

Parameters:
`className` - class name to toggle
Returns:
this element

  - 

### val

public String val()
Get the value of a form element (input, textarea, etc).

Returns:
the value of the form element, or empty string if not set.

  - 

### val

public Element val(String value)
Set the value of a form element (input, textarea, etc).

Parameters:
`value` - value to set
Returns:
this element (for chaining)

  - 

### endSourceRange

public Range endSourceRange()
Get the source range (start and end positions) of the end (closing) tag for this Element. Position tracking must be
     enabled prior to parsing the content.

Returns:
the range of the closing tag for this element, or `untracked` if its range was not tracked.
Since:
1.15.2
See Also:

    - `Parser.setTrackPosition(boolean)`

    - `Node.sourceRange()`

    - `Range.isImplicit()`

  - 

### html

public String html()
Retrieves the element's inner HTML. E.g. on a `<div>` with one empty `<p>`, would return
 `<p></p>`. (Whereas `Node.outerHtml()` would return `<div><p></p></div>`.)

Returns:
String of HTML.
See Also:

    - `Node.outerHtml()`

  - 

### html

public <T extends Appendable> T html(T accum)
Description copied from class: `Node`
Write this node and its children to the given `Appendable`.

Overrides:
`html` in class `Node`
Parameters:
`accum` - the `Appendable` to write to.
Returns:
the supplied `Appendable`, for chaining.

  - 

### html

public Element html(String html)
Set this element's inner HTML. Clears the existing HTML first.

Parameters:
`html` - HTML to parse and set into this element
Returns:
this element
See Also:

    - `append(String)`

  - 

### clone

public Element clone()
Description copied from class: `Node`
Create a stand-alone, deep copy of this node, and all of its children. The cloned node will have no siblings.
     

     
    - If this node is a `LeafNode`, the clone will have no parent.
     
    - If this node is an `Element`, the clone will have a simple owning `Document` to retain the
     configured output settings and parser.
     

     

The cloned node may be adopted into another Document or node structure using
     `appendChild(Node)`.

Overrides:
`clone` in class `Node`
Returns:
a stand-alone cloned node, including clones of any children
See Also:

    - `Node.shallowClone()`

  - 

### shallowClone

public Element shallowClone()
Description copied from class: `Node`
Create a stand-alone, shallow copy of this node. None of its children (if any) will be cloned, and it will have
 no parent or sibling nodes.

Overrides:
`shallowClone` in class `Node`
Returns:
a single independent copy of this node
See Also:

    - `Node.clone()`

  - 

### doClone

protected Element doClone(@Nullable Node parent)

Overrides:
`doClone` in class `Node`

  - 

### clearAttributes

public Element clearAttributes()
Description copied from class: `Node`
Clear (remove) each of the attributes in this node.

Overrides:
`clearAttributes` in class `Node`
Returns:
this, for chaining

  - 

### removeAttr

public Element removeAttr(String attributeKey)
Description copied from class: `Node`
Remove an attribute from this node.

Overrides:
`removeAttr` in class `Node`
Parameters:
`attributeKey` - The attribute to remove.
Returns:
this (for chaining)

  - 

### root

public Element root()
Description copied from class: `Node`
Get this node's root node; that is, its topmost ancestor. If this node is the top ancestor, returns `this`.

Overrides:
`root` in class `Node`
Returns:
topmost ancestor.

  - 

### traverse

public Element traverse(NodeVisitor nodeVisitor)
Description copied from class: `Node`
Perform a depth-first traversal through this node and its descendants.

Overrides:
`traverse` in class `Node`
Parameters:
`nodeVisitor` - the visitor callbacks to perform on each node
Returns:
this node, for chaining

  - 

### forEachNode

public Element forEachNode(Consumer<? super Node> action)
Description copied from class: `Node`
Perform the supplied action on this Node and each of its descendants, during a depth-first traversal. Nodes may be
     inspected, changed, added, replaced, or removed.

Overrides:
`forEachNode` in class `Node`
Parameters:
`action` - the function to perform on the node
Returns:
this Node, for chaining
See Also:

    - `forEach(Consumer)`

  - 

### forEach

public void forEach(Consumer<? super Element> action)
Perform the supplied action on this Element and each of its descendant Elements, during a depth-first traversal.
     Elements may be inspected, changed, added, replaced, or removed.

Specified by:
`forEach` in interface `Iterable<Element>`
Parameters:
`action` - the function to perform on the element
See Also:

    - `Node.forEachNode(Consumer)`

  - 

### iterator

public Iterator<Element> iterator()
Returns an Iterator that iterates this Element and each of its descendant Elements, in document order.

Specified by:
`iterator` in interface `Iterable<Element>`
Returns:
an Iterator

  - 

### filter

public Element filter(NodeFilter nodeFilter)
Description copied from class: `Node`
Perform a depth-first controllable traversal through this node and its descendants.

Overrides:
`filter` in class `Node`
Parameters:
`nodeFilter` - the filter callbacks to perform on each node
Returns:
this node, for chaining