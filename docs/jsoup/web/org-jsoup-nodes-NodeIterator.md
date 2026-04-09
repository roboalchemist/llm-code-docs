Package org.jsoup.nodes

# Class NodeIterator<T extends Node>

java.lang.Object
org.jsoup.nodes.NodeIterator<T>

All Implemented Interfaces:
`Iterator<T>`

---

public class NodeIterator<T extends Node>
extends Object
implements Iterator<T>
Iterate through a Node and its tree of descendants, in document order, and returns nodes of the specified type. This
 iterator supports structural changes to the tree during the traversal, such as `Node.remove()`,
 `Node.replaceWith(Node)`, `Node.wrap(String)`, etc.
 

See also the `NodeTraversor` if `head` and `tail` callbacks are
 desired for each node.

Since:
1.17.1

- 

## Constructor Summary

Constructors

Constructor
Description
`NodeIterator(Node start,
 Class<T> type)`

Create a NoteIterator that will iterate the supplied node, and all of its descendants.

- 

## Method Summary

Modifier and Type
Method
Description
`static NodeIterator<Node>`
`from(Node start)`

Create a NoteIterator that will iterate the supplied node, and all of its descendants.

`boolean`
`hasNext()`
 
`T`
`next()`
 
`void`
`remove()`
 
`void`
`restart(Node start)`

Restart this Iterator from the specified start node.

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

### Methods inherited from interface java.util.Iterator

`forEachRemaining`

- 

## Constructor Details

  - 

### NodeIterator

public NodeIterator(Node start,
 Class<T> type)
Create a NoteIterator that will iterate the supplied node, and all of its descendants. The returned `next`
     type will be filtered to the input type.

Parameters:
`start` - initial node
`type` - node type to filter for

- 

## Method Details

  - 

### from

public static NodeIterator<Node> from(Node start)
Create a NoteIterator that will iterate the supplied node, and all of its descendants. All node types will be
     returned.

Parameters:
`start` - initial node

  - 

### restart

public void restart(Node start)
Restart this Iterator from the specified start node. Will act as if it were newly constructed. Useful for e.g. to
     save some GC if the iterator is used in a tight loop.

Parameters:
`start` - the new start node.

  - 

### hasNext

public boolean hasNext()

Specified by:
`hasNext` in interface `Iterator<T extends Node>`

  - 

### next

public T next()

Specified by:
`next` in interface `Iterator<T extends Node>`

  - 

### remove

public void remove()

Specified by:
`remove` in interface `Iterator<T extends Node>`