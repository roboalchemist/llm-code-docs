# Source: https://mikro-orm.io/api/sql/class/AbstractSqlConnection.md

# abstractAbstractSqlConnection<!-- -->

### Hierarchy

* [Connection](https://mikro-orm.io/api/core/class/Connection.md)

  * *AbstractSqlConnection*

    * [BaseSqliteConnection](https://mikro-orm.io/api/sql/class/BaseSqliteConnection.md)
    * [PostgreSqlConnection](https://mikro-orm.io/api/postgresql/class/PostgreSqlConnection.md)
    * [MySqlConnection](https://mikro-orm.io/api/mysql/class/MySqlConnection.md)
    * [MsSqlConnection](https://mikro-orm.io/api/mssql/class/MsSqlConnection.md)
    * [OracleConnection](https://mikro-orm.io/api/oracledb/class/OracleConnection.md)

## Index[**](#index)

### Constructors

* [**constructor](#constructor)

### Methods

* [**begin](#begin)
* [**close](#close)
* [**commit](#commit)
* [**connect](#connect)
* [**createKysely](#createkysely)
* [**createKyselyDialect](#createKyselyDialect)
* [**ensureConnection](#ensureConnection)
* [**execute](#execute)
* [**executeDump](#executedump)
* [**getClient](#getclient)
* [**getConnectionOptions](#getConnectionOptions)
* [**getPlatform](#getPlatform)
* [**checkConnection](#checkconnection)
* [**initClient](#initclient)
* [**isConnected](#isconnected)
* [**rollback](#rollback)
* [**setMetadata](#setMetadata)
* [**setPlatform](#setPlatform)
* [**stream](#stream)
* [**transactional](#transactional)

## Constructors<!-- -->[**](#constructors)

### [**](#constructor)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/connections/Connection.ts#L24)constructor

* ****new AbstractSqlConnection**(config, options, type): [AbstractSqlConnection](https://mikro-orm.io/api/sql/class/AbstractSqlConnection.md)

* Inherited from Connection.constructor

  #### Parameters

  * ##### config: [Configuration](https://mikro-orm.io/api/core/class/Configuration.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>, [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>>>

  * ##### optionaloptions: [ConnectionOptions](https://mikro-orm.io/api/core/interface/ConnectionOptions.md)

  * ##### type: [ConnectionType](https://mikro-orm.io/api/core.md#ConnectionType) = <!-- -->'write'

  #### Returns [AbstractSqlConnection](https://mikro-orm.io/api/sql/class/AbstractSqlConnection.md)

## Methods<!-- -->[**](#methods)

### [**](#begin)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/AbstractSqlConnection.ts#L140)begin

* ****begin**(options): Promise\<ControlledTransaction\<any, any>>

* Overrides Connection.begin

  #### Parameters

  * ##### options: { ctx?<!-- -->: ControlledTransaction\<any, any>; eventBroadcaster?<!-- -->: [TransactionEventBroadcaster](https://mikro-orm.io/api/core/class/TransactionEventBroadcaster.md); isolationLevel?<!-- -->: [IsolationLevel](https://mikro-orm.io/api/core/enum/IsolationLevel.md); loggerContext?<!-- -->: [LogContext](https://mikro-orm.io/api/core/interface/LogContext.md); readOnly?<!-- -->: boolean } = <!-- -->{}

    * ##### optionalctx: ControlledTransaction\<any, any>

    * ##### optionaleventBroadcaster: [TransactionEventBroadcaster](https://mikro-orm.io/api/core/class/TransactionEventBroadcaster.md)

    * ##### optionalisolationLevel: [IsolationLevel](https://mikro-orm.io/api/core/enum/IsolationLevel.md)

    * ##### optionalloggerContext: [LogContext](https://mikro-orm.io/api/core/interface/LogContext.md)

    * ##### optionalreadOnly: boolean

  #### Returns Promise\<ControlledTransaction\<any, any>>

### [**](#close)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/AbstractSqlConnection.ts#L65)close

* ****close**(force): Promise\<void>

* Overrides Connection.close

  Closes the database connection (aka disconnect)

  ***

  #### Parameters

  * ##### optionalforce: boolean

  #### Returns Promise\<void>

### [**](#commit)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/AbstractSqlConnection.ts#L195)commit

* ****commit**(ctx, eventBroadcaster, loggerContext): Promise\<void>

* Overrides Connection.commit

  #### Parameters

  * ##### ctx: ControlledTransaction\<any, any>

  * ##### optionaleventBroadcaster: [TransactionEventBroadcaster](https://mikro-orm.io/api/core/class/TransactionEventBroadcaster.md)

  * ##### optionalloggerContext: [LogContext](https://mikro-orm.io/api/core/interface/LogContext.md)

  #### Returns Promise\<void>

### [**](#connect)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/AbstractSqlConnection.ts#L27)connect

* ****connect**(options): Promise\<void>

* Overrides Connection.connect

  Establishes connection to database

  ***

  #### Parameters

  * ##### optionaloptions: { skipOnConnect?<!-- -->: boolean }

    * ##### optionalskipOnConnect: boolean

  #### Returns Promise\<void>

### [**](#createkysely)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/AbstractSqlConnection.ts#L36)createKysely

* ****createKysely**(): [MaybePromise](https://mikro-orm.io/api/core.md#MaybePromise)\<void>

* #### Returns [MaybePromise](https://mikro-orm.io/api/core.md#MaybePromise)\<void>

### [**](#createKyselyDialect)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/AbstractSqlConnection.ts#L25)abstractcreateKyselyDialect

* ****createKyselyDialect**(overrides): [MaybePromise](https://mikro-orm.io/api/core.md#MaybePromise)\<Dialect>

* #### Parameters

  * ##### overrides: [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)

  #### Returns [MaybePromise](https://mikro-orm.io/api/core.md#MaybePromise)\<Dialect>

### [**](#ensureConnection)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/connections/Connection.ts#L81)inheritedensureConnection

* ****ensureConnection**(): Promise\<void>

* Inherited from Connection.ensureConnection

  Ensure the connection exists, this is used to support lazy connect when using `new MikroORM()` instead of the async `init` method.

  ***

  #### Returns Promise\<void>

### [**](#execute)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/AbstractSqlConnection.ts#L253)execute

* ****execute**\<T>(query, params, method, ctx, loggerContext): Promise\<T>

* Overrides Connection.execute

  #### Parameters

  * ##### query: string | [RawQueryFragment](https://mikro-orm.io/api/core/class/RawQueryFragment.md)\<string> | NativeQueryBuilder

  * ##### params: readonly<!-- --> unknown\[] = <!-- -->\[]

  * ##### method: get | all | run = <!-- -->'all'

  * ##### optionalctx: any

  * ##### optionalloggerContext: [LoggingOptions](https://mikro-orm.io/api/core.md#LoggingOptions)

  #### Returns Promise\<T>

### [**](#executedump)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/AbstractSqlConnection.ts#L316)executeDump

* ****executeDump**(dump): Promise\<void>

* Overrides Connection.executeDump

  Execute raw SQL queries, handy from running schema dump loaded from a file. This method doesn't support transactions, as opposed to `orm.schema.execute()`, which is used internally.

  ***

  #### Parameters

  * ##### dump: string

  #### Returns Promise\<void>

### [**](#getclient)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/AbstractSqlConnection.ts#L96)getClient

* ****getClient**\<T>(): [Kysely](https://mikro-orm.io/api/sql/class/Kysely.md)\<T>

* #### Returns [Kysely](https://mikro-orm.io/api/sql/class/Kysely.md)\<T>

### [**](#getConnectionOptions)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/connections/Connection.ts#L156)inheritedgetConnectionOptions

* ****getConnectionOptions**(): [ConnectionConfig](https://mikro-orm.io/api/core/interface/ConnectionConfig.md)

* Inherited from Connection.getConnectionOptions

  #### Returns [ConnectionConfig](https://mikro-orm.io/api/core/interface/ConnectionConfig.md)

### [**](#getPlatform)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/connections/Connection.ts#L193)inheritedgetPlatform

* ****getPlatform**(): [Platform](https://mikro-orm.io/api/core/class/Platform.md)

* Inherited from Connection.getPlatform

  #### Returns [Platform](https://mikro-orm.io/api/core/class/Platform.md)

### [**](#checkconnection)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/AbstractSqlConnection.ts#L83)checkConnection

* ****checkConnection**(): Promise<{ ok: true } | { error?
  <!-- -->
  : Error; ok: false; reason: string }>

* Overrides Connection.checkConnection

  Are we connected to the database

  ***

  #### Returns Promise<{ ok: true } | { error?<!-- -->: Error; ok: false; reason: string }>

### [**](#initclient)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/AbstractSqlConnection.ts#L111)initClient

* ****initClient**(): Promise\<void>

* #### Returns Promise\<void>

### [**](#isconnected)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/AbstractSqlConnection.ts#L75)isConnected

* ****isConnected**(): Promise\<boolean>

* Overrides Connection.isConnected

  Are we connected to the database

  ***

  #### Returns Promise\<boolean>

### [**](#rollback)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/AbstractSqlConnection.ts#L217)rollback

* ****rollback**(ctx, eventBroadcaster, loggerContext): Promise\<void>

* Overrides Connection.rollback

  #### Parameters

  * ##### ctx: ControlledTransaction\<any, any>

  * ##### optionaleventBroadcaster: [TransactionEventBroadcaster](https://mikro-orm.io/api/core/class/TransactionEventBroadcaster.md)

  * ##### optionalloggerContext: [LogContext](https://mikro-orm.io/api/core/interface/LogContext.md)

  #### Returns Promise\<void>

### [**](#setMetadata)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/connections/Connection.ts#L185)inheritedsetMetadata

* ****setMetadata**(metadata): void

* Inherited from Connection.setMetadata

  #### Parameters

  * ##### metadata: [MetadataStorage](https://mikro-orm.io/api/core/class/MetadataStorage.md)

  #### Returns void

### [**](#setPlatform)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/connections/Connection.ts#L189)inheritedsetPlatform

* ****setPlatform**(platform): void

* Inherited from Connection.setPlatform

  #### Parameters

  * ##### platform: [Platform](https://mikro-orm.io/api/core/class/Platform.md)

  #### Returns void

### [**](#stream)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/AbstractSqlConnection.ts#L275)stream

* ****stream**\<T>(query, params, ctx, loggerContext): AsyncIterableIterator\<T, any, any>

* #### Parameters

  * ##### query: string | [RawQueryFragment](https://mikro-orm.io/api/core/class/RawQueryFragment.md)\<string> | NativeQueryBuilder

  * ##### params: readonly<!-- --> unknown\[] = <!-- -->\[]

  * ##### optionalctx: [Kysely](https://mikro-orm.io/api/sql/class/Kysely.md)\<any>

  * ##### optionalloggerContext: [LoggingOptions](https://mikro-orm.io/api/core.md#LoggingOptions)

  #### Returns AsyncIterableIterator\<T, any, any>

### [**](#transactional)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/AbstractSqlConnection.ts#L117)transactional

* ****transactional**\<T>(cb, options): Promise\<T>

* Overrides Connection.transactional

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
