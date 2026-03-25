# Source: https://mikro-orm.io/api/core/class/MetadataStorage.md

# MetadataStorage<!-- -->

## Index[**](#index)

### Constructors

* [**constructor](#constructor)

### Properties

* [**PATH\_SYMBOL](#PATH_SYMBOL)

### Methods

* [**\[iterator\]](#\[iterator])
* [**decorate](#decorate)
* [**find](#find)
* [**get](#get)
* [**getAll](#getall)
* [**getByClassName](#getbyclassname)
* [**getById](#getbyid)
* [**getByUniqueName](#getbyuniquename)
* [**has](#has)
* [**reset](#reset)
* [**set](#set)
* [**clear](#clear)
* [**getMetadata](#getMetadata)
* [**isKnownEntity](#isKnownEntity)

## Constructors<!-- -->[**](#constructors)

### [**](#constructor)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/MetadataStorage.ts#L24)constructor

* ****new MetadataStorage**(metadata): [MetadataStorage](https://mikro-orm.io/api/core/class/MetadataStorage.md)

* #### Parameters

  * ##### metadata: [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)<[EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<any, [EntityCtor](https://mikro-orm.io/api/core.md#EntityCtor)\<any>>> = <!-- -->{}

  #### Returns [MetadataStorage](https://mikro-orm.io/api/core/class/MetadataStorage.md)

## Properties<!-- -->[**](#properties)

### [**](#PATH_SYMBOL)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/MetadataStorage.ts#L16)staticreadonlyPATH\_SYMBOL

**PATH\_SYMBOL: typeof PATH\_SYMBOL =

<!-- -->

...

## Methods<!-- -->[**](#methods)

### [**](#\[iterator])[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/MetadataStorage.ts#L129)\[iterator]

* ****\[iterator]**(): IterableIterator<[EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<any, [EntityCtor](https://mikro-orm.io/api/core.md#EntityCtor)\<any>>, any, any>

* #### Returns IterableIterator<[EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<any, [EntityCtor](https://mikro-orm.io/api/core.md#EntityCtor)\<any>>, any, any>

### [**](#decorate)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/MetadataStorage.ts#L125)decorate

* ****decorate**(em): void

* #### Parameters

  * ##### em: [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>>

  #### Returns void

### [**](#find)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/MetadataStorage.ts#L83)find

* ****find**\<T>(entityName): undefined | [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<T, [EntityCtor](https://mikro-orm.io/api/core.md#EntityCtor)\<T>>

* #### Parameters

  * ##### entityName: [EntityName](https://mikro-orm.io/api/core.md#EntityName)\<T>

  #### Returns undefined | [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<T, [EntityCtor](https://mikro-orm.io/api/core.md#EntityCtor)\<T>>

### [**](#get)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/MetadataStorage.ts#L64)get

* ****get**\<T>(entityName, init): [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<T, [EntityCtor](https://mikro-orm.io/api/core.md#EntityCtor)\<T>>

* #### Parameters

  * ##### entityName: [EntityName](https://mikro-orm.io/api/core.md#EntityName)\<T>

  * ##### init: boolean = <!-- -->false

  #### Returns [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<T, [EntityCtor](https://mikro-orm.io/api/core.md#EntityCtor)\<T>>

### [**](#getall)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/MetadataStorage.ts#L60)getAll

* ****getAll**(): Map<[EntityName](https://mikro-orm.io/api/core.md#EntityName), [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<any, [EntityCtor](https://mikro-orm.io/api/core.md#EntityCtor)\<any>>>

* #### Returns Map<[EntityName](https://mikro-orm.io/api/core.md#EntityName), [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<any, [EntityCtor](https://mikro-orm.io/api/core.md#EntityCtor)\<any>>>

### [**](#getbyclassname)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/MetadataStorage.ts#L139)getByClassName

* ****getByClassName**\<T, V>(className, validate): V extends true ? [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<T, [EntityCtor](https://mikro-orm.io/api/core.md#EntityCtor)\<T>> : undefined | [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<T, [EntityCtor](https://mikro-orm.io/api/core.md#EntityCtor)\<T>>

* #### Parameters

  * ##### className: string

  * ##### validate: V = <!-- -->

  #### Returns V extends true ? [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<T, [EntityCtor](https://mikro-orm.io/api/core.md#EntityCtor)\<T>> : undefined | [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<T, [EntityCtor](https://mikro-orm.io/api/core.md#EntityCtor)\<T>>

### [**](#getbyid)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/MetadataStorage.ts#L135)getById

* ****getById**\<T>(id): [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<T, [EntityCtor](https://mikro-orm.io/api/core.md#EntityCtor)\<T>>

* #### Parameters

  * ##### id: number

  #### Returns [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<T, [EntityCtor](https://mikro-orm.io/api/core.md#EntityCtor)\<T>>

### [**](#getbyuniquename)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/MetadataStorage.ts#L146)getByUniqueName

* ****getByUniqueName**\<T, V>(uniqueName, validate): V extends true ? [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<T, [EntityCtor](https://mikro-orm.io/api/core.md#EntityCtor)\<T>> : undefined | [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<T, [EntityCtor](https://mikro-orm.io/api/core.md#EntityCtor)\<T>>

* #### Parameters

  * ##### uniqueName: string

  * ##### validate: V = <!-- -->

  #### Returns V extends true ? [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<T, [EntityCtor](https://mikro-orm.io/api/core.md#EntityCtor)\<T>> : undefined | [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<T, [EntityCtor](https://mikro-orm.io/api/core.md#EntityCtor)\<T>>

### [**](#has)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/MetadataStorage.ts#L101)has

* ****has**\<T>(entityName): boolean

* #### Parameters

  * ##### entityName: [EntityName](https://mikro-orm.io/api/core.md#EntityName)\<T>

  #### Returns boolean

### [**](#reset)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/MetadataStorage.ts#L114)reset

* ****reset**\<T>(entityName): void

* #### Parameters

  * ##### entityName: [EntityName](https://mikro-orm.io/api/core.md#EntityName)\<T>

  #### Returns void

### [**](#set)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/MetadataStorage.ts#L105)set

* ****set**\<T>(entityName, meta): [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<any, [EntityCtor](https://mikro-orm.io/api/core.md#EntityCtor)\<any>>

* #### Parameters

  * ##### entityName: [EntityName](https://mikro-orm.io/api/core.md#EntityName)\<T>

  * ##### meta: [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<any, [EntityCtor](https://mikro-orm.io/api/core.md#EntityCtor)\<any>>

  #### Returns [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<any, [EntityCtor](https://mikro-orm.io/api/core.md#EntityCtor)\<any>>

### [**](#clear)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/MetadataStorage.ts#L56)staticclear

* ****clear**(): void

* #### Returns void

### [**](#getMetadata)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/MetadataStorage.ts#L36)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/MetadataStorage.ts#L37)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/MetadataStorage.ts#L38)staticgetMetadata

* ****getMetadata**(): [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)<[EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<any, [EntityCtor](https://mikro-orm.io/api/core.md#EntityCtor)\<any>>>
* ****getMetadata**\<T>(entity, path): [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<T, [EntityCtor](https://mikro-orm.io/api/core.md#EntityCtor)\<T>>

* #### Returns [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)<[EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<any, [EntityCtor](https://mikro-orm.io/api/core.md#EntityCtor)\<any>>>

### [**](#isKnownEntity)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/MetadataStorage.ts#L52)staticisKnownEntity

* ****isKnownEntity**(name): boolean

* #### Parameters

  * ##### name: string

  #### Returns boolean
