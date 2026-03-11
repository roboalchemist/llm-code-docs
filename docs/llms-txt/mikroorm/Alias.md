# Source: https://mikro-orm.io/api/sql/interface/Alias.md

# Alias<!-- --> \<T>

## Index[**](#index)

### Properties

* [**aliasName](#aliasname)
* [**entityName](#entityname)
* [**meta](#meta)
* [**rawTableName](#rawTableName)
* [**subQuery](#subQuery)

## Properties<!-- -->[**](#properties)

### [**](#aliasname)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilderHelper.ts#L1511)aliasName

**aliasName: string

### [**](#entityname)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilderHelper.ts#L1512)entityName

**entityName: [EntityName](https://mikro-orm.io/api/core.md#EntityName)\<T>

### [**](#meta)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilderHelper.ts#L1513)meta

**meta: [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<T, [EntityCtor](https://mikro-orm.io/api/core.md#EntityCtor)\<T>>

### [**](#rawTableName)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilderHelper.ts#L1515)optionalrawTableName

**rawTableName?

<!-- -->

: string

### [**](#subQuery)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilderHelper.ts#L1514)optionalsubQuery

**subQuery?

<!-- -->

: [RawQueryFragment](https://mikro-orm.io/api/core/class/RawQueryFragment.md)\<string> | NativeQueryBuilder
