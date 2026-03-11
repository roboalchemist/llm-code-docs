# Source: https://mikro-orm.io/api/mongodb/interface/MongoFindOptions.md

# MongoFindOptions<!-- --> \<T>

### Hierarchy

* [MongoQueryOptions](https://mikro-orm.io/api/mongodb/interface/MongoQueryOptions.md)
  * *MongoFindOptions*

## Index[**](#index)

### Properties

* [**allowDiskUse](#allowDiskUse)
* [**collation](#collation)
* [**ctx](#ctx)
* [**fields](#fields)
* [**indexHint](#indexHint)
* [**limit](#limit)
* [**loggerContext](#loggerContext)
* [**maxTimeMS](#maxTimeMS)
* [**offset](#offset)
* [**orderBy](#orderBy)

## Properties<!-- -->[**](#properties)

### [**](#allowDiskUse)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/mongodb/src/MongoConnection.ts#L668)optionalinheritedallowDiskUse

**allowDiskUse?

<!-- -->

: boolean

Inherited from MongoQueryOptions.allowDiskUse

### [**](#collation)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/mongodb/src/MongoConnection.ts#L665)optionalinheritedcollation

**collation?

<!-- -->

: [CollationOptions](https://mikro-orm.io/api/core/interface/CollationOptions.md)

Inherited from MongoQueryOptions.collation

### [**](#ctx)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/mongodb/src/MongoConnection.ts#L676)optionalctx

**ctx?

<!-- -->

: ClientSession

### [**](#fields)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/mongodb/src/MongoConnection.ts#L675)optionalfields

**fields?

<!-- -->

: string\[]

### [**](#indexHint)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/mongodb/src/MongoConnection.ts#L666)optionalinheritedindexHint

**indexHint?

<!-- -->

: string | [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)

Inherited from MongoQueryOptions.indexHint

### [**](#limit)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/mongodb/src/MongoConnection.ts#L673)optionallimit

**limit?

<!-- -->

: number

### [**](#loggerContext)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/mongodb/src/MongoConnection.ts#L677)optionalloggerContext

**loggerContext?

<!-- -->

: [LoggingOptions](https://mikro-orm.io/api/core.md#LoggingOptions)

### [**](#maxTimeMS)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/mongodb/src/MongoConnection.ts#L667)optionalinheritedmaxTimeMS

**maxTimeMS?

<!-- -->

: number

Inherited from MongoQueryOptions.maxTimeMS

### [**](#offset)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/mongodb/src/MongoConnection.ts#L674)optionaloffset

**offset?

<!-- -->

: number

### [**](#orderBy)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/mongodb/src/MongoConnection.ts#L672)optionalorderBy

**orderBy?

<!-- -->

: [QueryOrderMap](https://mikro-orm.io/api/core.md#QueryOrderMap)\<T> | [QueryOrderMap](https://mikro-orm.io/api/core.md#QueryOrderMap)\<T>\[]
