# Source: https://mikro-orm.io/api/sql/interface/OnConflictClause.md

# OnConflictClause<!-- --> \<T>

## Index[**](#index)

### Properties

* [**fields](#fields)
* [**ignore](#ignore)
* [**merge](#merge)
* [**where](#where)

## Properties<!-- -->[**](#properties)

### [**](#fields)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilderHelper.ts#L1519)fields

**fields: [RawQueryFragment](https://mikro-orm.io/api/core/class/RawQueryFragment.md)\<string> | string\[]

### [**](#ignore)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilderHelper.ts#L1520)optionalignore

**ignore?

<!-- -->

: boolean

### [**](#merge)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilderHelper.ts#L1521)optionalmerge

**merge?

<!-- -->

: InternalField\<T>\[] | [EntityData](https://mikro-orm.io/api/core.md#EntityData)\<T>

### [**](#where)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilderHelper.ts#L1522)optionalwhere

**where?

<!-- -->

: [FilterQuery](https://mikro-orm.io/api/core.md#FilterQuery)\<T>
