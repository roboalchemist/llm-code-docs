# Package org.h2.mvstore

---

package org.h2.mvstore

A persistent storage for tree maps.

- 

Related Packages

Package
Description
org.h2

Implementation of the JDBC driver.

org.h2.mvstore.cache

Classes related to caching.

org.h2.mvstore.db

Helper classes to use the MVStore in the H2 database.

org.h2.mvstore.rtree

An R-tree implementation.

org.h2.mvstore.tx

Helper classes to use the MVStore in a transactional manner.

org.h2.mvstore.type

Data types and serialization / deserialization.

- 

Class
Description
AppendOnlyMultiFileStore

Class AppendOnlyMultiFileStore.

Chunk<C extends Chunk<C>>

A chunk of data, containing one or multiple pages.

Chunk.PositionComparator<C extends Chunk<C>>
 
Cursor<K,V>

A cursor to iterate over elements in ascending or descending order.

CursorPos<K,V>

A position in a cursor.

DataUtils

Utility methods

FileStore<C extends Chunk<C>>

Class FileStore is a base class to allow for different store implementations.

FreeSpaceBitSet

A free space bit set.

MVMap<K,V>

A stored map.

MVMap.BasicBuilder<M extends MVMap<K,V>,K,V>

A builder for this class.

MVMap.Builder<K,V>

A builder for this class.

MVMap.Decision

The decision on what to do on an update.

MVMap.DecisionMaker<V>

Class DecisionMaker provides callback interface (and should become a such in Java 8)
 for MVMap.operate() method.

MVMap.MapBuilder<M extends MVMap<K,V>,K,V>

A builder for maps.

MVStore

A persistent storage for maps.

MVStore.Builder

A builder for an MVStore.

MVStore.TxCounter

Class TxCounter is a simple data structure to hold version of the store
 along with the counter of open transactions,
 which are still operating on this version.

MVStoreException

Various kinds of MVStore problems, along with associated error code.

MVStoreTool

Utility methods used in combination with the MVStore.

OffHeapStore

A storage mechanism that "persists" data in the off-heap area of the main memory.

Page<K,V>

A page (a node or a leaf).

Page.PageReference<K,V>

A pointer to a page, either in-memory or using a page position.

RandomAccessStore

Class RandomAccessStore.

RootReference<K,V>

Class RootReference is an immutable structure to represent state of the MVMap as a whole
 (not related to a particular B-Tree node).

SFChunk

Class SFChunk.

SingleFileStore

The default storage mechanism of the MVStore.

StreamStore

A facility to store streams in a map.

WriteBuffer

An auto-resize buffer to write data into a ByteBuffer.