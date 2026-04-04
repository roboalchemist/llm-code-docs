# Source: https://mikro-orm.io/api/libsql/class/LibSqlDriver.md

# LibSqlDriver<!-- -->

### Hierarchy

* [AbstractSqlDriver](https://mikro-orm.io/api/knex/class/AbstractSqlDriver.md)<[LibSqlConnection](https://mikro-orm.io/api/libsql/class/LibSqlConnection.md)>
  * *LibSqlDriver*

## Index[**](#Index)

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
* [**createEntityManager](#createEntityManager)
* [**execute](#execute)
* [**find](#find)
* [**findOne](#findOne)
* [**findVirtual](#findVirtual)
* [**getConnection](#getConnection)
* [**getDependencies](#getDependencies)
* [**getMetadata](#getMetadata)
* [**getPlatform](#getPlatform)
* [**loadFromPivotTable](#loadFromPivotTable)
* [**lockPessimistic](#lockPessimistic)
* [**mapResult](#mapResult)
* [**nativeDelete](#nativeDelete)
* [**nativeInsert](#nativeInsert)
* [**nativeInsertMany](#nativeInsertMany)
* [**nativeUpdate](#nativeUpdate)
* [**nativeUpdateMany](#nativeUpdateMany)
* [**reconnect](#reconnect)
* [**setMetadata](#setMetadata)
* [**syncCollections](#syncCollections)

## Constructors<!-- -->[**](#Constructors)

### [**](#constructor)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/libsql/src/LibSqlDriver.ts#L8)constructor

* ****new LibSqlDriver**(config): [LibSqlDriver](https://mikro-orm.io/api/libsql/class/LibSqlDriver.md)

- Overrides AbstractSqlDriver\<LibSqlConnection>.constructor

  #### Parameters

  * ##### config: [Configuration](https://mikro-orm.io/api/core/class/Configuration.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>, [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>>>

  #### Returns [LibSqlDriver](https://mikro-orm.io/api/libsql/class/LibSqlDriver.md)

## Properties<!-- -->[**](#Properties)

### [**](#\[EntityManagerType])[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/AbstractSqlDriver.ts#L70)inherited\[EntityManagerType]

**\[EntityManagerType]: [SqlEntityManager](https://mikro-orm.io/api/knex/class/EntityManager.md)<[LibSqlDriver](https://mikro-orm.io/api/libsql/class/LibSqlDriver.md)>

Inherited from AbstractSqlDriver.\[EntityManagerType]

### [**](#config)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/DatabaseDriver.ts#L51)readonlyinheritedconfig

**config: [Configuration](https://mikro-orm.io/api/core/class/Configuration.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>, [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>>>

Inherited from AbstractSqlDriver.config

## Methods<!-- -->[**](#Methods)

### [**](#aggregate)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/DatabaseDriver.ts#L89)inheritedaggregate

* ****aggregate**(entityName, pipeline): Promise\<any\[]>

- Inherited from AbstractSqlDriver.aggregate

  #### Parameters

  * ##### entityName: string
  * ##### pipeline: any\[]

  #### Returns Promise\<any\[]>

### [**](#close)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/DatabaseDriver.ts#L148)inheritedclose

* ****close**(force): Promise\<void>

- Inherited from AbstractSqlDriver.close

  #### Parameters

  * ##### optionalforce: boolean

  #### Returns Promise\<void>

### [**](#connect)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/DatabaseDriver.ts#L124)inheritedconnect

* ****connect**(): Promise<[LibSqlConnection](https://mikro-orm.io/api/libsql/class/LibSqlConnection.md)>

- Inherited from AbstractSqlDriver.connect

  #### Returns Promise<[LibSqlConnection](https://mikro-orm.io/api/libsql/class/LibSqlConnection.md)>

### [**](#convertException)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/DatabaseDriver.ts#L470)inheritedconvertException

* ****convertException**(exception): [DriverException](https://mikro-orm.io/api/core/class/DriverException.md)

- Inherited from AbstractSqlDriver.convertException

  Converts native db errors to standardized driver exceptions

  ***

  #### Parameters

  * ##### exception: Error

  #### Returns [DriverException](https://mikro-orm.io/api/core/class/DriverException.md)

### [**](#count)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/AbstractSqlDriver.ts#L450)inheritedcount

* ****count**\<T>(entityName, where, options): Promise\<number>

- Inherited from AbstractSqlDriver.count

  #### Parameters

  * ##### entityName: string
  * ##### where: any
  * ##### options: [CountOptions](https://mikro-orm.io/api/core/interface/CountOptions.md)\<T, never> = <!-- -->{}

  #### Returns Promise\<number>

### [**](#countVirtual)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/AbstractSqlDriver.ts#L198)inheritedcountVirtual

* ****countVirtual**\<T>(entityName, where, options): Promise\<number>

- Inherited from AbstractSqlDriver.countVirtual

  #### Parameters

  * ##### entityName: string
  * ##### where: [ObjectQuery](https://mikro-orm.io/api/core.md#ObjectQuery)\<T>
  * ##### options: [CountOptions](https://mikro-orm.io/api/core/interface/CountOptions.md)\<T, any>

  #### Returns Promise\<number>

### [**](#createEntityManager)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/AbstractSqlDriver.ts#L87)inheritedcreateEntityManager

* ****createEntityManager**\<D>(useContext): D\[typeof [EntityManagerType](https://mikro-orm.io/api/core.md#EntityManagerType)]

- Inherited from AbstractSqlDriver.createEntityManager

  #### Parameters

  * ##### optionaluseContext: boolean

  #### Returns D\[typeof [EntityManagerType](https://mikro-orm.io/api/core.md#EntityManagerType)]

### [**](#execute)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/AbstractSqlDriver.ts#L1067)inheritedexecute

* ****execute**\<T>(queryOrKnex, params, method, ctx, loggerContext): Promise\<T>

- Inherited from AbstractSqlDriver.execute

  #### Parameters

  * ##### queryOrKnex: string | QueryBuilder\<any, any> | Raw\<any>
  * ##### params: any\[] = <!-- -->\[]
  * ##### method: get | all | run = <!-- -->'all'
  * ##### optionalctx: any
  * ##### optionalloggerContext: [LoggingOptions](https://mikro-orm.io/api/core.md#LoggingOptions)

  #### Returns Promise\<T>

### [**](#find)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/AbstractSqlDriver.ts#L92)inheritedfind

* ****find**\<T, P, F, E>(entityName, where, options): Promise<[EntityData](https://mikro-orm.io/api/core.md#EntityData)\<T>\[]>

- Inherited from AbstractSqlDriver.find

  Finds selection of entities

  ***

  #### Parameters

  * ##### entityName: string
  * ##### where: [ObjectQuery](https://mikro-orm.io/api/core.md#ObjectQuery)\<T>
  * ##### options: [FindOptions](https://mikro-orm.io/api/core/interface/FindOptions.md)\<T, P, F, E> = <!-- -->{}

  #### Returns Promise<[EntityData](https://mikro-orm.io/api/core.md#EntityData)\<T>\[]>

### [**](#findOne)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/AbstractSqlDriver.ts#L158)inheritedfindOne

* ****findOne**\<T, P, F, E>(entityName, where, options): Promise\<null | [EntityData](https://mikro-orm.io/api/core.md#EntityData)\<T>>

- Inherited from AbstractSqlDriver.findOne

  Finds single entity (table row, document)

  ***

  #### Parameters

  * ##### entityName: string
  * ##### where: [ObjectQuery](https://mikro-orm.io/api/core.md#ObjectQuery)\<T>
  * ##### optionaloptions: [FindOneOptions](https://mikro-orm.io/api/core/interface/FindOneOptions.md)\<T, P, F, E>

  #### Returns Promise\<null | [EntityData](https://mikro-orm.io/api/core.md#EntityData)\<T>>

### [**](#findVirtual)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/AbstractSqlDriver.ts#L194)inheritedfindVirtual

* ****findVirtual**\<T>(entityName, where, options): Promise<[EntityData](https://mikro-orm.io/api/core.md#EntityData)\<T>\[]>

- Inherited from AbstractSqlDriver.findVirtual

  #### Parameters

  * ##### entityName: string
  * ##### where: [ObjectQuery](https://mikro-orm.io/api/core.md#ObjectQuery)\<T>
  * ##### options: [FindOptions](https://mikro-orm.io/api/core/interface/FindOptions.md)\<T, any, any, any>

  #### Returns Promise<[EntityData](https://mikro-orm.io/api/core.md#EntityData)\<T>\[]>

### [**](#getConnection)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/DatabaseDriver.ts#L138)inheritedgetConnection

* ****getConnection**(type): [LibSqlConnection](https://mikro-orm.io/api/libsql/class/LibSqlConnection.md)

- Inherited from AbstractSqlDriver.getConnection

  #### Parameters

  * ##### type: [ConnectionType](https://mikro-orm.io/api/core.md#ConnectionType) = <!-- -->'write'

  #### Returns [LibSqlConnection](https://mikro-orm.io/api/libsql/class/LibSqlConnection.md)

### [**](#getDependencies)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/DatabaseDriver.ts#L172)inheritedgetDependencies

* ****getDependencies**(): string\[]

- Inherited from AbstractSqlDriver.getDependencies

  Returns name of the underlying database dependencies (e.g. `mongodb` or `mysql2`) for SQL drivers it also returns `knex` in the array as connectors are not used directly there

  ***

  #### Returns string\[]

### [**](#getMetadata)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/DatabaseDriver.ts#L168)inheritedgetMetadata

* ****getMetadata**(): [MetadataStorage](https://mikro-orm.io/api/core/class/MetadataStorage.md)

- Inherited from AbstractSqlDriver.getMetadata

  #### Returns [MetadataStorage](https://mikro-orm.io/api/core/class/MetadataStorage.md)

### [**](#getPlatform)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/AbstractSqlDriver.ts#L83)inheritedgetPlatform

* ****getPlatform**(): [AbstractSqlPlatform](https://mikro-orm.io/api/knex/class/AbstractSqlPlatform.md)

- Inherited from AbstractSqlDriver.getPlatform

  #### Returns [AbstractSqlPlatform](https://mikro-orm.io/api/knex/class/AbstractSqlPlatform.md)

### [**](#loadFromPivotTable)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/AbstractSqlDriver.ts#L991)inheritedloadFromPivotTable

* ****loadFromPivotTable**\<T, O>(prop, owners, where, orderBy, ctx, options, pivotJoin): Promise<[Dictionary](https://mikro-orm.io/api/core.md#Dictionary)\<T\[]>>

- Inherited from AbstractSqlDriver.loadFromPivotTable

  When driver uses pivot tables for M:N, this method will load identifiers for given collections from them

  ***

  #### Parameters

  * ##### prop: [EntityProperty](https://mikro-orm.io/api/core/interface/EntityProperty.md)\<any, any>
  * ##### owners: (O extends { \[PrimaryKeyProp]?<!-- -->: PK } ? PK extends undefined ? Omit\<O\<O>, typeof [PrimaryKeyProp](https://mikro-orm.io/api/core.md#PrimaryKeyProp)> : PK extends keyof<!-- --> O\<O> ? ReadonlyPrimary\<UnwrapPrimary\<O\<O>\[PK\<PK>]>> : PK extends keyof<!-- --> O\<O>\[] ? ReadonlyPrimary\<PrimaryPropToType\<O\<O>, PK\<PK>>> : PK : O extends { \_id?<!-- -->: PK } ? string | ReadonlyPrimary\<PK> : O extends { id?<!-- -->: PK } ? ReadonlyPrimary\<PK> : O extends { uuid?<!-- -->: PK } ? ReadonlyPrimary\<PK> : O)\[]\[]
  * ##### where: any = <!-- -->...
  * ##### optionalorderBy: [OrderDefinition](https://mikro-orm.io/api/core.md#OrderDefinition)\<T>
  * ##### optionalctx: any
  * ##### optionaloptions: [FindOptions](https://mikro-orm.io/api/core/interface/FindOptions.md)\<T, any, any, any>
  * ##### optionalpivotJoin: boolean

  #### Returns Promise<[Dictionary](https://mikro-orm.io/api/core.md#Dictionary)\<T\[]>>

### [**](#lockPessimistic)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/AbstractSqlDriver.ts#L1390)inheritedlockPessimistic

* ****lockPessimistic**\<T>(entity, options): Promise\<void>

- Inherited from AbstractSqlDriver.lockPessimistic

  #### Parameters

  * ##### entity: T
  * ##### options: [LockOptions](https://mikro-orm.io/api/core/interface/LockOptions.md)

  #### Returns Promise\<void>

### [**](#mapResult)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/AbstractSqlDriver.ts#L282)inheritedmapResult

* ****mapResult**\<T>(result, meta, populate, qb, map): null | [EntityData](https://mikro-orm.io/api/core.md#EntityData)\<T>

- Inherited from AbstractSqlDriver.mapResult

  #### Parameters

  * ##### result: [EntityData](https://mikro-orm.io/api/core.md#EntityData)\<T>
  * ##### meta: [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<T>
  * ##### populate: [PopulateOptions](https://mikro-orm.io/api/core.md#PopulateOptions)\<T>\[] = <!-- -->\[]
  * ##### optionalqb: [QueryBuilder](https://mikro-orm.io/api/knex/class/QueryBuilder.md)\<T, any, any, any>
  * ##### map: [Dictionary](https://mikro-orm.io/api/core.md#Dictionary) = <!-- -->{}

  #### Returns null | [EntityData](https://mikro-orm.io/api/core.md#EntityData)\<T>

### [**](#nativeDelete)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/AbstractSqlDriver.ts#L871)inheritednativeDelete

* ****nativeDelete**\<T>(entityName, where, options): Promise<[QueryResult](https://mikro-orm.io/api/core/interface/QueryResult.md)\<T>>

- Inherited from AbstractSqlDriver.nativeDelete

  #### Parameters

  * ##### entityName: string
  * ##### where: any
  * ##### options: [DeleteOptions](https://mikro-orm.io/api/core/interface/DeleteOptions.md)\<T> = <!-- -->{}

  #### Returns Promise<[QueryResult](https://mikro-orm.io/api/core/interface/QueryResult.md)\<T>>

### [**](#nativeInsert)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/AbstractSqlDriver.ts#L488)inheritednativeInsert

* ****nativeInsert**\<T>(entityName, data, options): Promise<[QueryResult](https://mikro-orm.io/api/core/interface/QueryResult.md)\<T>>

- Inherited from AbstractSqlDriver.nativeInsert

  #### Parameters

  * ##### entityName: string
  * ##### data: [EntityDictionary](https://mikro-orm.io/api/core.md#EntityDictionary)\<T>
  * ##### options: [NativeInsertUpdateOptions](https://mikro-orm.io/api/core/interface/NativeInsertUpdateOptions.md)\<T> = <!-- -->{}

  #### Returns Promise<[QueryResult](https://mikro-orm.io/api/core/interface/QueryResult.md)\<T>>

### [**](#nativeInsertMany)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/AbstractSqlDriver.ts#L511)inheritednativeInsertMany

* ****nativeInsertMany**\<T>(entityName, data, options, transform): Promise<[QueryResult](https://mikro-orm.io/api/core/interface/QueryResult.md)\<T>>

- Inherited from AbstractSqlDriver.nativeInsertMany

  #### Parameters

  * ##### entityName: string
  * ##### data: [EntityDictionary](https://mikro-orm.io/api/core.md#EntityDictionary)\<T>\[]
  * ##### options: [NativeInsertUpdateManyOptions](https://mikro-orm.io/api/core/interface/NativeInsertUpdateManyOptions.md)\<T> = <!-- -->{}
  * ##### optionaltransform: (sql) => string


  #### Returns Promise<[QueryResult](https://mikro-orm.io/api/core/interface/QueryResult.md)\<T>>

### [**](#nativeUpdate)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/AbstractSqlDriver.ts#L666)inheritednativeUpdate

* ****nativeUpdate**\<T>(entityName, where, data, options): Promise<[QueryResult](https://mikro-orm.io/api/core/interface/QueryResult.md)\<T>>

- Inherited from AbstractSqlDriver.nativeUpdate

  #### Parameters

  * ##### entityName: string
  * ##### where: [FilterQuery](https://mikro-orm.io/api/core.md#FilterQuery)\<T>
  * ##### data: [EntityDictionary](https://mikro-orm.io/api/core.md#EntityDictionary)\<T>
  * ##### options: [NativeInsertUpdateOptions](https://mikro-orm.io/api/core/interface/NativeInsertUpdateOptions.md)\<T> & [UpsertOptions](https://mikro-orm.io/api/core/interface/UpsertOptions.md)\<T, never> = <!-- -->{}

  #### Returns Promise<[QueryResult](https://mikro-orm.io/api/core/interface/QueryResult.md)\<T>>

### [**](#nativeUpdateMany)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/AbstractSqlDriver.ts#L720)inheritednativeUpdateMany

* ****nativeUpdateMany**\<T>(entityName, where, data, options): Promise<[QueryResult](https://mikro-orm.io/api/core/interface/QueryResult.md)\<T>>

- Inherited from AbstractSqlDriver.nativeUpdateMany

  #### Parameters

  * ##### entityName: string
  * ##### where: [FilterQuery](https://mikro-orm.io/api/core.md#FilterQuery)\<T>\[]
  * ##### data: [EntityDictionary](https://mikro-orm.io/api/core.md#EntityDictionary)\<T>\[]
  * ##### options: [NativeInsertUpdateManyOptions](https://mikro-orm.io/api/core/interface/NativeInsertUpdateManyOptions.md)\<T> & [UpsertManyOptions](https://mikro-orm.io/api/core/interface/UpsertManyOptions.md)\<T, never> = <!-- -->{}

  #### Returns Promise<[QueryResult](https://mikro-orm.io/api/core/interface/QueryResult.md)\<T>>

### [**](#reconnect)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/DatabaseDriver.ts#L131)inheritedreconnect

* ****reconnect**(): Promise<[LibSqlConnection](https://mikro-orm.io/api/libsql/class/LibSqlConnection.md)>

- Inherited from AbstractSqlDriver.reconnect

  #### Returns Promise<[LibSqlConnection](https://mikro-orm.io/api/libsql/class/LibSqlConnection.md)>

### [**](#setMetadata)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/DatabaseDriver.ts#L157)inheritedsetMetadata

* ****setMetadata**(metadata): void

- Inherited from AbstractSqlDriver.setMetadata

  #### Parameters

  * ##### metadata: [MetadataStorage](https://mikro-orm.io/api/core/class/MetadataStorage.md)

  #### Returns void

### [**](#syncCollections)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/AbstractSqlDriver.ts#L905)inheritedsyncCollections

* ****syncCollections**\<T, O>(collections, options): Promise\<void>

- Inherited from AbstractSqlDriver.syncCollections

  #### Parameters

  * ##### collections: Iterable<[Collection](https://mikro-orm.io/api/core/class/Collection.md)\<T, O>, any, any>
  * ##### optionaloptions: [DriverMethodOptions](https://mikro-orm.io/api/core/interface/DriverMethodOptions.md)

  #### Returns Promise\<void>
