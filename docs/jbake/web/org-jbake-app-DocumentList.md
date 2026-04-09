Package org.jbake.app

# Class DocumentList<T>

java.lang.Object
java.util.AbstractCollection<E>
java.util.AbstractList<E>
java.util.AbstractSequentialList<E>
java.util.LinkedList<T>
org.jbake.app.DocumentList<T>

All Implemented Interfaces:
`Serializable`, `Cloneable`, `Iterable<T>`, `Collection<T>`, `Deque<T>`, `List<T>`, `Queue<T>`

---

public class DocumentList<T>
extends LinkedList<T>
Wraps an OrientDB document iterator into a model usable by
 template engines.

See Also:

- Serialized Form

- 

## Field Summary

### Fields inherited from class java.util.AbstractList

`modCount`

- 

## Constructor Summary

Constructors

Constructor
Description
`DocumentList()`
 

- 

## Method Summary

Modifier and Type
Method
Description
`static DocumentList<DocumentModel>`
`wrap(com.orientechnologies.orient.core.sql.executor.OResultSet docs)`
 

### Methods inherited from class java.util.LinkedList

`add, add, addAll, addAll, addFirst, addLast, clear, clone, contains, descendingIterator, element, get, getFirst, getLast, indexOf, lastIndexOf, listIterator, offer, offerFirst, offerLast, peek, peekFirst, peekLast, poll, pollFirst, pollLast, pop, push, remove, remove, remove, removeFirst, removeFirstOccurrence, removeLast, removeLastOccurrence, set, size, spliterator, toArray, toArray`

### Methods inherited from class java.util.AbstractSequentialList

`iterator`

### Methods inherited from class java.util.AbstractList

`equals, hashCode, listIterator, removeRange, subList`

### Methods inherited from class java.util.AbstractCollection

`containsAll, isEmpty, removeAll, retainAll, toString`

### Methods inherited from class java.lang.Object

`finalize, getClass, notify, notifyAll, wait, wait, wait`

### Methods inherited from interface java.util.Collection

`parallelStream, removeIf, stream, toArray`

### Methods inherited from interface java.util.Deque

`iterator`

### Methods inherited from interface java.lang.Iterable

`forEach`

### Methods inherited from interface java.util.List

`containsAll, equals, hashCode, isEmpty, iterator, listIterator, removeAll, replaceAll, retainAll, sort, subList`

- 

## Constructor Details

  - 

### DocumentList

public DocumentList()

- 

## Method Details

  - 

### wrap

public static DocumentList<DocumentModel> wrap(com.orientechnologies.orient.core.sql.executor.OResultSet docs)