# Source: https://mikro-orm.io/api/sql/class/AbstractSqlDriver.md

# abstractAbstractSqlDriver<!-- --> \<Connection, Platform>

### Hierarchy

* [DatabaseDriver](https://mikro-orm.io/api/core/class/DatabaseDriver.md)\<Connection>

  * *AbstractSqlDriver*

    * [SqliteDriver](https://mikro-orm.io/api/sql/class/SqliteDriver.md)
    * [PostgreSqlDriver](https://mikro-orm.io/api/postgresql/class/PostgreSqlDriver.md)
    * [MySqlDriver](https://mikro-orm.io/api/mysql/class/MySqlDriver.md)
    * [SqliteDriver](https://mikro-orm.io/api/sqlite/class/SqliteDriver.md)
    * [LibSqlDriver](https://mikro-orm.io/api/libsql/class/LibSqlDriver.md)
    * [MsSqlDriver](https://mikro-orm.io/api/mssql/class/MsSqlDriver.md)
    * [OracleDriver](https://mikro-orm.io/api/oracledb/class/OracleDriver.md)

## Index[**](#index)

### Properties

* [**\[EntityManagerType\]](#\[EntityManagerType])
* [**config](#config)

### Methods

* [**aggregate](#aggregate)
* [**close](#close)
* [**connect](#connect)
* [**convertException](#convertException)
* [**count](#count)
* [**countVirtual](#countvirtual)
* [**createEntityManager](#createentitymanager)
* [**evaluateFormula](#evaluateformula)
* [**execute](#execute)
* [**find](#find)
* [**findOne](#findone)
* [**findVirtual](#findvirtual)
* [**getConnection](#getConnection)
* [**getDependencies](#getDependencies)
* [**getMetadata](#getMetadata)
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
* [**setMetadata](#setMetadata)
* [**stream](#stream)
* [**syncCollections](#synccollections)

## Properties<!-- -->[**](#properties)

### [**](#\[EntityManagerType])[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/AbstractSqlDriver.ts#L76)\[EntityManagerType]

**\[EntityManagerType]: [SqlEntityManager](https://mikro-orm.io/api/sql/class/EntityManager.md)<[AbstractSqlDriver](https://mikro-orm.io/api/sql/class/AbstractSqlDriver.md)\<Connection, Platform>>

Overrides DatabaseDriver.\[EntityManagerType]

### [**](#config)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/DatabaseDriver.ts#L58)readonlyinheritedconfig

**config: [Configuration](https://mikro-orm.io/api/core/class/Configuration.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>, [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>>>

Inherited from DatabaseDriver.config

## Methods<!-- -->[**](#methods)

### [**](#aggregate)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/DatabaseDriver.ts#L138)inheritedaggregate

* ****aggregate**(entityName, pipeline): Promise\<any\[]>

* Inherited from DatabaseDriver.aggregate

  #### Parameters

  * ##### entityName: [EntityName](https://mikro-orm.io/api/core.md#EntityName)

  * ##### pipeline: any\[]

  #### Returns Promise\<any\[]>

### [**](#close)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/DatabaseDriver.ts#L218)inheritedclose

* ****close**(force): Promise\<void>

* Inherited from DatabaseDriver.close

  #### Parameters

  * ##### optionalforce: boolean

  #### Returns Promise\<void>

### [**](#connect)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/DatabaseDriver.ts#L194)inheritedconnect

* ****connect**(options): Promise\<Connection>

* Inherited from DatabaseDriver.connect

  #### Parameters

  * ##### optionaloptions: { skipOnConnect?<!-- -->: boolean }

    * ##### optionalskipOnConnect: boolean

  #### Returns Promise\<Connection>

### [**](#convertException)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/DatabaseDriver.ts#L691)inheritedconvertException

* ****convertException**(exception): [DriverException](https://mikro-orm.io/api/core/class/DriverException.md)

* Inherited from DatabaseDriver.convertException

  Converts native db errors to standardized driver exceptions

  ***

  #### Parameters

  * ##### exception: Error

  #### Returns [DriverException](https://mikro-orm.io/api/core/class/DriverException.md)

### [**](#count)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/AbstractSqlDriver.ts#L841)count

* ****count**\<T>(entityName, where, options): Promise\<number>

* Overrides DatabaseDriver.count

  #### Parameters

  * ##### entityName: [EntityName](https://mikro-orm.io/api/core.md#EntityName)\<T>

  * ##### where: any

  * ##### options: [CountOptions](https://mikro-orm.io/api/core/interface/CountOptions.md)\<T, never> = <!-- -->{}

  #### Returns Promise\<number>

### [**](#countvirtual)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/AbstractSqlDriver.ts#L287)countVirtual

* ****countVirtual**\<T>(entityName, where, options): Promise\<number>

* Overrides DatabaseDriver.countVirtual

  #### Parameters

  * ##### entityName: [EntityName](https://mikro-orm.io/api/core.md#EntityName)\<T>

  * ##### where: [ObjectQuery](https://mikro-orm.io/api/core.md#ObjectQuery)\<T>

  * ##### options: [CountOptions](https://mikro-orm.io/api/core/interface/CountOptions.md)\<T, any>

  #### Returns Promise\<number>

### [**](#createentitymanager)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/AbstractSqlDriver.ts#L130)createEntityManager

* ****createEntityManager**(useContext): [SqlEntityManager](https://mikro-orm.io/api/sql/class/EntityManager.md)<[AbstractSqlDriver](https://mikro-orm.io/api/sql/class/AbstractSqlDriver.md)\<Connection, Platform>>

* Overrides DatabaseDriver.createEntityManager

  #### Parameters

  * ##### optionaluseContext: boolean

  #### Returns [SqlEntityManager](https://mikro-orm.io/api/sql/class/EntityManager.md)<[AbstractSqlDriver](https://mikro-orm.io/api/sql/class/AbstractSqlDriver.md)\<Connection, Platform>>

### [**](#evaluateformula)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/AbstractSqlDriver.ts#L99)evaluateFormula

* ****evaluateFormula**(formula, columns, table): string

* Evaluates a formula callback, handling both string and Raw return values.

  ***

  #### Parameters

  * ##### formula: (...args) => string | [RawQueryFragment](https://mikro-orm.io/api/core/class/RawQueryFragment.md)\<string>

  *

    ##### columns: any

  * ##### table: [FormulaTable](https://mikro-orm.io/api/core.md#FormulaTable)

  #### Returns string

### [**](#execute)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/AbstractSqlDriver.ts#L1854)execute

* ****execute**\<T>(query, params, method, ctx, loggerContext): Promise\<T>

* #### Parameters

  * ##### query: string | [RawQueryFragment](https://mikro-orm.io/api/core/class/RawQueryFragment.md)\<string> | NativeQueryBuilder

  * ##### params: any\[] = <!-- -->\[]

  * ##### method: get | all | run = <!-- -->'all'

  * ##### optionalctx: any

  * ##### optionalloggerContext: [LoggingOptions](https://mikro-orm.io/api/core.md#LoggingOptions)

  #### Returns Promise\<T>

### [**](#find)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/AbstractSqlDriver.ts#L208)find

* ****find**\<T, P, F, E>(entityName, where, options): Promise<[EntityData](https://mikro-orm.io/api/core.md#EntityData)\<T>\[]>

* Overrides DatabaseDriver.find

  Finds selection of entities

  ***

  #### Parameters

  * ##### entityName: [EntityName](https://mikro-orm.io/api/core.md#EntityName)\<T>

  * ##### where: [ObjectQuery](https://mikro-orm.io/api/core.md#ObjectQuery)\<T>

  * ##### options: [FindOptions](https://mikro-orm.io/api/core/interface/FindOptions.md)\<T, P, F, E> = <!-- -->{}

  #### Returns Promise<[EntityData](https://mikro-orm.io/api/core.md#EntityData)\<T>\[]>

### [**](#findone)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/AbstractSqlDriver.ts#L234)findOne

* ****findOne**\<T, P, F, E>(entityName, where, options): Promise\<null | [EntityData](https://mikro-orm.io/api/core.md#EntityData)\<T>>

* Overrides DatabaseDriver.findOne

  Finds single entity (table row, document)

  ***

  #### Parameters

  * ##### entityName: [EntityName](https://mikro-orm.io/api/core.md#EntityName)\<T>

  * ##### where: [ObjectQuery](https://mikro-orm.io/api/core.md#ObjectQuery)\<T>

  * ##### optionaloptions: [FindOneOptions](https://mikro-orm.io/api/core/interface/FindOneOptions.md)\<T, P, F, E>

  #### Returns Promise\<null | [EntityData](https://mikro-orm.io/api/core.md#EntityData)\<T>>

### [**](#findvirtual)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/AbstractSqlDriver.ts#L279)findVirtual

* ****findVirtual**\<T>(entityName, where, options): Promise<[EntityData](https://mikro-orm.io/api/core.md#EntityData)\<T>\[]>

* Overrides DatabaseDriver.findVirtual

  #### Parameters

  * ##### entityName: [EntityName](https://mikro-orm.io/api/core.md#EntityName)\<T>

  * ##### where: [ObjectQuery](https://mikro-orm.io/api/core.md#ObjectQuery)\<T>

  * ##### options: [FindOptions](https://mikro-orm.io/api/core/interface/FindOptions.md)\<T, any, any, any>

  #### Returns Promise<[EntityData](https://mikro-orm.io/api/core.md#EntityData)\<T>\[]>

### [**](#getConnection)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/DatabaseDriver.ts#L208)inheritedgetConnection

* ****getConnection**(type): Connection

* Inherited from DatabaseDriver.getConnection

  #### Parameters

  * ##### type: [ConnectionType](https://mikro-orm.io/api/core.md#ConnectionType) = <!-- -->'write'

  #### Returns Connection

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

### [**](#getplatform)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/AbstractSqlDriver.ts#L94)getPlatform

* ****getPlatform**(): Platform

* Overrides DatabaseDriver.getPlatform

  #### Returns Platform

### [**](#loadfrompivottable)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/AbstractSqlDriver.ts#L1542)loadFromPivotTable

* ****loadFromPivotTable**\<T, O>(prop, owners, where, orderBy, ctx, options, pivotJoin): Promise<[Dictionary](https://mikro-orm.io/api/core.md#Dictionary)\<T\[]>>

* Overrides DatabaseDriver.loadFromPivotTable

  When driver uses pivot tables for M:N, this method will load identifiers for given collections from them

  ***

  #### Parameters

  * ##### prop: [EntityProperty](https://mikro-orm.io/api/core/interface/EntityProperty.md)\<any, any>

  * ##### owners: (O extends { \[PrimaryKeyProp]?<!-- -->: PK } ? PK extends undefined ? Omit\<O\<O>, typeof [PrimaryKeyProp](https://mikro-orm.io/api/core.md#PrimaryKeyProp)> : PK extends keyof<!-- --> O\<O> ? ReadonlyPrimary\<UnwrapPrimary\<O\<O>\[PK\<PK>]>> : PK extends keyof<!-- --> O\<O>\[] ? ReadonlyPrimary\<PrimaryPropToType\<O\<O>, PK\<PK>>> : PK : O extends { \_id?<!-- -->: PK } ? string | ReadonlyPrimary\<PK> : O extends { id?<!-- -->: PK } ? ReadonlyPrimary\<PK> : O extends { uuid?<!-- -->: PK } ? ReadonlyPrimary\<PK> : O)\[]\[]

  * ##### where: any = <!-- -->

  * ##### optionalorderBy: [OrderDefinition](https://mikro-orm.io/api/core.md#OrderDefinition)\<T>

  * ##### optionalctx: any

  * ##### optionaloptions: [FindOptions](https://mikro-orm.io/api/core/interface/FindOptions.md)\<T, any, any, any>

  * ##### optionalpivotJoin: boolean

  #### Returns Promise<[Dictionary](https://mikro-orm.io/api/core.md#Dictionary)\<T\[]>>

### [**](#lockpessimistic)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/AbstractSqlDriver.ts#L2524)lockPessimistic

* ****lockPessimistic**\<T>(entity, options): Promise\<void>

* Overrides DatabaseDriver.lockPessimistic

  #### Parameters

  * ##### entity: T

  * ##### options: [LockOptions](https://mikro-orm.io/api/core/interface/LockOptions.md)

  #### Returns Promise\<void>

### [**](#mapresult)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/AbstractSqlDriver.ts#L488)mapResult

* ****mapResult**\<T>(result, meta, populate, qb, map): null | [EntityData](https://mikro-orm.io/api/core.md#EntityData)\<T>

* Overrides DatabaseDriver.mapResult

  #### Parameters

  * ##### result: [EntityData](https://mikro-orm.io/api/core.md#EntityData)\<T>

  * ##### meta: [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<T, [EntityCtor](https://mikro-orm.io/api/core.md#EntityCtor)\<T>>

  * ##### populate: [PopulateOptions](https://mikro-orm.io/api/core.md#PopulateOptions)\<T>\[] = <!-- -->\[]

  * ##### optionalqb: [AnyQueryBuilder](https://mikro-orm.io/api/sql.md#AnyQueryBuilder)\<T>

  * ##### map: [Dictionary](https://mikro-orm.io/api/core.md#Dictionary) = <!-- -->{}

  #### Returns null | [EntityData](https://mikro-orm.io/api/core.md#EntityData)\<T>

### [**](#nativedelete)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/AbstractSqlDriver.ts#L1398)nativeDelete

* ****nativeDelete**\<T>(entityName, where, options): Promise<[QueryResult](https://mikro-orm.io/api/core/interface/QueryResult.md)\<T>>

* Overrides DatabaseDriver.nativeDelete

  #### Parameters

  * ##### entityName: [EntityName](https://mikro-orm.io/api/core.md#EntityName)\<T>

  * ##### where: any

  * ##### options: [DeleteOptions](https://mikro-orm.io/api/core/interface/DeleteOptions.md)\<T> = <!-- -->{}

  #### Returns Promise<[QueryResult](https://mikro-orm.io/api/core/interface/QueryResult.md)\<T>>

### [**](#nativeinsert)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/AbstractSqlDriver.ts#L887)nativeInsert

* ****nativeInsert**\<T>(entityName, data, options): Promise<[QueryResult](https://mikro-orm.io/api/core/interface/QueryResult.md)\<T>>

* Overrides DatabaseDriver.nativeInsert

  #### Parameters

  * ##### entityName: [EntityName](https://mikro-orm.io/api/core.md#EntityName)\<T>

  * ##### data: [EntityDictionary](https://mikro-orm.io/api/core.md#EntityDictionary)\<T>

  * ##### options: [NativeInsertUpdateOptions](https://mikro-orm.io/api/core/interface/NativeInsertUpdateOptions.md)\<T> = <!-- -->{}

  #### Returns Promise<[QueryResult](https://mikro-orm.io/api/core/interface/QueryResult.md)\<T>>

### [**](#nativeinsertmany)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/AbstractSqlDriver.ts#L925)nativeInsertMany

* ****nativeInsertMany**\<T>(entityName, data, options, transform): Promise<[QueryResult](https://mikro-orm.io/api/core/interface/QueryResult.md)\<T>>

* Overrides DatabaseDriver.nativeInsertMany

  #### Parameters

  * ##### entityName: [EntityName](https://mikro-orm.io/api/core.md#EntityName)\<T>

  * ##### data: [EntityDictionary](https://mikro-orm.io/api/core.md#EntityDictionary)\<T>\[]

  * ##### options: [NativeInsertUpdateManyOptions](https://mikro-orm.io/api/core/interface/NativeInsertUpdateManyOptions.md)\<T> = <!-- -->{}

  * ##### optionaltransform: (sql) => string

  #### Returns Promise<[QueryResult](https://mikro-orm.io/api/core/interface/QueryResult.md)\<T>>

### [**](#nativeupdate)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/AbstractSqlDriver.ts#L1125)nativeUpdate

* ****nativeUpdate**\<T>(entityName, where, data, options): Promise<[QueryResult](https://mikro-orm.io/api/core/interface/QueryResult.md)\<T>>

* Overrides DatabaseDriver.nativeUpdate

  #### Parameters

  * ##### entityName: [EntityName](https://mikro-orm.io/api/core.md#EntityName)\<T>

  * ##### where: [FilterQuery](https://mikro-orm.io/api/core.md#FilterQuery)\<T>

  * ##### data: [EntityDictionary](https://mikro-orm.io/api/core.md#EntityDictionary)\<T>

  * ##### options: [NativeInsertUpdateOptions](https://mikro-orm.io/api/core/interface/NativeInsertUpdateOptions.md)\<T> & [UpsertOptions](https://mikro-orm.io/api/core/interface/UpsertOptions.md)\<T, never> = <!-- -->{}

  #### Returns Promise<[QueryResult](https://mikro-orm.io/api/core/interface/QueryResult.md)\<T>>

### [**](#nativeupdatemany)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/AbstractSqlDriver.ts#L1199)nativeUpdateMany

* ****nativeUpdateMany**\<T>(entityName, where, data, options, transform): Promise<[QueryResult](https://mikro-orm.io/api/core/interface/QueryResult.md)\<T>>

* Overrides DatabaseDriver.nativeUpdateMany

  #### Parameters

  * ##### entityName: [EntityName](https://mikro-orm.io/api/core.md#EntityName)\<T>

  * ##### where: [FilterQuery](https://mikro-orm.io/api/core.md#FilterQuery)\<T>\[]

  * ##### data: [EntityDictionary](https://mikro-orm.io/api/core.md#EntityDictionary)\<T>\[]

  * ##### options: [NativeInsertUpdateManyOptions](https://mikro-orm.io/api/core/interface/NativeInsertUpdateManyOptions.md)\<T> & [UpsertManyOptions](https://mikro-orm.io/api/core/interface/UpsertManyOptions.md)\<T, never> = <!-- -->{}

  * ##### optionaltransform: (sql, params) => string

  #### Returns Promise<[QueryResult](https://mikro-orm.io/api/core/interface/QueryResult.md)\<T>>

### [**](#reconnect)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/DatabaseDriver.ts#L201)inheritedreconnect

* ****reconnect**(options): Promise\<Connection>

* Inherited from DatabaseDriver.reconnect

  #### Parameters

  * ##### optionaloptions: { skipOnConnect?<!-- -->: boolean }

    * ##### optionalskipOnConnect: boolean

  #### Returns Promise\<Connection>

### [**](#setMetadata)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/DatabaseDriver.ts#L227)inheritedsetMetadata

* ****setMetadata**(metadata): void

* Inherited from DatabaseDriver.setMetadata

  #### Parameters

  * ##### metadata: [MetadataStorage](https://mikro-orm.io/api/core/class/MetadataStorage.md)

  #### Returns void

### [**](#stream)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/AbstractSqlDriver.ts#L1864)stream

* ****stream**\<T>(entityName, where, options): AsyncIterableIterator\<T, any, any>

* Overrides DatabaseDriver.stream

  #### Parameters

  * ##### entityName: [EntityName](https://mikro-orm.io/api/core.md#EntityName)\<T>

  * ##### where: [FilterQuery](https://mikro-orm.io/api/core.md#FilterQuery)\<T>

  * ##### options: [StreamOptions](https://mikro-orm.io/api/core/interface/StreamOptions.md)\<T, any, any, any>

  #### Returns AsyncIterableIterator\<T, any, any>

### [**](#synccollections)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/AbstractSqlDriver.ts#L1442)syncCollections

* ****syncCollections**\<T, O>(collections, options): Promise\<void>

* Overrides DatabaseDriver.syncCollections

  #### Parameters

  * ##### collections: Iterable<[Collection](https://mikro-orm.io/api/core/class/Collection.md)\<T, O>, any, any>

  * ##### optionaloptions: [DriverMethodOptions](https://mikro-orm.io/api/core/interface/DriverMethodOptions.md)

  #### Returns Promise\<void>
