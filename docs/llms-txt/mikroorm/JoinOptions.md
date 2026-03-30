# Source: https://mikro-orm.io/api/sql/interface/JoinOptions.md

# JoinOptions<!-- -->

## Index[**](#index)

### Properties

* [**alias](#alias)
* [**cond](#cond)
* [**cond\_](#cond_)
* [**inverseAlias](#inverseAlias)
* [**inverseJoinColumns](#inverseJoinColumns)
* [**joinColumns](#joinColumns)
* [**nested](#nested)
* [**ownerAlias](#owneralias)
* [**parent](#parent)
* [**path](#path)
* [**primaryKeys](#primaryKeys)
* [**prop](#prop)
* [**schema](#schema)
* [**subquery](#subquery)
* [**table](#table)
* [**type](#type)

## Properties<!-- -->[**](#properties)

### [**](#alias)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/typings.ts#L42)alias

**alias: string

### [**](#cond)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/typings.ts#L50)cond

**cond: [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)

### [**](#cond_)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/typings.ts#L53)optionalcond\_

**cond\_?

<!-- -->

: [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)

### [**](#inverseAlias)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/typings.ts#L44)optionalinverseAlias

**inverseAlias?

<!-- -->

: string

### [**](#inverseJoinColumns)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/typings.ts#L46)optionalinverseJoinColumns

**inverseJoinColumns?

<!-- -->

: string\[]

### [**](#joinColumns)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/typings.ts#L45)optionaljoinColumns

**joinColumns?

<!-- -->

: string\[]

### [**](#nested)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/typings.ts#L55)optionalnested

**nested?

<!-- -->

: Set<[JoinOptions](https://mikro-orm.io/api/sql/interface/JoinOptions.md)>

### [**](#owneralias)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/typings.ts#L43)ownerAlias

**ownerAlias: string

### [**](#parent)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/typings.ts#L56)optionalparent

**parent?

<!-- -->

: [JoinOptions](https://mikro-orm.io/api/sql/interface/JoinOptions.md)

### [**](#path)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/typings.ts#L48)optionalpath

**path?

<!-- -->

: string

### [**](#primaryKeys)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/typings.ts#L47)optionalprimaryKeys

**primaryKeys?

<!-- -->

: string\[]

### [**](#prop)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/typings.ts#L49)prop

**prop: [EntityProperty](https://mikro-orm.io/api/core/interface/EntityProperty.md)\<any, any>

### [**](#schema)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/typings.ts#L40)optionalschema

**schema?

<!-- -->

: string

### [**](#subquery)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/typings.ts#L54)optionalsubquery

**subquery?

<!-- -->

: string

### [**](#table)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/typings.ts#L39)table

**table: string

### [**](#type)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/typings.ts#L41)type

**type: [JoinType](https://mikro-orm.io/api/sql/enum/JoinType.md)
