# Source: https://mikro-orm.io/api/core/interface/InitCollectionOptions.md

# InitCollectionOptions<!-- --> \<T, P, F, E>

### Hierarchy

* [EntityLoaderOptions](https://mikro-orm.io/api/core.md#EntityLoaderOptions)\<T, F, E>
  * *InitCollectionOptions*

## Index[**](#Index)

### Properties

* [**connectionType](#connectionType)
* [**convertCustomTypes](#convertCustomTypes)
* [**dataloader](#dataloader)
* [**exclude](#exclude)
* [**fields](#fields)
* [**filters](#filters)
* [**ignoreLazyScalarProperties](#ignoreLazyScalarProperties)
* [**lockMode](#lockMode)
* [**logging](#logging)
* [**lookup](#lookup)
* [**orderBy](#orderBy)
* [**populate](#populate)
* [**populateWhere](#populateWhere)
* [**ref](#ref)
* [**refresh](#refresh)
* [**schema](#schema)
* [**strategy](#strategy)
* [**validate](#validate)
* [**where](#where)

## Properties<!-- -->[**](#Properties)

### [**](#connectionType)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/EntityLoader.ts#L51)optionalinheritedconnectionType

**connectionType?

<!-- -->

: [ConnectionType](https://mikro-orm.io/api/core.md#ConnectionType)

Inherited from EntityLoaderOptions.connectionType

### [**](#convertCustomTypes)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/EntityLoader.ts#L45)optionalinheritedconvertCustomTypes

**convertCustomTypes?

<!-- -->

: boolean

Inherited from EntityLoaderOptions.convertCustomTypes

### [**](#dataloader)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/Collection.ts#L497)optionaldataloader

**dataloader?

<!-- -->

: boolean

### [**](#exclude)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/EntityLoader.ts#L40)optionalinheritedexclude

**exclude?

<!-- -->

: readonly

<!-- -->

[EntityField](https://mikro-orm.io/api/core.md#EntityField)\<T, E>\[]

Inherited from EntityLoaderOptions.exclude

### [**](#fields)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/EntityLoader.ts#L39)optionalinheritedfields

**fields?

<!-- -->

: readonly

<!-- -->

[EntityField](https://mikro-orm.io/api/core.md#EntityField)\<T, F>\[]

Inherited from EntityLoaderOptions.fields

### [**](#filters)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/EntityLoader.ts#L47)optionalinheritedfilters

**filters?

<!-- -->

: [FilterOptions](https://mikro-orm.io/api/core.md#FilterOptions)

Inherited from EntityLoaderOptions.filters

### [**](#ignoreLazyScalarProperties)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/EntityLoader.ts#L46)optionalinheritedignoreLazyScalarProperties

**ignoreLazyScalarProperties?

<!-- -->

: boolean

Inherited from EntityLoaderOptions.ignoreLazyScalarProperties

### [**](#lockMode)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/EntityLoader.ts#L49)optionalinheritedlockMode

**lockMode?

<!-- -->

: NONE | PESSIMISTIC\_READ | PESSIMISTIC\_WRITE | PESSIMISTIC\_PARTIAL\_WRITE | PESSIMISTIC\_WRITE\_OR\_FAIL | PESSIMISTIC\_PARTIAL\_READ | PESSIMISTIC\_READ\_OR\_FAIL

Inherited from EntityLoaderOptions.lockMode

### [**](#logging)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/EntityLoader.ts#L52)optionalinheritedlogging

**logging?

<!-- -->

: [LoggingOptions](https://mikro-orm.io/api/core.md#LoggingOptions)

Inherited from EntityLoaderOptions.logging

### [**](#lookup)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/EntityLoader.ts#L44)optionalinheritedlookup

**lookup?

<!-- -->

: boolean

Inherited from EntityLoaderOptions.lookup

### [**](#orderBy)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/EntityLoader.ts#L41)optionalinheritedorderBy

**orderBy?

<!-- -->

: [QueryOrderMap](https://mikro-orm.io/api/core.md#QueryOrderMap)\<T> | [QueryOrderMap](https://mikro-orm.io/api/core.md#QueryOrderMap)\<T>\[]

Inherited from EntityLoaderOptions.orderBy

### [**](#populate)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/Collection.ts#L498)optionalpopulate

**populate?

<!-- -->

: [Populate](https://mikro-orm.io/api/core.md#Populate)\<T, P>

### [**](#populateWhere)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/EntityLoader.ts#L38)optionalinheritedpopulateWhere

**populateWhere?

<!-- -->

: [PopulateHint](https://mikro-orm.io/api/core/enum/PopulateHint.md) | infer | all

Inherited from EntityLoaderOptions.populateWhere

### [**](#ref)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/Collection.ts#L499)optionalref

**ref?

<!-- -->

: boolean

### [**](#refresh)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/EntityLoader.ts#L42)optionalinheritedrefresh

**refresh?

<!-- -->

: boolean

Inherited from EntityLoaderOptions.refresh

### [**](#schema)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/EntityLoader.ts#L50)optionalinheritedschema

**schema?

<!-- -->

: string

Inherited from EntityLoaderOptions.schema

### [**](#strategy)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/EntityLoader.ts#L48)optionalinheritedstrategy

**strategy?

<!-- -->

: [LoadStrategy](https://mikro-orm.io/api/core/enum/LoadStrategy.md)

Inherited from EntityLoaderOptions.strategy

### [**](#validate)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/EntityLoader.ts#L43)optionalinheritedvalidate

**validate?

<!-- -->

: boolean

Inherited from EntityLoaderOptions.validate

### [**](#where)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/EntityLoader.ts#L37)optionalinheritedwhere

**where?

<!-- -->

: [FilterQuery](https://mikro-orm.io/api/core.md#FilterQuery)\<T>

Inherited from EntityLoaderOptions.where
