# Source: https://mikro-orm.io/api/core/interface/FindAllOptions.md

# FindAllOptions<!-- --> \<T, P, F, E>

### Hierarchy

* [FindOptions](https://mikro-orm.io/api/core/interface/FindOptions.md)\<T, P, F, E>
  * *FindAllOptions*

## Index[**](#Index)

### Properties

* [**after](#after)
* [**before](#before)
* [**cache](#cache)
* [**comments](#comments)
* [**connectionType](#connectionType)
* [**convertCustomTypes](#convertCustomTypes)
* [**ctx](#ctx)
* [**disableIdentityMap](#disableIdentityMap)
* [**exclude](#exclude)
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
* [**limit](#limit)
* [**lockMode](#lockMode)
* [**lockTableAliases](#lockTableAliases)
* [**loggerContext](#loggerContext)
* [**logging](#logging)
* [**offset](#offset)
* [**orderBy](#orderBy)
* [**overfetch](#overfetch)
* [**populate](#populate)
* [**populateFilter](#populateFilter)
* [**populateOrderBy](#populateOrderBy)
* [**populateWhere](#populateWhere)
* [**refresh](#refresh)
* [**schema](#schema)
* [**strategy](#strategy)
* [**where](#where)

## Properties<!-- -->[**](#Properties)

### [**](#after)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/IDatabaseDriver.ts#L163)optionalinheritedafter

**after?

<!-- -->

: string | { endCursor: null | string } | [FilterObject](https://mikro-orm.io/api/core.md#FilterObject)\<T>

Inherited from FindOptions.after

Fetch items `after` this cursor.

### [**](#before)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/IDatabaseDriver.ts#L160)optionalinheritedbefore

**before?

<!-- -->

: string | { startCursor: null | string } | [FilterObject](https://mikro-orm.io/api/core.md#FilterObject)\<T>

Inherited from FindOptions.before

Fetch items `before` this cursor.

### [**](#cache)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/IDatabaseDriver.ts#L143)optionalinheritedcache

**cache?

<!-- -->

: number | boolean | \[string, number]

Inherited from FindOptions.cache

Control result caching for this query. Result cache is by default disabled, not to be confused with the identity map.

### [**](#comments)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/IDatabaseDriver.ts#L195)optionalinheritedcomments

**comments?

<!-- -->

: string | string\[]

Inherited from FindOptions.comments

sql only

### [**](#connectionType)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/IDatabaseDriver.ts#L191)optionalinheritedconnectionType

**connectionType?

<!-- -->

: [ConnectionType](https://mikro-orm.io/api/core.md#ConnectionType)

Inherited from FindOptions.connectionType

### [**](#convertCustomTypes)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/IDatabaseDriver.ts#L175)optionalinheritedconvertCustomTypes

**convertCustomTypes?

<!-- -->

: boolean

Inherited from FindOptions.convertCustomTypes

### [**](#ctx)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/IDatabaseDriver.ts#L190)optionalinheritedctx

**ctx?

<!-- -->

: any

Inherited from FindOptions.ctx

### [**](#disableIdentityMap)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/IDatabaseDriver.ts#L176)optionalinheriteddisableIdentityMap

**disableIdentityMap?

<!-- -->

: boolean

Inherited from FindOptions.disableIdentityMap

### [**](#exclude)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/IDatabaseDriver.ts#L112)optionalinheritedexclude

**exclude?

<!-- -->

: readonly

<!-- -->

[AutoPath](https://mikro-orm.io/api/core.md#AutoPath)\<T, E, never, 9>\[]

Inherited from FindOptions.exclude

### [**](#fields)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/IDatabaseDriver.ts#L111)optionalinheritedfields

**fields?

<!-- -->

: readonly

<!-- -->

[AutoPath](https://mikro-orm.io/api/core.md#AutoPath)\<T, F, \*, 9>\[]

Inherited from FindOptions.fields

### [**](#filters)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/IDatabaseDriver.ts#L185)optionalinheritedfilters

**filters?

<!-- -->

: [FilterOptions](https://mikro-orm.io/api/core.md#FilterOptions)

Inherited from FindOptions.filters

### [**](#first)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/IDatabaseDriver.ts#L166)optionalinheritedfirst

**first?

<!-- -->

: number

Inherited from FindOptions.first

Fetch `first` N items.

### [**](#flags)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/IDatabaseDriver.ts#L178)optionalinheritedflags

**flags?

<!-- -->

: [QueryFlag](https://mikro-orm.io/api/core/enum/QueryFlag.md)\[]

Inherited from FindOptions.flags

### [**](#flushMode)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/IDatabaseDriver.ts#L184)optionalinheritedflushMode

**flushMode?

<!-- -->

: always | [FlushMode](https://mikro-orm.io/api/core/enum/FlushMode.md) | commit | auto

Inherited from FindOptions.flushMode

### [**](#groupBy)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/IDatabaseDriver.ts#L180)optionalinheritedgroupBy

**groupBy?

<!-- -->

: string | string\[]

Inherited from FindOptions.groupBy

sql only

### [**](#having)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/IDatabaseDriver.ts#L181)optionalinheritedhaving

**having?

<!-- -->

: [QBFilterQuery](https://mikro-orm.io/api/core.md#QBFilterQuery)\<T>

Inherited from FindOptions.having

### [**](#hintComments)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/IDatabaseDriver.ts#L197)optionalinheritedhintComments

**hintComments?

<!-- -->

: string | string\[]

Inherited from FindOptions.hintComments

sql only

### [**](#indexHint)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/IDatabaseDriver.ts#L193)optionalinheritedindexHint

**indexHint?

<!-- -->

: string

Inherited from FindOptions.indexHint

sql only

### [**](#last)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/IDatabaseDriver.ts#L169)optionalinheritedlast

**last?

<!-- -->

: number

Inherited from FindOptions.last

Fetch `last` N items.

### [**](#limit)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/IDatabaseDriver.ts#L150)optionalinheritedlimit

**limit?

<!-- -->

: number

Inherited from FindOptions.limit

Limit the number of returned results. If you try to use limit/offset on a query that joins a to-many relation, pagination mechanism will be triggered, resulting in a subquery condition, to apply this limit only to the root entities instead of the cartesian product you get from a database in this case.

### [**](#lockMode)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/IDatabaseDriver.ts#L187)optionalinheritedlockMode

**lockMode?

<!-- -->

: NONE | PESSIMISTIC\_READ | PESSIMISTIC\_WRITE | PESSIMISTIC\_PARTIAL\_WRITE | PESSIMISTIC\_WRITE\_OR\_FAIL | PESSIMISTIC\_PARTIAL\_READ | PESSIMISTIC\_READ\_OR\_FAIL

Inherited from FindOptions.lockMode

sql only

### [**](#lockTableAliases)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/IDatabaseDriver.ts#L189)optionalinheritedlockTableAliases

**lockTableAliases?

<!-- -->

: string\[]

Inherited from FindOptions.lockTableAliases

sql only

### [**](#loggerContext)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/IDatabaseDriver.ts#L198)optionalinheritedloggerContext

**loggerContext?

<!-- -->

: [LogContext](https://mikro-orm.io/api/core/interface/LogContext.md)

Inherited from FindOptions.loggerContext

### [**](#logging)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/IDatabaseDriver.ts#L199)optionalinheritedlogging

**logging?

<!-- -->

: [LoggingOptions](https://mikro-orm.io/api/core.md#LoggingOptions)

Inherited from FindOptions.logging

### [**](#offset)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/IDatabaseDriver.ts#L157)optionalinheritedoffset

**offset?

<!-- -->

: number

Inherited from FindOptions.offset

Sets the offset. If you try to use limit/offset on a query that joins a to-many relation, pagination mechanism will be triggered, resulting in a subquery condition, to apply this limit only to the root entities instead of the cartesian product you get from a database in this case.

### [**](#orderBy)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/IDatabaseDriver.ts#L140)optionalinheritedorderBy

**orderBy?

<!-- -->

: [OrderDefinition](https://mikro-orm.io/api/core.md#OrderDefinition)\<T>

Inherited from FindOptions.orderBy

Ordering of the results.Can be an object or array of objects, keys are property names, values are ordering (asc/desc)

### [**](#overfetch)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/IDatabaseDriver.ts#L172)optionalinheritedoverfetch

**overfetch?

<!-- -->

: boolean

Inherited from FindOptions.overfetch

Fetch one more item than `first`/`last`, enabled automatically in `em.findByCursor` to check if there is a next page.

### [**](#populate)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/IDatabaseDriver.ts#L110)optionalinheritedpopulate

**populate?

<!-- -->

: [Populate](https://mikro-orm.io/api/core.md#Populate)\<T, P>

Inherited from FindOptions.populate

### [**](#populateFilter)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/IDatabaseDriver.ts#L134)optionalinheritedpopulateFilter

**populateFilter?

<!-- -->

: [ObjectQuery](https://mikro-orm.io/api/core.md#ObjectQuery)\<T>

Inherited from FindOptions.populateFilter

Filter condition for populated relations. This is similar to `populateWhere`, but will produce a `left join` when nesting the condition. This is used for implementation of joined filters.

### [**](#populateOrderBy)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/IDatabaseDriver.ts#L137)optionalinheritedpopulateOrderBy

**populateOrderBy?

<!-- -->

: [OrderDefinition](https://mikro-orm.io/api/core.md#OrderDefinition)\<T>

Inherited from FindOptions.populateOrderBy

Used for ordering of the populate queries. If not specified, the value of `options.orderBy` is used.

### [**](#populateWhere)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/IDatabaseDriver.ts#L128)optionalinheritedpopulateWhere

**populateWhere?

<!-- -->

: [PopulateHint](https://mikro-orm.io/api/core/enum/PopulateHint.md) | infer | all | [ObjectQuery](https://mikro-orm.io/api/core.md#ObjectQuery)\<T>

Inherited from FindOptions.populateWhere

Where condition for populated relations. This will have no effect on the root entity. With `select-in` strategy, this is applied only to the populate queries. With `joined` strategy, those are applied as `join on` conditions. When you use a nested condition on a to-many relation, it will produce a nested inner join, discarding the collection items based on the child condition.

### [**](#refresh)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/IDatabaseDriver.ts#L174)optionalinheritedrefresh

**refresh?

<!-- -->

: boolean

Inherited from FindOptions.refresh

### [**](#schema)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/IDatabaseDriver.ts#L177)optionalinheritedschema

**schema?

<!-- -->

: string

Inherited from FindOptions.schema

### [**](#strategy)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/IDatabaseDriver.ts#L183)optionalinheritedstrategy

**strategy?

<!-- -->

: [LoadStrategy](https://mikro-orm.io/api/core/enum/LoadStrategy.md) | select-in | joined | balanced

Inherited from FindOptions.strategy

sql only

### [**](#where)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/IDatabaseDriver.ts#L99)optionalwhere

**where?

<!-- -->

: [FilterQuery](https://mikro-orm.io/api/core.md#FilterQuery)\<T>
