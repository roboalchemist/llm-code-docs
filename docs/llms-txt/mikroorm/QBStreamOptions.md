# Source: https://mikro-orm.io/api/sql/interface/QBStreamOptions.md

# QBStreamOptions<!-- -->

## Index[**](#index)

### Properties

* [**mapResults](#mapResults)
* [**mergeResults](#mergeResults)
* [**rawResults](#rawResults)

## Properties<!-- -->[**](#properties)

### [**](#mapResults)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L77)optionalmapResults

**mapResults?

<!-- -->

: boolean = true

Results are mapped to entities, if you set `mapResults: false` you will get POJOs instead.

### [**](#mergeResults)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L88)optionalmergeResults

**mergeResults?

<!-- -->

: boolean = true

When populating to-many relations, the ORM streams fully merged entities instead of yielding every row. You can opt out of this behavior by specifying `mergeResults: false`. This will yield every row from the SQL result, but still mapped to entities, meaning that to-many collections will contain at most one item, and you will get duplicate root entities when they have multiple items in the populated collection.

### [**](#rawResults)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L95)optionalrawResults

**rawResults?

<!-- -->

: boolean = false

When enabled, the driver will return the raw database results without renaming the fields to match the entity property names.
