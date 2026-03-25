# Source: https://mikro-orm.io/api/oracledb/class/OracleQueryBuilder.md

# OracleQueryBuilder<!-- --> \<Entity, RootAlias, Hint, Context>

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

* [QueryBuilder](https://mikro-orm.io/api/sql/class/QueryBuilder.md)\<Entity, RootAlias, Hint, Context>
  * *OracleQueryBuilder*

## Index[**](#index)

### Properties

* [**\_\_subquery](#__subquery)

### Accessors

* [**alias](#alias)
* [**helper](#helper)
* [**mainAlias](#mainAlias)
* [**type](#type)

### Methods

* [**addSelect](#addSelect)
* [**andHaving](#andHaving)
* [**andOrderBy](#andOrderBy)
* [**andWhere](#andWhere)
* [**applyFilters](#applyFilters)
* [**as](#as)
* [**cache](#cache)
* [**clone](#clone)
* [**collation](#collation)
* [**comment](#comment)
* [**count](#count)
* [**delete](#delete)
* [**distinct](#distinct)
* [**distinctOn](#distinctOn)
* [**execute](#execute)
* [**from](#from)
* [**getCount](#getCount)
* [**getFormattedQuery](#getFormattedQuery)
* [**getLoggerContext](#getLoggerContext)
* [**getNativeQuery](#getnativequery)
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
* [**setLockMode](#setlockmode)
* [**setLoggerContext](#setLoggerContext)
* [**stream](#stream)
* [**toQuery](#toQuery)
* [**toRaw](#toRaw)
* [**truncate](#truncate)
* [**union](#union)
* [**unionAll](#unionAll)
* [**unsetFlag](#unsetFlag)
* [**update](#update)
* [**where](#where)
* [**with](#with)
* [**withRecursive](#withRecursive)
* [**withSchema](#withSchema)
* [**withSubQuery](#withSubQuery)

## Properties<!-- -->[**](#properties)

### [**](#__subquery)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L566)readonlyinherited\_\_subquery

**\_\_subquery: true

Inherited from QueryBuilder.\_\_subquery

## Accessors<!-- -->[**](#accessors)

### [**](#alias)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L604)inheritedalias

* **get alias(): string

* Inherited from QueryBuilder.alias

  #### Returns string

### [**](#helper)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L608)inheritedhelper

* **get helper(): QueryBuilderHelper

* Inherited from QueryBuilder.helper

  #### Returns QueryBuilderHelper

### [**](#mainAlias)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L599)inheritedmainAlias

* **get mainAlias(): [Alias](https://mikro-orm.io/api/sql/interface/Alias.md)\<Entity>

* Inherited from QueryBuilder.mainAlias

  #### Returns [Alias](https://mikro-orm.io/api/sql/interface/Alias.md)\<Entity>

### [**](#type)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L613)inheritedtype

* **get type(): [QueryType](https://mikro-orm.io/api/sql/enum/QueryType.md)

* Inherited from QueryBuilder.type

  #### Returns [QueryType](https://mikro-orm.io/api/sql/enum/QueryType.md)

## Methods<!-- -->[**](#methods)

### [**](#addSelect)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L780)inheritedaddSelect

* ****addSelect**\<F>(fields): [SelectQueryBuilder](https://mikro-orm.io/api/sql/interface/SelectQueryBuilder.md)\<Entity, RootAlias, Hint, Context, ExtractRawAliases\<F extends readonly
  <!-- -->
  unknown\[] ? F\<F> : \[F]>, \* | ExtractRootFields\<F extends readonly
  <!-- -->
  U\[] ? U & string : F & string, RootAlias, Context>, {}>

* Inherited from QueryBuilder.addSelect

  Adds fields to an existing SELECT query.

  ***

  #### Parameters

  * ##### fields: F

  #### Returns [SelectQueryBuilder](https://mikro-orm.io/api/sql/interface/SelectQueryBuilder.md)\<Entity, RootAlias, Hint, Context, ExtractRawAliases\<F extends readonly<!-- --> unknown\[] ? F\<F> : \[F]>, \* | ExtractRootFields\<F extends readonly<!-- --> U\[] ? U & string : F & string, RootAlias, Context>, {}>

### [**](#andHaving)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L1803)inheritedandHaving

* ****andHaving**(cond, params): [SelectQueryBuilder](https://mikro-orm.io/api/sql/interface/SelectQueryBuilder.md)\<Entity, RootAlias, Hint, Context, never, \*, {}>

* Inherited from QueryBuilder.andHaving

  #### Parameters

  * ##### optionalcond: string | [QBFilterQuery](https://mikro-orm.io/api/sql.md#QBFilterQuery)\<Entity, RootAlias, Context, never>

  * ##### optionalparams: any\[]

  #### Returns [SelectQueryBuilder](https://mikro-orm.io/api/sql/interface/SelectQueryBuilder.md)\<Entity, RootAlias, Hint, Context, never, \*, {}>

### [**](#andOrderBy)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L1620)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L1628)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L1637)inheritedandOrderBy

* ****andOrderBy**(orderBy): [SelectQueryBuilder](https://mikro-orm.io/api/sql/interface/SelectQueryBuilder.md)\<Entity, RootAlias, Hint, Context, never, \*, {}>
* ****andOrderBy**\<T>(orderBy): [SelectQueryBuilder](https://mikro-orm.io/api/sql/interface/SelectQueryBuilder.md)\<Entity, RootAlias, Hint, Context, never, \*, {}>

* Inherited from QueryBuilder.andOrderBy

  Adds additional ORDER BY clause without replacing existing order.

  ***

  #### Parameters

  * ##### orderBy: [ContextOrderByMap](https://mikro-orm.io/api/sql.md#ContextOrderByMap)\<Entity, RootAlias, Context, never> | [ContextOrderByMap](https://mikro-orm.io/api/sql.md#ContextOrderByMap)\<Entity, RootAlias, Context, never>\[]

  #### Returns [SelectQueryBuilder](https://mikro-orm.io/api/sql/interface/SelectQueryBuilder.md)\<Entity, RootAlias, Hint, Context, never, \*, {}>

### [**](#andWhere)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L1534)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L1543)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L1544)inheritedandWhere

* ****andWhere**(cond): this
* ****andWhere**(cond, params): this

* Inherited from QueryBuilder.andWhere

  Adds an AND WHERE clause to the query using an object condition.

  * **@example**

    ```
    qb.where({ status: 'active' }).andWhere({ role: 'admin' });
    qb.where({ name: 'John' }).andWhere({ 'b.title': 'test' });
    ```

  ***

  #### Parameters

  * ##### cond: [QBFilterQuery](https://mikro-orm.io/api/sql.md#QBFilterQuery)\<Entity, RootAlias, Context, never>

  #### Returns this

### [**](#applyFilters)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L1346)inheritedapplyFilters

* ****applyFilters**(filterOptions): Promise\<void>

* Inherited from QueryBuilder.applyFilters

  Apply filters to the QB where condition.

  ***

  #### Parameters

  * ##### filterOptions: [FilterOptions](https://mikro-orm.io/api/core.md#FilterOptions) = <!-- -->{}

  #### Returns Promise\<void>

### [**](#as)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L2581)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L2587)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L2589)inheritedas

* ****as**(alias): NativeQueryBuilder
* ****as**\<T>(targetEntity, alias): NativeQueryBuilder

* Inherited from QueryBuilder.as

  Returns native query builder instance with sub-query aliased with given alias.

  ***

  #### Parameters

  * ##### alias: string

  #### Returns NativeQueryBuilder

### [**](#cache)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L1958)inheritedcache

* ****cache**(config): this

* Inherited from QueryBuilder.cache

  #### Parameters

  * ##### config: number | boolean | \[string, number] = <!-- -->true

  #### Returns this

### [**](#clone)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L2778)inheritedclone

* ****clone**(reset, preserve): [QueryBuilder](https://mikro-orm.io/api/sql/class/QueryBuilder.md)\<Entity, RootAlias, Hint, Context, never, \*, {}>

* Inherited from QueryBuilder.clone

  #### Parameters

  * ##### optionalreset: boolean | keyof<!-- --> QBState\<Entity>\[]

  * ##### optionalpreserve: keyof<!-- --> QBState\<Entity>\[]

  #### Returns [QueryBuilder](https://mikro-orm.io/api/sql/class/QueryBuilder.md)\<Entity, RootAlias, Hint, Context, never, \*, {}>

### [**](#collation)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L1976)inheritedcollation

* ****collation**(collation): this

* Inherited from QueryBuilder.collation

  Adds COLLATE clause to ORDER BY expressions.

  ***

  #### Parameters

  * ##### collation: undefined | string

  #### Returns this

### [**](#comment)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L1985)inheritedcomment

* ****comment**(comment): this

* Inherited from QueryBuilder.comment

  Prepend comment to the sql query using the syntax `/* ... *&#8205;/`. Some characters are forbidden such as `/*, *&#8205;/` and `?`.

  ***

  #### Parameters

  * ##### comment: undefined | string | string\[]

  #### Returns this

### [**](#count)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L903)inheritedcount

* ****count**\<F>(field, distinct): [CountQueryBuilder](https://mikro-orm.io/api/sql/interface/CountQueryBuilder.md)\<Entity>

* Inherited from QueryBuilder.count

  Creates a COUNT query to count matching rows.

  * **@example**

    ```
    const count = await em.createQueryBuilder(User)
      .count()
      .where({ isActive: true })
      .execute('get');
    ```

  ***

  #### Parameters

  * ##### optionalfield: F | F\[]

  * ##### distinct: boolean = <!-- -->false

  #### Returns [CountQueryBuilder](https://mikro-orm.io/api/sql/interface/CountQueryBuilder.md)\<Entity>

### [**](#delete)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L881)inheriteddelete

* ****delete**(cond): [DeleteQueryBuilder](https://mikro-orm.io/api/sql/interface/DeleteQueryBuilder.md)\<Entity, RootAlias, Context>

* Inherited from QueryBuilder.delete

  Creates a DELETE query. Use `where()` to specify which rows to delete.

  * **@example**

    ```
    await em.createQueryBuilder(User)
      .delete()
      .where({ id: 1 })
      .execute();

    // Or pass the condition directly
    await em.createQueryBuilder(User)
      .delete({ isActive: false })
      .execute();
    ```

  ***

  #### Parameters

  * ##### optionalcond: [QBFilterQuery](https://mikro-orm.io/api/sql.md#QBFilterQuery)\<Entity, RootAlias, Context, never>

  #### Returns [DeleteQueryBuilder](https://mikro-orm.io/api/sql/interface/DeleteQueryBuilder.md)\<Entity, RootAlias, Context>

### [**](#distinct)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L800)inheriteddistinct

* ****distinct**(): [SelectQueryBuilder](https://mikro-orm.io/api/sql/interface/SelectQueryBuilder.md)\<Entity, RootAlias, Hint, Context, never, \*, {}>

* Inherited from QueryBuilder.distinct

  #### Returns [SelectQueryBuilder](https://mikro-orm.io/api/sql/interface/SelectQueryBuilder.md)\<Entity, RootAlias, Hint, Context, never, \*, {}>

### [**](#distinctOn)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L814)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L818)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L821)inheriteddistinctOn

* ****distinctOn**\<F>(fields): [SelectQueryBuilder](https://mikro-orm.io/api/sql/interface/SelectQueryBuilder.md)\<Entity, RootAlias, Hint, Context, never, \*, {}>
* ****distinctOn**\<F>(fields): [SelectQueryBuilder](https://mikro-orm.io/api/sql/interface/SelectQueryBuilder.md)\<Entity, RootAlias, Hint, Context, never, \*, {}>

* Inherited from QueryBuilder.distinctOn

  postgres only

  ***

  #### Parameters

  * ##### fields: F

  #### Returns [SelectQueryBuilder](https://mikro-orm.io/api/sql/interface/SelectQueryBuilder.md)\<Entity, RootAlias, Hint, Context, never, \*, {}>

### [**](#execute)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L2333)inheritedexecute

* ****execute**\<U>(method, options): Promise\<U>

* Inherited from QueryBuilder.execute

  Executes this QB and returns the raw results, mapped to the property names (unless disabled via last parameter). Use `method` to specify what kind of result you want to get (array/single/meta).

  ***

  #### Parameters

  * ##### optionalmethod: get | all | run

  * ##### optionaloptions: boolean | [ExecuteOptions](https://mikro-orm.io/api/sql/interface/ExecuteOptions.md)

  #### Returns Promise\<U>

### [**](#from)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L2006)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L2014)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L2021)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L2025)inheritedfrom

* ****from**\<Entity>(target, aliasName): [SelectQueryBuilder](https://mikro-orm.io/api/sql/interface/SelectQueryBuilder.md)\<Entity, RootAlias, Hint, Context, never, \*, {}>
* ****from**\<Entity>(target): [SelectQueryBuilder](https://mikro-orm.io/api/sql/interface/SelectQueryBuilder.md)\<Entity, RootAlias, Hint, Context, never, \*, {}>
* ****from**\<Name, Alias>(target, aliasName): [SelectQueryBuilder](https://mikro-orm.io/api/sql/interface/SelectQueryBuilder.md)<{}\[Name], Alias, never, never, never, \*, {}>

* Inherited from QueryBuilder.from

  Specifies FROM which entity's table select/update/delete will be executed, removing all previously set FROM-s. Allows setting a main string alias of the selection data.

  ***

  #### Parameters

  * ##### target: [QueryBuilder](https://mikro-orm.io/api/sql/class/QueryBuilder.md)\<Entity, never, never, never, never, \*, {}>

  * ##### optionalaliasName: string

  #### Returns [SelectQueryBuilder](https://mikro-orm.io/api/sql/interface/SelectQueryBuilder.md)\<Entity, RootAlias, Hint, Context, never, \*, {}>

### [**](#getCount)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L2544)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L2545)inheritedgetCount

* ****getCount**\<F>(field, distinct): Promise\<number>

* Inherited from QueryBuilder.getCount

  Executes count query (without offset and limit), returning total count of results

  ***

  #### Parameters

  * ##### optionalfield: F | F\[]

  * ##### optionaldistinct: boolean

  #### Returns Promise\<number>

### [**](#getFormattedQuery)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L2220)inheritedgetFormattedQuery

* ****getFormattedQuery**(): string

* Inherited from QueryBuilder.getFormattedQuery

  Returns raw interpolated query string with all the parameters inlined.

  ***

  #### Returns string

### [**](#getLoggerContext)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L2826)inheritedgetLoggerContext

* ****getLoggerContext**\<T>(): T

* Inherited from QueryBuilder.getLoggerContext

  Gets logger context for this query builder.

  ***

  #### Returns T

### [**](#getnativequery)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/oracledb/src/OracleQueryBuilder.ts#L40)getNativeQuery

* ****getNativeQuery**(processVirtualEntity): NativeQueryBuilder

* Overrides QueryBuilder.getNativeQuery

  #### Parameters

  * ##### processVirtualEntity: boolean = <!-- -->true

  #### Returns NativeQueryBuilder

### [**](#getParams)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L2213)inheritedgetParams

* ****getParams**(): readonly
  <!-- -->
  unknown\[]

* Inherited from QueryBuilder.getParams

  Returns the list of all parameters for this query.

  ***

  #### Returns readonly<!-- --> unknown\[]

### [**](#getQuery)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L2182)inheritedgetQuery

* ****getQuery**(): string

* Inherited from QueryBuilder.getQuery

  Returns the query with parameters as wildcards.

  ***

  #### Returns string

### [**](#getResult)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L2470)inheritedgetResult

* ****getResult**(): Promise<[Loaded](https://mikro-orm.io/api/core.md#Loaded)\<Entity, Hint, \*>\[]>

* Inherited from QueryBuilder.getResult

  Alias for `qb.getResultList()`

  ***

  #### Returns Promise<[Loaded](https://mikro-orm.io/api/core.md#Loaded)\<Entity, Hint, \*>\[]>

### [**](#getResultAndCount)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L2574)inheritedgetResultAndCount

* ****getResultAndCount**(): Promise<\[[Loaded](https://mikro-orm.io/api/core.md#Loaded)\<Entity, Hint, \*>\[], number]>

* Inherited from QueryBuilder.getResultAndCount

  Executes the query, returning both array of results and total count query (without offset and limit).

  ***

  #### Returns Promise<\[[Loaded](https://mikro-orm.io/api/core.md#Loaded)\<Entity, Hint, \*>\[], number]>

### [**](#getResultList)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L2477)inheritedgetResultList

* ****getResultList**(limit): Promise<[Loaded](https://mikro-orm.io/api/core.md#Loaded)\<Entity, Hint, \*>\[]>

* Inherited from QueryBuilder.getResultList

  Executes the query, returning array of results mapped to entity instances.

  ***

  #### Parameters

  * ##### optionallimit: number

  #### Returns Promise<[Loaded](https://mikro-orm.io/api/core.md#Loaded)\<Entity, Hint, \*>\[]>

### [**](#getSingleResult)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L2532)inheritedgetSingleResult

* ****getSingleResult**(): Promise\<null | [Loaded](https://mikro-orm.io/api/core.md#Loaded)\<Entity, Hint, \*>>

* Inherited from QueryBuilder.getSingleResult

  Executes the query, returning the first result or null

  ***

  #### Returns Promise\<null | [Loaded](https://mikro-orm.io/api/core.md#Loaded)\<Entity, Hint, \*>>

### [**](#groupBy)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L1717)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L1729)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L1741)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L1744)inheritedgroupBy

* ****groupBy**\<F>(fields): [SelectQueryBuilder](https://mikro-orm.io/api/sql/interface/SelectQueryBuilder.md)\<Entity, RootAlias, Hint, Context, never, \*, {}>
* ****groupBy**\<F>(fields): [SelectQueryBuilder](https://mikro-orm.io/api/sql/interface/SelectQueryBuilder.md)\<Entity, RootAlias, Hint, Context, never, \*, {}>
* ****groupBy**\<P>(fields): [SelectQueryBuilder](https://mikro-orm.io/api/sql/interface/SelectQueryBuilder.md)\<Entity, RootAlias, Hint, Context, never, \*, {}>

* Inherited from QueryBuilder.groupBy

  Adds a GROUP BY clause to the query.

  * **@example**

    ```
    qb.select([raw('count(*) as count'), 'status'])
      .groupBy('status');
    ```

  ***

  #### Parameters

  * ##### fields: F

  #### Returns [SelectQueryBuilder](https://mikro-orm.io/api/sql/interface/SelectQueryBuilder.md)\<Entity, RootAlias, Hint, Context, never, \*, {}>

### [**](#hasFlag)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L1954)inheritedhasFlag

* ****hasFlag**(flag): boolean

* Inherited from QueryBuilder.hasFlag

  #### Parameters

  * ##### flag: [QueryFlag](https://mikro-orm.io/api/core/enum/QueryFlag.md)

  #### Returns boolean

### [**](#having)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L1773)inheritedhaving

* ****having**(cond, params, operator): [SelectQueryBuilder](https://mikro-orm.io/api/sql/interface/SelectQueryBuilder.md)\<Entity, RootAlias, Hint, Context, never, \*, {}>

* Inherited from QueryBuilder.having

  Adds a HAVING clause to the query, typically used with GROUP BY.

  * **@example**

    ```
    qb.select([raw('count(*) as count'), 'status'])
      .groupBy('status')
      .having({ count: { $gt: 5 } });
    ```

  ***

  #### Parameters

  * ##### cond: string | [QBFilterQuery](https://mikro-orm.io/api/sql.md#QBFilterQuery)\<Entity, RootAlias, Context, never> = <!-- -->{}

  * ##### optionalparams: any\[]

  * ##### optionaloperator: $and | $or

  #### Returns [SelectQueryBuilder](https://mikro-orm.io/api/sql/interface/SelectQueryBuilder.md)\<Entity, RootAlias, Hint, Context, never, \*, {}>

### [**](#hintComment)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L1996)inheritedhintComment

* ****hintComment**(comment): this

* Inherited from QueryBuilder.hintComment

  Add hints to the query using comment-like syntax `/*+ ... *&#8205;/`. MySQL and Oracle use this syntax for optimizer hints. Also various DB proxies and routers use this syntax to pass hints to alter their behavior. In other dialects the hints are ignored as simple comments.

  ***

  #### Parameters

  * ##### comment: undefined | string | string\[]

  #### Returns this

### [**](#ignore)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L1835)inheritedignore

* ****ignore**(): this

* Inherited from QueryBuilder.ignore

  #### Returns this

### [**](#indexHint)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L1967)inheritedindexHint

* ****indexHint**(sql): this

* Inherited from QueryBuilder.indexHint

  Adds index hint to the FROM clause.

  ***

  #### Parameters

  * ##### sql: undefined | string

  #### Returns this

### [**](#innerJoin)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L982)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L1000)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L1007)inheritedinnerJoin

* ****innerJoin**\<Field, Alias>(field, alias, cond, schema): [SelectQueryBuilder](https://mikro-orm.io/api/sql/interface/SelectQueryBuilder.md)\<Entity, RootAlias, Hint, [ModifyContext](https://mikro-orm.io/api/sql.md#ModifyContext)\<Entity, Context, Field, Alias, false>, never, \*, {}>
* ****innerJoin**\<Alias>(field, alias, cond, schema): [SelectQueryBuilder](https://mikro-orm.io/api/sql/interface/SelectQueryBuilder.md)\<Entity, RootAlias, Hint, [ModifyContext](https://mikro-orm.io/api/sql.md#ModifyContext)\<Entity, Context, string, Alias, false>, never, \*, {}>

* Inherited from QueryBuilder.innerJoin

  Adds an INNER JOIN clause to the query for an entity relation.

  ***

  #### Parameters

  * ##### field: Field

  * ##### alias: Alias

  * ##### optionalcond: JoinCondition<[ExpandProperty](https://mikro-orm.io/api/core.md#ExpandProperty)\<GetType\<Entity, Context, Field>\[GetPropName\<Field> & keyof<!-- --> GetType\<Entity, Context, Field>]>, Alias>

  * ##### optionalschema: string

  #### Returns [SelectQueryBuilder](https://mikro-orm.io/api/sql/interface/SelectQueryBuilder.md)\<Entity, RootAlias, Hint, [ModifyContext](https://mikro-orm.io/api/sql.md#ModifyContext)\<Entity, Context, Field, Alias, false>, never, \*, {}>

### [**](#innerJoinAndSelect)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L1225)inheritedinnerJoinAndSelect

* ****innerJoinAndSelect**\<Field, Alias, JoinFields>(field, alias, cond, fields, schema): [SelectQueryBuilder](https://mikro-orm.io/api/sql/interface/SelectQueryBuilder.md)\<Entity, RootAlias, [ModifyHint](https://mikro-orm.io/api/sql.md#ModifyHint)\<RootAlias, Context, Hint, Field, true> & {}, [ModifyContext](https://mikro-orm.io/api/sql.md#ModifyContext)\<Entity, Context, Field, Alias, true>, never, [ModifyFields](https://mikro-orm.io/api/sql.md#ModifyFields)<\*, RootAlias, Context, Field, Alias, JoinFields>, {}>

* Inherited from QueryBuilder.innerJoinAndSelect

  #### Parameters

  * ##### field: Field | \[Field, [RawQueryFragment](https://mikro-orm.io/api/core/class/RawQueryFragment.md)\<string> | [QueryBuilder](https://mikro-orm.io/api/sql/class/QueryBuilder.md)\<any, never, never, never, never, \*, {}>]

  * ##### alias: Alias

  * ##### cond: JoinCondition<[ExpandProperty](https://mikro-orm.io/api/core.md#ExpandProperty)\<GetType\<Entity, Context, Field>\[GetPropName\<Field> & keyof<!-- --> GetType\<Entity, Context, Field>]>, Alias> = <!-- -->

  * ##### optionalfields: JoinFields

  * ##### optionalschema: string

  #### Returns [SelectQueryBuilder](https://mikro-orm.io/api/sql/interface/SelectQueryBuilder.md)\<Entity, RootAlias, [ModifyHint](https://mikro-orm.io/api/sql.md#ModifyHint)\<RootAlias, Context, Hint, Field, true> & {}, [ModifyContext](https://mikro-orm.io/api/sql.md#ModifyContext)\<Entity, Context, Field, Alias, true>, never, [ModifyFields](https://mikro-orm.io/api/sql.md#ModifyFields)<\*, RootAlias, Context, Field, Alias, JoinFields>, {}>

### [**](#innerJoinLateral)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L1025)inheritedinnerJoinLateral

* ****innerJoinLateral**\<Alias>(field, alias, cond, schema): [SelectQueryBuilder](https://mikro-orm.io/api/sql/interface/SelectQueryBuilder.md)\<Entity, RootAlias, Hint, [ModifyContext](https://mikro-orm.io/api/sql.md#ModifyContext)\<Entity, Context, string, Alias, false>, never, \*, {}>

* Inherited from QueryBuilder.innerJoinLateral

  #### Parameters

  * ##### field: [RawQueryFragment](https://mikro-orm.io/api/core/class/RawQueryFragment.md)\<string> | [QueryBuilder](https://mikro-orm.io/api/sql/class/QueryBuilder.md)\<any, never, never, never, never, \*, {}>

  * ##### alias: Alias

  * ##### cond: RawJoinCondition = <!-- -->{}

  * ##### optionalschema: string

  #### Returns [SelectQueryBuilder](https://mikro-orm.io/api/sql/interface/SelectQueryBuilder.md)\<Entity, RootAlias, Hint, [ModifyContext](https://mikro-orm.io/api/sql.md#ModifyContext)\<Entity, Context, string, Alias, false>, never, \*, {}>

### [**](#innerJoinLateralAndSelect)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L1255)inheritedinnerJoinLateralAndSelect

* ****innerJoinLateralAndSelect**\<Field, Alias, JoinFields>(field, alias, cond, fields, schema): [SelectQueryBuilder](https://mikro-orm.io/api/sql/interface/SelectQueryBuilder.md)\<Entity, RootAlias, [ModifyHint](https://mikro-orm.io/api/sql.md#ModifyHint)\<RootAlias, Context, Hint, Field, true> & {}, [ModifyContext](https://mikro-orm.io/api/sql.md#ModifyContext)\<Entity, Context, Field, Alias, true>, never, [ModifyFields](https://mikro-orm.io/api/sql.md#ModifyFields)<\*, RootAlias, Context, Field, Alias, JoinFields>, {}>

* Inherited from QueryBuilder.innerJoinLateralAndSelect

  #### Parameters

  * ##### field: \[Field, [RawQueryFragment](https://mikro-orm.io/api/core/class/RawQueryFragment.md)\<string> | [QueryBuilder](https://mikro-orm.io/api/sql/class/QueryBuilder.md)\<any, never, never, never, never, \*, {}>]

  * ##### alias: Alias

  * ##### cond: JoinCondition<[ExpandProperty](https://mikro-orm.io/api/core.md#ExpandProperty)\<GetType\<Entity, Context, Field>\[GetPropName\<Field> & keyof<!-- --> GetType\<Entity, Context, Field>]>, Alias> = <!-- -->

  * ##### optionalfields: JoinFields

  * ##### optionalschema: string

  #### Returns [SelectQueryBuilder](https://mikro-orm.io/api/sql/interface/SelectQueryBuilder.md)\<Entity, RootAlias, [ModifyHint](https://mikro-orm.io/api/sql.md#ModifyHint)\<RootAlias, Context, Hint, Field, true> & {}, [ModifyContext](https://mikro-orm.io/api/sql.md#ModifyContext)\<Entity, Context, Field, Alias, true>, never, [ModifyFields](https://mikro-orm.io/api/sql.md#ModifyFields)<\*, RootAlias, Context, Field, Alias, JoinFields>, {}>

### [**](#insert)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/oracledb/src/OracleQueryBuilder.ts#L19)insert

* ****insert**(data): [InsertQueryBuilder](https://mikro-orm.io/api/sql/interface/InsertQueryBuilder.md)\<Entity, RootAlias, Context>

* Overrides QueryBuilder.insert

  Creates an INSERT query with the given data.

  * **@example**

    ```
    await em.createQueryBuilder(User)
      .insert({ name: 'John', email: 'john@example.com' })
      .execute();

    // Bulk insert
    await em.createQueryBuilder(User)
      .insert([{ name: 'John' }, { name: 'Jane' }])
      .execute();
    ```

  ***

  #### Parameters

  * ##### data: [RequiredEntityData](https://mikro-orm.io/api/core.md#RequiredEntityData)\<Entity> | [RequiredEntityData](https://mikro-orm.io/api/core.md#RequiredEntityData)\<Entity>\[]

  #### Returns [InsertQueryBuilder](https://mikro-orm.io/api/sql/interface/InsertQueryBuilder.md)\<Entity, RootAlias, Context>

### [**](#join)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L930)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L950)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L959)inheritedjoin

* ****join**\<Field, Alias>(field, alias, cond, type, path, schema): [SelectQueryBuilder](https://mikro-orm.io/api/sql/interface/SelectQueryBuilder.md)\<Entity, RootAlias, Hint, [ModifyContext](https://mikro-orm.io/api/sql.md#ModifyContext)\<Entity, Context, Field, Alias, false>, never, \*, {}>
* ****join**\<Alias>(field, alias, cond, type, path, schema): [SelectQueryBuilder](https://mikro-orm.io/api/sql/interface/SelectQueryBuilder.md)\<Entity, RootAlias, Hint, [ModifyContext](https://mikro-orm.io/api/sql.md#ModifyContext)\<Entity, Context, string, Alias, false>, never, \*, {}>

* Inherited from QueryBuilder.join

  Adds a JOIN clause to the query for an entity relation.

  * **@example**

    ```
    const qb = em.createQueryBuilder(Book, 'b');
    qb.select('*')
      .join('b.author', 'a')
      .where({ 'a.name': 'John' });
    ```

  ***

  #### Parameters

  * ##### field: Field

  * ##### alias: Alias

  * ##### optionalcond: JoinCondition<[ExpandProperty](https://mikro-orm.io/api/core.md#ExpandProperty)\<GetType\<Entity, Context, Field>\[GetPropName\<Field> & keyof<!-- --> GetType\<Entity, Context, Field>]>, Alias>

  * ##### optionaltype: [JoinType](https://mikro-orm.io/api/sql/enum/JoinType.md)

  * ##### optionalpath: string

  * ##### optionalschema: string

  #### Returns [SelectQueryBuilder](https://mikro-orm.io/api/sql/interface/SelectQueryBuilder.md)\<Entity, RootAlias, Hint, [ModifyContext](https://mikro-orm.io/api/sql.md#ModifyContext)\<Entity, Context, Field, Alias, false>, never, \*, {}>

### [**](#joinAndSelect)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L1100)inheritedjoinAndSelect

* ****joinAndSelect**\<Field, Alias, JoinFields>(field, alias, cond, type, path, fields, schema): [SelectQueryBuilder](https://mikro-orm.io/api/sql/interface/SelectQueryBuilder.md)\<Entity, RootAlias, [ModifyHint](https://mikro-orm.io/api/sql.md#ModifyHint)\<RootAlias, Context, Hint, Field, true> & {}, [ModifyContext](https://mikro-orm.io/api/sql.md#ModifyContext)\<Entity, Context, Field, Alias, true>, never, [ModifyFields](https://mikro-orm.io/api/sql.md#ModifyFields)<\*, RootAlias, Context, Field, Alias, JoinFields>, {}>

* Inherited from QueryBuilder.joinAndSelect

  Adds a JOIN clause and automatically selects the joined entity's fields. This is useful for eager loading related entities.

  * **@example**

    ```
    const qb = em.createQueryBuilder(Book, 'b');
    qb.select('*')
      .joinAndSelect('b.author', 'a')
      .where({ 'a.name': 'John' });
    ```

  ***

  #### Parameters

  * ##### field: Field | \[Field, [RawQueryFragment](https://mikro-orm.io/api/core/class/RawQueryFragment.md)\<string> | [QueryBuilder](https://mikro-orm.io/api/sql/class/QueryBuilder.md)\<any, never, never, never, never, \*, {}>]

  * ##### alias: Alias

  * ##### cond: JoinCondition<[ExpandProperty](https://mikro-orm.io/api/core.md#ExpandProperty)\<GetType\<Entity, Context, Field>\[GetPropName\<Field> & keyof<!-- --> GetType\<Entity, Context, Field>]>, Alias> = <!-- -->

  * ##### type: [JoinType](https://mikro-orm.io/api/sql/enum/JoinType.md) = <!-- -->JoinType.innerJoin

  * ##### optionalpath: string

  * ##### optionalfields: JoinFields

  * ##### optionalschema: string

  #### Returns [SelectQueryBuilder](https://mikro-orm.io/api/sql/interface/SelectQueryBuilder.md)\<Entity, RootAlias, [ModifyHint](https://mikro-orm.io/api/sql.md#ModifyHint)\<RootAlias, Context, Hint, Field, true> & {}, [ModifyContext](https://mikro-orm.io/api/sql.md#ModifyContext)\<Entity, Context, Field, Alias, true>, never, [ModifyFields](https://mikro-orm.io/api/sql.md#ModifyFields)<\*, RootAlias, Context, Field, Alias, JoinFields>, {}>

### [**](#leftJoin)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L1037)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L1055)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L1062)inheritedleftJoin

* ****leftJoin**\<Field, Alias>(field, alias, cond, schema): [SelectQueryBuilder](https://mikro-orm.io/api/sql/interface/SelectQueryBuilder.md)\<Entity, RootAlias, Hint, [ModifyContext](https://mikro-orm.io/api/sql.md#ModifyContext)\<Entity, Context, Field, Alias, false>, never, \*, {}>
* ****leftJoin**\<Alias>(field, alias, cond, schema): [SelectQueryBuilder](https://mikro-orm.io/api/sql/interface/SelectQueryBuilder.md)\<Entity, RootAlias, Hint, [ModifyContext](https://mikro-orm.io/api/sql.md#ModifyContext)\<Entity, Context, string, Alias, false>, never, \*, {}>

* Inherited from QueryBuilder.leftJoin

  Adds a LEFT JOIN clause to the query for an entity relation.

  ***

  #### Parameters

  * ##### field: Field

  * ##### alias: Alias

  * ##### optionalcond: JoinCondition<[ExpandProperty](https://mikro-orm.io/api/core.md#ExpandProperty)\<GetType\<Entity, Context, Field>\[GetPropName\<Field> & keyof<!-- --> GetType\<Entity, Context, Field>]>, Alias>

  * ##### optionalschema: string

  #### Returns [SelectQueryBuilder](https://mikro-orm.io/api/sql/interface/SelectQueryBuilder.md)\<Entity, RootAlias, Hint, [ModifyContext](https://mikro-orm.io/api/sql.md#ModifyContext)\<Entity, Context, Field, Alias, false>, never, \*, {}>

### [**](#leftJoinAndSelect)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L1164)inheritedleftJoinAndSelect

* ****leftJoinAndSelect**\<Field, Alias, JoinFields>(field, alias, cond, fields, schema): [SelectQueryBuilder](https://mikro-orm.io/api/sql/interface/SelectQueryBuilder.md)\<Entity, RootAlias, [ModifyHint](https://mikro-orm.io/api/sql.md#ModifyHint)\<RootAlias, Context, Hint, Field, true> & {}, [ModifyContext](https://mikro-orm.io/api/sql.md#ModifyContext)\<Entity, Context, Field, Alias, true>, never, [ModifyFields](https://mikro-orm.io/api/sql.md#ModifyFields)<\*, RootAlias, Context, Field, Alias, JoinFields>, {}>

* Inherited from QueryBuilder.leftJoinAndSelect

  #### Parameters

  * ##### field: Field | \[Field, [RawQueryFragment](https://mikro-orm.io/api/core/class/RawQueryFragment.md)\<string> | [QueryBuilder](https://mikro-orm.io/api/sql/class/QueryBuilder.md)\<any, never, never, never, never, \*, {}>]

  * ##### alias: Alias

  * ##### cond: JoinCondition<[ExpandProperty](https://mikro-orm.io/api/core.md#ExpandProperty)\<GetType\<Entity, Context, Field>\[GetPropName\<Field> & keyof<!-- --> GetType\<Entity, Context, Field>]>, Alias> = <!-- -->

  * ##### optionalfields: JoinFields

  * ##### optionalschema: string

  #### Returns [SelectQueryBuilder](https://mikro-orm.io/api/sql/interface/SelectQueryBuilder.md)\<Entity, RootAlias, [ModifyHint](https://mikro-orm.io/api/sql.md#ModifyHint)\<RootAlias, Context, Hint, Field, true> & {}, [ModifyContext](https://mikro-orm.io/api/sql.md#ModifyContext)\<Entity, Context, Field, Alias, true>, never, [ModifyFields](https://mikro-orm.io/api/sql.md#ModifyFields)<\*, RootAlias, Context, Field, Alias, JoinFields>, {}>

### [**](#leftJoinLateral)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L1079)inheritedleftJoinLateral

* ****leftJoinLateral**\<Alias>(field, alias, cond, schema): [SelectQueryBuilder](https://mikro-orm.io/api/sql/interface/SelectQueryBuilder.md)\<Entity, RootAlias, Hint, [ModifyContext](https://mikro-orm.io/api/sql.md#ModifyContext)\<Entity, Context, string, Alias, false>, never, \*, {}>

* Inherited from QueryBuilder.leftJoinLateral

  #### Parameters

  * ##### field: [RawQueryFragment](https://mikro-orm.io/api/core/class/RawQueryFragment.md)\<string> | [QueryBuilder](https://mikro-orm.io/api/sql/class/QueryBuilder.md)\<any, never, never, never, never, \*, {}>

  * ##### alias: Alias

  * ##### cond: RawJoinCondition = <!-- -->{}

  * ##### optionalschema: string

  #### Returns [SelectQueryBuilder](https://mikro-orm.io/api/sql/interface/SelectQueryBuilder.md)\<Entity, RootAlias, Hint, [ModifyContext](https://mikro-orm.io/api/sql.md#ModifyContext)\<Entity, Context, string, Alias, false>, never, \*, {}>

### [**](#leftJoinLateralAndSelect)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L1194)inheritedleftJoinLateralAndSelect

* ****leftJoinLateralAndSelect**\<Field, Alias, JoinFields>(field, alias, cond, fields, schema): [SelectQueryBuilder](https://mikro-orm.io/api/sql/interface/SelectQueryBuilder.md)\<Entity, RootAlias, [ModifyHint](https://mikro-orm.io/api/sql.md#ModifyHint)\<RootAlias, Context, Hint, Field, true> & {}, [ModifyContext](https://mikro-orm.io/api/sql.md#ModifyContext)\<Entity, Context, Field, Alias, true>, never, [ModifyFields](https://mikro-orm.io/api/sql.md#ModifyFields)<\*, RootAlias, Context, Field, Alias, JoinFields>, {}>

* Inherited from QueryBuilder.leftJoinLateralAndSelect

  #### Parameters

  * ##### field: \[Field, [RawQueryFragment](https://mikro-orm.io/api/core/class/RawQueryFragment.md)\<string> | [QueryBuilder](https://mikro-orm.io/api/sql/class/QueryBuilder.md)\<any, never, never, never, never, \*, {}>]

  * ##### alias: Alias

  * ##### cond: JoinCondition<[ExpandProperty](https://mikro-orm.io/api/core.md#ExpandProperty)\<GetType\<Entity, Context, Field>\[GetPropName\<Field> & keyof<!-- --> GetType\<Entity, Context, Field>]>, Alias> = <!-- -->

  * ##### optionalfields: JoinFields

  * ##### optionalschema: string

  #### Returns [SelectQueryBuilder](https://mikro-orm.io/api/sql/interface/SelectQueryBuilder.md)\<Entity, RootAlias, [ModifyHint](https://mikro-orm.io/api/sql.md#ModifyHint)\<RootAlias, Context, Hint, Field, true> & {}, [ModifyContext](https://mikro-orm.io/api/sql.md#ModifyContext)\<Entity, Context, Field, Alias, true>, never, [ModifyFields](https://mikro-orm.io/api/sql.md#ModifyFields)<\*, RootAlias, Context, Field, Alias, JoinFields>, {}>

### [**](#limit)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L1891)inheritedlimit

* ****limit**(limit, offset): [SelectQueryBuilder](https://mikro-orm.io/api/sql/interface/SelectQueryBuilder.md)\<Entity, RootAlias, Hint, Context, never, \*, {}>

* Inherited from QueryBuilder.limit

  Sets a LIMIT clause to restrict the number of results.

  * **@example**

    ```
    qb.select('*').limit(10);        // First 10 results
    qb.select('*').limit(10, 20);    // 10 results starting from offset 20
    ```

  ***

  #### Parameters

  * ##### optionallimit: number

  * ##### offset: number = <!-- -->0

  #### Returns [SelectQueryBuilder](https://mikro-orm.io/api/sql/interface/SelectQueryBuilder.md)\<Entity, RootAlias, Hint, Context, never, \*, {}>

### [**](#merge)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L1844)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L1845)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L1846)inheritedmerge

* ****merge**\<P>(data): this
* ****merge**\<F>(data): this

* Inherited from QueryBuilder.merge

  #### Parameters

  * ##### data: readonly<!-- --> NestedAutoPath\<Entity, RootAlias, Context, P>\[]

  #### Returns this

### [**](#offset)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L1910)inheritedoffset

* ****offset**(offset): [SelectQueryBuilder](https://mikro-orm.io/api/sql/interface/SelectQueryBuilder.md)\<Entity, RootAlias, Hint, Context, never, \*, {}>

* Inherited from QueryBuilder.offset

  Sets an OFFSET clause to skip a number of results.

  * **@example**

    ```
    qb.select('*').limit(10).offset(20);  // Results 21-30
    ```

  ***

  #### Parameters

  * ##### optionaloffset: number

  #### Returns [SelectQueryBuilder](https://mikro-orm.io/api/sql/interface/SelectQueryBuilder.md)\<Entity, RootAlias, Hint, Context, never, \*, {}>

### [**](#onConflict)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L1817)inheritedonConflict

* ****onConflict**\<F>(fields): [InsertQueryBuilder](https://mikro-orm.io/api/sql/interface/InsertQueryBuilder.md)\<Entity, RootAlias, Context>

* Inherited from QueryBuilder.onConflict

  #### Parameters

  * ##### fields: [RawQueryFragment](https://mikro-orm.io/api/core/class/RawQueryFragment.md)\<string> | F | F\[] = <!-- -->

  #### Returns [InsertQueryBuilder](https://mikro-orm.io/api/sql/interface/InsertQueryBuilder.md)\<Entity, RootAlias, Context>

### [**](#orderBy)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L1588)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L1604)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L1613)inheritedorderBy

* ****orderBy**(orderBy): [SelectQueryBuilder](https://mikro-orm.io/api/sql/interface/SelectQueryBuilder.md)\<Entity, RootAlias, Hint, Context, never, \*, {}>
* ****orderBy**\<T>(orderBy): [SelectQueryBuilder](https://mikro-orm.io/api/sql/interface/SelectQueryBuilder.md)\<Entity, RootAlias, Hint, Context, never, \*, {}>

* Inherited from QueryBuilder.orderBy

  Adds an ORDER BY clause to the query, replacing any existing order.

  * **@example**

    ```
    qb.orderBy({ name: 'asc', createdAt: 'desc' });
    qb.orderBy([{ name: 'asc' }, { createdAt: 'desc' }]);
    qb.orderBy({ profile: { bio: 'asc' } }); // nested via object
    qb.orderBy({ 'profile.bio': 'asc' }); // nested via dot notation
    ```

  ***

  #### Parameters

  * ##### orderBy: [ContextOrderByMap](https://mikro-orm.io/api/sql.md#ContextOrderByMap)\<Entity, RootAlias, Context, never> | [ContextOrderByMap](https://mikro-orm.io/api/sql.md#ContextOrderByMap)\<Entity, RootAlias, Context, never>\[]

  #### Returns [SelectQueryBuilder](https://mikro-orm.io/api/sql/interface/SelectQueryBuilder.md)\<Entity, RootAlias, Hint, Context, never, \*, {}>

### [**](#orHaving)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L1810)inheritedorHaving

* ****orHaving**(cond, params): [SelectQueryBuilder](https://mikro-orm.io/api/sql/interface/SelectQueryBuilder.md)\<Entity, RootAlias, Hint, Context, never, \*, {}>

* Inherited from QueryBuilder.orHaving

  #### Parameters

  * ##### optionalcond: string | [QBFilterQuery](https://mikro-orm.io/api/sql.md#QBFilterQuery)\<Entity, RootAlias, Context, never>

  * ##### optionalparams: any\[]

  #### Returns [SelectQueryBuilder](https://mikro-orm.io/api/sql/interface/SelectQueryBuilder.md)\<Entity, RootAlias, Hint, Context, never, \*, {}>

### [**](#orWhere)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L1560)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L1569)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L1570)inheritedorWhere

* ****orWhere**(cond): this
* ****orWhere**(cond, params): this

* Inherited from QueryBuilder.orWhere

  Adds an OR WHERE clause to the query using an object condition.

  * **@example**

    ```
    qb.where({ status: 'active' }).orWhere({ role: 'admin' });
    qb.where({ name: 'John' }).orWhere({ name: 'Jane' });
    ```

  ***

  #### Parameters

  * ##### cond: [QBFilterQuery](https://mikro-orm.io/api/sql.md#QBFilterQuery)\<Entity, RootAlias, Context, never>

  #### Returns this

### [**](#returning)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L1861)inheritedreturning

* ****returning**\<F>(fields): this

* Inherited from QueryBuilder.returning

  #### Parameters

  * ##### optionalfields: F | F\[]

  #### Returns this

### [**](#select)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L668)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L696)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L710)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L730)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L742)inheritedselect

* ****select**\<F>(fields, distinct): [SelectQueryBuilder](https://mikro-orm.io/api/sql/interface/SelectQueryBuilder.md)\<Entity, RootAlias, Hint, Context, ExtractRawAliases\<F>, ExtractRootFields\<F\[number] & string, RootAlias, Context>, {}>
* ****select**\<P>(fields, distinct): [SelectQueryBuilder](https://mikro-orm.io/api/sql/interface/SelectQueryBuilder.md)\<Entity, RootAlias, Hint, Context, never, ExtractRootFields\<P, RootAlias, Context>, {}>
* ****select**\<P>(fields, distinct): [SelectQueryBuilder](https://mikro-orm.io/api/sql/interface/SelectQueryBuilder.md)\<Entity, RootAlias, Hint, Context, never, ExtractRootFields\<P, RootAlias, Context>, {}>
* ****select**\<F>(fields, distinct): [SelectQueryBuilder](https://mikro-orm.io/api/sql/interface/SelectQueryBuilder.md)\<Entity, RootAlias, Hint, Context, ExtractRawAliasFromField\<F>, ExtractRootFields\<F & string, RootAlias, Context>, {}>

* Inherited from QueryBuilder.select

  Creates a SELECT query, specifying the fields to retrieve.

  * **@example**

    ```
    // Select specific fields
    const qb = em.createQueryBuilder(User, 'u');
    qb.select(['u.id', 'u.name', 'u.email']);

    // Select with raw expressions
    qb.select([raw('count(*) as total')]);

    // Select with aliases (works for regular and formula properties)
    qb.select(['id', 'fullName as displayName']);
    qb.select(['id', sql.ref('fullName').as('displayName')]);

    // Select with distinct
    qb.select('*', true);
    ```

  ***

  #### Parameters

  * ##### fields: F

  * ##### optionaldistinct: boolean

  #### Returns [SelectQueryBuilder](https://mikro-orm.io/api/sql/interface/SelectQueryBuilder.md)\<Entity, RootAlias, Hint, Context, ExtractRawAliases\<F>, ExtractRootFields\<F\[number] & string, RootAlias, Context>, {}>

### [**](#setFlag)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L1942)inheritedsetFlag

* ****setFlag**(flag): this

* Inherited from QueryBuilder.setFlag

  #### Parameters

  * ##### flag: [QueryFlag](https://mikro-orm.io/api/core/enum/QueryFlag.md)

  #### Returns this

### [**](#setFlushMode)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L1936)inheritedsetFlushMode

* ****setFlushMode**(flushMode): this

* Inherited from QueryBuilder.setFlushMode

  #### Parameters

  * ##### optionalflushMode: [FlushMode](https://mikro-orm.io/api/core/enum/FlushMode.md)

  #### Returns this

### [**](#setlockmode)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/oracledb/src/OracleQueryBuilder.ts#L32)setLockMode

* ****setLockMode**(mode, tables): this

* Overrides QueryBuilder.setLockMode

  #### Parameters

  * ##### optionalmode: [LockMode](https://mikro-orm.io/api/core/enum/LockMode.md)

  * ##### optionaltables: string\[]

  #### Returns this

### [**](#setLoggerContext)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L2819)inheritedsetLoggerContext

* ****setLoggerContext**(context): void

* Inherited from QueryBuilder.setLoggerContext

  Sets logger context for this query builder.

  ***

  #### Parameters

  * ##### context: [LoggingOptions](https://mikro-orm.io/api/core.md#LoggingOptions) & [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)

  #### Returns void

### [**](#stream)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L2419)inheritedstream

* ****stream**(options): AsyncIterableIterator<[Loaded](https://mikro-orm.io/api/core.md#Loaded)\<Entity, Hint, \*>, any, any>

* Inherited from QueryBuilder.stream

  Executes the query and returns an async iterable (async generator) that yields results one by one. By default, the results are merged and mapped to entity instances, without adding them to the identity map. You can disable merging and mapping by passing the options `{ mergeResults: false, mapResults: false }`. This is useful for processing large datasets without loading everything into memory at once.

  ```
  const qb = em.createQueryBuilder(Book, 'b');
  qb.select('*').where({ title: '1984' }).leftJoinAndSelect('b.author', 'a');

  for await (const book of qb.stream()) {
    // book is an instance of Book entity
    console.log(book.title, book.author.name);
  }
  ```

  ***

  #### Parameters

  * ##### optionaloptions: [QBStreamOptions](https://mikro-orm.io/api/sql/interface/QBStreamOptions.md)

  #### Returns AsyncIterableIterator<[Loaded](https://mikro-orm.io/api/core.md#Loaded)\<Entity, Hint, \*>, any, any>

### [**](#toQuery)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L2194)inheritedtoQuery

* ****toQuery**(): { params: readonly
  <!-- -->
  unknown\[]; sql: string }

* Inherited from QueryBuilder.toQuery

  #### Returns { params: readonly<!-- --> unknown\[]; sql: string }

  * ##### params: readonly<!-- --> unknown\[]

  * ##### sql: string

### [**](#toRaw)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L2189)inheritedtoRaw

* ****toRaw**(): [RawQueryFragment](https://mikro-orm.io/api/core/class/RawQueryFragment.md)\<string>

* Inherited from QueryBuilder.toRaw

  Returns raw fragment representation of this QueryBuilder.

  ***

  #### Returns [RawQueryFragment](https://mikro-orm.io/api/core/class/RawQueryFragment.md)\<string>

### [**](#truncate)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L888)inheritedtruncate

* ****truncate**(): [TruncateQueryBuilder](https://mikro-orm.io/api/sql/interface/TruncateQueryBuilder.md)\<Entity>

* Inherited from QueryBuilder.truncate

  Creates a TRUNCATE query to remove all rows from the table.

  ***

  #### Returns [TruncateQueryBuilder](https://mikro-orm.io/api/sql/interface/TruncateQueryBuilder.md)\<Entity>

### [**](#union)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L2647)inheritedunion

* ****union**(...others): [QueryBuilder](https://mikro-orm.io/api/sql/class/QueryBuilder.md)\<Entity, never, never, never, never, \*, {}>

* Inherited from QueryBuilder.union

  Combines the current query with one or more other queries using `UNION` (with deduplication). All queries must select the same columns. Returns a `QueryBuilder` that can be used with `$in`, passed to `qb.from()`, or converted via `.getQuery()`, `.getParams()`, `.toQuery()`, `.toRaw()`, etc.

  ```
  const qb1 = em.createQueryBuilder(Employee).select('id').where(condition1);
  const qb2 = em.createQueryBuilder(Employee).select('id').where(condition2);
  const subquery = qb1.union(qb2);

  const results = await em.find(Employee, { id: { $in: subquery } });
  ```

  ***

  #### Parameters

  * ##### rest...others: (NativeQueryBuilder | [QueryBuilder](https://mikro-orm.io/api/sql/class/QueryBuilder.md)\<any, never, never, never, never, \*, {}>)\[]

  #### Returns [QueryBuilder](https://mikro-orm.io/api/sql/class/QueryBuilder.md)\<Entity, never, never, never, never, \*, {}>

### [**](#unionAll)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L2629)inheritedunionAll

* ****unionAll**(...others): [QueryBuilder](https://mikro-orm.io/api/sql/class/QueryBuilder.md)\<Entity, never, never, never, never, \*, {}>

* Inherited from QueryBuilder.unionAll

  Combines the current query with one or more other queries using `UNION ALL`. All queries must select the same columns. Returns a `QueryBuilder` that can be used with `$in`, passed to `qb.from()`, or converted via `.getQuery()`, `.getParams()`, `.toQuery()`, `.toRaw()`, etc.

  ```
  const qb1 = em.createQueryBuilder(Employee).select('id').where(condition1);
  const qb2 = em.createQueryBuilder(Employee).select('id').where(condition2);
  const qb3 = em.createQueryBuilder(Employee).select('id').where(condition3);
  const subquery = qb1.unionAll(qb2, qb3);

  const results = await em.find(Employee, { id: { $in: subquery } });
  ```

  ***

  #### Parameters

  * ##### rest...others: (NativeQueryBuilder | [QueryBuilder](https://mikro-orm.io/api/sql/class/QueryBuilder.md)\<any, never, never, never, never, \*, {}>)\[]

  #### Returns [QueryBuilder](https://mikro-orm.io/api/sql/class/QueryBuilder.md)\<Entity, never, never, never, never, \*, {}>

### [**](#unsetFlag)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L1948)inheritedunsetFlag

* ****unsetFlag**(flag): this

* Inherited from QueryBuilder.unsetFlag

  #### Parameters

  * ##### flag: [QueryFlag](https://mikro-orm.io/api/core/enum/QueryFlag.md)

  #### Returns this

### [**](#update)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L860)inheritedupdate

* ****update**(data): [UpdateQueryBuilder](https://mikro-orm.io/api/sql/interface/UpdateQueryBuilder.md)\<Entity, RootAlias, Context>

* Inherited from QueryBuilder.update

  Creates an UPDATE query with the given data. Use `where()` to specify which rows to update.

  * **@example**

    ```
    await em.createQueryBuilder(User)
      .update({ name: 'John Doe' })
      .where({ id: 1 })
      .execute();
    ```

  ***

  #### Parameters

  * ##### data: [EntityData](https://mikro-orm.io/api/core.md#EntityData)\<Entity>

  #### Returns [UpdateQueryBuilder](https://mikro-orm.io/api/sql/interface/UpdateQueryBuilder.md)\<Entity, RootAlias, Context>

### [**](#where)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L1445)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L1458)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L1459)inheritedwhere

* ****where**(cond, operator): this
* ****where**(cond, params, operator): this

* Inherited from QueryBuilder.where

  Adds a WHERE clause to the query using an object condition.

  Supports filtering by:

  * Direct entity properties: `{ name: 'John' }`
  * Nested relations/embedded: `{ author: { name: 'John' } }`
  * Aliased properties after joins: `{ 'a.name': 'John' }` or `{ 'b.title': 'test' }`
  * Filter operators: `{ age: { $gte: 18 } }`
  * Logical operators: `{ $or: [{ name: 'John' }, { name: 'Jane' }] }`

  * **@example**

    ```
    // Filter by entity properties
    qb.where({ name: 'John', age: { $gte: 18 } });

    // Filter by nested relation
    qb.where({ author: { name: 'John' } });

    // Filter by aliased properties after join
    qb.leftJoin('a.books', 'b').where({ 'b.title': 'test' });

    // Combine with logical operators
    qb.where({ $or: [{ status: 'active' }, { role: 'admin' }] });
    ```

  ***

  #### Parameters

  * ##### cond: [QBFilterQuery](https://mikro-orm.io/api/sql.md#QBFilterQuery)\<Entity, RootAlias, Context, never>

  * ##### optionaloperator: $and | $or

  #### Returns this

### [**](#with)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L2683)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L2700)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L2705)inheritedwith

* ****with**\<Name, Q>(name, query, options): [QueryBuilder](https://mikro-orm.io/api/sql/class/QueryBuilder.md)\<Entity, RootAlias, Hint, Context, never, \*, Record\<Name, Q extends [QueryBuilder](https://mikro-orm.io/api/sql/class/QueryBuilder.md)\<T, never, never, never, never, \*, {}> ? T : object>>
* ****with**\<Name>(name, query, options): [QueryBuilder](https://mikro-orm.io/api/sql/class/QueryBuilder.md)\<Entity, RootAlias, Hint, Context, never, \*, Record\<Name, object>>

* Inherited from QueryBuilder.with

  Adds a Common Table Expression (CTE) to the query. When a `QueryBuilder` is passed, its entity type is tracked for type-safe `from()`.

  * **@example**

    ```
    const recentBooks = em.createQueryBuilder(Book, 'b').select('*').where({ ... });
    const qb = em.createQueryBuilder(Author, 'a')
      .with('recent_books', recentBooks)
      .select('*')
      .from('recent_books', 'rb'); // entity type inferred as Book
    ```

  ***

  #### Parameters

  * ##### name: Name

  * ##### query: Q

  * ##### optionaloptions: [CteOptions](https://mikro-orm.io/api/sql/interface/CteOptions.md)

  #### Returns [QueryBuilder](https://mikro-orm.io/api/sql/class/QueryBuilder.md)\<Entity, RootAlias, Hint, Context, never, \*, Record\<Name, Q extends [QueryBuilder](https://mikro-orm.io/api/sql/class/QueryBuilder.md)\<T, never, never, never, never, \*, {}> ? T : object>>

### [**](#withRecursive)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L2724)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L2741)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L2746)inheritedwithRecursive

* ****withRecursive**\<Name, Q>(name, query, options): [QueryBuilder](https://mikro-orm.io/api/sql/class/QueryBuilder.md)\<Entity, RootAlias, Hint, Context, never, \*, Record\<Name, Q extends [QueryBuilder](https://mikro-orm.io/api/sql/class/QueryBuilder.md)\<T, never, never, never, never, \*, {}> ? T : object>>
* ****withRecursive**\<Name>(name, query, options): [QueryBuilder](https://mikro-orm.io/api/sql/class/QueryBuilder.md)\<Entity, RootAlias, Hint, Context, never, \*, Record\<Name, object>>

* Inherited from QueryBuilder.withRecursive

  Adds a recursive Common Table Expression (CTE) to the query. When a `QueryBuilder` is passed, its entity type is tracked for type-safe `from()`.

  * **@example**

    ```
    const base = em.createQueryBuilder(Category).select('*').where({ parent: null });
    const rec = em.createQueryBuilder(Category, 'c').select('c.*')
      .leftJoin('c.parent', 'ct', { id: sql.ref('c.parentId') });
    const qb = em.createQueryBuilder(Category)
      .withRecursive('category_tree', base.unionAll(rec))
      .select('*')
      .from('category_tree', 'ct'); // entity type inferred as Category
    ```

  ***

  #### Parameters

  * ##### name: Name

  * ##### query: Q

  * ##### optionaloptions: [CteOptions](https://mikro-orm.io/api/sql/interface/CteOptions.md)

  #### Returns [QueryBuilder](https://mikro-orm.io/api/sql/class/QueryBuilder.md)\<Entity, RootAlias, Hint, Context, never, \*, Record\<Name, Q extends [QueryBuilder](https://mikro-orm.io/api/sql/class/QueryBuilder.md)\<T, never, never, never, never, \*, {}> ? T : object>>

### [**](#withSchema)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L1916)inheritedwithSchema

* ****withSchema**(schema): this

* Inherited from QueryBuilder.withSchema

  #### Parameters

  * ##### optionalschema: string

  #### Returns this

### [**](#withSubQuery)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L1408)inheritedwithSubQuery

* ****withSubQuery**(subQuery, alias): this

* Inherited from QueryBuilder.withSubQuery

  #### Parameters

  * ##### subQuery: [RawQueryFragment](https://mikro-orm.io/api/core/class/RawQueryFragment.md)\<string> | NativeQueryBuilder

  * ##### alias: string

  #### Returns this
