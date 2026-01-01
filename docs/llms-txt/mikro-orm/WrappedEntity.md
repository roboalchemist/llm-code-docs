# Source: https://mikro-orm.io/api/core/class/WrappedEntity.md

# WrappedEntity<!-- --> \<Entity>

## Index[**](#Index)

### Constructors

* [**constructor](#constructor)

### Properties

* [**\_\_data](#__data)
* [**\_\_em](#__em)
* [**\_\_identifier](#__identifier)
* [**\_\_initialized](#__initialized)
* [**\_\_loadedProperties](#__loadedProperties)
* [**\_\_managed](#__managed)
* [**\_\_onLoadFired](#__onLoadFired)
* [**\_\_originalEntityData](#__originalEntityData)
* [**\_\_pk](#__pk)
* [**\_\_populated](#__populated)
* [**\_\_processing](#__processing)
* [**\_\_reference](#__reference)
* [**\_\_schema](#__schema)
* [**\_\_serializationContext](#__serializationContext)
* [**\_\_touched](#__touched)

### Accessors

* [**\_\_config](#__config)
* [**\_\_meta](#__meta)
* [**\_\_platform](#__platform)
* [**\_\_primaryKeys](#__primaryKeys)

### Methods

* [**assign](#assign)
* [**getPrimaryKey](#getPrimaryKey)
* [**getPrimaryKeys](#getPrimaryKeys)
* [**getSchema](#getSchema)
* [**getSerializedPrimaryKey](#getSerializedPrimaryKey)
* [**hasPrimaryKey](#hasPrimaryKey)
* [**init](#init)
* [**isInitialized](#isInitialized)
* [**isManaged](#isManaged)
* [**isTouched](#isTouched)
* [**populate](#populate)
* [**populated](#populated)
* [**serialize](#serialize)
* [**setPrimaryKey](#setPrimaryKey)
* [**setSchema](#setSchema)
* [**setSerializationContext](#setSerializationContext)
* [**toJSON](#toJSON)
* [**toObject](#toObject)
* [**toPOJO](#toPOJO)
* [**toReference](#toReference)

## Constructors<!-- -->[**](#Constructors)

### [**](#constructor)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/WrappedEntity.ts#L76)constructor

* ****new WrappedEntity**\<Entity>(entity, hydrator, pkGetter, pkSerializer, pkGetterConverted): [WrappedEntity](https://mikro-orm.io/api/core/class/WrappedEntity.md)\<Entity>

- #### Parameters

  * ##### entity: Entity
  * ##### hydrator: IHydrator
  * ##### optionalpkGetter: (e) => Entity extends { \[PrimaryKeyProp]?<!-- -->: PK } ? PK extends undefined ? Omit\<Entity\<Entity>, typeof [PrimaryKeyProp](https://mikro-orm.io/api/core.md#PrimaryKeyProp)> : PK extends keyof<!-- --> Entity\<Entity> ? ReadonlyPrimary\<UnwrapPrimary\<Entity\<Entity>\[PK\<PK>]>> : PK extends keyof<!-- --> Entity\<Entity>\[] ? ReadonlyPrimary\<PrimaryPropToType\<Entity\<Entity>, PK\<PK>>> : PK : Entity extends { \_id?<!-- -->: PK } ? string | ReadonlyPrimary\<PK> : Entity extends { id?<!-- -->: PK } ? ReadonlyPrimary\<PK> : Entity extends { uuid?<!-- -->: PK } ? ReadonlyPrimary\<PK> : Entity
  *
    ##### optionalpkSerializer: (e) => string
  *
    ##### optionalpkGetterConverted: (e) => Entity extends { \[PrimaryKeyProp]?<!-- -->: PK } ? PK extends undefined ? Omit\<Entity\<Entity>, typeof [PrimaryKeyProp](https://mikro-orm.io/api/core.md#PrimaryKeyProp)> : PK extends keyof<!-- --> Entity\<Entity> ? ReadonlyPrimary\<UnwrapPrimary\<Entity\<Entity>\[PK\<PK>]>> : PK extends keyof<!-- --> Entity\<Entity>\[] ? ReadonlyPrimary\<PrimaryPropToType\<Entity\<Entity>, PK\<PK>>> : PK : Entity extends { \_id?<!-- -->: PK } ? string | ReadonlyPrimary\<PK> : Entity extends { id?<!-- -->: PK } ? ReadonlyPrimary\<PK> : Entity extends { uuid?<!-- -->: PK } ? ReadonlyPrimary\<PK> : Entity


  #### Returns [WrappedEntity](https://mikro-orm.io/api/core/class/WrappedEntity.md)\<Entity>

## Properties<!-- -->[**](#Properties)

### [**](#__data)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/WrappedEntity.ts#L49)\_\_data

**\_\_data: [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)

### [**](#__em)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/WrappedEntity.ts#L47)optional\_\_em

**\_\_em?

<!-- -->

: [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>>

### [**](#__identifier)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/WrappedEntity.ts#L68)optional\_\_identifier

**\_\_identifier?

<!-- -->

: EntityIdentifier

holds wrapped primary key, so we can compute change set without eager commit

### [**](#__initialized)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/WrappedEntity.ts#L41)\_\_initialized

**\_\_initialized: boolean

### [**](#__loadedProperties)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/WrappedEntity.ts#L48)\_\_loadedProperties

**\_\_loadedProperties: Set\<string>

### [**](#__managed)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/WrappedEntity.ts#L44)optional\_\_managed

**\_\_managed?

<!-- -->

: boolean

### [**](#__onLoadFired)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/WrappedEntity.ts#L45)optional\_\_onLoadFired

**\_\_onLoadFired?

<!-- -->

: boolean

### [**](#__originalEntityData)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/WrappedEntity.ts#L65)optional\_\_originalEntityData

**\_\_originalEntityData?

<!-- -->

: [EntityData](https://mikro-orm.io/api/core.md#EntityData)\<Entity>

holds last entity data snapshot, so we can compute changes when persisting managed entities

### [**](#__pk)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/WrappedEntity.ts#L59)optional\_\_pk

**\_\_pk?

<!-- -->

: Entity extends { \[PrimaryKeyProp]?

<!-- -->

: PK } ? PK extends undefined ? Omit\<Entity\<Entity>, typeof [PrimaryKeyProp](https://mikro-orm.io/api/core.md#PrimaryKeyProp)> : PK extends keyof

<!-- -->

Entity\<Entity> ? ReadonlyPrimary\<UnwrapPrimary\<Entity\<Entity>\[PK\<PK>]>> : PK extends keyof

<!-- -->

Entity\<Entity>\[] ? ReadonlyPrimary\<PrimaryPropToType\<Entity\<Entity>, PK\<PK>>> : PK : Entity extends { \_id?

<!-- -->

: PK } ? string | ReadonlyPrimary\<PK> : Entity extends { id?

<!-- -->

: PK } ? ReadonlyPrimary\<PK> : Entity extends { uuid?

<!-- -->

: PK } ? ReadonlyPrimary\<PK> : Entity

stores last known primary key, as its current state might be broken due to propagation/orphan removal, but we need to know the PK to be able t remove the entity

### [**](#__populated)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/WrappedEntity.ts#L43)optional\_\_populated

**\_\_populated?

<!-- -->

: boolean

### [**](#__processing)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/WrappedEntity.ts#L50)\_\_processing

**\_\_processing: boolean

### [**](#__reference)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/WrappedEntity.ts#L62)optional\_\_reference

**\_\_reference?

<!-- -->

: [Reference](https://mikro-orm.io/api/core/class/Reference.md)\<Entity>

holds the reference wrapper instance (if created), so we can maintain the identity on reference wrappers too

### [**](#__schema)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/WrappedEntity.ts#L46)optional\_\_schema

**\_\_schema?

<!-- -->

: string

### [**](#__serializationContext)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/WrappedEntity.ts#L51)\_\_serializationContext

**\_\_serializationContext: { exclude?

<!-- -->

: readonly

<!-- -->

string\[]; fields?

<!-- -->

: Set\<string>; populate?

<!-- -->

: [PopulateOptions](https://mikro-orm.io/api/core.md#PopulateOptions)\<Entity>\[]; root?

<!-- -->

: [SerializationContext](https://mikro-orm.io/api/core/class/SerializationContext.md)\<Entity> }

#### Type declaration

* ##### optionalexclude?<!-- -->: readonly<!-- --> string\[]
* ##### optionalfields?<!-- -->: Set\<string>
* ##### optionalpopulate?<!-- -->: [PopulateOptions](https://mikro-orm.io/api/core.md#PopulateOptions)\<Entity>\[]
* ##### optionalroot?<!-- -->: [SerializationContext](https://mikro-orm.io/api/core/class/SerializationContext.md)\<Entity>

### [**](#__touched)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/WrappedEntity.ts#L42)\_\_touched

**\_\_touched: boolean

## Accessors<!-- -->[**](#Accessors)

### [**](#__config)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/WrappedEntity.ts#L270)\_\_config

* **get \_\_config(): [Configuration](https://mikro-orm.io/api/core/class/Configuration.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>, [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>>>

- #### Returns [Configuration](https://mikro-orm.io/api/core/class/Configuration.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>, [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>>>

### [**](#__meta)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/WrappedEntity.ts#L262)\_\_meta

* **get \_\_meta(): [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<Entity>

- #### Returns [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<Entity>

### [**](#__platform)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/WrappedEntity.ts#L266)\_\_platform

* **get \_\_platform(): [Platform](https://mikro-orm.io/api/core/class/Platform.md)

- #### Returns [Platform](https://mikro-orm.io/api/core/class/Platform.md)

### [**](#__primaryKeys)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/WrappedEntity.ts#L274)\_\_primaryKeys

* **get \_\_primaryKeys(): (Entity extends { \[PrimaryKeyProp]?
  <!-- -->
  : PK } ? PK extends undefined ? Omit\<Entity\<Entity>, typeof [PrimaryKeyProp](https://mikro-orm.io/api/core.md#PrimaryKeyProp)> : PK extends keyof
  <!-- -->
  Entity\<Entity> ? ReadonlyPrimary\<UnwrapPrimary\<Entity\<Entity>\[PK\<PK>]>> : PK extends keyof
  <!-- -->
  Entity\<Entity>\[] ? ReadonlyPrimary\<PrimaryPropToType\<Entity\<Entity>, PK\<PK>>> : PK : Entity extends { \_id?
  <!-- -->
  : PK } ? string | ReadonlyPrimary\<PK> : Entity extends { id?
  <!-- -->
  : PK } ? ReadonlyPrimary\<PK> : Entity extends { uuid?
  <!-- -->
  : PK } ? ReadonlyPrimary\<PK> : Entity)\[]

- #### Returns (Entity extends { \[PrimaryKeyProp]?<!-- -->: PK } ? PK extends undefined ? Omit\<Entity\<Entity>, typeof [PrimaryKeyProp](https://mikro-orm.io/api/core.md#PrimaryKeyProp)> : PK extends keyof<!-- --> Entity\<Entity> ? ReadonlyPrimary\<UnwrapPrimary\<Entity\<Entity>\[PK\<PK>]>> : PK extends keyof<!-- --> Entity\<Entity>\[] ? ReadonlyPrimary\<PrimaryPropToType\<Entity\<Entity>, PK\<PK>>> : PK : Entity extends { \_id?<!-- -->: PK } ? string | ReadonlyPrimary\<PK> : Entity extends { id?<!-- -->: PK } ? ReadonlyPrimary\<PK> : Entity extends { uuid?<!-- -->: PK } ? ReadonlyPrimary\<PK> : Entity)\[]

## Methods<!-- -->[**](#Methods)

### [**](#assign)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/WrappedEntity.ts#L154)assign

* ****assign**\<Naked, Convert, Data>(data, options): [MergeSelected](https://mikro-orm.io/api/core.md#MergeSelected)\<Entity, Naked, keyof
  <!-- -->
  Data & string>

- #### Parameters

  * ##### data: Data & [IsSubset](https://mikro-orm.io/api/core.md#IsSubset)<[EntityData](https://mikro-orm.io/api/core.md#EntityData)\<Naked>, Data>
  * ##### optionaloptions: [AssignOptions](https://mikro-orm.io/api/core/interface/AssignOptions.md)\<Convert>

  #### Returns [MergeSelected](https://mikro-orm.io/api/core.md#MergeSelected)\<Entity, Naked, keyof<!-- --> Data & string>

### [**](#getPrimaryKey)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/WrappedEntity.ts#L197)getPrimaryKey

* ****getPrimaryKey**(convertCustomTypes): null | (Entity extends { \[PrimaryKeyProp]?
  <!-- -->
  : PK } ? PK extends undefined ? Omit\<Entity\<Entity>, typeof [PrimaryKeyProp](https://mikro-orm.io/api/core.md#PrimaryKeyProp)> : PK extends keyof
  <!-- -->
  Entity\<Entity> ? ReadonlyPrimary\<UnwrapPrimary\<Entity\<Entity>\[PK\<PK>]>> : PK extends keyof
  <!-- -->
  Entity\<Entity>\[] ? ReadonlyPrimary\<PrimaryPropToType\<Entity\<Entity>, PK\<PK>>> : PK : Entity extends { \_id?
  <!-- -->
  : PK } ? string | ReadonlyPrimary\<PK> : Entity extends { id?
  <!-- -->
  : PK } ? ReadonlyPrimary\<PK> : Entity extends { uuid?
  <!-- -->
  : PK } ? ReadonlyPrimary\<PK> : Entity)

- #### Parameters

  * ##### convertCustomTypes: boolean = <!-- -->false

  #### Returns null | (Entity extends { \[PrimaryKeyProp]?<!-- -->: PK } ? PK extends undefined ? Omit\<Entity\<Entity>, typeof [PrimaryKeyProp](https://mikro-orm.io/api/core.md#PrimaryKeyProp)> : PK extends keyof<!-- --> Entity\<Entity> ? ReadonlyPrimary\<UnwrapPrimary\<Entity\<Entity>\[PK\<PK>]>> : PK extends keyof<!-- --> Entity\<Entity>\[] ? ReadonlyPrimary\<PrimaryPropToType\<Entity\<Entity>, PK\<PK>>> : PK : Entity extends { \_id?<!-- -->: PK } ? string | ReadonlyPrimary\<PK> : Entity extends { id?<!-- -->: PK } ? ReadonlyPrimary\<PK> : Entity extends { uuid?<!-- -->: PK } ? ReadonlyPrimary\<PK> : Entity)

### [**](#getPrimaryKeys)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/WrappedEntity.ts#L220)getPrimaryKeys

* ****getPrimaryKeys**(convertCustomTypes): null | (Entity extends { \[PrimaryKeyProp]?
  <!-- -->
  : PK } ? PK extends undefined ? Omit\<Entity\<Entity>, typeof [PrimaryKeyProp](https://mikro-orm.io/api/core.md#PrimaryKeyProp)> : PK extends keyof
  <!-- -->
  Entity\<Entity> ? ReadonlyPrimary\<UnwrapPrimary\<Entity\<Entity>\[PK\<PK>]>> : PK extends keyof
  <!-- -->
  Entity\<Entity>\[] ? ReadonlyPrimary\<PrimaryPropToType\<Entity\<Entity>, PK\<PK>>> : PK : Entity extends { \_id?
  <!-- -->
  : PK } ? string | ReadonlyPrimary\<PK> : Entity extends { id?
  <!-- -->
  : PK } ? ReadonlyPrimary\<PK> : Entity extends { uuid?
  <!-- -->
  : PK } ? ReadonlyPrimary\<PK> : Entity)\[]

- #### Parameters

  * ##### convertCustomTypes: boolean = <!-- -->false

  #### Returns null | (Entity extends { \[PrimaryKeyProp]?<!-- -->: PK } ? PK extends undefined ? Omit\<Entity\<Entity>, typeof [PrimaryKeyProp](https://mikro-orm.io/api/core.md#PrimaryKeyProp)> : PK extends keyof<!-- --> Entity\<Entity> ? ReadonlyPrimary\<UnwrapPrimary\<Entity\<Entity>\[PK\<PK>]>> : PK extends keyof<!-- --> Entity\<Entity>\[] ? ReadonlyPrimary\<PrimaryPropToType\<Entity\<Entity>, PK\<PK>>> : PK : Entity extends { \_id?<!-- -->: PK } ? string | ReadonlyPrimary\<PK> : Entity extends { id?<!-- -->: PK } ? ReadonlyPrimary\<PK> : Entity extends { uuid?<!-- -->: PK } ? ReadonlyPrimary\<PK> : Entity)\[]

### [**](#getSchema)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/WrappedEntity.ts#L245)getSchema

* ****getSchema**(): undefined | string

- #### Returns undefined | string

### [**](#getSerializedPrimaryKey)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/WrappedEntity.ts#L258)getSerializedPrimaryKey

* ****getSerializedPrimaryKey**(): string

- #### Returns string

### [**](#hasPrimaryKey)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/WrappedEntity.ts#L192)hasPrimaryKey

* ****hasPrimaryKey**(): boolean

- #### Returns boolean

### [**](#init)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/WrappedEntity.ts#L166)init

* ****init**\<Hint, Fields, Excludes>(options): Promise\<null | [Loaded](https://mikro-orm.io/api/core.md#Loaded)\<Entity, Hint, Fields, Excludes>>

- #### Parameters

  * ##### optionaloptions: [FindOneOptions](https://mikro-orm.io/api/core/interface/FindOneOptions.md)\<Entity, Hint, Fields, Excludes>

  #### Returns Promise\<null | [Loaded](https://mikro-orm.io/api/core.md#Loaded)\<Entity, Hint, Fields, Excludes>>

### [**](#isInitialized)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/WrappedEntity.ts#L96)isInitialized

* ****isInitialized**(): boolean

- #### Returns boolean

### [**](#isManaged)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/WrappedEntity.ts#L104)isManaged

* ****isManaged**(): boolean

- #### Returns boolean

### [**](#isTouched)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/WrappedEntity.ts#L100)isTouched

* ****isTouched**(): boolean

- #### Returns boolean

### [**](#populate)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/WrappedEntity.ts#L178)populate

* ****populate**\<Hint>(populate, options): Promise<[Loaded](https://mikro-orm.io/api/core.md#Loaded)\<Entity, Hint>>

- #### Parameters

  * ##### populate: false | [AutoPath](https://mikro-orm.io/api/core.md#AutoPath)\<Entity, Hint, ALL>\[]
  * ##### options: [EntityLoaderOptions](https://mikro-orm.io/api/core.md#EntityLoaderOptions)\<Entity> = <!-- -->{}

  #### Returns Promise<[Loaded](https://mikro-orm.io/api/core.md#Loaded)\<Entity, Hint>>

### [**](#populated)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/WrappedEntity.ts#L108)populated

* ****populated**(populated): void

- #### Parameters

  * ##### populated: undefined | boolean = <!-- -->true

  #### Returns void

### [**](#serialize)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/WrappedEntity.ts#L141)serialize

* ****serialize**\<Hint, Exclude>(options): [EntityDTO](https://mikro-orm.io/api/core.md#EntityDTO)<[Loaded](https://mikro-orm.io/api/core.md#Loaded)\<Entity, Hint>>

- #### Parameters

  * ##### optionaloptions: [SerializeOptions](https://mikro-orm.io/api/core/interface/SerializeOptions.md)\<Entity, Hint, Exclude>

  #### Returns [EntityDTO](https://mikro-orm.io/api/core.md#EntityDTO)<[Loaded](https://mikro-orm.io/api/core.md#Loaded)\<Entity, Hint>>

### [**](#setPrimaryKey)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/WrappedEntity.ts#L253)setPrimaryKey

* ****setPrimaryKey**(id): void

- #### Parameters

  * ##### id: null | (Entity extends { \[PrimaryKeyProp]?<!-- -->: PK } ? PK extends undefined ? Omit\<Entity\<Entity>, typeof [PrimaryKeyProp](https://mikro-orm.io/api/core.md#PrimaryKeyProp)> : PK extends keyof<!-- --> Entity\<Entity> ? ReadonlyPrimary\<UnwrapPrimary\<Entity\<Entity>\[PK\<PK>]>> : PK extends keyof<!-- --> Entity\<Entity>\[] ? ReadonlyPrimary\<PrimaryPropToType\<Entity\<Entity>, PK\<PK>>> : PK : Entity extends { \_id?<!-- -->: PK } ? string | ReadonlyPrimary\<PK> : Entity extends { id?<!-- -->: PK } ? ReadonlyPrimary\<PK> : Entity extends { uuid?<!-- -->: PK } ? ReadonlyPrimary\<PK> : Entity)

  #### Returns void

### [**](#setSchema)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/WrappedEntity.ts#L249)setSchema

* ****setSchema**(schema): void

- #### Parameters

  * ##### optionalschema: string

  #### Returns void

### [**](#setSerializationContext)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/WrappedEntity.ts#L112)setSerializationContext

* ****setSerializationContext**\<Hint, Fields, Exclude>(options): void

- #### Parameters

  * ##### options: [LoadHint](https://mikro-orm.io/api/core/interface/LoadHint.md)\<Entity, Hint, Fields, Exclude>

  #### Returns void

### [**](#toJSON)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/WrappedEntity.ts#L149)toJSON

* ****toJSON**(...args): [EntityDictionary](https://mikro-orm.io/api/core.md#EntityDictionary)\<Entity>

- #### Parameters

  * ##### rest...args: any\[]

  #### Returns [EntityDictionary](https://mikro-orm.io/api/core.md#EntityDictionary)\<Entity>

### [**](#toObject)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/WrappedEntity.ts#L137)toObject

* ****toObject**\<Ignored>(ignoreFields): Omit<[EntityDTO](https://mikro-orm.io/api/core.md#EntityDTO)\<Entity>, Ignored>

- #### Parameters

  * ##### optionalignoreFields: Ignored\[]

  #### Returns Omit<[EntityDTO](https://mikro-orm.io/api/core.md#EntityDTO)\<Entity>, Ignored>

### [**](#toPOJO)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/WrappedEntity.ts#L145)toPOJO

* ****toPOJO**(): [EntityDTO](https://mikro-orm.io/api/core.md#EntityDTO)\<Entity>

- #### Returns [EntityDTO](https://mikro-orm.io/api/core.md#EntityDTO)\<Entity>

### [**](#toReference)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/WrappedEntity.ts#L132)toReference

* ****toReference**(): [Ref](https://mikro-orm.io/api/core.md#Ref)\<Entity> & [LoadedReference](https://mikro-orm.io/api/core/interface/LoadedReference.md)<[Loaded](https://mikro-orm.io/api/core.md#Loaded)\<Entity, AddEager\<Entity>>>

- #### Returns [Ref](https://mikro-orm.io/api/core.md#Ref)\<Entity> & [LoadedReference](https://mikro-orm.io/api/core/interface/LoadedReference.md)<[Loaded](https://mikro-orm.io/api/core.md#Loaded)\<Entity, AddEager\<Entity>>>
