# Package io.vavr.collection

---

package io.vavr.collection

Purely functional collections based on Traversable.

 
## Performance Characteristics of Vavr Collections

 
 Time Complexity of Sequential Operations
 
 
  
 head()
 tail()
 get(int)
 update(int, T)
 prepend(T)
 append(T)
 
 
 
 Arrayconstlinearconstlinearlinearlinear
 CharSeqconstlinearconstlinearlinearlinear
 *Iterator*constconst————
 Listconstconstlinearlinearconstlinear
 Queueconstconstalinearlinearconstconst
 PriorityQueueloglog——loglog
 Streamconstconstlinearlinearconstlazyconstlazy
 Vectorconsteffconsteffconsteffconsteffconsteffconsteff
 
 
 

 
 Time Complexity of Map/Set Operations
 
 
  
 contains/Key
 add/put
 remove
 min
 
 
 
 HashMapconsteffconsteffconstefflinear
 HashSetconsteffconsteffconstefflinear
 LinkedHashMapconstefflinearlinearlinear
 LinkedHashSetconstefflinearlinearlinear
 *Tree*loglogloglog
 TreeMaploglogloglog
 TreeSetloglogloglog
 
 
 

 

 
- const · constant time
 
- consta · amortized constant time, few operations may take longer
 
- consteff · effectively constant time, depending on assumptions like distribution of hash keys
 
- constlazy · lazy constant time, the operation is deferred
 
- log · logarithmic time
 
- linear · linear time
 

- 

Related Packages

Package
Description
io.vavr

Beside `API` the io.vavr package contains core types like (Checked)Functions and Tuples.

io.vavr.concurrent

This package contains basic building blocks for creating fast, asynchronous, non-blocking parallel code.

io.vavr.control

Control structures like the disjoint union type Either, the optional value type
 Option and Try for exception handling.

- 

Class
Description
Array<T>

Array is an immutable Traversable wrapper for `Object[]` containing elements of type `T`.

BitSet<T>

An immutable `BitSet` implementation.

BitSet.Builder<T>

Builder of the BitSet.

CharSeq

The CharSeq (read: character sequence) collection essentially is a rich String wrapper having all operations
 we know from the functional Vavr collections.

CharSeq.CharFunction<R>

Represents a function that accepts a `char`-valued argument and produces a result.

CharSeq.CharUnaryOperator

Represents an operation on a single `char`-valued operand that produces
 a `char`-valued result.

Foldable<T>

Represents a data structure that can be folded (reduced) into a single value.

HashMap<K,V>

An immutable `HashMap` implementation based on a
 Hash array mapped trie (HAMT).

HashMultimap<K,V>

A `HashMap`-based implementation of `Multimap`

HashMultimap.Builder<V>

Builder for creating `HashMultimap` instances with different container types.

HashSet<T>

An immutable `HashSet` implementation.

IndexedSeq<T>

Represents an immutable, indexed sequence of elements.

Iterator<T>

A compositional alternative to `java.util.Iterator` designed for single-pass
 traversal of a sequence.

LinearSeq<T>

Interface for immutable, linear sequences.

LinkedHashMap<K,V>

An immutable `LinkedHashMap` implementation that has predictable (insertion-order) iteration.

LinkedHashMultimap<K,V>

A `LinkedHashMap`-based implementation of `Multimap`

LinkedHashMultimap.Builder<V>

Builder class for creating LinkedHashMultimap instances.

LinkedHashSet<T>

An immutable `HashSet` implementation that has predictable (insertion-order) iteration.

List<T>

An immutable `List` is an eager sequence of elements.

List.Cons<T>

Non-empty `List`, consisting of a `head` and a `tail`.

List.Nil<T>

Representation of the singleton empty `List`.

Map<K,V>

An immutable `Map` interface.

Multimap<K,V>

An immutable `Multimap` interface.

Multimap.ContainerType

Defines the type of container used to store values associated with keys in a Multimap.

Ordered<T>

A collection whose elements are arranged according to a well-defined order.

PriorityQueue<T>

A PriorityQueue.

Queue<T>

An immutable `Queue` stores elements allowing a first-in-first-out (FIFO) retrieval.

Seq<T>

Base interface for immutable, sequential collections.

Set<T>

An immutable `Set` interface.

SortedMap<K,V>

An immutable `SortedMap` interface.

SortedMultimap<K,V>

An immutable `SortedMultimap` interface.

SortedSet<T>

An immutable `SortedSet` interface.

Stream<T>

An immutable `Stream` is lazy sequence of elements which may be infinitely long.

Stream.Cons<T>

Non-empty `Stream`, consisting of a `head`, and `tail`.

Stream.Empty<T>

The empty Stream.

Traversable<T>

Represents a recursive, multi-valued data structure whose elements can be traversed in order.

Tree<T>

A general Tree interface.

Tree.Empty<T>

The empty tree.

Tree.Node<T>

Represents a tree node.

Tree.Order

Tree traversal order.

TreeMap<K,V>

An immutable `SortedMap` implementation backed by a Red-Black tree.

TreeMultimap<K,V>

A `TreeMap`-based implementation of `Multimap`

TreeMultimap.Builder<V>

Builder class for creating TreeMultimap instances.

TreeSet<T>

SortedSet implementation, backed by a Red/Black Tree.

Vector<T>

Vector is the default Seq implementation that provides effectively constant time access to any element.