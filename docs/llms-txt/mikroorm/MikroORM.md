# Source: https://mikro-orm.io/api/sqlite/class/MikroORM.md

# Source: https://mikro-orm.io/api/postgresql/class/MikroORM.md

# Source: https://mikro-orm.io/api/oracledb/class/MikroORM.md

# Source: https://mikro-orm.io/api/mysql/class/MikroORM.md

# Source: https://mikro-orm.io/api/mssql/class/MikroORM.md

# Source: https://mikro-orm.io/api/mongodb/class/MikroORM.md

# Source: https://mikro-orm.io/api/mariadb/class/MikroORM.md

# Source: https://mikro-orm.io/api/libsql/class/MikroORM.md

# Source: https://mikro-orm.io/api/core/class/MikroORM.md

# MikroORM<!-- --> \<Driver, EM, Entities>

The main class used to configure and bootstrap the ORM.

* **@example**

  ```
  // import from driver package
  import { MikroORM, defineEntity, p } from '@mikro-orm/sqlite';

  const User = defineEntity({
    name: 'User',
    properties: {
      id: p.integer().primary(),
      name: p.string(),
    },
  });

  const orm = new MikroORM({
    entities: [User],
    dbName: 'my.db',
  });
  await orm.schema.update();

  const em = orm.em.fork();
  const u1 = em.create(User, { name: 'John' });
  const u2 = em.create(User, { name: 'Ben' });
  await em.flush();
  ```

### Hierarchy

* *MikroORM*

  * [MikroORM](https://mikro-orm.io/api/postgresql/class/MikroORM.md)
  * [MikroORM](https://mikro-orm.io/api/mysql/class/MikroORM.md)
  * [MikroORM](https://mikro-orm.io/api/mariadb/class/MikroORM.md)
  * [MikroORM](https://mikro-orm.io/api/sqlite/class/MikroORM.md)
  * [MikroORM](https://mikro-orm.io/api/libsql/class/MikroORM.md)
  * [MikroORM](https://mikro-orm.io/api/mssql/class/MikroORM.md)
  * [MikroORM](https://mikro-orm.io/api/oracledb/class/MikroORM.md)
  * [MikroORM](https://mikro-orm.io/api/mongodb/class/MikroORM.md)

## Index[**](#index)

### Constructors

* [**constructor](#constructor)

### Properties

* [**config](#config)
* [**driver](#driver)
* [**em](#em)

### Accessors

* [**entityGenerator](#entitygenerator)
* [**migrator](#migrator)
* [**seeder](#seeder)
* [**schema](#schema)

### Methods

* [**close](#close)
* [**connect](#connect)
* [**discoverEntity](#discoverentity)
* [**getMetadata](#getmetadata)
* [**checkConnection](#checkconnection)
* [**isConnected](#isconnected)
* [**reconnect](#reconnect)
* [**init](#init)

## Constructors<!-- -->[**](#constructors)

### [**](#constructor)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/MikroORM.ts#L150)constructor

* ****new MikroORM**\<Driver, EM, Entities>(options): [MikroORM](https://mikro-orm.io/api/core/class/MikroORM.md)\<Driver, EM, Entities>

* Synchronous variant of the `init` method with some limitations:

  * folder-based discovery not supported
  * ORM extensions are not autoloaded
  * when metadata cache is enabled, `FileCacheAdapter` needs to be explicitly set in the config

  ***

  #### Parameters

  * ##### options: Partial<[Options](https://mikro-orm.io/api/core/interface/Options.md)\<Driver, EM, Entities>>

  #### Returns [MikroORM](https://mikro-orm.io/api/core/class/MikroORM.md)\<Driver, EM, Entities>

## Properties<!-- -->[**](#properties)

### [**](#config)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/MikroORM.ts#L109)readonlyconfig

**config: [Configuration](https://mikro-orm.io/api/core/class/Configuration.md)\<Driver, Driver\[typeof [EntityManagerType](https://mikro-orm.io/api/core.md#EntityManagerType)] & [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)\<Driver>>

### [**](#driver)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/MikroORM.ts#L108)readonlydriver

**driver: Driver

### [**](#em)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/MikroORM.ts#L107)em

**em: EM & { \~entities?

<!-- -->

: Entities }

The global EntityManager instance. If you are using `RequestContext` helper, it will automatically pick the request specific context under the hood

## Accessors<!-- -->[**](#accessors)

### [**](#entitygenerator)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/MikroORM.ts#L287)entityGenerator

* **get entityGenerator(): [IEntityGenerator](https://mikro-orm.io/api/core/interface/IEntityGenerator.md)

* Gets the EntityGenerator.

  ***

  #### Returns [IEntityGenerator](https://mikro-orm.io/api/core/interface/IEntityGenerator.md)

### [**](#migrator)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/MikroORM.ts#L280)migrator

* **get migrator(): [IMigrator](https://mikro-orm.io/api/core/interface/IMigrator.md)

* Gets the Migrator.

  ***

  #### Returns [IMigrator](https://mikro-orm.io/api/core/interface/IMigrator.md)

### [**](#seeder)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/MikroORM.ts#L273)seeder

* **get seeder(): [ISeedManager](https://mikro-orm.io/api/core/interface/ISeedManager.md)

* Gets the SeedManager

  ***

  #### Returns [ISeedManager](https://mikro-orm.io/api/core/interface/ISeedManager.md)

### [**](#schema)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/MikroORM.ts#L266)schema

* **get schema(): ReturnType\<ReturnType\<Driver\[getPlatform]>\[getSchemaGenerator]>

* Gets the SchemaGenerator.

  ***

  #### Returns ReturnType\<ReturnType\<Driver\[getPlatform]>\[getSchemaGenerator]>

## Methods<!-- -->[**](#methods)

### [**](#close)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/MikroORM.ts#L208)close

* ****close**(force): Promise\<void>

* Closes the database connection.

  ***

  #### Parameters

  * ##### force: boolean = <!-- -->false

  #### Returns Promise\<void>

### [**](#connect)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/MikroORM.ts#L174)connect

* ****connect**(): Promise\<Driver>

* Connects to the database.

  ***

  #### Returns Promise\<Driver>

### [**](#discoverentity)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/MikroORM.ts#L246)discoverEntity

* ****discoverEntity**\<T>(entities, reset): void

* Allows dynamically discovering new entity by reference, handy for testing schema diffing.

  ***

  #### Parameters

  * ##### entities: T | T\[]

  * ##### optionalreset: [EntityName](https://mikro-orm.io/api/core.md#EntityName) | [EntityName](https://mikro-orm.io/api/core.md#EntityName)\[]

  #### Returns void

### [**](#getmetadata)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/MikroORM.ts#L217)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/MikroORM.ts#L222)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/MikroORM.ts#L227)getMetadata

* ****getMetadata**(): [MetadataStorage](https://mikro-orm.io/api/core/class/MetadataStorage.md)
* ****getMetadata**\<Entity>(entityName): [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<Entity, [EntityCtor](https://mikro-orm.io/api/core.md#EntityCtor)\<Entity>>

* Gets the `MetadataStorage`.

  ***

  #### Returns [MetadataStorage](https://mikro-orm.io/api/core/class/MetadataStorage.md)

### [**](#checkconnection)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/MikroORM.ts#L201)checkConnection

* ****checkConnection**(): Promise<{ ok: true } | { error?
  <!-- -->
  : Error; ok: false; reason: string }>

* Checks whether the database connection is active, returns the reason if not.

  ***

  #### Returns Promise<{ ok: true } | { error?<!-- -->: Error; ok: false; reason: string }>

### [**](#isconnected)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/MikroORM.ts#L194)isConnected

* ****isConnected**(): Promise\<boolean>

* Checks whether the database connection is active.

  ***

  #### Returns Promise\<boolean>

### [**](#reconnect)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/MikroORM.ts#L182)reconnect

* ****reconnect**(options): Promise\<void>

* Reconnects, possibly to a different database.

  ***

  #### Parameters

  * ##### options: Partial<[Options](https://mikro-orm.io/api/core/interface/Options.md)\<Driver, EM, Entities>> = <!-- -->{}

  #### Returns Promise\<void>

### [**](#init)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/MikroORM.ts#L118)staticinit

* ****init**\<D, EM, Entities>(options): Promise<[MikroORM](https://mikro-orm.io/api/core/class/MikroORM.md)\<D, EM, Entities>>

* Initialize the ORM, load entity metadata, create EntityManager and connect to the database. If you omit the `options` parameter, your CLI config will be used.

  ***

  #### Parameters

  * ##### options: Partial<[Options](https://mikro-orm.io/api/core/interface/Options.md)\<D, EM, Entities>>

  #### Returns Promise<[MikroORM](https://mikro-orm.io/api/core/class/MikroORM.md)\<D, EM, Entities>>
