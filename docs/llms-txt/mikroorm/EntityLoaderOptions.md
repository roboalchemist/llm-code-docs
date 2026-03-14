# Source: https://mikro-orm.io/api/core/interface/EntityLoaderOptions.md

# EntityLoaderOptions<!-- --> \<Entity, Fields, Excludes>

### Hierarchy

* *EntityLoaderOptions*
  * [InitCollectionOptions](https://mikro-orm.io/api/core/interface/InitCollectionOptions.md)

## Index[**](#index)

### Properties

* [**connectionType](#connectionType)
* [**convertCustomTypes](#convertCustomTypes)
* [**exclude](#exclude)
* [**fields](#fields)
* [**filters](#filters)
* [**ignoreLazyScalarProperties](#ignoreLazyScalarProperties)
* [**lockMode](#lockMode)
* [**logging](#logging)
* [**lookup](#lookup)
* [**orderBy](#orderBy)
* [**populateWhere](#populateWhere)
* [**refresh](#refresh)
* [**schema](#schema)
* [**strategy](#strategy)
* [**validate](#validate)
* [**where](#where)

## Properties<!-- -->[**](#properties)

### [**](#connectionType)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/EntityLoader.ts#L57)optionalconnectionType

**connectionType?

<!-- -->

: [ConnectionType](https://mikro-orm.io/api/core.md#ConnectionType)

### [**](#convertCustomTypes)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/EntityLoader.ts#L51)optionalconvertCustomTypes

**convertCustomTypes?

<!-- -->

: boolean

### [**](#exclude)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/EntityLoader.ts#L44)optionalexclude

**exclude?

<!-- -->

: readonly

<!-- -->

[AutoPath](https://mikro-orm.io/api/core.md#AutoPath)\<Entity, Excludes, never, 9>\[]

### [**](#fields)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/EntityLoader.ts#L43)optionalfields

**fields?

<!-- -->

: readonly

<!-- -->

[AutoPath](https://mikro-orm.io/api/core.md#AutoPath)\<Entity, Fields, \*, 9>\[]

### [**](#filters)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/EntityLoader.ts#L53)optionalfilters

**filters?

<!-- -->

: [FilterOptions](https://mikro-orm.io/api/core.md#FilterOptions)

### [**](#ignoreLazyScalarProperties)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/EntityLoader.ts#L52)optionalignoreLazyScalarProperties

**ignoreLazyScalarProperties?

<!-- -->

: boolean

### [**](#lockMode)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/EntityLoader.ts#L55)optionallockMode

**lockMode?

<!-- -->

: NONE | PESSIMISTIC\_READ | PESSIMISTIC\_WRITE | PESSIMISTIC\_PARTIAL\_WRITE | PESSIMISTIC\_WRITE\_OR\_FAIL | PESSIMISTIC\_PARTIAL\_READ | PESSIMISTIC\_READ\_OR\_FAIL

### [**](#logging)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/EntityLoader.ts#L58)optionallogging

**logging?

<!-- -->

: [LoggingOptions](https://mikro-orm.io/api/core.md#LoggingOptions)

### [**](#lookup)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/EntityLoader.ts#L50)optionallookup

**lookup?

<!-- -->

: boolean

### [**](#orderBy)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/EntityLoader.ts#L47)optionalorderBy

**orderBy?

<!-- -->

: [QueryOrderMap](https://mikro-orm.io/api/core.md#QueryOrderMap)\<Entity> | [QueryOrderMap](https://mikro-orm.io/api/core.md#QueryOrderMap)\<Entity>\[]

### [**](#populateWhere)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/EntityLoader.ts#L46)optionalpopulateWhere

**populateWhere?

<!-- -->

: [PopulateHint](https://mikro-orm.io/api/core/enum/PopulateHint.md) | infer | all

### [**](#refresh)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/EntityLoader.ts#L48)optionalrefresh

**refresh?

<!-- -->

: boolean

### [**](#schema)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/EntityLoader.ts#L56)optionalschema

**schema?

<!-- -->

: string

### [**](#strategy)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/EntityLoader.ts#L54)optionalstrategy

**strategy?

<!-- -->

: [LoadStrategy](https://mikro-orm.io/api/core/enum/LoadStrategy.md) | select-in | joined | balanced

### [**](#validate)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/EntityLoader.ts#L49)optionalvalidate

**validate?

<!-- -->

: boolean

### [**](#where)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/EntityLoader.ts#L45)optionalwhere

**where?

<!-- -->

: [FilterQuery](https://mikro-orm.io/api/core.md#FilterQuery)\<Entity>
