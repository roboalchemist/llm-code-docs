# Source: https://mikro-orm.io/api/knex/interface/IQueryBuilder.md

# IQueryBuilder<!-- --> \<T>

## Index[**](#Index)

### Properties

* [**\_fields](#_fields)
* [**alias](#alias)
* [**type](#type)

### Methods

* [**addSelect](#addSelect)
* [**andWhere](#andWhere)
* [**clone](#clone)
* [**count](#count)
* [**delete](#delete)
* [**from](#from)
* [**getAliasForJoinPath](#getAliasForJoinPath)
* [**getJoinForPath](#getJoinForPath)
* [**getNextAlias](#getNextAlias)
* [**groupBy](#groupBy)
* [**hasFlag](#hasFlag)
* [**having](#having)
* [**innerJoin](#innerJoin)
* [**innerJoinAndSelect](#innerJoinAndSelect)
* [**insert](#insert)
* [**join](#join)
* [**joinAndSelect](#joinAndSelect)
* [**leftJoin](#leftJoin)
* [**leftJoinAndSelect](#leftJoinAndSelect)
* [**orderBy](#orderBy)
* [**orWhere](#orWhere)
* [**scheduleFilterCheck](#scheduleFilterCheck)
* [**select](#select)
* [**setFlag](#setFlag)
* [**truncate](#truncate)
* [**unsetFlag](#unsetFlag)
* [**update](#update)
* [**where](#where)
* [**withSubQuery](#withSubQuery)

## Properties<!-- -->[**](#Properties)

### [**](#_fields)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/typings.ts#L150)optional\_fields

**\_fields?

<!-- -->

: [Field](https://mikro-orm.io/api/knex.md#Field)\<T>\[]

### [**](#alias)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/typings.ts#L148)readonlyalias

**alias: string

### [**](#type)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/typings.ts#L149)optionalreadonlytype

**type?

<!-- -->

: [QueryType](https://mikro-orm.io/api/knex/enum/QueryType.md)

## Methods<!-- -->[**](#Methods)

### [**](#addSelect)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/typings.ts#L154)addSelect

* ****addSelect**(fields): this

- #### Parameters

  * ##### fields: string | string\[]

  #### Returns this

### [**](#andWhere)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/typings.ts#L170)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/typings.ts#L171)andWhere

* ****andWhere**(cond): this
* ****andWhere**(cond, params): this

- #### Parameters

  * ##### cond: [QBFilterQuery](https://mikro-orm.io/api/core.md#QBFilterQuery)\<T>

  #### Returns this

### [**](#clone)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/typings.ts#L180)clone

* ****clone**(reset): [IQueryBuilder](https://mikro-orm.io/api/knex/interface/IQueryBuilder.md)\<T>

- #### Parameters

  * ##### optionalreset: boolean

  #### Returns [IQueryBuilder](https://mikro-orm.io/api/knex/interface/IQueryBuilder.md)\<T>

### [**](#count)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/typings.ts#L160)count

* ****count**(field, distinct): this

- #### Parameters

  * ##### optionalfield: string | string\[]
  * ##### optionaldistinct: boolean

  #### Returns this

### [**](#delete)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/typings.ts#L158)delete

* ****delete**(cond): this

- #### Parameters

  * ##### optionalcond: [QBFilterQuery](https://mikro-orm.io/api/core.md#QBFilterQuery)

  #### Returns this

### [**](#from)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/typings.ts#L155)from

* ****from**\<T>(target, aliasName): [IQueryBuilder](https://mikro-orm.io/api/knex/interface/IQueryBuilder.md)\<T>

- #### Parameters

  * ##### target: [EntityName](https://mikro-orm.io/api/core.md#EntityName)\<T> | [IQueryBuilder](https://mikro-orm.io/api/knex/interface/IQueryBuilder.md)\<T>
  * ##### optionalaliasName: string

  #### Returns [IQueryBuilder](https://mikro-orm.io/api/knex/interface/IQueryBuilder.md)\<T>

### [**](#getAliasForJoinPath)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/typings.ts#L177)getAliasForJoinPath

* ****getAliasForJoinPath**(path, options): undefined | string

- #### Parameters

  * ##### path: string
  * ##### optionaloptions: [ICriteriaNodeProcessOptions](https://mikro-orm.io/api/knex/interface/ICriteriaNodeProcessOptions.md)

  #### Returns undefined | string

### [**](#getJoinForPath)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/typings.ts#L178)getJoinForPath

* ****getJoinForPath**(path, options): undefined | [JoinOptions](https://mikro-orm.io/api/knex/interface/JoinOptions.md)

- #### Parameters

  * ##### optionalpath: string
  * ##### optionaloptions: [ICriteriaNodeProcessOptions](https://mikro-orm.io/api/knex/interface/ICriteriaNodeProcessOptions.md)

  #### Returns undefined | [JoinOptions](https://mikro-orm.io/api/knex/interface/JoinOptions.md)

### [**](#getNextAlias)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/typings.ts#L179)getNextAlias

* ****getNextAlias**(entityName): string

- #### Parameters

  * ##### optionalentityName: string

  #### Returns string

### [**](#groupBy)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/typings.ts#L175)groupBy

* ****groupBy**(fields): this

- #### Parameters

  * ##### fields: string | keyof<!-- --> T | (string | keyof<!-- --> T)\[]

  #### Returns this

### [**](#hasFlag)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/typings.ts#L183)hasFlag

* ****hasFlag**(flag): boolean

- #### Parameters

  * ##### flag: [QueryFlag](https://mikro-orm.io/api/core/enum/QueryFlag.md)

  #### Returns boolean

### [**](#having)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/typings.ts#L176)having

* ****having**(cond, params): this

- #### Parameters

  * ##### optionalcond: string | [QBFilterQuery](https://mikro-orm.io/api/core.md#QBFilterQuery)
  * ##### optionalparams: any\[]

  #### Returns this

### [**](#innerJoin)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/typings.ts#L162)innerJoin

* ****innerJoin**(field, alias, cond): this

- #### Parameters

  * ##### field: string
  * ##### alias: string
  * ##### optionalcond: [QBFilterQuery](https://mikro-orm.io/api/core.md#QBFilterQuery)

  #### Returns this

### [**](#innerJoinAndSelect)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/typings.ts#L166)innerJoinAndSelect

* ****innerJoinAndSelect**(field, alias, cond, fields): this

- #### Parameters

  * ##### field: string
  * ##### alias: string
  * ##### optionalcond: [QBFilterQuery](https://mikro-orm.io/api/core.md#QBFilterQuery)
  * ##### optionalfields: string\[]

  #### Returns this

### [**](#insert)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/typings.ts#L156)insert

* ****insert**(data): this

- #### Parameters

  * ##### data: any

  #### Returns this

### [**](#join)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/typings.ts#L161)join

* ****join**(field, alias, cond, type, path): this

- #### Parameters

  * ##### field: string
  * ##### alias: string
  * ##### optionalcond: [QBFilterQuery](https://mikro-orm.io/api/core.md#QBFilterQuery)
  * ##### optionaltype: [JoinType](https://mikro-orm.io/api/knex/enum/JoinType.md)
  * ##### optionalpath: string

  #### Returns this

### [**](#joinAndSelect)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/typings.ts#L164)joinAndSelect

* ****joinAndSelect**(field, alias, cond): this

- #### Parameters

  * ##### field: string
  * ##### alias: string
  * ##### optionalcond: [QBFilterQuery](https://mikro-orm.io/api/core.md#QBFilterQuery)

  #### Returns this

### [**](#leftJoin)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/typings.ts#L163)leftJoin

* ****leftJoin**(field, alias, cond): this

- #### Parameters

  * ##### field: string
  * ##### alias: string
  * ##### optionalcond: [QBFilterQuery](https://mikro-orm.io/api/core.md#QBFilterQuery)

  #### Returns this

### [**](#leftJoinAndSelect)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/typings.ts#L165)leftJoinAndSelect

* ****leftJoinAndSelect**(field, alias, cond, fields): this

- #### Parameters

  * ##### field: string
  * ##### alias: string
  * ##### optionalcond: [QBFilterQuery](https://mikro-orm.io/api/core.md#QBFilterQuery)
  * ##### optionalfields: string\[]

  #### Returns this

### [**](#orderBy)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/typings.ts#L174)orderBy

* ****orderBy**(orderBy): this

- #### Parameters

  * ##### orderBy: [QueryOrderMap](https://mikro-orm.io/api/core.md#QueryOrderMap)\<T>

  #### Returns this

### [**](#orWhere)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/typings.ts#L172)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/typings.ts#L173)orWhere

* ****orWhere**(cond): this
* ****orWhere**(cond, params): this

- #### Parameters

  * ##### cond: [QBFilterQuery](https://mikro-orm.io/api/core.md#QBFilterQuery)\<T>

  #### Returns this

### [**](#scheduleFilterCheck)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/typings.ts#L184)scheduleFilterCheck

* ****scheduleFilterCheck**(path): void

- #### Parameters

  * ##### path: string

  #### Returns void

### [**](#select)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/typings.ts#L153)select

* ****select**(fields, distinct): this

- #### Parameters

  * ##### fields: [Field](https://mikro-orm.io/api/knex.md#Field)\<T> | [Field](https://mikro-orm.io/api/knex.md#Field)\<T>\[]
  * ##### optionaldistinct: boolean

  #### Returns this

### [**](#setFlag)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/typings.ts#L181)setFlag

* ****setFlag**(flag): this

- #### Parameters

  * ##### flag: [QueryFlag](https://mikro-orm.io/api/core/enum/QueryFlag.md)

  #### Returns this

### [**](#truncate)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/typings.ts#L159)truncate

* ****truncate**(): this

- #### Returns this

### [**](#unsetFlag)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/typings.ts#L182)unsetFlag

* ****unsetFlag**(flag): this

- #### Parameters

  * ##### flag: [QueryFlag](https://mikro-orm.io/api/core/enum/QueryFlag.md)

  #### Returns this

### [**](#update)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/typings.ts#L157)update

* ****update**(data): this

- #### Parameters

  * ##### data: any

  #### Returns this

### [**](#where)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/typings.ts#L168)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/typings.ts#L169)where

* ****where**(cond, operator): this
* ****where**(cond, params, operator): this

- #### Parameters

  * ##### cond: [QBFilterQuery](https://mikro-orm.io/api/core.md#QBFilterQuery)\<T>
  * ##### optionaloperator: $and | $or

  #### Returns this

### [**](#withSubQuery)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/typings.ts#L167)withSubQuery

* ****withSubQuery**(subQuery, alias): this

- #### Parameters

  * ##### subQuery: QueryBuilder\<any, any>
  * ##### alias: string

  #### Returns this
