# Source: https://mikro-orm.io/api/mongodb/class/MongoConnection.md

# MongoConnection<!-- -->

### Hierarchy

* [Connection](https://mikro-orm.io/api/core/class/Connection.md)
  * *MongoConnection*

## Index[**](#index)

### Constructors

* [**constructor](#constructor)

### Methods

* [**aggregate](#aggregate)
* [**begin](#begin)
* [**bulkUpdateMany](#bulkupdatemany)
* [**close](#close)
* [**commit](#commit)
* [**connect](#connect)
* [**countDocuments](#countdocuments)
* [**createClient](#createclient)
* [**createCollection](#createcollection)
* [**deleteMany](#deletemany)
* [**dropCollection](#dropcollection)
* [**ensureConnection](#ensureConnection)
* [**execute](#execute)
* [**executeDump](#executeDump)
* [**find](#find)
* [**getClient](#getclient)
* [**getCollection](#getcollection)
* [**getConnectionOptions](#getConnectionOptions)
* [**getDb](#getdb)
* [**getPlatform](#getPlatform)
* [**checkConnection](#checkconnection)
* [**insertMany](#insertmany)
* [**insertOne](#insertone)
* [**isConnected](#isconnected)
* [**listCollections](#listcollections)
* [**mapOptions](#mapoptions)
* [**rollback](#rollback)
* [**setMetadata](#setMetadata)
* [**setPlatform](#setPlatform)
* [**stream](#stream)
* [**streamAggregate](#streamaggregate)
* [**transactional](#transactional)
* [**updateMany](#updatemany)

## Constructors<!-- -->[**](#constructors)

### [**](#constructor)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/mongodb/src/MongoConnection.ts#L50)constructor

* ****new MongoConnection**(config, options, type): [MongoConnection](https://mikro-orm.io/api/mongodb/class/MongoConnection.md)

* Overrides Connection.constructor

  #### Parameters

  * ##### config: [Configuration](https://mikro-orm.io/api/core/class/Configuration.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>, [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>>>

  * ##### optionaloptions: [ConnectionOptions](https://mikro-orm.io/api/core/interface/ConnectionOptions.md)

  * ##### type: [ConnectionType](https://mikro-orm.io/api/core.md#ConnectionType) = <!-- -->'write'

  #### Returns [MongoConnection](https://mikro-orm.io/api/mongodb/class/MongoConnection.md)

## Methods<!-- -->[**](#methods)

### [**](#aggregate)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/mongodb/src/MongoConnection.ts#L315)aggregate

* ****aggregate**\<T>(entityName, pipeline, ctx, loggerContext): Promise\<T\[]>

* #### Parameters

  * ##### entityName: [EntityName](https://mikro-orm.io/api/core.md#EntityName)\<T>

  * ##### pipeline: any\[]

  * ##### optionalctx: ClientSession

  * ##### optionalloggerContext: [LoggingOptions](https://mikro-orm.io/api/core.md#LoggingOptions)

  #### Returns Promise\<T\[]>

### [**](#begin)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/mongodb/src/MongoConnection.ts#L388)begin

* ****begin**(options): Promise\<ClientSession>

* Overrides Connection.begin

  #### Parameters

  * ##### options: { ctx?<!-- -->: ClientSession; eventBroadcaster?<!-- -->: [TransactionEventBroadcaster](https://mikro-orm.io/api/core/class/TransactionEventBroadcaster.md); isolationLevel?<!-- -->: [IsolationLevel](https://mikro-orm.io/api/core/enum/IsolationLevel.md) } & TransactionOptions = <!-- -->{}

  #### Returns Promise\<ClientSession>

### [**](#bulkupdatemany)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/mongodb/src/MongoConnection.ts#L296)bulkUpdateMany

* ****bulkUpdateMany**\<T>(entityName, where, data, ctx, upsert, upsertOptions): Promise<[QueryResult](https://mikro-orm.io/api/core/interface/QueryResult.md)\<T>>

* #### Parameters

  * ##### entityName: [EntityName](https://mikro-orm.io/api/core.md#EntityName)\<T>

  * ##### where: [FilterQuery](https://mikro-orm.io/api/core.md#FilterQuery)\<T>\[]

  * ##### data: Partial\<T>\[]

  * ##### optionalctx: ClientSession

  * ##### optionalupsert: boolean

  * ##### optionalupsertOptions: [UpsertManyOptions](https://mikro-orm.io/api/core/interface/UpsertManyOptions.md)\<T, never>

  #### Returns Promise<[QueryResult](https://mikro-orm.io/api/core/interface/QueryResult.md)\<T>>

### [**](#close)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/mongodb/src/MongoConnection.ts#L102)close

* ****close**(force): Promise\<void>

* Overrides Connection.close

  Closes the database connection (aka disconnect)

  ***

  #### Parameters

  * ##### optionalforce: boolean

  #### Returns Promise\<void>

### [**](#commit)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/mongodb/src/MongoConnection.ts#L409)commit

* ****commit**(ctx, eventBroadcaster): Promise\<void>

* Overrides Connection.commit

  #### Parameters

  * ##### ctx: ClientSession

  * ##### optionaleventBroadcaster: [TransactionEventBroadcaster](https://mikro-orm.io/api/core/class/TransactionEventBroadcaster.md)

  #### Returns Promise\<void>

### [**](#connect)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/mongodb/src/MongoConnection.ts#L64)connect

* ****connect**(options): Promise\<void>

* Overrides Connection.connect

  Establishes connection to database

  ***

  #### Parameters

  * ##### optionaloptions: { skipOnConnect?<!-- -->: boolean }

    * ##### optionalskipOnConnect: boolean

  #### Returns Promise\<void>

### [**](#countdocuments)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/mongodb/src/MongoConnection.ts#L351)countDocuments

* ****countDocuments**\<T>(entityName, where, opts): Promise\<number>

* #### Parameters

  * ##### entityName: [EntityName](https://mikro-orm.io/api/core.md#EntityName)\<T>

  * ##### where: [FilterQuery](https://mikro-orm.io/api/core.md#FilterQuery)\<T>

  * ##### opts: [MongoCountOptions](https://mikro-orm.io/api/mongodb/interface/MongoCountOptions.md) = <!-- -->{}

  #### Returns Promise\<number>

### [**](#createclient)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/mongodb/src/MongoConnection.ts#L73)createClient

* ****createClient**(): void

* #### Returns void

### [**](#createcollection)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/mongodb/src/MongoConnection.ts#L140)createCollection

* ****createCollection**\<T>(name): Promise\<Collection\<T>>

* #### Parameters

  * ##### name: [EntityName](https://mikro-orm.io/api/core.md#EntityName)\<T>

  #### Returns Promise\<Collection\<T>>

### [**](#deletemany)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/mongodb/src/MongoConnection.ts#L307)deleteMany

* ****deleteMany**\<T>(entityName, where, ctx): Promise<[QueryResult](https://mikro-orm.io/api/core/interface/QueryResult.md)\<T>>

* #### Parameters

  * ##### entityName: [EntityName](https://mikro-orm.io/api/core.md#EntityName)\<T>

  * ##### where: [FilterQuery](https://mikro-orm.io/api/core.md#FilterQuery)\<T>

  * ##### optionalctx: ClientSession

  #### Returns Promise<[QueryResult](https://mikro-orm.io/api/core/interface/QueryResult.md)\<T>>

### [**](#dropcollection)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/mongodb/src/MongoConnection.ts#L149)dropCollection

* ****dropCollection**(name): Promise\<boolean>

* #### Parameters

  * ##### name: [EntityName](https://mikro-orm.io/api/core.md#EntityName)\<Partial\<any>>

  #### Returns Promise\<boolean>

### [**](#ensureConnection)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/connections/Connection.ts#L81)inheritedensureConnection

* ****ensureConnection**(): Promise\<void>

* Inherited from Connection.ensureConnection

  Ensure the connection exists, this is used to support lazy connect when using `new MikroORM()` instead of the async `init` method.

  ***

  #### Returns Promise\<void>

### [**](#execute)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/mongodb/src/MongoConnection.ts#L178)execute

* ****execute**(query): Promise\<any>

* Overrides Connection.execute

  #### Parameters

  * ##### query: string

  #### Returns Promise\<any>

### [**](#executeDump)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/connections/Connection.ts#L91)inheritedexecuteDump

* ****executeDump**(dump): Promise\<void>

* Inherited from Connection.executeDump

  Execute raw SQL queries, handy from running schema dump loaded from a file. This method doesn't support transactions, as opposed to `orm.schema.execute()`, which is used internally.

  ***

  #### Parameters

  * ##### dump: string

  #### Returns Promise\<void>

### [**](#find)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/mongodb/src/MongoConnection.ts#L182)find

* ****find**\<T>(entityName, where, opts): Promise<[EntityData](https://mikro-orm.io/api/core.md#EntityData)\<T>\[]>

* #### Parameters

  * ##### entityName: [EntityName](https://mikro-orm.io/api/core.md#EntityName)\<T>

  * ##### where: [FilterQuery](https://mikro-orm.io/api/core.md#FilterQuery)\<T>

  * ##### opts: [MongoFindOptions](https://mikro-orm.io/api/mongodb/interface/MongoFindOptions.md)\<T> = <!-- -->{}

  #### Returns Promise<[EntityData](https://mikro-orm.io/api/core.md#EntityData)\<T>\[]>

### [**](#getclient)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/mongodb/src/MongoConnection.ts#L128)getClient

* ****getClient**(): MongoClient

* #### Returns MongoClient

### [**](#getcollection)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/mongodb/src/MongoConnection.ts#L136)getCollection

* ****getCollection**\<T>(name): Collection\<T>

* #### Parameters

  * ##### name: string | [EntityName](https://mikro-orm.io/api/core.md#EntityName)\<T>

  #### Returns Collection\<T>

### [**](#getConnectionOptions)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/connections/Connection.ts#L156)inheritedgetConnectionOptions

* ****getConnectionOptions**(): [ConnectionConfig](https://mikro-orm.io/api/core/interface/ConnectionConfig.md)

* Inherited from Connection.getConnectionOptions

  #### Returns [ConnectionConfig](https://mikro-orm.io/api/core/interface/ConnectionConfig.md)

### [**](#getdb)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/mongodb/src/MongoConnection.ts#L173)getDb

* ****getDb**(): Db

* #### Returns Db

### [**](#getPlatform)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/connections/Connection.ts#L193)inheritedgetPlatform

* ****getPlatform**(): [Platform](https://mikro-orm.io/api/core/class/Platform.md)

* Inherited from Connection.getPlatform

  #### Returns [Platform](https://mikro-orm.io/api/core/class/Platform.md)

### [**](#checkconnection)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/mongodb/src/MongoConnection.ts#L117)checkConnection

* ****checkConnection**(): Promise<{ ok: true } | { error?
  <!-- -->
  : Error; ok: false; reason: string }>

* Overrides Connection.checkConnection

  Are we connected to the database

  ***

  #### Returns Promise<{ ok: true } | { error?<!-- -->: Error; ok: false; reason: string }>

### [**](#insertmany)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/mongodb/src/MongoConnection.ts#L277)insertMany

* ****insertMany**\<T>(entityName, data, ctx): Promise<[QueryResult](https://mikro-orm.io/api/core/interface/QueryResult.md)\<T>>

* #### Parameters

  * ##### entityName: [EntityName](https://mikro-orm.io/api/core.md#EntityName)\<T>

  * ##### data: Partial\<T>\[]

  * ##### optionalctx: ClientSession

  #### Returns Promise<[QueryResult](https://mikro-orm.io/api/core/interface/QueryResult.md)\<T>>

### [**](#insertone)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/mongodb/src/MongoConnection.ts#L269)insertOne

* ****insertOne**\<T>(entityName, data, ctx): Promise<[QueryResult](https://mikro-orm.io/api/core/interface/QueryResult.md)\<T>>

* #### Parameters

  * ##### entityName: [EntityName](https://mikro-orm.io/api/core.md#EntityName)\<T>

  * ##### data: Partial\<T>

  * ##### optionalctx: ClientSession

  #### Returns Promise<[QueryResult](https://mikro-orm.io/api/core/interface/QueryResult.md)\<T>>

### [**](#isconnected)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/mongodb/src/MongoConnection.ts#L108)isConnected

* ****isConnected**(): Promise\<boolean>

* Overrides Connection.isConnected

  Are we connected to the database

  ***

  #### Returns Promise\<boolean>

### [**](#listcollections)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/mongodb/src/MongoConnection.ts#L144)listCollections

* ****listCollections**(): Promise\<string\[]>

* #### Returns Promise\<string\[]>

### [**](#mapoptions)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/mongodb/src/MongoConnection.ts#L153)mapOptions

* ****mapOptions**(overrides): MongoClientOptions

* #### Parameters

  * ##### overrides: MongoClientOptions

  #### Returns MongoClientOptions

### [**](#rollback)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/mongodb/src/MongoConnection.ts#L417)rollback

* ****rollback**(ctx, eventBroadcaster): Promise\<void>

* Overrides Connection.rollback

  #### Parameters

  * ##### ctx: ClientSession

  * ##### optionaleventBroadcaster: [TransactionEventBroadcaster](https://mikro-orm.io/api/core/class/TransactionEventBroadcaster.md)

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

### [**](#stream)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/mongodb/src/MongoConnection.ts#L195)stream

* ****stream**\<T>(entityName, where, opts): AsyncIterableIterator\<T, any, any>

* #### Parameters

  * ##### entityName: [EntityName](https://mikro-orm.io/api/core.md#EntityName)\<T>

  * ##### where: [FilterQuery](https://mikro-orm.io/api/core.md#FilterQuery)\<T>

  * ##### opts: [MongoFindOptions](https://mikro-orm.io/api/mongodb/interface/MongoFindOptions.md)\<T> = <!-- -->{}

  #### Returns AsyncIterableIterator\<T, any, any>

### [**](#streamaggregate)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/mongodb/src/MongoConnection.ts#L333)streamAggregate

* ****streamAggregate**\<T>(entityName, pipeline, ctx, loggerContext, stream): AsyncIterableIterator\<T, any, any>

* #### Parameters

  * ##### entityName: [EntityName](https://mikro-orm.io/api/core.md#EntityName)\<T>

  * ##### pipeline: any\[]

  * ##### optionalctx: ClientSession

  * ##### optionalloggerContext: [LoggingOptions](https://mikro-orm.io/api/core.md#LoggingOptions)

  * ##### stream: boolean = <!-- -->false

  #### Returns AsyncIterableIterator\<T, any, any>

### [**](#transactional)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/mongodb/src/MongoConnection.ts#L364)transactional

* ****transactional**\<T>(cb, options): Promise\<T>

* Overrides Connection.transactional

  #### Parameters

  * ##### cb: (trx) => Promise\<T>

  *

    ##### options: { ctx?<!-- -->: ClientSession; eventBroadcaster?<!-- -->: [TransactionEventBroadcaster](https://mikro-orm.io/api/core/class/TransactionEventBroadcaster.md); isolationLevel?<!-- -->: [IsolationLevel](https://mikro-orm.io/api/core/enum/IsolationLevel.md) } & TransactionOptions = <!-- -->{}

  #### Returns Promise\<T>

### [**](#updatemany)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/mongodb/src/MongoConnection.ts#L285)updateMany

* ****updateMany**\<T>(entityName, where, data, ctx, upsert, upsertOptions): Promise<[QueryResult](https://mikro-orm.io/api/core/interface/QueryResult.md)\<T>>

* #### Parameters

  * ##### entityName: [EntityName](https://mikro-orm.io/api/core.md#EntityName)\<T>

  * ##### where: [FilterQuery](https://mikro-orm.io/api/core.md#FilterQuery)\<T>

  * ##### data: Partial\<T>

  * ##### optionalctx: ClientSession

  * ##### optionalupsert: boolean

  * ##### optionalupsertOptions: [UpsertOptions](https://mikro-orm.io/api/core/interface/UpsertOptions.md)\<T, never>

  #### Returns Promise<[QueryResult](https://mikro-orm.io/api/core/interface/QueryResult.md)\<T>>
