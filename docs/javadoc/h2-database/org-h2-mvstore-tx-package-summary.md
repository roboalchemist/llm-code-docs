# Package org.h2.mvstore.tx

---

package org.h2.mvstore.tx

Helper classes to use the MVStore in a transactional manner.

- 

Related Packages

Package
Description
org.h2.mvstore

A persistent storage for tree maps.

org.h2.mvstore.cache

Classes related to caching.

org.h2.mvstore.db

Helper classes to use the MVStore in the H2 database.

org.h2.mvstore.rtree

An R-tree implementation.

org.h2.mvstore.type

Data types and serialization / deserialization.

- 

Class
Description
Transaction

A transaction.

TransactionMap<K,V>

A map that supports transactions.

TransactionMap.TMIterator<K,V,X>
 
TransactionStore

A store that supports concurrent MVCC read-committed transactions.

TransactionStore.Change

A change in a map.

TransactionStore.RollbackListener

This listener can be registered with the transaction to be notified of
 every compensating change during transaction rollback.

VersionedValueType<T,D>

The value type for a versioned value.

VersionedValueType.Factory<D>