Package org.jsoup.helper

# Class W3CDom.W3CBuilder

java.lang.Object
org.jsoup.helper.W3CDom.W3CBuilder

All Implemented Interfaces:
`NodeVisitor`

Enclosing class:
W3CDom

---

protected static class W3CDom.W3CBuilder
extends Object
implements NodeVisitor
Implements the conversion by walking the input.

- 

## Constructor Summary

Constructors

Constructor
Description
`W3CBuilder(Document doc)`
 

- 

## Method Summary

Modifier and Type
Method
Description
`void`
`head(Node source,
 int depth)`

Callback for when a node is first visited.

`void`
`tail(Node source,
 int depth)`

Callback for when a node is last visited, after all of its descendants have been visited.

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

### Methods inherited from interface org.jsoup.select.NodeVisitor

`traverse`

- 

## Constructor Details

  - 

### W3CBuilder

public W3CBuilder(Document doc)

- 

## Method Details

  - 

### head

public void head(Node source,
 int depth)
Description copied from interface: `NodeVisitor`
Callback for when a node is first visited.
     

The node may be modified (e.g. `Node.attr(String)`, replaced `Node.replaceWith(Node)`) or removed
     `Node.remove()`. If it's `instanceOf Element`, you may cast it to an `Element` and access those
     methods.

Specified by:
`head` in interface `NodeVisitor`
Parameters:
`source` - the node being visited.
`depth` - the depth of the node, relative to the root node. E.g., the root node has depth 0, and a child node
     of that will have depth 1.

  - 

### tail

public void tail(Node source,
 int depth)
Description copied from interface: `NodeVisitor`
Callback for when a node is last visited, after all of its descendants have been visited.
     

This method has a default no-op implementation.
     

Note that neither replacement with `Node.replaceWith(Node)` nor removal with `Node.remove()` is
     supported during `tail()`.

Specified by:
`tail` in interface `NodeVisitor`
Parameters:
`source` - the node being visited.
`depth` - the depth of the node, relative to the root node. E.g., the root node has depth 0, and a child node
     of that will have depth 1.