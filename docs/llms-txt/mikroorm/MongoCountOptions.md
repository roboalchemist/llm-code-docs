# Source: https://mikro-orm.io/api/mongodb/interface/MongoCountOptions.md

# MongoCountOptions<!-- -->

### Hierarchy

* Omit<[MongoQueryOptions](https://mikro-orm.io/api/mongodb/interface/MongoQueryOptions.md), allowDiskUse>
  * *MongoCountOptions*

## Index[**](#index)

### Properties

* [**collation](#collation)
* [**ctx](#ctx)
* [**indexHint](#indexHint)
* [**loggerContext](#loggerContext)
* [**maxTimeMS](#maxTimeMS)

## Properties<!-- -->[**](#properties)

### [**](#collation)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/mongodb/src/MongoConnection.ts#L665)optionalinheritedcollation

**collation?

<!-- -->

: [CollationOptions](https://mikro-orm.io/api/core/interface/CollationOptions.md)

Inherited from Omit.collation

### [**](#ctx)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/mongodb/src/MongoConnection.ts#L681)optionalctx

**ctx?

<!-- -->

: ClientSession

### [**](#indexHint)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/mongodb/src/MongoConnection.ts#L666)optionalinheritedindexHint

**indexHint?

<!-- -->

: string | [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)

Inherited from Omit.indexHint

### [**](#loggerContext)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/mongodb/src/MongoConnection.ts#L682)optionalloggerContext

**loggerContext?

<!-- -->

: [LoggingOptions](https://mikro-orm.io/api/core.md#LoggingOptions)

### [**](#maxTimeMS)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/mongodb/src/MongoConnection.ts#L667)optionalinheritedmaxTimeMS

**maxTimeMS?

<!-- -->

: number

Inherited from Omit.maxTimeMS
