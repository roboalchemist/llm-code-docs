# Source: https://mikro-orm.io/api/migrations/class/MigrationRunner.md

# MigrationRunner<!-- -->

## Index[**](#index)

### Constructors

* [**constructor](#constructor)

### Methods

* [**run](#run)
* [**setMasterMigration](#setmastermigration)
* [**unsetMasterMigration](#unsetmastermigration)

## Constructors<!-- -->[**](#constructors)

### [**](#constructor)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/migrations/src/MigrationRunner.ts#L10)constructor

* ****new MigrationRunner**(driver, options, config): [MigrationRunner](https://mikro-orm.io/api/migrations/class/MigrationRunner.md)

* #### Parameters

  * ##### driver: [AbstractSqlDriver](https://mikro-orm.io/api/sql/class/AbstractSqlDriver.md)<[AbstractSqlConnection](https://mikro-orm.io/api/sql/class/AbstractSqlConnection.md), [AbstractSqlPlatform](https://mikro-orm.io/api/sql/class/AbstractSqlPlatform.md)>

  * ##### options: [MigrationsOptions](https://mikro-orm.io/api/core.md#MigrationsOptions)

  * ##### config: [Configuration](https://mikro-orm.io/api/core/class/Configuration.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>, [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>>>

  #### Returns [MigrationRunner](https://mikro-orm.io/api/migrations/class/MigrationRunner.md)

## Methods<!-- -->[**](#methods)

### [**](#run)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/migrations/src/MigrationRunner.ts#L19)run

* ****run**(migration, method): Promise\<void>

* #### Parameters

  * ##### migration: [Migration](https://mikro-orm.io/api/migrations/class/Migration.md)

  * ##### method: up | down

  #### Returns Promise\<void>

### [**](#setmastermigration)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/migrations/src/MigrationRunner.ts#L37)setMasterMigration

* ****setMasterMigration**(trx): void

* #### Parameters

  * ##### trx: any

  #### Returns void

### [**](#unsetmastermigration)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/migrations/src/MigrationRunner.ts#L41)unsetMasterMigration

* ****unsetMasterMigration**(): void

* #### Returns void
