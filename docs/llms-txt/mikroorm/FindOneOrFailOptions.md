# Source: https://mikro-orm.io/api/core/interface/FindOneOrFailOptions.md

# FindOneOrFailOptions<!-- --> \<T, P, F, E>

### Hierarchy

* [FindOneOptions](https://mikro-orm.io/api/core/interface/FindOneOptions.md)\<T, P, F, E>
  * *FindOneOrFailOptions*
    * [LoadReferenceOrFailOptions](https://mikro-orm.io/api/core/interface/LoadReferenceOrFailOptions.md)

## Index[**](#index)

### Properties

* [**after](#after)
* [**allowDiskUse](#allowDiskUse)
* [**before](#before)
* [**cache](#cache)
* [**collation](#collation)
* [**comments](#comments)
* [**connectionType](#connectionType)
* [**convertCustomTypes](#convertCustomTypes)
* [**ctx](#ctx)
* [**disableIdentityMap](#disableIdentityMap)
* [**exclude](#exclude)
* [**failHandler](#failHandler)
* [**fields](#fields)
* [**filters](#filters)
* [**first](#first)
* [**flags](#flags)
* [**flushMode](#flushMode)
* [**groupBy](#groupBy)
* [**having](#having)
* [**hintComments](#hintComments)
* [**indexHint](#indexHint)
* [**last](#last)
* [**lockMode](#lockMode)
* [**lockTableAliases](#lockTableAliases)
* [**lockVersion](#lockVersion)
* [**loggerContext](#loggerContext)
* [**logging](#logging)
* [**maxTimeMS](#maxTimeMS)
* [**offset](#offset)
* [**orderBy](#orderBy)
* [**overfetch](#overfetch)
* [**populate](#populate)
* [**populateFilter](#populateFilter)
* [**populateHints](#populateHints)
* [**populateOrderBy](#populateOrderBy)
* [**populateWhere](#populateWhere)
* [**refresh](#refresh)
* [**schema](#schema)
* [**strategy](#strategy)
* [**strict](#strict)
* [**unionWhere](#unionWhere)
* [**unionWhereStrategy](#unionWhereStrategy)

## Properties<!-- -->[**](#properties)

### [**](#after)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/IDatabaseDriver.ts#L301)optionalinheritedafter

**after?

<!-- -->

: string | { endCursor: null | string } | [FilterObject](https://mikro-orm.io/api/core.md#FilterObject)\<T>

Inherited from FindOneOptions.after

Fetch items `after` this cursor.

### [**](#allowDiskUse)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/IDatabaseDriver.ts#L341)optionalinheritedallowDiskUse

**allowDiskUse?

<!-- -->

: boolean

Inherited from FindOneOptions.allowDiskUse

mongodb only

### [**](#before)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/IDatabaseDriver.ts#L298)optionalinheritedbefore

**before?

<!-- -->

: string | { startCursor: null | string } | [FilterObject](https://mikro-orm.io/api/core.md#FilterObject)\<T>

Inherited from FindOneOptions.before

Fetch items `before` this cursor.

### [**](#cache)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/IDatabaseDriver.ts#L281)optionalinheritedcache

**cache?

<!-- -->

: number | boolean | \[string, number]

Inherited from FindOneOptions.cache

Control result caching for this query. Result cache is by default disabled, not to be confused with the identity map.

### [**](#collation)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/IDatabaseDriver.ts#L337)optionalinheritedcollation

**collation?

<!-- -->

: string | [CollationOptions](https://mikro-orm.io/api/core/interface/CollationOptions.md)

Inherited from FindOneOptions.collation

SQL: collation name string applied as COLLATE to ORDER BY; MongoDB: CollationOptions object.

### [**](#comments)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/IDatabaseDriver.ts#L333)optionalinheritedcomments

**comments?

<!-- -->

: string | string\[]

Inherited from FindOneOptions.comments

sql only

### [**](#connectionType)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/IDatabaseDriver.ts#L329)optionalinheritedconnectionType

**connectionType?

<!-- -->

: [ConnectionType](https://mikro-orm.io/api/core.md#ConnectionType)

Inherited from FindOneOptions.connectionType

### [**](#convertCustomTypes)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/IDatabaseDriver.ts#L313)optionalinheritedconvertCustomTypes

**convertCustomTypes?

<!-- -->

: boolean

Inherited from FindOneOptions.convertCustomTypes

### [**](#ctx)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/IDatabaseDriver.ts#L328)optionalinheritedctx

**ctx?

<!-- -->

: any

Inherited from FindOneOptions.ctx

### [**](#disableIdentityMap)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/IDatabaseDriver.ts#L314)optionalinheriteddisableIdentityMap

**disableIdentityMap?

<!-- -->

: boolean

Inherited from FindOneOptions.disableIdentityMap

### [**](#exclude)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/IDatabaseDriver.ts#L229)optionalinheritedexclude

**exclude?

<!-- -->

: readonly

<!-- -->

[AutoPath](https://mikro-orm.io/api/core.md#AutoPath)\<T, E, never, 9>\[]

Inherited from FindOneOptions.exclude

### [**](#failHandler)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/IDatabaseDriver.ts#L374)optionalfailHandler

**failHandler?

<!-- -->

: (entityName, where) => Error

#### Type declaration

* * **(entityName, where): Error

  * #### Parameters

    * ##### entityName: string

    * ##### where: any

    #### Returns Error

### [**](#fields)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/IDatabaseDriver.ts#L228)optionalinheritedfields

**fields?

<!-- -->

: readonly

<!-- -->

[AutoPath](https://mikro-orm.io/api/core.md#AutoPath)\<T, F, \*, 9>\[]

Inherited from FindOneOptions.fields

### [**](#filters)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/IDatabaseDriver.ts#L323)optionalinheritedfilters

**filters?

<!-- -->

: [FilterOptions](https://mikro-orm.io/api/core.md#FilterOptions)

Inherited from FindOneOptions.filters

### [**](#first)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/IDatabaseDriver.ts#L304)optionalinheritedfirst

**first?

<!-- -->

: number

Inherited from FindOneOptions.first

Fetch `first` N items.

### [**](#flags)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/IDatabaseDriver.ts#L316)optionalinheritedflags

**flags?

<!-- -->

: [QueryFlag](https://mikro-orm.io/api/core/enum/QueryFlag.md)\[]

Inherited from FindOneOptions.flags

### [**](#flushMode)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/IDatabaseDriver.ts#L322)optionalinheritedflushMode

**flushMode?

<!-- -->

: always | [FlushMode](https://mikro-orm.io/api/core/enum/FlushMode.md) | commit | auto

Inherited from FindOneOptions.flushMode

### [**](#groupBy)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/IDatabaseDriver.ts#L318)optionalinheritedgroupBy

**groupBy?

<!-- -->

: string | string\[]

Inherited from FindOneOptions.groupBy

sql only

### [**](#having)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/IDatabaseDriver.ts#L319)optionalinheritedhaving

**having?

<!-- -->

: [FilterQuery](https://mikro-orm.io/api/core.md#FilterQuery)\<T>

Inherited from FindOneOptions.having

### [**](#hintComments)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/IDatabaseDriver.ts#L335)optionalinheritedhintComments

**hintComments?

<!-- -->

: string | string\[]

Inherited from FindOneOptions.hintComments

sql only

### [**](#indexHint)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/IDatabaseDriver.ts#L331)optionalinheritedindexHint

**indexHint?

<!-- -->

: string | [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)

Inherited from FindOneOptions.indexHint

SQL: appended to FROM clause (e.g. `'force index(my_index)'`); MongoDB: index name or spec passed as `hint`.

### [**](#last)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/IDatabaseDriver.ts#L307)optionalinheritedlast

**last?

<!-- -->

: number

Inherited from FindOneOptions.last

Fetch `last` N items.

### [**](#lockMode)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/IDatabaseDriver.ts#L364)optionalinheritedlockMode

**lockMode?

<!-- -->

: [LockMode](https://mikro-orm.io/api/core/enum/LockMode.md)

Inherited from FindOneOptions.lockMode

### [**](#lockTableAliases)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/IDatabaseDriver.ts#L327)optionalinheritedlockTableAliases

**lockTableAliases?

<!-- -->

: string\[]

Inherited from FindOneOptions.lockTableAliases

sql only

### [**](#lockVersion)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/IDatabaseDriver.ts#L365)optionalinheritedlockVersion

**lockVersion?

<!-- -->

: number | Date

Inherited from FindOneOptions.lockVersion

### [**](#loggerContext)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/IDatabaseDriver.ts#L342)optionalinheritedloggerContext

**loggerContext?

<!-- -->

: [LogContext](https://mikro-orm.io/api/core/interface/LogContext.md)

Inherited from FindOneOptions.loggerContext

### [**](#logging)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/IDatabaseDriver.ts#L343)optionalinheritedlogging

**logging?

<!-- -->

: [LoggingOptions](https://mikro-orm.io/api/core.md#LoggingOptions)

Inherited from FindOneOptions.logging

### [**](#maxTimeMS)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/IDatabaseDriver.ts#L339)optionalinheritedmaxTimeMS

**maxTimeMS?

<!-- -->

: number

Inherited from FindOneOptions.maxTimeMS

mongodb only

### [**](#offset)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/IDatabaseDriver.ts#L295)optionalinheritedoffset

**offset?

<!-- -->

: number

Inherited from FindOneOptions.offset

Sets the offset. If you try to use limit/offset on a query that joins a to-many relation, pagination mechanism will be triggered, resulting in a subquery condition, to apply this limit only to the root entities instead of the cartesian product you get from a database in this case.

### [**](#orderBy)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/IDatabaseDriver.ts#L278)optionalinheritedorderBy

**orderBy?

<!-- -->

: [OrderDefinition](https://mikro-orm.io/api/core.md#OrderDefinition)\<T>

Inherited from FindOneOptions.orderBy

Ordering of the results.Can be an object or array of objects, keys are property names, values are ordering (asc/desc)

### [**](#overfetch)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/IDatabaseDriver.ts#L310)optionalinheritedoverfetch

**overfetch?

<!-- -->

: boolean

Inherited from FindOneOptions.overfetch

Fetch one more item than `first`/`last`, enabled automatically in `em.findByCursor` to check if there is a next page.

### [**](#populate)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/IDatabaseDriver.ts#L227)optionalinheritedpopulate

**populate?

<!-- -->

: [Populate](https://mikro-orm.io/api/core.md#Populate)\<T, P>

Inherited from FindOneOptions.populate

### [**](#populateFilter)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/IDatabaseDriver.ts#L251)optionalinheritedpopulateFilter

**populateFilter?

<!-- -->

: [ObjectQuery](https://mikro-orm.io/api/core.md#ObjectQuery)\<T>

Inherited from FindOneOptions.populateFilter

Filter condition for populated relations. This is similar to `populateWhere`, but will produce a `left join` when nesting the condition. This is used for implementation of joined filters.

### [**](#populateHints)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/IDatabaseDriver.ts#L275)optionalinheritedpopulateHints

**populateHints?

<!-- -->

: \[P] extends \[never] ? never : { \[ K in string ]?: [PopulateHintOptions](https://mikro-orm.io/api/core.md#PopulateHintOptions) }

Inherited from FindOneOptions.populateHints

Per-relation overrides for populate loading behavior. Keys are populate paths (same as used in `populate`).

### [**](#populateOrderBy)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/IDatabaseDriver.ts#L272)optionalinheritedpopulateOrderBy

**populateOrderBy?

<!-- -->

: [OrderDefinition](https://mikro-orm.io/api/core.md#OrderDefinition)\<T>

Inherited from FindOneOptions.populateOrderBy

Used for ordering of the populate queries. If not specified, the value of `options.orderBy` is used.

### [**](#populateWhere)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/IDatabaseDriver.ts#L245)optionalinheritedpopulateWhere

**populateWhere?

<!-- -->

: [PopulateHint](https://mikro-orm.io/api/core/enum/PopulateHint.md) | infer | all | [ObjectQuery](https://mikro-orm.io/api/core.md#ObjectQuery)\<T>

Inherited from FindOneOptions.populateWhere

Where condition for populated relations. This will have no effect on the root entity. With `select-in` strategy, this is applied only to the populate queries. With `joined` strategy, those are applied as `join on` conditions. When you use a nested condition on a to-many relation, it will produce a nested inner join, discarding the collection items based on the child condition.

### [**](#refresh)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/IDatabaseDriver.ts#L312)optionalinheritedrefresh

**refresh?

<!-- -->

: boolean

Inherited from FindOneOptions.refresh

### [**](#schema)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/IDatabaseDriver.ts#L315)optionalinheritedschema

**schema?

<!-- -->

: string

Inherited from FindOneOptions.schema

### [**](#strategy)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/IDatabaseDriver.ts#L321)optionalinheritedstrategy

**strategy?

<!-- -->

: [LoadStrategy](https://mikro-orm.io/api/core/enum/LoadStrategy.md) | select-in | joined | balanced

Inherited from FindOneOptions.strategy

sql only

### [**](#strict)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/IDatabaseDriver.ts#L375)optionalstrict

**strict?

<!-- -->

: boolean

### [**](#unionWhere)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/IDatabaseDriver.ts#L261)optionalinheritedunionWhere

**unionWhere?

<!-- -->

: [ObjectQuery](https://mikro-orm.io/api/core.md#ObjectQuery)\<T>\[]

Inherited from FindOneOptions.unionWhere

Index-friendly alternative to `$or` for conditions that span joined relations. Each array element becomes an independent branch combined via `UNION ALL` subquery: `WHERE pk IN (branch_1 UNION ALL branch_2 ... branch_N)`. The database plans each branch independently, enabling per-table index usage (e.g. GIN trigram indexes for fuzzy search across related entities). sql only

### [**](#unionWhereStrategy)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/IDatabaseDriver.ts#L269)optionalinheritedunionWhereStrategy

**unionWhereStrategy?

<!-- -->

: union-all | union

Inherited from FindOneOptions.unionWhereStrategy

Strategy for combining `unionWhere` branches.

* `'union-all'` (default) — skips deduplication, faster for most use cases.
* `'union'` — deduplicates rows between branches; useful when branch overlap is very high. sql only
