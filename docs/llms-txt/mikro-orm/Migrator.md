# Source: https://mikro-orm.io/api/migrations/class/Migrator.md

# Migrator<!-- -->

### Implements

* [IMigrator](https://mikro-orm.io/api/core/interface/IMigrator.md)

## Index[**](#Index)

### Constructors

* [**constructor](#constructor)

### Methods

* [**checkMigrationNeeded](#checkMigrationNeeded)
* [**createInitialMigration](#createInitialMigration)
* [**createMigration](#createMigration)
* [**down](#down)
* [**getExecutedMigrations](#getExecutedMigrations)
* [**getPendingMigrations](#getPendingMigrations)
* [**off](#off)
* [**on](#on)
* [**up](#up)
* [**register](#register)

## Constructors<!-- -->[**](#Constructors)

### [**](#constructor)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/migrations/src/Migrator.ts#L47)constructor

* ****new Migrator**(em): [Migrator](https://mikro-orm.io/api/migrations/class/Migrator.md)

- #### Parameters

  * ##### em: [SqlEntityManager](https://mikro-orm.io/api/knex/class/EntityManager.md)<[AbstractSqlDriver](https://mikro-orm.io/api/knex/class/AbstractSqlDriver.md)<[AbstractSqlConnection](https://mikro-orm.io/api/knex/class/AbstractSqlConnection.md), [AbstractSqlPlatform](https://mikro-orm.io/api/knex/class/AbstractSqlPlatform.md)>>

  #### Returns [Migrator](https://mikro-orm.io/api/migrations/class/Migrator.md)

## Methods<!-- -->[**](#Methods)

### [**](#checkMigrationNeeded)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/migrations/src/Migrator.ts#L95)checkMigrationNeeded

* ****checkMigrationNeeded**(): Promise\<boolean>

- Implementation of IMigrator.checkMigrationNeeded

  Checks current schema for changes.

  ***

  #### Returns Promise\<boolean>

### [**](#createInitialMigration)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/migrations/src/Migrator.ts#L104)createInitialMigration

* ****createInitialMigration**(path, name, blank): Promise<[MigrationResult](https://mikro-orm.io/api/core.md#MigrationResult)>

- Implementation of IMigrator.createInitialMigration

  Creates initial migration. This generates the schema based on metadata, and checks whether all the tables are already present. If yes, it will also automatically log the migration as executed. Initial migration can be created only if the schema is already aligned with the metadata, or when no schema is present - in such case regular migration would have the same effect.

  ***

  #### Parameters

  * ##### optionalpath: string
  * ##### optionalname: string
  * ##### blank: boolean = <!-- -->false

  #### Returns Promise<[MigrationResult](https://mikro-orm.io/api/core.md#MigrationResult)>

### [**](#createMigration)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/migrations/src/Migrator.ts#L73)createMigration

* ****createMigration**(path, blank, initial, name): Promise<[MigrationResult](https://mikro-orm.io/api/core.md#MigrationResult)>

- Implementation of IMigrator.createMigration

  Checks current schema for changes, generates new migration if there are any.

  ***

  #### Parameters

  * ##### optionalpath: string
  * ##### blank: boolean = <!-- -->false
  * ##### initial: boolean = <!-- -->false
  * ##### optionalname: string

  #### Returns Promise<[MigrationResult](https://mikro-orm.io/api/core.md#MigrationResult)>

### [**](#down)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/migrations/src/Migrator.ts#L264)down

* ****down**(options): Promise<[UmzugMigration](https://mikro-orm.io/api/core.md#UmzugMigration)\[]>

- Implementation of IMigrator.down

  Executes down migrations to the given point. Without parameter it will migrate one version down.

  ***

  #### Parameters

  * ##### optionaloptions: string | string\[] | [MigrateOptions](https://mikro-orm.io/api/core.md#MigrateOptions)

  #### Returns Promise<[UmzugMigration](https://mikro-orm.io/api/core.md#UmzugMigration)\[]>

### [**](#getExecutedMigrations)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/migrations/src/Migrator.ts#L229)getExecutedMigrations

* ****getExecutedMigrations**(): Promise<[MigrationRow](https://mikro-orm.io/api/core.md#MigrationRow)\[]>

- Implementation of IMigrator.getExecutedMigrations

  Returns list of already executed migrations.

  ***

  #### Returns Promise<[MigrationRow](https://mikro-orm.io/api/core.md#MigrationRow)\[]>

### [**](#getPendingMigrations)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/migrations/src/Migrator.ts#L249)getPendingMigrations

* ****getPendingMigrations**(): Promise<[UmzugMigration](https://mikro-orm.io/api/core.md#UmzugMigration)\[]>

- Implementation of IMigrator.getPendingMigrations

  Returns list of pending (not yet executed) migrations found in the migration directory.

  ***

  #### Returns Promise<[UmzugMigration](https://mikro-orm.io/api/core.md#UmzugMigration)\[]>

### [**](#off)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/migrations/src/Migrator.ts#L133)off

* ****off**(eventName, listener): this

- Implementation of IMigrator.off

  Removes event handler.

  ***

  #### Parameters

  * ##### eventName: [MigratorEvent](https://mikro-orm.io/api/core.md#MigratorEvent)
  * ##### listener: (event) => [MaybePromise](https://mikro-orm.io/api/core.md#MaybePromise)\<void>


  #### Returns this

### [**](#on)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/migrations/src/Migrator.ts#L125)on

* ****on**(eventName, listener): this

- Implementation of IMigrator.on

  Registers event handler.

  ***

  #### Parameters

  * ##### eventName: [MigratorEvent](https://mikro-orm.io/api/core.md#MigratorEvent)
  * ##### listener: (event) => [MaybePromise](https://mikro-orm.io/api/core.md#MaybePromise)\<void>


  #### Returns this

### [**](#up)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/migrations/src/Migrator.ts#L257)up

* ****up**(options): Promise<[UmzugMigration](https://mikro-orm.io/api/core.md#UmzugMigration)\[]>

- Implementation of IMigrator.up

  Executes specified migrations. Without parameter it will migrate up to the latest version.

  ***

  #### Parameters

  * ##### optionaloptions: string | string\[] | [MigrateOptions](https://mikro-orm.io/api/core.md#MigrateOptions)

  #### Returns Promise<[UmzugMigration](https://mikro-orm.io/api/core.md#UmzugMigration)\[]>

### [**](#register)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/migrations/src/Migrator.ts#L66)staticregister

* ****register**(orm): void

- #### Parameters

  * ##### orm: [MikroORM](https://mikro-orm.io/api/core/class/MikroORM.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>, [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>>>

  #### Returns void
