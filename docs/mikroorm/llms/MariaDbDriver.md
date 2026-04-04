# Source: https://mikro-orm.io/api/mariadb/class/MariaDbDriver.md

# MariaDbDriver<!-- -->

### Hierarchy

* [MySqlDriver](https://mikro-orm.io/api/mysql/class/MySqlDriver.md)
  * *MariaDbDriver*

## Index[**](#index)

### Constructors

* [**constructor](#constructor)

### Properties

* [**\[EntityManagerType\]](#\[EntityManagerType])
* [**config](#config)
* [**platform](#platform)

### Methods

* [**aggregate](#aggregate)
* [**close](#close)
* [**connect](#connect)
* [**convertException](#convertException)
* [**count](#count)
* [**countVirtual](#countVirtual)
* [**createEntityManager](#createEntityManager)
* [**evaluateFormula](#evaluateFormula)
* [**execute](#execute)
* [**find](#find)
* [**findOne](#findOne)
* [**findVirtual](#findVirtual)
* [**getConnection](#getConnection)
* [**getDependencies](#getDependencies)
* [**getMetadata](#getMetadata)
* [**getORMClass](#getormclass)
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
* [**stream](#stream)
* [**syncCollections](#syncCollections)

## Constructors<!-- -->[**](#constructors)

### [**](#constructor)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/mariadb/src/MariaDbDriver.ts#L19)constructor

* ****new MariaDbDriver**(config): [MariaDbDriver](https://mikro-orm.io/api/mariadb/class/MariaDbDriver.md)

* Overrides MySqlDriver.constructor

  #### Parameters

  * ##### config: [Configuration](https://mikro-orm.io/api/core/class/Configuration.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>, [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>>>

  #### Returns [MariaDbDriver](https://mikro-orm.io/api/mariadb/class/MariaDbDriver.md)

## Properties<!-- -->[**](#properties)

### [**](#\[EntityManagerType])[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/AbstractSqlDriver.ts#L76)inherited\[EntityManagerType]

**\[EntityManagerType]: [SqlEntityManager](https://mikro-orm.io/api/sql/class/EntityManager.md)<[MariaDbDriver](https://mikro-orm.io/api/mariadb/class/MariaDbDriver.md)>

Inherited from MySqlDriver.\[EntityManagerType]

### [**](#config)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/DatabaseDriver.ts#L58)readonlyinheritedconfig

**config: [Configuration](https://mikro-orm.io/api/core/class/Configuration.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>, [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>>>

Inherited from MySqlDriver.config

### [**](#platform)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/mariadb/src/MariaDbDriver.ts#L17)readonlyplatform

**platform: [MariaDbPlatform](https://mikro-orm.io/api/mariadb/class/MariaDbPlatform.md)

Overrides MySqlDriver.platform

## Methods<!-- -->[**](#methods)

### [**](#aggregate)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/DatabaseDriver.ts#L138)inheritedaggregate

* ****aggregate**(entityName, pipeline): Promise\<any\[]>

* Inherited from MySqlDriver.aggregate

  #### Parameters

  * ##### entityName: [EntityName](https://mikro-orm.io/api/core.md#EntityName)

  * ##### pipeline: any\[]

  #### Returns Promise\<any\[]>

### [**](#close)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/DatabaseDriver.ts#L218)inheritedclose

* ****close**(force): Promise\<void>

* Inherited from MySqlDriver.close

  #### Parameters

  * ##### optionalforce: boolean

  #### Returns Promise\<void>

### [**](#connect)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/DatabaseDriver.ts#L194)inheritedconnect

* ****connect**(options): Promise<[MySqlConnection](https://mikro-orm.io/api/mysql/class/MySqlConnection.md)>

* Inherited from MySqlDriver.connect

  #### Parameters

  * ##### optionaloptions: { skipOnConnect?<!-- -->: boolean }

    * ##### optionalskipOnConnect: boolean

  #### Returns Promise<[MySqlConnection](https://mikro-orm.io/api/mysql/class/MySqlConnection.md)>

### [**](#convertException)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/DatabaseDriver.ts#L691)inheritedconvertException

* ****convertException**(exception): [DriverException](https://mikro-orm.io/api/core/class/DriverException.md)

* Inherited from MySqlDriver.convertException

  Converts native db errors to standardized driver exceptions

  ***

  #### Parameters

  * ##### exception: Error

  #### Returns [DriverException](https://mikro-orm.io/api/core/class/DriverException.md)

### [**](#count)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/AbstractSqlDriver.ts#L841)inheritedcount

* ****count**\<T>(entityName, where, options): Promise\<number>

* Inherited from MySqlDriver.count

  #### Parameters

  * ##### entityName: [EntityName](https://mikro-orm.io/api/core.md#EntityName)\<T>

  * ##### where: any

  * ##### options: [CountOptions](https://mikro-orm.io/api/core/interface/CountOptions.md)\<T, never> = <!-- -->{}

  #### Returns Promise\<number>

### [**](#countVirtual)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/AbstractSqlDriver.ts#L287)inheritedcountVirtual

* ****countVirtual**\<T>(entityName, where, options): Promise\<number>

* Inherited from MySqlDriver.countVirtual

  #### Parameters

  * ##### entityName: [EntityName](https://mikro-orm.io/api/core.md#EntityName)\<T>

  * ##### where: [ObjectQuery](https://mikro-orm.io/api/core.md#ObjectQuery)\<T>

  * ##### options: [CountOptions](https://mikro-orm.io/api/core/interface/CountOptions.md)\<T, any>

  #### Returns Promise\<number>

### [**](#createEntityManager)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/AbstractSqlDriver.ts#L130)inheritedcreateEntityManager

* ****createEntityManager**(useContext): [SqlEntityManager](https://mikro-orm.io/api/sql/class/EntityManager.md)<[MariaDbDriver](https://mikro-orm.io/api/mariadb/class/MariaDbDriver.md)>

* Inherited from MySqlDriver.createEntityManager

  #### Parameters

  * ##### optionaluseContext: boolean

  #### Returns [SqlEntityManager](https://mikro-orm.io/api/sql/class/EntityManager.md)<[MariaDbDriver](https://mikro-orm.io/api/mariadb/class/MariaDbDriver.md)>

### [**](#evaluateFormula)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/AbstractSqlDriver.ts#L99)inheritedevaluateFormula

* ****evaluateFormula**(formula, columns, table): string

* Inherited from MySqlDriver.evaluateFormula

  Evaluates a formula callback, handling both string and Raw return values.

  ***

  #### Parameters

  * ##### formula: (...args) => string | [RawQueryFragment](https://mikro-orm.io/api/core/class/RawQueryFragment.md)\<string>

  *

    ##### columns: any

  * ##### table: [FormulaTable](https://mikro-orm.io/api/core.md#FormulaTable)

  #### Returns string

### [**](#execute)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/AbstractSqlDriver.ts#L1854)inheritedexecute

* ****execute**\<T>(query, params, method, ctx, loggerContext): Promise\<T>

* Inherited from MySqlDriver.execute

  #### Parameters

  * ##### query: string | [RawQueryFragment](https://mikro-orm.io/api/core/class/RawQueryFragment.md)\<string> | NativeQueryBuilder

  * ##### params: any\[] = <!-- -->\[]

  * ##### method: get | all | run = <!-- -->'all'

  * ##### optionalctx: any

  * ##### optionalloggerContext: [LoggingOptions](https://mikro-orm.io/api/core.md#LoggingOptions)

  #### Returns Promise\<T>

### [**](#find)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/AbstractSqlDriver.ts#L208)inheritedfind

* ****find**\<T, P, F, E>(entityName, where, options): Promise<[EntityData](https://mikro-orm.io/api/core.md#EntityData)\<T>\[]>

* Inherited from MySqlDriver.find

  Finds selection of entities

  ***

  #### Parameters

  * ##### entityName: [EntityName](https://mikro-orm.io/api/core.md#EntityName)\<T>

  * ##### where: [ObjectQuery](https://mikro-orm.io/api/core.md#ObjectQuery)\<T>

  * ##### options: [FindOptions](https://mikro-orm.io/api/core/interface/FindOptions.md)\<T, P, F, E> = <!-- -->{}

  #### Returns Promise<[EntityData](https://mikro-orm.io/api/core.md#EntityData)\<T>\[]>

### [**](#findOne)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/AbstractSqlDriver.ts#L234)inheritedfindOne

* ****findOne**\<T, P, F, E>(entityName, where, options): Promise\<null | [EntityData](https://mikro-orm.io/api/core.md#EntityData)\<T>>

* Inherited from MySqlDriver.findOne

  Finds single entity (table row, document)

  ***

  #### Parameters

  * ##### entityName: [EntityName](https://mikro-orm.io/api/core.md#EntityName)\<T>

  * ##### where: [ObjectQuery](https://mikro-orm.io/api/core.md#ObjectQuery)\<T>

  * ##### optionaloptions: [FindOneOptions](https://mikro-orm.io/api/core/interface/FindOneOptions.md)\<T, P, F, E>

  #### Returns Promise\<null | [EntityData](https://mikro-orm.io/api/core.md#EntityData)\<T>>

### [**](#findVirtual)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/AbstractSqlDriver.ts#L279)inheritedfindVirtual

* ****findVirtual**\<T>(entityName, where, options): Promise<[EntityData](https://mikro-orm.io/api/core.md#EntityData)\<T>\[]>

* Inherited from MySqlDriver.findVirtual

  #### Parameters

  * ##### entityName: [EntityName](https://mikro-orm.io/api/core.md#EntityName)\<T>

  * ##### where: [ObjectQuery](https://mikro-orm.io/api/core.md#ObjectQuery)\<T>

  * ##### options: [FindOptions](https://mikro-orm.io/api/core/interface/FindOptions.md)\<T, any, any, any>

  #### Returns Promise<[EntityData](https://mikro-orm.io/api/core.md#EntityData)\<T>\[]>

### [**](#getConnection)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/DatabaseDriver.ts#L208)inheritedgetConnection

* ****getConnection**(type): [MySqlConnection](https://mikro-orm.io/api/mysql/class/MySqlConnection.md)

* Inherited from MySqlDriver.getConnection

  #### Parameters

  * ##### type: [ConnectionType](https://mikro-orm.io/api/core.md#ConnectionType) = <!-- -->'write'

  #### Returns [MySqlConnection](https://mikro-orm.io/api/mysql/class/MySqlConnection.md)

### [**](#getDependencies)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/DatabaseDriver.ts#L242)inheritedgetDependencies

* ****getDependencies**(): string\[]

* Inherited from MySqlDriver.getDependencies

  Returns name of the underlying database dependencies (e.g. `mongodb` or `mysql2`) for SQL drivers it also returns `knex` in the array as connectors are not used directly there

  ***

  #### Returns string\[]

### [**](#getMetadata)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/DatabaseDriver.ts#L238)inheritedgetMetadata

* ****getMetadata**(): [MetadataStorage](https://mikro-orm.io/api/core/class/MetadataStorage.md)

* Inherited from MySqlDriver.getMetadata

  #### Returns [MetadataStorage](https://mikro-orm.io/api/core/class/MetadataStorage.md)

### [**](#getormclass)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/mariadb/src/MariaDbDriver.ts#L56)getORMClass

* ****getORMClass**(): [Constructor](https://mikro-orm.io/api/core.md#Constructor)<[MariaDbMikroORM](https://mikro-orm.io/api/mariadb/class/MikroORM.md)<[SqlEntityManager](https://mikro-orm.io/api/sql/class/EntityManager.md)<[MariaDbDriver](https://mikro-orm.io/api/mariadb/class/MariaDbDriver.md)>, (string | [EntitySchema](https://mikro-orm.io/api/core/class/EntitySchema.md)\<any, never, [EntityCtor](https://mikro-orm.io/api/core.md#EntityCtor)\<any>> | [EntityClass](https://mikro-orm.io/api/core.md#EntityClass)\<Partial\<any>>)\[]>>

* Overrides MySqlDriver.getORMClass

  * **@inheritDoc**

  ***

  #### Returns [Constructor](https://mikro-orm.io/api/core.md#Constructor)<[MariaDbMikroORM](https://mikro-orm.io/api/mariadb/class/MikroORM.md)<[SqlEntityManager](https://mikro-orm.io/api/sql/class/EntityManager.md)<[MariaDbDriver](https://mikro-orm.io/api/mariadb/class/MariaDbDriver.md)>, (string | [EntitySchema](https://mikro-orm.io/api/core/class/EntitySchema.md)\<any, never, [EntityCtor](https://mikro-orm.io/api/core.md#EntityCtor)\<any>> | [EntityClass](https://mikro-orm.io/api/core.md#EntityClass)\<Partial\<any>>)\[]>>

### [**](#getPlatform)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/AbstractSqlDriver.ts#L94)inheritedgetPlatform

* ****getPlatform**(): [MySqlPlatform](https://mikro-orm.io/api/mysql/class/MySqlPlatform.md)

* Inherited from MySqlDriver.getPlatform

  #### Returns [MySqlPlatform](https://mikro-orm.io/api/mysql/class/MySqlPlatform.md)

### [**](#loadFromPivotTable)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/AbstractSqlDriver.ts#L1542)inheritedloadFromPivotTable

* ****loadFromPivotTable**\<T, O>(prop, owners, where, orderBy, ctx, options, pivotJoin): Promise<[Dictionary](https://mikro-orm.io/api/core.md#Dictionary)\<T\[]>>

* Inherited from MySqlDriver.loadFromPivotTable

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

### [**](#lockPessimistic)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/AbstractSqlDriver.ts#L2524)inheritedlockPessimistic

* ****lockPessimistic**\<T>(entity, options): Promise\<void>

* Inherited from MySqlDriver.lockPessimistic

  #### Parameters

  * ##### entity: T

  * ##### options: [LockOptions](https://mikro-orm.io/api/core/interface/LockOptions.md)

  #### Returns Promise\<void>

### [**](#mapResult)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/AbstractSqlDriver.ts#L488)inheritedmapResult

* ****mapResult**\<T>(result, meta, populate, qb, map): null | [EntityData](https://mikro-orm.io/api/core.md#EntityData)\<T>

* Inherited from MySqlDriver.mapResult

  #### Parameters

  * ##### result: [EntityData](https://mikro-orm.io/api/core.md#EntityData)\<T>

  * ##### meta: [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<T, [EntityCtor](https://mikro-orm.io/api/core.md#EntityCtor)\<T>>

  * ##### populate: [PopulateOptions](https://mikro-orm.io/api/core.md#PopulateOptions)\<T>\[] = <!-- -->\[]

  * ##### optionalqb: [AnyQueryBuilder](https://mikro-orm.io/api/sql.md#AnyQueryBuilder)\<T>

  * ##### map: [Dictionary](https://mikro-orm.io/api/core.md#Dictionary) = <!-- -->{}

  #### Returns null | [EntityData](https://mikro-orm.io/api/core.md#EntityData)\<T>

### [**](#nativeDelete)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/AbstractSqlDriver.ts#L1398)inheritednativeDelete

* ****nativeDelete**\<T>(entityName, where, options): Promise<[QueryResult](https://mikro-orm.io/api/core/interface/QueryResult.md)\<T>>

* Inherited from MySqlDriver.nativeDelete

  #### Parameters

  * ##### entityName: [EntityName](https://mikro-orm.io/api/core.md#EntityName)\<T>

  * ##### where: any

  * ##### options: [DeleteOptions](https://mikro-orm.io/api/core/interface/DeleteOptions.md)\<T> = <!-- -->{}

  #### Returns Promise<[QueryResult](https://mikro-orm.io/api/core/interface/QueryResult.md)\<T>>

### [**](#nativeInsert)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/AbstractSqlDriver.ts#L887)inheritednativeInsert

* ****nativeInsert**\<T>(entityName, data, options): Promise<[QueryResult](https://mikro-orm.io/api/core/interface/QueryResult.md)\<T>>

* Inherited from MySqlDriver.nativeInsert

  #### Parameters

  * ##### entityName: [EntityName](https://mikro-orm.io/api/core.md#EntityName)\<T>

  * ##### data: [EntityDictionary](https://mikro-orm.io/api/core.md#EntityDictionary)\<T>

  * ##### options: [NativeInsertUpdateOptions](https://mikro-orm.io/api/core/interface/NativeInsertUpdateOptions.md)\<T> = <!-- -->{}

  #### Returns Promise<[QueryResult](https://mikro-orm.io/api/core/interface/QueryResult.md)\<T>>

### [**](#nativeInsertMany)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/mysql/src/MySqlDriver.ts#L43)inheritednativeInsertMany

* ****nativeInsertMany**\<T>(entityName, data, options): Promise<[QueryResult](https://mikro-orm.io/api/core/interface/QueryResult.md)\<T>>

* Inherited from MySqlDriver.nativeInsertMany

  #### Parameters

  * ##### entityName: [EntityName](https://mikro-orm.io/api/core.md#EntityName)\<T>

  * ##### data: [EntityDictionary](https://mikro-orm.io/api/core.md#EntityDictionary)\<T>\[]

  * ##### options: [NativeInsertUpdateManyOptions](https://mikro-orm.io/api/core/interface/NativeInsertUpdateManyOptions.md)\<T> = <!-- -->{}

  #### Returns Promise<[QueryResult](https://mikro-orm.io/api/core/interface/QueryResult.md)\<T>>

### [**](#nativeUpdate)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/AbstractSqlDriver.ts#L1125)inheritednativeUpdate

* ****nativeUpdate**\<T>(entityName, where, data, options): Promise<[QueryResult](https://mikro-orm.io/api/core/interface/QueryResult.md)\<T>>

* Inherited from MySqlDriver.nativeUpdate

  #### Parameters

  * ##### entityName: [EntityName](https://mikro-orm.io/api/core.md#EntityName)\<T>

  * ##### where: [FilterQuery](https://mikro-orm.io/api/core.md#FilterQuery)\<T>

  * ##### data: [EntityDictionary](https://mikro-orm.io/api/core.md#EntityDictionary)\<T>

  * ##### options: [NativeInsertUpdateOptions](https://mikro-orm.io/api/core/interface/NativeInsertUpdateOptions.md)\<T> & [UpsertOptions](https://mikro-orm.io/api/core/interface/UpsertOptions.md)\<T, never> = <!-- -->{}

  #### Returns Promise<[QueryResult](https://mikro-orm.io/api/core/interface/QueryResult.md)\<T>>

### [**](#nativeUpdateMany)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/mysql/src/MySqlDriver.ts#L63)inheritednativeUpdateMany

* ****nativeUpdateMany**\<T>(entityName, where, data, options): Promise<[QueryResult](https://mikro-orm.io/api/core/interface/QueryResult.md)\<T>>

* Inherited from MySqlDriver.nativeUpdateMany

  #### Parameters

  * ##### entityName: [EntityName](https://mikro-orm.io/api/core.md#EntityName)\<T>

  * ##### where: [FilterQuery](https://mikro-orm.io/api/core.md#FilterQuery)\<T>\[]

  * ##### data: [EntityDictionary](https://mikro-orm.io/api/core.md#EntityDictionary)\<T>\[]

  * ##### options: [NativeInsertUpdateManyOptions](https://mikro-orm.io/api/core/interface/NativeInsertUpdateManyOptions.md)\<T> & [UpsertManyOptions](https://mikro-orm.io/api/core/interface/UpsertManyOptions.md)\<T, never> = <!-- -->{}

  #### Returns Promise<[QueryResult](https://mikro-orm.io/api/core/interface/QueryResult.md)\<T>>

### [**](#reconnect)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/DatabaseDriver.ts#L201)inheritedreconnect

* ****reconnect**(options): Promise<[MySqlConnection](https://mikro-orm.io/api/mysql/class/MySqlConnection.md)>

* Inherited from MySqlDriver.reconnect

  #### Parameters

  * ##### optionaloptions: { skipOnConnect?<!-- -->: boolean }

    * ##### optionalskipOnConnect: boolean

  #### Returns Promise<[MySqlConnection](https://mikro-orm.io/api/mysql/class/MySqlConnection.md)>

### [**](#setMetadata)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/DatabaseDriver.ts#L227)inheritedsetMetadata

* ****setMetadata**(metadata): void

* Inherited from MySqlDriver.setMetadata

  #### Parameters

  * ##### metadata: [MetadataStorage](https://mikro-orm.io/api/core/class/MetadataStorage.md)

  #### Returns void

### [**](#stream)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/AbstractSqlDriver.ts#L1864)inheritedstream

* ****stream**\<T>(entityName, where, options): AsyncIterableIterator\<T, any, any>

* Inherited from MySqlDriver.stream

  #### Parameters

  * ##### entityName: [EntityName](https://mikro-orm.io/api/core.md#EntityName)\<T>

  * ##### where: [FilterQuery](https://mikro-orm.io/api/core.md#FilterQuery)\<T>

  * ##### options: [StreamOptions](https://mikro-orm.io/api/core/interface/StreamOptions.md)\<T, any, any, any>

  #### Returns AsyncIterableIterator\<T, any, any>

### [**](#syncCollections)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/AbstractSqlDriver.ts#L1442)inheritedsyncCollections

* ****syncCollections**\<T, O>(collections, options): Promise\<void>

* Inherited from MySqlDriver.syncCollections

  #### Parameters

  * ##### collections: Iterable<[Collection](https://mikro-orm.io/api/core/class/Collection.md)\<T, O>, any, any>

  * ##### optionaloptions: [DriverMethodOptions](https://mikro-orm.io/api/core/interface/DriverMethodOptions.md)

  #### Returns Promise\<void>
