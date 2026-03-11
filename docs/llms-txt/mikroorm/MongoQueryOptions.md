# Source: https://mikro-orm.io/api/mongodb/interface/MongoQueryOptions.md

# MongoQueryOptions<!-- -->

### Hierarchy

* *MongoQueryOptions*
  * [MongoFindOptions](https://mikro-orm.io/api/mongodb/interface/MongoFindOptions.md)

## Index[**](#index)

### Properties

* [**allowDiskUse](#allowDiskUse)
* [**collation](#collation)
* [**indexHint](#indexHint)
* [**maxTimeMS](#maxTimeMS)

## Properties<!-- -->[**](#properties)

### [**](#allowDiskUse)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/mongodb/src/MongoConnection.ts#L668)optionalallowDiskUse

**allowDiskUse?

<!-- -->

: boolean

### [**](#collation)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/mongodb/src/MongoConnection.ts#L665)optionalcollation

**collation?

<!-- -->

: [CollationOptions](https://mikro-orm.io/api/core/interface/CollationOptions.md)

### [**](#indexHint)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/mongodb/src/MongoConnection.ts#L666)optionalindexHint

**indexHint?

<!-- -->

: string | [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)

### [**](#maxTimeMS)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/mongodb/src/MongoConnection.ts#L667)optionalmaxTimeMS

**maxTimeMS?

<!-- -->

: number
