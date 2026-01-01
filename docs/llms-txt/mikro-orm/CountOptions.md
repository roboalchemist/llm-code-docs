# Source: https://mikro-orm.io/api/core/interface/CountOptions.md

# CountOptions<!-- --> \<T, P>

### Hierarchy

* *CountOptions*
  * [LoadCountOptions](https://mikro-orm.io/api/core/interface/LoadCountOptions.md)

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
* [**schema](#schema)

## Properties<!-- -->[**](#Properties)

### [**](#cache)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/IDatabaseDriver.ts#L248)optionalcache

**cache?

<!-- -->

: number | boolean | \[string, number]

### [**](#comments)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/IDatabaseDriver.ts#L258)optionalcomments

**comments?

<!-- -->

: string | string\[]

sql only

### [**](#connectionType)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/IDatabaseDriver.ts#L253)optionalconnectionType

**connectionType?

<!-- -->

: [ConnectionType](https://mikro-orm.io/api/core.md#ConnectionType)

### [**](#ctx)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/IDatabaseDriver.ts#L252)optionalctx

**ctx?

<!-- -->

: any

### [**](#filters)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/IDatabaseDriver.ts#L244)optionalfilters

**filters?

<!-- -->

: [FilterOptions](https://mikro-orm.io/api/core.md#FilterOptions)

### [**](#flushMode)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/IDatabaseDriver.ts#L254)optionalflushMode

**flushMode?

<!-- -->

: always | [FlushMode](https://mikro-orm.io/api/core/enum/FlushMode.md) | commit | auto

### [**](#groupBy)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/IDatabaseDriver.ts#L246)optionalgroupBy

**groupBy?

<!-- -->

: string | readonly

<!-- -->

string\[]

### [**](#having)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/IDatabaseDriver.ts#L247)optionalhaving

**having?

<!-- -->

: [QBFilterQuery](https://mikro-orm.io/api/core.md#QBFilterQuery)\<T>

### [**](#hintComments)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/IDatabaseDriver.ts#L260)optionalhintComments

**hintComments?

<!-- -->

: string | string\[]

sql only

### [**](#indexHint)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/IDatabaseDriver.ts#L256)optionalindexHint

**indexHint?

<!-- -->

: string

sql only

### [**](#loggerContext)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/IDatabaseDriver.ts#L261)optionalloggerContext

**loggerContext?

<!-- -->

: [LogContext](https://mikro-orm.io/api/core/interface/LogContext.md)

### [**](#logging)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/IDatabaseDriver.ts#L262)optionallogging

**logging?

<!-- -->

: [LoggingOptions](https://mikro-orm.io/api/core.md#LoggingOptions)

### [**](#populate)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/IDatabaseDriver.ts#L249)optionalpopulate

**populate?

<!-- -->

: [Populate](https://mikro-orm.io/api/core.md#Populate)\<T, P>

### [**](#populateFilter)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/IDatabaseDriver.ts#L251)optionalpopulateFilter

**populateFilter?

<!-- -->

: [ObjectQuery](https://mikro-orm.io/api/core.md#ObjectQuery)\<T>

### [**](#populateWhere)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/IDatabaseDriver.ts#L250)optionalpopulateWhere

**populateWhere?

<!-- -->

: [ObjectQuery](https://mikro-orm.io/api/core.md#ObjectQuery)\<T> | [PopulateHint](https://mikro-orm.io/api/core/enum/PopulateHint.md) | infer | all

### [**](#schema)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/IDatabaseDriver.ts#L245)optionalschema

**schema?

<!-- -->

: string
