# Source: https://mikro-orm.io/api/core/class/DatabaseDriver.md

# abstractDatabaseDriver<!-- --> \<C>

### Hierarchy

* *DatabaseDriver*

  * [AbstractSqlDriver](https://mikro-orm.io/api/knex/class/AbstractSqlDriver.md)
  * [MongoDriver](https://mikro-orm.io/api/mongodb/class/MongoDriver.md)

### Implements

* [IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)\<C>

## Index[**](#Index)

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

## Properties<!-- -->[**](#Properties)

### [**](#\[EntityManagerType])[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/DatabaseDriver.ts#L42)\[EntityManagerType]

**\[EntityManagerType]: [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[DatabaseDriver](https://mikro-orm.io/api/core/class/DatabaseDriver.md)\<C>>

Implementation of IDatabaseDriver.\[EntityManagerType]

### [**](#config)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/DatabaseDriver.ts#L51)readonlyconfig

**config: [Configuration](https://mikro-orm.io/api/core/class/Configuration.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>, [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>>>

Implementation of IDatabaseDriver.config

## Methods<!-- -->[**](#Methods)

### [**](#aggregate)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/DatabaseDriver.ts#L89)aggregate

* ****aggregate**(entityName, pipeline): Promise\<any\[]>

- Implementation of IDatabaseDriver.aggregate

  #### Parameters

  * ##### entityName: string
  * ##### pipeline: any\[]

  #### Returns Promise\<any\[]>

### [**](#close)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/DatabaseDriver.ts#L148)close

* ****close**(force): Promise\<void>

- Implementation of IDatabaseDriver.close

  #### Parameters

  * ##### optionalforce: boolean

  #### Returns Promise\<void>

### [**](#connect)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/DatabaseDriver.ts#L124)connect

* ****connect**(): Promise\<C>

- Implementation of IDatabaseDriver.connect

  #### Returns Promise\<C>

### [**](#convertException)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/DatabaseDriver.ts#L470)convertException

* ****convertException**(exception): [DriverException](https://mikro-orm.io/api/core/class/DriverException.md)

- Implementation of IDatabaseDriver.convertException

  Converts native db errors to standardized driver exceptions

  ***

  #### Parameters

  * ##### exception: Error

  #### Returns [DriverException](https://mikro-orm.io/api/core/class/DriverException.md)

### [**](#count)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/DatabaseDriver.ts#L72)abstractcount

* ****count**\<T, P>(entityName, where, options): Promise\<number>

- Implementation of IDatabaseDriver.count

  #### Parameters

  * ##### entityName: string
  * ##### where: [FilterQuery](https://mikro-orm.io/api/core.md#FilterQuery)\<T>
  * ##### optionaloptions: [CountOptions](https://mikro-orm.io/api/core/interface/CountOptions.md)\<T, P>

  #### Returns Promise\<number>

### [**](#countVirtual)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/DatabaseDriver.ts#L85)countVirtual

* ****countVirtual**\<T>(entityName, where, options): Promise\<number>

- #### Parameters

  * ##### entityName: string
  * ##### where: [FilterQuery](https://mikro-orm.io/api/core.md#FilterQuery)\<T>
  * ##### options: [CountOptions](https://mikro-orm.io/api/core/interface/CountOptions.md)\<T, any>

  #### Returns Promise\<number>

### [**](#createEntityManager)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/DatabaseDriver.ts#L74)createEntityManager

* ****createEntityManager**\<D>(useContext): D\[typeof [EntityManagerType](https://mikro-orm.io/api/core.md#EntityManagerType)]

- Implementation of IDatabaseDriver.createEntityManager

  #### Parameters

  * ##### optionaluseContext: boolean

  #### Returns D\[typeof [EntityManagerType](https://mikro-orm.io/api/core.md#EntityManagerType)]

### [**](#find)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/DatabaseDriver.ts#L56)abstractfind

* ****find**\<T, P, F, E>(entityName, where, options): Promise<[EntityData](https://mikro-orm.io/api/core.md#EntityData)\<T>\[]>

- Implementation of IDatabaseDriver.find

  Finds selection of entities

  ***

  #### Parameters

  * ##### entityName: string
  * ##### where: [FilterQuery](https://mikro-orm.io/api/core.md#FilterQuery)\<T>
  * ##### optionaloptions: [FindOptions](https://mikro-orm.io/api/core/interface/FindOptions.md)\<T, P, F, E>

  #### Returns Promise<[EntityData](https://mikro-orm.io/api/core.md#EntityData)\<T>\[]>

### [**](#findOne)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/DatabaseDriver.ts#L58)abstractfindOne

* ****findOne**\<T, P, F, E>(entityName, where, options): Promise\<null | [EntityData](https://mikro-orm.io/api/core.md#EntityData)\<T>>

- Implementation of IDatabaseDriver.findOne

  Finds single entity (table row, document)

  ***

  #### Parameters

  * ##### entityName: string
  * ##### where: [FilterQuery](https://mikro-orm.io/api/core.md#FilterQuery)\<T>
  * ##### optionaloptions: [FindOneOptions](https://mikro-orm.io/api/core/interface/FindOneOptions.md)\<T, P, F, E>

  #### Returns Promise\<null | [EntityData](https://mikro-orm.io/api/core.md#EntityData)\<T>>

### [**](#findVirtual)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/DatabaseDriver.ts#L80)findVirtual

* ****findVirtual**\<T>(entityName, where, options): Promise<[EntityData](https://mikro-orm.io/api/core.md#EntityData)\<T>\[]>

- Implementation of IDatabaseDriver.findVirtual

  #### Parameters

  * ##### entityName: string
  * ##### where: [FilterQuery](https://mikro-orm.io/api/core.md#FilterQuery)\<T>
  * ##### options: [FindOptions](https://mikro-orm.io/api/core/interface/FindOptions.md)\<T, any, any, any>

  #### Returns Promise<[EntityData](https://mikro-orm.io/api/core.md#EntityData)\<T>\[]>

### [**](#getConnection)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/DatabaseDriver.ts#L138)getConnection

* ****getConnection**(type): C

- Implementation of IDatabaseDriver.getConnection

  #### Parameters

  * ##### type: [ConnectionType](https://mikro-orm.io/api/core.md#ConnectionType) = <!-- -->'write'

  #### Returns C

### [**](#getDependencies)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/DatabaseDriver.ts#L172)getDependencies

* ****getDependencies**(): string\[]

- Implementation of IDatabaseDriver.getDependencies

  Returns name of the underlying database dependencies (e.g. `mongodb` or `mysql2`) for SQL drivers it also returns `knex` in the array as connectors are not used directly there

  ***

  #### Returns string\[]

### [**](#getMetadata)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/DatabaseDriver.ts#L168)getMetadata

* ****getMetadata**(): [MetadataStorage](https://mikro-orm.io/api/core/class/MetadataStorage.md)

- Implementation of IDatabaseDriver.getMetadata

  #### Returns [MetadataStorage](https://mikro-orm.io/api/core/class/MetadataStorage.md)

### [**](#getPlatform)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/DatabaseDriver.ts#L153)getPlatform

* ****getPlatform**(): [Platform](https://mikro-orm.io/api/core/class/Platform.md)

- Implementation of IDatabaseDriver.getPlatform

  #### Returns [Platform](https://mikro-orm.io/api/core/class/Platform.md)

### [**](#loadFromPivotTable)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/DatabaseDriver.ts#L93)loadFromPivotTable

* ****loadFromPivotTable**\<T, O>(prop, owners, where, orderBy, ctx, options, pivotJoin): Promise<[Dictionary](https://mikro-orm.io/api/core.md#Dictionary)\<T\[]>>

- Implementation of IDatabaseDriver.loadFromPivotTable

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

### [**](#lockPessimistic)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/DatabaseDriver.ts#L463)lockPessimistic

* ****lockPessimistic**\<T>(entity, options): Promise\<void>

- Implementation of IDatabaseDriver.lockPessimistic

  #### Parameters

  * ##### entity: T
  * ##### options: [LockOptions](https://mikro-orm.io/api/core/interface/LockOptions.md)

  #### Returns Promise\<void>

### [**](#mapResult)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/DatabaseDriver.ts#L116)mapResult

* ****mapResult**\<T>(result, meta, populate): null | [EntityData](https://mikro-orm.io/api/core.md#EntityData)\<T>

- Implementation of IDatabaseDriver.mapResult

  #### Parameters

  * ##### result: [EntityDictionary](https://mikro-orm.io/api/core.md#EntityDictionary)\<T>
  * ##### optionalmeta: [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<T>
  * ##### populate: [PopulateOptions](https://mikro-orm.io/api/core.md#PopulateOptions)\<T>\[] = <!-- -->\[]

  #### Returns null | [EntityData](https://mikro-orm.io/api/core.md#EntityData)\<T>

### [**](#nativeDelete)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/DatabaseDriver.ts#L70)abstractnativeDelete

* ****nativeDelete**\<T>(entityName, where, options): Promise<[QueryResult](https://mikro-orm.io/api/core/interface/QueryResult.md)\<T>>

- Implementation of IDatabaseDriver.nativeDelete

  #### Parameters

  * ##### entityName: string
  * ##### where: [FilterQuery](https://mikro-orm.io/api/core.md#FilterQuery)\<T>
  * ##### optionaloptions: [DeleteOptions](https://mikro-orm.io/api/core/interface/DeleteOptions.md)\<T>

  #### Returns Promise<[QueryResult](https://mikro-orm.io/api/core/interface/QueryResult.md)\<T>>

### [**](#nativeInsert)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/DatabaseDriver.ts#L60)abstractnativeInsert

* ****nativeInsert**\<T>(entityName, data, options): Promise<[QueryResult](https://mikro-orm.io/api/core/interface/QueryResult.md)\<T>>

- Implementation of IDatabaseDriver.nativeInsert

  #### Parameters

  * ##### entityName: string
  * ##### data: [EntityDictionary](https://mikro-orm.io/api/core.md#EntityDictionary)\<T>
  * ##### optionaloptions: [NativeInsertUpdateOptions](https://mikro-orm.io/api/core/interface/NativeInsertUpdateOptions.md)\<T>

  #### Returns Promise<[QueryResult](https://mikro-orm.io/api/core/interface/QueryResult.md)\<T>>

### [**](#nativeInsertMany)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/DatabaseDriver.ts#L62)abstractnativeInsertMany

* ****nativeInsertMany**\<T>(entityName, data, options, transform): Promise<[QueryResult](https://mikro-orm.io/api/core/interface/QueryResult.md)\<T>>

- Implementation of IDatabaseDriver.nativeInsertMany

  #### Parameters

  * ##### entityName: string
  * ##### data: [EntityDictionary](https://mikro-orm.io/api/core.md#EntityDictionary)\<T>\[]
  * ##### optionaloptions: [NativeInsertUpdateManyOptions](https://mikro-orm.io/api/core/interface/NativeInsertUpdateManyOptions.md)\<T>
  * ##### optionaltransform: (sql) => string


  #### Returns Promise<[QueryResult](https://mikro-orm.io/api/core/interface/QueryResult.md)\<T>>

### [**](#nativeUpdate)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/DatabaseDriver.ts#L64)abstractnativeUpdate

* ****nativeUpdate**\<T>(entityName, where, data, options): Promise<[QueryResult](https://mikro-orm.io/api/core/interface/QueryResult.md)\<T>>

- Implementation of IDatabaseDriver.nativeUpdate

  #### Parameters

  * ##### entityName: string
  * ##### where: [FilterQuery](https://mikro-orm.io/api/core.md#FilterQuery)\<T>
  * ##### data: [EntityDictionary](https://mikro-orm.io/api/core.md#EntityDictionary)\<T>
  * ##### optionaloptions: [NativeInsertUpdateOptions](https://mikro-orm.io/api/core/interface/NativeInsertUpdateOptions.md)\<T>

  #### Returns Promise<[QueryResult](https://mikro-orm.io/api/core/interface/QueryResult.md)\<T>>

### [**](#nativeUpdateMany)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/DatabaseDriver.ts#L66)nativeUpdateMany

* ****nativeUpdateMany**\<T>(entityName, where, data, options): Promise<[QueryResult](https://mikro-orm.io/api/core/interface/QueryResult.md)\<T>>

- Implementation of IDatabaseDriver.nativeUpdateMany

  #### Parameters

  * ##### entityName: string
  * ##### where: [FilterQuery](https://mikro-orm.io/api/core.md#FilterQuery)\<T>\[]
  * ##### data: [EntityDictionary](https://mikro-orm.io/api/core.md#EntityDictionary)\<T>\[]
  * ##### optionaloptions: [NativeInsertUpdateManyOptions](https://mikro-orm.io/api/core/interface/NativeInsertUpdateManyOptions.md)\<T>

  #### Returns Promise<[QueryResult](https://mikro-orm.io/api/core/interface/QueryResult.md)\<T>>

### [**](#reconnect)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/DatabaseDriver.ts#L131)reconnect

* ****reconnect**(): Promise\<C>

- Implementation of IDatabaseDriver.reconnect

  #### Returns Promise\<C>

### [**](#setMetadata)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/DatabaseDriver.ts#L157)setMetadata

* ****setMetadata**(metadata): void

- Implementation of IDatabaseDriver.setMetadata

  #### Parameters

  * ##### metadata: [MetadataStorage](https://mikro-orm.io/api/core/class/MetadataStorage.md)

  #### Returns void

### [**](#syncCollections)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/DatabaseDriver.ts#L97)syncCollections

* ****syncCollections**\<T, O>(collections, options): Promise\<void>

- Implementation of IDatabaseDriver.syncCollections

  #### Parameters

  * ##### collections: Iterable<[Collection](https://mikro-orm.io/api/core/class/Collection.md)\<T, O>, any, any>
  * ##### optionaloptions: [DriverMethodOptions](https://mikro-orm.io/api/core/interface/DriverMethodOptions.md)

  #### Returns Promise\<void>
