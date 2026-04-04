# Source: https://mikro-orm.io/api/core/interface/LoadReferenceOrFailOptions.md

# LoadReferenceOrFailOptions<!-- --> \<T, P, F, E>

### Hierarchy

* [FindOneOrFailOptions](https://mikro-orm.io/api/core/interface/FindOneOrFailOptions.md)\<T, P, F, E>
  * *LoadReferenceOrFailOptions*

## Index[**](#Index)

### Properties

* [**after](#after)
* [**before](#before)
* [**cache](#cache)
* [**comments](#comments)
* [**connectionType](#connectionType)
* [**convertCustomTypes](#convertCustomTypes)
* [**ctx](#ctx)
* [**dataloader](#dataloader)
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
* [**strict](#strict)

## Properties<!-- -->[**](#Properties)

### [**](#after)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/IDatabaseDriver.ts#L163)optionalinheritedafter

**after?

<!-- -->

: string | { endCursor: null | string } | [FilterObject](https://mikro-orm.io/api/core.md#FilterObject)\<T>

Inherited from FindOneOrFailOptions.after

Fetch items `after` this cursor.

### [**](#before)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/IDatabaseDriver.ts#L160)optionalinheritedbefore

**before?

<!-- -->

: string | { startCursor: null | string } | [FilterObject](https://mikro-orm.io/api/core.md#FilterObject)\<T>

Inherited from FindOneOrFailOptions.before

Fetch items `before` this cursor.

### [**](#cache)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/IDatabaseDriver.ts#L143)optionalinheritedcache

**cache?

<!-- -->

: number | boolean | \[string, number]

Inherited from FindOneOrFailOptions.cache

Control result caching for this query. Result cache is by default disabled, not to be confused with the identity map.

### [**](#comments)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/IDatabaseDriver.ts#L195)optionalinheritedcomments

**comments?

<!-- -->

: string | string\[]

Inherited from FindOneOrFailOptions.comments

sql only

### [**](#connectionType)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/IDatabaseDriver.ts#L191)optionalinheritedconnectionType

**connectionType?

<!-- -->

: [ConnectionType](https://mikro-orm.io/api/core.md#ConnectionType)

Inherited from FindOneOrFailOptions.connectionType

### [**](#convertCustomTypes)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/IDatabaseDriver.ts#L175)optionalinheritedconvertCustomTypes

**convertCustomTypes?

<!-- -->

: boolean

Inherited from FindOneOrFailOptions.convertCustomTypes

### [**](#ctx)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/IDatabaseDriver.ts#L190)optionalinheritedctx

**ctx?

<!-- -->

: any

Inherited from FindOneOrFailOptions.ctx

### [**](#dataloader)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/Reference.ts#L306)optionaldataloader

**dataloader?

<!-- -->

: boolean

### [**](#disableIdentityMap)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/IDatabaseDriver.ts#L176)optionalinheriteddisableIdentityMap

**disableIdentityMap?

<!-- -->

: boolean

Inherited from FindOneOrFailOptions.disableIdentityMap

### [**](#exclude)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/IDatabaseDriver.ts#L112)optionalinheritedexclude

**exclude?

<!-- -->

: readonly

<!-- -->

[AutoPath](https://mikro-orm.io/api/core.md#AutoPath)\<T, E, never, 9>\[]

Inherited from FindOneOrFailOptions.exclude

### [**](#failHandler)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/IDatabaseDriver.ts#L214)optionalinheritedfailHandler

**failHandler?

<!-- -->

: (entityName, where) => Error

Inherited from FindOneOrFailOptions.failHandler

#### Type declaration

* * **(entityName, where): Error

  - #### Parameters

    * ##### entityName: string
    * ##### where: any

    #### Returns Error

### [**](#fields)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/IDatabaseDriver.ts#L111)optionalinheritedfields

**fields?

<!-- -->

: readonly

<!-- -->

[AutoPath](https://mikro-orm.io/api/core.md#AutoPath)\<T, F, \*, 9>\[]

Inherited from FindOneOrFailOptions.fields

### [**](#filters)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/IDatabaseDriver.ts#L185)optionalinheritedfilters

**filters?

<!-- -->

: [FilterOptions](https://mikro-orm.io/api/core.md#FilterOptions)

Inherited from FindOneOrFailOptions.filters

### [**](#first)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/IDatabaseDriver.ts#L166)optionalinheritedfirst

**first?

<!-- -->

: number

Inherited from FindOneOrFailOptions.first

Fetch `first` N items.

### [**](#flags)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/IDatabaseDriver.ts#L178)optionalinheritedflags

**flags?

<!-- -->

: [QueryFlag](https://mikro-orm.io/api/core/enum/QueryFlag.md)\[]

Inherited from FindOneOrFailOptions.flags

### [**](#flushMode)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/IDatabaseDriver.ts#L184)optionalinheritedflushMode

**flushMode?

<!-- -->

: always | [FlushMode](https://mikro-orm.io/api/core/enum/FlushMode.md) | commit | auto

Inherited from FindOneOrFailOptions.flushMode

### [**](#groupBy)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/IDatabaseDriver.ts#L180)optionalinheritedgroupBy

**groupBy?

<!-- -->

: string | string\[]

Inherited from FindOneOrFailOptions.groupBy

sql only

### [**](#having)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/IDatabaseDriver.ts#L181)optionalinheritedhaving

**having?

<!-- -->

: [QBFilterQuery](https://mikro-orm.io/api/core.md#QBFilterQuery)\<T>

Inherited from FindOneOrFailOptions.having

### [**](#hintComments)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/IDatabaseDriver.ts#L197)optionalinheritedhintComments

**hintComments?

<!-- -->

: string | string\[]

Inherited from FindOneOrFailOptions.hintComments

sql only

### [**](#indexHint)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/IDatabaseDriver.ts#L193)optionalinheritedindexHint

**indexHint?

<!-- -->

: string

Inherited from FindOneOrFailOptions.indexHint

sql only

### [**](#last)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/IDatabaseDriver.ts#L169)optionalinheritedlast

**last?

<!-- -->

: number

Inherited from FindOneOrFailOptions.last

Fetch `last` N items.

### [**](#lockMode)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/IDatabaseDriver.ts#L209)optionalinheritedlockMode

**lockMode?

<!-- -->

: [LockMode](https://mikro-orm.io/api/core/enum/LockMode.md)

Inherited from FindOneOrFailOptions.lockMode

### [**](#lockTableAliases)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/IDatabaseDriver.ts#L189)optionalinheritedlockTableAliases

**lockTableAliases?

<!-- -->

: string\[]

Inherited from FindOneOrFailOptions.lockTableAliases

sql only

### [**](#lockVersion)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/IDatabaseDriver.ts#L210)optionalinheritedlockVersion

**lockVersion?

<!-- -->

: number | Date

Inherited from FindOneOrFailOptions.lockVersion

### [**](#loggerContext)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/IDatabaseDriver.ts#L198)optionalinheritedloggerContext

**loggerContext?

<!-- -->

: [LogContext](https://mikro-orm.io/api/core/interface/LogContext.md)

Inherited from FindOneOrFailOptions.loggerContext

### [**](#logging)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/IDatabaseDriver.ts#L199)optionalinheritedlogging

**logging?

<!-- -->

: [LoggingOptions](https://mikro-orm.io/api/core.md#LoggingOptions)

Inherited from FindOneOrFailOptions.logging

### [**](#offset)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/IDatabaseDriver.ts#L157)optionalinheritedoffset

**offset?

<!-- -->

: number

Inherited from FindOneOrFailOptions.offset

Sets the offset. If you try to use limit/offset on a query that joins a to-many relation, pagination mechanism will be triggered, resulting in a subquery condition, to apply this limit only to the root entities instead of the cartesian product you get from a database in this case.

### [**](#orderBy)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/IDatabaseDriver.ts#L140)optionalinheritedorderBy

**orderBy?

<!-- -->

: [OrderDefinition](https://mikro-orm.io/api/core.md#OrderDefinition)\<T>

Inherited from FindOneOrFailOptions.orderBy

Ordering of the results.Can be an object or array of objects, keys are property names, values are ordering (asc/desc)

### [**](#overfetch)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/IDatabaseDriver.ts#L172)optionalinheritedoverfetch

**overfetch?

<!-- -->

: boolean

Inherited from FindOneOrFailOptions.overfetch

Fetch one more item than `first`/`last`, enabled automatically in `em.findByCursor` to check if there is a next page.

### [**](#populate)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/IDatabaseDriver.ts#L110)optionalinheritedpopulate

**populate?

<!-- -->

: [Populate](https://mikro-orm.io/api/core.md#Populate)\<T, P>

Inherited from FindOneOrFailOptions.populate

### [**](#populateFilter)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/IDatabaseDriver.ts#L134)optionalinheritedpopulateFilter

**populateFilter?

<!-- -->

: [ObjectQuery](https://mikro-orm.io/api/core.md#ObjectQuery)\<T>

Inherited from FindOneOrFailOptions.populateFilter

Filter condition for populated relations. This is similar to `populateWhere`, but will produce a `left join` when nesting the condition. This is used for implementation of joined filters.

### [**](#populateOrderBy)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/IDatabaseDriver.ts#L137)optionalinheritedpopulateOrderBy

**populateOrderBy?

<!-- -->

: [OrderDefinition](https://mikro-orm.io/api/core.md#OrderDefinition)\<T>

Inherited from FindOneOrFailOptions.populateOrderBy

Used for ordering of the populate queries. If not specified, the value of `options.orderBy` is used.

### [**](#populateWhere)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/IDatabaseDriver.ts#L128)optionalinheritedpopulateWhere

**populateWhere?

<!-- -->

: [PopulateHint](https://mikro-orm.io/api/core/enum/PopulateHint.md) | infer | all | [ObjectQuery](https://mikro-orm.io/api/core.md#ObjectQuery)\<T>

Inherited from FindOneOrFailOptions.populateWhere

Where condition for populated relations. This will have no effect on the root entity. With `select-in` strategy, this is applied only to the populate queries. With `joined` strategy, those are applied as `join on` conditions. When you use a nested condition on a to-many relation, it will produce a nested inner join, discarding the collection items based on the child condition.

### [**](#refresh)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/IDatabaseDriver.ts#L174)optionalinheritedrefresh

**refresh?

<!-- -->

: boolean

Inherited from FindOneOrFailOptions.refresh

### [**](#schema)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/IDatabaseDriver.ts#L177)optionalinheritedschema

**schema?

<!-- -->

: string

Inherited from FindOneOrFailOptions.schema

### [**](#strategy)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/IDatabaseDriver.ts#L183)optionalinheritedstrategy

**strategy?

<!-- -->

: [LoadStrategy](https://mikro-orm.io/api/core/enum/LoadStrategy.md) | select-in | joined | balanced

Inherited from FindOneOrFailOptions.strategy

sql only

### [**](#strict)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/IDatabaseDriver.ts#L215)optionalinheritedstrict

**strict?

<!-- -->

: boolean

Inherited from FindOneOrFailOptions.strict
