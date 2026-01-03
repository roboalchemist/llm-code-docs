# Source: https://mikro-orm.io/api/core/class/Connection.md

# abstractConnection<!-- -->

### Hierarchy

* *Connection*

  * [AbstractSqlConnection](https://mikro-orm.io/api/knex/class/AbstractSqlConnection.md)
  * [MongoConnection](https://mikro-orm.io/api/mongodb/class/MongoConnection.md)

## Index[**](#Index)

### Constructors

* [**constructor](#constructor)

### Methods

* [**begin](#begin)
* [**checkConnection](#checkConnection)
* [**close](#close)
* [**commit](#commit)
* [**connect](#connect)
* [**ensureConnection](#ensureConnection)
* [**execute](#execute)
* [**getClientUrl](#getClientUrl)
* [**getConnectionOptions](#getConnectionOptions)
* [**getDefaultClientUrl](#getDefaultClientUrl)
* [**getPlatform](#getPlatform)
* [**isConnected](#isConnected)
* [**rollback](#rollback)
* [**setMetadata](#setMetadata)
* [**setPlatform](#setPlatform)
* [**transactional](#transactional)

## Constructors<!-- -->[**](#Constructors)

### [**](#constructor)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/connections/Connection.ts#L18)constructor

* ****new Connection**(config, options, type): [Connection](https://mikro-orm.io/api/core/class/Connection.md)

- #### Parameters

  * ##### config: [Configuration](https://mikro-orm.io/api/core/class/Configuration.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>, [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>>>
  * ##### optionaloptions: [ConnectionOptions](https://mikro-orm.io/api/core/interface/ConnectionOptions.md)
  * ##### type: [ConnectionType](https://mikro-orm.io/api/core.md#ConnectionType) = <!-- -->'write'

  #### Returns [Connection](https://mikro-orm.io/api/core/class/Connection.md)

## Methods<!-- -->[**](#Methods)

### [**](#begin)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/connections/Connection.ts#L77)begin

* ****begin**(options): Promise\<any>

- #### Parameters

  * ##### optionaloptions: { ctx?<!-- -->: any; eventBroadcaster?<!-- -->: [TransactionEventBroadcaster](https://mikro-orm.io/api/core/class/TransactionEventBroadcaster.md); isolationLevel?<!-- -->: [IsolationLevel](https://mikro-orm.io/api/core/enum/IsolationLevel.md); loggerContext?<!-- -->: [LogContext](https://mikro-orm.io/api/core/interface/LogContext.md); readOnly?<!-- -->: boolean }
    * ##### optionalctx: any
    * ##### optionaleventBroadcaster: [TransactionEventBroadcaster](https://mikro-orm.io/api/core/class/TransactionEventBroadcaster.md)
    * ##### optionalisolationLevel: [IsolationLevel](https://mikro-orm.io/api/core/enum/IsolationLevel.md)
    * ##### optionalloggerContext: [LogContext](https://mikro-orm.io/api/core/interface/LogContext.md)
    * ##### optionalreadOnly: boolean

  #### Returns Promise\<any>

### [**](#checkConnection)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/connections/Connection.ts#L48)abstractcheckConnection

* ****checkConnection**(): Promise<{ ok: true } | { error?
  <!-- -->
  : Error; ok: false; reason: string }>

- Are we connected to the database

  ***

  #### Returns Promise<{ ok: true } | { error?<!-- -->: Error; ok: false; reason: string }>

### [**](#close)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/connections/Connection.ts#L53)close

* ****close**(force): Promise\<void>

- Closes the database connection (aka disconnect)

  ***

  #### Parameters

  * ##### optionalforce: boolean

  #### Returns Promise\<void>

### [**](#commit)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/connections/Connection.ts#L81)commit

* ****commit**(ctx, eventBroadcaster, loggerContext): Promise\<void>

- #### Parameters

  * ##### ctx: any
  * ##### optionaleventBroadcaster: [TransactionEventBroadcaster](https://mikro-orm.io/api/core/class/TransactionEventBroadcaster.md)
  * ##### optionalloggerContext: [LogContext](https://mikro-orm.io/api/core/interface/LogContext.md)

  #### Returns Promise\<void>

### [**](#connect)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/connections/Connection.ts#L38)abstractconnect

* ****connect**(): void | Promise\<void>

- Establishes connection to database

  ***

  #### Returns void | Promise\<void>

### [**](#ensureConnection)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/connections/Connection.ts#L62)ensureConnection

* ****ensureConnection**(): Promise\<void>

- Ensure the connection exists, this is used to support lazy connect when using `MikroORM.initSync()`

  ***

  #### Returns Promise\<void>

### [**](#execute)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/connections/Connection.ts#L89)abstractexecute

* ****execute**\<T>(query, params, method, ctx): Promise\<any>

- #### Parameters

  * ##### query: string
  * ##### optionalparams: any\[]
  * ##### optionalmethod: get | all | run
  * ##### optionalctx: any

  #### Returns Promise\<any>

### [**](#getClientUrl)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/connections/Connection.ts#L118)getClientUrl

* ****getClientUrl**(): string

- #### Returns string

### [**](#getConnectionOptions)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/connections/Connection.ts#L91)getConnectionOptions

* ****getConnectionOptions**(): [ConnectionConfig](https://mikro-orm.io/api/core/interface/ConnectionConfig.md)

- #### Returns [ConnectionConfig](https://mikro-orm.io/api/core/interface/ConnectionConfig.md)

### [**](#getDefaultClientUrl)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/connections/Connection.ts#L71)abstractgetDefaultClientUrl

* ****getDefaultClientUrl**(): string

- Returns default client url for given driver (e.g. mongodb://127.0.0.1:27017 for mongodb)

  ***

  #### Returns string

### [**](#getPlatform)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/connections/Connection.ts#L137)getPlatform

* ****getPlatform**(): [Platform](https://mikro-orm.io/api/core/class/Platform.md)

- #### Returns [Platform](https://mikro-orm.io/api/core/class/Platform.md)

### [**](#isConnected)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/connections/Connection.ts#L43)abstractisConnected

* ****isConnected**(): Promise\<boolean>

- Are we connected to the database

  ***

  #### Returns Promise\<boolean>

### [**](#rollback)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/connections/Connection.ts#L85)rollback

* ****rollback**(ctx, eventBroadcaster, loggerContext): Promise\<void>

- #### Parameters

  * ##### ctx: any
  * ##### optionaleventBroadcaster: [TransactionEventBroadcaster](https://mikro-orm.io/api/core/class/TransactionEventBroadcaster.md)
  * ##### optionalloggerContext: [LogContext](https://mikro-orm.io/api/core/interface/LogContext.md)

  #### Returns Promise\<void>

### [**](#setMetadata)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/connections/Connection.ts#L129)setMetadata

* ****setMetadata**(metadata): void

- #### Parameters

  * ##### metadata: [MetadataStorage](https://mikro-orm.io/api/core/class/MetadataStorage.md)

  #### Returns void

### [**](#setPlatform)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/connections/Connection.ts#L133)setPlatform

* ****setPlatform**(platform): void

- #### Parameters

  * ##### platform: [Platform](https://mikro-orm.io/api/core/class/Platform.md)

  #### Returns void

### [**](#transactional)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/connections/Connection.ts#L73)transactional

* ****transactional**\<T>(cb, options): Promise\<T>

- #### Parameters

  * ##### cb: (trx) => Promise\<T>
  *
    ##### optionaloptions: { ctx?<!-- -->: any; eventBroadcaster?<!-- -->: [TransactionEventBroadcaster](https://mikro-orm.io/api/core/class/TransactionEventBroadcaster.md); isolationLevel?<!-- -->: [IsolationLevel](https://mikro-orm.io/api/core/enum/IsolationLevel.md); loggerContext?<!-- -->: [LogContext](https://mikro-orm.io/api/core/interface/LogContext.md); readOnly?<!-- -->: boolean }
    * ##### optionalctx: any
    * ##### optionaleventBroadcaster: [TransactionEventBroadcaster](https://mikro-orm.io/api/core/class/TransactionEventBroadcaster.md)
    * ##### optionalisolationLevel: [IsolationLevel](https://mikro-orm.io/api/core/enum/IsolationLevel.md)
    * ##### optionalloggerContext: [LogContext](https://mikro-orm.io/api/core/interface/LogContext.md)
    * ##### optionalreadOnly: boolean

  #### Returns Promise\<T>
