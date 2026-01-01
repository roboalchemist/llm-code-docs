# Source: https://mikro-orm.io/api/knex/interface/UpdateQueryBuilder.md

# UpdateQueryBuilder<!-- --> \<T>

### Hierarchy

* [RunQueryBuilder](https://mikro-orm.io/api/knex/interface/RunQueryBuilder.md)\<T>
  * *UpdateQueryBuilder*

## Index[**](#Index)

### Properties

* [**alias](#alias)
* [**helper](#helper)
* [**mainAlias](#mainAlias)

### Methods

* [**addSelect](#addSelect)
* [**andHaving](#andHaving)
* [**andWhere](#andWhere)
* [**applyFilters](#applyFilters)
* [**as](#as)
* [**cache](#cache)
* [**clone](#clone)
* [**comment](#comment)
* [**count](#count)
* [**delete](#delete)
* [**distinct](#distinct)
* [**distinctOn](#distinctOn)
* [**execute](#execute)
* [**from](#from)
* [**getCount](#getCount)
* [**getFormattedQuery](#getFormattedQuery)
* [**getKnex](#getKnex)
* [**getKnexQuery](#getKnexQuery)
* [**getLoggerContext](#getLoggerContext)
* [**getParams](#getParams)
* [**getQuery](#getQuery)
* [**getResultAndCount](#getResultAndCount)
* [**groupBy](#groupBy)
* [**hasFlag](#hasFlag)
* [**having](#having)
* [**hintComment](#hintComment)
* [**ignore](#ignore)
* [**indexHint](#indexHint)
* [**innerJoin](#innerJoin)
* [**innerJoinAndSelect](#innerJoinAndSelect)
* [**innerJoinLateral](#innerJoinLateral)
* [**innerJoinLateralAndSelect](#innerJoinLateralAndSelect)
* [**insert](#insert)
* [**join](#join)
* [**joinAndSelect](#joinAndSelect)
* [**leftJoin](#leftJoin)
* [**leftJoinAndSelect](#leftJoinAndSelect)
* [**leftJoinLateral](#leftJoinLateral)
* [**leftJoinLateralAndSelect](#leftJoinLateralAndSelect)
* [**limit](#limit)
* [**merge](#merge)
* [**offset](#offset)
* [**onConflict](#onConflict)
* [**orderBy](#orderBy)
* [**orHaving](#orHaving)
* [**orWhere](#orWhere)
* [**returning](#returning)
* [**select](#select)
* [**setFlag](#setFlag)
* [**setFlushMode](#setFlushMode)
* [**setLockMode](#setLockMode)
* [**setLoggerContext](#setLoggerContext)
* [**then](#then)
* [**toQuery](#toQuery)
* [**truncate](#truncate)
* [**unsetFlag](#unsetFlag)
* [**update](#update)
* [**where](#where)
* [**withSchema](#withSchema)
* [**withSubQuery](#withSubQuery)

## Properties<!-- -->[**](#Properties)

### [**](#alias)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L150)inheritedalias

**alias: string

Inherited from RunQueryBuilder.alias

### [**](#helper)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L154)inheritedhelper

**helper: QueryBuilderHelper

Inherited from RunQueryBuilder.helper

### [**](#mainAlias)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L145)inheritedmainAlias

**mainAlias: [Alias](https://mikro-orm.io/api/knex/interface/Alias.md)\<T>

Inherited from RunQueryBuilder.mainAlias

## Methods<!-- -->[**](#Methods)

### [**](#addSelect)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L245)inheritedaddSelect

* ****addSelect**(fields): [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<T, any, any, never>

- Inherited from RunQueryBuilder.addSelect

  #### Parameters

  * ##### fields: [Field](https://mikro-orm.io/api/knex.md#Field)\<T> | [Field](https://mikro-orm.io/api/knex.md#Field)\<T>\[]

  #### Returns [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<T, any, any, never>

### [**](#andHaving)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L643)inheritedandHaving

* ****andHaving**(cond, params): [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<T, any, any, never>

- Inherited from RunQueryBuilder.andHaving

  #### Parameters

  * ##### optionalcond: string | [QBFilterQuery](https://mikro-orm.io/api/core.md#QBFilterQuery)
  * ##### optionalparams: any\[]

  #### Returns [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<T, any, any, never>

### [**](#andWhere)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L585)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L586)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L587)inheritedandWhere

* ****andWhere**(cond): this
* ****andWhere**(cond, params): this

- Inherited from RunQueryBuilder.andWhere

  #### Parameters

  * ##### cond: [QBFilterQuery](https://mikro-orm.io/api/core.md#QBFilterQuery)\<T>

  #### Returns this

### [**](#applyFilters)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L475)inheritedapplyFilters

* ****applyFilters**(filterOptions): Promise\<void>

- Inherited from RunQueryBuilder.applyFilters

  Apply filters to the QB where condition.

  ***

  #### Parameters

  * ##### filterOptions: [FilterOptions](https://mikro-orm.io/api/core.md#FilterOptions) = <!-- -->{}

  #### Returns Promise\<void>

### [**](#as)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L1161)inheritedas

* ****as**(alias): QueryBuilder\<any, any>

- Inherited from RunQueryBuilder.as

  Returns knex instance with sub-query aliased with given alias. You can provide `EntityName.propName` as alias, then the field name will be used based on the metadata

  ***

  #### Parameters

  * ##### alias: string

  #### Returns QueryBuilder\<any, any>

### [**](#cache)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L769)inheritedcache

* ****cache**(config): this

- Inherited from RunQueryBuilder.cache

  #### Parameters

  * ##### config: number | boolean | \[string, number] = <!-- -->true

  #### Returns this

### [**](#clone)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L1179)inheritedclone

* ****clone**(reset): [QueryBuilder](https://mikro-orm.io/api/knex/class/QueryBuilder.md)\<T, never, never, never>

- Inherited from RunQueryBuilder.clone

  #### Parameters

  * ##### optionalreset: boolean | string\[]

  #### Returns [QueryBuilder](https://mikro-orm.io/api/knex/class/QueryBuilder.md)\<T, never, never, never>

### [**](#comment)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L787)inheritedcomment

* ****comment**(comment): this

- Inherited from RunQueryBuilder.comment

  Prepend comment to the sql query using the syntax `/* ... *&#8205;/`. Some characters are forbidden such as `/*, *&#8205;/` and `?`.

  ***

  #### Parameters

  * ##### comment: string | string\[]

  #### Returns this

### [**](#count)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L283)inheritedcount

* ****count**(field, distinct): [CountQueryBuilder](https://mikro-orm.io/api/knex/interface/CountQueryBuilder.md)\<T>

- Inherited from RunQueryBuilder.count

  #### Parameters

  * ##### optionalfield: EntityKeyOrString\<T> | EntityKeyOrString\<T>\[]
  * ##### distinct: boolean = <!-- -->false

  #### Returns [CountQueryBuilder](https://mikro-orm.io/api/knex/interface/CountQueryBuilder.md)\<T>

### [**](#delete)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L275)inheriteddelete

* ****delete**(cond): [DeleteQueryBuilder](https://mikro-orm.io/api/knex/interface/DeleteQueryBuilder.md)\<T>

- Inherited from RunQueryBuilder.delete

  #### Parameters

  * ##### optionalcond: [QBFilterQuery](https://mikro-orm.io/api/core.md#QBFilterQuery)

  #### Returns [DeleteQueryBuilder](https://mikro-orm.io/api/knex/interface/DeleteQueryBuilder.md)\<T>

### [**](#distinct)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L255)inheriteddistinct

* ****distinct**(): [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<T, any, any, never>

- Inherited from RunQueryBuilder.distinct

  #### Returns [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<T, any, any, never>

### [**](#distinctOn)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L261)inheriteddistinctOn

* ****distinctOn**(fields): [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<T, any, any, never>

- Inherited from RunQueryBuilder.distinctOn

  postgres only

  ***

  #### Parameters

  * ##### fields: EntityKeyOrString\<T> | EntityKeyOrString\<T>\[]

  #### Returns [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<T, any, any, never>

### [**](#execute)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L2014)inheritedexecute

* ****execute**\<Result>(method, mapResults): Promise\<Result>

- Inherited from RunQueryBuilder.execute

  Executes this QB and returns the raw results, mapped to the property names (unless disabled via last parameter). Use `method` to specify what kind of result you want to get (array/single/meta).

  ***

  #### Parameters

  * ##### optionalmethod: get | all | run
  * ##### optionalmapResults: boolean

  #### Returns Promise\<Result>

### [**](#from)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L808)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L809)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L810)inheritedfrom

* ****from**\<Entity>(target, aliasName): [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<Entity, any, any, never>
* ****from**\<Entity>(target): [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<Entity, any, any, never>

- Inherited from RunQueryBuilder.from

  Specifies FROM which entity's table select/update/delete will be executed, removing all previously set FROM-s. Allows setting a main string alias of the selection data.

  ***

  #### Parameters

  * ##### target: [QueryBuilder](https://mikro-orm.io/api/knex/class/QueryBuilder.md)\<Entity, never, never, never>
  * ##### optionalaliasName: string

  #### Returns [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<Entity, any, any, never>

### [**](#getCount)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L1109)inheritedgetCount

* ****getCount**(field, distinct): Promise\<number>

- Inherited from RunQueryBuilder.getCount

  Executes count query (without offset and limit), returning total count of results

  ***

  #### Parameters

  * ##### optionalfield: EntityKeyOrString\<T> | EntityKeyOrString\<T>\[]
  * ##### optionaldistinct: boolean

  #### Returns Promise\<number>

### [**](#getFormattedQuery)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L911)inheritedgetFormattedQuery

* ****getFormattedQuery**(): string

- Inherited from RunQueryBuilder.getFormattedQuery

  Returns raw interpolated query string with all the parameters inlined.

  ***

  #### Returns string

### [**](#getKnex)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L1219)inheritedgetKnex

* ****getKnex**(processVirtualEntity): QueryBuilder\<any, any>

- Inherited from RunQueryBuilder.getKnex

  #### Parameters

  * ##### processVirtualEntity: boolean = <!-- -->true

  #### Returns QueryBuilder\<any, any>

### [**](#getKnexQuery)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L828)inheritedgetKnexQuery

* ****getKnexQuery**(processVirtualEntity): QueryBuilder\<any, any>

- Inherited from RunQueryBuilder.getKnexQuery

  #### Parameters

  * ##### processVirtualEntity: boolean = <!-- -->true

  #### Returns QueryBuilder\<any, any>

### [**](#getLoggerContext)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L1257)inheritedgetLoggerContext

* ****getLoggerContext**\<T>(): T

- Inherited from RunQueryBuilder.getLoggerContext

  Gets logger context for this query builder.

  ***

  #### Returns T

### [**](#getParams)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L904)inheritedgetParams

* ****getParams**(): readonly
  <!-- -->
  Value\[]

- Inherited from RunQueryBuilder.getParams

  Returns the list of all parameters for this query.

  ***

  #### Returns readonly<!-- --> Value\[]

### [**](#getQuery)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L882)inheritedgetQuery

* ****getQuery**(): string

- Inherited from RunQueryBuilder.getQuery

  Returns the query with parameters as wildcards.

  ***

  #### Returns string

### [**](#getResultAndCount)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L1127)inheritedgetResultAndCount

* ****getResultAndCount**(): Promise<\[T\[], number]>

- Inherited from RunQueryBuilder.getResultAndCount

  Executes the query, returning both array of results and total count query (without offset and limit).

  ***

  #### Returns Promise<\[T\[], number]>

### [**](#groupBy)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L617)inheritedgroupBy

* ****groupBy**(fields): [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<T, any, any, never>

- Inherited from RunQueryBuilder.groupBy

  #### Parameters

  * ##### fields: EntityKeyOrString\<T> | readonly<!-- --> EntityKeyOrString\<T>\[]

  #### Returns [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<T, any, any, never>

### [**](#hasFlag)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L765)inheritedhasFlag

* ****hasFlag**(flag): boolean

- Inherited from RunQueryBuilder.hasFlag

  #### Parameters

  * ##### flag: [QueryFlag](https://mikro-orm.io/api/core/enum/QueryFlag.md)

  #### Returns boolean

### [**](#having)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L624)inheritedhaving

* ****having**(cond, params, operator): [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<T, any, any, never>

- Inherited from RunQueryBuilder.having

  #### Parameters

  * ##### cond: string | [QBFilterQuery](https://mikro-orm.io/api/core.md#QBFilterQuery) = <!-- -->{}
  * ##### optionalparams: any\[]
  * ##### optionaloperator: $and | $or

  #### Returns [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<T, any, any, never>

### [**](#hintComment)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L798)inheritedhintComment

* ****hintComment**(comment): this

- Inherited from RunQueryBuilder.hintComment

  Add hints to the query using comment-like syntax `/*+ ... *&#8205;/`. MySQL and Oracle use this syntax for optimizer hints. Also various DB proxies and routers use this syntax to pass hints to alter their behavior. In other dialects the hints are ignored as simple comments.

  ***

  #### Parameters

  * ##### comment: string | string\[]

  #### Returns this

### [**](#ignore)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L667)inheritedignore

* ****ignore**(): this

- Inherited from RunQueryBuilder.ignore

  #### Returns this

### [**](#indexHint)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L778)inheritedindexHint

* ****indexHint**(sql): this

- Inherited from RunQueryBuilder.indexHint

  Adds index hint to the FROM clause.

  ***

  #### Parameters

  * ##### sql: string

  #### Returns this

### [**](#innerJoin)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L311)inheritedinnerJoin

* ****innerJoin**\<Field, Alias>(field, alias, cond, schema): [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<T, any, any, { \[ K in string ]: AddToContext\<GetType\<T, object, Field>, object, Field, Alias, false>\[K] }>

- Inherited from RunQueryBuilder.innerJoin

  #### Parameters

  * ##### field: QueryBuilder\<any, any> | [QueryBuilder](https://mikro-orm.io/api/knex/class/QueryBuilder.md)\<any, never, never, never> | Field
  * ##### alias: Alias
  * ##### cond: [QBFilterQuery](https://mikro-orm.io/api/core.md#QBFilterQuery) = <!-- -->{}
  * ##### optionalschema: string

  #### Returns [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<T, any, any, { \[ K in string ]: AddToContext\<GetType\<T, object, Field>, object, Field, Alias, false>\[K] }>

### [**](#innerJoinAndSelect)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L401)inheritedinnerJoinAndSelect

* ****innerJoinAndSelect**\<Field, Alias>(field, alias, cond, fields, schema): [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<T, any, any, { \[ K in string ]: AddToContext\<GetType\<T, object, Field>, object, Field, Alias, true>\[K] }>

- Inherited from RunQueryBuilder.innerJoinAndSelect

  #### Parameters

  * ##### field: Field | \[field: Field, qb: QueryBuilder\<any, any> | [QueryBuilder](https://mikro-orm.io/api/knex/class/QueryBuilder.md)\<any, never, never, never>]
  * ##### alias: Alias
  * ##### cond: [QBFilterQuery](https://mikro-orm.io/api/core.md#QBFilterQuery) = <!-- -->{}
  * ##### optionalfields: string\[]
  * ##### optionalschema: string

  #### Returns [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<T, any, any, { \[ K in string ]: AddToContext\<GetType\<T, object, Field>, object, Field, Alias, true>\[K] }>

### [**](#innerJoinLateral)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L321)inheritedinnerJoinLateral

* ****innerJoinLateral**(field, alias, cond, schema): this

- Inherited from RunQueryBuilder.innerJoinLateral

  #### Parameters

  * ##### field: QueryBuilder\<any, any> | [QueryBuilder](https://mikro-orm.io/api/knex/class/QueryBuilder.md)\<any, never, never, never>
  * ##### alias: string
  * ##### cond: [QBFilterQuery](https://mikro-orm.io/api/core.md#QBFilterQuery) = <!-- -->{}
  * ##### optionalschema: string

  #### Returns this

### [**](#innerJoinLateralAndSelect)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L411)inheritedinnerJoinLateralAndSelect

* ****innerJoinLateralAndSelect**\<Field, Alias>(field, alias, cond, fields, schema): [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<T, any, any, { \[ K in string ]: AddToContext\<GetType\<T, object, Field>, object, Field, Alias, true>\[K] }>

- Inherited from RunQueryBuilder.innerJoinLateralAndSelect

  #### Parameters

  * ##### field: \[field: Field, qb: QueryBuilder\<any, any> | [QueryBuilder](https://mikro-orm.io/api/knex/class/QueryBuilder.md)\<any, never, never, never>]
  * ##### alias: Alias
  * ##### cond: [QBFilterQuery](https://mikro-orm.io/api/core.md#QBFilterQuery) = <!-- -->{}
  * ##### optionalfields: string\[]
  * ##### optionalschema: string

  #### Returns [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<T, any, any, { \[ K in string ]: AddToContext\<GetType\<T, object, Field>, object, Field, Alias, true>\[K] }>

### [**](#insert)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L267)inheritedinsert

* ****insert**(data): [InsertQueryBuilder](https://mikro-orm.io/api/knex/interface/InsertQueryBuilder.md)\<T>

- Inherited from RunQueryBuilder.insert

  #### Parameters

  * ##### data: [RequiredEntityData](https://mikro-orm.io/api/core.md#RequiredEntityData)\<T> | [RequiredEntityData](https://mikro-orm.io/api/core.md#RequiredEntityData)\<T>\[]

  #### Returns [InsertQueryBuilder](https://mikro-orm.io/api/knex/interface/InsertQueryBuilder.md)\<T>

### [**](#join)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L299)inheritedjoin

* ****join**\<Field, Alias>(field, alias, cond, type, path, schema): [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<T, any, any, { \[ K in string ]: AddToContext\<GetType\<T, object, Field>, object, Field, Alias, false>\[K] }>

- Inherited from RunQueryBuilder.join

  #### Parameters

  * ##### field: QueryBuilder\<any, any> | [QueryBuilder](https://mikro-orm.io/api/knex/class/QueryBuilder.md)\<any, never, never, never> | Field
  * ##### alias: Alias
  * ##### cond: [QBFilterQuery](https://mikro-orm.io/api/core.md#QBFilterQuery) = <!-- -->{}
  * ##### type: [JoinType](https://mikro-orm.io/api/knex/enum/JoinType.md) = <!-- -->JoinType.innerJoin
  * ##### optionalpath: string
  * ##### optionalschema: string

  #### Returns [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<T, any, any, { \[ K in string ]: AddToContext\<GetType\<T, object, Field>, object, Field, Alias, false>\[K] }>

### [**](#joinAndSelect)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L339)inheritedjoinAndSelect

* ****joinAndSelect**\<Field, Alias>(field, alias, cond, type, path, fields, schema): [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<T, any, any, { \[ K in string ]: AddToContext\<GetType\<T, object, Field>, object, Field, Alias, true>\[K] }>

- Inherited from RunQueryBuilder.joinAndSelect

  #### Parameters

  * ##### field: Field | \[field: Field, qb: QueryBuilder\<any, any> | [QueryBuilder](https://mikro-orm.io/api/knex/class/QueryBuilder.md)\<any, never, never, never>]
  * ##### alias: Alias
  * ##### cond: [QBFilterQuery](https://mikro-orm.io/api/core.md#QBFilterQuery) = <!-- -->{}
  * ##### type: [JoinType](https://mikro-orm.io/api/knex/enum/JoinType.md) = <!-- -->JoinType.innerJoin
  * ##### optionalpath: string
  * ##### optionalfields: string\[]
  * ##### optionalschema: string

  #### Returns [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<T, any, any, { \[ K in string ]: AddToContext\<GetType\<T, object, Field>, object, Field, Alias, true>\[K] }>

### [**](#leftJoin)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L326)inheritedleftJoin

* ****leftJoin**\<Field, Alias>(field, alias, cond, schema): [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<T, any, any, { \[ K in string ]: AddToContext\<GetType\<T, object, Field>, object, Field, Alias, false>\[K] }>

- Inherited from RunQueryBuilder.leftJoin

  #### Parameters

  * ##### field: QueryBuilder\<any, any> | [QueryBuilder](https://mikro-orm.io/api/knex/class/QueryBuilder.md)\<any, never, never, never> | Field
  * ##### alias: Alias
  * ##### cond: [QBFilterQuery](https://mikro-orm.io/api/core.md#QBFilterQuery) = <!-- -->{}
  * ##### optionalschema: string

  #### Returns [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<T, any, any, { \[ K in string ]: AddToContext\<GetType\<T, object, Field>, object, Field, Alias, false>\[K] }>

### [**](#leftJoinAndSelect)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L381)inheritedleftJoinAndSelect

* ****leftJoinAndSelect**\<Field, Alias>(field, alias, cond, fields, schema): [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<T, any, any, { \[ K in string ]: AddToContext\<GetType\<T, object, Field>, object, Field, Alias, true>\[K] }>

- Inherited from RunQueryBuilder.leftJoinAndSelect

  #### Parameters

  * ##### field: Field | \[field: Field, qb: QueryBuilder\<any, any> | [QueryBuilder](https://mikro-orm.io/api/knex/class/QueryBuilder.md)\<any, never, never, never>]
  * ##### alias: Alias
  * ##### cond: [QBFilterQuery](https://mikro-orm.io/api/core.md#QBFilterQuery) = <!-- -->{}
  * ##### optionalfields: string\[]
  * ##### optionalschema: string

  #### Returns [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<T, any, any, { \[ K in string ]: AddToContext\<GetType\<T, object, Field>, object, Field, Alias, true>\[K] }>

### [**](#leftJoinLateral)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L335)inheritedleftJoinLateral

* ****leftJoinLateral**(field, alias, cond, schema): this

- Inherited from RunQueryBuilder.leftJoinLateral

  #### Parameters

  * ##### field: QueryBuilder\<any, any> | [QueryBuilder](https://mikro-orm.io/api/knex/class/QueryBuilder.md)\<any, never, never, never>
  * ##### alias: string
  * ##### cond: [QBFilterQuery](https://mikro-orm.io/api/core.md#QBFilterQuery) = <!-- -->{}
  * ##### optionalschema: string

  #### Returns this

### [**](#leftJoinLateralAndSelect)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L391)inheritedleftJoinLateralAndSelect

* ****leftJoinLateralAndSelect**\<Field, Alias>(field, alias, cond, fields, schema): [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<T, any, any, { \[ K in string ]: AddToContext\<GetType\<T, object, Field>, object, Field, Alias, true>\[K] }>

- Inherited from RunQueryBuilder.leftJoinLateralAndSelect

  #### Parameters

  * ##### field: \[field: Field, qb: QueryBuilder\<any, any> | [QueryBuilder](https://mikro-orm.io/api/knex/class/QueryBuilder.md)\<any, never, never, never>]
  * ##### alias: Alias
  * ##### cond: [QBFilterQuery](https://mikro-orm.io/api/core.md#QBFilterQuery) = <!-- -->{}
  * ##### optionalfields: string\[]
  * ##### optionalschema: string

  #### Returns [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<T, any, any, { \[ K in string ]: AddToContext\<GetType\<T, object, Field>, object, Field, Alias, true>\[K] }>

### [**](#limit)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L710)inheritedlimit

* ****limit**(limit, offset): [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<T, any, any, never>

- Inherited from RunQueryBuilder.limit

  #### Parameters

  * ##### optionallimit: number
  * ##### offset: number = <!-- -->0

  #### Returns [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<T, any, any, never>

### [**](#merge)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L676)inheritedmerge

* ****merge**(data): this

- Inherited from RunQueryBuilder.merge

  #### Parameters

  * ##### optionaldata: [Field](https://mikro-orm.io/api/knex.md#Field)\<T>\[] | [EntityData](https://mikro-orm.io/api/core.md#EntityData)\<T>

  #### Returns this

### [**](#offset)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L721)inheritedoffset

* ****offset**(offset): [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<T, any, any, never>

- Inherited from RunQueryBuilder.offset

  #### Parameters

  * ##### optionaloffset: number

  #### Returns [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<T, any, any, never>

### [**](#onConflict)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L651)inheritedonConflict

* ****onConflict**(fields): [InsertQueryBuilder](https://mikro-orm.io/api/knex/interface/InsertQueryBuilder.md)\<T>

- Inherited from RunQueryBuilder.onConflict

  #### Parameters

  * ##### fields: [Field](https://mikro-orm.io/api/knex.md#Field)\<T> | [Field](https://mikro-orm.io/api/knex.md#Field)\<T>\[] = <!-- -->\[]

  #### Returns [InsertQueryBuilder](https://mikro-orm.io/api/knex/interface/InsertQueryBuilder.md)\<T>

### [**](#orderBy)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L597)inheritedorderBy

* ****orderBy**(orderBy): [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<T, any, any, never>

- Inherited from RunQueryBuilder.orderBy

  #### Parameters

  * ##### orderBy: [QBQueryOrderMap](https://mikro-orm.io/api/core.md#QBQueryOrderMap)\<T> | [QBQueryOrderMap](https://mikro-orm.io/api/core.md#QBQueryOrderMap)\<T>\[]

  #### Returns [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<T, any, any, never>

### [**](#orHaving)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L647)inheritedorHaving

* ****orHaving**(cond, params): [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<T, any, any, never>

- Inherited from RunQueryBuilder.orHaving

  #### Parameters

  * ##### optionalcond: string | [QBFilterQuery](https://mikro-orm.io/api/core.md#QBFilterQuery)
  * ##### optionalparams: any\[]

  #### Returns [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<T, any, any, never>

### [**](#orWhere)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L591)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L592)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L593)inheritedorWhere

* ****orWhere**(cond): this
* ****orWhere**(cond, params): this

- Inherited from RunQueryBuilder.orWhere

  #### Parameters

  * ##### cond: [QBFilterQuery](https://mikro-orm.io/api/core.md#QBFilterQuery)\<T>

  #### Returns this

### [**](#returning)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L689)inheritedreturning

* ****returning**(fields): this

- Inherited from RunQueryBuilder.returning

  #### Parameters

  * ##### optionalfields: [Field](https://mikro-orm.io/api/knex.md#Field)\<T> | [Field](https://mikro-orm.io/api/knex.md#Field)\<T>\[]

  #### Returns this

### [**](#select)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L234)inheritedselect

* ****select**(fields, distinct): [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<T, any, any, never>

- Inherited from RunQueryBuilder.select

  #### Parameters

  * ##### fields: [Field](https://mikro-orm.io/api/knex.md#Field)\<T> | [Field](https://mikro-orm.io/api/knex.md#Field)\<T>\[]
  * ##### distinct: boolean = <!-- -->false

  #### Returns [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<T, any, any, never>

### [**](#setFlag)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L753)inheritedsetFlag

* ****setFlag**(flag): this

- Inherited from RunQueryBuilder.setFlag

  #### Parameters

  * ##### flag: [QueryFlag](https://mikro-orm.io/api/core/enum/QueryFlag.md)

  #### Returns this

### [**](#setFlushMode)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L747)inheritedsetFlushMode

* ****setFlushMode**(flushMode): this

- Inherited from RunQueryBuilder.setFlushMode

  #### Parameters

  * ##### optionalflushMode: [FlushMode](https://mikro-orm.io/api/core/enum/FlushMode.md)

  #### Returns this

### [**](#setLockMode)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L734)inheritedsetLockMode

* ****setLockMode**(mode, tables): this

- Inherited from RunQueryBuilder.setLockMode

  #### Parameters

  * ##### optionalmode: [LockMode](https://mikro-orm.io/api/core/enum/LockMode.md)
  * ##### optionaltables: string\[]

  #### Returns this

### [**](#setLoggerContext)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L1250)inheritedsetLoggerContext

* ****setLoggerContext**(context): void

- Inherited from RunQueryBuilder.setLoggerContext

  Sets logger context for this query builder.

  ***

  #### Parameters

  * ##### context: [LoggingOptions](https://mikro-orm.io/api/core.md#LoggingOptions) & [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)

  #### Returns void

### [**](#then)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L2015)inheritedthen

* ****then**\<TResult1, TResult2>(onfulfilled, onrejected): Promise<[QueryResult](https://mikro-orm.io/api/core/interface/QueryResult.md)\<T>>

- Inherited from RunQueryBuilder.then

  Provides promise-like interface so we can await the QB instance.

  ***

  #### Parameters

  * ##### optionalonfulfilled: null | (value) => TResult1 | PromiseLike\<TResult1>
  *
    ##### optionalonrejected: null | (reason) => TResult2 | PromiseLike\<TResult2>


  #### Returns Promise<[QueryResult](https://mikro-orm.io/api/core/interface/QueryResult.md)\<T>>

### [**](#toQuery)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L886)inheritedtoQuery

* ****toQuery**(): { \_sql: Sql; params: readonly
  <!-- -->
  unknown\[]; sql: string }

- Inherited from RunQueryBuilder.toQuery

  #### Returns { \_sql: Sql; params: readonly<!-- --> unknown\[]; sql: string }

  * ##### \_sql: Sql
  * ##### params: readonly<!-- --> unknown\[]
  * ##### sql: string

### [**](#truncate)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L279)inheritedtruncate

* ****truncate**(): [TruncateQueryBuilder](https://mikro-orm.io/api/knex/interface/TruncateQueryBuilder.md)\<T>

- Inherited from RunQueryBuilder.truncate

  #### Returns [TruncateQueryBuilder](https://mikro-orm.io/api/knex/interface/TruncateQueryBuilder.md)\<T>

### [**](#unsetFlag)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L759)inheritedunsetFlag

* ****unsetFlag**(flag): this

- Inherited from RunQueryBuilder.unsetFlag

  #### Parameters

  * ##### flag: [QueryFlag](https://mikro-orm.io/api/core/enum/QueryFlag.md)

  #### Returns this

### [**](#update)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L271)inheritedupdate

* ****update**(data): [UpdateQueryBuilder](https://mikro-orm.io/api/knex/interface/UpdateQueryBuilder.md)\<T>

- Inherited from RunQueryBuilder.update

  #### Parameters

  * ##### data: [EntityData](https://mikro-orm.io/api/core.md#EntityData)\<T>

  #### Returns [UpdateQueryBuilder](https://mikro-orm.io/api/knex/interface/UpdateQueryBuilder.md)\<T>

### [**](#where)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L2013)inheritedwhere

* ****where**(cond, params, operator): this

- Inherited from RunQueryBuilder.where

  #### Parameters

  * ##### cond: string | [QBFilterQuery](https://mikro-orm.io/api/core.md#QBFilterQuery)\<T>
  * ##### optionalparams: any\[] | $and | $or
  * ##### optionaloperator: $and | $or

  #### Returns this

### [**](#withSchema)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L727)inheritedwithSchema

* ****withSchema**(schema): this

- Inherited from RunQueryBuilder.withSchema

  #### Parameters

  * ##### optionalschema: string

  #### Returns this

### [**](#withSubQuery)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L526)inheritedwithSubQuery

* ****withSubQuery**(subQuery, alias): this

- Inherited from RunQueryBuilder.withSubQuery

  #### Parameters

  * ##### subQuery: QueryBuilder\<any, any>
  * ##### alias: string

  #### Returns this
