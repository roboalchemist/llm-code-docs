# Source: https://mikro-orm.io/api/core/class/EntityFactory.md

# EntityFactory<!-- -->

## Index[**](#index)

### Constructors

* [**constructor](#constructor)

### Methods

* [**create](#create)
* [**createEmbeddable](#createembeddable)
* [**createReference](#createreference)
* [**getComparator](#getcomparator)
* [**mergeData](#mergedata)

## Constructors<!-- -->[**](#constructors)

### [**](#constructor)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/EntityFactory.ts#L61)constructor

* ****new EntityFactory**(em): [EntityFactory](https://mikro-orm.io/api/core/class/EntityFactory.md)

* #### Parameters

  * ##### em: [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>>

  #### Returns [EntityFactory](https://mikro-orm.io/api/core/class/EntityFactory.md)

## Methods<!-- -->[**](#methods)

### [**](#create)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/EntityFactory.ts#L72)create

* ****create**\<T, P>(entityName, data, options): [New](https://mikro-orm.io/api/core.md#New)\<T, P>

* #### Parameters

  * ##### entityName: [EntityName](https://mikro-orm.io/api/core.md#EntityName)\<T>

  * ##### data: [EntityData](https://mikro-orm.io/api/core.md#EntityData)\<T>

  * ##### options: [FactoryOptions](https://mikro-orm.io/api/core/interface/FactoryOptions.md) = <!-- -->{}

  #### Returns [New](https://mikro-orm.io/api/core.md#New)\<T, P>

### [**](#createembeddable)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/EntityFactory.ts#L343)createEmbeddable

* ****createEmbeddable**\<T>(entityName, data, options): T

* #### Parameters

  * ##### entityName: [EntityName](https://mikro-orm.io/api/core.md#EntityName)\<T>

  * ##### data: [EntityData](https://mikro-orm.io/api/core.md#EntityData)\<T>

  * ##### options: Pick<[FactoryOptions](https://mikro-orm.io/api/core/interface/FactoryOptions.md), convertCustomTypes | newEntity> = <!-- -->{}

  #### Returns T

### [**](#createreference)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/EntityFactory.ts#L288)createReference

* ****createReference**\<T>(entityName, id, options): T

* #### Parameters

  * ##### entityName: [EntityName](https://mikro-orm.io/api/core.md#EntityName)\<T>

  * ##### id: (T extends { \[PrimaryKeyProp]?<!-- -->: PK } ? PK extends undefined ? Omit\<T\<T>, typeof [PrimaryKeyProp](https://mikro-orm.io/api/core.md#PrimaryKeyProp)> : PK extends keyof<!-- --> T\<T> ? ReadonlyPrimary\<UnwrapPrimary\<T\<T>\[PK\<PK>]>> : PK extends keyof<!-- --> T\<T>\[] ? ReadonlyPrimary\<PrimaryPropToType\<T\<T>, PK\<PK>>> : PK : T extends { \_id?<!-- -->: PK } ? string | ReadonlyPrimary\<PK> : T extends { id?<!-- -->: PK } ? ReadonlyPrimary\<PK> : T extends { uuid?<!-- -->: PK } ? ReadonlyPrimary\<PK> : T) | (T extends { \[PrimaryKeyProp]?<!-- -->: PK } ? PK extends undefined ? Omit\<T\<T>, typeof [PrimaryKeyProp](https://mikro-orm.io/api/core.md#PrimaryKeyProp)> : PK extends keyof<!-- --> T\<T> ? ReadonlyPrimary\<UnwrapPrimary\<T\<T>\[PK\<PK>]>> : PK extends keyof<!-- --> T\<T>\[] ? ReadonlyPrimary\<PrimaryPropToType\<T\<T>, PK\<PK>>> : PK : T extends { \_id?<!-- -->: PK } ? string | ReadonlyPrimary\<PK> : T extends { id?<!-- -->: PK } ? ReadonlyPrimary\<PK> : T extends { uuid?<!-- -->: PK } ? ReadonlyPrimary\<PK> : T)\[] | Record\<string, T extends { \[PrimaryKeyProp]?<!-- -->: PK } ? PK extends undefined ? Omit\<T\<T>, typeof [PrimaryKeyProp](https://mikro-orm.io/api/core.md#PrimaryKeyProp)> : PK extends keyof<!-- --> T\<T> ? ReadonlyPrimary\<UnwrapPrimary\<T\<T>\[PK\<PK>]>> : PK extends keyof<!-- --> T\<T>\[] ? ReadonlyPrimary\<PrimaryPropToType\<T\<T>, PK\<PK>>> : PK : T extends { \_id?<!-- -->: PK } ? string | ReadonlyPrimary\<PK> : T extends { id?<!-- -->: PK } ? ReadonlyPrimary\<PK> : T extends { uuid?<!-- -->: PK } ? ReadonlyPrimary\<PK> : T>

  * ##### options: Pick<[FactoryOptions](https://mikro-orm.io/api/core/interface/FactoryOptions.md), schema | key | convertCustomTypes | merge> = <!-- -->{}

  #### Returns T

### [**](#getcomparator)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/EntityFactory.ts#L355)getComparator

* ****getComparator**(): [EntityComparator](https://mikro-orm.io/api/core/class/EntityComparator.md)

* #### Returns [EntityComparator](https://mikro-orm.io/api/core/class/EntityComparator.md)

### [**](#mergedata)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/EntityFactory.ts#L181)mergeData

* ****mergeData**\<T>(meta, entity, data, options): void

* #### Parameters

  * ##### meta: [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<T, [EntityCtor](https://mikro-orm.io/api/core.md#EntityCtor)\<T>>

  * ##### entity: T

  * ##### data: [EntityData](https://mikro-orm.io/api/core.md#EntityData)\<T>

  * ##### options: [FactoryOptions](https://mikro-orm.io/api/core/interface/FactoryOptions.md) = <!-- -->{}

  #### Returns void
