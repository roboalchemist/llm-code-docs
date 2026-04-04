# Source: https://mikro-orm.io/api/sql/interface/DatabaseView.md

# DatabaseView<!-- -->

## Index[**](#index)

### Properties

* [**definition](#definition)
* [**materialized](#materialized)
* [**name](#name)
* [**schema](#schema)
* [**withData](#withData)

## Properties<!-- -->[**](#properties)

### [**](#definition)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/typings.ts#L167)definition

**definition: string

### [**](#materialized)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/typings.ts#L169)optionalmaterialized

**materialized?

<!-- -->

: boolean

True if this is a materialized view (PostgreSQL only).

### [**](#name)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/typings.ts#L165)name

**name: string

### [**](#schema)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/typings.ts#L166)optionalschema

**schema?

<!-- -->

: string

### [**](#withData)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/typings.ts#L171)optionalwithData

**withData?

<!-- -->

: boolean

For materialized views, whether data was populated on creation.
