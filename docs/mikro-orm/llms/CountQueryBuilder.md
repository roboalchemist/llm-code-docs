# Source: https://mikro-orm.io/api/knex/interface/CountQueryBuilder.md

# CountQueryBuilder<!-- --> \<Entity>

SQL query builder with fluent interface.

```
const qb = orm.em.createQueryBuilder(Publisher);
qb.select('*')
  .where({
    name: 'test 123',
    type: PublisherType.GLOBAL,
  })
  .orderBy({
    name: QueryOrder.DESC,
    type: QueryOrder.ASC,
  })
  .limit(2, 1);

const publisher = await qb.getSingleResult();
```

### Hierarchy

* [QueryBuilder](https://mikro-orm.io/api/knex/class/QueryBuilder.md)\<Entity, any, any>
  * *CountQueryBuilder*

## Index[**](#Index)

### Accessors

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
* [**getResult](#getResult)
* [**getResultAndCount](#getResultAndCount)
* [**getResultList](#getResultList)
* [**getSingleResult](#getSingleResult)
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

## Accessors<!-- -->[**](#Accessors)

### [**](#alias)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L150)inheritedalias

* **get alias(): string

- Inherited from QueryBuilder.alias

  #### Returns string

### [**](#helper)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L154)inheritedhelper

* **get helper(): QueryBuilderHelper

- Inherited from QueryBuilder.helper

  #### Returns QueryBuilderHelper

### [**](#mainAlias)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L145)inheritedmainAlias

* **get mainAlias(): [Alias](https://mikro-orm.io/api/knex/interface/Alias.md)\<Entity>

- Inherited from QueryBuilder.mainAlias

  #### Returns [Alias](https://mikro-orm.io/api/knex/interface/Alias.md)\<Entity>

## Methods<!-- -->[**](#Methods)

### [**](#addSelect)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L245)inheritedaddSelect

* ****addSelect**(fields): [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<Entity, any, any, never>

- Inherited from QueryBuilder.addSelect

  #### Parameters

  * ##### fields: [Field](https://mikro-orm.io/api/knex.md#Field)\<Entity> | [Field](https://mikro-orm.io/api/knex.md#Field)\<Entity>\[]

  #### Returns [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<Entity, any, any, never>

### [**](#andHaving)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L643)inheritedandHaving

* ****andHaving**(cond, params): [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<Entity, any, any, never>

- Inherited from QueryBuilder.andHaving

  #### Parameters

  * ##### optionalcond: string | [QBFilterQuery](https://mikro-orm.io/api/core.md#QBFilterQuery)
  * ##### optionalparams: any\[]

  #### Returns [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<Entity, any, any, never>

### [**](#andWhere)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L585)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L586)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L587)inheritedandWhere

* ****andWhere**(cond): this
* ****andWhere**(cond, params): this

- Inherited from QueryBuilder.andWhere

  #### Parameters

  * ##### cond: [QBFilterQuery](https://mikro-orm.io/api/core.md#QBFilterQuery)\<Entity>

  #### Returns this

### [**](#applyFilters)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L475)inheritedapplyFilters

* ****applyFilters**(filterOptions): Promise\<void>

- Inherited from QueryBuilder.applyFilters

  Apply filters to the QB where condition.

  ***

  #### Parameters

  * ##### filterOptions: [FilterOptions](https://mikro-orm.io/api/core.md#FilterOptions) = <!-- -->{}

  #### Returns Promise\<void>

### [**](#as)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L1161)inheritedas

* ****as**(alias): QueryBuilder\<any, any>

- Inherited from QueryBuilder.as

  Returns knex instance with sub-query aliased with given alias. You can provide `EntityName.propName` as alias, then the field name will be used based on the metadata

  ***

  #### Parameters

  * ##### alias: string

  #### Returns QueryBuilder\<any, any>

### [**](#cache)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L769)inheritedcache

* ****cache**(config): this

- Inherited from QueryBuilder.cache

  #### Parameters

  * ##### config: number | boolean | \[string, number] = <!-- -->true

  #### Returns this

### [**](#clone)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L1179)inheritedclone

* ****clone**(reset): [QueryBuilder](https://mikro-orm.io/api/knex/class/QueryBuilder.md)\<Entity, never, never, never>

- Inherited from QueryBuilder.clone

  #### Parameters

  * ##### optionalreset: boolean | string\[]

  #### Returns [QueryBuilder](https://mikro-orm.io/api/knex/class/QueryBuilder.md)\<Entity, never, never, never>

### [**](#comment)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L787)inheritedcomment

* ****comment**(comment): this

- Inherited from QueryBuilder.comment

  Prepend comment to the sql query using the syntax `/* ... *&#8205;/`. Some characters are forbidden such as `/*, *&#8205;/` and `?`.

  ***

  #### Parameters

  * ##### comment: string | string\[]

  #### Returns this

### [**](#count)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L283)inheritedcount

* ****count**(field, distinct): [CountQueryBuilder](https://mikro-orm.io/api/knex/interface/CountQueryBuilder.md)\<Entity>

- Inherited from QueryBuilder.count

  #### Parameters

  * ##### optionalfield: EntityKeyOrString\<Entity> | EntityKeyOrString\<Entity>\[]
  * ##### distinct: boolean = <!-- -->false

  #### Returns [CountQueryBuilder](https://mikro-orm.io/api/knex/interface/CountQueryBuilder.md)\<Entity>

### [**](#delete)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L275)inheriteddelete

* ****delete**(cond): [DeleteQueryBuilder](https://mikro-orm.io/api/knex/interface/DeleteQueryBuilder.md)\<Entity>

- Inherited from QueryBuilder.delete

  #### Parameters

  * ##### optionalcond: [QBFilterQuery](https://mikro-orm.io/api/core.md#QBFilterQuery)

  #### Returns [DeleteQueryBuilder](https://mikro-orm.io/api/knex/interface/DeleteQueryBuilder.md)\<Entity>

### [**](#distinct)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L255)inheriteddistinct

* ****distinct**(): [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<Entity, any, any, never>

- Inherited from QueryBuilder.distinct

  #### Returns [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<Entity, any, any, never>

### [**](#distinctOn)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L261)inheriteddistinctOn

* ****distinctOn**(fields): [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<Entity, any, any, never>

- Inherited from QueryBuilder.distinctOn

  postgres only

  ***

  #### Parameters

  * ##### fields: EntityKeyOrString\<Entity> | EntityKeyOrString\<Entity>\[]

  #### Returns [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<Entity, any, any, never>

### [**](#execute)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L2032)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L2033)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L2034)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L2035)execute

* ****execute**\<Result>(method, mapResults): Promise\<Result>
* ****execute**\<Result>(method, mapResults): Promise\<Result>
* ****execute**\<Result>(method, mapResults): Promise\<Result>
* ****execute**\<Result>(method, mapResults): Promise\<Result>

- Overrides QueryBuilder.execute

  Executes this QB and returns the raw results, mapped to the property names (unless disabled via last parameter). Use `method` to specify what kind of result you want to get (array/single/meta).

  ***

  #### Parameters

  * ##### optionalmethod: get | all | run
  * ##### optionalmapResults: boolean

  #### Returns Promise\<Result>

### [**](#from)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L808)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L809)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L810)inheritedfrom

* ****from**\<Entity>(target, aliasName): [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<Entity, any, any, never>
* ****from**\<Entity>(target): [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<Entity, any, any, never>

- Inherited from QueryBuilder.from

  Specifies FROM which entity's table select/update/delete will be executed, removing all previously set FROM-s. Allows setting a main string alias of the selection data.

  ***

  #### Parameters

  * ##### target: [QueryBuilder](https://mikro-orm.io/api/knex/class/QueryBuilder.md)\<Entity, never, never, never>
  * ##### optionalaliasName: string

  #### Returns [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<Entity, any, any, never>

### [**](#getCount)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L1109)inheritedgetCount

* ****getCount**(field, distinct): Promise\<number>

- Inherited from QueryBuilder.getCount

  Executes count query (without offset and limit), returning total count of results

  ***

  #### Parameters

  * ##### optionalfield: EntityKeyOrString\<Entity> | EntityKeyOrString\<Entity>\[]
  * ##### optionaldistinct: boolean

  #### Returns Promise\<number>

### [**](#getFormattedQuery)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L911)inheritedgetFormattedQuery

* ****getFormattedQuery**(): string

- Inherited from QueryBuilder.getFormattedQuery

  Returns raw interpolated query string with all the parameters inlined.

  ***

  #### Returns string

### [**](#getKnex)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L1219)inheritedgetKnex

* ****getKnex**(processVirtualEntity): QueryBuilder\<any, any>

- Inherited from QueryBuilder.getKnex

  #### Parameters

  * ##### processVirtualEntity: boolean = <!-- -->true

  #### Returns QueryBuilder\<any, any>

### [**](#getKnexQuery)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L828)inheritedgetKnexQuery

* ****getKnexQuery**(processVirtualEntity): QueryBuilder\<any, any>

- Inherited from QueryBuilder.getKnexQuery

  #### Parameters

  * ##### processVirtualEntity: boolean = <!-- -->true

  #### Returns QueryBuilder\<any, any>

### [**](#getLoggerContext)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L1257)inheritedgetLoggerContext

* ****getLoggerContext**\<T>(): T

- Inherited from QueryBuilder.getLoggerContext

  Gets logger context for this query builder.

  ***

  #### Returns T

### [**](#getParams)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L904)inheritedgetParams

* ****getParams**(): readonly
  <!-- -->
  Value\[]

- Inherited from QueryBuilder.getParams

  Returns the list of all parameters for this query.

  ***

  #### Returns readonly<!-- --> Value\[]

### [**](#getQuery)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L882)inheritedgetQuery

* ****getQuery**(): string

- Inherited from QueryBuilder.getQuery

  Returns the query with parameters as wildcards.

  ***

  #### Returns string

### [**](#getResult)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L1054)inheritedgetResult

* ****getResult**(): Promise<[Loaded](https://mikro-orm.io/api/core.md#Loaded)\<Entity, any>\[]>

- Inherited from QueryBuilder.getResult

  Alias for `qb.getResultList()`

  ***

  #### Returns Promise<[Loaded](https://mikro-orm.io/api/core.md#Loaded)\<Entity, any>\[]>

### [**](#getResultAndCount)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L1127)inheritedgetResultAndCount

* ****getResultAndCount**(): Promise<\[Entity\[], number]>

- Inherited from QueryBuilder.getResultAndCount

  Executes the query, returning both array of results and total count query (without offset and limit).

  ***

  #### Returns Promise<\[Entity\[], number]>

### [**](#getResultList)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L1061)inheritedgetResultList

* ****getResultList**(limit): Promise<[Loaded](https://mikro-orm.io/api/core.md#Loaded)\<Entity, any>\[]>

- Inherited from QueryBuilder.getResultList

  Executes the query, returning array of results

  ***

  #### Parameters

  * ##### optionallimit: number

  #### Returns Promise<[Loaded](https://mikro-orm.io/api/core.md#Loaded)\<Entity, any>\[]>

### [**](#getSingleResult)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L1097)inheritedgetSingleResult

* ****getSingleResult**(): Promise\<null | Entity>

- Inherited from QueryBuilder.getSingleResult

  Executes the query, returning the first result or null

  ***

  #### Returns Promise\<null | Entity>

### [**](#groupBy)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L617)inheritedgroupBy

* ****groupBy**(fields): [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<Entity, any, any, never>

- Inherited from QueryBuilder.groupBy

  #### Parameters

  * ##### fields: EntityKeyOrString\<Entity> | readonly<!-- --> EntityKeyOrString\<Entity>\[]

  #### Returns [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<Entity, any, any, never>

### [**](#hasFlag)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L765)inheritedhasFlag

* ****hasFlag**(flag): boolean

- Inherited from QueryBuilder.hasFlag

  #### Parameters

  * ##### flag: [QueryFlag](https://mikro-orm.io/api/core/enum/QueryFlag.md)

  #### Returns boolean

### [**](#having)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L624)inheritedhaving

* ****having**(cond, params, operator): [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<Entity, any, any, never>

- Inherited from QueryBuilder.having

  #### Parameters

  * ##### cond: string | [QBFilterQuery](https://mikro-orm.io/api/core.md#QBFilterQuery) = <!-- -->{}
  * ##### optionalparams: any\[]
  * ##### optionaloperator: $and | $or

  #### Returns [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<Entity, any, any, never>

### [**](#hintComment)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L798)inheritedhintComment

* ****hintComment**(comment): this

- Inherited from QueryBuilder.hintComment

  Add hints to the query using comment-like syntax `/*+ ... *&#8205;/`. MySQL and Oracle use this syntax for optimizer hints. Also various DB proxies and routers use this syntax to pass hints to alter their behavior. In other dialects the hints are ignored as simple comments.

  ***

  #### Parameters

  * ##### comment: string | string\[]

  #### Returns this

### [**](#ignore)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L667)inheritedignore

* ****ignore**(): this

- Inherited from QueryBuilder.ignore

  #### Returns this

### [**](#indexHint)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L778)inheritedindexHint

* ****indexHint**(sql): this

- Inherited from QueryBuilder.indexHint

  Adds index hint to the FROM clause.

  ***

  #### Parameters

  * ##### sql: string

  #### Returns this

### [**](#innerJoin)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L311)inheritedinnerJoin

* ****innerJoin**\<Field, Alias>(field, alias, cond, schema): [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<Entity, any, any, { \[ K in string ]: AddToContext\<GetType\<Entity, object, Field>, object, Field, Alias, false>\[K] }>

- Inherited from QueryBuilder.innerJoin

  #### Parameters

  * ##### field: QueryBuilder\<any, any> | [QueryBuilder](https://mikro-orm.io/api/knex/class/QueryBuilder.md)\<any, never, never, never> | Field
  * ##### alias: Alias
  * ##### cond: [QBFilterQuery](https://mikro-orm.io/api/core.md#QBFilterQuery) = <!-- -->{}
  * ##### optionalschema: string

  #### Returns [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<Entity, any, any, { \[ K in string ]: AddToContext\<GetType\<Entity, object, Field>, object, Field, Alias, false>\[K] }>

### [**](#innerJoinAndSelect)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L401)inheritedinnerJoinAndSelect

* ****innerJoinAndSelect**\<Field, Alias>(field, alias, cond, fields, schema): [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<Entity, any, any, { \[ K in string ]: AddToContext\<GetType\<Entity, object, Field>, object, Field, Alias, true>\[K] }>

- Inherited from QueryBuilder.innerJoinAndSelect

  #### Parameters

  * ##### field: Field | \[field: Field, qb: QueryBuilder\<any, any> | [QueryBuilder](https://mikro-orm.io/api/knex/class/QueryBuilder.md)\<any, never, never, never>]
  * ##### alias: Alias
  * ##### cond: [QBFilterQuery](https://mikro-orm.io/api/core.md#QBFilterQuery) = <!-- -->{}
  * ##### optionalfields: string\[]
  * ##### optionalschema: string

  #### Returns [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<Entity, any, any, { \[ K in string ]: AddToContext\<GetType\<Entity, object, Field>, object, Field, Alias, true>\[K] }>

### [**](#innerJoinLateral)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L321)inheritedinnerJoinLateral

* ****innerJoinLateral**(field, alias, cond, schema): this

- Inherited from QueryBuilder.innerJoinLateral

  #### Parameters

  * ##### field: QueryBuilder\<any, any> | [QueryBuilder](https://mikro-orm.io/api/knex/class/QueryBuilder.md)\<any, never, never, never>
  * ##### alias: string
  * ##### cond: [QBFilterQuery](https://mikro-orm.io/api/core.md#QBFilterQuery) = <!-- -->{}
  * ##### optionalschema: string

  #### Returns this

### [**](#innerJoinLateralAndSelect)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L411)inheritedinnerJoinLateralAndSelect

* ****innerJoinLateralAndSelect**\<Field, Alias>(field, alias, cond, fields, schema): [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<Entity, any, any, { \[ K in string ]: AddToContext\<GetType\<Entity, object, Field>, object, Field, Alias, true>\[K] }>

- Inherited from QueryBuilder.innerJoinLateralAndSelect

  #### Parameters

  * ##### field: \[field: Field, qb: QueryBuilder\<any, any> | [QueryBuilder](https://mikro-orm.io/api/knex/class/QueryBuilder.md)\<any, never, never, never>]
  * ##### alias: Alias
  * ##### cond: [QBFilterQuery](https://mikro-orm.io/api/core.md#QBFilterQuery) = <!-- -->{}
  * ##### optionalfields: string\[]
  * ##### optionalschema: string

  #### Returns [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<Entity, any, any, { \[ K in string ]: AddToContext\<GetType\<Entity, object, Field>, object, Field, Alias, true>\[K] }>

### [**](#insert)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L267)inheritedinsert

* ****insert**(data): [InsertQueryBuilder](https://mikro-orm.io/api/knex/interface/InsertQueryBuilder.md)\<Entity>

- Inherited from QueryBuilder.insert

  #### Parameters

  * ##### data: [RequiredEntityData](https://mikro-orm.io/api/core.md#RequiredEntityData)\<Entity> | [RequiredEntityData](https://mikro-orm.io/api/core.md#RequiredEntityData)\<Entity>\[]

  #### Returns [InsertQueryBuilder](https://mikro-orm.io/api/knex/interface/InsertQueryBuilder.md)\<Entity>

### [**](#join)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L299)inheritedjoin

* ****join**\<Field, Alias>(field, alias, cond, type, path, schema): [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<Entity, any, any, { \[ K in string ]: AddToContext\<GetType\<Entity, object, Field>, object, Field, Alias, false>\[K] }>

- Inherited from QueryBuilder.join

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

- Inherited from QueryBuilder.joinAndSelect

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

- Inherited from QueryBuilder.leftJoin

  #### Parameters

  * ##### field: QueryBuilder\<any, any> | [QueryBuilder](https://mikro-orm.io/api/knex/class/QueryBuilder.md)\<any, never, never, never> | Field
  * ##### alias: Alias
  * ##### cond: [QBFilterQuery](https://mikro-orm.io/api/core.md#QBFilterQuery) = <!-- -->{}
  * ##### optionalschema: string

  #### Returns [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<Entity, any, any, { \[ K in string ]: AddToContext\<GetType\<Entity, object, Field>, object, Field, Alias, false>\[K] }>

### [**](#leftJoinAndSelect)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L381)inheritedleftJoinAndSelect

* ****leftJoinAndSelect**\<Field, Alias>(field, alias, cond, fields, schema): [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<Entity, any, any, { \[ K in string ]: AddToContext\<GetType\<Entity, object, Field>, object, Field, Alias, true>\[K] }>

- Inherited from QueryBuilder.leftJoinAndSelect

  #### Parameters

  * ##### field: Field | \[field: Field, qb: QueryBuilder\<any, any> | [QueryBuilder](https://mikro-orm.io/api/knex/class/QueryBuilder.md)\<any, never, never, never>]
  * ##### alias: Alias
  * ##### cond: [QBFilterQuery](https://mikro-orm.io/api/core.md#QBFilterQuery) = <!-- -->{}
  * ##### optionalfields: string\[]
  * ##### optionalschema: string

  #### Returns [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<Entity, any, any, { \[ K in string ]: AddToContext\<GetType\<Entity, object, Field>, object, Field, Alias, true>\[K] }>

### [**](#leftJoinLateral)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L335)inheritedleftJoinLateral

* ****leftJoinLateral**(field, alias, cond, schema): this

- Inherited from QueryBuilder.leftJoinLateral

  #### Parameters

  * ##### field: QueryBuilder\<any, any> | [QueryBuilder](https://mikro-orm.io/api/knex/class/QueryBuilder.md)\<any, never, never, never>
  * ##### alias: string
  * ##### cond: [QBFilterQuery](https://mikro-orm.io/api/core.md#QBFilterQuery) = <!-- -->{}
  * ##### optionalschema: string

  #### Returns this

### [**](#leftJoinLateralAndSelect)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L391)inheritedleftJoinLateralAndSelect

* ****leftJoinLateralAndSelect**\<Field, Alias>(field, alias, cond, fields, schema): [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<Entity, any, any, { \[ K in string ]: AddToContext\<GetType\<Entity, object, Field>, object, Field, Alias, true>\[K] }>

- Inherited from QueryBuilder.leftJoinLateralAndSelect

  #### Parameters

  * ##### field: \[field: Field, qb: QueryBuilder\<any, any> | [QueryBuilder](https://mikro-orm.io/api/knex/class/QueryBuilder.md)\<any, never, never, never>]
  * ##### alias: Alias
  * ##### cond: [QBFilterQuery](https://mikro-orm.io/api/core.md#QBFilterQuery) = <!-- -->{}
  * ##### optionalfields: string\[]
  * ##### optionalschema: string

  #### Returns [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<Entity, any, any, { \[ K in string ]: AddToContext\<GetType\<Entity, object, Field>, object, Field, Alias, true>\[K] }>

### [**](#limit)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L710)inheritedlimit

* ****limit**(limit, offset): [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<Entity, any, any, never>

- Inherited from QueryBuilder.limit

  #### Parameters

  * ##### optionallimit: number
  * ##### offset: number = <!-- -->0

  #### Returns [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<Entity, any, any, never>

### [**](#merge)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L676)inheritedmerge

* ****merge**(data): this

- Inherited from QueryBuilder.merge

  #### Parameters

  * ##### optionaldata: [Field](https://mikro-orm.io/api/knex.md#Field)\<Entity>\[] | [EntityData](https://mikro-orm.io/api/core.md#EntityData)\<Entity>

  #### Returns this

### [**](#offset)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L721)inheritedoffset

* ****offset**(offset): [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<Entity, any, any, never>

- Inherited from QueryBuilder.offset

  #### Parameters

  * ##### optionaloffset: number

  #### Returns [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<Entity, any, any, never>

### [**](#onConflict)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L651)inheritedonConflict

* ****onConflict**(fields): [InsertQueryBuilder](https://mikro-orm.io/api/knex/interface/InsertQueryBuilder.md)\<Entity>

- Inherited from QueryBuilder.onConflict

  #### Parameters

  * ##### fields: [Field](https://mikro-orm.io/api/knex.md#Field)\<Entity> | [Field](https://mikro-orm.io/api/knex.md#Field)\<Entity>\[] = <!-- -->\[]

  #### Returns [InsertQueryBuilder](https://mikro-orm.io/api/knex/interface/InsertQueryBuilder.md)\<Entity>

### [**](#orderBy)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L597)inheritedorderBy

* ****orderBy**(orderBy): [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<Entity, any, any, never>

- Inherited from QueryBuilder.orderBy

  #### Parameters

  * ##### orderBy: [QBQueryOrderMap](https://mikro-orm.io/api/core.md#QBQueryOrderMap)\<Entity> | [QBQueryOrderMap](https://mikro-orm.io/api/core.md#QBQueryOrderMap)\<Entity>\[]

  #### Returns [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<Entity, any, any, never>

### [**](#orHaving)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L647)inheritedorHaving

* ****orHaving**(cond, params): [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<Entity, any, any, never>

- Inherited from QueryBuilder.orHaving

  #### Parameters

  * ##### optionalcond: string | [QBFilterQuery](https://mikro-orm.io/api/core.md#QBFilterQuery)
  * ##### optionalparams: any\[]

  #### Returns [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<Entity, any, any, never>

### [**](#orWhere)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L591)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L592)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L593)inheritedorWhere

* ****orWhere**(cond): this
* ****orWhere**(cond, params): this

- Inherited from QueryBuilder.orWhere

  #### Parameters

  * ##### cond: [QBFilterQuery](https://mikro-orm.io/api/core.md#QBFilterQuery)\<Entity>

  #### Returns this

### [**](#returning)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L689)inheritedreturning

* ****returning**(fields): this

- Inherited from QueryBuilder.returning

  #### Parameters

  * ##### optionalfields: [Field](https://mikro-orm.io/api/knex.md#Field)\<Entity> | [Field](https://mikro-orm.io/api/knex.md#Field)\<Entity>\[]

  #### Returns this

### [**](#select)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L234)inheritedselect

* ****select**(fields, distinct): [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<Entity, any, any, never>

- Inherited from QueryBuilder.select

  #### Parameters

  * ##### fields: [Field](https://mikro-orm.io/api/knex.md#Field)\<Entity> | [Field](https://mikro-orm.io/api/knex.md#Field)\<Entity>\[]
  * ##### distinct: boolean = <!-- -->false

  #### Returns [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<Entity, any, any, never>

### [**](#setFlag)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L753)inheritedsetFlag

* ****setFlag**(flag): this

- Inherited from QueryBuilder.setFlag

  #### Parameters

  * ##### flag: [QueryFlag](https://mikro-orm.io/api/core/enum/QueryFlag.md)

  #### Returns this

### [**](#setFlushMode)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L747)inheritedsetFlushMode

* ****setFlushMode**(flushMode): this

- Inherited from QueryBuilder.setFlushMode

  #### Parameters

  * ##### optionalflushMode: [FlushMode](https://mikro-orm.io/api/core/enum/FlushMode.md)

  #### Returns this

### [**](#setLockMode)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L734)inheritedsetLockMode

* ****setLockMode**(mode, tables): this

- Inherited from QueryBuilder.setLockMode

  #### Parameters

  * ##### optionalmode: [LockMode](https://mikro-orm.io/api/core/enum/LockMode.md)
  * ##### optionaltables: string\[]

  #### Returns this

### [**](#setLoggerContext)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L1250)inheritedsetLoggerContext

* ****setLoggerContext**(context): void

- Inherited from QueryBuilder.setLoggerContext

  Sets logger context for this query builder.

  ***

  #### Parameters

  * ##### context: [LoggingOptions](https://mikro-orm.io/api/core.md#LoggingOptions) & [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)

  #### Returns void

### [**](#then)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L2036)then

* ****then**\<TResult1, TResult2>(onfulfilled, onrejected): Promise\<number>

- Overrides QueryBuilder.then

  Provides promise-like interface so we can await the QB instance.

  ***

  #### Parameters

  * ##### optionalonfulfilled: null | (value) => TResult1 | PromiseLike\<TResult1>
  *
    ##### optionalonrejected: null | (reason) => TResult2 | PromiseLike\<TResult2>


  #### Returns Promise\<number>

### [**](#toQuery)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L886)inheritedtoQuery

* ****toQuery**(): { \_sql: Sql; params: readonly
  <!-- -->
  unknown\[]; sql: string }

- Inherited from QueryBuilder.toQuery

  #### Returns { \_sql: Sql; params: readonly<!-- --> unknown\[]; sql: string }

  * ##### \_sql: Sql
  * ##### params: readonly<!-- --> unknown\[]
  * ##### sql: string

### [**](#truncate)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L279)inheritedtruncate

* ****truncate**(): [TruncateQueryBuilder](https://mikro-orm.io/api/knex/interface/TruncateQueryBuilder.md)\<Entity>

- Inherited from QueryBuilder.truncate

  #### Returns [TruncateQueryBuilder](https://mikro-orm.io/api/knex/interface/TruncateQueryBuilder.md)\<Entity>

### [**](#unsetFlag)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L759)inheritedunsetFlag

* ****unsetFlag**(flag): this

- Inherited from QueryBuilder.unsetFlag

  #### Parameters

  * ##### flag: [QueryFlag](https://mikro-orm.io/api/core/enum/QueryFlag.md)

  #### Returns this

### [**](#update)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L271)inheritedupdate

* ****update**(data): [UpdateQueryBuilder](https://mikro-orm.io/api/knex/interface/UpdateQueryBuilder.md)\<Entity>

- Inherited from QueryBuilder.update

  #### Parameters

  * ##### data: [EntityData](https://mikro-orm.io/api/core.md#EntityData)\<Entity>

  #### Returns [UpdateQueryBuilder](https://mikro-orm.io/api/knex/interface/UpdateQueryBuilder.md)\<Entity>

### [**](#where)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L532)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L533)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L534)inheritedwhere

* ****where**(cond, operator): this
* ****where**(cond, params, operator): this

- Inherited from QueryBuilder.where

  #### Parameters

  * ##### cond: [QBFilterQuery](https://mikro-orm.io/api/core.md#QBFilterQuery)\<Entity>
  * ##### optionaloperator: $and | $or

  #### Returns this

### [**](#withSchema)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L727)inheritedwithSchema

* ****withSchema**(schema): this

- Inherited from QueryBuilder.withSchema

  #### Parameters

  * ##### optionalschema: string

  #### Returns this

### [**](#withSubQuery)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L526)inheritedwithSubQuery

* ****withSubQuery**(subQuery, alias): this

- Inherited from QueryBuilder.withSubQuery

  #### Parameters

  * ##### subQuery: QueryBuilder\<any, any>
  * ##### alias: string

  #### Returns this
