# Source: https://mikro-orm.io/api/core/class/MetadataStorage.md

# MetadataStorage<!-- -->

## Index[**](#Index)

### Constructors

* [**constructor](#constructor)

### Properties

* [**PATH\_SYMBOL](#PATH_SYMBOL)

### Methods

* [**\[iterator\]](#\[iterator])
* [**decorate](#decorate)
* [**find](#find)
* [**get](#get)
* [**getAll](#getAll)
* [**getByDiscriminatorColumn](#getByDiscriminatorColumn)
* [**has](#has)
* [**reset](#reset)
* [**set](#set)
* [**clear](#clear)
* [**getMetadata](#getMetadata)
* [**getMetadataFromDecorator](#getMetadataFromDecorator)
* [**init](#init)
* [**isKnownEntity](#isKnownEntity)

## Constructors<!-- -->[**](#Constructors)

### [**](#constructor)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/metadata/MetadataStorage.ts#L14)constructor

* ****new MetadataStorage**(metadata): [MetadataStorage](https://mikro-orm.io/api/core/class/MetadataStorage.md)

- #### Parameters

  * ##### metadata: [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)<[EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<any>> = <!-- -->{}

  #### Returns [MetadataStorage](https://mikro-orm.io/api/core/class/MetadataStorage.md)

## Properties<!-- -->[**](#Properties)

### [**](#PATH_SYMBOL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/metadata/MetadataStorage.ts#L9)staticreadonlyPATH\_SYMBOL

**PATH\_SYMBOL: typeof PATH\_SYMBOL =

<!-- -->

...

## Methods<!-- -->[**](#Methods)

### [**](#\[iterator])[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/metadata/MetadataStorage.ts#L115)\[iterator]

* ****\[iterator]**(): IterableIterator<[EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<any>, any, any>

- #### Returns IterableIterator<[EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<any>, any, any>

### [**](#decorate)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/metadata/MetadataStorage.ts#L109)decorate

* ****decorate**(em): void

- #### Parameters

  * ##### em: [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>>

  #### Returns void

### [**](#find)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/metadata/MetadataStorage.ts#L88)find

* ****find**\<T>(entityName): undefined | [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<T>

- #### Parameters

  * ##### entityName: [EntityName](https://mikro-orm.io/api/core.md#EntityName)\<T>

  #### Returns undefined | [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<T>

### [**](#get)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/metadata/MetadataStorage.ts#L74)get

* ****get**\<T>(entityName, init, validate): [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<T>

- #### Parameters

  * ##### entityName: [EntityName](https://mikro-orm.io/api/core.md#EntityName)\<T>
  * ##### init: boolean = <!-- -->false
  * ##### validate: boolean = <!-- -->true

  #### Returns [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<T>

### [**](#getAll)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/metadata/MetadataStorage.ts#L58)getAll

* ****getAll**(): [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)<[EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<any>>

- #### Returns [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)<[EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<any>>

### [**](#getByDiscriminatorColumn)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/metadata/MetadataStorage.ts#L62)getByDiscriminatorColumn

* ****getByDiscriminatorColumn**\<T>(meta, data): undefined | [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<T>

- #### Parameters

  * ##### meta: [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<T>
  * ##### data: [EntityData](https://mikro-orm.io/api/core.md#EntityData)\<T>

  #### Returns undefined | [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<T>

### [**](#has)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/metadata/MetadataStorage.ts#L97)has

* ****has**(entity): boolean

- #### Parameters

  * ##### entity: string

  #### Returns boolean

### [**](#reset)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/metadata/MetadataStorage.ts#L105)reset

* ****reset**(entity): void

- #### Parameters

  * ##### entity: string

  #### Returns void

### [**](#set)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/metadata/MetadataStorage.ts#L101)set

* ****set**(entity, meta): [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<any>

- #### Parameters

  * ##### entity: string
  * ##### meta: [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<any>

  #### Returns [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<any>

### [**](#clear)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/metadata/MetadataStorage.ts#L54)staticclear

* ****clear**(): void

- #### Returns void

### [**](#getMetadata)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/metadata/MetadataStorage.ts#L18)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/metadata/MetadataStorage.ts#L19)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/metadata/MetadataStorage.ts#L20)staticgetMetadata

* ****getMetadata**(): [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)<[EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<any>>
* ****getMetadata**\<T>(entity, path): [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<T>

- #### Returns [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)<[EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<any>>

### [**](#getMetadataFromDecorator)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/metadata/MetadataStorage.ts#L38)staticgetMetadataFromDecorator

* ****getMetadataFromDecorator**\<T>(target): [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<T>

- #### Parameters

  * ##### target: T & [Dictionary](https://mikro-orm.io/api/core.md#Dictionary) & { \[PATH\_SYMBOL]?<!-- -->: string }

  #### Returns [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<T>

### [**](#init)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/metadata/MetadataStorage.ts#L50)staticinit

* ****init**(): [MetadataStorage](https://mikro-orm.io/api/core/class/MetadataStorage.md)

- #### Returns [MetadataStorage](https://mikro-orm.io/api/core/class/MetadataStorage.md)

### [**](#isKnownEntity)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/metadata/MetadataStorage.ts#L34)staticisKnownEntity

* ****isKnownEntity**(name): boolean

- #### Parameters

  * ##### name: string

  #### Returns boolean
