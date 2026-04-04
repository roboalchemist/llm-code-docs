# Source: https://mikro-orm.io/api/migrations/class/MigrationStorage.md

# MigrationStorage<!-- -->

### Implements

* UmzugStorage

## Index[**](#Index)

### Constructors

* [**constructor](#constructor)

### Methods

* [**ensureTable](#ensureTable)
* [**executed](#executed)
* [**getExecutedMigrations](#getExecutedMigrations)
* [**logMigration](#logMigration)
* [**setMasterMigration](#setMasterMigration)
* [**unlogMigration](#unlogMigration)
* [**unsetMasterMigration](#unsetMasterMigration)

## Constructors<!-- -->[**](#Constructors)

### [**](#constructor)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/migrations/src/MigrationStorage.ts#L13)constructor

* ****new MigrationStorage**(driver, options): [MigrationStorage](https://mikro-orm.io/api/migrations/class/MigrationStorage.md)

- #### Parameters

  * ##### driver: [AbstractSqlDriver](https://mikro-orm.io/api/knex/class/AbstractSqlDriver.md)<[AbstractSqlConnection](https://mikro-orm.io/api/knex/class/AbstractSqlConnection.md), [AbstractSqlPlatform](https://mikro-orm.io/api/knex/class/AbstractSqlPlatform.md)>
  * ##### options: [MigrationsOptions](https://mikro-orm.io/api/core.md#MigrationsOptions)

  #### Returns [MigrationStorage](https://mikro-orm.io/api/migrations/class/MigrationStorage.md)

## Methods<!-- -->[**](#Methods)

### [**](#ensureTable)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/migrations/src/MigrationStorage.ts#L62)ensureTable

* ****ensureTable**(): Promise\<void>

- #### Returns Promise\<void>

### [**](#executed)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/migrations/src/MigrationStorage.ts#L19)executed

* ****executed**(): Promise\<string\[]>

- Implementation of UmzugStorage.executed

  Gets list of executed migrations.

  ***

  #### Returns Promise\<string\[]>

### [**](#getExecutedMigrations)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/migrations/src/MigrationStorage.ts#L43)getExecutedMigrations

* ****getExecutedMigrations**(): Promise<[MigrationRow](https://mikro-orm.io/api/core.md#MigrationRow)\[]>

- #### Returns Promise<[MigrationRow](https://mikro-orm.io/api/core.md#MigrationRow)\[]>

### [**](#logMigration)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/migrations/src/MigrationStorage.ts#L24)logMigration

* ****logMigration**(params): Promise\<void>

- Implementation of UmzugStorage.logMigration

  Logs migration to be considered as executed.

  ***

  #### Parameters

  * ##### params: MigrationParams\<any>

  #### Returns Promise\<void>

### [**](#setMasterMigration)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/migrations/src/MigrationStorage.ts#L88)setMasterMigration

* ****setMasterMigration**(trx): void

- #### Parameters

  * ##### trx: any

  #### Returns void

### [**](#unlogMigration)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/migrations/src/MigrationStorage.ts#L30)unlogMigration

* ****unlogMigration**(params): Promise\<void>

- Implementation of UmzugStorage.unlogMigration

  Unlogs migration (makes it to be considered as pending).

  ***

  #### Parameters

  * ##### params: MigrationParams\<any>

  #### Returns Promise\<void>

### [**](#unsetMasterMigration)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/migrations/src/MigrationStorage.ts#L92)unsetMasterMigration

* ****unsetMasterMigration**(): void

- #### Returns void
