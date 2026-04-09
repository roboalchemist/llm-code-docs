Package org.jsoup.nodes

# Class PseudoTextElement

java.lang.Object
org.jsoup.nodes.Node
org.jsoup.nodes.Element
org.jsoup.nodes.PseudoTextElement

All Implemented Interfaces:
`Cloneable`, `Iterable<Element>`

---

@Deprecated
public class PseudoTextElement
extends Element
Deprecated.
use `Element.selectNodes(String, Class)` instead, with selector of `::textnode` and class `TextNode`;
 will be removed in jsoup 1.24.1.

Represents a `TextNode` as an `Element`, to enable text nodes to be selected with
 the `Selector` `:matchText` syntax.

- 

## Constructor Summary

Constructors

Constructor
Description
`PseudoTextElement(Tag tag,
 String baseUri,
 Attributes attributes)`

Deprecated.
 

- 

## Method Summary

### Methods inherited from class org.jsoup.nodes.Element

`addClass, after, after, append, appendChild, appendChildren, appendElement, appendElement, appendText, appendTo, attr, attr, attribute, attributes, baseUri, before, before, child, childNodeSize, children, childrenSize, className, classNames, classNames, clearAttributes, clone, closest, closest, cssSelector, data, dataNodes, dataset, doClone, doSetBaseUri, elementIs, elementSiblingIndex, empty, endSourceRange, ensureChildNodes, expectFirst, expectFirstNode, filter, firstElementChild, firstElementSibling, forEach, forEachNode, getAllElements, getElementById, getElementsByAttribute, getElementsByAttributeStarting, getElementsByAttributeValue, getElementsByAttributeValueContaining, getElementsByAttributeValueEnding, getElementsByAttributeValueMatching, getElementsByAttributeValueMatching, getElementsByAttributeValueNot, getElementsByAttributeValueStarting, getElementsByClass, getElementsByIndexEquals, getElementsByIndexGreaterThan, getElementsByIndexLessThan, getElementsByTag, getElementsContainingOwnText, getElementsContainingText, getElementsMatchingOwnText, getElementsMatchingOwnText, getElementsMatchingText, getElementsMatchingText, hasAttributes, hasChildNodes, hasClass, hasText, html, html, html, id, id, insertChildren, insertChildren, is, is, isBlock, iterator, lastElementChild, lastElementSibling, nextElementSiblings, nodeName, nodeValue, normalName, ownText, parent, parents, prepend, prependChild, prependChildren, prependElement, prependElement, prependText, previousElementSiblings, removeAttr, removeClass, root, select, select, selectFirst, selectFirst, selectFirstNode, selectFirstNode, selectNodes, selectNodes, selectNodes, selectNodes, selectStream, selectStream, selectXpath, selectXpath, shallowClone, siblingElements, stream, tag, tag, tagName, tagName, tagName, text, text, textNodes, toggleClass, traverse, val, val, wholeOwnText, wholeText, wrap`

### Methods inherited from class org.jsoup.nodes.Node

`absUrl, addChildren, addChildren, attr, attributesSize, childNode, childNodes, childNodesAsArray, childNodesCopy, equals, firstChild, firstSibling, hasAttr, hashCode, hasParent, hasSameValue, indent, lastChild, lastSibling, nameIs, nextElementSibling, nextSibling, nodeStream, nodeStream, outerHtml, outerHtml, outerHtml, ownerDocument, parentElement, parentElementIs, parentNameIs, parentNode, previousElementSibling, previousSibling, remove, removeChild, reparentChild, replaceChild, replaceWith, setBaseUri, setParentNode, setSiblingIndex, siblingIndex, siblingNodes, sourceRange, toString, unwrap`

### Methods inherited from class java.lang.Object

`finalize, getClass, notify, notifyAll, wait, wait, wait`

### Methods inherited from interface java.lang.Iterable

`spliterator`

- 

## Constructor Details

  - 

### PseudoTextElement

public PseudoTextElement(Tag tag,
 String baseUri,
 Attributes attributes)
Deprecated.