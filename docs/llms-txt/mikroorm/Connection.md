# Source: https://mikro-orm.io/api/core/class/Connection.md

# abstractConnection<!-- -->

### Hierarchy

* *Connection*

  * [AbstractSqlConnection](https://mikro-orm.io/api/sql/class/AbstractSqlConnection.md)
  * [MongoConnection](https://mikro-orm.io/api/mongodb/class/MongoConnection.md)

## Index[**](#index)

### Constructors

* [**constructor](#constructor)

### Methods

* [**begin](#begin)
* [**close](#close)
* [**commit](#commit)
* [**connect](#connect)
* [**ensureConnection](#ensureconnection)
* [**execute](#execute)
* [**executeDump](#executedump)
* [**getConnectionOptions](#getconnectionoptions)
* [**getPlatform](#getplatform)
* [**checkConnection](#checkConnection)
* [**isConnected](#isConnected)
* [**rollback](#rollback)
* [**setMetadata](#setmetadata)
* [**setPlatform](#setplatform)
* [**transactional](#transactional)

## Constructors<!-- -->[**](#constructors)

### [**](#constructor)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/connections/Connection.ts#L24)constructor

* ****new Connection**(config, options, type): [Connection](https://mikro-orm.io/api/core/class/Connection.md)

* #### Parameters

  * ##### config: [Configuration](https://mikro-orm.io/api/core/class/Configuration.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>, [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>>>

  * ##### optionaloptions: [ConnectionOptions](https://mikro-orm.io/api/core/interface/ConnectionOptions.md)

  * ##### type: [ConnectionType](https://mikro-orm.io/api/core.md#ConnectionType) = <!-- -->'write'

  #### Returns [Connection](https://mikro-orm.io/api/core/class/Connection.md)

## Methods<!-- -->[**](#methods)

### [**](#begin)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/connections/Connection.ts#L123)begin

* ****begin**(options): Promise\<any>

* #### Parameters

  * ##### optionaloptions: { ctx?<!-- -->: any; eventBroadcaster?<!-- -->: [TransactionEventBroadcaster](https://mikro-orm.io/api/core/class/TransactionEventBroadcaster.md); isolationLevel?<!-- -->: [IsolationLevel](https://mikro-orm.io/api/core/enum/IsolationLevel.md) | read uncommitted | read committed | snapshot | repeatable read | serializable; loggerContext?<!-- -->: [LogContext](https://mikro-orm.io/api/core/interface/LogContext.md); readOnly?<!-- -->: boolean }

    * ##### optionalctx: any

    * ##### optionaleventBroadcaster: [TransactionEventBroadcaster](https://mikro-orm.io/api/core/class/TransactionEventBroadcaster.md)

    * ##### optionalisolationLevel: [IsolationLevel](https://mikro-orm.io/api/core/enum/IsolationLevel.md) | read uncommitted | read committed | snapshot | repeatable read | serializable

    * ##### optionalloggerContext: [LogContext](https://mikro-orm.io/api/core/interface/LogContext.md)

    * ##### optionalreadOnly: boolean

  #### Returns Promise\<any>

### [**](#close)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/connections/Connection.ts#L72)close

* ****close**(force): Promise\<void>

* Closes the database connection (aka disconnect)

  ***

  #### Parameters

  * ##### optionalforce: boolean

  #### Returns Promise\<void>

### [**](#commit)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/connections/Connection.ts#L133)commit

* ****commit**(ctx, eventBroadcaster, loggerContext): Promise\<void>

* #### Parameters

  * ##### ctx: any

  * ##### optionaleventBroadcaster: [TransactionEventBroadcaster](https://mikro-orm.io/api/core/class/TransactionEventBroadcaster.md)

  * ##### optionalloggerContext: [LogContext](https://mikro-orm.io/api/core/interface/LogContext.md)

  #### Returns Promise\<void>

### [**](#connect)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/connections/Connection.ts#L57)abstractconnect

* ****connect**(options): void | Promise\<void>

* Establishes connection to database

  ***

  #### Parameters

  * ##### optionaloptions: { skipOnConnect?<!-- -->: boolean }

    * ##### optionalskipOnConnect: boolean

  #### Returns void | Promise\<void>

### [**](#ensureconnection)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/connections/Connection.ts#L81)ensureConnection

* ****ensureConnection**(): Promise\<void>

* Ensure the connection exists, this is used to support lazy connect when using `new MikroORM()` instead of the async `init` method.

  ***

  #### Returns Promise\<void>

### [**](#execute)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/connections/Connection.ts#L149)abstractexecute

* ****execute**\<T>(query, params, method, ctx): Promise\<any>

* #### Parameters

  * ##### query: string

  * ##### optionalparams: any\[]

  * ##### optionalmethod: get | all | run

  * ##### optionalctx: any

  #### Returns Promise\<any>

### [**](#executedump)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/connections/Connection.ts#L91)executeDump

* ****executeDump**(dump): Promise\<void>

* Execute raw SQL queries, handy from running schema dump loaded from a file. This method doesn't support transactions, as opposed to `orm.schema.execute()`, which is used internally.

  ***

  #### Parameters

  * ##### dump: string

  #### Returns Promise\<void>

### [**](#getconnectionoptions)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/connections/Connection.ts#L156)getConnectionOptions

* ****getConnectionOptions**(): [ConnectionConfig](https://mikro-orm.io/api/core/interface/ConnectionConfig.md)

* #### Returns [ConnectionConfig](https://mikro-orm.io/api/core/interface/ConnectionConfig.md)

### [**](#getplatform)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/connections/Connection.ts#L193)getPlatform

* ****getPlatform**(): [Platform](https://mikro-orm.io/api/core/class/Platform.md)

* #### Returns [Platform](https://mikro-orm.io/api/core/class/Platform.md)

### [**](#checkConnection)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/connections/Connection.ts#L67)abstractcheckConnection

* ****checkConnection**(): Promise<{ ok: true } | { error?
  <!-- -->
  : Error; ok: false; reason: string }>

* Are we connected to the database

  ***

  #### Returns Promise<{ ok: true } | { error?<!-- -->: Error; ok: false; reason: string }>

### [**](#isConnected)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/connections/Connection.ts#L62)abstractisConnected

* ****isConnected**(): Promise\<boolean>

* Are we connected to the database

  ***

  #### Returns Promise\<boolean>

### [**](#rollback)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/connections/Connection.ts#L141)rollback

* ****rollback**(ctx, eventBroadcaster, loggerContext): Promise\<void>

* #### Parameters

  * ##### ctx: any

  * ##### optionaleventBroadcaster: [TransactionEventBroadcaster](https://mikro-orm.io/api/core/class/TransactionEventBroadcaster.md)

  * ##### optionalloggerContext: [LogContext](https://mikro-orm.io/api/core/interface/LogContext.md)

  #### Returns Promise\<void>

### [**](#setmetadata)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/connections/Connection.ts#L185)setMetadata

* ****setMetadata**(metadata): void

* #### Parameters

  * ##### metadata: [MetadataStorage](https://mikro-orm.io/api/core/class/MetadataStorage.md)

  #### Returns void

### [**](#setplatform)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/connections/Connection.ts#L189)setPlatform

* ****setPlatform**(platform): void

* #### Parameters

  * ##### platform: [Platform](https://mikro-orm.io/api/core/class/Platform.md)

  #### Returns void

### [**](#transactional)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/connections/Connection.ts#L110)transactional

* ****transactional**\<T>(cb, options): Promise\<T>

* #### Parameters

  * ##### cb: (trx) => Promise\<T>

  *

    ##### optionaloptions: { ctx?<!-- -->: any; eventBroadcaster?<!-- -->: [TransactionEventBroadcaster](https://mikro-orm.io/api/core/class/TransactionEventBroadcaster.md); isolationLevel?<!-- -->: [IsolationLevel](https://mikro-orm.io/api/core/enum/IsolationLevel.md) | read uncommitted | read committed | snapshot | repeatable read | serializable; loggerContext?<!-- -->: [LogContext](https://mikro-orm.io/api/core/interface/LogContext.md); readOnly?<!-- -->: boolean }

    * ##### optionalctx: any

    * ##### optionaleventBroadcaster: [TransactionEventBroadcaster](https://mikro-orm.io/api/core/class/TransactionEventBroadcaster.md)

    * ##### optionalisolationLevel: [IsolationLevel](https://mikro-orm.io/api/core/enum/IsolationLevel.md) | read uncommitted | read committed | snapshot | repeatable read | serializable

    * ##### optionalloggerContext: [LogContext](https://mikro-orm.io/api/core/interface/LogContext.md)

    * ##### optionalreadOnly: boolean

  #### Returns Promise\<T>
