# Source: https://mikro-orm.io/api/core/interface/IMigrator.md

# IMigrator<!-- -->

### Implemented by

* [Migrator](https://mikro-orm.io/api/migrations/class/Migrator.md)

## Index[**](#Index)

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

## Methods<!-- -->[**](#Methods)

### [**](#checkMigrationNeeded)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L991)checkMigrationNeeded

* ****checkMigrationNeeded**(): Promise\<boolean>

- Checks current schema for changes.

  ***

  #### Returns Promise\<boolean>

### [**](#createInitialMigration)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L999)createInitialMigration

* ****createInitialMigration**(path): Promise<[MigrationResult](https://mikro-orm.io/api/core.md#MigrationResult)>

- Creates initial migration. This generates the schema based on metadata, and checks whether all the tables are already present. If yes, it will also automatically log the migration as executed. Initial migration can be created only if the schema is already aligned with the metadata, or when no schema is present - in such case regular migration would have the same effect.

  ***

  #### Parameters

  * ##### optionalpath: string

  #### Returns Promise<[MigrationResult](https://mikro-orm.io/api/core.md#MigrationResult)>

### [**](#createMigration)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L986)createMigration

* ****createMigration**(path, blank, initial, name): Promise<[MigrationResult](https://mikro-orm.io/api/core.md#MigrationResult)>

- Checks current schema for changes, generates new migration if there are any.

  ***

  #### Parameters

  * ##### optionalpath: string
  * ##### optionalblank: boolean
  * ##### optionalinitial: boolean
  * ##### optionalname: string

  #### Returns Promise<[MigrationResult](https://mikro-orm.io/api/core.md#MigrationResult)>

### [**](#down)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L1019)down

* ****down**(options): Promise<[UmzugMigration](https://mikro-orm.io/api/core.md#UmzugMigration)\[]>

- Executes down migrations to the given point. Without parameter it will migrate one version down.

  ***

  #### Parameters

  * ##### optionaloptions: string | string\[] | [MigrateOptions](https://mikro-orm.io/api/core.md#MigrateOptions)

  #### Returns Promise<[UmzugMigration](https://mikro-orm.io/api/core.md#UmzugMigration)\[]>

### [**](#getExecutedMigrations)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L1004)getExecutedMigrations

* ****getExecutedMigrations**(): Promise<[MigrationRow](https://mikro-orm.io/api/core.md#MigrationRow)\[]>

- Returns list of already executed migrations.

  ***

  #### Returns Promise<[MigrationRow](https://mikro-orm.io/api/core.md#MigrationRow)\[]>

### [**](#getPendingMigrations)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L1009)getPendingMigrations

* ****getPendingMigrations**(): Promise<[UmzugMigration](https://mikro-orm.io/api/core.md#UmzugMigration)\[]>

- Returns list of pending (not yet executed) migrations found in the migration directory.

  ***

  #### Returns Promise<[UmzugMigration](https://mikro-orm.io/api/core.md#UmzugMigration)\[]>

### [**](#off)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L1029)off

* ****off**(event, listener): [IMigrator](https://mikro-orm.io/api/core/interface/IMigrator.md)

- Removes event handler.

  ***

  #### Parameters

  * ##### event: [MigratorEvent](https://mikro-orm.io/api/core.md#MigratorEvent)
  * ##### listener: (event) => [MaybePromise](https://mikro-orm.io/api/core.md#MaybePromise)\<void>


  #### Returns [IMigrator](https://mikro-orm.io/api/core/interface/IMigrator.md)

### [**](#on)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L1024)on

* ****on**(event, listener): [IMigrator](https://mikro-orm.io/api/core/interface/IMigrator.md)

- Registers event handler.

  ***

  #### Parameters

  * ##### event: [MigratorEvent](https://mikro-orm.io/api/core.md#MigratorEvent)
  * ##### listener: (event) => [MaybePromise](https://mikro-orm.io/api/core.md#MaybePromise)\<void>


  #### Returns [IMigrator](https://mikro-orm.io/api/core/interface/IMigrator.md)

### [**](#up)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L1014)up

* ****up**(options): Promise<[UmzugMigration](https://mikro-orm.io/api/core.md#UmzugMigration)\[]>

- Executes specified migrations. Without parameter it will migrate up to the latest version.

  ***

  #### Parameters

  * ##### optionaloptions: string | string\[] | [MigrateOptions](https://mikro-orm.io/api/core.md#MigrateOptions)

  #### Returns Promise<[UmzugMigration](https://mikro-orm.io/api/core.md#UmzugMigration)\[]>
