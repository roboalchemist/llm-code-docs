# Source: https://mikro-orm.io/api/core/interface/EntityMetadataWithProperties.md

# EntityMetadataWithProperties<!-- --> \<TName, TTableName, TProperties, TPK, TBase, TRepository, TForceObject>

### Hierarchy

* Omit\<Partial<[EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)<[InferEntityFromProperties](https://mikro-orm.io/api/core.md#InferEntityFromProperties)\<TProperties, TPK, TBase, TRepository>>>, properties | extends | primaryKeys | hooks | discriminatorColumn | versionProperty | concurrencyCheckKeys | serializedPrimaryKey | indexes | uniques | repository | orderBy>
  * *EntityMetadataWithProperties*

## Index[**](#index)

### Properties

* [**abstract](#abstract)
* [**allTPTDescendants](#allTPTDescendants)
* [**bidirectionalRelations](#bidirectionalRelations)
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
* [**forceObject](#forceObject)
* [**getterProps](#getterProps)
* [**hasTriggers](#hasTriggers)
* [**hasUniqueProps](#hasUniqueProps)
* [**hooks](#hooks)
* [**hydrateProps](#hydrateProps)
* [**checks](#checks)
* [**indexes](#indexes)
* [**inheritance](#inheritance)
* [**inheritanceType](#inheritanceType)
* [**materialized](#materialized)
* [**name](#name)
* [**orderBy](#orderBy)
* [**ownProps](#ownProps)
* [**path](#path)
* [**pivotTable](#pivotTable)
* [**polymorphicDiscriminatorMap](#polymorphicDiscriminatorMap)
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
* [**selfReferencing](#selfReferencing)
* [**serializedPrimaryKey](#serializedPrimaryKey)
* [**schema](#schema)
* [**simplePK](#simplePK)
* [**tableName](#tableName)
* [**tptDiscriminatorColumn](#tptDiscriminatorColumn)
* [**tptChildren](#tptChildren)
* [**tptInverseProp](#tptInverseProp)
* [**tptParent](#tptParent)
* [**tptParentProp](#tptParentProp)
* [**trackingProps](#trackingProps)
* [**uniqueName](#uniqueName)
* [**uniqueProps](#uniqueProps)
* [**uniques](#uniques)
* [**validateProps](#validateProps)
* [**versionProperty](#versionProperty)
* [**view](#view)
* [**virtual](#virtual)
* [**withData](#withData)

### Methods

* [**addProperty](#addProperty)
* [**createColumnMappingObject](#createColumnMappingObject)
* [**createSchemaColumnMappingObject](#createSchemaColumnMappingObject)
* [**getPrimaryProp](#getPrimaryProp)
* [**getPrimaryProps](#getPrimaryProps)
* [**removeProperty](#removeProperty)
* [**sync](#sync)

## Properties<!-- -->[**](#properties)

### [**](#abstract)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1285)optionalinheritedabstract

**abstract?

<!-- -->

: boolean

Inherited from Omit.abstract

### [**](#allTPTDescendants)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1303)optionalinheritedallTPTDescendants

**allTPTDescendants?

<!-- -->

: [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<any, [EntityCtor](https://mikro-orm.io/api/core.md#EntityCtor)\<any>>\[]

Inherited from Omit.allTPTDescendants

For TPT: all non-abstract descendants, sorted by depth (deepest first). Precomputed during discovery.

### [**](#bidirectionalRelations)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1247)optionalinheritedbidirectionalRelations

**bidirectionalRelations?

<!-- -->

: [EntityProperty](https://mikro-orm.io/api/core/interface/EntityProperty.md)<[InferEntityFromProperties](https://mikro-orm.io/api/core.md#InferEntityFromProperties)\<TProperties, TPK, TBase, TRepository, false>, any>\[]

Inherited from Omit.bidirectionalRelations

### [**](#class)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1284)optionalinheritedclass

**class?

<!-- -->

: [EntityCtor](https://mikro-orm.io/api/core.md#EntityCtor)<[InferEntityFromProperties](https://mikro-orm.io/api/core.md#InferEntityFromProperties)\<TProperties, TPK, TBase, TRepository, false>>

Inherited from Omit.class

### [**](#className)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1208)optionalinheritedclassName

**className?

<!-- -->

: string

Inherited from Omit.className

### [**](#collection)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1236)optionalinheritedcollection

**collection?

<!-- -->

: string

Inherited from Omit.collection

### [**](#comment)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1287)optionalinheritedcomment

**comment?

<!-- -->

: string

Inherited from Omit.comment

### [**](#comparableProps)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1249)optionalinheritedcomparableProps

**comparableProps?

<!-- -->

: [EntityProperty](https://mikro-orm.io/api/core/interface/EntityProperty.md)<[InferEntityFromProperties](https://mikro-orm.io/api/core.md#InferEntityFromProperties)\<TProperties, TPK, TBase, TRepository, false>, any>\[]

Inherited from Omit.comparableProps

### [**](#compositePK)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1240)optionalinheritedcompositePK

**compositePK?

<!-- -->

: boolean

Inherited from Omit.compositePK

### [**](#concurrencyCheckKeys)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/defineEntity.ts#L1219)optionalconcurrencyCheckKeys

**concurrencyCheckKeys?

<!-- -->

: Set\<AllKeys\<TProperties, TBase>>

### [**](#constructorParams)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1233)optionalinheritedconstructorParams

**constructorParams?

<!-- -->

: (typeof [PrimaryKeyProp](https://mikro-orm.io/api/core.md#PrimaryKeyProp) | keyof

<!-- -->

TProperties | keyof

<!-- -->

IsNever\<TBase, true, false> extends true ? {} : TBase extends { toObject: any } ? Pick<[IWrappedEntity](https://mikro-orm.io/api/core/interface/IWrappedEntity.md)<{ -readonly \[ K in ... | ... | ... ]: InferBuilderValue<...> } & { \[PrimaryKeyProp]?

<!-- -->

: ... | ... } & (IsNever<..., ..., ...> extends true ? {} : { \[EntityRepositoryType]?

<!-- -->

: ... }) & Omit\<TBase<...>, typeof [PrimaryKeyProp](https://mikro-orm.io/api/core.md#PrimaryKeyProp)>>, BaseEntityMethodKeys> : {} | keyof

<!-- -->

IsNever\<TRepository, true, false> extends true ? {} : { \[EntityRepositoryType]?

<!-- -->

: TRepository extends [Constructor](https://mikro-orm.io/api/core.md#Constructor)\<R> ? R : TRepository } | keyof

<!-- -->

IsNever\<TBase, true, false> extends true ? {} : Omit\<TBase, typeof [PrimaryKeyProp](https://mikro-orm.io/api/core.md#PrimaryKeyProp)>)\[]

Inherited from Omit.constructorParams

### [**](#definedProperties)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1293)optionalinheriteddefinedProperties

**definedProperties?

<!-- -->

: [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)\<any>

Inherited from Omit.definedProperties

### [**](#discriminatorColumn)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/defineEntity.ts#L1217)optionaldiscriminatorColumn

**discriminatorColumn?

<!-- -->

: string

### [**](#discriminatorMap)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1231)optionalinheriteddiscriminatorMap

**discriminatorMap?

<!-- -->

: [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)<[EntityClass](https://mikro-orm.io/api/core.md#EntityClass)\<any>>

Inherited from Omit.discriminatorMap

### [**](#discriminatorValue)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1230)optionalinheriteddiscriminatorValue

**discriminatorValue?

<!-- -->

: string | number

Inherited from Omit.discriminatorValue

### [**](#embeddable)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1232)optionalinheritedembeddable

**embeddable?

<!-- -->

: boolean

Inherited from Omit.embeddable

### [**](#expression)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1221)optionalinheritedexpression

**expression?

<!-- -->

: string | (em, where, options, stream) => [MaybePromise](https://mikro-orm.io/api/core.md#MaybePromise)\<string | object | [RawQueryFragment](https://mikro-orm.io/api/core/class/RawQueryFragment.md)\<string>>

Inherited from Omit.expression

### [**](#extends)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/defineEntity.ts#L1202)optionalextends

**extends?

<!-- -->

: { \~entity: TBase } | [EntityCtor](https://mikro-orm.io/api/core.md#EntityCtor)\<TBase>

### [**](#filters)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1286)optionalinheritedfilters

**filters?

<!-- -->

: [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)<[FilterDef](https://mikro-orm.io/api/core.md#FilterDef)\<any>>

Inherited from Omit.filters

### [**](#forceConstructor)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1234)optionalinheritedforceConstructor

**forceConstructor?

<!-- -->

: boolean

Inherited from Omit.forceConstructor

### [**](#forceObject)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/defineEntity.ts#L1208)optionalforceObject

**forceObject?

<!-- -->

: TForceObject

### [**](#getterProps)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1254)optionalinheritedgetterProps

**getterProps?

<!-- -->

: [EntityProperty](https://mikro-orm.io/api/core/interface/EntityProperty.md)<[InferEntityFromProperties](https://mikro-orm.io/api/core.md#InferEntityFromProperties)\<TProperties, TPK, TBase, TRepository, false>, any>\[]

Inherited from Omit.getterProps

### [**](#hasTriggers)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1313)optionalinheritedhasTriggers

**hasTriggers?

<!-- -->

: boolean

Inherited from Omit.hasTriggers

### [**](#hasUniqueProps)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1289)optionalinheritedhasUniqueProps

**hasUniqueProps?

<!-- -->

: boolean

Inherited from Omit.hasUniqueProps

### [**](#hooks)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/defineEntity.ts#L1205)optionalhooks

**hooks?

<!-- -->

: [DefineEntityHooks](https://mikro-orm.io/api/core/interface/DefineEntityHooks.md)\<any>

### [**](#hydrateProps)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1251)optionalinheritedhydrateProps

**hydrateProps?

<!-- -->

: [EntityProperty](https://mikro-orm.io/api/core/interface/EntityProperty.md)<[InferEntityFromProperties](https://mikro-orm.io/api/core.md#InferEntityFromProperties)\<TProperties, TPK, TBase, TRepository, false>, any>\[]

Inherited from Omit.hydrateProps

### [**](#checks)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1279)optionalinheritedchecks

**checks?

<!-- -->

: [CheckConstraint](https://mikro-orm.io/api/core/interface/CheckConstraint.md)<[InferEntityFromProperties](https://mikro-orm.io/api/core.md#InferEntityFromProperties)\<TProperties, TPK, TBase, TRepository, false>>\[]

Inherited from Omit.checks

### [**](#indexes)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/defineEntity.ts#L1221)optionalindexes

**indexes?

<!-- -->

: { expression?

<!-- -->

: string | [IndexCallback](https://mikro-orm.io/api/core.md#IndexCallback)<[InferEntityFromProperties](https://mikro-orm.io/api/core.md#InferEntityFromProperties)\<TProperties, TPK, TBase, never, false>>; name?

<!-- -->

: string; options?

<!-- -->

: [Dictionary](https://mikro-orm.io/api/core.md#Dictionary); properties?

<!-- -->

: keyof

<!-- -->

TProperties | keyof

<!-- -->

TProperties\[]; type?

<!-- -->

: string }\[]

### [**](#inheritance)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/defineEntity.ts#L1211)optionalinheritance

**inheritance?

<!-- -->

: tpt

### [**](#inheritanceType)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1297)optionalinheritedinheritanceType

**inheritanceType?

<!-- -->

: sti | tpt

Inherited from Omit.inheritanceType

Inheritance type: 'sti' (Single Table Inheritance) or 'tpt' (Table-Per-Type). Only set on root entities.

### [**](#materialized)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1216)optionalinheritedmaterialized

**materialized?

<!-- -->

: boolean

Inherited from Omit.materialized

True if this is a materialized view (PostgreSQL only). Requires `view: true`.

### [**](#name)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/defineEntity.ts#L1198)name

**name: TName

Overrides Omit.name

### [**](#orderBy)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/defineEntity.ts#L1214)optionalorderBy

**orderBy?

<!-- -->

: { \[ K in string ]?: [QueryOrderKeysFlat](https://mikro-orm.io/api/core.md#QueryOrderKeysFlat) } | { \[ K in string ]?: [QueryOrderKeysFlat](https://mikro-orm.io/api/core.md#QueryOrderKeysFlat) }\[]

### [**](#ownProps)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1311)optionalinheritedownProps

**ownProps?

<!-- -->

: [EntityProperty](https://mikro-orm.io/api/core/interface/EntityProperty.md)<[InferEntityFromProperties](https://mikro-orm.io/api/core.md#InferEntityFromProperties)\<TProperties, TPK, TBase, TRepository, false>, any>\[]

Inherited from Omit.ownProps

For TPT: properties defined only in THIS entity (not inherited from parent).

### [**](#path)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1237)optionalinheritedpath

**path?

<!-- -->

: string

Inherited from Omit.path

### [**](#pivotTable)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1211)optionalinheritedpivotTable

**pivotTable?

<!-- -->

: boolean

Inherited from Omit.pivotTable

### [**](#polymorphicDiscriminatorMap)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1295)optionalinheritedpolymorphicDiscriminatorMap

**polymorphicDiscriminatorMap?

<!-- -->

: [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)<[EntityClass](https://mikro-orm.io/api/core.md#EntityClass)\<any>>

Inherited from Omit.polymorphicDiscriminatorMap

For polymorphic M:N pivot tables, maps discriminator values to entity classes

### [**](#polymorphs)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1291)optionalinheritedpolymorphs

**polymorphs?

<!-- -->

: [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<any, [EntityCtor](https://mikro-orm.io/api/core.md#EntityCtor)\<any>>\[]

Inherited from Omit.polymorphs

### [**](#primaryKeys)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/defineEntity.ts#L1204)optionalprimaryKeys

**primaryKeys?

<!-- -->

: TPK & [InferPrimaryKey](https://mikro-orm.io/api/core.md#InferPrimaryKey)\<TProperties>\[]

### [**](#properties)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/defineEntity.ts#L1203)properties

**properties: TProperties | (properties) => TProperties

### [**](#propertyOrder)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L887)optionalreadonlyinheritedpropertyOrder

**propertyOrder?

<!-- -->

: Map\<string, number> =

<!-- -->

...

Inherited from Omit.propertyOrder

### [**](#props)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1245)optionalinheritedprops

**props?

<!-- -->

: [EntityProperty](https://mikro-orm.io/api/core/interface/EntityProperty.md)<[InferEntityFromProperties](https://mikro-orm.io/api/core.md#InferEntityFromProperties)\<TProperties, TPK, TBase, TRepository, false>, any>\[]

Inherited from Omit.props

### [**](#prototype)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1283)optionalinheritedprototype

**prototype?

<!-- -->

: [InferEntityFromProperties](https://mikro-orm.io/api/core.md#InferEntityFromProperties)\<TProperties, TPK, TBase, TRepository, false>

Inherited from Omit.prototype

### [**](#readonly)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1290)optionalinheritedreadonly

**readonly?

<!-- -->

: boolean

Inherited from Omit.readonly

### [**](#referencingProperties)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1248)optionalinheritedreferencingProperties

**referencingProperties?

<!-- -->

: { meta: [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)<[InferEntityFromProperties](https://mikro-orm.io/api/core.md#InferEntityFromProperties)\<TProperties, TPK, TBase, TRepository, false>, [EntityCtor](https://mikro-orm.io/api/core.md#EntityCtor)<[InferEntityFromProperties](https://mikro-orm.io/api/core.md#InferEntityFromProperties)\<TProperties, TPK, TBase, TRepository, false>>>; prop: [EntityProperty](https://mikro-orm.io/api/core/interface/EntityProperty.md)<[InferEntityFromProperties](https://mikro-orm.io/api/core.md#InferEntityFromProperties)\<TProperties, TPK, TBase, TRepository, false>, any> }\[]

Inherited from Omit.referencingProperties

### [**](#relations)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1246)optionalinheritedrelations

**relations?

<!-- -->

: [EntityProperty](https://mikro-orm.io/api/core/interface/EntityProperty.md)<[InferEntityFromProperties](https://mikro-orm.io/api/core.md#InferEntityFromProperties)\<TProperties, TPK, TBase, TRepository, false>, any>\[]

Inherited from Omit.relations

### [**](#repository)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/defineEntity.ts#L1207)optionalrepository

**repository?

<!-- -->

: () => TRepository

#### Type declaration

* * **(): TRepository

  * #### Returns TRepository

### [**](#repositoryClass)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1280)optionalinheritedrepositoryClass

**repositoryClass?

<!-- -->

: string

Inherited from Omit.repositoryClass

### [**](#root)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1292)optionalinheritedroot

**root?

<!-- -->

: [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)<[InferEntityFromProperties](https://mikro-orm.io/api/core.md#InferEntityFromProperties)\<TProperties, TPK, TBase, TRepository, false>, [EntityCtor](https://mikro-orm.io/api/core.md#EntityCtor)<[InferEntityFromProperties](https://mikro-orm.io/api/core.md#InferEntityFromProperties)\<TProperties, TPK, TBase, TRepository, false>>>

Inherited from Omit.root

### [**](#selfReferencing)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1288)optionalinheritedselfReferencing

**selfReferencing?

<!-- -->

: boolean

Inherited from Omit.selfReferencing

### [**](#serializedPrimaryKey)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/defineEntity.ts#L1220)optionalserializedPrimaryKey

**serializedPrimaryKey?

<!-- -->

: AllKeys\<TProperties, TBase>

### [**](#schema)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1210)optionalinheritedschema

**schema?

<!-- -->

: string

Inherited from Omit.schema

### [**](#simplePK)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1239)optionalinheritedsimplePK

**simplePK?

<!-- -->

: boolean

Inherited from Omit.simplePK

### [**](#tableName)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/defineEntity.ts#L1199)optionaltableName

**tableName?

<!-- -->

: TTableName

Overrides Omit.tableName

### [**](#tptDiscriminatorColumn)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1309)optionalinheritedtptDiscriminatorColumn

**tptDiscriminatorColumn?

<!-- -->

: string

Inherited from Omit.tptDiscriminatorColumn

For TPT: virtual discriminator property name (computed at query time, not persisted).

### [**](#tptChildren)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1301)optionalinheritedtptChildren

**tptChildren?

<!-- -->

: [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<any, [EntityCtor](https://mikro-orm.io/api/core.md#EntityCtor)\<any>>\[]

Inherited from Omit.tptChildren

For TPT: direct child entities (entities that extend this one).

### [**](#tptInverseProp)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1307)optionalinheritedtptInverseProp

**tptInverseProp?

<!-- -->

: [EntityProperty](https://mikro-orm.io/api/core/interface/EntityProperty.md)\<any, any>

Inherited from Omit.tptInverseProp

For TPT: inverse of tptParentProp, used for joining from parent to child (parent PK → child PK).

### [**](#tptParent)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1299)optionalinheritedtptParent

**tptParent?

<!-- -->

: [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<any, [EntityCtor](https://mikro-orm.io/api/core.md#EntityCtor)\<any>>

Inherited from Omit.tptParent

For TPT: direct parent entity metadata (the entity this one extends).

### [**](#tptParentProp)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1305)optionalinheritedtptParentProp

**tptParentProp?

<!-- -->

: [EntityProperty](https://mikro-orm.io/api/core/interface/EntityProperty.md)\<any, any>

Inherited from Omit.tptParentProp

For TPT: synthetic property representing the join to the parent table (child PK → parent PK).

### [**](#trackingProps)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1250)optionalinheritedtrackingProps

**trackingProps?

<!-- -->

: [EntityProperty](https://mikro-orm.io/api/core/interface/EntityProperty.md)<[InferEntityFromProperties](https://mikro-orm.io/api/core.md#InferEntityFromProperties)\<TProperties, TPK, TBase, TRepository, false>, any>\[]

Inherited from Omit.trackingProps

### [**](#uniqueName)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1020)inheriteduniqueName

**uniqueName: undefined | string

Inherited from Omit.uniqueName

### [**](#uniqueProps)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1253)optionalinheriteduniqueProps

**uniqueProps?

<!-- -->

: [EntityProperty](https://mikro-orm.io/api/core/interface/EntityProperty.md)<[InferEntityFromProperties](https://mikro-orm.io/api/core.md#InferEntityFromProperties)\<TProperties, TPK, TBase, TRepository, false>, any>\[]

Inherited from Omit.uniqueProps

### [**](#uniques)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/defineEntity.ts#L1228)optionaluniques

**uniques?

<!-- -->

: { deferMode?

<!-- -->

: [DeferMode](https://mikro-orm.io/api/core/enum/DeferMode.md) | immediate | deferred; expression?

<!-- -->

: string | [IndexCallback](https://mikro-orm.io/api/core.md#IndexCallback)<[InferEntityFromProperties](https://mikro-orm.io/api/core.md#InferEntityFromProperties)\<TProperties, TPK, TBase, never, false>>; name?

<!-- -->

: string; options?

<!-- -->

: [Dictionary](https://mikro-orm.io/api/core.md#Dictionary); properties?

<!-- -->

: keyof

<!-- -->

TProperties | keyof

<!-- -->

TProperties\[] }\[]

### [**](#validateProps)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1252)optionalinheritedvalidateProps

**validateProps?

<!-- -->

: [EntityProperty](https://mikro-orm.io/api/core/interface/EntityProperty.md)<[InferEntityFromProperties](https://mikro-orm.io/api/core.md#InferEntityFromProperties)\<TProperties, TPK, TBase, TRepository, false>, any>\[]

Inherited from Omit.validateProps

### [**](#versionProperty)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/defineEntity.ts#L1218)optionalversionProperty

**versionProperty?

<!-- -->

: AllKeys\<TProperties, TBase>

### [**](#view)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1214)optionalinheritedview

**view?

<!-- -->

: boolean | { materialized?

<!-- -->

: boolean; withData?

<!-- -->

: boolean }

Inherited from Omit.view

True if this entity represents a database view (not a virtual entity). Accepts `{ materialized: true }` as input, normalized to `true` during sync.

### [**](#virtual)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1212)optionalinheritedvirtual

**virtual?

<!-- -->

: boolean

Inherited from Omit.virtual

### [**](#withData)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1218)optionalinheritedwithData

**withData?

<!-- -->

: boolean

Inherited from Omit.withData

For materialized views, whether data is populated on creation. Defaults to true.

## Methods<!-- -->[**](#methods)

### [**](#addProperty)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L910)optionalinheritedaddProperty

* ****addProperty**(prop): void

* Inherited from Omit.addProperty

  #### Parameters

  * ##### prop: Partial<[EntityProperty](https://mikro-orm.io/api/core/interface/EntityProperty.md)<[InferEntityFromProperties](https://mikro-orm.io/api/core.md#InferEntityFromProperties)\<TProperties, TPK, TBase, TRepository, false>, any>>

  #### Returns void

### [**](#createColumnMappingObject)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L951)optionalinheritedcreateColumnMappingObject

* ****createColumnMappingObject**(alias, toStringAlias): FormulaColumns<[InferEntityFromProperties](https://mikro-orm.io/api/core.md#InferEntityFromProperties)\<TProperties, TPK, TBase, TRepository, false>>

* Inherited from Omit.createColumnMappingObject

  Creates a mapping from property names to field names.

  ***

  #### Parameters

  * ##### optionalalias: string | (prop) => string

    Optional alias to prefix field names. Can be a string (same for all) or a function (per-property). When provided, also adds toString() returning the alias for backwards compatibility with formulas.

  *

  ##### optionaltoStringAlias: string

    Optional alias to return from toString(). Defaults to `alias` when it's a string.

  #### Returns FormulaColumns<[InferEntityFromProperties](https://mikro-orm.io/api/core.md#InferEntityFromProperties)\<TProperties, TPK, TBase, TRepository, false>>

### [**](#createSchemaColumnMappingObject)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L998)optionalinheritedcreateSchemaColumnMappingObject

* ****createSchemaColumnMappingObject**(): [SchemaColumns](https://mikro-orm.io/api/core.md#SchemaColumns)<[InferEntityFromProperties](https://mikro-orm.io/api/core.md#InferEntityFromProperties)\<TProperties, TPK, TBase, TRepository, false>>

* Inherited from Omit.createSchemaColumnMappingObject

  Creates a column mapping for schema callbacks (indexes, checks, generated columns). For TPT entities, only includes properties that belong to the current table (ownProps).

  ***

  #### Returns [SchemaColumns](https://mikro-orm.io/api/core.md#SchemaColumns)<[InferEntityFromProperties](https://mikro-orm.io/api/core.md#InferEntityFromProperties)\<TProperties, TPK, TBase, TRepository, false>>

### [**](#getPrimaryProp)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L941)optionalinheritedgetPrimaryProp

* ****getPrimaryProp**(): [EntityProperty](https://mikro-orm.io/api/core/interface/EntityProperty.md)<[InferEntityFromProperties](https://mikro-orm.io/api/core.md#InferEntityFromProperties)\<TProperties, TPK, TBase, TRepository, false>, any>

* Inherited from Omit.getPrimaryProp

  #### Returns [EntityProperty](https://mikro-orm.io/api/core/interface/EntityProperty.md)<[InferEntityFromProperties](https://mikro-orm.io/api/core.md#InferEntityFromProperties)\<TProperties, TPK, TBase, TRepository, false>, any>

### [**](#getPrimaryProps)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L925)optionalinheritedgetPrimaryProps

* ****getPrimaryProps**(flatten): [EntityProperty](https://mikro-orm.io/api/core/interface/EntityProperty.md)<[InferEntityFromProperties](https://mikro-orm.io/api/core.md#InferEntityFromProperties)\<TProperties, TPK, TBase, TRepository, false>, any>\[]

* Inherited from Omit.getPrimaryProps

  #### Parameters

  * ##### flatten: boolean = <!-- -->false

  #### Returns [EntityProperty](https://mikro-orm.io/api/core/interface/EntityProperty.md)<[InferEntityFromProperties](https://mikro-orm.io/api/core.md#InferEntityFromProperties)\<TProperties, TPK, TBase, TRepository, false>, any>\[]

### [**](#removeProperty)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L916)optionalinheritedremoveProperty

* ****removeProperty**(name, sync): void

* Inherited from Omit.removeProperty

  #### Parameters

  * ##### name: string

  * ##### sync: boolean = <!-- -->true

  #### Returns void

### [**](#sync)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1024)optionalinheritedsync

* ****sync**(initIndexes, config): void

* Inherited from Omit.sync

  #### Parameters

  * ##### initIndexes: boolean = <!-- -->false

  * ##### optionalconfig: [Configuration](https://mikro-orm.io/api/core/class/Configuration.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>, [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>>>

  #### Returns void
