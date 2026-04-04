# Source: https://mikro-orm.io/api/core/class/EntityFactory.md

# EntityFactory<!-- -->

## Index[**](#Index)

### Constructors

* [**constructor](#constructor)

### Methods

* [**create](#create)
* [**createEmbeddable](#createEmbeddable)
* [**createReference](#createReference)
* [**getComparator](#getComparator)
* [**mergeData](#mergeData)

## Constructors<!-- -->[**](#Constructors)

### [**](#constructor)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/EntityFactory.ts#L57)constructor

* ****new EntityFactory**(em): [EntityFactory](https://mikro-orm.io/api/core/class/EntityFactory.md)

- #### Parameters

  * ##### em: [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>>

  #### Returns [EntityFactory](https://mikro-orm.io/api/core/class/EntityFactory.md)

## Methods<!-- -->[**](#Methods)

### [**](#create)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/EntityFactory.ts#L67)create

* ****create**\<T, P>(entityName, data, options): [New](https://mikro-orm.io/api/core.md#New)\<T, P>

- #### Parameters

  * ##### entityName: [EntityName](https://mikro-orm.io/api/core.md#EntityName)\<T>
  * ##### data: [EntityData](https://mikro-orm.io/api/core.md#EntityData)\<T>
  * ##### options: [FactoryOptions](https://mikro-orm.io/api/core/interface/FactoryOptions.md) = <!-- -->{}

  #### Returns [New](https://mikro-orm.io/api/core.md#New)\<T, P>

### [**](#createEmbeddable)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/EntityFactory.ts#L277)createEmbeddable

* ****createEmbeddable**\<T>(entityName, data, options): T

- #### Parameters

  * ##### entityName: [EntityName](https://mikro-orm.io/api/core.md#EntityName)\<T>
  * ##### data: [EntityData](https://mikro-orm.io/api/core.md#EntityData)\<T>
  * ##### options: Pick<[FactoryOptions](https://mikro-orm.io/api/core/interface/FactoryOptions.md), convertCustomTypes | newEntity> = <!-- -->{}

  #### Returns T

### [**](#createReference)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/EntityFactory.ts#L242)createReference

* ****createReference**\<T>(entityName, id, options): T

- #### Parameters

  * ##### entityName: [EntityName](https://mikro-orm.io/api/core.md#EntityName)\<T>
  * ##### id: (T extends { \[PrimaryKeyProp]?<!-- -->: PK } ? PK extends undefined ? Omit\<T\<T>, typeof [PrimaryKeyProp](https://mikro-orm.io/api/core.md#PrimaryKeyProp)> : PK extends keyof<!-- --> T\<T> ? ReadonlyPrimary\<UnwrapPrimary\<T\<T>\[PK\<PK>]>> : PK extends keyof<!-- --> T\<T>\[] ? ReadonlyPrimary\<PrimaryPropToType\<T\<T>, PK\<PK>>> : PK : T extends { \_id?<!-- -->: PK } ? string | ReadonlyPrimary\<PK> : T extends { id?<!-- -->: PK } ? ReadonlyPrimary\<PK> : T extends { uuid?<!-- -->: PK } ? ReadonlyPrimary\<PK> : T) | (T extends { \[PrimaryKeyProp]?<!-- -->: PK } ? PK extends undefined ? Omit\<T\<T>, typeof [PrimaryKeyProp](https://mikro-orm.io/api/core.md#PrimaryKeyProp)> : PK extends keyof<!-- --> T\<T> ? ReadonlyPrimary\<UnwrapPrimary\<T\<T>\[PK\<PK>]>> : PK extends keyof<!-- --> T\<T>\[] ? ReadonlyPrimary\<PrimaryPropToType\<T\<T>, PK\<PK>>> : PK : T extends { \_id?<!-- -->: PK } ? string | ReadonlyPrimary\<PK> : T extends { id?<!-- -->: PK } ? ReadonlyPrimary\<PK> : T extends { uuid?<!-- -->: PK } ? ReadonlyPrimary\<PK> : T)\[] | Record\<string, T extends { \[PrimaryKeyProp]?<!-- -->: PK } ? PK extends undefined ? Omit\<T\<T>, typeof [PrimaryKeyProp](https://mikro-orm.io/api/core.md#PrimaryKeyProp)> : PK extends keyof<!-- --> T\<T> ? ReadonlyPrimary\<UnwrapPrimary\<T\<T>\[PK\<PK>]>> : PK extends keyof<!-- --> T\<T>\[] ? ReadonlyPrimary\<PrimaryPropToType\<T\<T>, PK\<PK>>> : PK : T extends { \_id?<!-- -->: PK } ? string | ReadonlyPrimary\<PK> : T extends { id?<!-- -->: PK } ? ReadonlyPrimary\<PK> : T extends { uuid?<!-- -->: PK } ? ReadonlyPrimary\<PK> : T>
  * ##### options: Pick<[FactoryOptions](https://mikro-orm.io/api/core/interface/FactoryOptions.md), schema | convertCustomTypes | merge> = <!-- -->{}

  #### Returns T

### [**](#getComparator)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/EntityFactory.ts#L286)getComparator

* ****getComparator**(): [EntityComparator](https://mikro-orm.io/api/core/class/EntityComparator.md)

- #### Returns [EntityComparator](https://mikro-orm.io/api/core/class/EntityComparator.md)

### [**](#mergeData)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/EntityFactory.ts#L169)mergeData

* ****mergeData**\<T>(meta, entity, data, options): void

- #### Parameters

  * ##### meta: [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<T>
  * ##### entity: T
  * ##### data: [EntityData](https://mikro-orm.io/api/core.md#EntityData)\<T>
  * ##### options: [FactoryOptions](https://mikro-orm.io/api/core/interface/FactoryOptions.md) = <!-- -->{}

  #### Returns void
