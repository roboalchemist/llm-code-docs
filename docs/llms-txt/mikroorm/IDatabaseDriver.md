# Source: https://mikro-orm.io/api/core/interface/IDatabaseDriver.md

# IDatabaseDriver<!-- --> \<C>

### Implemented by

* [DatabaseDriver](https://mikro-orm.io/api/core/class/DatabaseDriver.md)

## Index[**](#index)

### Properties

* [**\[EntityManagerType\]](#\[EntityManagerType])
* [**config](#config)

### Methods

* [**aggregate](#aggregate)
* [**close](#close)
* [**connect](#connect)
* [**convertException](#convertexception)
* [**count](#count)
* [**createEntityManager](#createentitymanager)
* [**find](#find)
* [**findOne](#findone)
* [**findVirtual](#findvirtual)
* [**getConnection](#getconnection)
* [**getDependencies](#getdependencies)
* [**getMetadata](#getmetadata)
* [**getPlatform](#getplatform)
* [**loadFromPivotTable](#loadfrompivottable)
* [**lockPessimistic](#lockpessimistic)
* [**mapResult](#mapresult)
* [**nativeDelete](#nativedelete)
* [**nativeInsert](#nativeinsert)
* [**nativeInsertMany](#nativeinsertmany)
* [**nativeUpdate](#nativeupdate)
* [**nativeUpdateMany](#nativeupdatemany)
* [**reconnect](#reconnect)
* [**setMetadata](#setmetadata)
* [**stream](#stream)
* [**syncCollections](#synccollections)

## Properties<!-- -->[**](#properties)

### [**](#\[EntityManagerType])[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/IDatabaseDriver.ts#L44)\[EntityManagerType]

**\[EntityManagerType]: [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)\<C>>

### [**](#config)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/IDatabaseDriver.ts#L45)readonlyconfig

**config: [Configuration](https://mikro-orm.io/api/core/class/Configuration.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>, [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>>>

## Methods<!-- -->[**](#methods)

### [**](#aggregate)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/IDatabaseDriver.ts#L131)aggregate

* ****aggregate**(entityName, pipeline): Promise\<any\[]>

* #### Parameters

  * ##### entityName: [EntityName](https://mikro-orm.io/api/core.md#EntityName)

  * ##### pipeline: any\[]

  #### Returns Promise\<any\[]>

### [**](#close)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/IDatabaseDriver.ts#L51)close

* ****close**(force): Promise\<void>

* #### Parameters

  * ##### optionalforce: boolean

  #### Returns Promise\<void>

### [**](#connect)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/IDatabaseDriver.ts#L49)connect

* ****connect**(options): Promise\<C>

* #### Parameters

  * ##### optionaloptions: { skipOnConnect?<!-- -->: boolean }

    * ##### optionalskipOnConnect: boolean

  #### Returns Promise\<C>

### [**](#convertexception)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/IDatabaseDriver.ts#L169)convertException

* ****convertException**(exception): [DriverException](https://mikro-orm.io/api/core/class/DriverException.md)

* Converts native db errors to standardized driver exceptions

  ***

  #### Parameters

  * ##### exception: Error

  #### Returns [DriverException](https://mikro-orm.io/api/core/class/DriverException.md)

### [**](#count)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/IDatabaseDriver.ts#L125)count

* ****count**\<T, P>(entityName, where, options): Promise\<number>

* #### Parameters

  * ##### entityName: [EntityName](https://mikro-orm.io/api/core.md#EntityName)\<T>

  * ##### where: [FilterQuery](https://mikro-orm.io/api/core.md#FilterQuery)\<T>

  * ##### optionaloptions: [CountOptions](https://mikro-orm.io/api/core/interface/CountOptions.md)\<T, P>

  #### Returns Promise\<number>

### [**](#createentitymanager)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/IDatabaseDriver.ts#L47)createEntityManager

* ****createEntityManager**(useContext): [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)\<C>>

* #### Parameters

  * ##### optionaluseContext: boolean

  #### Returns [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)\<C>>

### [**](#find)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/IDatabaseDriver.ts#L60)find

* ****find**\<T, P, F, E>(entityName, where, options): Promise<[EntityData](https://mikro-orm.io/api/core.md#EntityData)\<T>\[]>

* Finds selection of entities

  ***

  #### Parameters

  * ##### entityName: [EntityName](https://mikro-orm.io/api/core.md#EntityName)\<T>

  * ##### where: [FilterQuery](https://mikro-orm.io/api/core.md#FilterQuery)\<T>

  * ##### optionaloptions: [FindOptions](https://mikro-orm.io/api/core/interface/FindOptions.md)\<T, P, F, E>

  #### Returns Promise<[EntityData](https://mikro-orm.io/api/core.md#EntityData)\<T>\[]>

### [**](#findone)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/IDatabaseDriver.ts#L69)findOne

* ****findOne**\<T, P, F, E>(entityName, where, options): Promise\<null | [EntityData](https://mikro-orm.io/api/core.md#EntityData)\<T>>

* Finds single entity (table row, document)

  ***

  #### Parameters

  * ##### entityName: [EntityName](https://mikro-orm.io/api/core.md#EntityName)\<T>

  * ##### where: [FilterQuery](https://mikro-orm.io/api/core.md#FilterQuery)\<T>

  * ##### optionaloptions: [FindOneOptions](https://mikro-orm.io/api/core/interface/FindOneOptions.md)\<T, P, F, E>

  #### Returns Promise\<null | [EntityData](https://mikro-orm.io/api/core.md#EntityData)\<T>>

### [**](#findvirtual)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/IDatabaseDriver.ts#L75)findVirtual

* ****findVirtual**\<T>(entityName, where, options): Promise<[EntityData](https://mikro-orm.io/api/core.md#EntityData)\<T>\[]>

* #### Parameters

  * ##### entityName: [EntityName](https://mikro-orm.io/api/core.md#EntityName)\<T>

  * ##### where: [FilterQuery](https://mikro-orm.io/api/core.md#FilterQuery)\<T>

  * ##### options: [FindOptions](https://mikro-orm.io/api/core/interface/FindOptions.md)\<T, any, any, any>

  #### Returns Promise<[EntityData](https://mikro-orm.io/api/core.md#EntityData)\<T>\[]>

### [**](#getconnection)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/IDatabaseDriver.ts#L55)getConnection

* ****getConnection**(type): C

* #### Parameters

  * ##### optionaltype: [ConnectionType](https://mikro-orm.io/api/core.md#ConnectionType)

  #### Returns C

### [**](#getdependencies)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/IDatabaseDriver.ts#L162)getDependencies

* ****getDependencies**(): string\[]

* Returns name of the underlying database dependencies (e.g. `mongodb` or `mysql2`) for SQL drivers it also returns `knex` in the array as connectors are not used directly there

  ***

  #### Returns string\[]

### [**](#getmetadata)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/IDatabaseDriver.ts#L156)getMetadata

* ****getMetadata**(): [MetadataStorage](https://mikro-orm.io/api/core/class/MetadataStorage.md)

* #### Returns [MetadataStorage](https://mikro-orm.io/api/core/class/MetadataStorage.md)

### [**](#getplatform)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/IDatabaseDriver.ts#L152)getPlatform

* ****getPlatform**(): [Platform](https://mikro-orm.io/api/core/class/Platform.md)

* #### Returns [Platform](https://mikro-orm.io/api/core/class/Platform.md)

### [**](#loadfrompivottable)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/IDatabaseDriver.ts#L142)loadFromPivotTable

* ****loadFromPivotTable**\<T, O>(prop, owners, where, orderBy, ctx, options, pivotJoin): Promise<[Dictionary](https://mikro-orm.io/api/core.md#Dictionary)\<T\[]>>

* When driver uses pivot tables for M:N, this method will load identifiers for given collections from them

  ***

  #### Parameters

  * ##### prop: [EntityProperty](https://mikro-orm.io/api/core/interface/EntityProperty.md)\<any, any>

  * ##### owners: (O extends { \[PrimaryKeyProp]?<!-- -->: PK } ? PK extends undefined ? Omit\<O\<O>, typeof [PrimaryKeyProp](https://mikro-orm.io/api/core.md#PrimaryKeyProp)> : PK extends keyof<!-- --> O\<O> ? ReadonlyPrimary\<UnwrapPrimary\<O\<O>\[PK\<PK>]>> : PK extends keyof<!-- --> O\<O>\[] ? ReadonlyPrimary\<PrimaryPropToType\<O\<O>, PK\<PK>>> : PK : O extends { \_id?<!-- -->: PK } ? string | ReadonlyPrimary\<PK> : O extends { id?<!-- -->: PK } ? ReadonlyPrimary\<PK> : O extends { uuid?<!-- -->: PK } ? ReadonlyPrimary\<PK> : O)\[]\[]

  * ##### optionalwhere: [FilterQuery](https://mikro-orm.io/api/core.md#FilterQuery)\<T>

  * ##### optionalorderBy: [OrderDefinition](https://mikro-orm.io/api/core.md#OrderDefinition)\<T>

  * ##### optionalctx: any

  * ##### optionaloptions: [FindOptions](https://mikro-orm.io/api/core/interface/FindOptions.md)\<T, any, any, any>

  * ##### optionalpivotJoin: boolean

  #### Returns Promise<[Dictionary](https://mikro-orm.io/api/core.md#Dictionary)\<T\[]>>

### [**](#lockpessimistic)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/IDatabaseDriver.ts#L164)lockPessimistic

* ****lockPessimistic**\<T>(entity, options): Promise\<void>

* #### Parameters

  * ##### entity: T

  * ##### options: [LockOptions](https://mikro-orm.io/api/core/interface/LockOptions.md)

  #### Returns Promise\<void>

### [**](#mapresult)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/IDatabaseDriver.ts#L133)mapResult

* ****mapResult**\<T>(result, meta, populate): null | [EntityData](https://mikro-orm.io/api/core.md#EntityData)\<T>

* #### Parameters

  * ##### result: [EntityDictionary](https://mikro-orm.io/api/core.md#EntityDictionary)\<T>

  * ##### meta: [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<T, [EntityCtor](https://mikro-orm.io/api/core.md#EntityCtor)\<T>>

  * ##### optionalpopulate: [PopulateOptions](https://mikro-orm.io/api/core.md#PopulateOptions)\<T>\[]

  #### Returns null | [EntityData](https://mikro-orm.io/api/core.md#EntityData)\<T>

### [**](#nativedelete)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/IDatabaseDriver.ts#L114)nativeDelete

* ****nativeDelete**\<T>(entityName, where, options): Promise<[QueryResult](https://mikro-orm.io/api/core/interface/QueryResult.md)\<T>>

* #### Parameters

  * ##### entityName: [EntityName](https://mikro-orm.io/api/core.md#EntityName)\<T>

  * ##### where: [FilterQuery](https://mikro-orm.io/api/core.md#FilterQuery)\<T>

  * ##### optionaloptions: [NativeDeleteOptions](https://mikro-orm.io/api/core/interface/NativeDeleteOptions.md)\<T>

  #### Returns Promise<[QueryResult](https://mikro-orm.io/api/core/interface/QueryResult.md)\<T>>

### [**](#nativeinsert)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/IDatabaseDriver.ts#L87)nativeInsert

* ****nativeInsert**\<T>(entityName, data, options): Promise<[QueryResult](https://mikro-orm.io/api/core/interface/QueryResult.md)\<T>>

* #### Parameters

  * ##### entityName: [EntityName](https://mikro-orm.io/api/core.md#EntityName)\<T>

  * ##### data: [EntityDictionary](https://mikro-orm.io/api/core.md#EntityDictionary)\<T>

  * ##### optionaloptions: [NativeInsertUpdateOptions](https://mikro-orm.io/api/core/interface/NativeInsertUpdateOptions.md)\<T>

  #### Returns Promise<[QueryResult](https://mikro-orm.io/api/core/interface/QueryResult.md)\<T>>

### [**](#nativeinsertmany)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/IDatabaseDriver.ts#L93)nativeInsertMany

* ****nativeInsertMany**\<T>(entityName, data, options, transform): Promise<[QueryResult](https://mikro-orm.io/api/core/interface/QueryResult.md)\<T>>

* #### Parameters

  * ##### entityName: [EntityName](https://mikro-orm.io/api/core.md#EntityName)\<T>

  * ##### data: [EntityDictionary](https://mikro-orm.io/api/core.md#EntityDictionary)\<T>\[]

  * ##### optionaloptions: [NativeInsertUpdateManyOptions](https://mikro-orm.io/api/core/interface/NativeInsertUpdateManyOptions.md)\<T>

  * ##### optionaltransform: (sql) => string

  #### Returns Promise<[QueryResult](https://mikro-orm.io/api/core/interface/QueryResult.md)\<T>>

### [**](#nativeupdate)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/IDatabaseDriver.ts#L100)nativeUpdate

* ****nativeUpdate**\<T>(entityName, where, data, options): Promise<[QueryResult](https://mikro-orm.io/api/core/interface/QueryResult.md)\<T>>

* #### Parameters

  * ##### entityName: [EntityName](https://mikro-orm.io/api/core.md#EntityName)\<T>

  * ##### where: [FilterQuery](https://mikro-orm.io/api/core.md#FilterQuery)\<T>

  * ##### data: [EntityDictionary](https://mikro-orm.io/api/core.md#EntityDictionary)\<T>

  * ##### optionaloptions: [NativeInsertUpdateOptions](https://mikro-orm.io/api/core/interface/NativeInsertUpdateOptions.md)\<T>

  #### Returns Promise<[QueryResult](https://mikro-orm.io/api/core/interface/QueryResult.md)\<T>>

### [**](#nativeupdatemany)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/IDatabaseDriver.ts#L107)nativeUpdateMany

* ****nativeUpdateMany**\<T>(entityName, where, data, options): Promise<[QueryResult](https://mikro-orm.io/api/core/interface/QueryResult.md)\<T>>

* #### Parameters

  * ##### entityName: [EntityName](https://mikro-orm.io/api/core.md#EntityName)\<T>

  * ##### where: [FilterQuery](https://mikro-orm.io/api/core.md#FilterQuery)\<T>\[]

  * ##### data: [EntityDictionary](https://mikro-orm.io/api/core.md#EntityDictionary)\<T>\[]

  * ##### optionaloptions: [NativeInsertUpdateManyOptions](https://mikro-orm.io/api/core/interface/NativeInsertUpdateManyOptions.md)\<T>

  #### Returns Promise<[QueryResult](https://mikro-orm.io/api/core/interface/QueryResult.md)\<T>>

### [**](#reconnect)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/IDatabaseDriver.ts#L53)reconnect

* ****reconnect**(options): Promise\<C>

* #### Parameters

  * ##### optionaloptions: { skipOnConnect?<!-- -->: boolean }

    * ##### optionalskipOnConnect: boolean

  #### Returns Promise\<C>

### [**](#setmetadata)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/IDatabaseDriver.ts#L154)setMetadata

* ****setMetadata**(metadata): void

* #### Parameters

  * ##### metadata: [MetadataStorage](https://mikro-orm.io/api/core/class/MetadataStorage.md)

  #### Returns void

### [**](#stream)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/IDatabaseDriver.ts#L81)stream

* ****stream**\<T>(entityName, where, options): AsyncIterableIterator\<T, any, any>

* #### Parameters

  * ##### entityName: [EntityName](https://mikro-orm.io/api/core.md#EntityName)\<T>

  * ##### where: [FilterQuery](https://mikro-orm.io/api/core.md#FilterQuery)\<T>

  * ##### options: [StreamOptions](https://mikro-orm.io/api/core/interface/StreamOptions.md)\<T, never, \*, never>

  #### Returns AsyncIterableIterator\<T, any, any>

### [**](#synccollections)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/IDatabaseDriver.ts#L120)syncCollections

* ****syncCollections**\<T, O>(collections, options): Promise\<void>

* #### Parameters

  * ##### collections: Iterable<[Collection](https://mikro-orm.io/api/core/class/Collection.md)\<T, O>, any, any>

  * ##### optionaloptions: [DriverMethodOptions](https://mikro-orm.io/api/core/interface/DriverMethodOptions.md)

  #### Returns Promise\<void>
