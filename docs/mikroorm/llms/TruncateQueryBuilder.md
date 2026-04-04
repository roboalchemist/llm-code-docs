# Source: https://mikro-orm.io/api/sql/interface/TruncateQueryBuilder.md

# TruncateQueryBuilder<!-- --> \<T>

### Hierarchy

* [RunQueryBuilder](https://mikro-orm.io/api/sql/interface/RunQueryBuilder.md)\<T>
  * *TruncateQueryBuilder*

## Index[**](#index)

### Properties

* [**\_\_subquery](#__subquery)
* [**alias](#alias)
* [**helper](#helper)
* [**mainAlias](#mainAlias)
* [**state](#state)
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
* [**getNativeQuery](#getNativeQuery)
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

Inherited from RunQueryBuilder.\_\_subquery

### [**](#alias)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L604)inheritedalias

**alias: string

Inherited from RunQueryBuilder.alias

### [**](#helper)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L608)inheritedhelper

**helper: QueryBuilderHelper

Inherited from RunQueryBuilder.helper

### [**](#mainAlias)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L599)inheritedmainAlias

**mainAlias: [Alias](https://mikro-orm.io/api/sql/interface/Alias.md)\<T>

Inherited from RunQueryBuilder.mainAlias

### [**](#state)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L618)inheritedstate

**state: QBState\<T>

Inherited from RunQueryBuilder.state

### [**](#type)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L613)inheritedtype

**type: [QueryType](https://mikro-orm.io/api/sql/enum/QueryType.md)

Inherited from RunQueryBuilder.type

## Methods<!-- -->[**](#methods)

### [**](#addSelect)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L780)inheritedaddSelect

* ****addSelect**\<F>(fields): [SelectQueryBuilder](https://mikro-orm.io/api/sql/interface/SelectQueryBuilder.md)\<T, never, never, never, ExtractRawAliases\<F extends readonly
  <!-- -->
  unknown\[] ? F\<F> : \[F]>, \* | ExtractRootFields\<F extends readonly
  <!-- -->
  U\[] ? U & string : F & string, never, never>, {}>

* Inherited from RunQueryBuilder.addSelect

  Adds fields to an existing SELECT query.

  ***

  #### Parameters

  * ##### fields: F

  #### Returns [SelectQueryBuilder](https://mikro-orm.io/api/sql/interface/SelectQueryBuilder.md)\<T, never, never, never, ExtractRawAliases\<F extends readonly<!-- --> unknown\[] ? F\<F> : \[F]>, \* | ExtractRootFields\<F extends readonly<!-- --> U\[] ? U & string : F & string, never, never>, {}>

### [**](#andHaving)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L1803)inheritedandHaving

* ****andHaving**(cond, params): [SelectQueryBuilder](https://mikro-orm.io/api/sql/interface/SelectQueryBuilder.md)\<T, never, never, never, never, \*, {}>

* Inherited from RunQueryBuilder.andHaving

  #### Parameters

  * ##### optionalcond: string | [QBFilterQuery](https://mikro-orm.io/api/sql.md#QBFilterQuery)\<T, never, never, never>

  * ##### optionalparams: any\[]

  #### Returns [SelectQueryBuilder](https://mikro-orm.io/api/sql/interface/SelectQueryBuilder.md)\<T, never, never, never, never, \*, {}>

### [**](#andOrderBy)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L1620)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L1628)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L1637)inheritedandOrderBy

* ****andOrderBy**(orderBy): [SelectQueryBuilder](https://mikro-orm.io/api/sql/interface/SelectQueryBuilder.md)\<T, never, never, never, never, \*, {}>
* ****andOrderBy**\<T>(orderBy): [SelectQueryBuilder](https://mikro-orm.io/api/sql/interface/SelectQueryBuilder.md)\<T, never, never, never, never, \*, {}>

* Inherited from RunQueryBuilder.andOrderBy

  Adds additional ORDER BY clause without replacing existing order.

  ***

  #### Parameters

  * ##### orderBy: [ContextOrderByMap](https://mikro-orm.io/api/sql.md#ContextOrderByMap)\<T, never, never, never> | [ContextOrderByMap](https://mikro-orm.io/api/sql.md#ContextOrderByMap)\<T, never, never, never>\[]

  #### Returns [SelectQueryBuilder](https://mikro-orm.io/api/sql/interface/SelectQueryBuilder.md)\<T, never, never, never, never, \*, {}>

### [**](#andWhere)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L1534)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L1543)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L1544)inheritedandWhere

* ****andWhere**(cond): this
* ****andWhere**(cond, params): this

* Inherited from RunQueryBuilder.andWhere

  Adds an AND WHERE clause to the query using an object condition.

  * **@example**

    ```
    qb.where({ status: 'active' }).andWhere({ role: 'admin' });
    qb.where({ name: 'John' }).andWhere({ 'b.title': 'test' });
    ```

  ***

  #### Parameters

  * ##### cond: [QBFilterQuery](https://mikro-orm.io/api/sql.md#QBFilterQuery)\<T, never, never, never>

  #### Returns this

### [**](#applyFilters)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L1346)inheritedapplyFilters

* ****applyFilters**(filterOptions): Promise\<void>

* Inherited from RunQueryBuilder.applyFilters

  Apply filters to the QB where condition.

  ***

  #### Parameters

  * ##### filterOptions: [FilterOptions](https://mikro-orm.io/api/core.md#FilterOptions) = <!-- -->{}

  #### Returns Promise\<void>

### [**](#as)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L2581)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L2587)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L2589)inheritedas

* ****as**(alias): NativeQueryBuilder
* ****as**\<T>(targetEntity, alias): NativeQueryBuilder

* Inherited from RunQueryBuilder.as

  Returns native query builder instance with sub-query aliased with given alias.

  ***

  #### Parameters

  * ##### alias: string

  #### Returns NativeQueryBuilder

### [**](#cache)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L1958)inheritedcache

* ****cache**(config): this

* Inherited from RunQueryBuilder.cache

  #### Parameters

  * ##### config: number | boolean | \[string, number] = <!-- -->true

  #### Returns this

### [**](#clone)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L2778)inheritedclone

* ****clone**(reset, preserve): [QueryBuilder](https://mikro-orm.io/api/sql/class/QueryBuilder.md)\<T, never, never, never, never, \*, {}>

* Inherited from RunQueryBuilder.clone

  #### Parameters

  * ##### optionalreset: boolean | keyof<!-- --> QBState\<Entity>\[]

  * ##### optionalpreserve: keyof<!-- --> QBState\<Entity>\[]

  #### Returns [QueryBuilder](https://mikro-orm.io/api/sql/class/QueryBuilder.md)\<T, never, never, never, never, \*, {}>

### [**](#collation)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L1976)inheritedcollation

* ****collation**(collation): this

* Inherited from RunQueryBuilder.collation

  Adds COLLATE clause to ORDER BY expressions.

  ***

  #### Parameters

  * ##### collation: undefined | string

  #### Returns this

### [**](#comment)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L1985)inheritedcomment

* ****comment**(comment): this

* Inherited from RunQueryBuilder.comment

  Prepend comment to the sql query using the syntax `/* ... *&#8205;/`. Some characters are forbidden such as `/*, *&#8205;/` and `?`.

  ***

  #### Parameters

  * ##### comment: undefined | string | string\[]

  #### Returns this

### [**](#count)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L903)inheritedcount

* ****count**\<F>(field, distinct): [CountQueryBuilder](https://mikro-orm.io/api/sql/interface/CountQueryBuilder.md)\<T>

* Inherited from RunQueryBuilder.count

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

  #### Returns [CountQueryBuilder](https://mikro-orm.io/api/sql/interface/CountQueryBuilder.md)\<T>

### [**](#delete)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L881)inheriteddelete

* ****delete**(cond): [DeleteQueryBuilder](https://mikro-orm.io/api/sql/interface/DeleteQueryBuilder.md)\<T, never, never>

* Inherited from RunQueryBuilder.delete

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

  * ##### optionalcond: [QBFilterQuery](https://mikro-orm.io/api/sql.md#QBFilterQuery)\<T, never, never, never>

  #### Returns [DeleteQueryBuilder](https://mikro-orm.io/api/sql/interface/DeleteQueryBuilder.md)\<T, never, never>

### [**](#distinct)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L800)inheriteddistinct

* ****distinct**(): [SelectQueryBuilder](https://mikro-orm.io/api/sql/interface/SelectQueryBuilder.md)\<T, never, never, never, never, \*, {}>

* Inherited from RunQueryBuilder.distinct

  #### Returns [SelectQueryBuilder](https://mikro-orm.io/api/sql/interface/SelectQueryBuilder.md)\<T, never, never, never, never, \*, {}>

### [**](#distinctOn)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L814)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L818)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L821)inheriteddistinctOn

* ****distinctOn**\<F>(fields): [SelectQueryBuilder](https://mikro-orm.io/api/sql/interface/SelectQueryBuilder.md)\<T, never, never, never, never, \*, {}>
* ****distinctOn**\<F>(fields): [SelectQueryBuilder](https://mikro-orm.io/api/sql/interface/SelectQueryBuilder.md)\<T, never, never, never, never, \*, {}>

* Inherited from RunQueryBuilder.distinctOn

  postgres only

  ***

  #### Parameters

  * ##### fields: F

  #### Returns [SelectQueryBuilder](https://mikro-orm.io/api/sql/interface/SelectQueryBuilder.md)\<T, never, never, never, never, \*, {}>

### [**](#execute)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L4093)inheritedexecute

* ****execute**\<Result>(method, mapResults): Promise\<Result>

* Inherited from RunQueryBuilder.execute

  Executes this QB and returns the raw results, mapped to the property names (unless disabled via last parameter). Use `method` to specify what kind of result you want to get (array/single/meta).

  ***

  #### Parameters

  * ##### optionalmethod: get | all | run

  * ##### optionalmapResults: boolean

  #### Returns Promise\<Result>

### [**](#from)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L2006)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L2014)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L2021)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L2025)inheritedfrom

* ****from**\<Entity>(target, aliasName): [SelectQueryBuilder](https://mikro-orm.io/api/sql/interface/SelectQueryBuilder.md)\<Entity, never, never, never, never, \*, {}>
* ****from**\<Entity>(target): [SelectQueryBuilder](https://mikro-orm.io/api/sql/interface/SelectQueryBuilder.md)\<Entity, never, never, never, never, \*, {}>
* ****from**\<Name, Alias>(target, aliasName): [SelectQueryBuilder](https://mikro-orm.io/api/sql/interface/SelectQueryBuilder.md)<{}\[Name], Alias, never, never, never, \*, {}>

* Inherited from RunQueryBuilder.from

  Specifies FROM which entity's table select/update/delete will be executed, removing all previously set FROM-s. Allows setting a main string alias of the selection data.

  ***

  #### Parameters

  * ##### target: [QueryBuilder](https://mikro-orm.io/api/sql/class/QueryBuilder.md)\<Entity, never, never, never, never, \*, {}>

  * ##### optionalaliasName: string

  #### Returns [SelectQueryBuilder](https://mikro-orm.io/api/sql/interface/SelectQueryBuilder.md)\<Entity, never, never, never, never, \*, {}>

### [**](#getCount)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L2544)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L2545)inheritedgetCount

* ****getCount**\<F>(field, distinct): Promise\<number>

* Inherited from RunQueryBuilder.getCount

  Executes count query (without offset and limit), returning total count of results

  ***

  #### Parameters

  * ##### optionalfield: F | F\[]

  * ##### optionaldistinct: boolean

  #### Returns Promise\<number>

### [**](#getFormattedQuery)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L2220)inheritedgetFormattedQuery

* ****getFormattedQuery**(): string

* Inherited from RunQueryBuilder.getFormattedQuery

  Returns raw interpolated query string with all the parameters inlined.

  ***

  #### Returns string

### [**](#getLoggerContext)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L2826)inheritedgetLoggerContext

* ****getLoggerContext**\<T>(): T

* Inherited from RunQueryBuilder.getLoggerContext

  Gets logger context for this query builder.

  ***

  #### Returns T

### [**](#getNativeQuery)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L2045)inheritedgetNativeQuery

* ****getNativeQuery**(processVirtualEntity): NativeQueryBuilder

* Inherited from RunQueryBuilder.getNativeQuery

  #### Parameters

  * ##### processVirtualEntity: boolean = <!-- -->true

  #### Returns NativeQueryBuilder

### [**](#getParams)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L2213)inheritedgetParams

* ****getParams**(): readonly
  <!-- -->
  unknown\[]

* Inherited from RunQueryBuilder.getParams

  Returns the list of all parameters for this query.

  ***

  #### Returns readonly<!-- --> unknown\[]

### [**](#getQuery)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L2182)inheritedgetQuery

* ****getQuery**(): string

* Inherited from RunQueryBuilder.getQuery

  Returns the query with parameters as wildcards.

  ***

  #### Returns string

### [**](#getResultAndCount)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L2574)inheritedgetResultAndCount

* ****getResultAndCount**(): Promise<\[[Loaded](https://mikro-orm.io/api/core.md#Loaded)\<T, never, \*>\[], number]>

* Inherited from RunQueryBuilder.getResultAndCount

  Executes the query, returning both array of results and total count query (without offset and limit).

  ***

  #### Returns Promise<\[[Loaded](https://mikro-orm.io/api/core.md#Loaded)\<T, never, \*>\[], number]>

### [**](#groupBy)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L1717)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L1729)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L1741)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L1744)inheritedgroupBy

* ****groupBy**\<F>(fields): [SelectQueryBuilder](https://mikro-orm.io/api/sql/interface/SelectQueryBuilder.md)\<T, never, never, never, never, \*, {}>
* ****groupBy**\<F>(fields): [SelectQueryBuilder](https://mikro-orm.io/api/sql/interface/SelectQueryBuilder.md)\<T, never, never, never, never, \*, {}>
* ****groupBy**\<P>(fields): [SelectQueryBuilder](https://mikro-orm.io/api/sql/interface/SelectQueryBuilder.md)\<T, never, never, never, never, \*, {}>

* Inherited from RunQueryBuilder.groupBy

  Adds a GROUP BY clause to the query.

  * **@example**

    ```
    qb.select([raw('count(*) as count'), 'status'])
      .groupBy('status');
    ```

  ***

  #### Parameters

  * ##### fields: F

  #### Returns [SelectQueryBuilder](https://mikro-orm.io/api/sql/interface/SelectQueryBuilder.md)\<T, never, never, never, never, \*, {}>

### [**](#hasFlag)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L1954)inheritedhasFlag

* ****hasFlag**(flag): boolean

* Inherited from RunQueryBuilder.hasFlag

  #### Parameters

  * ##### flag: [QueryFlag](https://mikro-orm.io/api/core/enum/QueryFlag.md)

  #### Returns boolean

### [**](#having)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L1773)inheritedhaving

* ****having**(cond, params, operator): [SelectQueryBuilder](https://mikro-orm.io/api/sql/interface/SelectQueryBuilder.md)\<T, never, never, never, never, \*, {}>

* Inherited from RunQueryBuilder.having

  Adds a HAVING clause to the query, typically used with GROUP BY.

  * **@example**

    ```
    qb.select([raw('count(*) as count'), 'status'])
      .groupBy('status')
      .having({ count: { $gt: 5 } });
    ```

  ***

  #### Parameters

  * ##### cond: string | [QBFilterQuery](https://mikro-orm.io/api/sql.md#QBFilterQuery)\<T, never, never, never> = <!-- -->{}

  * ##### optionalparams: any\[]

  * ##### optionaloperator: $and | $or

  #### Returns [SelectQueryBuilder](https://mikro-orm.io/api/sql/interface/SelectQueryBuilder.md)\<T, never, never, never, never, \*, {}>

### [**](#hintComment)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L1996)inheritedhintComment

* ****hintComment**(comment): this

* Inherited from RunQueryBuilder.hintComment

  Add hints to the query using comment-like syntax `/*+ ... *&#8205;/`. MySQL and Oracle use this syntax for optimizer hints. Also various DB proxies and routers use this syntax to pass hints to alter their behavior. In other dialects the hints are ignored as simple comments.

  ***

  #### Parameters

  * ##### comment: undefined | string | string\[]

  #### Returns this

### [**](#ignore)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L1835)inheritedignore

* ****ignore**(): this

* Inherited from RunQueryBuilder.ignore

  #### Returns this

### [**](#indexHint)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L1967)inheritedindexHint

* ****indexHint**(sql): this

* Inherited from RunQueryBuilder.indexHint

  Adds index hint to the FROM clause.

  ***

  #### Parameters

  * ##### sql: undefined | string

  #### Returns this

### [**](#innerJoin)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L982)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L1000)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L1007)inheritedinnerJoin

* ****innerJoin**\<Field, Alias>(field, alias, cond, schema): [SelectQueryBuilder](https://mikro-orm.io/api/sql/interface/SelectQueryBuilder.md)\<T, never, never, AddToContext\<GetType\<T, object, Field>, object, Field, Alias, false>, never, \*, {}>
* ****innerJoin**\<Alias>(field, alias, cond, schema): [SelectQueryBuilder](https://mikro-orm.io/api/sql/interface/SelectQueryBuilder.md)\<T, never, never, AddToContext\<T, object, string, Alias, false>, never, \*, {}>

* Inherited from RunQueryBuilder.innerJoin

  Adds an INNER JOIN clause to the query for an entity relation.

  ***

  #### Parameters

  * ##### field: Field

  * ##### alias: Alias

  * ##### optionalcond: JoinCondition<[ExpandProperty](https://mikro-orm.io/api/core.md#ExpandProperty)\<GetType\<T, never, Field>\[GetPropName\<Field> & keyof<!-- --> GetType\<T, never, Field>]>, Alias>

  * ##### optionalschema: string

  #### Returns [SelectQueryBuilder](https://mikro-orm.io/api/sql/interface/SelectQueryBuilder.md)\<T, never, never, AddToContext\<GetType\<T, object, Field>, object, Field, Alias, false>, never, \*, {}>

### [**](#innerJoinAndSelect)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L1225)inheritedinnerJoinAndSelect

* ****innerJoinAndSelect**\<Field, Alias, JoinFields>(field, alias, cond, fields, schema): [SelectQueryBuilder](https://mikro-orm.io/api/sql/interface/SelectQueryBuilder.md)\<T, never, (GetAlias\<Field> extends Alias ? IsNever\<Alias, true, false> extends true ? GetPropName\<Field> : Alias extends never ? GetPropName\<Field> : Alias extends string | number | symbol ? never\[Alias\<Alias>] extends \[Path, ...any\[]] ? \`${Path & string}.${GetPropName\<Field>}\` : GetPropName\<Field> : GetPropName\<Field> : GetPropName\<Field>) & {}, AddToContext\<GetType\<T, object, Field>, object, Field, Alias, true>, never, [ModifyFields](https://mikro-orm.io/api/sql.md#ModifyFields)<\*, never, never, Field, Alias, JoinFields>, {}>

* Inherited from RunQueryBuilder.innerJoinAndSelect

  #### Parameters

  * ##### field: Field | \[Field, [RawQueryFragment](https://mikro-orm.io/api/core/class/RawQueryFragment.md)\<string> | [QueryBuilder](https://mikro-orm.io/api/sql/class/QueryBuilder.md)\<any, never, never, never, never, \*, {}>]

  * ##### alias: Alias

  * ##### cond: JoinCondition<[ExpandProperty](https://mikro-orm.io/api/core.md#ExpandProperty)\<GetType\<T, never, Field>\[GetPropName\<Field> & keyof<!-- --> GetType\<T, never, Field>]>, Alias> = <!-- -->

  * ##### optionalfields: JoinFields

  * ##### optionalschema: string

  #### Returns [SelectQueryBuilder](https://mikro-orm.io/api/sql/interface/SelectQueryBuilder.md)\<T, never, (GetAlias\<Field> extends Alias ? IsNever\<Alias, true, false> extends true ? GetPropName\<Field> : Alias extends never ? GetPropName\<Field> : Alias extends string | number | symbol ? never\[Alias\<Alias>] extends \[Path, ...any\[]] ? \`${Path & string}.${GetPropName\<Field>}\` : GetPropName\<Field> : GetPropName\<Field> : GetPropName\<Field>) & {}, AddToContext\<GetType\<T, object, Field>, object, Field, Alias, true>, never, [ModifyFields](https://mikro-orm.io/api/sql.md#ModifyFields)<\*, never, never, Field, Alias, JoinFields>, {}>

### [**](#innerJoinLateral)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L1025)inheritedinnerJoinLateral

* ****innerJoinLateral**\<Alias>(field, alias, cond, schema): [SelectQueryBuilder](https://mikro-orm.io/api/sql/interface/SelectQueryBuilder.md)\<T, never, never, AddToContext\<T, object, string, Alias, false>, never, \*, {}>

* Inherited from RunQueryBuilder.innerJoinLateral

  #### Parameters

  * ##### field: [RawQueryFragment](https://mikro-orm.io/api/core/class/RawQueryFragment.md)\<string> | [QueryBuilder](https://mikro-orm.io/api/sql/class/QueryBuilder.md)\<any, never, never, never, never, \*, {}>

  * ##### alias: Alias

  * ##### cond: RawJoinCondition = <!-- -->{}

  * ##### optionalschema: string

  #### Returns [SelectQueryBuilder](https://mikro-orm.io/api/sql/interface/SelectQueryBuilder.md)\<T, never, never, AddToContext\<T, object, string, Alias, false>, never, \*, {}>

### [**](#innerJoinLateralAndSelect)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L1255)inheritedinnerJoinLateralAndSelect

* ****innerJoinLateralAndSelect**\<Field, Alias, JoinFields>(field, alias, cond, fields, schema): [SelectQueryBuilder](https://mikro-orm.io/api/sql/interface/SelectQueryBuilder.md)\<T, never, (GetAlias\<Field> extends Alias ? IsNever\<Alias, true, false> extends true ? GetPropName\<Field> : Alias extends never ? GetPropName\<Field> : Alias extends string | number | symbol ? never\[Alias\<Alias>] extends \[Path, ...any\[]] ? \`${Path & string}.${GetPropName\<Field>}\` : GetPropName\<Field> : GetPropName\<Field> : GetPropName\<Field>) & {}, AddToContext\<GetType\<T, object, Field>, object, Field, Alias, true>, never, [ModifyFields](https://mikro-orm.io/api/sql.md#ModifyFields)<\*, never, never, Field, Alias, JoinFields>, {}>

* Inherited from RunQueryBuilder.innerJoinLateralAndSelect

  #### Parameters

  * ##### field: \[Field, [RawQueryFragment](https://mikro-orm.io/api/core/class/RawQueryFragment.md)\<string> | [QueryBuilder](https://mikro-orm.io/api/sql/class/QueryBuilder.md)\<any, never, never, never, never, \*, {}>]

  * ##### alias: Alias

  * ##### cond: JoinCondition<[ExpandProperty](https://mikro-orm.io/api/core.md#ExpandProperty)\<GetType\<T, never, Field>\[GetPropName\<Field> & keyof<!-- --> GetType\<T, never, Field>]>, Alias> = <!-- -->

  * ##### optionalfields: JoinFields

  * ##### optionalschema: string

  #### Returns [SelectQueryBuilder](https://mikro-orm.io/api/sql/interface/SelectQueryBuilder.md)\<T, never, (GetAlias\<Field> extends Alias ? IsNever\<Alias, true, false> extends true ? GetPropName\<Field> : Alias extends never ? GetPropName\<Field> : Alias extends string | number | symbol ? never\[Alias\<Alias>] extends \[Path, ...any\[]] ? \`${Path & string}.${GetPropName\<Field>}\` : GetPropName\<Field> : GetPropName\<Field> : GetPropName\<Field>) & {}, AddToContext\<GetType\<T, object, Field>, object, Field, Alias, true>, never, [ModifyFields](https://mikro-orm.io/api/sql.md#ModifyFields)<\*, never, never, Field, Alias, JoinFields>, {}>

### [**](#insert)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L842)inheritedinsert

* ****insert**(data): [InsertQueryBuilder](https://mikro-orm.io/api/sql/interface/InsertQueryBuilder.md)\<T, never, never>

* Inherited from RunQueryBuilder.insert

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

  * ##### data: [RequiredEntityData](https://mikro-orm.io/api/core.md#RequiredEntityData)\<T> | [RequiredEntityData](https://mikro-orm.io/api/core.md#RequiredEntityData)\<T>\[]

  #### Returns [InsertQueryBuilder](https://mikro-orm.io/api/sql/interface/InsertQueryBuilder.md)\<T, never, never>

### [**](#join)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L930)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L950)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L959)inheritedjoin

* ****join**\<Field, Alias>(field, alias, cond, type, path, schema): [SelectQueryBuilder](https://mikro-orm.io/api/sql/interface/SelectQueryBuilder.md)\<T, never, never, AddToContext\<GetType\<T, object, Field>, object, Field, Alias, false>, never, \*, {}>
* ****join**\<Alias>(field, alias, cond, type, path, schema): [SelectQueryBuilder](https://mikro-orm.io/api/sql/interface/SelectQueryBuilder.md)\<T, never, never, AddToContext\<T, object, string, Alias, false>, never, \*, {}>

* Inherited from RunQueryBuilder.join

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

  * ##### optionalcond: JoinCondition<[ExpandProperty](https://mikro-orm.io/api/core.md#ExpandProperty)\<GetType\<T, never, Field>\[GetPropName\<Field> & keyof<!-- --> GetType\<T, never, Field>]>, Alias>

  * ##### optionaltype: [JoinType](https://mikro-orm.io/api/sql/enum/JoinType.md)

  * ##### optionalpath: string

  * ##### optionalschema: string

  #### Returns [SelectQueryBuilder](https://mikro-orm.io/api/sql/interface/SelectQueryBuilder.md)\<T, never, never, AddToContext\<GetType\<T, object, Field>, object, Field, Alias, false>, never, \*, {}>

### [**](#joinAndSelect)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L1100)inheritedjoinAndSelect

* ****joinAndSelect**\<Field, Alias, JoinFields>(field, alias, cond, type, path, fields, schema): [SelectQueryBuilder](https://mikro-orm.io/api/sql/interface/SelectQueryBuilder.md)\<T, never, (GetAlias\<Field> extends Alias ? IsNever\<Alias, true, false> extends true ? GetPropName\<Field> : Alias extends never ? GetPropName\<Field> : Alias extends string | number | symbol ? never\[Alias\<Alias>] extends \[Path, ...any\[]] ? \`${Path & string}.${GetPropName\<Field>}\` : GetPropName\<Field> : GetPropName\<Field> : GetPropName\<Field>) & {}, AddToContext\<GetType\<T, object, Field>, object, Field, Alias, true>, never, [ModifyFields](https://mikro-orm.io/api/sql.md#ModifyFields)<\*, never, never, Field, Alias, JoinFields>, {}>

* Inherited from RunQueryBuilder.joinAndSelect

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

  * ##### cond: JoinCondition<[ExpandProperty](https://mikro-orm.io/api/core.md#ExpandProperty)\<GetType\<T, never, Field>\[GetPropName\<Field> & keyof<!-- --> GetType\<T, never, Field>]>, Alias> = <!-- -->

  * ##### type: [JoinType](https://mikro-orm.io/api/sql/enum/JoinType.md) = <!-- -->JoinType.innerJoin

  * ##### optionalpath: string

  * ##### optionalfields: JoinFields

  * ##### optionalschema: string

  #### Returns [SelectQueryBuilder](https://mikro-orm.io/api/sql/interface/SelectQueryBuilder.md)\<T, never, (GetAlias\<Field> extends Alias ? IsNever\<Alias, true, false> extends true ? GetPropName\<Field> : Alias extends never ? GetPropName\<Field> : Alias extends string | number | symbol ? never\[Alias\<Alias>] extends \[Path, ...any\[]] ? \`${Path & string}.${GetPropName\<Field>}\` : GetPropName\<Field> : GetPropName\<Field> : GetPropName\<Field>) & {}, AddToContext\<GetType\<T, object, Field>, object, Field, Alias, true>, never, [ModifyFields](https://mikro-orm.io/api/sql.md#ModifyFields)<\*, never, never, Field, Alias, JoinFields>, {}>

### [**](#leftJoin)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L1037)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L1055)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L1062)inheritedleftJoin

* ****leftJoin**\<Field, Alias>(field, alias, cond, schema): [SelectQueryBuilder](https://mikro-orm.io/api/sql/interface/SelectQueryBuilder.md)\<T, never, never, AddToContext\<GetType\<T, object, Field>, object, Field, Alias, false>, never, \*, {}>
* ****leftJoin**\<Alias>(field, alias, cond, schema): [SelectQueryBuilder](https://mikro-orm.io/api/sql/interface/SelectQueryBuilder.md)\<T, never, never, AddToContext\<T, object, string, Alias, false>, never, \*, {}>

* Inherited from RunQueryBuilder.leftJoin

  Adds a LEFT JOIN clause to the query for an entity relation.

  ***

  #### Parameters

  * ##### field: Field

  * ##### alias: Alias

  * ##### optionalcond: JoinCondition<[ExpandProperty](https://mikro-orm.io/api/core.md#ExpandProperty)\<GetType\<T, never, Field>\[GetPropName\<Field> & keyof<!-- --> GetType\<T, never, Field>]>, Alias>

  * ##### optionalschema: string

  #### Returns [SelectQueryBuilder](https://mikro-orm.io/api/sql/interface/SelectQueryBuilder.md)\<T, never, never, AddToContext\<GetType\<T, object, Field>, object, Field, Alias, false>, never, \*, {}>

### [**](#leftJoinAndSelect)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L1164)inheritedleftJoinAndSelect

* ****leftJoinAndSelect**\<Field, Alias, JoinFields>(field, alias, cond, fields, schema): [SelectQueryBuilder](https://mikro-orm.io/api/sql/interface/SelectQueryBuilder.md)\<T, never, (GetAlias\<Field> extends Alias ? IsNever\<Alias, true, false> extends true ? GetPropName\<Field> : Alias extends never ? GetPropName\<Field> : Alias extends string | number | symbol ? never\[Alias\<Alias>] extends \[Path, ...any\[]] ? \`${Path & string}.${GetPropName\<Field>}\` : GetPropName\<Field> : GetPropName\<Field> : GetPropName\<Field>) & {}, AddToContext\<GetType\<T, object, Field>, object, Field, Alias, true>, never, [ModifyFields](https://mikro-orm.io/api/sql.md#ModifyFields)<\*, never, never, Field, Alias, JoinFields>, {}>

* Inherited from RunQueryBuilder.leftJoinAndSelect

  #### Parameters

  * ##### field: Field | \[Field, [RawQueryFragment](https://mikro-orm.io/api/core/class/RawQueryFragment.md)\<string> | [QueryBuilder](https://mikro-orm.io/api/sql/class/QueryBuilder.md)\<any, never, never, never, never, \*, {}>]

  * ##### alias: Alias

  * ##### cond: JoinCondition<[ExpandProperty](https://mikro-orm.io/api/core.md#ExpandProperty)\<GetType\<T, never, Field>\[GetPropName\<Field> & keyof<!-- --> GetType\<T, never, Field>]>, Alias> = <!-- -->

  * ##### optionalfields: JoinFields

  * ##### optionalschema: string

  #### Returns [SelectQueryBuilder](https://mikro-orm.io/api/sql/interface/SelectQueryBuilder.md)\<T, never, (GetAlias\<Field> extends Alias ? IsNever\<Alias, true, false> extends true ? GetPropName\<Field> : Alias extends never ? GetPropName\<Field> : Alias extends string | number | symbol ? never\[Alias\<Alias>] extends \[Path, ...any\[]] ? \`${Path & string}.${GetPropName\<Field>}\` : GetPropName\<Field> : GetPropName\<Field> : GetPropName\<Field>) & {}, AddToContext\<GetType\<T, object, Field>, object, Field, Alias, true>, never, [ModifyFields](https://mikro-orm.io/api/sql.md#ModifyFields)<\*, never, never, Field, Alias, JoinFields>, {}>

### [**](#leftJoinLateral)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L1079)inheritedleftJoinLateral

* ****leftJoinLateral**\<Alias>(field, alias, cond, schema): [SelectQueryBuilder](https://mikro-orm.io/api/sql/interface/SelectQueryBuilder.md)\<T, never, never, AddToContext\<T, object, string, Alias, false>, never, \*, {}>

* Inherited from RunQueryBuilder.leftJoinLateral

  #### Parameters

  * ##### field: [RawQueryFragment](https://mikro-orm.io/api/core/class/RawQueryFragment.md)\<string> | [QueryBuilder](https://mikro-orm.io/api/sql/class/QueryBuilder.md)\<any, never, never, never, never, \*, {}>

  * ##### alias: Alias

  * ##### cond: RawJoinCondition = <!-- -->{}

  * ##### optionalschema: string

  #### Returns [SelectQueryBuilder](https://mikro-orm.io/api/sql/interface/SelectQueryBuilder.md)\<T, never, never, AddToContext\<T, object, string, Alias, false>, never, \*, {}>

### [**](#leftJoinLateralAndSelect)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L1194)inheritedleftJoinLateralAndSelect

* ****leftJoinLateralAndSelect**\<Field, Alias, JoinFields>(field, alias, cond, fields, schema): [SelectQueryBuilder](https://mikro-orm.io/api/sql/interface/SelectQueryBuilder.md)\<T, never, (GetAlias\<Field> extends Alias ? IsNever\<Alias, true, false> extends true ? GetPropName\<Field> : Alias extends never ? GetPropName\<Field> : Alias extends string | number | symbol ? never\[Alias\<Alias>] extends \[Path, ...any\[]] ? \`${Path & string}.${GetPropName\<Field>}\` : GetPropName\<Field> : GetPropName\<Field> : GetPropName\<Field>) & {}, AddToContext\<GetType\<T, object, Field>, object, Field, Alias, true>, never, [ModifyFields](https://mikro-orm.io/api/sql.md#ModifyFields)<\*, never, never, Field, Alias, JoinFields>, {}>

* Inherited from RunQueryBuilder.leftJoinLateralAndSelect

  #### Parameters

  * ##### field: \[Field, [RawQueryFragment](https://mikro-orm.io/api/core/class/RawQueryFragment.md)\<string> | [QueryBuilder](https://mikro-orm.io/api/sql/class/QueryBuilder.md)\<any, never, never, never, never, \*, {}>]

  * ##### alias: Alias

  * ##### cond: JoinCondition<[ExpandProperty](https://mikro-orm.io/api/core.md#ExpandProperty)\<GetType\<T, never, Field>\[GetPropName\<Field> & keyof<!-- --> GetType\<T, never, Field>]>, Alias> = <!-- -->

  * ##### optionalfields: JoinFields

  * ##### optionalschema: string

  #### Returns [SelectQueryBuilder](https://mikro-orm.io/api/sql/interface/SelectQueryBuilder.md)\<T, never, (GetAlias\<Field> extends Alias ? IsNever\<Alias, true, false> extends true ? GetPropName\<Field> : Alias extends never ? GetPropName\<Field> : Alias extends string | number | symbol ? never\[Alias\<Alias>] extends \[Path, ...any\[]] ? \`${Path & string}.${GetPropName\<Field>}\` : GetPropName\<Field> : GetPropName\<Field> : GetPropName\<Field>) & {}, AddToContext\<GetType\<T, object, Field>, object, Field, Alias, true>, never, [ModifyFields](https://mikro-orm.io/api/sql.md#ModifyFields)<\*, never, never, Field, Alias, JoinFields>, {}>

### [**](#limit)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L1891)inheritedlimit

* ****limit**(limit, offset): [SelectQueryBuilder](https://mikro-orm.io/api/sql/interface/SelectQueryBuilder.md)\<T, never, never, never, never, \*, {}>

* Inherited from RunQueryBuilder.limit

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

  #### Returns [SelectQueryBuilder](https://mikro-orm.io/api/sql/interface/SelectQueryBuilder.md)\<T, never, never, never, never, \*, {}>

### [**](#merge)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L1844)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L1845)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L1846)inheritedmerge

* ****merge**\<P>(data): this
* ****merge**\<F>(data): this

* Inherited from RunQueryBuilder.merge

  #### Parameters

  * ##### data: readonly<!-- --> NestedAutoPath\<T, never, never, P>\[]

  #### Returns this

### [**](#offset)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L1910)inheritedoffset

* ****offset**(offset): [SelectQueryBuilder](https://mikro-orm.io/api/sql/interface/SelectQueryBuilder.md)\<T, never, never, never, never, \*, {}>

* Inherited from RunQueryBuilder.offset

  Sets an OFFSET clause to skip a number of results.

  * **@example**

    ```
    qb.select('*').limit(10).offset(20);  // Results 21-30
    ```

  ***

  #### Parameters

  * ##### optionaloffset: number

  #### Returns [SelectQueryBuilder](https://mikro-orm.io/api/sql/interface/SelectQueryBuilder.md)\<T, never, never, never, never, \*, {}>

### [**](#onConflict)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L1817)inheritedonConflict

* ****onConflict**\<F>(fields): [InsertQueryBuilder](https://mikro-orm.io/api/sql/interface/InsertQueryBuilder.md)\<T, never, never>

* Inherited from RunQueryBuilder.onConflict

  #### Parameters

  * ##### fields: [RawQueryFragment](https://mikro-orm.io/api/core/class/RawQueryFragment.md)\<string> | F | F\[] = <!-- -->

  #### Returns [InsertQueryBuilder](https://mikro-orm.io/api/sql/interface/InsertQueryBuilder.md)\<T, never, never>

### [**](#orderBy)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L1588)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L1604)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L1613)inheritedorderBy

* ****orderBy**(orderBy): [SelectQueryBuilder](https://mikro-orm.io/api/sql/interface/SelectQueryBuilder.md)\<T, never, never, never, never, \*, {}>
* ****orderBy**\<T>(orderBy): [SelectQueryBuilder](https://mikro-orm.io/api/sql/interface/SelectQueryBuilder.md)\<T, never, never, never, never, \*, {}>

* Inherited from RunQueryBuilder.orderBy

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

  * ##### orderBy: [ContextOrderByMap](https://mikro-orm.io/api/sql.md#ContextOrderByMap)\<T, never, never, never> | [ContextOrderByMap](https://mikro-orm.io/api/sql.md#ContextOrderByMap)\<T, never, never, never>\[]

  #### Returns [SelectQueryBuilder](https://mikro-orm.io/api/sql/interface/SelectQueryBuilder.md)\<T, never, never, never, never, \*, {}>

### [**](#orHaving)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L1810)inheritedorHaving

* ****orHaving**(cond, params): [SelectQueryBuilder](https://mikro-orm.io/api/sql/interface/SelectQueryBuilder.md)\<T, never, never, never, never, \*, {}>

* Inherited from RunQueryBuilder.orHaving

  #### Parameters

  * ##### optionalcond: string | [QBFilterQuery](https://mikro-orm.io/api/sql.md#QBFilterQuery)\<T, never, never, never>

  * ##### optionalparams: any\[]

  #### Returns [SelectQueryBuilder](https://mikro-orm.io/api/sql/interface/SelectQueryBuilder.md)\<T, never, never, never, never, \*, {}>

### [**](#orWhere)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L1560)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L1569)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L1570)inheritedorWhere

* ****orWhere**(cond): this
* ****orWhere**(cond, params): this

* Inherited from RunQueryBuilder.orWhere

  Adds an OR WHERE clause to the query using an object condition.

  * **@example**

    ```
    qb.where({ status: 'active' }).orWhere({ role: 'admin' });
    qb.where({ name: 'John' }).orWhere({ name: 'Jane' });
    ```

  ***

  #### Parameters

  * ##### cond: [QBFilterQuery](https://mikro-orm.io/api/sql.md#QBFilterQuery)\<T, never, never, never>

  #### Returns this

### [**](#returning)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L1861)inheritedreturning

* ****returning**\<F>(fields): this

* Inherited from RunQueryBuilder.returning

  #### Parameters

  * ##### optionalfields: F | F\[]

  #### Returns this

### [**](#select)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L668)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L696)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L710)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L730)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L742)inheritedselect

* ****select**\<F>(fields, distinct): [SelectQueryBuilder](https://mikro-orm.io/api/sql/interface/SelectQueryBuilder.md)\<T, never, never, never, ExtractRawAliases\<F>, ExtractRootFields\<F\[number] & string, never, never>, {}>
* ****select**\<P>(fields, distinct): [SelectQueryBuilder](https://mikro-orm.io/api/sql/interface/SelectQueryBuilder.md)\<T, never, never, never, never, ExtractRootFields\<P, never, never>, {}>
* ****select**\<P>(fields, distinct): [SelectQueryBuilder](https://mikro-orm.io/api/sql/interface/SelectQueryBuilder.md)\<T, never, never, never, never, ExtractRootFields\<P, never, never>, {}>
* ****select**\<F>(fields, distinct): [SelectQueryBuilder](https://mikro-orm.io/api/sql/interface/SelectQueryBuilder.md)\<T, never, never, never, ExtractRawAliasFromField\<F>, ExtractRootFields\<F & string, never, never>, {}>

* Inherited from RunQueryBuilder.select

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

  #### Returns [SelectQueryBuilder](https://mikro-orm.io/api/sql/interface/SelectQueryBuilder.md)\<T, never, never, never, ExtractRawAliases\<F>, ExtractRootFields\<F\[number] & string, never, never>, {}>

### [**](#setFlag)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L1942)inheritedsetFlag

* ****setFlag**(flag): this

* Inherited from RunQueryBuilder.setFlag

  #### Parameters

  * ##### flag: [QueryFlag](https://mikro-orm.io/api/core/enum/QueryFlag.md)

  #### Returns this

### [**](#setFlushMode)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L1936)inheritedsetFlushMode

* ****setFlushMode**(flushMode): this

* Inherited from RunQueryBuilder.setFlushMode

  #### Parameters

  * ##### optionalflushMode: [FlushMode](https://mikro-orm.io/api/core/enum/FlushMode.md)

  #### Returns this

### [**](#setLockMode)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L1923)inheritedsetLockMode

* ****setLockMode**(mode, tables): this

* Inherited from RunQueryBuilder.setLockMode

  #### Parameters

  * ##### optionalmode: [LockMode](https://mikro-orm.io/api/core/enum/LockMode.md)

  * ##### optionaltables: string\[]

  #### Returns this

### [**](#setLoggerContext)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L2819)inheritedsetLoggerContext

* ****setLoggerContext**(context): void

* Inherited from RunQueryBuilder.setLoggerContext

  Sets logger context for this query builder.

  ***

  #### Parameters

  * ##### context: [LoggingOptions](https://mikro-orm.io/api/core.md#LoggingOptions) & [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)

  #### Returns void

### [**](#stream)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L2419)inheritedstream

* ****stream**(options): AsyncIterableIterator<[Loaded](https://mikro-orm.io/api/core.md#Loaded)\<T, never, \*>, any, any>

* Inherited from RunQueryBuilder.stream

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

  #### Returns AsyncIterableIterator<[Loaded](https://mikro-orm.io/api/core.md#Loaded)\<T, never, \*>, any, any>

### [**](#toQuery)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L2194)inheritedtoQuery

* ****toQuery**(): { params: readonly
  <!-- -->
  unknown\[]; sql: string }

* Inherited from RunQueryBuilder.toQuery

  #### Returns { params: readonly<!-- --> unknown\[]; sql: string }

  * ##### params: readonly<!-- --> unknown\[]

  * ##### sql: string

### [**](#toRaw)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L2189)inheritedtoRaw

* ****toRaw**(): [RawQueryFragment](https://mikro-orm.io/api/core/class/RawQueryFragment.md)\<string>

* Inherited from RunQueryBuilder.toRaw

  Returns raw fragment representation of this QueryBuilder.

  ***

  #### Returns [RawQueryFragment](https://mikro-orm.io/api/core/class/RawQueryFragment.md)\<string>

### [**](#truncate)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L888)inheritedtruncate

* ****truncate**(): [TruncateQueryBuilder](https://mikro-orm.io/api/sql/interface/TruncateQueryBuilder.md)\<T>

* Inherited from RunQueryBuilder.truncate

  Creates a TRUNCATE query to remove all rows from the table.

  ***

  #### Returns [TruncateQueryBuilder](https://mikro-orm.io/api/sql/interface/TruncateQueryBuilder.md)\<T>

### [**](#union)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L2647)inheritedunion

* ****union**(...others): [QueryBuilder](https://mikro-orm.io/api/sql/class/QueryBuilder.md)\<T, never, never, never, never, \*, {}>

* Inherited from RunQueryBuilder.union

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

  #### Returns [QueryBuilder](https://mikro-orm.io/api/sql/class/QueryBuilder.md)\<T, never, never, never, never, \*, {}>

### [**](#unionAll)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L2629)inheritedunionAll

* ****unionAll**(...others): [QueryBuilder](https://mikro-orm.io/api/sql/class/QueryBuilder.md)\<T, never, never, never, never, \*, {}>

* Inherited from RunQueryBuilder.unionAll

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

  #### Returns [QueryBuilder](https://mikro-orm.io/api/sql/class/QueryBuilder.md)\<T, never, never, never, never, \*, {}>

### [**](#unsetFlag)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L1948)inheritedunsetFlag

* ****unsetFlag**(flag): this

* Inherited from RunQueryBuilder.unsetFlag

  #### Parameters

  * ##### flag: [QueryFlag](https://mikro-orm.io/api/core/enum/QueryFlag.md)

  #### Returns this

### [**](#update)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L860)inheritedupdate

* ****update**(data): [UpdateQueryBuilder](https://mikro-orm.io/api/sql/interface/UpdateQueryBuilder.md)\<T, never, never>

* Inherited from RunQueryBuilder.update

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

  * ##### data: [EntityData](https://mikro-orm.io/api/core.md#EntityData)\<T>

  #### Returns [UpdateQueryBuilder](https://mikro-orm.io/api/sql/interface/UpdateQueryBuilder.md)\<T, never, never>

### [**](#where)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L4088)inheritedwhere

* ****where**(cond, params, operator): this

* Inherited from RunQueryBuilder.where

  #### Parameters

  * ##### cond: string | [QBFilterQuery](https://mikro-orm.io/api/sql.md#QBFilterQuery)\<T, never, never, never>

  * ##### optionalparams: any\[] | $and | $or

  * ##### optionaloperator: $and | $or

  #### Returns this

### [**](#with)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L2683)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L2700)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L2705)inheritedwith

* ****with**\<Name, Q>(name, query, options): [QueryBuilder](https://mikro-orm.io/api/sql/class/QueryBuilder.md)\<T, never, never, never, never, \*, Record\<Name, Q extends [QueryBuilder](https://mikro-orm.io/api/sql/class/QueryBuilder.md)\<T, never, never, never, never, \*, {}> ? T : object>>
* ****with**\<Name>(name, query, options): [QueryBuilder](https://mikro-orm.io/api/sql/class/QueryBuilder.md)\<T, never, never, never, never, \*, Record\<Name, object>>

* Inherited from RunQueryBuilder.with

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

  #### Returns [QueryBuilder](https://mikro-orm.io/api/sql/class/QueryBuilder.md)\<T, never, never, never, never, \*, Record\<Name, Q extends [QueryBuilder](https://mikro-orm.io/api/sql/class/QueryBuilder.md)\<T, never, never, never, never, \*, {}> ? T : object>>

### [**](#withRecursive)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L2724)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L2741)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L2746)inheritedwithRecursive

* ****withRecursive**\<Name, Q>(name, query, options): [QueryBuilder](https://mikro-orm.io/api/sql/class/QueryBuilder.md)\<T, never, never, never, never, \*, Record\<Name, Q extends [QueryBuilder](https://mikro-orm.io/api/sql/class/QueryBuilder.md)\<T, never, never, never, never, \*, {}> ? T : object>>
* ****withRecursive**\<Name>(name, query, options): [QueryBuilder](https://mikro-orm.io/api/sql/class/QueryBuilder.md)\<T, never, never, never, never, \*, Record\<Name, object>>

* Inherited from RunQueryBuilder.withRecursive

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

  #### Returns [QueryBuilder](https://mikro-orm.io/api/sql/class/QueryBuilder.md)\<T, never, never, never, never, \*, Record\<Name, Q extends [QueryBuilder](https://mikro-orm.io/api/sql/class/QueryBuilder.md)\<T, never, never, never, never, \*, {}> ? T : object>>

### [**](#withSchema)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L1916)inheritedwithSchema

* ****withSchema**(schema): this

* Inherited from RunQueryBuilder.withSchema

  #### Parameters

  * ##### optionalschema: string

  #### Returns this

### [**](#withSubQuery)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/query/QueryBuilder.ts#L1408)inheritedwithSubQuery

* ****withSubQuery**(subQuery, alias): this

* Inherited from RunQueryBuilder.withSubQuery

  #### Parameters

  * ##### subQuery: [RawQueryFragment](https://mikro-orm.io/api/core/class/RawQueryFragment.md)\<string> | NativeQueryBuilder

  * ##### alias: string

  #### Returns this
