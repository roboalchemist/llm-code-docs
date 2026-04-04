# Source: https://mikro-orm.io/api/sqlite/class/MikroORM.md

# Source: https://mikro-orm.io/api/postgresql/class/MikroORM.md

# Source: https://mikro-orm.io/api/mysql/class/MikroORM.md

# Source: https://mikro-orm.io/api/mssql/class/MikroORM.md

# Source: https://mikro-orm.io/api/mongodb/class/MikroORM.md

# Source: https://mikro-orm.io/api/mariadb/class/MikroORM.md

# Source: https://mikro-orm.io/api/libsql/class/MikroORM.md

# Source: https://mikro-orm.io/api/core/class/MikroORM.md

# Source: https://mikro-orm.io/api/better-sqlite/class/MikroORM.md

# MikroORM<!-- --> \<EM>

Helper class for bootstrapping the MikroORM.

### Hierarchy

* [MikroORM](https://mikro-orm.io/api/core/class/MikroORM.md)<[BetterSqliteDriver](https://mikro-orm.io/api/better-sqlite/class/BetterSqliteDriver.md), EM>
  * *MikroORM*

## Index[**](#Index)

### Constructors

* [**constructor](#constructor)

### Properties

* [**config](#config)
* [**em](#em)

### Accessors

* [**entityGenerator](#entityGenerator)
* [**migrator](#migrator)
* [**schema](#schema)
* [**seeder](#seeder)

### Methods

* [**checkConnection](#checkConnection)
* [**close](#close)
* [**connect](#connect)
* [**discoverEntities](#discoverEntities)
* [**discoverEntitiesSync](#discoverEntitiesSync)
* [**discoverEntity](#discoverEntity)
* [**getEntityGenerator](#getEntityGenerator)
* [**getMetadata](#getMetadata)
* [**getMigrator](#getMigrator)
* [**getSchemaGenerator](#getSchemaGenerator)
* [**getSeeder](#getSeeder)
* [**isConnected](#isConnected)
* [**reconnect](#reconnect)
* [**init](#init)
* [**initSync](#initSync)

## Constructors<!-- -->[**](#Constructors)

### [**](#constructor)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/MikroORM.ts#L114)constructor

* ****new MikroORM**\<EM>(options): [BetterSqliteMikroORM](https://mikro-orm.io/api/better-sqlite/class/MikroORM.md)\<EM>

- Inherited from MikroORM.constructor

  #### Parameters

  * ##### options: [Options](https://mikro-orm.io/api/core.md#Options)<[BetterSqliteDriver](https://mikro-orm.io/api/better-sqlite/class/BetterSqliteDriver.md), EM> | [Configuration](https://mikro-orm.io/api/core/class/Configuration.md)<[BetterSqliteDriver](https://mikro-orm.io/api/better-sqlite/class/BetterSqliteDriver.md), EM>

  #### Returns [BetterSqliteMikroORM](https://mikro-orm.io/api/better-sqlite/class/MikroORM.md)\<EM>

## Properties<!-- -->[**](#Properties)

### [**](#config)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/MikroORM.ts#L16)readonlyinheritedconfig

**config: [Configuration](https://mikro-orm.io/api/core/class/Configuration.md)<[BetterSqliteDriver](https://mikro-orm.io/api/better-sqlite/class/BetterSqliteDriver.md), [SqlEntityManager](https://mikro-orm.io/api/knex/class/EntityManager.md)<[BetterSqliteDriver](https://mikro-orm.io/api/better-sqlite/class/BetterSqliteDriver.md)> & [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>>>

Inherited from MikroORM.config

### [**](#em)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/MikroORM.ts#L15)inheritedem

**em: EM

Inherited from MikroORM.em

The global EntityManager instance. If you are using `RequestContext` helper, it will automatically pick the request specific context under the hood

## Accessors<!-- -->[**](#Accessors)

### [**](#entityGenerator)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/MikroORM.ts#L322)inheritedentityGenerator

* **get entityGenerator(): [IEntityGenerator](https://mikro-orm.io/api/core/interface/IEntityGenerator.md)

- Inherited from MikroORM.entityGenerator

  Shortcut for `orm.getEntityGenerator()`

  ***

  #### Returns [IEntityGenerator](https://mikro-orm.io/api/core/interface/IEntityGenerator.md)

### [**](#migrator)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/MikroORM.ts#L315)inheritedmigrator

* **get migrator(): [IMigrator](https://mikro-orm.io/api/core/interface/IMigrator.md)

- Inherited from MikroORM.migrator

  Shortcut for `orm.getMigrator()`

  ***

  #### Returns [IMigrator](https://mikro-orm.io/api/core/interface/IMigrator.md)

### [**](#schema)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/MikroORM.ts#L301)inheritedschema

* **get schema(): ReturnType\<ReturnType\<D\[getPlatform]>\[getSchemaGenerator]>

- Inherited from MikroORM.schema

  Shortcut for `orm.getSchemaGenerator()`

  ***

  #### Returns ReturnType\<ReturnType\<D\[getPlatform]>\[getSchemaGenerator]>

### [**](#seeder)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/MikroORM.ts#L308)inheritedseeder

* **get seeder(): [ISeedManager](https://mikro-orm.io/api/core/interface/ISeedManager.md)

- Inherited from MikroORM.seeder

  Shortcut for `orm.getSeeder()`

  ***

  #### Returns [ISeedManager](https://mikro-orm.io/api/core/interface/ISeedManager.md)

## Methods<!-- -->[**](#Methods)

### [**](#checkConnection)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/MikroORM.ts#L179)inheritedcheckConnection

* ****checkConnection**(): Promise<{ ok: true } | { error?
  <!-- -->
  : Error; ok: false; reason: string }>

- Inherited from MikroORM.checkConnection

  Checks whether the database connection is active, returns .

  ***

  #### Returns Promise<{ ok: true } | { error?<!-- -->: Error; ok: false; reason: string }>

### [**](#close)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/MikroORM.ts#L186)inheritedclose

* ****close**(force): Promise\<void>

- Inherited from MikroORM.close

  Closes the database connection.

  ***

  #### Parameters

  * ##### force: boolean = <!-- -->false

  #### Returns Promise\<void>

### [**](#connect)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/MikroORM.ts#L137)inheritedconnect

* ****connect**(): Promise<[BetterSqliteDriver](https://mikro-orm.io/api/better-sqlite/class/BetterSqliteDriver.md)>

- Inherited from MikroORM.connect

  Connects to the database.

  ***

  #### Returns Promise<[BetterSqliteDriver](https://mikro-orm.io/api/better-sqlite/class/BetterSqliteDriver.md)>

### [**](#discoverEntities)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/MikroORM.ts#L223)inheriteddiscoverEntities

* ****discoverEntities**(): Promise\<void>

- Inherited from MikroORM.discoverEntities

  #### Returns Promise\<void>

### [**](#discoverEntitiesSync)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/MikroORM.ts#L228)inheriteddiscoverEntitiesSync

* ****discoverEntitiesSync**(): void

- Inherited from MikroORM.discoverEntitiesSync

  #### Returns void

### [**](#discoverEntity)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/MikroORM.ts#L244)inheriteddiscoverEntity

* ****discoverEntity**\<T>(entities, reset): void

- Inherited from MikroORM.discoverEntity

  Allows dynamically discovering new entity by reference, handy for testing schema diffing.

  ***

  #### Parameters

  * ##### entities: T | T\[]
  * ##### optionalreset: string | string\[]

  #### Returns void

### [**](#getEntityGenerator)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/MikroORM.ts#L280)inheritedgetEntityGenerator

* ****getEntityGenerator**\<T>(): T

- Inherited from MikroORM.getEntityGenerator

  Gets the EntityGenerator.

  ***

  #### Returns T

### [**](#getMetadata)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/MikroORM.ts#L204)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/MikroORM.ts#L209)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/MikroORM.ts#L214)inheritedgetMetadata

* ****getMetadata**(): [MetadataStorage](https://mikro-orm.io/api/core/class/MetadataStorage.md)
* ****getMetadata**\<Entity>(entityName): [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<Entity>

- Inherited from MikroORM.getMetadata

  Gets the `MetadataStorage`.

  ***

  #### Returns [MetadataStorage](https://mikro-orm.io/api/core/class/MetadataStorage.md)

### [**](#getMigrator)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/MikroORM.ts#L287)inheritedgetMigrator

* ****getMigrator**\<T>(): T

- Inherited from MikroORM.getMigrator

  Gets the Migrator.

  ***

  #### Returns T

### [**](#getSchemaGenerator)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/MikroORM.ts#L266)inheritedgetSchemaGenerator

* ****getSchemaGenerator**(): [SqlSchemaGenerator](https://mikro-orm.io/api/knex/class/SqlSchemaGenerator.md)

- Inherited from MikroORM.getSchemaGenerator

  Gets the SchemaGenerator.

  ***

  #### Returns [SqlSchemaGenerator](https://mikro-orm.io/api/knex/class/SqlSchemaGenerator.md)

### [**](#getSeeder)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/MikroORM.ts#L294)inheritedgetSeeder

* ****getSeeder**\<T>(): T

- Inherited from MikroORM.getSeeder

  Gets the SeedManager

  ***

  #### Returns T

### [**](#isConnected)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/MikroORM.ts#L172)inheritedisConnected

* ****isConnected**(): Promise\<boolean>

- Inherited from MikroORM.isConnected

  Checks whether the database connection is active.

  ***

  #### Returns Promise\<boolean>

### [**](#reconnect)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/MikroORM.ts#L160)inheritedreconnect

* ****reconnect**(options): Promise\<void>

- Inherited from MikroORM.reconnect

  Reconnects, possibly to a different database.

  ***

  #### Parameters

  * ##### options: [Options](https://mikro-orm.io/api/core.md#Options) = <!-- -->{}

  #### Returns Promise\<void>

### [**](#init)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/better-sqlite/src/BetterSqliteMikroORM.ts#L22)staticinit

* ****init**\<D, EM>(options): Promise<[MikroORM](https://mikro-orm.io/api/core/class/MikroORM.md)\<D, EM>>

- Overrides MikroORM.init

  Initialize the ORM, load entity metadata, create EntityManager and connect to the database. If you omit the `options` parameter, your CLI config will be used.

  ***

  #### Parameters

  * ##### optionaloptions: [Options](https://mikro-orm.io/api/core.md#Options)\<D, EM>

  #### Returns Promise<[MikroORM](https://mikro-orm.io/api/core/class/MikroORM.md)\<D, EM>>

### [**](#initSync)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/better-sqlite/src/BetterSqliteMikroORM.ts#L29)staticinitSync

* ****initSync**\<D, EM>(options): [MikroORM](https://mikro-orm.io/api/core/class/MikroORM.md)\<D, EM>

- Overrides MikroORM.initSync

  Synchronous variant of the `init` method with some limitations:

  * database connection will be established when you first interact with the database (or you can use `orm.connect()` explicitly)
  * no loading of the `config` file, `options` parameter is mandatory
  * no support for folder based discovery
  * no check for mismatched package versions

  ***

  #### Parameters

  * ##### options: [Options](https://mikro-orm.io/api/core.md#Options)\<D, EM>

  #### Returns [MikroORM](https://mikro-orm.io/api/core/class/MikroORM.md)\<D, EM>
