# Source: https://mikro-orm.io/api/core/class/EntityMetadata.md

# EntityMetadata<!-- --> \<Entity, Class>

## Index[**](#index)

### Constructors

* [**constructor](#constructor)

### Properties

* [**abstract](#abstract)
* [**allTPTDescendants](#allTPTDescendants)
* [**bidirectionalRelations](#bidirectionalrelations)
* [**class](#class)
* [**className](#classname)
* [**collection](#collection)
* [**comment](#comment)
* [**comparableProps](#comparableprops)
* [**compositePK](#compositepk)
* [**concurrencyCheckKeys](#concurrencycheckkeys)
* [**constructorParams](#constructorParams)
* [**definedProperties](#definedproperties)
* [**discriminatorColumn](#discriminatorColumn)
* [**discriminatorMap](#discriminatorMap)
* [**discriminatorValue](#discriminatorValue)
* [**embeddable](#embeddable)
* [**expression](#expression)
* [**extends](#extends)
* [**filters](#filters)
* [**forceConstructor](#forceconstructor)
* [**getterProps](#getterprops)
* [**hasTriggers](#hasTriggers)
* [**hasUniqueProps](#hasUniqueProps)
* [**hooks](#hooks)
* [**hydrateProps](#hydrateprops)
* [**checks](#checks)
* [**indexes](#indexes)
* [**inheritanceType](#inheritanceType)
* [**materialized](#materialized)
* [**name](#name)
* [**orderBy](#orderBy)
* [**ownProps](#ownProps)
* [**path](#path)
* [**pivotTable](#pivotTable)
* [**polymorphicDiscriminatorMap](#polymorphicDiscriminatorMap)
* [**polymorphs](#polymorphs)
* [**primaryKeys](#primarykeys)
* [**properties](#properties)
* [**propertyOrder](#propertyOrder)
* [**props](#props)
* [**prototype](#prototype)
* [**readonly](#readonly)
* [**referencingProperties](#referencingproperties)
* [**relations](#relations)
* [**repository](#repository)
* [**repositoryClass](#repositoryClass)
* [**root](#root)
* [**selfReferencing](#selfReferencing)
* [**serializedPrimaryKey](#serializedPrimaryKey)
* [**schema](#schema)
* [**simplePK](#simplepk)
* [**tableName](#tablename)
* [**tptDiscriminatorColumn](#tptDiscriminatorColumn)
* [**tptChildren](#tptChildren)
* [**tptInverseProp](#tptInverseProp)
* [**tptParent](#tptParent)
* [**tptParentProp](#tptParentProp)
* [**trackingProps](#trackingprops)
* [**uniqueProps](#uniqueprops)
* [**uniques](#uniques)
* [**validateProps](#validateprops)
* [**versionProperty](#versionproperty)
* [**view](#view)
* [**virtual](#virtual)
* [**withData](#withData)

### Accessors

* [**tableName](#tablename)
* [**uniqueName](#uniquename)

### Methods

* [**addProperty](#addproperty)
* [**createColumnMappingObject](#createcolumnmappingobject)
* [**createSchemaColumnMappingObject](#createschemacolumnmappingobject)
* [**getPrimaryProp](#getprimaryprop)
* [**getPrimaryProps](#getprimaryprops)
* [**removeProperty](#removeproperty)
* [**sync](#sync)

## Constructors<!-- -->[**](#constructors)

### [**](#constructor)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L889)constructor

* ****new EntityMetadata**\<Entity, Class>(meta): [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<Entity, Class>

* #### Parameters

  * ##### meta: Partial<[EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<any, [EntityCtor](https://mikro-orm.io/api/core.md#EntityCtor)\<any>>> = <!-- -->{}

  #### Returns [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<Entity, Class>

## Properties<!-- -->[**](#properties)

### [**](#abstract)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1285)abstract

**abstract: boolean

### [**](#allTPTDescendants)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1303)optionalallTPTDescendants

**allTPTDescendants?

<!-- -->

: [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<any, [EntityCtor](https://mikro-orm.io/api/core.md#EntityCtor)\<any>>\[]

For TPT: all non-abstract descendants, sorted by depth (deepest first). Precomputed during discovery.

### [**](#bidirectionalrelations)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1247)bidirectionalRelations

**bidirectionalRelations: [EntityProperty](https://mikro-orm.io/api/core/interface/EntityProperty.md)\<Entity, any>\[]

### [**](#class)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1284)class

**class: Class

### [**](#classname)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1208)className

**className: string

### [**](#collection)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1236)collection

**collection: string

### [**](#comment)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1287)optionalcomment

**comment?

<!-- -->

: string

### [**](#comparableprops)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1249)comparableProps

**comparableProps: [EntityProperty](https://mikro-orm.io/api/core/interface/EntityProperty.md)\<Entity, any>\[]

### [**](#compositepk)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1240)compositePK

**compositePK: boolean

### [**](#concurrencycheckkeys)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1242)concurrencyCheckKeys

**concurrencyCheckKeys: Set<[EntityKey](https://mikro-orm.io/api/core.md#EntityKey)\<Entity, false>>

### [**](#constructorParams)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1233)optionalconstructorParams

**constructorParams?

<!-- -->

: keyof

<!-- -->

Entity\[]

### [**](#definedproperties)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1293)definedProperties

**definedProperties: [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)\<any>

### [**](#discriminatorColumn)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1229)optionaldiscriminatorColumn

**discriminatorColumn?

<!-- -->

: [EntityKey](https://mikro-orm.io/api/core.md#EntityKey)\<Entity, false> | [AnyString](https://mikro-orm.io/api/core.md#AnyString)

### [**](#discriminatorMap)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1231)optionaldiscriminatorMap

**discriminatorMap?

<!-- -->

: [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)<[EntityClass](https://mikro-orm.io/api/core.md#EntityClass)\<any>>

### [**](#discriminatorValue)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1230)optionaldiscriminatorValue

**discriminatorValue?

<!-- -->

: string | number

### [**](#embeddable)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1232)embeddable

**embeddable: boolean

### [**](#expression)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1221)optionalexpression

**expression?

<!-- -->

: string | (em, where, options, stream) => [MaybePromise](https://mikro-orm.io/api/core.md#MaybePromise)\<string | object | [RawQueryFragment](https://mikro-orm.io/api/core/class/RawQueryFragment.md)\<string>>

### [**](#extends)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1235)optionalextends

**extends?

<!-- -->

: [EntityName](https://mikro-orm.io/api/core.md#EntityName)\<Entity>

### [**](#filters)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1286)filters

**filters: [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)<[FilterDef](https://mikro-orm.io/api/core.md#FilterDef)\<any>>

### [**](#forceconstructor)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1234)forceConstructor

**forceConstructor: boolean

### [**](#getterprops)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1254)getterProps

**getterProps: [EntityProperty](https://mikro-orm.io/api/core/interface/EntityProperty.md)\<Entity, any>\[]

### [**](#hasTriggers)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1313)optionalhasTriggers

**hasTriggers?

<!-- -->

: boolean

### [**](#hasUniqueProps)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1289)optionalhasUniqueProps

**hasUniqueProps?

<!-- -->

: boolean

### [**](#hooks)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1282)hooks

**hooks: { afterCreate: undefined | (undefined | keyof

<!-- -->

Entity | (args) => void | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void>)\[]; afterDelete: undefined | (undefined | keyof

<!-- -->

Entity | (args) => void | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void>)\[]; afterFlush: undefined | (undefined | keyof

<!-- -->

Entity | (args) => void | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void>)\[]; afterTransactionCommit: undefined | (undefined | keyof

<!-- -->

Entity | (args) => void | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void>)\[]; afterTransactionRollback: undefined | (undefined | keyof

<!-- -->

Entity | (args) => void | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void>)\[]; afterTransactionStart: undefined | (undefined | keyof

<!-- -->

Entity | (args) => void | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void>)\[]; afterUpdate: undefined | (undefined | keyof

<!-- -->

Entity | (args) => void | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void>)\[]; afterUpsert: undefined | (undefined | keyof

<!-- -->

Entity | (args) => void | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void>)\[]; beforeCreate: undefined | (undefined | keyof

<!-- -->

Entity | (args) => void | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void>)\[]; beforeDelete: undefined | (undefined | keyof

<!-- -->

Entity | (args) => void | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void>)\[]; beforeFlush: undefined | (undefined | keyof

<!-- -->

Entity | (args) => void | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void>)\[]; beforeTransactionCommit: undefined | (undefined | keyof

<!-- -->

Entity | (args) => void | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void>)\[]; beforeTransactionRollback: undefined | (undefined | keyof

<!-- -->

Entity | (args) => void | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void>)\[]; beforeTransactionStart: undefined | (undefined | keyof

<!-- -->

Entity | (args) => void | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void>)\[]; beforeUpdate: undefined | (undefined | keyof

<!-- -->

Entity | (args) => void | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void>)\[]; beforeUpsert: undefined | (undefined | keyof

<!-- -->

Entity | (args) => void | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void>)\[]; onFlush: undefined | (undefined | keyof

<!-- -->

Entity | (args) => void | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void>)\[]; onInit: undefined | (undefined | keyof

<!-- -->

Entity | (args) => void | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void>)\[]; onLoad: undefined | (undefined | keyof

<!-- -->

Entity | (args) => void | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void>)\[] }

#### Type declaration

* ##### afterCreate: undefined | (undefined | keyof<!-- --> Entity | (args) => void | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void>)\[]

* ##### afterDelete: undefined | (undefined | keyof<!-- --> Entity | (args) => void | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void>)\[]

* ##### afterFlush: undefined | (undefined | keyof<!-- --> Entity | (args) => void | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void>)\[]

* ##### afterTransactionCommit: undefined | (undefined | keyof<!-- --> Entity | (args) => void | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void>)\[]

* ##### afterTransactionRollback: undefined | (undefined | keyof<!-- --> Entity | (args) => void | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void>)\[]

* ##### afterTransactionStart: undefined | (undefined | keyof<!-- --> Entity | (args) => void | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void>)\[]

* ##### afterUpdate: undefined | (undefined | keyof<!-- --> Entity | (args) => void | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void>)\[]

* ##### afterUpsert: undefined | (undefined | keyof<!-- --> Entity | (args) => void | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void>)\[]

* ##### beforeCreate: undefined | (undefined | keyof<!-- --> Entity | (args) => void | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void>)\[]

* ##### beforeDelete: undefined | (undefined | keyof<!-- --> Entity | (args) => void | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void>)\[]

* ##### beforeFlush: undefined | (undefined | keyof<!-- --> Entity | (args) => void | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void>)\[]

* ##### beforeTransactionCommit: undefined | (undefined | keyof<!-- --> Entity | (args) => void | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void>)\[]

* ##### beforeTransactionRollback: undefined | (undefined | keyof<!-- --> Entity | (args) => void | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void>)\[]

* ##### beforeTransactionStart: undefined | (undefined | keyof<!-- --> Entity | (args) => void | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void>)\[]

* ##### beforeUpdate: undefined | (undefined | keyof<!-- --> Entity | (args) => void | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void>)\[]

* ##### beforeUpsert: undefined | (undefined | keyof<!-- --> Entity | (args) => void | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void>)\[]

* ##### onFlush: undefined | (undefined | keyof<!-- --> Entity | (args) => void | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void>)\[]

* ##### onInit: undefined | (undefined | keyof<!-- --> Entity | (args) => void | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void>)\[]

* ##### onLoad: undefined | (undefined | keyof<!-- --> Entity | (args) => void | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void> | (args) => void | Promise\<void>)\[]

### [**](#hydrateprops)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1251)hydrateProps

**hydrateProps: [EntityProperty](https://mikro-orm.io/api/core/interface/EntityProperty.md)\<Entity, any>\[]

### [**](#checks)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1279)checks

**checks: [CheckConstraint](https://mikro-orm.io/api/core/interface/CheckConstraint.md)\<Entity>\[]

### [**](#indexes)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1255)indexes

**indexes: { clustered?

<!-- -->

: boolean; columns?

<!-- -->

: [IndexColumnOptions](https://mikro-orm.io/api/core/interface/IndexColumnOptions.md)\[]; disabled?

<!-- -->

: boolean; expression?

<!-- -->

: string | [IndexCallback](https://mikro-orm.io/api/core.md#IndexCallback)\<Entity>; fillFactor?

<!-- -->

: number; include?

<!-- -->

: [EntityKey](https://mikro-orm.io/api/core.md#EntityKey)\<Entity, false> | [EntityKey](https://mikro-orm.io/api/core.md#EntityKey)\<Entity, false>\[]; invisible?

<!-- -->

: boolean; name?

<!-- -->

: string; options?

<!-- -->

: [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)\<any>; properties?

<!-- -->

: [EntityKey](https://mikro-orm.io/api/core.md#EntityKey)\<Entity, false> | [EntityKey](https://mikro-orm.io/api/core.md#EntityKey)\<Entity, false>\[]; type?

<!-- -->

: string }\[]

### [**](#inheritanceType)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1297)optionalinheritanceType

**inheritanceType?

<!-- -->

: sti | tpt

Inheritance type: 'sti' (Single Table Inheritance) or 'tpt' (Table-Per-Type). Only set on root entities.

### [**](#materialized)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1216)optionalmaterialized

**materialized?

<!-- -->

: boolean

True if this is a materialized view (PostgreSQL only). Requires `view: true`.

### [**](#name)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1207)optionalname

**name?

<!-- -->

: string

### [**](#orderBy)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1318)optionalorderBy

**orderBy?

<!-- -->

: [QueryOrderMap](https://mikro-orm.io/api/core.md#QueryOrderMap)\<Entity> | [QueryOrderMap](https://mikro-orm.io/api/core.md#QueryOrderMap)\<Entity>\[]

Default ordering for this entity. Applied when querying this entity directly or when it's populated as a relation. Combined with other orderings based on precedence.

### [**](#ownProps)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1311)optionalownProps

**ownProps?

<!-- -->

: [EntityProperty](https://mikro-orm.io/api/core/interface/EntityProperty.md)\<Entity, any>\[]

For TPT: properties defined only in THIS entity (not inherited from parent).

### [**](#path)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1237)path

**path: string

### [**](#pivotTable)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1211)optionalpivotTable

**pivotTable?

<!-- -->

: boolean

### [**](#polymorphicDiscriminatorMap)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1295)optionalpolymorphicDiscriminatorMap

**polymorphicDiscriminatorMap?

<!-- -->

: [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)<[EntityClass](https://mikro-orm.io/api/core.md#EntityClass)\<any>>

For polymorphic M:N pivot tables, maps discriminator values to entity classes

### [**](#polymorphs)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1291)optionalpolymorphs

**polymorphs?

<!-- -->

: [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<any, [EntityCtor](https://mikro-orm.io/api/core.md#EntityCtor)\<any>>\[]

### [**](#primarykeys)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1238)primaryKeys

**primaryKeys: [EntityKey](https://mikro-orm.io/api/core.md#EntityKey)\<Entity, false>\[]

### [**](#properties)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1244)properties

**properties: { \[ K in string ]: [EntityProperty](https://mikro-orm.io/api/core/interface/EntityProperty.md)\<Entity, any> }

### [**](#propertyOrder)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L887)readonlypropertyOrder

**propertyOrder: Map\<string, number> =

<!-- -->

...

### [**](#props)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1245)props

**props: [EntityProperty](https://mikro-orm.io/api/core/interface/EntityProperty.md)\<Entity, any>\[]

### [**](#prototype)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1283)prototype

**prototype: Entity

### [**](#readonly)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1290)optionalreadonly

**readonly?

<!-- -->

: boolean

### [**](#referencingproperties)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1248)referencingProperties

**referencingProperties: { meta: [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<Entity, [EntityCtor](https://mikro-orm.io/api/core.md#EntityCtor)\<Entity>>; prop: [EntityProperty](https://mikro-orm.io/api/core/interface/EntityProperty.md)\<Entity, any> }\[]

### [**](#relations)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1246)relations

**relations: [EntityProperty](https://mikro-orm.io/api/core/interface/EntityProperty.md)\<Entity, any>\[]

### [**](#repository)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1281)repository

**repository: () => [EntityClass](https://mikro-orm.io/api/core.md#EntityClass)<[EntityRepository](https://mikro-orm.io/api/core/class/EntityRepository.md)\<any>>

#### Type declaration

* * **(): [EntityClass](https://mikro-orm.io/api/core.md#EntityClass)<[EntityRepository](https://mikro-orm.io/api/core/class/EntityRepository.md)\<any>>

  * #### Returns [EntityClass](https://mikro-orm.io/api/core.md#EntityClass)<[EntityRepository](https://mikro-orm.io/api/core/class/EntityRepository.md)\<any>>

### [**](#repositoryClass)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1280)optionalrepositoryClass

**repositoryClass?

<!-- -->

: string

### [**](#root)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1292)root

**root: [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<Entity, [EntityCtor](https://mikro-orm.io/api/core.md#EntityCtor)\<Entity>>

### [**](#selfReferencing)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1288)optionalselfReferencing

**selfReferencing?

<!-- -->

: boolean

### [**](#serializedPrimaryKey)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1243)optionalserializedPrimaryKey

**serializedPrimaryKey?

<!-- -->

: [EntityKey](https://mikro-orm.io/api/core.md#EntityKey)\<Entity, false>

### [**](#schema)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1210)optionalschema

**schema?

<!-- -->

: string

### [**](#simplepk)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1239)simplePK

**simplePK: boolean

### [**](#tablename)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1012)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1016)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1209)tableName

**tableName: string

### [**](#tptDiscriminatorColumn)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1309)optionaltptDiscriminatorColumn

**tptDiscriminatorColumn?

<!-- -->

: string

For TPT: virtual discriminator property name (computed at query time, not persisted).

### [**](#tptChildren)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1301)optionaltptChildren

**tptChildren?

<!-- -->

: [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<any, [EntityCtor](https://mikro-orm.io/api/core.md#EntityCtor)\<any>>\[]

For TPT: direct child entities (entities that extend this one).

### [**](#tptInverseProp)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1307)optionaltptInverseProp

**tptInverseProp?

<!-- -->

: [EntityProperty](https://mikro-orm.io/api/core/interface/EntityProperty.md)\<any, any>

For TPT: inverse of tptParentProp, used for joining from parent to child (parent PK → child PK).

### [**](#tptParent)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1299)optionaltptParent

**tptParent?

<!-- -->

: [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<any, [EntityCtor](https://mikro-orm.io/api/core.md#EntityCtor)\<any>>

For TPT: direct parent entity metadata (the entity this one extends).

### [**](#tptParentProp)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1305)optionaltptParentProp

**tptParentProp?

<!-- -->

: [EntityProperty](https://mikro-orm.io/api/core/interface/EntityProperty.md)\<any, any>

For TPT: synthetic property representing the join to the parent table (child PK → parent PK).

### [**](#trackingprops)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1250)trackingProps

**trackingProps: [EntityProperty](https://mikro-orm.io/api/core/interface/EntityProperty.md)\<Entity, any>\[]

### [**](#uniqueprops)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1253)uniqueProps

**uniqueProps: [EntityProperty](https://mikro-orm.io/api/core/interface/EntityProperty.md)\<Entity, any>\[]

### [**](#uniques)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1268)uniques

**uniques: { columns?

<!-- -->

: [IndexColumnOptions](https://mikro-orm.io/api/core/interface/IndexColumnOptions.md)\[]; deferMode?

<!-- -->

: [DeferMode](https://mikro-orm.io/api/core/enum/DeferMode.md) | immediate | deferred; disabled?

<!-- -->

: boolean; expression?

<!-- -->

: string | [IndexCallback](https://mikro-orm.io/api/core.md#IndexCallback)\<Entity>; fillFactor?

<!-- -->

: number; include?

<!-- -->

: [EntityKey](https://mikro-orm.io/api/core.md#EntityKey)\<Entity, false> | [EntityKey](https://mikro-orm.io/api/core.md#EntityKey)\<Entity, false>\[]; name?

<!-- -->

: string; options?

<!-- -->

: [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)\<any>; properties?

<!-- -->

: [EntityKey](https://mikro-orm.io/api/core.md#EntityKey)\<Entity, false> | [EntityKey](https://mikro-orm.io/api/core.md#EntityKey)\<Entity, false>\[] }\[]

### [**](#validateprops)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1252)validateProps

**validateProps: [EntityProperty](https://mikro-orm.io/api/core/interface/EntityProperty.md)\<Entity, any>\[]

### [**](#versionproperty)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1241)versionProperty

**versionProperty: [EntityKey](https://mikro-orm.io/api/core.md#EntityKey)\<Entity, false>

### [**](#view)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1214)optionalview

**view?

<!-- -->

: boolean | { materialized?

<!-- -->

: boolean; withData?

<!-- -->

: boolean }

True if this entity represents a database view (not a virtual entity). Accepts `{ materialized: true }` as input, normalized to `true` during sync.

### [**](#virtual)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1212)optionalvirtual

**virtual?

<!-- -->

: boolean

### [**](#withData)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1218)optionalwithData

**withData?

<!-- -->

: boolean

For materialized views, whether data is populated on creation. Defaults to true.

## Accessors<!-- -->[**](#accessors)

### [**](#tablename)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1012)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1016)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1209)tableName

* **get tableName(): string
* **set tableName(name): void

* #### Returns string

* #### Parameters

  * ##### name: string

  #### Returns void

### [**](#uniquename)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1020)uniqueName

* **get uniqueName(): string

* #### Returns string

## Methods<!-- -->[**](#methods)

### [**](#addproperty)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L910)addProperty

* ****addProperty**(prop): void

* #### Parameters

  * ##### prop: Partial<[EntityProperty](https://mikro-orm.io/api/core/interface/EntityProperty.md)\<Entity, any>>

  #### Returns void

### [**](#createcolumnmappingobject)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L951)createColumnMappingObject

* ****createColumnMappingObject**(alias, toStringAlias): FormulaColumns\<Entity>

* Creates a mapping from property names to field names.

  ***

  #### Parameters

  * ##### optionalalias: string | (prop) => string

    Optional alias to prefix field names. Can be a string (same for all) or a function (per-property). When provided, also adds toString() returning the alias for backwards compatibility with formulas.

  *

  ##### optionaltoStringAlias: string

    Optional alias to return from toString(). Defaults to `alias` when it's a string.

  #### Returns FormulaColumns\<Entity>

### [**](#createschemacolumnmappingobject)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L998)createSchemaColumnMappingObject

* ****createSchemaColumnMappingObject**(): [SchemaColumns](https://mikro-orm.io/api/core.md#SchemaColumns)\<Entity>

* Creates a column mapping for schema callbacks (indexes, checks, generated columns). For TPT entities, only includes properties that belong to the current table (ownProps).

  ***

  #### Returns [SchemaColumns](https://mikro-orm.io/api/core.md#SchemaColumns)\<Entity>

### [**](#getprimaryprop)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L941)getPrimaryProp

* ****getPrimaryProp**(): [EntityProperty](https://mikro-orm.io/api/core/interface/EntityProperty.md)\<Entity, any>

* #### Returns [EntityProperty](https://mikro-orm.io/api/core/interface/EntityProperty.md)\<Entity, any>

### [**](#getprimaryprops)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L925)getPrimaryProps

* ****getPrimaryProps**(flatten): [EntityProperty](https://mikro-orm.io/api/core/interface/EntityProperty.md)\<Entity, any>\[]

* #### Parameters

  * ##### flatten: boolean = <!-- -->false

  #### Returns [EntityProperty](https://mikro-orm.io/api/core/interface/EntityProperty.md)\<Entity, any>\[]

### [**](#removeproperty)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L916)removeProperty

* ****removeProperty**(name, sync): void

* #### Parameters

  * ##### name: string

  * ##### sync: boolean = <!-- -->true

  #### Returns void

### [**](#sync)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1024)sync

* ****sync**(initIndexes, config): void

* #### Parameters

  * ##### initIndexes: boolean = <!-- -->false

  * ##### optionalconfig: [Configuration](https://mikro-orm.io/api/core/class/Configuration.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>, [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>>>

  #### Returns void
