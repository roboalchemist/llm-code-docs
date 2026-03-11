# Source: https://mikro-orm.io/api/sql/interface/IndexDef.md

# IndexDef<!-- -->

## Index[**](#index)

### Properties

* [**clustered](#clustered)
* [**columnNames](#columnnames)
* [**columns](#columns)
* [**composite](#composite)
* [**constraint](#constraint)
* [**deferMode](#deferMode)
* [**disabled](#disabled)
* [**expression](#expression)
* [**fillFactor](#fillFactor)
* [**include](#include)
* [**invisible](#invisible)
* [**keyName](#keyname)
* [**options](#options)
* [**primary](#primary)
* [**type](#type)
* [**unique](#unique)

## Properties<!-- -->[**](#properties)

### [**](#clustered)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/typings.ts#L126)optionalclustered

**clustered?

<!-- -->

: boolean

Whether the index should be clustered (MariaDB, MSSQL).

### [**](#columnnames)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/typings.ts#L94)columnNames

**columnNames: string\[]

### [**](#columns)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/typings.ts#L108)optionalcolumns

**columns?

<!-- -->

: [IndexColumnOptions](https://mikro-orm.io/api/core/interface/IndexColumnOptions.md)\[]

Advanced column options for the index. When specified, these options override the simple columnNames for index generation.

### [**](#composite)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/typings.ts#L99)optionalcomposite

**composite?

<!-- -->

: boolean

### [**](#constraint)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/typings.ts#L97)constraint

**constraint: boolean

### [**](#deferMode)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/typings.ts#L103)optionaldeferMode

**deferMode?

<!-- -->

: [DeferMode](https://mikro-orm.io/api/core/enum/DeferMode.md) | immediate | deferred

### [**](#disabled)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/typings.ts#L122)optionaldisabled

**disabled?

<!-- -->

: boolean

Whether the index is disabled (MSSQL only).

### [**](#expression)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/typings.ts#L100)optionalexpression

**expression?

<!-- -->

: string

### [**](#fillFactor)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/typings.ts#L114)optionalfillFactor

**fillFactor?

<!-- -->

: number

Fill factor for the index as a percentage 0-100 (PostgreSQL, MSSQL).

### [**](#include)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/typings.ts#L112)optionalinclude

**include?

<!-- -->

: string\[]

Columns to include in the index but not as part of the key (PostgreSQL, MSSQL).

### [**](#invisible)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/typings.ts#L118)optionalinvisible

**invisible?

<!-- -->

: boolean

Whether the index is invisible/hidden from the query optimizer (MySQL 8+, MariaDB 10.6+, MongoDB).

### [**](#keyname)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/typings.ts#L95)keyName

**keyName: string

### [**](#options)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/typings.ts#L101)optionaloptions

**options?

<!-- -->

: [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)

### [**](#primary)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/typings.ts#L98)primary

**primary: boolean

### [**](#type)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/typings.ts#L102)optionaltype

**type?

<!-- -->

: string | Readonly<{ indexType?

<!-- -->

: string; predicate?

<!-- -->

: string; storageEngineIndexType?

<!-- -->

: hash | btree }>

### [**](#unique)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/typings.ts#L96)unique

**unique: boolean
