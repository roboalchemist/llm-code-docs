Package org.jsoup.nodes

# Class FormElement

java.lang.Object
org.jsoup.nodes.Node
org.jsoup.nodes.Element
org.jsoup.nodes.FormElement

All Implemented Interfaces:
`Cloneable`, `Iterable<Element>`

---

public class FormElement
extends Element
An HTML Form Element provides ready access to the form fields/controls that are associated with it. It also allows a
 form to easily be submitted.

- 

## Constructor Summary

Constructors

Constructor
Description
`FormElement(Tag tag,
 @Nullable String baseUri,
 @Nullable Attributes attributes)`

Create a new, standalone form element.

- 

## Method Summary

Modifier and Type
Method
Description
`FormElement`
`addElement(Element element)`

Add a form control element to this form.

`FormElement`
`clone()`

Create a stand-alone, deep copy of this node, and all of its children.

`Elements`
`elements()`

Get the list of form control elements associated with this form.

`List<Connection.KeyVal>`
`formData()`

Get the data that this form submits.

`protected void`
`removeChild(Node out)`
 
`Connection`
`submit()`

Prepare to submit this form.

### Methods inherited from class org.jsoup.nodes.Element

`addClass, after, after, append, appendChild, appendChildren, appendElement, appendElement, appendText, appendTo, attr, attr, attribute, attributes, baseUri, before, before, child, childNodeSize, children, childrenSize, className, classNames, classNames, clearAttributes, closest, closest, cssSelector, data, dataNodes, dataset, doClone, doSetBaseUri, elementIs, elementSiblingIndex, empty, endSourceRange, ensureChildNodes, expectFirst, expectFirstNode, filter, firstElementChild, firstElementSibling, forEach, forEachNode, getAllElements, getElementById, getElementsByAttribute, getElementsByAttributeStarting, getElementsByAttributeValue, getElementsByAttributeValueContaining, getElementsByAttributeValueEnding, getElementsByAttributeValueMatching, getElementsByAttributeValueMatching, getElementsByAttributeValueNot, getElementsByAttributeValueStarting, getElementsByClass, getElementsByIndexEquals, getElementsByIndexGreaterThan, getElementsByIndexLessThan, getElementsByTag, getElementsContainingOwnText, getElementsContainingText, getElementsMatchingOwnText, getElementsMatchingOwnText, getElementsMatchingText, getElementsMatchingText, hasAttributes, hasChildNodes, hasClass, hasText, html, html, html, id, id, insertChildren, insertChildren, is, is, isBlock, iterator, lastElementChild, lastElementSibling, nextElementSiblings, nodeName, nodeValue, normalName, ownText, parent, parents, prepend, prependChild, prependChildren, prependElement, prependElement, prependText, previousElementSiblings, removeAttr, removeClass, root, select, select, selectFirst, selectFirst, selectFirstNode, selectFirstNode, selectNodes, selectNodes, selectNodes, selectNodes, selectStream, selectStream, selectXpath, selectXpath, shallowClone, siblingElements, stream, tag, tag, tagName, tagName, tagName, text, text, textNodes, toggleClass, traverse, val, val, wholeOwnText, wholeText, wrap`

### Methods inherited from class org.jsoup.nodes.Node

`absUrl, addChildren, addChildren, attr, attributesSize, childNode, childNodes, childNodesAsArray, childNodesCopy, equals, firstChild, firstSibling, hasAttr, hashCode, hasParent, hasSameValue, indent, lastChild, lastSibling, nameIs, nextElementSibling, nextSibling, nodeStream, nodeStream, outerHtml, outerHtml, outerHtml, ownerDocument, parentElement, parentElementIs, parentNameIs, parentNode, previousElementSibling, previousSibling, remove, reparentChild, replaceChild, replaceWith, setBaseUri, setParentNode, setSiblingIndex, siblingIndex, siblingNodes, sourceRange, toString, unwrap`

### Methods inherited from class java.lang.Object

`finalize, getClass, notify, notifyAll, wait, wait, wait`

### Methods inherited from interface java.lang.Iterable

`spliterator`

- 

## Constructor Details

  - 

### FormElement

public FormElement(Tag tag,
 @Nullable String baseUri,
 @Nullable Attributes attributes)
Create a new, standalone form element.

Parameters:
`tag` - tag of this element
`baseUri` - the base URI
`attributes` - initial attributes

- 

## Method Details

  - 

### elements

public Elements elements()
Get the list of form control elements associated with this form.

Returns:
form controls associated with this element.

  - 

### addElement

public FormElement addElement(Element element)
Add a form control element to this form.

Parameters:
`element` - form control to add
Returns:
this form element, for chaining

  - 

### removeChild

protected void removeChild(Node out)

Overrides:
`removeChild` in class `Node`

  - 

### submit

public Connection submit()
Prepare to submit this form. A Connection object is created with the request set up from the form values. This
     Connection will inherit the settings and the cookies (etc) of the connection/session used to request this Document
     (if any), as available in `Document.connection()`
     

You can then set up other options (like user-agent, timeout, cookies), then execute it.

Returns:
a connection prepared from the values of this form, in the same session as the one used to request it
Throws:
`IllegalArgumentException` - if the form's absolute action URL cannot be determined. Make sure you pass the
     document's base URI when parsing.

  - 

### formData

public List<Connection.KeyVal> formData()
Get the data that this form submits. The returned list is a copy of the data, and changes to the contents of the
 list will not be reflected in the DOM.

Returns:
a list of key vals

  - 

### clone

public FormElement clone()
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