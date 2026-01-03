# Source: https://mikro-orm.io/api/mariadb/class/MariaDbConnection.md

# MariaDbConnection<!-- -->

### Hierarchy

* [MySqlConnection](https://mikro-orm.io/api/knex/class/MySqlConnection.md)
  * *MariaDbConnection*

## Index[**](#Index)

### Constructors

* [**constructor](#constructor)

### Methods

* [**begin](#begin)
* [**checkConnection](#checkConnection)
* [**close](#close)
* [**commit](#commit)
* [**connect](#connect)
* [**createKnex](#createKnex)
* [**ensureConnection](#ensureConnection)
* [**execute](#execute)
* [**getClientUrl](#getClientUrl)
* [**getConnectionOptions](#getConnectionOptions)
* [**getDefaultClientUrl](#getDefaultClientUrl)
* [**getKnex](#getKnex)
* [**getPlatform](#getPlatform)
* [**isConnected](#isConnected)
* [**loadFile](#loadFile)
* [**rollback](#rollback)
* [**setMetadata](#setMetadata)
* [**setPlatform](#setPlatform)
* [**transactional](#transactional)

## Constructors<!-- -->[**](#Constructors)

### [**](#constructor)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/AbstractSqlConnection.ts#L34)constructor

* ****new MariaDbConnection**(config, options, type): [MariaDbConnection](https://mikro-orm.io/api/mariadb/class/MariaDbConnection.md)

- Inherited from MySqlConnection.constructor

  #### Parameters

  * ##### config: [Configuration](https://mikro-orm.io/api/core/class/Configuration.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>, [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>>>
  * ##### optionaloptions: [ConnectionOptions](https://mikro-orm.io/api/core/interface/ConnectionOptions.md)
  * ##### optionaltype: read | write

  #### Returns [MariaDbConnection](https://mikro-orm.io/api/mariadb/class/MariaDbConnection.md)

## Methods<!-- -->[**](#Methods)

### [**](#begin)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/AbstractSqlConnection.ts#L96)inheritedbegin

* ****begin**(options): Promise\<Transaction\<any, any\[]>>

- Inherited from MySqlConnection.begin

  #### Parameters

  * ##### options: { ctx?<!-- -->: Transaction\<any, any\[]>; eventBroadcaster?<!-- -->: [TransactionEventBroadcaster](https://mikro-orm.io/api/core/class/TransactionEventBroadcaster.md); isolationLevel?<!-- -->: [IsolationLevel](https://mikro-orm.io/api/core/enum/IsolationLevel.md); loggerContext?<!-- -->: [LogContext](https://mikro-orm.io/api/core/interface/LogContext.md); readOnly?<!-- -->: boolean } = <!-- -->{}
    * ##### optionalctx: Transaction\<any, any\[]>
    * ##### optionaleventBroadcaster: [TransactionEventBroadcaster](https://mikro-orm.io/api/core/class/TransactionEventBroadcaster.md)
    * ##### optionalisolationLevel: [IsolationLevel](https://mikro-orm.io/api/core/enum/IsolationLevel.md)
    * ##### optionalloggerContext: [LogContext](https://mikro-orm.io/api/core/interface/LogContext.md)
    * ##### optionalreadOnly: boolean

  #### Returns Promise\<Transaction\<any, any\[]>>

### [**](#checkConnection)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/AbstractSqlConnection.ts#L73)inheritedcheckConnection

* ****checkConnection**(): Promise<{ ok: true } | { error?
  <!-- -->
  : Error; ok: false; reason: string }>

- Inherited from MySqlConnection.checkConnection

  Are we connected to the database

  ***

  #### Returns Promise<{ ok: true } | { error?<!-- -->: Error; ok: false; reason: string }>

### [**](#close)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/AbstractSqlConnection.ts#L57)inheritedclose

* ****close**(force): Promise\<void>

- Inherited from MySqlConnection.close

  Closes the database connection (aka disconnect)

  ***

  #### Parameters

  * ##### optionalforce: boolean

  #### Returns Promise\<void>

### [**](#commit)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/AbstractSqlConnection.ts#L128)inheritedcommit

* ****commit**(ctx, eventBroadcaster, loggerContext): Promise\<void>

- Inherited from MySqlConnection.commit

  #### Parameters

  * ##### ctx: Transaction\<any, any\[]>
  * ##### optionaleventBroadcaster: [TransactionEventBroadcaster](https://mikro-orm.io/api/core/class/TransactionEventBroadcaster.md)
  * ##### optionalloggerContext: [LogContext](https://mikro-orm.io/api/core/interface/LogContext.md)

  #### Returns Promise\<void>

### [**](#connect)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/AbstractSqlConnection.ts#L42)inheritedconnect

* ****connect**(): void | Promise\<void>

- Inherited from MySqlConnection.connect

  Establishes connection to database

  ***

  #### Returns void | Promise\<void>

### [**](#createKnex)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/mariadb/src/MariaDbConnection.ts#L6)createKnex

* ****createKnex**(): void

- Overrides MySqlConnection.createKnex

  #### Returns void

### [**](#ensureConnection)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/connections/Connection.ts#L62)inheritedensureConnection

* ****ensureConnection**(): Promise\<void>

- Inherited from MySqlConnection.ensureConnection

  Ensure the connection exists, this is used to support lazy connect when using `MikroORM.initSync()`

  ***

  #### Returns Promise\<void>

### [**](#execute)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/AbstractSqlConnection.ts#L169)inheritedexecute

* ****execute**\<T>(queryOrKnex, params, method, ctx, loggerContext): Promise\<T>

- Inherited from MySqlConnection.execute

  #### Parameters

  * ##### queryOrKnex: string | QueryBuilder\<any, any> | Raw\<any>
  * ##### params: unknown\[] = <!-- -->\[]
  * ##### method: get | all | run = <!-- -->'all'
  * ##### optionalctx: any
  * ##### optionalloggerContext: [LoggingOptions](https://mikro-orm.io/api/core.md#LoggingOptions)

  #### Returns Promise\<T>

### [**](#getClientUrl)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/connections/Connection.ts#L118)inheritedgetClientUrl

* ****getClientUrl**(): string

- Inherited from MySqlConnection.getClientUrl

  #### Returns string

### [**](#getConnectionOptions)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/mariadb/src/MariaDbConnection.ts#L11)getConnectionOptions

* ****getConnectionOptions**(): MySqlConnectionConfig

- Overrides MySqlConnection.getConnectionOptions

  #### Returns MySqlConnectionConfig

### [**](#getDefaultClientUrl)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/dialects/mysql/MySqlConnection.ts#L12)inheritedgetDefaultClientUrl

* ****getDefaultClientUrl**(): string

- Inherited from MySqlConnection.getDefaultClientUrl

  Returns default client url for given driver (e.g. mongodb://127.0.0.1:27017 for mongodb)

  ***

  #### Returns string

### [**](#getKnex)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/AbstractSqlConnection.ts#L46)inheritedgetKnex

* ****getKnex**(): [Knex](https://mikro-orm.io/api/knex/interface/Knex.md)\<any, any\[]>

- Inherited from MySqlConnection.getKnex

  #### Returns [Knex](https://mikro-orm.io/api/knex/interface/Knex.md)\<any, any\[]>

### [**](#getPlatform)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/connections/Connection.ts#L137)inheritedgetPlatform

* ****getPlatform**(): [Platform](https://mikro-orm.io/api/core/class/Platform.md)

- Inherited from MySqlConnection.getPlatform

  #### Returns [Platform](https://mikro-orm.io/api/core/class/Platform.md)

### [**](#isConnected)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/AbstractSqlConnection.ts#L65)inheritedisConnected

* ****isConnected**(): Promise\<boolean>

- Inherited from MySqlConnection.isConnected

  Are we connected to the database

  ***

  #### Returns Promise\<boolean>

### [**](#loadFile)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/AbstractSqlConnection.ts#L197)inheritedloadFile

* ****loadFile**(path): Promise\<void>

- Inherited from MySqlConnection.loadFile

  Execute raw SQL queries from file

  ***

  #### Parameters

  * ##### path: string

  #### Returns Promise\<void>

### [**](#rollback)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/AbstractSqlConnection.ts#L149)inheritedrollback

* ****rollback**(ctx, eventBroadcaster, loggerContext): Promise\<void>

- Inherited from MySqlConnection.rollback

  #### Parameters

  * ##### ctx: Transaction\<any, any\[]>
  * ##### optionaleventBroadcaster: [TransactionEventBroadcaster](https://mikro-orm.io/api/core/class/TransactionEventBroadcaster.md)
  * ##### optionalloggerContext: [LogContext](https://mikro-orm.io/api/core/interface/LogContext.md)

  #### Returns Promise\<void>

### [**](#setMetadata)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/connections/Connection.ts#L129)inheritedsetMetadata

* ****setMetadata**(metadata): void

- Inherited from MySqlConnection.setMetadata

  #### Parameters

  * ##### metadata: [MetadataStorage](https://mikro-orm.io/api/core/class/MetadataStorage.md)

  #### Returns void

### [**](#setPlatform)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/connections/Connection.ts#L133)inheritedsetPlatform

* ****setPlatform**(platform): void

- Inherited from MySqlConnection.setPlatform

  #### Parameters

  * ##### platform: [Platform](https://mikro-orm.io/api/core/class/Platform.md)

  #### Returns void

### [**](#transactional)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/AbstractSqlConnection.ts#L82)inheritedtransactional

* ****transactional**\<T>(cb, options): Promise\<T>

- Inherited from MySqlConnection.transactional

  #### Parameters

  * ##### cb: (trx) => Promise\<T>
  *
    ##### options: { ctx?<!-- -->: Transaction\<any, any\[]>; eventBroadcaster?<!-- -->: [TransactionEventBroadcaster](https://mikro-orm.io/api/core/class/TransactionEventBroadcaster.md); isolationLevel?<!-- -->: [IsolationLevel](https://mikro-orm.io/api/core/enum/IsolationLevel.md); loggerContext?<!-- -->: [LogContext](https://mikro-orm.io/api/core/interface/LogContext.md); readOnly?<!-- -->: boolean } = <!-- -->{}
    * ##### optionalctx: Transaction\<any, any\[]>
    * ##### optionaleventBroadcaster: [TransactionEventBroadcaster](https://mikro-orm.io/api/core/class/TransactionEventBroadcaster.md)
    * ##### optionalisolationLevel: [IsolationLevel](https://mikro-orm.io/api/core/enum/IsolationLevel.md)
    * ##### optionalloggerContext: [LogContext](https://mikro-orm.io/api/core/interface/LogContext.md)
    * ##### optionalreadOnly: boolean

  #### Returns Promise\<T>
