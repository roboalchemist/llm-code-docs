# Source: https://mikro-orm.io/api/core/interface/LoadCountOptions.md

# LoadCountOptions<!-- --> \<T>

### Hierarchy

* [CountOptions](https://mikro-orm.io/api/core/interface/CountOptions.md)\<T, \*>
  * *LoadCountOptions*

## Index[**](#Index)

### Properties

* [**cache](#cache)
* [**comments](#comments)
* [**connectionType](#connectionType)
* [**ctx](#ctx)
* [**filters](#filters)
* [**flushMode](#flushMode)
* [**groupBy](#groupBy)
* [**having](#having)
* [**hintComments](#hintComments)
* [**indexHint](#indexHint)
* [**loggerContext](#loggerContext)
* [**logging](#logging)
* [**populate](#populate)
* [**populateFilter](#populateFilter)
* [**populateWhere](#populateWhere)
* [**refresh](#refresh)
* [**schema](#schema)
* [**where](#where)

## Properties<!-- -->[**](#Properties)

### [**](#cache)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/IDatabaseDriver.ts#L248)optionalinheritedcache

**cache?

<!-- -->

: number | boolean | \[string, number]

Inherited from CountOptions.cache

### [**](#comments)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/IDatabaseDriver.ts#L258)optionalinheritedcomments

**comments?

<!-- -->

: string | string\[]

Inherited from CountOptions.comments

sql only

### [**](#connectionType)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/IDatabaseDriver.ts#L253)optionalinheritedconnectionType

**connectionType?

<!-- -->

: [ConnectionType](https://mikro-orm.io/api/core.md#ConnectionType)

Inherited from CountOptions.connectionType

### [**](#ctx)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/IDatabaseDriver.ts#L252)optionalinheritedctx

**ctx?

<!-- -->

: any

Inherited from CountOptions.ctx

### [**](#filters)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/IDatabaseDriver.ts#L244)optionalinheritedfilters

**filters?

<!-- -->

: [FilterOptions](https://mikro-orm.io/api/core.md#FilterOptions)

Inherited from CountOptions.filters

### [**](#flushMode)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/IDatabaseDriver.ts#L254)optionalinheritedflushMode

**flushMode?

<!-- -->

: always | [FlushMode](https://mikro-orm.io/api/core/enum/FlushMode.md) | commit | auto

Inherited from CountOptions.flushMode

### [**](#groupBy)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/IDatabaseDriver.ts#L246)optionalinheritedgroupBy

**groupBy?

<!-- -->

: string | readonly

<!-- -->

string\[]

Inherited from CountOptions.groupBy

### [**](#having)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/IDatabaseDriver.ts#L247)optionalinheritedhaving

**having?

<!-- -->

: [QBFilterQuery](https://mikro-orm.io/api/core.md#QBFilterQuery)\<T>

Inherited from CountOptions.having

### [**](#hintComments)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/IDatabaseDriver.ts#L260)optionalinheritedhintComments

**hintComments?

<!-- -->

: string | string\[]

Inherited from CountOptions.hintComments

sql only

### [**](#indexHint)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/IDatabaseDriver.ts#L256)optionalinheritedindexHint

**indexHint?

<!-- -->

: string

Inherited from CountOptions.indexHint

sql only

### [**](#loggerContext)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/IDatabaseDriver.ts#L261)optionalinheritedloggerContext

**loggerContext?

<!-- -->

: [LogContext](https://mikro-orm.io/api/core/interface/LogContext.md)

Inherited from CountOptions.loggerContext

### [**](#logging)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/IDatabaseDriver.ts#L262)optionalinheritedlogging

**logging?

<!-- -->

: [LoggingOptions](https://mikro-orm.io/api/core.md#LoggingOptions)

Inherited from CountOptions.logging

### [**](#populate)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/IDatabaseDriver.ts#L249)optionalinheritedpopulate

**populate?

<!-- -->

: [Populate](https://mikro-orm.io/api/core.md#Populate)\<T, \*>

Inherited from CountOptions.populate

### [**](#populateFilter)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/IDatabaseDriver.ts#L251)optionalinheritedpopulateFilter

**populateFilter?

<!-- -->

: [ObjectQuery](https://mikro-orm.io/api/core.md#ObjectQuery)\<T>

Inherited from CountOptions.populateFilter

### [**](#populateWhere)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/IDatabaseDriver.ts#L250)optionalinheritedpopulateWhere

**populateWhere?

<!-- -->

: [ObjectQuery](https://mikro-orm.io/api/core.md#ObjectQuery)\<T> | [PopulateHint](https://mikro-orm.io/api/core/enum/PopulateHint.md) | infer | all

Inherited from CountOptions.populateWhere

### [**](#refresh)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/Collection.ts#L503)optionalrefresh

**refresh?

<!-- -->

: boolean

### [**](#schema)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/IDatabaseDriver.ts#L245)optionalinheritedschema

**schema?

<!-- -->

: string

Inherited from CountOptions.schema

### [**](#where)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/Collection.ts#L504)optionalwhere

**where?

<!-- -->

: [FilterQuery](https://mikro-orm.io/api/core.md#FilterQuery)\<T>
