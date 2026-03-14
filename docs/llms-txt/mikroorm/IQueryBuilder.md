# Source: https://mikro-orm.io/api/sql/interface/IQueryBuilder.md

# IQueryBuilder<!-- --> \<T>

## Index[**](#index)

### Properties

* [**alias](#alias)
* [**type](#type)

### Methods

* [**addSelect](#addselect)
* [**andWhere](#andwhere)
* [**clone](#clone)
* [**count](#count)
* [**delete](#delete)
* [**from](#from)
* [**getAliasForJoinPath](#getaliasforjoinpath)
* [**getJoinForPath](#getjoinforpath)
* [**getNextAlias](#getnextalias)
* [**groupBy](#groupby)
* [**hasFlag](#hasflag)
* [**having](#having)
* [**innerJoin](#innerjoin)
* [**innerJoinAndSelect](#innerjoinandselect)
* [**insert](#insert)
* [**join](#join)
* [**joinAndSelect](#joinandselect)
* [**leftJoin](#leftjoin)
* [**leftJoinAndSelect](#leftjoinandselect)
* [**orderBy](#orderby)
* [**orWhere](#orwhere)
* [**select](#select)
* [**setFlag](#setflag)
* [**scheduleFilterCheck](#schedulefiltercheck)
* [**truncate](#truncate)
* [**unsetFlag](#unsetflag)
* [**update](#update)
* [**where](#where)
* [**with](#with)
* [**withRecursive](#withrecursive)
* [**withSchema](#withschema)
* [**withSubQuery](#withsubquery)

## Properties<!-- -->[**](#properties)

### [**](#alias)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/typings.ts#L190)readonlyalias

**alias: string

### [**](#type)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/typings.ts#L191)readonlytype

**type: [QueryType](https://mikro-orm.io/api/sql/enum/QueryType.md)

## Methods<!-- -->[**](#methods)

### [**](#addselect)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/typings.ts#L197)addSelect

* ****addSelect**(fields): this

* #### Parameters

  * ##### fields: string | string\[]

  #### Returns this

### [**](#andwhere)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/typings.ts#L216)andWhere

* ****andWhere**(cond, params): this

* #### Parameters

  * ##### cond: string | [RawQueryFragment](https://mikro-orm.io/api/core/class/RawQueryFragment.md)\<string> | [Dictionary](https://mikro-orm.io/api/core.md#Dictionary) | [FilterQuery](https://mikro-orm.io/api/core.md#FilterQuery)\<T>

  * ##### optionalparams: any\[]

  #### Returns this

### [**](#clone)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/typings.ts#L224)clone

* ****clone**(reset, preserve): [IQueryBuilder](https://mikro-orm.io/api/sql/interface/IQueryBuilder.md)\<T>

* #### Parameters

  * ##### optionalreset: boolean | string\[]

  * ##### optionalpreserve: string\[]

  #### Returns [IQueryBuilder](https://mikro-orm.io/api/sql/interface/IQueryBuilder.md)\<T>

### [**](#count)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/typings.ts#L203)count

* ****count**(field, distinct): this

* #### Parameters

  * ##### optionalfield: string | string\[]

  * ##### optionaldistinct: boolean

  #### Returns this

### [**](#delete)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/typings.ts#L201)delete

* ****delete**(cond): this

* #### Parameters

  * ##### optionalcond: any

  #### Returns this

### [**](#from)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/typings.ts#L198)from

* ****from**\<T>(target, aliasName): [IQueryBuilder](https://mikro-orm.io/api/sql/interface/IQueryBuilder.md)\<T>

* #### Parameters

  * ##### target: [EntityName](https://mikro-orm.io/api/core.md#EntityName)\<T> | [IQueryBuilder](https://mikro-orm.io/api/sql/interface/IQueryBuilder.md)\<T>

  * ##### optionalaliasName: string

  #### Returns [IQueryBuilder](https://mikro-orm.io/api/sql/interface/IQueryBuilder.md)\<T>

### [**](#getaliasforjoinpath)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/typings.ts#L221)getAliasForJoinPath

* ****getAliasForJoinPath**(path, options): undefined | string

* #### Parameters

  * ##### path: string

  * ##### optionaloptions: [ICriteriaNodeProcessOptions](https://mikro-orm.io/api/sql/interface/ICriteriaNodeProcessOptions.md)

  #### Returns undefined | string

### [**](#getjoinforpath)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/typings.ts#L222)getJoinForPath

* ****getJoinForPath**(path, options): undefined | [JoinOptions](https://mikro-orm.io/api/sql/interface/JoinOptions.md)

* #### Parameters

  * ##### optionalpath: string

  * ##### optionaloptions: [ICriteriaNodeProcessOptions](https://mikro-orm.io/api/sql/interface/ICriteriaNodeProcessOptions.md)

  #### Returns undefined | [JoinOptions](https://mikro-orm.io/api/sql/interface/JoinOptions.md)

### [**](#getnextalias)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/typings.ts#L223)getNextAlias

* ****getNextAlias**(entityName): string

* #### Parameters

  * ##### optionalentityName: string | [EntityName](https://mikro-orm.io/api/core.md#EntityName)\<T>

  #### Returns string

### [**](#groupby)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/typings.ts#L219)groupBy

* ****groupBy**(fields): this

* #### Parameters

  * ##### fields: string | keyof<!-- --> T | (string | keyof<!-- --> T)\[]

  #### Returns this

### [**](#hasflag)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/typings.ts#L227)hasFlag

* ****hasFlag**(flag): boolean

* #### Parameters

  * ##### flag: [QueryFlag](https://mikro-orm.io/api/core/enum/QueryFlag.md)

  #### Returns boolean

### [**](#having)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/typings.ts#L220)having

* ****having**(cond, params): this

* #### Parameters

  * ##### optionalcond: any

  * ##### optionalparams: any\[]

  #### Returns this

### [**](#innerjoin)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/typings.ts#L205)innerJoin

* ****innerJoin**(field, alias, cond): this

* #### Parameters

  * ##### field: string

  * ##### alias: string

  * ##### optionalcond: any

  #### Returns this

### [**](#innerjoinandselect)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/typings.ts#L209)innerJoinAndSelect

* ****innerJoinAndSelect**(field, alias, cond, fields): this

* #### Parameters

  * ##### field: any

  * ##### alias: string

  * ##### optionalcond: any

  * ##### optionalfields: string\[]

  #### Returns this

### [**](#insert)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/typings.ts#L199)insert

* ****insert**(data): this

* #### Parameters

  * ##### data: any

  #### Returns this

### [**](#join)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/typings.ts#L204)join

* ****join**(field, alias, cond, type, path): this

* #### Parameters

  * ##### field: string

  * ##### alias: string

  * ##### optionalcond: any

  * ##### optionaltype: [JoinType](https://mikro-orm.io/api/sql/enum/JoinType.md)

  * ##### optionalpath: string

  #### Returns this

### [**](#joinandselect)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/typings.ts#L207)joinAndSelect

* ****joinAndSelect**(field, alias, cond): this

* #### Parameters

  * ##### field: any

  * ##### alias: string

  * ##### optionalcond: any

  #### Returns this

### [**](#leftjoin)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/typings.ts#L206)leftJoin

* ****leftJoin**(field, alias, cond): this

* #### Parameters

  * ##### field: string

  * ##### alias: string

  * ##### optionalcond: any

  #### Returns this

### [**](#leftjoinandselect)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/typings.ts#L208)leftJoinAndSelect

* ****leftJoinAndSelect**(field, alias, cond, fields): this

* #### Parameters

  * ##### field: any

  * ##### alias: string

  * ##### optionalcond: any

  * ##### optionalfields: string\[]

  #### Returns this

### [**](#orderby)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/typings.ts#L218)orderBy

* ****orderBy**(orderBy): this

* #### Parameters

  * ##### orderBy: [QueryOrderMap](https://mikro-orm.io/api/core.md#QueryOrderMap)\<T>

  #### Returns this

### [**](#orwhere)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/typings.ts#L217)orWhere

* ****orWhere**(cond, params): this

* #### Parameters

  * ##### cond: string | [RawQueryFragment](https://mikro-orm.io/api/core/class/RawQueryFragment.md)\<string> | [Dictionary](https://mikro-orm.io/api/core.md#Dictionary) | [FilterQuery](https://mikro-orm.io/api/core.md#FilterQuery)\<T>

  * ##### optionalparams: any\[]

  #### Returns this

### [**](#select)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/typings.ts#L196)select

* ****select**(fields, distinct): this

* #### Parameters

  * ##### fields: string | [RawQueryFragment](https://mikro-orm.io/api/core/class/RawQueryFragment.md)\<string> | (string | [RawQueryFragment](https://mikro-orm.io/api/core/class/RawQueryFragment.md)\<string>)\[]

  * ##### optionaldistinct: boolean

  #### Returns this

### [**](#setflag)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/typings.ts#L225)setFlag

* ****setFlag**(flag): this

* #### Parameters

  * ##### flag: [QueryFlag](https://mikro-orm.io/api/core/enum/QueryFlag.md)

  #### Returns this

### [**](#schedulefiltercheck)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/typings.ts#L234)scheduleFilterCheck

* ****scheduleFilterCheck**(path): void

* #### Parameters

  * ##### path: string

  #### Returns void

### [**](#truncate)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/typings.ts#L202)truncate

* ****truncate**(): this

* #### Returns this

### [**](#unsetflag)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/typings.ts#L226)unsetFlag

* ****unsetFlag**(flag): this

* #### Parameters

  * ##### flag: [QueryFlag](https://mikro-orm.io/api/core/enum/QueryFlag.md)

  #### Returns this

### [**](#update)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/typings.ts#L200)update

* ****update**(data): this

* #### Parameters

  * ##### data: any

  #### Returns this

### [**](#where)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/typings.ts#L211)where

* ****where**(cond, operator, operator2): this

* #### Parameters

  * ##### cond: string | [RawQueryFragment](https://mikro-orm.io/api/core/class/RawQueryFragment.md)\<string> | [Dictionary](https://mikro-orm.io/api/core.md#Dictionary) | [FilterQuery](https://mikro-orm.io/api/core.md#FilterQuery)\<T>

  * ##### optionaloperator: any\[] | $and | $or

  * ##### optionaloperator2: $and | $or

  #### Returns this

### [**](#with)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/typings.ts#L228)with

* ****with**(name, query, options): this

* #### Parameters

  * ##### name: string

  * ##### query: [RawQueryFragment](https://mikro-orm.io/api/core/class/RawQueryFragment.md)\<string> | NativeQueryBuilder | [AnyQueryBuilder](https://mikro-orm.io/api/sql.md#AnyQueryBuilder)

  * ##### optionaloptions: [CteOptions](https://mikro-orm.io/api/sql/interface/CteOptions.md)

  #### Returns this

### [**](#withrecursive)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/typings.ts#L229)withRecursive

* ****withRecursive**(name, query, options): this

* #### Parameters

  * ##### name: string

  * ##### query: [RawQueryFragment](https://mikro-orm.io/api/core/class/RawQueryFragment.md)\<string> | NativeQueryBuilder | [AnyQueryBuilder](https://mikro-orm.io/api/sql.md#AnyQueryBuilder)

  * ##### optionaloptions: [CteOptions](https://mikro-orm.io/api/sql/interface/CteOptions.md)

  #### Returns this

### [**](#withschema)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/typings.ts#L235)withSchema

* ****withSchema**(schema): this

* #### Parameters

  * ##### schema: string

  #### Returns this

### [**](#withsubquery)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/typings.ts#L210)withSubQuery

* ****withSubQuery**(subQuery, alias): this

* #### Parameters

  * ##### subQuery: [RawQueryFragment](https://mikro-orm.io/api/core/class/RawQueryFragment.md)\<string> | NativeQueryBuilder

  * ##### alias: string

  #### Returns this
