# Source: https://mikro-orm.io/api/mongodb/class/MongoDriver.md

# MongoDriver<!-- -->

### Hierarchy

* [DatabaseDriver](https://mikro-orm.io/api/core/class/DatabaseDriver.md)<[MongoConnection](https://mikro-orm.io/api/mongodb/class/MongoConnection.md)>
  * *MongoDriver*

## Index[**](#index)

### Constructors

* [**constructor](#constructor)

### Properties

* [**\[EntityManagerType\]](#\[EntityManagerType])
* [**config](#config)

### Methods

* [**aggregate](#aggregate)
* [**close](#close)
* [**connect](#connect)
* [**convertException](#convertException)
* [**count](#count)
* [**countVirtual](#countVirtual)
* [**createEntityManager](#createentitymanager)
* [**find](#find)
* [**findOne](#findone)
* [**findVirtual](#findvirtual)
* [**getConnection](#getConnection)
* [**getDependencies](#getDependencies)
* [**getMetadata](#getMetadata)
* [**getORMClass](#getormclass)
* [**getPlatform](#getplatform)
* [**loadFromPivotTable](#loadFromPivotTable)
* [**lockPessimistic](#lockPessimistic)
* [**mapResult](#mapResult)
* [**nativeDelete](#nativedelete)
* [**nativeInsert](#nativeinsert)
* [**nativeInsertMany](#nativeinsertmany)
* [**nativeUpdate](#nativeupdate)
* [**nativeUpdateMany](#nativeupdatemany)
* [**reconnect](#reconnect)
* [**setMetadata](#setMetadata)
* [**stream](#stream)
* [**streamAggregate](#streamaggregate)
* [**streamVirtual](#streamvirtual)
* [**syncCollections](#syncCollections)

## Constructors<!-- -->[**](#constructors)

### [**](#constructor)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/mongodb/src/MongoDriver.ts#L42)constructor

* ****new MongoDriver**(config): [MongoDriver](https://mikro-orm.io/api/mongodb/class/MongoDriver.md)

* Overrides DatabaseDriver\<MongoConnection>.constructor

  #### Parameters

  * ##### config: [Configuration](https://mikro-orm.io/api/core/class/Configuration.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>, [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>>>

  #### Returns [MongoDriver](https://mikro-orm.io/api/mongodb/class/MongoDriver.md)

## Properties<!-- -->[**](#properties)

### [**](#\[EntityManagerType])[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/mongodb/src/MongoDriver.ts#L37)\[EntityManagerType]

**\[EntityManagerType]: [MongoEntityManager](https://mikro-orm.io/api/mongodb/class/EntityManager.md)<[MongoDriver](https://mikro-orm.io/api/mongodb/class/MongoDriver.md)>

Overrides DatabaseDriver.\[EntityManagerType]

### [**](#config)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/DatabaseDriver.ts#L58)readonlyinheritedconfig

**config: [Configuration](https://mikro-orm.io/api/core/class/Configuration.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>, [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>>>

Inherited from DatabaseDriver.config

## Methods<!-- -->[**](#methods)

### [**](#aggregate)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/mongodb/src/MongoDriver.ts#L407)aggregate

* ****aggregate**(entityName, pipeline, ctx): Promise\<any\[]>

* Overrides DatabaseDriver.aggregate

  #### Parameters

  * ##### entityName: [EntityName](https://mikro-orm.io/api/core.md#EntityName)

  * ##### pipeline: any\[]

  * ##### optionalctx: ClientSession

  #### Returns Promise\<any\[]>

### [**](#close)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/DatabaseDriver.ts#L218)inheritedclose

* ****close**(force): Promise\<void>

* Inherited from DatabaseDriver.close

  #### Parameters

  * ##### optionalforce: boolean

  #### Returns Promise\<void>

### [**](#connect)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/DatabaseDriver.ts#L194)inheritedconnect

* ****connect**(options): Promise<[MongoConnection](https://mikro-orm.io/api/mongodb/class/MongoConnection.md)>

* Inherited from DatabaseDriver.connect

  #### Parameters

  * ##### optionaloptions: { skipOnConnect?<!-- -->: boolean }

    * ##### optionalskipOnConnect: boolean

  #### Returns Promise<[MongoConnection](https://mikro-orm.io/api/mongodb/class/MongoConnection.md)>

### [**](#convertException)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/DatabaseDriver.ts#L691)inheritedconvertException

* ****convertException**(exception): [DriverException](https://mikro-orm.io/api/core/class/DriverException.md)

* Inherited from DatabaseDriver.convertException

  Converts native db errors to standardized driver exceptions

  ***

  #### Parameters

  * ##### exception: Error

  #### Returns [DriverException](https://mikro-orm.io/api/core/class/DriverException.md)

### [**](#count)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/mongodb/src/MongoDriver.ts#L233)count

* ****count**\<T>(entityName, where, options): Promise\<number>

* Overrides DatabaseDriver.count

  #### Parameters

  * ##### entityName: [EntityName](https://mikro-orm.io/api/core.md#EntityName)\<T>

  * ##### where: [FilterQuery](https://mikro-orm.io/api/core.md#FilterQuery)\<T>

  * ##### options: [CountOptions](https://mikro-orm.io/api/core/interface/CountOptions.md)\<T, never> = <!-- -->{}

  #### Returns Promise\<number>

### [**](#countVirtual)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/DatabaseDriver.ts#L130)inheritedcountVirtual

* ****countVirtual**\<T>(entityName, where, options): Promise\<number>

* Inherited from DatabaseDriver.countVirtual

  #### Parameters

  * ##### entityName: [EntityName](https://mikro-orm.io/api/core.md#EntityName)\<T>

  * ##### where: [FilterQuery](https://mikro-orm.io/api/core.md#FilterQuery)\<T>

  * ##### options: [CountOptions](https://mikro-orm.io/api/core/interface/CountOptions.md)\<T, any>

  #### Returns Promise\<number>

### [**](#createentitymanager)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/mongodb/src/MongoDriver.ts#L46)createEntityManager

* ****createEntityManager**(useContext): [MongoEntityManager](https://mikro-orm.io/api/mongodb/class/EntityManager.md)<[MongoDriver](https://mikro-orm.io/api/mongodb/class/MongoDriver.md)>

* Overrides DatabaseDriver.createEntityManager

  #### Parameters

  * ##### optionaluseContext: boolean

  #### Returns [MongoEntityManager](https://mikro-orm.io/api/mongodb/class/EntityManager.md)<[MongoDriver](https://mikro-orm.io/api/mongodb/class/MongoDriver.md)>

### [**](#find)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/mongodb/src/MongoDriver.ts#L87)find

* ****find**\<T, P, F, E>(entityName, where, options): Promise<[EntityData](https://mikro-orm.io/api/core.md#EntityData)\<T>\[]>

* Overrides DatabaseDriver.find

  Finds selection of entities

  ***

  #### Parameters

  * ##### entityName: [EntityName](https://mikro-orm.io/api/core.md#EntityName)\<T>

  * ##### where: [FilterQuery](https://mikro-orm.io/api/core.md#FilterQuery)\<T>

  * ##### options: [FindOptions](https://mikro-orm.io/api/core/interface/FindOptions.md)\<T, P, F, E> = <!-- -->{}

  #### Returns Promise<[EntityData](https://mikro-orm.io/api/core.md#EntityData)\<T>\[]>

### [**](#findone)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/mongodb/src/MongoDriver.ts#L156)findOne

* ****findOne**\<T, P, F, E>(entityName, where, options): Promise\<null | [EntityData](https://mikro-orm.io/api/core.md#EntityData)\<T>>

* Overrides DatabaseDriver.findOne

  Finds single entity (table row, document)

  ***

  #### Parameters

  * ##### entityName: [EntityName](https://mikro-orm.io/api/core.md#EntityName)\<T>

  * ##### where: [FilterQuery](https://mikro-orm.io/api/core.md#FilterQuery)\<T>

  * ##### options: [FindOneOptions](https://mikro-orm.io/api/core/interface/FindOneOptions.md)\<T, P, F, E> = <!-- -->

  #### Returns Promise\<null | [EntityData](https://mikro-orm.io/api/core.md#EntityData)\<T>>

### [**](#findvirtual)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/mongodb/src/MongoDriver.ts#L198)findVirtual

* ****findVirtual**\<T>(entityName, where, options): Promise<[EntityData](https://mikro-orm.io/api/core.md#EntityData)\<T>\[]>

* Overrides DatabaseDriver.findVirtual

  #### Parameters

  * ##### entityName: [EntityName](https://mikro-orm.io/api/core.md#EntityName)\<T>

  * ##### where: [FilterQuery](https://mikro-orm.io/api/core.md#FilterQuery)\<T>

  * ##### options: [FindOptions](https://mikro-orm.io/api/core/interface/FindOptions.md)\<T, any, any, any>

  #### Returns Promise<[EntityData](https://mikro-orm.io/api/core.md#EntityData)\<T>\[]>

### [**](#getConnection)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/DatabaseDriver.ts#L208)inheritedgetConnection

* ****getConnection**(type): [MongoConnection](https://mikro-orm.io/api/mongodb/class/MongoConnection.md)

* Inherited from DatabaseDriver.getConnection

  #### Parameters

  * ##### type: [ConnectionType](https://mikro-orm.io/api/core.md#ConnectionType) = <!-- -->'write'

  #### Returns [MongoConnection](https://mikro-orm.io/api/mongodb/class/MongoConnection.md)

### [**](#getDependencies)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/DatabaseDriver.ts#L242)inheritedgetDependencies

* ****getDependencies**(): string\[]

* Inherited from DatabaseDriver.getDependencies

  Returns name of the underlying database dependencies (e.g. `mongodb` or `mysql2`) for SQL drivers it also returns `knex` in the array as connectors are not used directly there

  ***

  #### Returns string\[]

### [**](#getMetadata)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/DatabaseDriver.ts#L238)inheritedgetMetadata

* ****getMetadata**(): [MetadataStorage](https://mikro-orm.io/api/core/class/MetadataStorage.md)

* Inherited from DatabaseDriver.getMetadata

  #### Returns [MetadataStorage](https://mikro-orm.io/api/core/class/MetadataStorage.md)

### [**](#getormclass)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/mongodb/src/MongoDriver.ts#L687)getORMClass

* ****getORMClass**(): [Constructor](https://mikro-orm.io/api/core.md#Constructor)<[MongoMikroORM](https://mikro-orm.io/api/mongodb/class/MikroORM.md)<[MongoEntityManager](https://mikro-orm.io/api/mongodb/class/EntityManager.md)<[MongoDriver](https://mikro-orm.io/api/mongodb/class/MongoDriver.md)>, (string | [EntitySchema](https://mikro-orm.io/api/core/class/EntitySchema.md)\<any, never, [EntityCtor](https://mikro-orm.io/api/core.md#EntityCtor)\<any>> | [EntityClass](https://mikro-orm.io/api/core.md#EntityClass)\<Partial\<any>>)\[]>>

* Overrides DatabaseDriver.getORMClass

  * **@inheritDoc**

  ***

  #### Returns [Constructor](https://mikro-orm.io/api/core.md#Constructor)<[MongoMikroORM](https://mikro-orm.io/api/mongodb/class/MikroORM.md)<[MongoEntityManager](https://mikro-orm.io/api/mongodb/class/EntityManager.md)<[MongoDriver](https://mikro-orm.io/api/mongodb/class/MongoDriver.md)>, (string | [EntitySchema](https://mikro-orm.io/api/core/class/EntitySchema.md)\<any, never, [EntityCtor](https://mikro-orm.io/api/core.md#EntityCtor)\<any>> | [EntityClass](https://mikro-orm.io/api/core.md#EntityClass)\<Partial\<any>>)\[]>>

### [**](#getplatform)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/mongodb/src/MongoDriver.ts#L419)getPlatform

* ****getPlatform**(): [MongoPlatform](https://mikro-orm.io/api/mongodb/class/MongoPlatform.md)

* Overrides DatabaseDriver.getPlatform

  #### Returns [MongoPlatform](https://mikro-orm.io/api/mongodb/class/MongoPlatform.md)

### [**](#loadFromPivotTable)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/DatabaseDriver.ts#L142)inheritedloadFromPivotTable

* ****loadFromPivotTable**\<T, O>(prop, owners, where, orderBy, ctx, options, pivotJoin): Promise<[Dictionary](https://mikro-orm.io/api/core.md#Dictionary)\<T\[]>>

* Inherited from DatabaseDriver.loadFromPivotTable

  When driver uses pivot tables for M:N, this method will load identifiers for given collections from them

  ***

  #### Parameters

  * ##### prop: [EntityProperty](https://mikro-orm.io/api/core/interface/EntityProperty.md)\<any, any>

  * ##### owners: (O extends { \[PrimaryKeyProp]?<!-- -->: PK } ? PK extends undefined ? Omit\<O\<O>, typeof [PrimaryKeyProp](https://mikro-orm.io/api/core.md#PrimaryKeyProp)> : PK extends keyof<!-- --> O\<O> ? ReadonlyPrimary\<UnwrapPrimary\<O\<O>\[PK\<PK>]>> : PK extends keyof<!-- --> O\<O>\[] ? ReadonlyPrimary\<PrimaryPropToType\<O\<O>, PK\<PK>>> : PK : O extends { \_id?<!-- -->: PK } ? string | ReadonlyPrimary\<PK> : O extends { id?<!-- -->: PK } ? ReadonlyPrimary\<PK> : O extends { uuid?<!-- -->: PK } ? ReadonlyPrimary\<PK> : O)\[]\[]

  * ##### optionalwhere: any

  * ##### optionalorderBy: [OrderDefinition](https://mikro-orm.io/api/core.md#OrderDefinition)\<T>

  * ##### optionalctx: any

  * ##### optionaloptions: [FindOptions](https://mikro-orm.io/api/core/interface/FindOptions.md)\<T, any, any, any>

  * ##### optionalpivotJoin: boolean

  #### Returns Promise<[Dictionary](https://mikro-orm.io/api/core.md#Dictionary)\<T\[]>>

### [**](#lockPessimistic)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/DatabaseDriver.ts#L678)inheritedlockPessimistic

* ****lockPessimistic**\<T>(entity, options): Promise\<void>

* Inherited from DatabaseDriver.lockPessimistic

  #### Parameters

  * ##### entity: T

  * ##### options: [LockOptions](https://mikro-orm.io/api/core/interface/LockOptions.md)

  #### Returns Promise\<void>

### [**](#mapResult)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/DatabaseDriver.ts#L182)inheritedmapResult

* ****mapResult**\<T>(result, meta, populate): null | [EntityData](https://mikro-orm.io/api/core.md#EntityData)\<T>

* Inherited from DatabaseDriver.mapResult

  #### Parameters

  * ##### result: [EntityDictionary](https://mikro-orm.io/api/core.md#EntityDictionary)\<T>

  * ##### optionalmeta: [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<T, [EntityCtor](https://mikro-orm.io/api/core.md#EntityCtor)\<T>>

  * ##### populate: [PopulateOptions](https://mikro-orm.io/api/core.md#PopulateOptions)\<T>\[] = <!-- -->\[]

  #### Returns null | [EntityData](https://mikro-orm.io/api/core.md#EntityData)\<T>

### [**](#nativedelete)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/mongodb/src/MongoDriver.ts#L391)nativeDelete

* ****nativeDelete**\<T>(entityName, where, options): Promise<[QueryResult](https://mikro-orm.io/api/core/interface/QueryResult.md)\<T>>

* Overrides DatabaseDriver.nativeDelete

  #### Parameters

  * ##### entityName: [EntityName](https://mikro-orm.io/api/core.md#EntityName)\<T>

  * ##### where: [FilterQuery](https://mikro-orm.io/api/core.md#FilterQuery)\<T>

  * ##### options: { ctx?<!-- -->: ClientSession } = <!-- -->{}

    * ##### optionalctx: ClientSession

  #### Returns Promise<[QueryResult](https://mikro-orm.io/api/core/interface/QueryResult.md)\<T>>

### [**](#nativeinsert)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/mongodb/src/MongoDriver.ts#L254)nativeInsert

* ****nativeInsert**\<T>(entityName, data, options): Promise<[QueryResult](https://mikro-orm.io/api/core/interface/QueryResult.md)\<T>>

* Overrides DatabaseDriver.nativeInsert

  #### Parameters

  * ##### entityName: [EntityName](https://mikro-orm.io/api/core.md#EntityName)\<T>

  * ##### data: [EntityDictionary](https://mikro-orm.io/api/core.md#EntityDictionary)\<T>

  * ##### options: [NativeInsertUpdateOptions](https://mikro-orm.io/api/core/interface/NativeInsertUpdateOptions.md)\<T> = <!-- -->{}

  #### Returns Promise<[QueryResult](https://mikro-orm.io/api/core/interface/QueryResult.md)\<T>>

### [**](#nativeinsertmany)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/mongodb/src/MongoDriver.ts#L266)nativeInsertMany

* ****nativeInsertMany**\<T>(entityName, data, options): Promise<[QueryResult](https://mikro-orm.io/api/core/interface/QueryResult.md)\<T>>

* Overrides DatabaseDriver.nativeInsertMany

  #### Parameters

  * ##### entityName: [EntityName](https://mikro-orm.io/api/core.md#EntityName)\<T>

  * ##### data: [EntityDictionary](https://mikro-orm.io/api/core.md#EntityDictionary)\<T>\[]

  * ##### options: [NativeInsertUpdateManyOptions](https://mikro-orm.io/api/core/interface/NativeInsertUpdateManyOptions.md)\<T> = <!-- -->{}

  #### Returns Promise<[QueryResult](https://mikro-orm.io/api/core/interface/QueryResult.md)\<T>>

### [**](#nativeupdate)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/mongodb/src/MongoDriver.ts#L284)nativeUpdate

* ****nativeUpdate**\<T>(entityName, where, data, options): Promise<[QueryResult](https://mikro-orm.io/api/core/interface/QueryResult.md)\<T>>

* Overrides DatabaseDriver.nativeUpdate

  #### Parameters

  * ##### entityName: [EntityName](https://mikro-orm.io/api/core.md#EntityName)\<T>

  * ##### where: [FilterQuery](https://mikro-orm.io/api/core.md#FilterQuery)\<T>

  * ##### data: [EntityDictionary](https://mikro-orm.io/api/core.md#EntityDictionary)\<T>

  * ##### options: [NativeInsertUpdateOptions](https://mikro-orm.io/api/core/interface/NativeInsertUpdateOptions.md)\<T> & [UpsertOptions](https://mikro-orm.io/api/core/interface/UpsertOptions.md)\<T, never> = <!-- -->{}

  #### Returns Promise<[QueryResult](https://mikro-orm.io/api/core/interface/QueryResult.md)\<T>>

### [**](#nativeupdatemany)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/mongodb/src/MongoDriver.ts#L328)nativeUpdateMany

* ****nativeUpdateMany**\<T>(entityName, where, data, options): Promise<[QueryResult](https://mikro-orm.io/api/core/interface/QueryResult.md)\<T>>

* Overrides DatabaseDriver.nativeUpdateMany

  #### Parameters

  * ##### entityName: [EntityName](https://mikro-orm.io/api/core.md#EntityName)\<T>

  * ##### where: [FilterQuery](https://mikro-orm.io/api/core.md#FilterQuery)\<T>\[]

  * ##### data: [EntityDictionary](https://mikro-orm.io/api/core.md#EntityDictionary)\<T>\[]

  * ##### options: [NativeInsertUpdateOptions](https://mikro-orm.io/api/core/interface/NativeInsertUpdateOptions.md)\<T> & [UpsertManyOptions](https://mikro-orm.io/api/core/interface/UpsertManyOptions.md)\<T, never> = <!-- -->{}

  #### Returns Promise<[QueryResult](https://mikro-orm.io/api/core/interface/QueryResult.md)\<T>>

### [**](#reconnect)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/DatabaseDriver.ts#L201)inheritedreconnect

* ****reconnect**(options): Promise<[MongoConnection](https://mikro-orm.io/api/mongodb/class/MongoConnection.md)>

* Inherited from DatabaseDriver.reconnect

  #### Parameters

  * ##### optionaloptions: { skipOnConnect?<!-- -->: boolean }

    * ##### optionalskipOnConnect: boolean

  #### Returns Promise<[MongoConnection](https://mikro-orm.io/api/mongodb/class/MongoConnection.md)>

### [**](#setMetadata)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/DatabaseDriver.ts#L227)inheritedsetMetadata

* ****setMetadata**(metadata): void

* Inherited from DatabaseDriver.setMetadata

  #### Parameters

  * ##### metadata: [MetadataStorage](https://mikro-orm.io/api/core/class/MetadataStorage.md)

  #### Returns void

### [**](#stream)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/mongodb/src/MongoDriver.ts#L51)stream

* ****stream**\<T>(entityName, where, options): AsyncIterableIterator\<T, any, any>

* Overrides DatabaseDriver.stream

  #### Parameters

  * ##### entityName: [EntityName](https://mikro-orm.io/api/core.md#EntityName)\<T>

  * ##### where: [FilterQuery](https://mikro-orm.io/api/core.md#FilterQuery)\<T>

  * ##### options: [StreamOptions](https://mikro-orm.io/api/core/interface/StreamOptions.md)\<T, any, any, any> & { rawResults?<!-- -->: boolean }

  #### Returns AsyncIterableIterator\<T, any, any>

### [**](#streamaggregate)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/mongodb/src/MongoDriver.ts#L411)streamAggregate

* ****streamAggregate**\<T>(entityName, pipeline, ctx): AsyncIterableIterator\<T, any, any>

* #### Parameters

  * ##### entityName: [EntityName](https://mikro-orm.io/api/core.md#EntityName)\<T>

  * ##### pipeline: any\[]

  * ##### optionalctx: ClientSession

  #### Returns AsyncIterableIterator\<T, any, any>

### [**](#streamvirtual)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/mongodb/src/MongoDriver.ts#L214)streamVirtual

* ****streamVirtual**\<T>(entityName, where, options): AsyncIterableIterator<[EntityData](https://mikro-orm.io/api/core.md#EntityData)\<T>, any, any>

* #### Parameters

  * ##### entityName: [EntityName](https://mikro-orm.io/api/core.md#EntityName)\<T>

  * ##### where: [FilterQuery](https://mikro-orm.io/api/core.md#FilterQuery)\<T>

  * ##### options: [FindOptions](https://mikro-orm.io/api/core/interface/FindOptions.md)\<T, any, any, any>

  #### Returns AsyncIterableIterator<[EntityData](https://mikro-orm.io/api/core.md#EntityData)\<T>, any, any>

### [**](#syncCollections)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/DatabaseDriver.ts#L154)inheritedsyncCollections

* ****syncCollections**\<T, O>(collections, options): Promise\<void>

* Inherited from DatabaseDriver.syncCollections

  #### Parameters

  * ##### collections: Iterable<[Collection](https://mikro-orm.io/api/core/class/Collection.md)\<T, O>, any, any>

  * ##### optionaloptions: [DriverMethodOptions](https://mikro-orm.io/api/core/interface/DriverMethodOptions.md)

  #### Returns Promise\<void>
