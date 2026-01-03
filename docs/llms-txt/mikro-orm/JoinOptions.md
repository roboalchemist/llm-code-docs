# Source: https://mikro-orm.io/api/knex/interface/JoinOptions.md

# JoinOptions<!-- -->

## Index[**](#Index)

### Properties

* [**alias](#alias)
* [**cond](#cond)
* [**cond\_](#cond_)
* [**inverseAlias](#inverseAlias)
* [**inverseJoinColumns](#inverseJoinColumns)
* [**joinColumns](#joinColumns)
* [**nested](#nested)
* [**ownerAlias](#ownerAlias)
* [**parent](#parent)
* [**path](#path)
* [**primaryKeys](#primaryKeys)
* [**prop](#prop)
* [**schema](#schema)
* [**subquery](#subquery)
* [**table](#table)
* [**type](#type)

## Properties<!-- -->[**](#Properties)

### [**](#alias)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/typings.ts#L37)alias

**alias: string

### [**](#cond)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/typings.ts#L45)cond

**cond: [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)

### [**](#cond_)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/typings.ts#L48)optionalcond\_

**cond\_?

<!-- -->

: [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)

### [**](#inverseAlias)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/typings.ts#L39)optionalinverseAlias

**inverseAlias?

<!-- -->

: string

### [**](#inverseJoinColumns)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/typings.ts#L41)optionalinverseJoinColumns

**inverseJoinColumns?

<!-- -->

: string\[]

### [**](#joinColumns)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/typings.ts#L40)optionaljoinColumns

**joinColumns?

<!-- -->

: string\[]

### [**](#nested)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/typings.ts#L50)optionalnested

**nested?

<!-- -->

: Set<[JoinOptions](https://mikro-orm.io/api/knex/interface/JoinOptions.md)>

### [**](#ownerAlias)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/typings.ts#L38)ownerAlias

**ownerAlias: string

### [**](#parent)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/typings.ts#L51)optionalparent

**parent?

<!-- -->

: [JoinOptions](https://mikro-orm.io/api/knex/interface/JoinOptions.md)

### [**](#path)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/typings.ts#L43)optionalpath

**path?

<!-- -->

: string

### [**](#primaryKeys)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/typings.ts#L42)optionalprimaryKeys

**primaryKeys?

<!-- -->

: string\[]

### [**](#prop)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/typings.ts#L44)prop

**prop: [EntityProperty](https://mikro-orm.io/api/core/interface/EntityProperty.md)\<any, any>

### [**](#schema)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/typings.ts#L35)optionalschema

**schema?

<!-- -->

: string

### [**](#subquery)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/typings.ts#L49)optionalsubquery

**subquery?

<!-- -->

: string

### [**](#table)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/typings.ts#L34)table

**table: string

### [**](#type)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/typings.ts#L36)type

**type: [JoinType](https://mikro-orm.io/api/knex/enum/JoinType.md)
