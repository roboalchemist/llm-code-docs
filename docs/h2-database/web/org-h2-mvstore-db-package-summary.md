# Package org.h2.mvstore.db

---

package org.h2.mvstore.db

Helper classes to use the MVStore in the H2 database.

- 

Related Packages

Package
Description
org.h2.mvstore

A persistent storage for tree maps.

org.h2.mvstore.cache

Classes related to caching.

org.h2.mvstore.rtree

An R-tree implementation.

org.h2.mvstore.tx

Helper classes to use the MVStore in a transactional manner.

org.h2.mvstore.type

Data types and serialization / deserialization.

- 

Classes

Class
Description
LobStorageMap

This class stores LOB objects in the database, in maps.

LobStorageMap.BlobMeta
 
LobStorageMap.BlobMeta.Type
 
LobStorageMap.BlobReference
 
LobStorageMap.BlobReference.Type
 
MVDelegateIndex

An index that delegates indexing to another index.

MVIndex<K,V>

An index that stores the data in an MVStore.

MVPrimaryIndex

A table stored in a MVStore.

MVSecondaryIndex

An index stored in a MVStore.

MVSpatialIndex

This is an index based on a MVRTreeMap.

MVTable

A table stored in a MVStore.

MVTempResult

Temporary result.

NullValueDataType

Dummy data type used when no value is required.

RowDataType

The data type for rows.

RowDataType.Factory
 
SpatialKey

A unique spatial key.

Store

A store with open tables.

ValueDataType

A row type.

ValueDataType.Factory