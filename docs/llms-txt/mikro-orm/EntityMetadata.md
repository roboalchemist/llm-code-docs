# Source: https://mikro-orm.io/api/core/class/EntityMetadata.md

# EntityMetadata<!-- --> \<T>

## Index[**](#Index)

### Constructors

* [**constructor](#constructor)

### Properties

* [**abstract](#abstract)
* [**bidirectionalRelations](#bidirectionalRelations)
* [**checks](#checks)
* [**class](#class)
* [**className](#className)
* [**collection](#collection)
* [**comment](#comment)
* [**comparableProps](#comparableProps)
* [**compositePK](#compositePK)
* [**concurrencyCheckKeys](#concurrencyCheckKeys)
* [**constructorParams](#constructorParams)
* [**definedProperties](#definedProperties)
* [**discriminatorColumn](#discriminatorColumn)
* [**discriminatorMap](#discriminatorMap)
* [**discriminatorValue](#discriminatorValue)
* [**embeddable](#embeddable)
* [**expression](#expression)
* [**extends](#extends)
* [**filters](#filters)
* [**forceConstructor](#forceConstructor)
* [**getterProps](#getterProps)
* [**hasTriggers](#hasTriggers)
* [**hasUniqueProps](#hasUniqueProps)
* [**hooks](#hooks)
* [**hydrateProps](#hydrateProps)
* [**indexes](#indexes)
* [**name](#name)
* [**path](#path)
* [**pivotTable](#pivotTable)
* [**polymorphs](#polymorphs)
* [**primaryKeys](#primaryKeys)
* [**properties](#properties)
* [**propertyOrder](#propertyOrder)
* [**props](#props)
* [**prototype](#prototype)
* [**readonly](#readonly)
* [**referencingProperties](#referencingProperties)
* [**relations](#relations)
* [**repository](#repository)
* [**repositoryClass](#repositoryClass)
* [**root](#root)
* [**schema](#schema)
* [**selfReferencing](#selfReferencing)
* [**serializedPrimaryKey](#serializedPrimaryKey)
* [**simplePK](#simplePK)
* [**tableName](#tableName)
* [**toJsonParams](#toJsonParams)
* [**trackingProps](#trackingProps)
* [**uniqueProps](#uniqueProps)
* [**uniques](#uniques)
* [**useCache](#useCache)
* [**versionProperty](#versionProperty)
* [**virtual](#virtual)

### Accessors

* [**tableName](#tableName)

### Methods

* [**addProperty](#addProperty)
* [**createColumnMappingObject](#createColumnMappingObject)
* [**getPrimaryProp](#getPrimaryProp)
* [**getPrimaryProps](#getPrimaryProps)
* [**removeProperty](#removeProperty)
* [**sync](#sync)

## Constructors<!-- -->[**](#Constructors)

### [**](#constructor)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L592)constructor

* ****new EntityMetadata**\<T>(meta): [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<T>

- #### Parameters

  * ##### meta: Partial<[EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<any>> = <!-- -->{}

  #### Returns [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<T>

## Properties<!-- -->[**](#Properties)

### [**](#abstract)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L853)abstract

**abstract: boolean

### [**](#bidirectionalRelations)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L838)bidirectionalRelations

**bidirectionalRelations: [EntityProperty](https://mikro-orm.io/api/core/interface/EntityProperty.md)\<T, any>\[]

### [**](#checks)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L847)checks

**checks: CheckConstraint\<T>\[]

### [**](#class)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L852)class

**class: [EntityClass](https://mikro-orm.io/api/core.md#EntityClass)\<T>

### [**](#className)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L811)className

**className: string

### [**](#collection)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L827)collection

**collection: string

### [**](#comment)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L856)optionalcomment

**comment?

<!-- -->

: string

### [**](#comparableProps)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L840)comparableProps

**comparableProps: [EntityProperty](https://mikro-orm.io/api/core/interface/EntityProperty.md)\<T, any>\[]

### [**](#compositePK)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L831)compositePK

**compositePK: boolean

### [**](#concurrencyCheckKeys)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L833)concurrencyCheckKeys

**concurrencyCheckKeys: Set<[EntityKey](https://mikro-orm.io/api/core.md#EntityKey)\<T, false>>

### [**](#constructorParams)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L823)constructorParams

**constructorParams: [EntityKey](https://mikro-orm.io/api/core.md#EntityKey)\<T, false>\[]

### [**](#definedProperties)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L862)definedProperties

**definedProperties: [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)\<any>

### [**](#discriminatorColumn)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L819)optionaldiscriminatorColumn

**discriminatorColumn?

<!-- -->

: [AnyString](https://mikro-orm.io/api/core.md#AnyString) | [EntityKey](https://mikro-orm.io/api/core.md#EntityKey)\<T, false>

### [**](#discriminatorMap)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L821)optionaldiscriminatorMap

**discriminatorMap?

<!-- -->

: [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)\<string>

### [**](#discriminatorValue)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L820)optionaldiscriminatorValue

**discriminatorValue?

<!-- -->

: string | number

### [**](#embeddable)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L822)embeddable

**embeddable: boolean

### [**](#expression)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L818)optionalexpression

**expression?

<!-- -->

: string | (em, where, options) => [MaybePromise](https://mikro-orm.io/api/core.md#MaybePromise)\<string | object>

### [**](#extends)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L826)extends

**extends: string

### [**](#filters)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L855)filters

**filters: [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)\<FilterDef>

### [**](#forceConstructor)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L824)forceConstructor

**forceConstructor: boolean

### [**](#getterProps)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L844)getterProps

**getterProps: [EntityProperty](https://mikro-orm.io/api/core/interface/EntityProperty.md)\<T, any>\[]

### [**](#hasTriggers)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L864)optionalhasTriggers

**hasTriggers?

<!-- -->

: boolean

### [**](#hasUniqueProps)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L858)optionalhasUniqueProps

**hasUniqueProps?

<!-- -->

: boolean

### [**](#hooks)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L850)hooks

**hooks: { afterCreate: undefined | (undefined | keyof

<!-- -->

T | (args) => void | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void>)\[]; afterDelete: undefined | (undefined | keyof

<!-- -->

T | (args) => void | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void>)\[]; afterFlush: undefined | (undefined | keyof

<!-- -->

T | (args) => void | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void>)\[]; afterTransactionCommit: undefined | (undefined | keyof

<!-- -->

T | (args) => void | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void>)\[]; afterTransactionRollback: undefined | (undefined | keyof

<!-- -->

T | (args) => void | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void>)\[]; afterTransactionStart: undefined | (undefined | keyof

<!-- -->

T | (args) => void | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void>)\[]; afterUpdate: undefined | (undefined | keyof

<!-- -->

T | (args) => void | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void>)\[]; afterUpsert: undefined | (undefined | keyof

<!-- -->

T | (args) => void | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void>)\[]; beforeCreate: undefined | (undefined | keyof

<!-- -->

T | (args) => void | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void>)\[]; beforeDelete: undefined | (undefined | keyof

<!-- -->

T | (args) => void | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void>)\[]; beforeFlush: undefined | (undefined | keyof

<!-- -->

T | (args) => void | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void>)\[]; beforeTransactionCommit: undefined | (undefined | keyof

<!-- -->

T | (args) => void | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void>)\[]; beforeTransactionRollback: undefined | (undefined | keyof

<!-- -->

T | (args) => void | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void>)\[]; beforeTransactionStart: undefined | (undefined | keyof

<!-- -->

T | (args) => void | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void>)\[]; beforeUpdate: undefined | (undefined | keyof

<!-- -->

T | (args) => void | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void>)\[]; beforeUpsert: undefined | (undefined | keyof

<!-- -->

T | (args) => void | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void>)\[]; onFlush: undefined | (undefined | keyof

<!-- -->

T | (args) => void | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void>)\[]; onInit: undefined | (undefined | keyof

<!-- -->

T | (args) => void | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void>)\[]; onLoad: undefined | (undefined | keyof

<!-- -->

T | (args) => void | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void>)\[] }

#### Type declaration

* ##### afterCreate: undefined | (undefined | keyof<!-- --> T | (args) => void | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void>)\[]
* ##### afterDelete: undefined | (undefined | keyof<!-- --> T | (args) => void | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void>)\[]
* ##### afterFlush: undefined | (undefined | keyof<!-- --> T | (args) => void | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void>)\[]
* ##### afterTransactionCommit: undefined | (undefined | keyof<!-- --> T | (args) => void | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void>)\[]
* ##### afterTransactionRollback: undefined | (undefined | keyof<!-- --> T | (args) => void | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void>)\[]
* ##### afterTransactionStart: undefined | (undefined | keyof<!-- --> T | (args) => void | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void>)\[]
* ##### afterUpdate: undefined | (undefined | keyof<!-- --> T | (args) => void | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void>)\[]
* ##### afterUpsert: undefined | (undefined | keyof<!-- --> T | (args) => void | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void>)\[]
* ##### beforeCreate: undefined | (undefined | keyof<!-- --> T | (args) => void | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void>)\[]
* ##### beforeDelete: undefined | (undefined | keyof<!-- --> T | (args) => void | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void>)\[]
* ##### beforeFlush: undefined | (undefined | keyof<!-- --> T | (args) => void | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void>)\[]
* ##### beforeTransactionCommit: undefined | (undefined | keyof<!-- --> T | (args) => void | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void>)\[]
* ##### beforeTransactionRollback: undefined | (undefined | keyof<!-- --> T | (args) => void | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void>)\[]
* ##### beforeTransactionStart: undefined | (undefined | keyof<!-- --> T | (args) => void | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void>)\[]
* ##### beforeUpdate: undefined | (undefined | keyof<!-- --> T | (args) => void | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void>)\[]
* ##### beforeUpsert: undefined | (undefined | keyof<!-- --> T | (args) => void | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void>)\[]
* ##### onFlush: undefined | (undefined | keyof<!-- --> T | (args) => void | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void>)\[]
* ##### onInit: undefined | (undefined | keyof<!-- --> T | (args) => void | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void>)\[]
* ##### onLoad: undefined | (undefined | keyof<!-- --> T | (args) => void | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void>)\[]

### [**](#hydrateProps)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L842)hydrateProps

**hydrateProps: [EntityProperty](https://mikro-orm.io/api/core/interface/EntityProperty.md)\<T, any>\[]

### [**](#indexes)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L845)indexes

**indexes: { expression?

<!-- -->

: string | [IndexCallback](https://mikro-orm.io/api/core.md#IndexCallback)\<T>; name?

<!-- -->

: string; options?

<!-- -->

: [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)\<any>; properties?

<!-- -->

: [EntityKey](https://mikro-orm.io/api/core.md#EntityKey)\<T, false> | [EntityKey](https://mikro-orm.io/api/core.md#EntityKey)\<T, false>\[]; type?

<!-- -->

: string }\[]

### [**](#name)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L810)optionalname

**name?

<!-- -->

: string

### [**](#path)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L828)path

**path: string

### [**](#pivotTable)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L814)optionalpivotTable

**pivotTable?

<!-- -->

: boolean

### [**](#polymorphs)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L860)optionalpolymorphs

**polymorphs?

<!-- -->

: [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<any>\[]

### [**](#primaryKeys)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L829)primaryKeys

**primaryKeys: [EntityKey](https://mikro-orm.io/api/core.md#EntityKey)\<T, false>\[]

### [**](#properties)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L835)properties

**properties: { \[ K in string ]: [EntityProperty](https://mikro-orm.io/api/core/interface/EntityProperty.md)\<T, any> }

### [**](#propertyOrder)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L590)readonlypropertyOrder

**propertyOrder: Map\<string, number> =

<!-- -->

...

### [**](#props)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L836)props

**props: [EntityProperty](https://mikro-orm.io/api/core/interface/EntityProperty.md)\<T, any>\[]

### [**](#prototype)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L851)prototype

**prototype: T

### [**](#readonly)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L859)optionalreadonly

**readonly?

<!-- -->

: boolean

### [**](#referencingProperties)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L839)referencingProperties

**referencingProperties: { meta: [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<T>; prop: [EntityProperty](https://mikro-orm.io/api/core/interface/EntityProperty.md)\<T, any> }\[]

### [**](#relations)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L837)relations

**relations: [EntityProperty](https://mikro-orm.io/api/core/interface/EntityProperty.md)\<T, any>\[]

### [**](#repository)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L849)repository

**repository: () => [EntityClass](https://mikro-orm.io/api/core.md#EntityClass)<[EntityRepository](https://mikro-orm.io/api/core/class/EntityRepository.md)\<any>>

#### Type declaration

* * **(): [EntityClass](https://mikro-orm.io/api/core.md#EntityClass)<[EntityRepository](https://mikro-orm.io/api/core/class/EntityRepository.md)\<any>>

  - #### Returns [EntityClass](https://mikro-orm.io/api/core.md#EntityClass)<[EntityRepository](https://mikro-orm.io/api/core/class/EntityRepository.md)\<any>>

### [**](#repositoryClass)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L848)optionalrepositoryClass

**repositoryClass?

<!-- -->

: string

### [**](#root)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L861)root

**root: [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<T>

### [**](#schema)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L813)optionalschema

**schema?

<!-- -->

: string

### [**](#selfReferencing)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L857)optionalselfReferencing

**selfReferencing?

<!-- -->

: boolean

### [**](#serializedPrimaryKey)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L834)serializedPrimaryKey

**serializedPrimaryKey: [EntityKey](https://mikro-orm.io/api/core.md#EntityKey)\<T, false>

### [**](#simplePK)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L830)simplePK

**simplePK: boolean

### [**](#tableName)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L660)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L664)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L812)tableName

**tableName: string

### [**](#toJsonParams)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L825)toJsonParams

**toJsonParams: string\[]

### [**](#trackingProps)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L841)trackingProps

**trackingProps: [EntityProperty](https://mikro-orm.io/api/core/interface/EntityProperty.md)\<T, any>\[]

### [**](#uniqueProps)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L843)uniqueProps

**uniqueProps: [EntityProperty](https://mikro-orm.io/api/core/interface/EntityProperty.md)\<T, any>\[]

### [**](#uniques)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L846)uniques

**uniques: { deferMode?

<!-- -->

: [DeferMode](https://mikro-orm.io/api/core/enum/DeferMode.md) | immediate | deferred; expression?

<!-- -->

: string | [IndexCallback](https://mikro-orm.io/api/core.md#IndexCallback)\<T>; name?

<!-- -->

: string; options?

<!-- -->

: [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)\<any>; properties?

<!-- -->

: [EntityKey](https://mikro-orm.io/api/core.md#EntityKey)\<T, false> | [EntityKey](https://mikro-orm.io/api/core.md#EntityKey)\<T, false>\[] }\[]

### [**](#useCache)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L854)useCache

**useCache: boolean

### [**](#versionProperty)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L832)versionProperty

**versionProperty: [EntityKey](https://mikro-orm.io/api/core.md#EntityKey)\<T, false>

### [**](#virtual)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L815)optionalvirtual

**virtual?

<!-- -->

: boolean

## Accessors<!-- -->[**](#Accessors)

### [**](#tableName)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L660)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L664)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L812)tableName

* **get tableName(): string
* **set tableName(name): void

- #### Returns string

- #### Parameters

  * ##### name: string

  #### Returns void

## Methods<!-- -->[**](#Methods)

### [**](#addProperty)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L606)addProperty

* ****addProperty**(prop, sync): void

- #### Parameters

  * ##### prop: Partial<[EntityProperty](https://mikro-orm.io/api/core/interface/EntityProperty.md)\<T, any>>
  * ##### sync: boolean = <!-- -->true

  #### Returns void

### [**](#createColumnMappingObject)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L650)createColumnMappingObject

* ****createColumnMappingObject**(): [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)\<any>

- #### Returns [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)\<any>

### [**](#getPrimaryProp)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L646)getPrimaryProp

* ****getPrimaryProp**(): [EntityProperty](https://mikro-orm.io/api/core/interface/EntityProperty.md)\<T, any>

- #### Returns [EntityProperty](https://mikro-orm.io/api/core/interface/EntityProperty.md)\<T, any>

### [**](#getPrimaryProps)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L630)getPrimaryProps

* ****getPrimaryProps**(flatten): [EntityProperty](https://mikro-orm.io/api/core/interface/EntityProperty.md)\<T, any>\[]

- #### Parameters

  * ##### flatten: boolean = <!-- -->false

  #### Returns [EntityProperty](https://mikro-orm.io/api/core/interface/EntityProperty.md)\<T, any>\[]

### [**](#removeProperty)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L620)removeProperty

* ****removeProperty**(name, sync): void

- #### Parameters

  * ##### name: string
  * ##### sync: boolean = <!-- -->true

  #### Returns void

### [**](#sync)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L668)sync

* ****sync**(initIndexes): void

- #### Parameters

  * ##### initIndexes: boolean = <!-- -->false

  #### Returns void
