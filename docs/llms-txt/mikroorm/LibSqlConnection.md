# Source: https://mikro-orm.io/api/libsql/class/LibSqlConnection.md

# LibSqlConnection<!-- -->

### Hierarchy

* [BaseSqliteConnection](https://mikro-orm.io/api/sql/class/BaseSqliteConnection.md)
  * *LibSqlConnection*

## Index[**](#index)

### Constructors

* [**constructor](#constructor)

### Methods

* [**begin](#begin)
* [**close](#close)
* [**commit](#commit)
* [**connect](#connect)
* [**createKysely](#createKysely)
* [**createKyselyDialect](#createkyselydialect)
* [**ensureConnection](#ensureConnection)
* [**execute](#execute)
* [**executeDump](#executedump)
* [**getClient](#getClient)
* [**getConnectionOptions](#getConnectionOptions)
* [**getPlatform](#getPlatform)
* [**checkConnection](#checkConnection)
* [**initClient](#initClient)
* [**isConnected](#isConnected)
* [**rollback](#rollback)
* [**setMetadata](#setMetadata)
* [**setPlatform](#setPlatform)
* [**stream](#stream)
* [**transactional](#transactional)

## Constructors<!-- -->[**](#constructors)

### [**](#constructor)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/connections/Connection.ts#L24)constructor

* ****new LibSqlConnection**(config, options, type): [LibSqlConnection](https://mikro-orm.io/api/libsql/class/LibSqlConnection.md)

* Inherited from BaseSqliteConnection.constructor

  #### Parameters

  * ##### config: [Configuration](https://mikro-orm.io/api/core/class/Configuration.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>, [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>>>

  * ##### optionaloptions: [ConnectionOptions](https://mikro-orm.io/api/core/interface/ConnectionOptions.md)

  * ##### type: [ConnectionType](https://mikro-orm.io/api/core.md#ConnectionType) = <!-- -->'write'

  #### Returns [LibSqlConnection](https://mikro-orm.io/api/libsql/class/LibSqlConnection.md)

## Methods<!-- -->[**](#methods)

### [**](#begin)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/AbstractSqlConnection.ts#L140)inheritedbegin

* ****begin**(options): Promise\<ControlledTransaction\<any, any>>

* Inherited from BaseSqliteConnection.begin

  #### Parameters

  * ##### options: { ctx?<!-- -->: ControlledTransaction\<any, any>; eventBroadcaster?<!-- -->: [TransactionEventBroadcaster](https://mikro-orm.io/api/core/class/TransactionEventBroadcaster.md); isolationLevel?<!-- -->: [IsolationLevel](https://mikro-orm.io/api/core/enum/IsolationLevel.md); loggerContext?<!-- -->: [LogContext](https://mikro-orm.io/api/core/interface/LogContext.md); readOnly?<!-- -->: boolean } = <!-- -->{}

    * ##### optionalctx: ControlledTransaction\<any, any>

    * ##### optionaleventBroadcaster: [TransactionEventBroadcaster](https://mikro-orm.io/api/core/class/TransactionEventBroadcaster.md)

    * ##### optionalisolationLevel: [IsolationLevel](https://mikro-orm.io/api/core/enum/IsolationLevel.md)

    * ##### optionalloggerContext: [LogContext](https://mikro-orm.io/api/core/interface/LogContext.md)

    * ##### optionalreadOnly: boolean

  #### Returns Promise\<ControlledTransaction\<any, any>>

### [**](#close)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/AbstractSqlConnection.ts#L65)inheritedclose

* ****close**(force): Promise\<void>

* Inherited from BaseSqliteConnection.close

  Closes the database connection (aka disconnect)

  ***

  #### Parameters

  * ##### optionalforce: boolean

  #### Returns Promise\<void>

### [**](#commit)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/AbstractSqlConnection.ts#L195)inheritedcommit

* ****commit**(ctx, eventBroadcaster, loggerContext): Promise\<void>

* Inherited from BaseSqliteConnection.commit

  #### Parameters

  * ##### ctx: ControlledTransaction\<any, any>

  * ##### optionaleventBroadcaster: [TransactionEventBroadcaster](https://mikro-orm.io/api/core/class/TransactionEventBroadcaster.md)

  * ##### optionalloggerContext: [LogContext](https://mikro-orm.io/api/core/interface/LogContext.md)

  #### Returns Promise\<void>

### [**](#connect)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/libsql/src/LibSqlConnection.ts#L8)connect

* ****connect**(options): Promise\<void>

* Overrides BaseSqliteConnection.connect

  Establishes connection to database

  ***

  #### Parameters

  * ##### optionaloptions: { skipOnConnect?<!-- -->: boolean }

    * ##### optionalskipOnConnect: boolean

  #### Returns Promise\<void>

### [**](#createKysely)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/AbstractSqlConnection.ts#L36)inheritedcreateKysely

* ****createKysely**(): [MaybePromise](https://mikro-orm.io/api/core.md#MaybePromise)\<void>

* Inherited from BaseSqliteConnection.createKysely

  #### Returns [MaybePromise](https://mikro-orm.io/api/core.md#MaybePromise)\<void>

### [**](#createkyselydialect)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/libsql/src/LibSqlConnection.ts#L13)createKyselyDialect

* ****createKyselyDialect**(options): LibSqlDialect

* Overrides BaseSqliteConnection.createKyselyDialect

  #### Parameters

  * ##### options: [Dictionary](https://mikro-orm.io/api/core.md#Dictionary) & Options

  #### Returns LibSqlDialect

### [**](#ensureConnection)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/connections/Connection.ts#L81)inheritedensureConnection

* ****ensureConnection**(): Promise\<void>

* Inherited from BaseSqliteConnection.ensureConnection

  Ensure the connection exists, this is used to support lazy connect when using `new MikroORM()` instead of the async `init` method.

  ***

  #### Returns Promise\<void>

### [**](#execute)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/AbstractSqlConnection.ts#L253)inheritedexecute

* ****execute**\<T>(query, params, method, ctx, loggerContext): Promise\<T>

* Inherited from BaseSqliteConnection.execute

  #### Parameters

  * ##### query: string | [RawQueryFragment](https://mikro-orm.io/api/core/class/RawQueryFragment.md)\<string> | NativeQueryBuilder

  * ##### params: readonly<!-- --> unknown\[] = <!-- -->\[]

  * ##### method: get | all | run = <!-- -->'all'

  * ##### optionalctx: any

  * ##### optionalloggerContext: [LoggingOptions](https://mikro-orm.io/api/core.md#LoggingOptions)

  #### Returns Promise\<T>

### [**](#executedump)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/libsql/src/LibSqlConnection.ts#L25)executeDump

* ****executeDump**(source): Promise\<void>

* Overrides BaseSqliteConnection.executeDump

  Execute raw SQL queries, handy from running schema dump loaded from a file. This method doesn't support transactions, as opposed to `orm.schema.execute()`, which is used internally.

  ***

  #### Parameters

  * ##### source: string

  #### Returns Promise\<void>

### [**](#getClient)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/AbstractSqlConnection.ts#L96)inheritedgetClient

* ****getClient**\<T>(): [Kysely](https://mikro-orm.io/api/sql/class/Kysely.md)\<T>

* Inherited from BaseSqliteConnection.getClient

  #### Returns [Kysely](https://mikro-orm.io/api/sql/class/Kysely.md)\<T>

### [**](#getConnectionOptions)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/connections/Connection.ts#L156)inheritedgetConnectionOptions

* ****getConnectionOptions**(): [ConnectionConfig](https://mikro-orm.io/api/core/interface/ConnectionConfig.md)

* Inherited from BaseSqliteConnection.getConnectionOptions

  #### Returns [ConnectionConfig](https://mikro-orm.io/api/core/interface/ConnectionConfig.md)

### [**](#getPlatform)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/connections/Connection.ts#L193)inheritedgetPlatform

* ****getPlatform**(): [Platform](https://mikro-orm.io/api/core/class/Platform.md)

* Inherited from BaseSqliteConnection.getPlatform

  #### Returns [Platform](https://mikro-orm.io/api/core/class/Platform.md)

### [**](#checkConnection)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/AbstractSqlConnection.ts#L83)inheritedcheckConnection

* ****checkConnection**(): Promise<{ ok: true } | { error?
  <!-- -->
  : Error; ok: false; reason: string }>

* Inherited from BaseSqliteConnection.checkConnection

  Are we connected to the database

  ***

  #### Returns Promise<{ ok: true } | { error?<!-- -->: Error; ok: false; reason: string }>

### [**](#initClient)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/AbstractSqlConnection.ts#L111)inheritedinitClient

* ****initClient**(): Promise\<void>

* Inherited from BaseSqliteConnection.initClient

  #### Returns Promise\<void>

### [**](#isConnected)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/AbstractSqlConnection.ts#L75)inheritedisConnected

* ****isConnected**(): Promise\<boolean>

* Inherited from BaseSqliteConnection.isConnected

  Are we connected to the database

  ***

  #### Returns Promise\<boolean>

### [**](#rollback)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/AbstractSqlConnection.ts#L217)inheritedrollback

* ****rollback**(ctx, eventBroadcaster, loggerContext): Promise\<void>

* Inherited from BaseSqliteConnection.rollback

  #### Parameters

  * ##### ctx: ControlledTransaction\<any, any>

  * ##### optionaleventBroadcaster: [TransactionEventBroadcaster](https://mikro-orm.io/api/core/class/TransactionEventBroadcaster.md)

  * ##### optionalloggerContext: [LogContext](https://mikro-orm.io/api/core/interface/LogContext.md)

  #### Returns Promise\<void>

### [**](#setMetadata)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/connections/Connection.ts#L185)inheritedsetMetadata

* ****setMetadata**(metadata): void

* Inherited from BaseSqliteConnection.setMetadata

  #### Parameters

  * ##### metadata: [MetadataStorage](https://mikro-orm.io/api/core/class/MetadataStorage.md)

  #### Returns void

### [**](#setPlatform)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/connections/Connection.ts#L189)inheritedsetPlatform

* ****setPlatform**(platform): void

* Inherited from BaseSqliteConnection.setPlatform

  #### Parameters

  * ##### platform: [Platform](https://mikro-orm.io/api/core/class/Platform.md)

  #### Returns void

### [**](#stream)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/AbstractSqlConnection.ts#L275)inheritedstream

* ****stream**\<T>(query, params, ctx, loggerContext): AsyncIterableIterator\<T, any, any>

* Inherited from BaseSqliteConnection.stream

  #### Parameters

  * ##### query: string | [RawQueryFragment](https://mikro-orm.io/api/core/class/RawQueryFragment.md)\<string> | NativeQueryBuilder

  * ##### params: readonly<!-- --> unknown\[] = <!-- -->\[]

  * ##### optionalctx: [Kysely](https://mikro-orm.io/api/sql/class/Kysely.md)\<any>

  * ##### optionalloggerContext: [LoggingOptions](https://mikro-orm.io/api/core.md#LoggingOptions)

  #### Returns AsyncIterableIterator\<T, any, any>

### [**](#transactional)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/AbstractSqlConnection.ts#L117)inheritedtransactional

* ****transactional**\<T>(cb, options): Promise\<T>

* Inherited from BaseSqliteConnection.transactional

  #### Parameters

  * ##### cb: (trx) => Promise\<T>

  *

    ##### options: { ctx?<!-- -->: ControlledTransaction\<any, \[]>; eventBroadcaster?<!-- -->: [TransactionEventBroadcaster](https://mikro-orm.io/api/core/class/TransactionEventBroadcaster.md); isolationLevel?<!-- -->: [IsolationLevel](https://mikro-orm.io/api/core/enum/IsolationLevel.md); loggerContext?<!-- -->: [LogContext](https://mikro-orm.io/api/core/interface/LogContext.md); readOnly?<!-- -->: boolean } = <!-- -->{}

    * ##### optionalctx: ControlledTransaction\<any, \[]>

    * ##### optionaleventBroadcaster: [TransactionEventBroadcaster](https://mikro-orm.io/api/core/class/TransactionEventBroadcaster.md)

    * ##### optionalisolationLevel: [IsolationLevel](https://mikro-orm.io/api/core/enum/IsolationLevel.md)

    * ##### optionalloggerContext: [LogContext](https://mikro-orm.io/api/core/interface/LogContext.md)

    * ##### optionalreadOnly: boolean

  #### Returns Promise\<T>
