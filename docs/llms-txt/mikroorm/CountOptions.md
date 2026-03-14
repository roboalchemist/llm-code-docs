# Source: https://mikro-orm.io/api/core/interface/CountOptions.md

# CountOptions<!-- --> \<T, P>

### Hierarchy

* *CountOptions*
  * [LoadCountOptions](https://mikro-orm.io/api/core/interface/LoadCountOptions.md)

## Index[**](#index)

### Properties

* [**cache](#cache)
* [**collation](#collation)
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
* [**maxTimeMS](#maxTimeMS)
* [**populate](#populate)
* [**populateFilter](#populateFilter)
* [**populateWhere](#populateWhere)
* [**schema](#schema)
* [**unionWhere](#unionWhere)
* [**unionWhereStrategy](#unionWhereStrategy)

## Properties<!-- -->[**](#properties)

### [**](#cache)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/IDatabaseDriver.ts#L419)optionalcache

**cache?

<!-- -->

: number | boolean | \[string, number]

### [**](#collation)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/IDatabaseDriver.ts#L437)optionalcollation

**collation?

<!-- -->

: string | [CollationOptions](https://mikro-orm.io/api/core/interface/CollationOptions.md)

SQL: collation name string applied as COLLATE; MongoDB: CollationOptions object.

### [**](#comments)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/IDatabaseDriver.ts#L433)optionalcomments

**comments?

<!-- -->

: string | string\[]

sql only

### [**](#connectionType)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/IDatabaseDriver.ts#L428)optionalconnectionType

**connectionType?

<!-- -->

: [ConnectionType](https://mikro-orm.io/api/core.md#ConnectionType)

### [**](#ctx)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/IDatabaseDriver.ts#L427)optionalctx

**ctx?

<!-- -->

: any

### [**](#filters)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/IDatabaseDriver.ts#L415)optionalfilters

**filters?

<!-- -->

: [FilterOptions](https://mikro-orm.io/api/core.md#FilterOptions)

### [**](#flushMode)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/IDatabaseDriver.ts#L429)optionalflushMode

**flushMode?

<!-- -->

: always | [FlushMode](https://mikro-orm.io/api/core/enum/FlushMode.md) | commit | auto

### [**](#groupBy)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/IDatabaseDriver.ts#L417)optionalgroupBy

**groupBy?

<!-- -->

: string | readonly

<!-- -->

string\[]

### [**](#having)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/IDatabaseDriver.ts#L418)optionalhaving

**having?

<!-- -->

: [FilterQuery](https://mikro-orm.io/api/core.md#FilterQuery)\<T>

### [**](#hintComments)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/IDatabaseDriver.ts#L435)optionalhintComments

**hintComments?

<!-- -->

: string | string\[]

sql only

### [**](#indexHint)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/IDatabaseDriver.ts#L431)optionalindexHint

**indexHint?

<!-- -->

: string | [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)

SQL: appended to FROM clause (e.g. `'force index(my_index)'`); MongoDB: index name or spec passed as `hint`.

### [**](#loggerContext)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/IDatabaseDriver.ts#L440)optionalloggerContext

**loggerContext?

<!-- -->

: [LogContext](https://mikro-orm.io/api/core/interface/LogContext.md)

### [**](#logging)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/IDatabaseDriver.ts#L441)optionallogging

**logging?

<!-- -->

: [LoggingOptions](https://mikro-orm.io/api/core.md#LoggingOptions)

### [**](#maxTimeMS)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/IDatabaseDriver.ts#L439)optionalmaxTimeMS

**maxTimeMS?

<!-- -->

: number

mongodb only

### [**](#populate)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/IDatabaseDriver.ts#L420)optionalpopulate

**populate?

<!-- -->

: [Populate](https://mikro-orm.io/api/core.md#Populate)\<T, P>

### [**](#populateFilter)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/IDatabaseDriver.ts#L422)optionalpopulateFilter

**populateFilter?

<!-- -->

: [ObjectQuery](https://mikro-orm.io/api/core.md#ObjectQuery)\<T>

### [**](#populateWhere)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/IDatabaseDriver.ts#L421)optionalpopulateWhere

**populateWhere?

<!-- -->

: [PopulateHint](https://mikro-orm.io/api/core/enum/PopulateHint.md) | infer | all | [ObjectQuery](https://mikro-orm.io/api/core.md#ObjectQuery)\<T>

### [**](#schema)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/IDatabaseDriver.ts#L416)optionalschema

**schema?

<!-- -->

: string

### [**](#unionWhere)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/IDatabaseDriver.ts#L424)optionalunionWhere

**unionWhere?

<!-- -->

: [ObjectQuery](https://mikro-orm.io/api/core.md#ObjectQuery)\<T>\[]

* **@see**

  FindOptions.unionWhere

### [**](#unionWhereStrategy)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/IDatabaseDriver.ts#L426)optionalunionWhereStrategy

**unionWhereStrategy?

<!-- -->

: union-all | union

* **@see**

  FindOptions.unionWhereStrategy
