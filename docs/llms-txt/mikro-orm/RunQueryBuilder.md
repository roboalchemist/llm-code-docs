# Source: https://mikro-orm.io/api/knex/interface/RunQueryBuilder.md

# RunQueryBuilder<!-- --> \<Entity>

### Hierarchy

* Omit<[QueryBuilder](https://mikro-orm.io/api/knex/class/QueryBuilder.md)\<Entity, any, any>, getResult | getSingleResult | getResultList | where>

  * *RunQueryBuilder*

    * [InsertQueryBuilder](https://mikro-orm.io/api/knex/interface/InsertQueryBuilder.md)
    * [UpdateQueryBuilder](https://mikro-orm.io/api/knex/interface/UpdateQueryBuilder.md)
    * [DeleteQueryBuilder](https://mikro-orm.io/api/knex/interface/DeleteQueryBuilder.md)
    * [TruncateQueryBuilder](https://mikro-orm.io/api/knex/interface/TruncateQueryBuilder.md)

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

Inherited from Omit.alias

### [**](#helper)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L154)inheritedhelper

**helper: QueryBuilderHelper

Inherited from Omit.helper

### [**](#mainAlias)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L145)inheritedmainAlias

**mainAlias: [Alias](https://mikro-orm.io/api/knex/interface/Alias.md)\<Entity>

Inherited from Omit.mainAlias

## Methods<!-- -->[**](#Methods)

### [**](#addSelect)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L245)inheritedaddSelect

* ****addSelect**(fields): [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<Entity, any, any, never>

- Inherited from Omit.addSelect

  #### Parameters

  * ##### fields: [Field](https://mikro-orm.io/api/knex.md#Field)\<Entity> | [Field](https://mikro-orm.io/api/knex.md#Field)\<Entity>\[]

  #### Returns [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<Entity, any, any, never>

### [**](#andHaving)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L643)inheritedandHaving

* ****andHaving**(cond, params): [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<Entity, any, any, never>

- Inherited from Omit.andHaving

  #### Parameters

  * ##### optionalcond: string | [QBFilterQuery](https://mikro-orm.io/api/core.md#QBFilterQuery)
  * ##### optionalparams: any\[]

  #### Returns [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<Entity, any, any, never>

### [**](#andWhere)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L585)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L586)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L587)inheritedandWhere

* ****andWhere**(cond): this
* ****andWhere**(cond, params): this

- Inherited from Omit.andWhere

  #### Parameters

  * ##### cond: [QBFilterQuery](https://mikro-orm.io/api/core.md#QBFilterQuery)\<Entity>

  #### Returns this

### [**](#applyFilters)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L475)inheritedapplyFilters

* ****applyFilters**(filterOptions): Promise\<void>

- Inherited from Omit.applyFilters

  Apply filters to the QB where condition.

  ***

  #### Parameters

  * ##### filterOptions: [FilterOptions](https://mikro-orm.io/api/core.md#FilterOptions) = <!-- -->{}

  #### Returns Promise\<void>

### [**](#as)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L1161)inheritedas

* ****as**(alias): QueryBuilder\<any, any>

- Inherited from Omit.as

  Returns knex instance with sub-query aliased with given alias. You can provide `EntityName.propName` as alias, then the field name will be used based on the metadata

  ***

  #### Parameters

  * ##### alias: string

  #### Returns QueryBuilder\<any, any>

### [**](#cache)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L769)inheritedcache

* ****cache**(config): this

- Inherited from Omit.cache

  #### Parameters

  * ##### config: number | boolean | \[string, number] = <!-- -->true

  #### Returns this

### [**](#clone)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L1179)inheritedclone

* ****clone**(reset): [QueryBuilder](https://mikro-orm.io/api/knex/class/QueryBuilder.md)\<Entity, never, never, never>

- Inherited from Omit.clone

  #### Parameters

  * ##### optionalreset: boolean | string\[]

  #### Returns [QueryBuilder](https://mikro-orm.io/api/knex/class/QueryBuilder.md)\<Entity, never, never, never>

### [**](#comment)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L787)inheritedcomment

* ****comment**(comment): this

- Inherited from Omit.comment

  Prepend comment to the sql query using the syntax `/* ... *&#8205;/`. Some characters are forbidden such as `/*, *&#8205;/` and `?`.

  ***

  #### Parameters

  * ##### comment: string | string\[]

  #### Returns this

### [**](#count)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L283)inheritedcount

* ****count**(field, distinct): [CountQueryBuilder](https://mikro-orm.io/api/knex/interface/CountQueryBuilder.md)\<Entity>

- Inherited from Omit.count

  #### Parameters

  * ##### optionalfield: EntityKeyOrString\<Entity> | EntityKeyOrString\<Entity>\[]
  * ##### distinct: boolean = <!-- -->false

  #### Returns [CountQueryBuilder](https://mikro-orm.io/api/knex/interface/CountQueryBuilder.md)\<Entity>

### [**](#delete)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L275)inheriteddelete

* ****delete**(cond): [DeleteQueryBuilder](https://mikro-orm.io/api/knex/interface/DeleteQueryBuilder.md)\<Entity>

- Inherited from Omit.delete

  #### Parameters

  * ##### optionalcond: [QBFilterQuery](https://mikro-orm.io/api/core.md#QBFilterQuery)

  #### Returns [DeleteQueryBuilder](https://mikro-orm.io/api/knex/interface/DeleteQueryBuilder.md)\<Entity>

### [**](#distinct)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L255)inheriteddistinct

* ****distinct**(): [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<Entity, any, any, never>

- Inherited from Omit.distinct

  #### Returns [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<Entity, any, any, never>

### [**](#distinctOn)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L261)inheriteddistinctOn

* ****distinctOn**(fields): [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<Entity, any, any, never>

- Inherited from Omit.distinctOn

  postgres only

  ***

  #### Parameters

  * ##### fields: EntityKeyOrString\<Entity> | EntityKeyOrString\<Entity>\[]

  #### Returns [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<Entity, any, any, never>

### [**](#execute)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L2014)execute

* ****execute**\<Result>(method, mapResults): Promise\<Result>

- Overrides Omit.execute

  Executes this QB and returns the raw results, mapped to the property names (unless disabled via last parameter). Use `method` to specify what kind of result you want to get (array/single/meta).

  ***

  #### Parameters

  * ##### optionalmethod: get | all | run
  * ##### optionalmapResults: boolean

  #### Returns Promise\<Result>

### [**](#from)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L808)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L809)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L810)inheritedfrom

* ****from**\<Entity>(target, aliasName): [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<Entity, any, any, never>
* ****from**\<Entity>(target): [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<Entity, any, any, never>

- Inherited from Omit.from

  Specifies FROM which entity's table select/update/delete will be executed, removing all previously set FROM-s. Allows setting a main string alias of the selection data.

  ***

  #### Parameters

  * ##### target: [QueryBuilder](https://mikro-orm.io/api/knex/class/QueryBuilder.md)\<Entity, never, never, never>
  * ##### optionalaliasName: string

  #### Returns [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<Entity, any, any, never>

### [**](#getCount)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L1109)inheritedgetCount

* ****getCount**(field, distinct): Promise\<number>

- Inherited from Omit.getCount

  Executes count query (without offset and limit), returning total count of results

  ***

  #### Parameters

  * ##### optionalfield: EntityKeyOrString\<Entity> | EntityKeyOrString\<Entity>\[]
  * ##### optionaldistinct: boolean

  #### Returns Promise\<number>

### [**](#getFormattedQuery)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L911)inheritedgetFormattedQuery

* ****getFormattedQuery**(): string

- Inherited from Omit.getFormattedQuery

  Returns raw interpolated query string with all the parameters inlined.

  ***

  #### Returns string

### [**](#getKnex)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L1219)inheritedgetKnex

* ****getKnex**(processVirtualEntity): QueryBuilder\<any, any>

- Inherited from Omit.getKnex

  #### Parameters

  * ##### processVirtualEntity: boolean = <!-- -->true

  #### Returns QueryBuilder\<any, any>

### [**](#getKnexQuery)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L828)inheritedgetKnexQuery

* ****getKnexQuery**(processVirtualEntity): QueryBuilder\<any, any>

- Inherited from Omit.getKnexQuery

  #### Parameters

  * ##### processVirtualEntity: boolean = <!-- -->true

  #### Returns QueryBuilder\<any, any>

### [**](#getLoggerContext)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L1257)inheritedgetLoggerContext

* ****getLoggerContext**\<T>(): T

- Inherited from Omit.getLoggerContext

  Gets logger context for this query builder.

  ***

  #### Returns T

### [**](#getParams)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L904)inheritedgetParams

* ****getParams**(): readonly
  <!-- -->
  Value\[]

- Inherited from Omit.getParams

  Returns the list of all parameters for this query.

  ***

  #### Returns readonly<!-- --> Value\[]

### [**](#getQuery)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L882)inheritedgetQuery

* ****getQuery**(): string

- Inherited from Omit.getQuery

  Returns the query with parameters as wildcards.

  ***

  #### Returns string

### [**](#getResultAndCount)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L1127)inheritedgetResultAndCount

* ****getResultAndCount**(): Promise<\[Entity\[], number]>

- Inherited from Omit.getResultAndCount

  Executes the query, returning both array of results and total count query (without offset and limit).

  ***

  #### Returns Promise<\[Entity\[], number]>

### [**](#groupBy)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L617)inheritedgroupBy

* ****groupBy**(fields): [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<Entity, any, any, never>

- Inherited from Omit.groupBy

  #### Parameters

  * ##### fields: EntityKeyOrString\<Entity> | readonly<!-- --> EntityKeyOrString\<Entity>\[]

  #### Returns [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<Entity, any, any, never>

### [**](#hasFlag)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L765)inheritedhasFlag

* ****hasFlag**(flag): boolean

- Inherited from Omit.hasFlag

  #### Parameters

  * ##### flag: [QueryFlag](https://mikro-orm.io/api/core/enum/QueryFlag.md)

  #### Returns boolean

### [**](#having)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L624)inheritedhaving

* ****having**(cond, params, operator): [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<Entity, any, any, never>

- Inherited from Omit.having

  #### Parameters

  * ##### cond: string | [QBFilterQuery](https://mikro-orm.io/api/core.md#QBFilterQuery) = <!-- -->{}
  * ##### optionalparams: any\[]
  * ##### optionaloperator: $and | $or

  #### Returns [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<Entity, any, any, never>

### [**](#hintComment)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L798)inheritedhintComment

* ****hintComment**(comment): this

- Inherited from Omit.hintComment

  Add hints to the query using comment-like syntax `/*+ ... *&#8205;/`. MySQL and Oracle use this syntax for optimizer hints. Also various DB proxies and routers use this syntax to pass hints to alter their behavior. In other dialects the hints are ignored as simple comments.

  ***

  #### Parameters

  * ##### comment: string | string\[]

  #### Returns this

### [**](#ignore)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L667)inheritedignore

* ****ignore**(): this

- Inherited from Omit.ignore

  #### Returns this

### [**](#indexHint)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L778)inheritedindexHint

* ****indexHint**(sql): this

- Inherited from Omit.indexHint

  Adds index hint to the FROM clause.

  ***

  #### Parameters

  * ##### sql: string

  #### Returns this

### [**](#innerJoin)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L311)inheritedinnerJoin

* ****innerJoin**\<Field, Alias>(field, alias, cond, schema): [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<Entity, any, any, { \[ K in string ]: AddToContext\<GetType\<Entity, object, Field>, object, Field, Alias, false>\[K] }>

- Inherited from Omit.innerJoin

  #### Parameters

  * ##### field: QueryBuilder\<any, any> | [QueryBuilder](https://mikro-orm.io/api/knex/class/QueryBuilder.md)\<any, never, never, never> | Field
  * ##### alias: Alias
  * ##### cond: [QBFilterQuery](https://mikro-orm.io/api/core.md#QBFilterQuery) = <!-- -->{}
  * ##### optionalschema: string

  #### Returns [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<Entity, any, any, { \[ K in string ]: AddToContext\<GetType\<Entity, object, Field>, object, Field, Alias, false>\[K] }>

### [**](#innerJoinAndSelect)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L401)inheritedinnerJoinAndSelect

* ****innerJoinAndSelect**\<Field, Alias>(field, alias, cond, fields, schema): [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<Entity, any, any, { \[ K in string ]: AddToContext\<GetType\<Entity, object, Field>, object, Field, Alias, true>\[K] }>

- Inherited from Omit.innerJoinAndSelect

  #### Parameters

  * ##### field: Field | \[field: Field, qb: QueryBuilder\<any, any> | [QueryBuilder](https://mikro-orm.io/api/knex/class/QueryBuilder.md)\<any, never, never, never>]
  * ##### alias: Alias
  * ##### cond: [QBFilterQuery](https://mikro-orm.io/api/core.md#QBFilterQuery) = <!-- -->{}
  * ##### optionalfields: string\[]
  * ##### optionalschema: string

  #### Returns [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<Entity, any, any, { \[ K in string ]: AddToContext\<GetType\<Entity, object, Field>, object, Field, Alias, true>\[K] }>

### [**](#innerJoinLateral)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L321)inheritedinnerJoinLateral

* ****innerJoinLateral**(field, alias, cond, schema): this

- Inherited from Omit.innerJoinLateral

  #### Parameters

  * ##### field: QueryBuilder\<any, any> | [QueryBuilder](https://mikro-orm.io/api/knex/class/QueryBuilder.md)\<any, never, never, never>
  * ##### alias: string
  * ##### cond: [QBFilterQuery](https://mikro-orm.io/api/core.md#QBFilterQuery) = <!-- -->{}
  * ##### optionalschema: string

  #### Returns this

### [**](#innerJoinLateralAndSelect)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L411)inheritedinnerJoinLateralAndSelect

* ****innerJoinLateralAndSelect**\<Field, Alias>(field, alias, cond, fields, schema): [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<Entity, any, any, { \[ K in string ]: AddToContext\<GetType\<Entity, object, Field>, object, Field, Alias, true>\[K] }>

- Inherited from Omit.innerJoinLateralAndSelect

  #### Parameters

  * ##### field: \[field: Field, qb: QueryBuilder\<any, any> | [QueryBuilder](https://mikro-orm.io/api/knex/class/QueryBuilder.md)\<any, never, never, never>]
  * ##### alias: Alias
  * ##### cond: [QBFilterQuery](https://mikro-orm.io/api/core.md#QBFilterQuery) = <!-- -->{}
  * ##### optionalfields: string\[]
  * ##### optionalschema: string

  #### Returns [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<Entity, any, any, { \[ K in string ]: AddToContext\<GetType\<Entity, object, Field>, object, Field, Alias, true>\[K] }>

### [**](#insert)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L267)inheritedinsert

* ****insert**(data): [InsertQueryBuilder](https://mikro-orm.io/api/knex/interface/InsertQueryBuilder.md)\<Entity>

- Inherited from Omit.insert

  #### Parameters

  * ##### data: [RequiredEntityData](https://mikro-orm.io/api/core.md#RequiredEntityData)\<Entity> | [RequiredEntityData](https://mikro-orm.io/api/core.md#RequiredEntityData)\<Entity>\[]

  #### Returns [InsertQueryBuilder](https://mikro-orm.io/api/knex/interface/InsertQueryBuilder.md)\<Entity>

### [**](#join)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L299)inheritedjoin

* ****join**\<Field, Alias>(field, alias, cond, type, path, schema): [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<Entity, any, any, { \[ K in string ]: AddToContext\<GetType\<Entity, object, Field>, object, Field, Alias, false>\[K] }>

- Inherited from Omit.join

  #### Parameters

  * ##### field: QueryBuilder\<any, any> | [QueryBuilder](https://mikro-orm.io/api/knex/class/QueryBuilder.md)\<any, never, never, never> | Field
  * ##### alias: Alias
  * ##### cond: [QBFilterQuery](https://mikro-orm.io/api/core.md#QBFilterQuery) = <!-- -->{}
  * ##### type: [JoinType](https://mikro-orm.io/api/knex/enum/JoinType.md) = <!-- -->JoinType.innerJoin
  * ##### optionalpath: string
  * ##### optionalschema: string

  #### Returns [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<Entity, any, any, { \[ K in string ]: AddToContext\<GetType\<Entity, object, Field>, object, Field, Alias, false>\[K] }>

### [**](#joinAndSelect)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L339)inheritedjoinAndSelect

* ****joinAndSelect**\<Field, Alias>(field, alias, cond, type, path, fields, schema): [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<Entity, any, any, { \[ K in string ]: AddToContext\<GetType\<Entity, object, Field>, object, Field, Alias, true>\[K] }>

- Inherited from Omit.joinAndSelect

  #### Parameters

  * ##### field: Field | \[field: Field, qb: QueryBuilder\<any, any> | [QueryBuilder](https://mikro-orm.io/api/knex/class/QueryBuilder.md)\<any, never, never, never>]
  * ##### alias: Alias
  * ##### cond: [QBFilterQuery](https://mikro-orm.io/api/core.md#QBFilterQuery) = <!-- -->{}
  * ##### type: [JoinType](https://mikro-orm.io/api/knex/enum/JoinType.md) = <!-- -->JoinType.innerJoin
  * ##### optionalpath: string
  * ##### optionalfields: string\[]
  * ##### optionalschema: string

  #### Returns [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<Entity, any, any, { \[ K in string ]: AddToContext\<GetType\<Entity, object, Field>, object, Field, Alias, true>\[K] }>

### [**](#leftJoin)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L326)inheritedleftJoin

* ****leftJoin**\<Field, Alias>(field, alias, cond, schema): [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<Entity, any, any, { \[ K in string ]: AddToContext\<GetType\<Entity, object, Field>, object, Field, Alias, false>\[K] }>

- Inherited from Omit.leftJoin

  #### Parameters

  * ##### field: QueryBuilder\<any, any> | [QueryBuilder](https://mikro-orm.io/api/knex/class/QueryBuilder.md)\<any, never, never, never> | Field
  * ##### alias: Alias
  * ##### cond: [QBFilterQuery](https://mikro-orm.io/api/core.md#QBFilterQuery) = <!-- -->{}
  * ##### optionalschema: string

  #### Returns [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<Entity, any, any, { \[ K in string ]: AddToContext\<GetType\<Entity, object, Field>, object, Field, Alias, false>\[K] }>

### [**](#leftJoinAndSelect)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L381)inheritedleftJoinAndSelect

* ****leftJoinAndSelect**\<Field, Alias>(field, alias, cond, fields, schema): [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<Entity, any, any, { \[ K in string ]: AddToContext\<GetType\<Entity, object, Field>, object, Field, Alias, true>\[K] }>

- Inherited from Omit.leftJoinAndSelect

  #### Parameters

  * ##### field: Field | \[field: Field, qb: QueryBuilder\<any, any> | [QueryBuilder](https://mikro-orm.io/api/knex/class/QueryBuilder.md)\<any, never, never, never>]
  * ##### alias: Alias
  * ##### cond: [QBFilterQuery](https://mikro-orm.io/api/core.md#QBFilterQuery) = <!-- -->{}
  * ##### optionalfields: string\[]
  * ##### optionalschema: string

  #### Returns [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<Entity, any, any, { \[ K in string ]: AddToContext\<GetType\<Entity, object, Field>, object, Field, Alias, true>\[K] }>

### [**](#leftJoinLateral)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L335)inheritedleftJoinLateral

* ****leftJoinLateral**(field, alias, cond, schema): this

- Inherited from Omit.leftJoinLateral

  #### Parameters

  * ##### field: QueryBuilder\<any, any> | [QueryBuilder](https://mikro-orm.io/api/knex/class/QueryBuilder.md)\<any, never, never, never>
  * ##### alias: string
  * ##### cond: [QBFilterQuery](https://mikro-orm.io/api/core.md#QBFilterQuery) = <!-- -->{}
  * ##### optionalschema: string

  #### Returns this

### [**](#leftJoinLateralAndSelect)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L391)inheritedleftJoinLateralAndSelect

* ****leftJoinLateralAndSelect**\<Field, Alias>(field, alias, cond, fields, schema): [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<Entity, any, any, { \[ K in string ]: AddToContext\<GetType\<Entity, object, Field>, object, Field, Alias, true>\[K] }>

- Inherited from Omit.leftJoinLateralAndSelect

  #### Parameters

  * ##### field: \[field: Field, qb: QueryBuilder\<any, any> | [QueryBuilder](https://mikro-orm.io/api/knex/class/QueryBuilder.md)\<any, never, never, never>]
  * ##### alias: Alias
  * ##### cond: [QBFilterQuery](https://mikro-orm.io/api/core.md#QBFilterQuery) = <!-- -->{}
  * ##### optionalfields: string\[]
  * ##### optionalschema: string

  #### Returns [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<Entity, any, any, { \[ K in string ]: AddToContext\<GetType\<Entity, object, Field>, object, Field, Alias, true>\[K] }>

### [**](#limit)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L710)inheritedlimit

* ****limit**(limit, offset): [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<Entity, any, any, never>

- Inherited from Omit.limit

  #### Parameters

  * ##### optionallimit: number
  * ##### offset: number = <!-- -->0

  #### Returns [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<Entity, any, any, never>

### [**](#merge)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L676)inheritedmerge

* ****merge**(data): this

- Inherited from Omit.merge

  #### Parameters

  * ##### optionaldata: [Field](https://mikro-orm.io/api/knex.md#Field)\<Entity>\[] | [EntityData](https://mikro-orm.io/api/core.md#EntityData)\<Entity>

  #### Returns this

### [**](#offset)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L721)inheritedoffset

* ****offset**(offset): [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<Entity, any, any, never>

- Inherited from Omit.offset

  #### Parameters

  * ##### optionaloffset: number

  #### Returns [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<Entity, any, any, never>

### [**](#onConflict)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L651)inheritedonConflict

* ****onConflict**(fields): [InsertQueryBuilder](https://mikro-orm.io/api/knex/interface/InsertQueryBuilder.md)\<Entity>

- Inherited from Omit.onConflict

  #### Parameters

  * ##### fields: [Field](https://mikro-orm.io/api/knex.md#Field)\<Entity> | [Field](https://mikro-orm.io/api/knex.md#Field)\<Entity>\[] = <!-- -->\[]

  #### Returns [InsertQueryBuilder](https://mikro-orm.io/api/knex/interface/InsertQueryBuilder.md)\<Entity>

### [**](#orderBy)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L597)inheritedorderBy

* ****orderBy**(orderBy): [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<Entity, any, any, never>

- Inherited from Omit.orderBy

  #### Parameters

  * ##### orderBy: [QBQueryOrderMap](https://mikro-orm.io/api/core.md#QBQueryOrderMap)\<Entity> | [QBQueryOrderMap](https://mikro-orm.io/api/core.md#QBQueryOrderMap)\<Entity>\[]

  #### Returns [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<Entity, any, any, never>

### [**](#orHaving)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L647)inheritedorHaving

* ****orHaving**(cond, params): [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<Entity, any, any, never>

- Inherited from Omit.orHaving

  #### Parameters

  * ##### optionalcond: string | [QBFilterQuery](https://mikro-orm.io/api/core.md#QBFilterQuery)
  * ##### optionalparams: any\[]

  #### Returns [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<Entity, any, any, never>

### [**](#orWhere)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L591)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L592)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L593)inheritedorWhere

* ****orWhere**(cond): this
* ****orWhere**(cond, params): this

- Inherited from Omit.orWhere

  #### Parameters

  * ##### cond: [QBFilterQuery](https://mikro-orm.io/api/core.md#QBFilterQuery)\<Entity>

  #### Returns this

### [**](#returning)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L689)inheritedreturning

* ****returning**(fields): this

- Inherited from Omit.returning

  #### Parameters

  * ##### optionalfields: [Field](https://mikro-orm.io/api/knex.md#Field)\<Entity> | [Field](https://mikro-orm.io/api/knex.md#Field)\<Entity>\[]

  #### Returns this

### [**](#select)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L234)inheritedselect

* ****select**(fields, distinct): [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<Entity, any, any, never>

- Inherited from Omit.select

  #### Parameters

  * ##### fields: [Field](https://mikro-orm.io/api/knex.md#Field)\<Entity> | [Field](https://mikro-orm.io/api/knex.md#Field)\<Entity>\[]
  * ##### distinct: boolean = <!-- -->false

  #### Returns [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<Entity, any, any, never>

### [**](#setFlag)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L753)inheritedsetFlag

* ****setFlag**(flag): this

- Inherited from Omit.setFlag

  #### Parameters

  * ##### flag: [QueryFlag](https://mikro-orm.io/api/core/enum/QueryFlag.md)

  #### Returns this

### [**](#setFlushMode)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L747)inheritedsetFlushMode

* ****setFlushMode**(flushMode): this

- Inherited from Omit.setFlushMode

  #### Parameters

  * ##### optionalflushMode: [FlushMode](https://mikro-orm.io/api/core/enum/FlushMode.md)

  #### Returns this

### [**](#setLockMode)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L734)inheritedsetLockMode

* ****setLockMode**(mode, tables): this

- Inherited from Omit.setLockMode

  #### Parameters

  * ##### optionalmode: [LockMode](https://mikro-orm.io/api/core/enum/LockMode.md)
  * ##### optionaltables: string\[]

  #### Returns this

### [**](#setLoggerContext)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L1250)inheritedsetLoggerContext

* ****setLoggerContext**(context): void

- Inherited from Omit.setLoggerContext

  Sets logger context for this query builder.

  ***

  #### Parameters

  * ##### context: [LoggingOptions](https://mikro-orm.io/api/core.md#LoggingOptions) & [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)

  #### Returns void

### [**](#then)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L2015)then

* ****then**\<TResult1, TResult2>(onfulfilled, onrejected): Promise<[QueryResult](https://mikro-orm.io/api/core/interface/QueryResult.md)\<Entity>>

- Overrides Omit.then

  Provides promise-like interface so we can await the QB instance.

  ***

  #### Parameters

  * ##### optionalonfulfilled: null | (value) => TResult1 | PromiseLike\<TResult1>
  *
    ##### optionalonrejected: null | (reason) => TResult2 | PromiseLike\<TResult2>


  #### Returns Promise<[QueryResult](https://mikro-orm.io/api/core/interface/QueryResult.md)\<Entity>>

### [**](#toQuery)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L886)inheritedtoQuery

* ****toQuery**(): { \_sql: Sql; params: readonly
  <!-- -->
  unknown\[]; sql: string }

- Inherited from Omit.toQuery

  #### Returns { \_sql: Sql; params: readonly<!-- --> unknown\[]; sql: string }

  * ##### \_sql: Sql
  * ##### params: readonly<!-- --> unknown\[]
  * ##### sql: string

### [**](#truncate)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L279)inheritedtruncate

* ****truncate**(): [TruncateQueryBuilder](https://mikro-orm.io/api/knex/interface/TruncateQueryBuilder.md)\<Entity>

- Inherited from Omit.truncate

  #### Returns [TruncateQueryBuilder](https://mikro-orm.io/api/knex/interface/TruncateQueryBuilder.md)\<Entity>

### [**](#unsetFlag)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L759)inheritedunsetFlag

* ****unsetFlag**(flag): this

- Inherited from Omit.unsetFlag

  #### Parameters

  * ##### flag: [QueryFlag](https://mikro-orm.io/api/core/enum/QueryFlag.md)

  #### Returns this

### [**](#update)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L271)inheritedupdate

* ****update**(data): [UpdateQueryBuilder](https://mikro-orm.io/api/knex/interface/UpdateQueryBuilder.md)\<Entity>

- Inherited from Omit.update

  #### Parameters

  * ##### data: [EntityData](https://mikro-orm.io/api/core.md#EntityData)\<Entity>

  #### Returns [UpdateQueryBuilder](https://mikro-orm.io/api/knex/interface/UpdateQueryBuilder.md)\<Entity>

### [**](#where)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L2013)where

* ****where**(cond, params, operator): this

- #### Parameters

  * ##### cond: string | [QBFilterQuery](https://mikro-orm.io/api/core.md#QBFilterQuery)\<Entity>
  * ##### optionalparams: any\[] | $and | $or
  * ##### optionaloperator: $and | $or

  #### Returns this

### [**](#withSchema)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L727)inheritedwithSchema

* ****withSchema**(schema): this

- Inherited from Omit.withSchema

  #### Parameters

  * ##### optionalschema: string

  #### Returns this

### [**](#withSubQuery)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L526)inheritedwithSubQuery

* ****withSubQuery**(subQuery, alias): this

- Inherited from Omit.withSubQuery

  #### Parameters

  * ##### subQuery: QueryBuilder\<any, any>
  * ##### alias: string

  #### Returns this
