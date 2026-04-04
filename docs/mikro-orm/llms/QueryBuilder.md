# Source: https://mikro-orm.io/api/knex/class/QueryBuilder.md

# QueryBuilder<!-- --> \<Entity, RootAlias, Hint, Context>

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

* *QueryBuilder*

  * [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)
  * [CountQueryBuilder](https://mikro-orm.io/api/knex/interface/CountQueryBuilder.md)

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

### [**](#alias)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L150)alias

* **get alias(): string

- #### Returns string

### [**](#helper)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L154)helper

* **get helper(): QueryBuilderHelper

- #### Returns QueryBuilderHelper

### [**](#mainAlias)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L145)mainAlias

* **get mainAlias(): [Alias](https://mikro-orm.io/api/knex/interface/Alias.md)\<Entity>

- #### Returns [Alias](https://mikro-orm.io/api/knex/interface/Alias.md)\<Entity>

## Methods<!-- -->[**](#Methods)

### [**](#addSelect)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L245)addSelect

* ****addSelect**(fields): [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<Entity, RootAlias, Hint, Context>

- #### Parameters

  * ##### fields: [Field](https://mikro-orm.io/api/knex.md#Field)\<Entity> | [Field](https://mikro-orm.io/api/knex.md#Field)\<Entity>\[]

  #### Returns [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<Entity, RootAlias, Hint, Context>

### [**](#andHaving)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L643)andHaving

* ****andHaving**(cond, params): [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<Entity, RootAlias, Hint, Context>

- #### Parameters

  * ##### optionalcond: string | [QBFilterQuery](https://mikro-orm.io/api/core.md#QBFilterQuery)
  * ##### optionalparams: any\[]

  #### Returns [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<Entity, RootAlias, Hint, Context>

### [**](#andWhere)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L585)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L586)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L587)andWhere

* ****andWhere**(cond): this
* ****andWhere**(cond, params): this

- #### Parameters

  * ##### cond: [QBFilterQuery](https://mikro-orm.io/api/core.md#QBFilterQuery)\<Entity>

  #### Returns this

### [**](#applyFilters)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L475)applyFilters

* ****applyFilters**(filterOptions): Promise\<void>

- Apply filters to the QB where condition.

  ***

  #### Parameters

  * ##### filterOptions: [FilterOptions](https://mikro-orm.io/api/core.md#FilterOptions) = <!-- -->{}

  #### Returns Promise\<void>

### [**](#as)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L1161)as

* ****as**(alias): QueryBuilder\<any, any>

- Returns knex instance with sub-query aliased with given alias. You can provide `EntityName.propName` as alias, then the field name will be used based on the metadata

  ***

  #### Parameters

  * ##### alias: string

  #### Returns QueryBuilder\<any, any>

### [**](#cache)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L769)cache

* ****cache**(config): this

- #### Parameters

  * ##### config: number | boolean | \[string, number] = <!-- -->true

  #### Returns this

### [**](#clone)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L1179)clone

* ****clone**(reset): [QueryBuilder](https://mikro-orm.io/api/knex/class/QueryBuilder.md)\<Entity, never, never, never>

- #### Parameters

  * ##### optionalreset: boolean | string\[]

  #### Returns [QueryBuilder](https://mikro-orm.io/api/knex/class/QueryBuilder.md)\<Entity, never, never, never>

### [**](#comment)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L787)comment

* ****comment**(comment): this

- Prepend comment to the sql query using the syntax `/* ... *&#8205;/`. Some characters are forbidden such as `/*, *&#8205;/` and `?`.

  ***

  #### Parameters

  * ##### comment: string | string\[]

  #### Returns this

### [**](#count)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L283)count

* ****count**(field, distinct): [CountQueryBuilder](https://mikro-orm.io/api/knex/interface/CountQueryBuilder.md)\<Entity>

- #### Parameters

  * ##### optionalfield: EntityKeyOrString\<Entity> | EntityKeyOrString\<Entity>\[]
  * ##### distinct: boolean = <!-- -->false

  #### Returns [CountQueryBuilder](https://mikro-orm.io/api/knex/interface/CountQueryBuilder.md)\<Entity>

### [**](#delete)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L275)delete

* ****delete**(cond): [DeleteQueryBuilder](https://mikro-orm.io/api/knex/interface/DeleteQueryBuilder.md)\<Entity>

- #### Parameters

  * ##### optionalcond: [QBFilterQuery](https://mikro-orm.io/api/core.md#QBFilterQuery)

  #### Returns [DeleteQueryBuilder](https://mikro-orm.io/api/knex/interface/DeleteQueryBuilder.md)\<Entity>

### [**](#distinct)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L255)distinct

* ****distinct**(): [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<Entity, RootAlias, Hint, Context>

- #### Returns [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<Entity, RootAlias, Hint, Context>

### [**](#distinctOn)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L261)distinctOn

* ****distinctOn**(fields): [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<Entity, RootAlias, Hint, Context>

- postgres only

  ***

  #### Parameters

  * ##### fields: EntityKeyOrString\<Entity> | EntityKeyOrString\<Entity>\[]

  #### Returns [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<Entity, RootAlias, Hint, Context>

### [**](#execute)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L990)execute

* ****execute**\<U>(method, options): Promise\<U>

- Executes this QB and returns the raw results, mapped to the property names (unless disabled via last parameter). Use `method` to specify what kind of result you want to get (array/single/meta).

  ***

  #### Parameters

  * ##### optionalmethod: get | all | run
  * ##### optionaloptions: boolean | [ExecuteOptions](https://mikro-orm.io/api/knex/interface/ExecuteOptions.md)

  #### Returns Promise\<U>

### [**](#from)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L808)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L809)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L810)from

* ****from**\<Entity>(target, aliasName): [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<Entity, RootAlias, Hint, Context>
* ****from**\<Entity>(target): [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<Entity, RootAlias, Hint, Context>

- Specifies FROM which entity's table select/update/delete will be executed, removing all previously set FROM-s. Allows setting a main string alias of the selection data.

  ***

  #### Parameters

  * ##### target: [QueryBuilder](https://mikro-orm.io/api/knex/class/QueryBuilder.md)\<Entity, never, never, never>
  * ##### optionalaliasName: string

  #### Returns [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<Entity, RootAlias, Hint, Context>

### [**](#getCount)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L1109)getCount

* ****getCount**(field, distinct): Promise\<number>

- Executes count query (without offset and limit), returning total count of results

  ***

  #### Parameters

  * ##### optionalfield: EntityKeyOrString\<Entity> | EntityKeyOrString\<Entity>\[]
  * ##### optionaldistinct: boolean

  #### Returns Promise\<number>

### [**](#getFormattedQuery)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L911)getFormattedQuery

* ****getFormattedQuery**(): string

- Returns raw interpolated query string with all the parameters inlined.

  ***

  #### Returns string

### [**](#getKnex)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L1219)getKnex

* ****getKnex**(processVirtualEntity): QueryBuilder\<any, any>

- #### Parameters

  * ##### processVirtualEntity: boolean = <!-- -->true

  #### Returns QueryBuilder\<any, any>

### [**](#getKnexQuery)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L828)getKnexQuery

* ****getKnexQuery**(processVirtualEntity): QueryBuilder\<any, any>

- #### Parameters

  * ##### processVirtualEntity: boolean = <!-- -->true

  #### Returns QueryBuilder\<any, any>

### [**](#getLoggerContext)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L1257)getLoggerContext

* ****getLoggerContext**\<T>(): T

- Gets logger context for this query builder.

  ***

  #### Returns T

### [**](#getParams)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L904)getParams

* ****getParams**(): readonly
  <!-- -->
  Value\[]

- Returns the list of all parameters for this query.

  ***

  #### Returns readonly<!-- --> Value\[]

### [**](#getQuery)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L882)getQuery

* ****getQuery**(): string

- Returns the query with parameters as wildcards.

  ***

  #### Returns string

### [**](#getResult)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L1054)getResult

* ****getResult**(): Promise<[Loaded](https://mikro-orm.io/api/core.md#Loaded)\<Entity, Hint>\[]>

- Alias for `qb.getResultList()`

  ***

  #### Returns Promise<[Loaded](https://mikro-orm.io/api/core.md#Loaded)\<Entity, Hint>\[]>

### [**](#getResultAndCount)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L1127)getResultAndCount

* ****getResultAndCount**(): Promise<\[Entity\[], number]>

- Executes the query, returning both array of results and total count query (without offset and limit).

  ***

  #### Returns Promise<\[Entity\[], number]>

### [**](#getResultList)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L1061)getResultList

* ****getResultList**(limit): Promise<[Loaded](https://mikro-orm.io/api/core.md#Loaded)\<Entity, Hint>\[]>

- Executes the query, returning array of results

  ***

  #### Parameters

  * ##### optionallimit: number

  #### Returns Promise<[Loaded](https://mikro-orm.io/api/core.md#Loaded)\<Entity, Hint>\[]>

### [**](#getSingleResult)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L1097)getSingleResult

* ****getSingleResult**(): Promise\<null | Entity>

- Executes the query, returning the first result or null

  ***

  #### Returns Promise\<null | Entity>

### [**](#groupBy)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L617)groupBy

* ****groupBy**(fields): [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<Entity, RootAlias, Hint, Context>

- #### Parameters

  * ##### fields: EntityKeyOrString\<Entity> | readonly<!-- --> EntityKeyOrString\<Entity>\[]

  #### Returns [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<Entity, RootAlias, Hint, Context>

### [**](#hasFlag)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L765)hasFlag

* ****hasFlag**(flag): boolean

- #### Parameters

  * ##### flag: [QueryFlag](https://mikro-orm.io/api/core/enum/QueryFlag.md)

  #### Returns boolean

### [**](#having)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L624)having

* ****having**(cond, params, operator): [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<Entity, RootAlias, Hint, Context>

- #### Parameters

  * ##### cond: string | [QBFilterQuery](https://mikro-orm.io/api/core.md#QBFilterQuery) = <!-- -->{}
  * ##### optionalparams: any\[]
  * ##### optionaloperator: $and | $or

  #### Returns [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<Entity, RootAlias, Hint, Context>

### [**](#hintComment)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L798)hintComment

* ****hintComment**(comment): this

- Add hints to the query using comment-like syntax `/*+ ... *&#8205;/`. MySQL and Oracle use this syntax for optimizer hints. Also various DB proxies and routers use this syntax to pass hints to alter their behavior. In other dialects the hints are ignored as simple comments.

  ***

  #### Parameters

  * ##### comment: string | string\[]

  #### Returns this

### [**](#ignore)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L667)ignore

* ****ignore**(): this

- #### Returns this

### [**](#indexHint)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L778)indexHint

* ****indexHint**(sql): this

- Adds index hint to the FROM clause.

  ***

  #### Parameters

  * ##### sql: string

  #### Returns this

### [**](#innerJoin)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L311)innerJoin

* ****innerJoin**\<Field, Alias>(field, alias, cond, schema): [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<Entity, RootAlias, Hint, { \[ K in string | number | symbol ]: IsNever\<Context, true, false> extends true ? AddToContext\<GetType\<Entity, object, Field>, object, Field, Alias, false> : Context & AddToContext\<GetType\<Entity, Context, Field>, Context, Field, Alias, false>\[K] }>

- #### Parameters

  * ##### field: QueryBuilder\<any, any> | [QueryBuilder](https://mikro-orm.io/api/knex/class/QueryBuilder.md)\<any, never, never, never> | Field
  * ##### alias: Alias
  * ##### cond: [QBFilterQuery](https://mikro-orm.io/api/core.md#QBFilterQuery) = <!-- -->{}
  * ##### optionalschema: string

  #### Returns [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<Entity, RootAlias, Hint, { \[ K in string | number | symbol ]: IsNever\<Context, true, false> extends true ? AddToContext\<GetType\<Entity, object, Field>, object, Field, Alias, false> : Context & AddToContext\<GetType\<Entity, Context, Field>, Context, Field, Alias, false>\[K] }>

### [**](#innerJoinAndSelect)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L401)innerJoinAndSelect

* ****innerJoinAndSelect**\<Field, Alias>(field, alias, cond, fields, schema): [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<Entity, RootAlias, [ModifyHint](https://mikro-orm.io/api/knex.md#ModifyHint)\<RootAlias, Context, Hint, Field, true> & {}, { \[ K in string | number | symbol ]: IsNever\<Context, true, false> extends true ? AddToContext\<GetType\<Entity, object, Field>, object, Field, Alias, true> : Context & AddToContext\<GetType\<Entity, Context, Field>, Context, Field, Alias, true>\[K] }>

- #### Parameters

  * ##### field: Field | \[field: Field, qb: QueryBuilder\<any, any> | [QueryBuilder](https://mikro-orm.io/api/knex/class/QueryBuilder.md)\<any, never, never, never>]
  * ##### alias: Alias
  * ##### cond: [QBFilterQuery](https://mikro-orm.io/api/core.md#QBFilterQuery) = <!-- -->{}
  * ##### optionalfields: string\[]
  * ##### optionalschema: string

  #### Returns [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<Entity, RootAlias, [ModifyHint](https://mikro-orm.io/api/knex.md#ModifyHint)\<RootAlias, Context, Hint, Field, true> & {}, { \[ K in string | number | symbol ]: IsNever\<Context, true, false> extends true ? AddToContext\<GetType\<Entity, object, Field>, object, Field, Alias, true> : Context & AddToContext\<GetType\<Entity, Context, Field>, Context, Field, Alias, true>\[K] }>

### [**](#innerJoinLateral)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L321)innerJoinLateral

* ****innerJoinLateral**(field, alias, cond, schema): this

- #### Parameters

  * ##### field: QueryBuilder\<any, any> | [QueryBuilder](https://mikro-orm.io/api/knex/class/QueryBuilder.md)\<any, never, never, never>
  * ##### alias: string
  * ##### cond: [QBFilterQuery](https://mikro-orm.io/api/core.md#QBFilterQuery) = <!-- -->{}
  * ##### optionalschema: string

  #### Returns this

### [**](#innerJoinLateralAndSelect)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L411)innerJoinLateralAndSelect

* ****innerJoinLateralAndSelect**\<Field, Alias>(field, alias, cond, fields, schema): [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<Entity, RootAlias, [ModifyHint](https://mikro-orm.io/api/knex.md#ModifyHint)\<RootAlias, Context, Hint, Field, true> & {}, { \[ K in string | number | symbol ]: IsNever\<Context, true, false> extends true ? AddToContext\<GetType\<Entity, object, Field>, object, Field, Alias, true> : Context & AddToContext\<GetType\<Entity, Context, Field>, Context, Field, Alias, true>\[K] }>

- #### Parameters

  * ##### field: \[field: Field, qb: QueryBuilder\<any, any> | [QueryBuilder](https://mikro-orm.io/api/knex/class/QueryBuilder.md)\<any, never, never, never>]
  * ##### alias: Alias
  * ##### cond: [QBFilterQuery](https://mikro-orm.io/api/core.md#QBFilterQuery) = <!-- -->{}
  * ##### optionalfields: string\[]
  * ##### optionalschema: string

  #### Returns [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<Entity, RootAlias, [ModifyHint](https://mikro-orm.io/api/knex.md#ModifyHint)\<RootAlias, Context, Hint, Field, true> & {}, { \[ K in string | number | symbol ]: IsNever\<Context, true, false> extends true ? AddToContext\<GetType\<Entity, object, Field>, object, Field, Alias, true> : Context & AddToContext\<GetType\<Entity, Context, Field>, Context, Field, Alias, true>\[K] }>

### [**](#insert)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L267)insert

* ****insert**(data): [InsertQueryBuilder](https://mikro-orm.io/api/knex/interface/InsertQueryBuilder.md)\<Entity>

- #### Parameters

  * ##### data: [RequiredEntityData](https://mikro-orm.io/api/core.md#RequiredEntityData)\<Entity> | [RequiredEntityData](https://mikro-orm.io/api/core.md#RequiredEntityData)\<Entity>\[]

  #### Returns [InsertQueryBuilder](https://mikro-orm.io/api/knex/interface/InsertQueryBuilder.md)\<Entity>

### [**](#join)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L299)join

* ****join**\<Field, Alias>(field, alias, cond, type, path, schema): [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<Entity, RootAlias, Hint, { \[ K in string | number | symbol ]: IsNever\<Context, true, false> extends true ? AddToContext\<GetType\<Entity, object, Field>, object, Field, Alias, false> : Context & AddToContext\<GetType\<Entity, Context, Field>, Context, Field, Alias, false>\[K] }>

- #### Parameters

  * ##### field: QueryBuilder\<any, any> | Field | [QueryBuilder](https://mikro-orm.io/api/knex/class/QueryBuilder.md)\<any, never, never, never>
  * ##### alias: Alias
  * ##### cond: [QBFilterQuery](https://mikro-orm.io/api/core.md#QBFilterQuery) = <!-- -->{}
  * ##### type: [JoinType](https://mikro-orm.io/api/knex/enum/JoinType.md) = <!-- -->JoinType.innerJoin
  * ##### optionalpath: string
  * ##### optionalschema: string

  #### Returns [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<Entity, RootAlias, Hint, { \[ K in string | number | symbol ]: IsNever\<Context, true, false> extends true ? AddToContext\<GetType\<Entity, object, Field>, object, Field, Alias, false> : Context & AddToContext\<GetType\<Entity, Context, Field>, Context, Field, Alias, false>\[K] }>

### [**](#joinAndSelect)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L339)joinAndSelect

* ****joinAndSelect**\<Field, Alias>(field, alias, cond, type, path, fields, schema): [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<Entity, RootAlias, [ModifyHint](https://mikro-orm.io/api/knex.md#ModifyHint)\<RootAlias, Context, Hint, Field, true> & {}, { \[ K in string | number | symbol ]: IsNever\<Context, true, false> extends true ? AddToContext\<GetType\<Entity, object, Field>, object, Field, Alias, true> : Context & AddToContext\<GetType\<Entity, Context, Field>, Context, Field, Alias, true>\[K] }>

- #### Parameters

  * ##### field: Field | \[field: Field, qb: QueryBuilder\<any, any> | [QueryBuilder](https://mikro-orm.io/api/knex/class/QueryBuilder.md)\<any, never, never, never>]
  * ##### alias: Alias
  * ##### cond: [QBFilterQuery](https://mikro-orm.io/api/core.md#QBFilterQuery) = <!-- -->{}
  * ##### type: [JoinType](https://mikro-orm.io/api/knex/enum/JoinType.md) = <!-- -->JoinType.innerJoin
  * ##### optionalpath: string
  * ##### optionalfields: string\[]
  * ##### optionalschema: string

  #### Returns [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<Entity, RootAlias, [ModifyHint](https://mikro-orm.io/api/knex.md#ModifyHint)\<RootAlias, Context, Hint, Field, true> & {}, { \[ K in string | number | symbol ]: IsNever\<Context, true, false> extends true ? AddToContext\<GetType\<Entity, object, Field>, object, Field, Alias, true> : Context & AddToContext\<GetType\<Entity, Context, Field>, Context, Field, Alias, true>\[K] }>

### [**](#leftJoin)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L326)leftJoin

* ****leftJoin**\<Field, Alias>(field, alias, cond, schema): [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<Entity, RootAlias, Hint, { \[ K in string | number | symbol ]: IsNever\<Context, true, false> extends true ? AddToContext\<GetType\<Entity, object, Field>, object, Field, Alias, false> : Context & AddToContext\<GetType\<Entity, Context, Field>, Context, Field, Alias, false>\[K] }>

- #### Parameters

  * ##### field: QueryBuilder\<any, any> | [QueryBuilder](https://mikro-orm.io/api/knex/class/QueryBuilder.md)\<any, never, never, never> | Field
  * ##### alias: Alias
  * ##### cond: [QBFilterQuery](https://mikro-orm.io/api/core.md#QBFilterQuery) = <!-- -->{}
  * ##### optionalschema: string

  #### Returns [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<Entity, RootAlias, Hint, { \[ K in string | number | symbol ]: IsNever\<Context, true, false> extends true ? AddToContext\<GetType\<Entity, object, Field>, object, Field, Alias, false> : Context & AddToContext\<GetType\<Entity, Context, Field>, Context, Field, Alias, false>\[K] }>

### [**](#leftJoinAndSelect)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L381)leftJoinAndSelect

* ****leftJoinAndSelect**\<Field, Alias>(field, alias, cond, fields, schema): [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<Entity, RootAlias, [ModifyHint](https://mikro-orm.io/api/knex.md#ModifyHint)\<RootAlias, Context, Hint, Field, true> & {}, { \[ K in string | number | symbol ]: IsNever\<Context, true, false> extends true ? AddToContext\<GetType\<Entity, object, Field>, object, Field, Alias, true> : Context & AddToContext\<GetType\<Entity, Context, Field>, Context, Field, Alias, true>\[K] }>

- #### Parameters

  * ##### field: Field | \[field: Field, qb: QueryBuilder\<any, any> | [QueryBuilder](https://mikro-orm.io/api/knex/class/QueryBuilder.md)\<any, never, never, never>]
  * ##### alias: Alias
  * ##### cond: [QBFilterQuery](https://mikro-orm.io/api/core.md#QBFilterQuery) = <!-- -->{}
  * ##### optionalfields: string\[]
  * ##### optionalschema: string

  #### Returns [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<Entity, RootAlias, [ModifyHint](https://mikro-orm.io/api/knex.md#ModifyHint)\<RootAlias, Context, Hint, Field, true> & {}, { \[ K in string | number | symbol ]: IsNever\<Context, true, false> extends true ? AddToContext\<GetType\<Entity, object, Field>, object, Field, Alias, true> : Context & AddToContext\<GetType\<Entity, Context, Field>, Context, Field, Alias, true>\[K] }>

### [**](#leftJoinLateral)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L335)leftJoinLateral

* ****leftJoinLateral**(field, alias, cond, schema): this

- #### Parameters

  * ##### field: QueryBuilder\<any, any> | [QueryBuilder](https://mikro-orm.io/api/knex/class/QueryBuilder.md)\<any, never, never, never>
  * ##### alias: string
  * ##### cond: [QBFilterQuery](https://mikro-orm.io/api/core.md#QBFilterQuery) = <!-- -->{}
  * ##### optionalschema: string

  #### Returns this

### [**](#leftJoinLateralAndSelect)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L391)leftJoinLateralAndSelect

* ****leftJoinLateralAndSelect**\<Field, Alias>(field, alias, cond, fields, schema): [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<Entity, RootAlias, [ModifyHint](https://mikro-orm.io/api/knex.md#ModifyHint)\<RootAlias, Context, Hint, Field, true> & {}, { \[ K in string | number | symbol ]: IsNever\<Context, true, false> extends true ? AddToContext\<GetType\<Entity, object, Field>, object, Field, Alias, true> : Context & AddToContext\<GetType\<Entity, Context, Field>, Context, Field, Alias, true>\[K] }>

- #### Parameters

  * ##### field: \[field: Field, qb: QueryBuilder\<any, any> | [QueryBuilder](https://mikro-orm.io/api/knex/class/QueryBuilder.md)\<any, never, never, never>]
  * ##### alias: Alias
  * ##### cond: [QBFilterQuery](https://mikro-orm.io/api/core.md#QBFilterQuery) = <!-- -->{}
  * ##### optionalfields: string\[]
  * ##### optionalschema: string

  #### Returns [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<Entity, RootAlias, [ModifyHint](https://mikro-orm.io/api/knex.md#ModifyHint)\<RootAlias, Context, Hint, Field, true> & {}, { \[ K in string | number | symbol ]: IsNever\<Context, true, false> extends true ? AddToContext\<GetType\<Entity, object, Field>, object, Field, Alias, true> : Context & AddToContext\<GetType\<Entity, Context, Field>, Context, Field, Alias, true>\[K] }>

### [**](#limit)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L710)limit

* ****limit**(limit, offset): [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<Entity, RootAlias, Hint, Context>

- #### Parameters

  * ##### optionallimit: number
  * ##### offset: number = <!-- -->0

  #### Returns [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<Entity, RootAlias, Hint, Context>

### [**](#merge)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L676)merge

* ****merge**(data): this

- #### Parameters

  * ##### optionaldata: [Field](https://mikro-orm.io/api/knex.md#Field)\<Entity>\[] | [EntityData](https://mikro-orm.io/api/core.md#EntityData)\<Entity>

  #### Returns this

### [**](#offset)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L721)offset

* ****offset**(offset): [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<Entity, RootAlias, Hint, Context>

- #### Parameters

  * ##### optionaloffset: number

  #### Returns [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<Entity, RootAlias, Hint, Context>

### [**](#onConflict)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L651)onConflict

* ****onConflict**(fields): [InsertQueryBuilder](https://mikro-orm.io/api/knex/interface/InsertQueryBuilder.md)\<Entity>

- #### Parameters

  * ##### fields: [Field](https://mikro-orm.io/api/knex.md#Field)\<Entity> | [Field](https://mikro-orm.io/api/knex.md#Field)\<Entity>\[] = <!-- -->\[]

  #### Returns [InsertQueryBuilder](https://mikro-orm.io/api/knex/interface/InsertQueryBuilder.md)\<Entity>

### [**](#orderBy)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L597)orderBy

* ****orderBy**(orderBy): [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<Entity, RootAlias, Hint, Context>

- #### Parameters

  * ##### orderBy: [QBQueryOrderMap](https://mikro-orm.io/api/core.md#QBQueryOrderMap)\<Entity> | [QBQueryOrderMap](https://mikro-orm.io/api/core.md#QBQueryOrderMap)\<Entity>\[]

  #### Returns [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<Entity, RootAlias, Hint, Context>

### [**](#orHaving)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L647)orHaving

* ****orHaving**(cond, params): [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<Entity, RootAlias, Hint, Context>

- #### Parameters

  * ##### optionalcond: string | [QBFilterQuery](https://mikro-orm.io/api/core.md#QBFilterQuery)
  * ##### optionalparams: any\[]

  #### Returns [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<Entity, RootAlias, Hint, Context>

### [**](#orWhere)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L591)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L592)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L593)orWhere

* ****orWhere**(cond): this
* ****orWhere**(cond, params): this

- #### Parameters

  * ##### cond: [QBFilterQuery](https://mikro-orm.io/api/core.md#QBFilterQuery)\<Entity>

  #### Returns this

### [**](#returning)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L689)returning

* ****returning**(fields): this

- #### Parameters

  * ##### optionalfields: [Field](https://mikro-orm.io/api/knex.md#Field)\<Entity> | [Field](https://mikro-orm.io/api/knex.md#Field)\<Entity>\[]

  #### Returns this

### [**](#select)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L234)select

* ****select**(fields, distinct): [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<Entity, RootAlias, Hint, Context>

- #### Parameters

  * ##### fields: [Field](https://mikro-orm.io/api/knex.md#Field)\<Entity> | [Field](https://mikro-orm.io/api/knex.md#Field)\<Entity>\[]
  * ##### distinct: boolean = <!-- -->false

  #### Returns [SelectQueryBuilder](https://mikro-orm.io/api/knex/interface/SelectQueryBuilder.md)\<Entity, RootAlias, Hint, Context>

### [**](#setFlag)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L753)setFlag

* ****setFlag**(flag): this

- #### Parameters

  * ##### flag: [QueryFlag](https://mikro-orm.io/api/core/enum/QueryFlag.md)

  #### Returns this

### [**](#setFlushMode)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L747)setFlushMode

* ****setFlushMode**(flushMode): this

- #### Parameters

  * ##### optionalflushMode: [FlushMode](https://mikro-orm.io/api/core/enum/FlushMode.md)

  #### Returns this

### [**](#setLockMode)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L734)setLockMode

* ****setLockMode**(mode, tables): this

- #### Parameters

  * ##### optionalmode: [LockMode](https://mikro-orm.io/api/core/enum/LockMode.md)
  * ##### optionaltables: string\[]

  #### Returns this

### [**](#setLoggerContext)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L1250)setLoggerContext

* ****setLoggerContext**(context): void

- Sets logger context for this query builder.

  ***

  #### Parameters

  * ##### context: [LoggingOptions](https://mikro-orm.io/api/core.md#LoggingOptions) & [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)

  #### Returns void

### [**](#then)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L1137)then

* ****then**\<TResult1, TResult2>(onfulfilled, onrejected): Promise\<number | [Loaded](https://mikro-orm.io/api/core.md#Loaded)\<Entity, Hint>\[] | [QueryResult](https://mikro-orm.io/api/core/interface/QueryResult.md)\<Entity>>

- Provides promise-like interface so we can await the QB instance.

  ***

  #### Parameters

  * ##### optionalonfulfilled: null | (value) => TResult1 | PromiseLike\<TResult1>
  *
    ##### optionalonrejected: null | (reason) => TResult2 | PromiseLike\<TResult2>


  #### Returns Promise\<number | [Loaded](https://mikro-orm.io/api/core.md#Loaded)\<Entity, Hint>\[] | [QueryResult](https://mikro-orm.io/api/core/interface/QueryResult.md)\<Entity>>

### [**](#toQuery)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L886)toQuery

* ****toQuery**(): { \_sql: Sql; params: readonly
  <!-- -->
  unknown\[]; sql: string }

- #### Returns { \_sql: Sql; params: readonly<!-- --> unknown\[]; sql: string }

  * ##### \_sql: Sql
  * ##### params: readonly<!-- --> unknown\[]
  * ##### sql: string

### [**](#truncate)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L279)truncate

* ****truncate**(): [TruncateQueryBuilder](https://mikro-orm.io/api/knex/interface/TruncateQueryBuilder.md)\<Entity>

- #### Returns [TruncateQueryBuilder](https://mikro-orm.io/api/knex/interface/TruncateQueryBuilder.md)\<Entity>

### [**](#unsetFlag)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L759)unsetFlag

* ****unsetFlag**(flag): this

- #### Parameters

  * ##### flag: [QueryFlag](https://mikro-orm.io/api/core/enum/QueryFlag.md)

  #### Returns this

### [**](#update)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L271)update

* ****update**(data): [UpdateQueryBuilder](https://mikro-orm.io/api/knex/interface/UpdateQueryBuilder.md)\<Entity>

- #### Parameters

  * ##### data: [EntityData](https://mikro-orm.io/api/core.md#EntityData)\<Entity>

  #### Returns [UpdateQueryBuilder](https://mikro-orm.io/api/knex/interface/UpdateQueryBuilder.md)\<Entity>

### [**](#where)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L532)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L533)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L534)where

* ****where**(cond, operator): this
* ****where**(cond, params, operator): this

- #### Parameters

  * ##### cond: [QBFilterQuery](https://mikro-orm.io/api/core.md#QBFilterQuery)\<Entity>
  * ##### optionaloperator: $and | $or

  #### Returns this

### [**](#withSchema)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L727)withSchema

* ****withSchema**(schema): this

- #### Parameters

  * ##### optionalschema: string

  #### Returns this

### [**](#withSubQuery)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/query/QueryBuilder.ts#L526)withSubQuery

* ****withSubQuery**(subQuery, alias): this

- #### Parameters

  * ##### subQuery: QueryBuilder\<any, any>
  * ##### alias: string

  #### Returns this
