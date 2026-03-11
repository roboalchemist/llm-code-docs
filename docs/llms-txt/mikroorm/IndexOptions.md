# Source: https://mikro-orm.io/api/core/interface/IndexOptions.md

# IndexOptions<!-- --> \<T, H>

### Hierarchy

* BaseOptions\<T, H>
  * *IndexOptions*

## Index[**](#index)

### Properties

* [**clustered](#clustered)
* [**columns](#columns)
* [**disabled](#disabled)
* [**expression](#expression)
* [**fillFactor](#fillFactor)
* [**include](#include)
* [**invisible](#invisible)
* [**name](#name)
* [**options](#options)
* [**properties](#properties)
* [**type](#type)

## Properties<!-- -->[**](#properties)

### [**](#clustered)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/types.ts#L731)optionalclustered

**clustered?

<!-- -->

: boolean

Whether the index should be clustered (MariaDB, MSSQL). A clustered index determines the physical order of data in the table. Only one clustered index can exist per table.

### [**](#columns)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/types.ts#L692)optionalinheritedcolumns

**columns?

<!-- -->

: [IndexColumnOptions](https://mikro-orm.io/api/core/interface/IndexColumnOptions.md)\[]

Inherited from BaseOptions.columns

Advanced column options for the index. When specified, allows fine-grained control over each column in the index including sort order, nulls ordering, prefix length, and collation. If both `columns` and `properties` are specified, `columns` takes precedence for index creation.

### [**](#disabled)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/types.ts#L725)optionaldisabled

**disabled?

<!-- -->

: boolean

Whether the index is disabled (MSSQL only). A disabled index is not used for query planning and is not maintained on writes. It can be re-enabled later using `ALTER INDEX ... REBUILD`.

### [**](#expression)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/types.ts#L685)optionalinheritedexpression

**expression?

<!-- -->

: string | (T extends [EntityClass](https://mikro-orm.io/api/core.md#EntityClass)\<P> ? [IndexCallback](https://mikro-orm.io/api/core.md#IndexCallback)\<P> : [IndexCallback](https://mikro-orm.io/api/core.md#IndexCallback)\<T>)

Inherited from BaseOptions.expression

### [**](#fillFactor)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/types.ts#L699)optionalinheritedfillFactor

**fillFactor?

<!-- -->

: number

Inherited from BaseOptions.fillFactor

Fill factor for the index as a percentage 0-100 (PostgreSQL, MSSQL).

### [**](#include)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/types.ts#L697)optionalinheritedinclude

**include?

<!-- -->

: T extends [EntityClass](https://mikro-orm.io/api/core.md#EntityClass)\<P> ? Properties\<P, H> : Properties\<T, H>

Inherited from BaseOptions.include

Columns to include in the index but not as part of the key (PostgreSQL, MSSQL). These columns are stored in the leaf level of the index but not used for searching.

### [**](#invisible)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/types.ts#L719)optionalinvisible

**invisible?

<!-- -->

: boolean

Whether the index is invisible/hidden from the query optimizer (MySQL 8+, MariaDB 10.6+, MongoDB). An invisible index is still maintained on writes but not used for query planning. Useful for testing the impact of removing an index before actually dropping it.

### [**](#name)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/types.ts#L682)optionalinheritedname

**name?

<!-- -->

: string

Inherited from BaseOptions.name

### [**](#options)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/types.ts#L684)optionalinheritedoptions

**options?

<!-- -->

: [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)

Inherited from BaseOptions.options

### [**](#properties)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/types.ts#L683)optionalinheritedproperties

**properties?

<!-- -->

: T extends [EntityClass](https://mikro-orm.io/api/core.md#EntityClass)\<P> ? Properties\<P, H> : Properties\<T, H>

Inherited from BaseOptions.properties

### [**](#type)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/types.ts#L713)optionaltype

**type?

<!-- -->

: string
