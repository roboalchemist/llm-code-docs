# Source: https://mikro-orm.io/api/mongodb/class/MongoConnection.md

# MongoConnection<!-- -->

### Hierarchy

* [Connection](https://mikro-orm.io/api/core/class/Connection.md)
  * *MongoConnection*

## Index[**](#Index)

### Constructors

* [**constructor](#constructor)

### Methods

* [**aggregate](#aggregate)
* [**begin](#begin)
* [**bulkUpdateMany](#bulkUpdateMany)
* [**checkConnection](#checkConnection)
* [**close](#close)
* [**commit](#commit)
* [**connect](#connect)
* [**countDocuments](#countDocuments)
* [**createCollection](#createCollection)
* [**deleteMany](#deleteMany)
* [**dropCollection](#dropCollection)
* [**ensureConnection](#ensureConnection)
* [**execute](#execute)
* [**find](#find)
* [**getClient](#getClient)
* [**getClientUrl](#getClientUrl)
* [**getCollection](#getCollection)
* [**getConnectionOptions](#getConnectionOptions)
* [**getDb](#getDb)
* [**getDefaultClientUrl](#getDefaultClientUrl)
* [**getPlatform](#getPlatform)
* [**insertMany](#insertMany)
* [**insertOne](#insertOne)
* [**isConnected](#isConnected)
* [**listCollections](#listCollections)
* [**rollback](#rollback)
* [**setMetadata](#setMetadata)
* [**setPlatform](#setPlatform)
* [**transactional](#transactional)
* [**updateMany](#updateMany)

## Constructors<!-- -->[**](#Constructors)

### [**](#constructor)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/mongodb/src/MongoConnection.ts#L49)constructor

* ****new MongoConnection**(config, options, type): [MongoConnection](https://mikro-orm.io/api/mongodb/class/MongoConnection.md)

- Overrides Connection.constructor

  #### Parameters

  * ##### config: [Configuration](https://mikro-orm.io/api/core/class/Configuration.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>, [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>>>
  * ##### optionaloptions: [ConnectionOptions](https://mikro-orm.io/api/core/interface/ConnectionOptions.md)
  * ##### type: [ConnectionType](https://mikro-orm.io/api/core.md#ConnectionType) = <!-- -->'write'

  #### Returns [MongoConnection](https://mikro-orm.io/api/mongodb/class/MongoConnection.md)

## Methods<!-- -->[**](#Methods)

### [**](#aggregate)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/mongodb/src/MongoConnection.ts#L239)aggregate

* ****aggregate**\<T>(collection, pipeline, ctx, loggerContext): Promise\<T\[]>

- #### Parameters

  * ##### collection: string
  * ##### pipeline: any\[]
  * ##### optionalctx: ClientSession
  * ##### optionalloggerContext: [LoggingOptions](https://mikro-orm.io/api/core.md#LoggingOptions)

  #### Returns Promise\<T\[]>

### [**](#begin)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/mongodb/src/MongoConnection.ts#L273)begin

* ****begin**(options): Promise\<ClientSession>

- Overrides Connection.begin

  #### Parameters

  * ##### options: { ctx?<!-- -->: ClientSession; eventBroadcaster?<!-- -->: [TransactionEventBroadcaster](https://mikro-orm.io/api/core/class/TransactionEventBroadcaster.md); isolationLevel?<!-- -->: [IsolationLevel](https://mikro-orm.io/api/core/enum/IsolationLevel.md) } & TransactionOptions = <!-- -->{}

  #### Returns Promise\<ClientSession>

### [**](#bulkUpdateMany)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/mongodb/src/MongoConnection.ts#L231)bulkUpdateMany

* ****bulkUpdateMany**\<T>(collection, where, data, ctx, upsert, upsertOptions): Promise<[QueryResult](https://mikro-orm.io/api/core/interface/QueryResult.md)\<T>>

- #### Parameters

  * ##### collection: string
  * ##### where: [FilterQuery](https://mikro-orm.io/api/core.md#FilterQuery)\<T>\[]
  * ##### data: Partial\<T>\[]
  * ##### optionalctx: ClientSession
  * ##### optionalupsert: boolean
  * ##### optionalupsertOptions: [UpsertManyOptions](https://mikro-orm.io/api/core/interface/UpsertManyOptions.md)\<T, never>

  #### Returns Promise<[QueryResult](https://mikro-orm.io/api/core/interface/QueryResult.md)\<T>>

### [**](#checkConnection)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/mongodb/src/MongoConnection.ts#L92)checkConnection

* ****checkConnection**(): Promise<{ ok: true } | { error?
  <!-- -->
  : Error; ok: false; reason: string }>

- Overrides Connection.checkConnection

  Are we connected to the database

  ***

  #### Returns Promise<{ ok: true } | { error?<!-- -->: Error; ok: false; reason: string }>

### [**](#close)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/mongodb/src/MongoConnection.ts#L78)close

* ****close**(force): Promise\<void>

- Overrides Connection.close

  Closes the database connection (aka disconnect)

  ***

  #### Parameters

  * ##### optionalforce: boolean

  #### Returns Promise\<void>

### [**](#commit)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/mongodb/src/MongoConnection.ts#L288)commit

* ****commit**(ctx, eventBroadcaster): Promise\<void>

- Overrides Connection.commit

  #### Parameters

  * ##### ctx: ClientSession
  * ##### optionaleventBroadcaster: [TransactionEventBroadcaster](https://mikro-orm.io/api/core/class/TransactionEventBroadcaster.md)

  #### Returns Promise\<void>

### [**](#connect)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/mongodb/src/MongoConnection.ts#L63)connect

* ****connect**(): Promise\<void>

- Overrides Connection.connect

  Establishes connection to database

  ***

  #### Returns Promise\<void>

### [**](#countDocuments)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/mongodb/src/MongoConnection.ts#L252)countDocuments

* ****countDocuments**\<T>(collection, where, ctx): Promise\<number>

- #### Parameters

  * ##### collection: string
  * ##### where: [FilterQuery](https://mikro-orm.io/api/core.md#FilterQuery)\<T>
  * ##### optionalctx: ClientSession

  #### Returns Promise\<number>

### [**](#createCollection)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/mongodb/src/MongoConnection.ts#L111)createCollection

* ****createCollection**\<T>(name): Promise\<Collection\<T>>

- #### Parameters

  * ##### name: [EntityName](https://mikro-orm.io/api/core.md#EntityName)\<T>

  #### Returns Promise\<Collection\<T>>

### [**](#deleteMany)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/mongodb/src/MongoConnection.ts#L235)deleteMany

* ****deleteMany**\<T>(collection, where, ctx): Promise<[QueryResult](https://mikro-orm.io/api/core/interface/QueryResult.md)\<T>>

- #### Parameters

  * ##### collection: string
  * ##### where: [FilterQuery](https://mikro-orm.io/api/core.md#FilterQuery)\<T>
  * ##### optionalctx: ClientSession

  #### Returns Promise<[QueryResult](https://mikro-orm.io/api/core/interface/QueryResult.md)\<T>>

### [**](#dropCollection)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/mongodb/src/MongoConnection.ts#L120)dropCollection

* ****dropCollection**(name): Promise\<boolean>

- #### Parameters

  * ##### name: [EntityName](https://mikro-orm.io/api/core.md#EntityName)\<Partial\<any>>

  #### Returns Promise\<boolean>

### [**](#ensureConnection)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/connections/Connection.ts#L62)inheritedensureConnection

* ****ensureConnection**(): Promise\<void>

- Inherited from Connection.ensureConnection

  Ensure the connection exists, this is used to support lazy connect when using `MikroORM.initSync()`

  ***

  #### Returns Promise\<void>

### [**](#execute)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/mongodb/src/MongoConnection.ts#L170)execute

* ****execute**(query): Promise\<any>

- Overrides Connection.execute

  #### Parameters

  * ##### query: string

  #### Returns Promise\<any>

### [**](#find)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/mongodb/src/MongoConnection.ts#L174)find

* ****find**\<T>(collection, where, orderBy, limit, offset, fields, ctx, loggerContext): Promise<[EntityData](https://mikro-orm.io/api/core.md#EntityData)\<T>\[]>

- #### Parameters

  * ##### collection: string
  * ##### where: [FilterQuery](https://mikro-orm.io/api/core.md#FilterQuery)\<T>
  * ##### optionalorderBy: [QueryOrderMap](https://mikro-orm.io/api/core.md#QueryOrderMap)\<T> | [QueryOrderMap](https://mikro-orm.io/api/core.md#QueryOrderMap)\<T>\[]
  * ##### optionallimit: number
  * ##### optionaloffset: number
  * ##### optionalfields: string\[]
  * ##### optionalctx: ClientSession
  * ##### optionalloggerContext: [LoggingOptions](https://mikro-orm.io/api/core.md#LoggingOptions)

  #### Returns Promise<[EntityData](https://mikro-orm.io/api/core.md#EntityData)\<T>\[]>

### [**](#getClient)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/mongodb/src/MongoConnection.ts#L103)getClient

* ****getClient**(): MongoClient

- #### Returns MongoClient

### [**](#getClientUrl)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/mongodb/src/MongoConnection.ts#L158)getClientUrl

* ****getClientUrl**(): string

- Overrides Connection.getClientUrl

  #### Returns string

### [**](#getCollection)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/mongodb/src/MongoConnection.ts#L107)getCollection

* ****getCollection**\<T>(name): Collection\<T>

- #### Parameters

  * ##### name: [EntityName](https://mikro-orm.io/api/core.md#EntityName)\<T>

  #### Returns Collection\<T>

### [**](#getConnectionOptions)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/mongodb/src/MongoConnection.ts#L128)getConnectionOptions

* ****getConnectionOptions**(): MongoClientOptions & [ConnectionConfig](https://mikro-orm.io/api/core/interface/ConnectionConfig.md)

- Overrides Connection.getConnectionOptions

  #### Returns MongoClientOptions & [ConnectionConfig](https://mikro-orm.io/api/core/interface/ConnectionConfig.md)

### [**](#getDb)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/mongodb/src/MongoConnection.ts#L166)getDb

* ****getDb**(): Db

- #### Returns Db

### [**](#getDefaultClientUrl)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/mongodb/src/MongoConnection.ts#L124)getDefaultClientUrl

* ****getDefaultClientUrl**(): string

- Overrides Connection.getDefaultClientUrl

  Returns default client url for given driver (e.g. mongodb://127.0.0.1:27017 for mongodb)

  ***

  #### Returns string

### [**](#getPlatform)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/connections/Connection.ts#L137)inheritedgetPlatform

* ****getPlatform**(): [Platform](https://mikro-orm.io/api/core/class/Platform.md)

- Inherited from Connection.getPlatform

  #### Returns [Platform](https://mikro-orm.io/api/core/class/Platform.md)

### [**](#insertMany)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/mongodb/src/MongoConnection.ts#L223)insertMany

* ****insertMany**\<T>(collection, data, ctx): Promise<[QueryResult](https://mikro-orm.io/api/core/interface/QueryResult.md)\<T>>

- #### Parameters

  * ##### collection: string
  * ##### data: Partial\<T>\[]
  * ##### optionalctx: ClientSession

  #### Returns Promise<[QueryResult](https://mikro-orm.io/api/core/interface/QueryResult.md)\<T>>

### [**](#insertOne)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/mongodb/src/MongoConnection.ts#L219)insertOne

* ****insertOne**\<T>(collection, data, ctx): Promise<[QueryResult](https://mikro-orm.io/api/core/interface/QueryResult.md)\<T>>

- #### Parameters

  * ##### collection: string
  * ##### data: Partial\<T>
  * ##### optionalctx: ClientSession

  #### Returns Promise<[QueryResult](https://mikro-orm.io/api/core/interface/QueryResult.md)\<T>>

### [**](#isConnected)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/mongodb/src/MongoConnection.ts#L83)isConnected

* ****isConnected**(): Promise\<boolean>

- Overrides Connection.isConnected

  Are we connected to the database

  ***

  #### Returns Promise\<boolean>

### [**](#listCollections)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/mongodb/src/MongoConnection.ts#L115)listCollections

* ****listCollections**(): Promise\<string\[]>

- #### Returns Promise\<string\[]>

### [**](#rollback)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/mongodb/src/MongoConnection.ts#L296)rollback

* ****rollback**(ctx, eventBroadcaster): Promise\<void>

- Overrides Connection.rollback

  #### Parameters

  * ##### ctx: ClientSession
  * ##### optionaleventBroadcaster: [TransactionEventBroadcaster](https://mikro-orm.io/api/core/class/TransactionEventBroadcaster.md)

  #### Returns Promise\<void>

### [**](#setMetadata)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/connections/Connection.ts#L129)inheritedsetMetadata

* ****setMetadata**(metadata): void

- Inherited from Connection.setMetadata

  #### Parameters

  * ##### metadata: [MetadataStorage](https://mikro-orm.io/api/core/class/MetadataStorage.md)

  #### Returns void

### [**](#setPlatform)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/connections/Connection.ts#L133)inheritedsetPlatform

* ****setPlatform**(platform): void

- Inherited from Connection.setPlatform

  #### Parameters

  * ##### platform: [Platform](https://mikro-orm.io/api/core/class/Platform.md)

  #### Returns void

### [**](#transactional)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/mongodb/src/MongoConnection.ts#L256)transactional

* ****transactional**\<T>(cb, options): Promise\<T>

- Overrides Connection.transactional

  #### Parameters

  * ##### cb: (trx) => Promise\<T>
  *
    ##### options: { ctx?<!-- -->: ClientSession; eventBroadcaster?<!-- -->: [TransactionEventBroadcaster](https://mikro-orm.io/api/core/class/TransactionEventBroadcaster.md); isolationLevel?<!-- -->: [IsolationLevel](https://mikro-orm.io/api/core/enum/IsolationLevel.md) } & TransactionOptions = <!-- -->{}

  #### Returns Promise\<T>

### [**](#updateMany)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/mongodb/src/MongoConnection.ts#L227)updateMany

* ****updateMany**\<T>(collection, where, data, ctx, upsert, upsertOptions): Promise<[QueryResult](https://mikro-orm.io/api/core/interface/QueryResult.md)\<T>>

- #### Parameters

  * ##### collection: string
  * ##### where: [FilterQuery](https://mikro-orm.io/api/core.md#FilterQuery)\<T>
  * ##### data: Partial\<T>
  * ##### optionalctx: ClientSession
  * ##### optionalupsert: boolean
  * ##### optionalupsertOptions: [UpsertOptions](https://mikro-orm.io/api/core/interface/UpsertOptions.md)\<T, never>

  #### Returns Promise<[QueryResult](https://mikro-orm.io/api/core/interface/QueryResult.md)\<T>>
