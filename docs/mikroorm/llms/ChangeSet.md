# Source: https://mikro-orm.io/api/core/class/ChangeSet.md

# ChangeSet<!-- --> \<T>

## Index[**](#index)

### Constructors

* [**constructor](#constructor)

### Properties

* [**entity](#entity)
* [**meta](#meta)
* [**originalEntity](#originalEntity)
* [**payload](#payload)
* [**persisted](#persisted)
* [**rootMeta](#rootmeta)
* [**schema](#schema)
* [**tptChangeSets](#tptChangeSets)
* [**type](#type)

### Methods

* [**getPrimaryKey](#getprimarykey)
* [**getSerializedPrimaryKey](#getserializedprimarykey)

## Constructors<!-- -->[**](#constructors)

### [**](#constructor)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/unit-of-work/ChangeSet.ts#L10)constructor

* ****new ChangeSet**\<T>(entity, type, payload, meta): [ChangeSet](https://mikro-orm.io/api/core/class/ChangeSet.md)\<T>

* #### Parameters

  * ##### entity: T

  * ##### type: [ChangeSetType](https://mikro-orm.io/api/core/enum/ChangeSetType.md)

  * ##### payload: [EntityDictionary](https://mikro-orm.io/api/core.md#EntityDictionary)\<T>

  * ##### meta: [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<T, [EntityCtor](https://mikro-orm.io/api/core.md#EntityCtor)\<T>>

  #### Returns [ChangeSet](https://mikro-orm.io/api/core/class/ChangeSet.md)\<T>

## Properties<!-- -->[**](#properties)

### [**](#entity)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/unit-of-work/ChangeSet.ts#L11)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/unit-of-work/ChangeSet.ts#L71)publicentity

**entity: T

### [**](#meta)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/unit-of-work/ChangeSet.ts#L14)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/unit-of-work/ChangeSet.ts#L67)publicmeta

**meta: [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<T, [EntityCtor](https://mikro-orm.io/api/core.md#EntityCtor)\<T>>

### [**](#originalEntity)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/unit-of-work/ChangeSet.ts#L74)optionaloriginalEntity

**originalEntity?

<!-- -->

: [EntityData](https://mikro-orm.io/api/core.md#EntityData)\<T>

### [**](#payload)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/unit-of-work/ChangeSet.ts#L13)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/unit-of-work/ChangeSet.ts#L72)publicpayload

**payload: [EntityDictionary](https://mikro-orm.io/api/core.md#EntityDictionary)\<T>

### [**](#persisted)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/unit-of-work/ChangeSet.ts#L73)persisted

**persisted: boolean

### [**](#rootmeta)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/unit-of-work/ChangeSet.ts#L68)rootMeta

**rootMeta: [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<T, [EntityCtor](https://mikro-orm.io/api/core.md#EntityCtor)\<T>>

### [**](#schema)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/unit-of-work/ChangeSet.ts#L69)optionalschema

**schema?

<!-- -->

: string

### [**](#tptChangeSets)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/unit-of-work/ChangeSet.ts#L76)optionaltptChangeSets

**tptChangeSets?

<!-- -->

: [ChangeSet](https://mikro-orm.io/api/core/class/ChangeSet.md)\<T>\[]

For TPT: changesets for parent tables, ordered from immediate parent to root

### [**](#type)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/unit-of-work/ChangeSet.ts#L12)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/unit-of-work/ChangeSet.ts#L70)publictype

**type: [ChangeSetType](https://mikro-orm.io/api/core/enum/ChangeSetType.md)

## Methods<!-- -->[**](#methods)

### [**](#getprimarykey)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/unit-of-work/ChangeSet.ts#L21)getPrimaryKey

* ****getPrimaryKey**(object): null | (T extends { \[PrimaryKeyProp]?
  <!-- -->
  : PK } ? PK extends undefined ? Omit\<T\<T>, typeof [PrimaryKeyProp](https://mikro-orm.io/api/core.md#PrimaryKeyProp)> : PK extends keyof
  <!-- -->
  T\<T> ? ReadonlyPrimary\<UnwrapPrimary\<T\<T>\[PK\<PK>]>> : PK extends keyof
  <!-- -->
  T\<T>\[] ? ReadonlyPrimary\<PrimaryPropToType\<T\<T>, PK\<PK>>> : PK : T extends { \_id?
  <!-- -->
  : PK } ? string | ReadonlyPrimary\<PK> : T extends { id?
  <!-- -->
  : PK } ? ReadonlyPrimary\<PK> : T extends { uuid?
  <!-- -->
  : PK } ? ReadonlyPrimary\<PK> : T)

* #### Parameters

  * ##### object: boolean = <!-- -->false

  #### Returns null | (T extends { \[PrimaryKeyProp]?<!-- -->: PK } ? PK extends undefined ? Omit\<T\<T>, typeof [PrimaryKeyProp](https://mikro-orm.io/api/core.md#PrimaryKeyProp)> : PK extends keyof<!-- --> T\<T> ? ReadonlyPrimary\<UnwrapPrimary\<T\<T>\[PK\<PK>]>> : PK extends keyof<!-- --> T\<T>\[] ? ReadonlyPrimary\<PrimaryPropToType\<T\<T>, PK\<PK>>> : PK : T extends { \_id?<!-- -->: PK } ? string | ReadonlyPrimary\<PK> : T extends { id?<!-- -->: PK } ? ReadonlyPrimary\<PK> : T extends { uuid?<!-- -->: PK } ? ReadonlyPrimary\<PK> : T)

### [**](#getserializedprimarykey)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/unit-of-work/ChangeSet.ts#L48)getSerializedPrimaryKey

* ****getSerializedPrimaryKey**(): null | string

* #### Returns null | string
