# Package org.h2.mvstore.type

---

package org.h2.mvstore.type

Data types and serialization / deserialization.

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

org.h2.mvstore.tx

Helper classes to use the MVStore in a transactional manner.

- 

Class
Description
BasicDataType<T>

The base class for data type implementations.

ByteArrayDataType

Class ByteArrayDataType.

DataType<T>

A data type.

IntegerDataType

Class IntegerDataType.

LongDataType

Class LongDataType.

MetaType<D>

Class DBMetaType is a type for values in the type registry map.

ObjectDataType

A data type implementation for the most common data types, including
 serializable objects.

StatefulDataType<D>

A data type that allows to save its state.

StatefulDataType.Factory<D>

A factory for data types.

StringDataType

A string type.