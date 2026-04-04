# Source: https://mikro-orm.io/api/core/class/EntityValidator.md

# EntityValidator<!-- -->

## Index[**](#Index)

### Constructors

* [**constructor](#constructor)

### Properties

* [**KNOWN\_TYPES](#KNOWN_TYPES)

### Methods

* [**validate](#validate)
* [**validateEmptyWhere](#validateEmptyWhere)
* [**validateParams](#validateParams)
* [**validatePrimaryKey](#validatePrimaryKey)
* [**validateProperty](#validateProperty)
* [**validateRequired](#validateRequired)

## Constructors<!-- -->[**](#Constructors)

### [**](#constructor)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/EntityValidator.ts#L12)constructor

* ****new EntityValidator**(strict): [EntityValidator](https://mikro-orm.io/api/core/class/EntityValidator.md)

- #### Parameters

  * ##### strict: boolean

  #### Returns [EntityValidator](https://mikro-orm.io/api/core/class/EntityValidator.md)

## Properties<!-- -->[**](#Properties)

### [**](#KNOWN_TYPES)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/EntityValidator.ts#L10)KNOWN\_TYPES

**KNOWN\_TYPES: Set\<string> =

<!-- -->

...

## Methods<!-- -->[**](#Methods)

### [**](#validate)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/EntityValidator.ts#L14)validate

* ****validate**\<T>(entity, payload, meta): void

- #### Parameters

  * ##### entity: T
  * ##### payload: any
  * ##### meta: [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<T>

  #### Returns void

### [**](#validateEmptyWhere)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/EntityValidator.ts#L120)validateEmptyWhere

* ****validateEmptyWhere**\<T>(where): void

- #### Parameters

  * ##### where: [FilterQuery](https://mikro-orm.io/api/core.md#FilterQuery)\<T>

  #### Returns void

### [**](#validateParams)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/EntityValidator.ts#L96)validateParams

* ****validateParams**(params, type, field): void

- #### Parameters

  * ##### params: any
  * ##### type: string = <!-- -->'search condition'
  * ##### optionalfield: string

  #### Returns void

### [**](#validatePrimaryKey)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/EntityValidator.ts#L112)validatePrimaryKey

* ****validatePrimaryKey**\<T>(entity, meta): void

- #### Parameters

  * ##### entity: [EntityData](https://mikro-orm.io/api/core.md#EntityData)\<T>
  * ##### meta: [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<T>

  #### Returns void

### [**](#validateProperty)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/EntityValidator.ts#L68)validateProperty

* ****validateProperty**\<T>(prop, givenValue, entity): any

- #### Parameters

  * ##### prop: [EntityProperty](https://mikro-orm.io/api/core/interface/EntityProperty.md)\<any, any>
  * ##### givenValue: any
  * ##### entity: T

  #### Returns any

### [**](#validateRequired)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/EntityValidator.ts#L45)validateRequired

* ****validateRequired**\<T>(entity): void

- #### Parameters

  * ##### entity: T

  #### Returns void
