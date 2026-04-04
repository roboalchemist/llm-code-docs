# Source: https://mikro-orm.io/api/core/class/ChangeSet.md

# ChangeSet<!-- --> \<T>

## Index[**](#Index)

### Constructors

* [**constructor](#constructor)

### Properties

* [**collection](#collection)
* [**entity](#entity)
* [**meta](#meta)
* [**name](#name)
* [**originalEntity](#originalEntity)
* [**payload](#payload)
* [**persisted](#persisted)
* [**rootName](#rootName)
* [**schema](#schema)
* [**type](#type)

### Methods

* [**getPrimaryKey](#getPrimaryKey)
* [**getSerializedPrimaryKey](#getSerializedPrimaryKey)

## Constructors<!-- -->[**](#Constructors)

### [**](#constructor)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/unit-of-work/ChangeSet.ts#L11)constructor

* ****new ChangeSet**\<T>(entity, type, payload, meta): [ChangeSet](https://mikro-orm.io/api/core/class/ChangeSet.md)\<T>

- #### Parameters

  * ##### entity: T
  * ##### type: [ChangeSetType](https://mikro-orm.io/api/core/enum/ChangeSetType.md)
  * ##### payload: [EntityDictionary](https://mikro-orm.io/api/core.md#EntityDictionary)\<T>
  * ##### meta: [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<T>

  #### Returns [ChangeSet](https://mikro-orm.io/api/core/class/ChangeSet.md)\<T>

## Properties<!-- -->[**](#Properties)

### [**](#collection)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/unit-of-work/ChangeSet.ts#L70)collection

**collection: string

### [**](#entity)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/unit-of-work/ChangeSet.ts#L11)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/unit-of-work/ChangeSet.ts#L73)publicentity

**entity: T

### [**](#meta)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/unit-of-work/ChangeSet.ts#L14)publicmeta

**meta: [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<T>

### [**](#name)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/unit-of-work/ChangeSet.ts#L68)name

**name: string

### [**](#originalEntity)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/unit-of-work/ChangeSet.ts#L76)optionaloriginalEntity

**originalEntity?

<!-- -->

: [EntityData](https://mikro-orm.io/api/core.md#EntityData)\<T>

### [**](#payload)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/unit-of-work/ChangeSet.ts#L13)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/unit-of-work/ChangeSet.ts#L74)publicpayload

**payload: [EntityDictionary](https://mikro-orm.io/api/core.md#EntityDictionary)\<T>

### [**](#persisted)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/unit-of-work/ChangeSet.ts#L75)persisted

**persisted: boolean

### [**](#rootName)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/unit-of-work/ChangeSet.ts#L69)rootName

**rootName: string

### [**](#schema)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/unit-of-work/ChangeSet.ts#L71)optionalschema

**schema?

<!-- -->

: string

### [**](#type)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/unit-of-work/ChangeSet.ts#L12)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/unit-of-work/ChangeSet.ts#L72)publictype

**type: [ChangeSetType](https://mikro-orm.io/api/core/enum/ChangeSetType.md)

## Methods<!-- -->[**](#Methods)

### [**](#getPrimaryKey)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/unit-of-work/ChangeSet.ts#L21)getPrimaryKey

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

- #### Parameters

  * ##### object: boolean = <!-- -->false

  #### Returns null | (T extends { \[PrimaryKeyProp]?<!-- -->: PK } ? PK extends undefined ? Omit\<T\<T>, typeof [PrimaryKeyProp](https://mikro-orm.io/api/core.md#PrimaryKeyProp)> : PK extends keyof<!-- --> T\<T> ? ReadonlyPrimary\<UnwrapPrimary\<T\<T>\[PK\<PK>]>> : PK extends keyof<!-- --> T\<T>\[] ? ReadonlyPrimary\<PrimaryPropToType\<T\<T>, PK\<PK>>> : PK : T extends { \_id?<!-- -->: PK } ? string | ReadonlyPrimary\<PK> : T extends { id?<!-- -->: PK } ? ReadonlyPrimary\<PK> : T extends { uuid?<!-- -->: PK } ? ReadonlyPrimary\<PK> : T)

### [**](#getSerializedPrimaryKey)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/unit-of-work/ChangeSet.ts#L48)getSerializedPrimaryKey

* ****getSerializedPrimaryKey**(): null | string

- #### Returns null | string
