# Package org.jsoup.select

---

@NullMarked
package org.jsoup.select

Packages to support the CSS-style element selector.
 `Selector defines the query syntax.`

- 

Related Packages

Package
Description
org.jsoup

Contains the main `Jsoup` class, which provides convenient static access to the jsoup functionality.

org.jsoup.helper

Package containing classes supporting the core jsoup code.

org.jsoup.nodes

HTML document structure nodes.

org.jsoup.parser

Contains the HTML parser, tag specifications, and HTML tokeniser.

org.jsoup.safety

Contains the jsoup HTML cleaner, and safelist definitions.

- 

Class
Description
Collector

Collects a list of elements that match the supplied criteria.

CombiningEvaluator

Base combining (and, or) evaluator.

CombiningEvaluator.And
 
CombiningEvaluator.Or
 
Elements

A list of `Element`s, with methods that act on every element in the list.

Evaluator

An Evaluator tests if an element (or a node) meets the selector's requirements.

Evaluator.AllElements

Evaluator for any / all element matching

Evaluator.Attribute

Evaluator for attribute name matching

Evaluator.AttributeKeyPair

Abstract evaluator for attribute name/value matching

Evaluator.AttributeStarting

Evaluator for attribute name prefix matching

Evaluator.AttributeWithValue

Evaluator for attribute name/value matching

Evaluator.AttributeWithValueContaining

Evaluator for attribute name/value matching (value containing)

Evaluator.AttributeWithValueEnding

Evaluator for attribute name/value matching (value ending)

Evaluator.AttributeWithValueMatching

Evaluator for attribute name/value matching (value regex matching)

Evaluator.AttributeWithValueNot

Evaluator for attribute name !

Evaluator.AttributeWithValueStarting

Evaluator for attribute name/value matching (value prefix)

Evaluator.Class

Evaluator for element class

Evaluator.ContainsData

Evaluator for matching Element (and its descendants) data

Evaluator.ContainsOwnText

Evaluator for matching Element's own text

Evaluator.ContainsText

Evaluator for matching Element (and its descendants) text

Evaluator.ContainsWholeOwnText

Evaluator for matching Element (but **not** its descendants) wholeText.

Evaluator.ContainsWholeText

Evaluator for matching Element (and its descendants) wholeText.

Evaluator.CssNthEvaluator
 
Evaluator.Id

Evaluator for element id

Evaluator.IndexEquals

Evaluator for matching by sibling index number (e = idx)

Evaluator.IndexEvaluator

Abstract evaluator for sibling index matching

Evaluator.IndexGreaterThan

Evaluator for matching by sibling index number (e > idx)

Evaluator.IndexLessThan

Evaluator for matching by sibling index number (e < idx)

Evaluator.IsEmpty
 
Evaluator.IsFirstChild

Evaluator for matching the first sibling (css :first-child)

Evaluator.IsFirstOfType
 
Evaluator.IsLastChild

Evaluator for matching the last sibling (css :last-child)

Evaluator.IsLastOfType
 
Evaluator.IsNthChild

css-compatible Evaluator for :eq (css :nth-child)

Evaluator.IsNthLastChild

css pseudo class :nth-last-child)

Evaluator.IsNthLastOfType
 
Evaluator.IsNthOfType

css pseudo class nth-of-type

Evaluator.IsOnlyChild
 
Evaluator.IsOnlyOfType
 
Evaluator.IsRoot

css3 pseudo-class :root

Evaluator.Matches

Evaluator for matching Element (and its descendants) text with regex

Evaluator.MatchesOwn

Evaluator for matching Element's own text with regex

Evaluator.MatchesWholeOwnText

Evaluator for matching Element's own whole text with regex.

Evaluator.MatchesWholeText

Evaluator for matching Element (and its descendants) whole text with regex.

Evaluator.MatchText
Deprecated.
This selector is deprecated and will be removed in jsoup 1.24.1.

Evaluator.Tag

Evaluator for tag name

Evaluator.TagEndsWith

Evaluator for tag name that ends with suffix; used for *|el

Evaluator.TagStartsWith

Evaluator for tag name that starts with prefix; used for ns|*

NodeFilter

A controllable Node visitor interface.

NodeFilter.FilterResult

Traversal action.

Nodes<T extends Node>

A list of `Node` objects, with methods that act on every node in the list.

NodeTraversor

A depth-first node traversor.

NodeVisitor

Node visitor interface, used to walk the DOM, and visit each Node.

QueryParser

Parses a CSS selector into an Evaluator tree.

Selector

CSS element selector, that finds elements matching a query.

Selector.SelectorParseException