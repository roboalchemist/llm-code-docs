# Source: https://mikro-orm.io/api/migrations/class/MigrationRunner.md

# MigrationRunner<!-- -->

## Index[**](#Index)

### Constructors

* [**constructor](#constructor)

### Methods

* [**run](#run)
* [**setMasterMigration](#setMasterMigration)
* [**unsetMasterMigration](#unsetMasterMigration)

## Constructors<!-- -->[**](#Constructors)

### [**](#constructor)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/migrations/src/MigrationRunner.ts#L11)constructor

* ****new MigrationRunner**(driver, options, config): [MigrationRunner](https://mikro-orm.io/api/migrations/class/MigrationRunner.md)

- #### Parameters

  * ##### driver: [AbstractSqlDriver](https://mikro-orm.io/api/knex/class/AbstractSqlDriver.md)<[AbstractSqlConnection](https://mikro-orm.io/api/knex/class/AbstractSqlConnection.md), [AbstractSqlPlatform](https://mikro-orm.io/api/knex/class/AbstractSqlPlatform.md)>
  * ##### options: [MigrationsOptions](https://mikro-orm.io/api/core.md#MigrationsOptions)
  * ##### config: [Configuration](https://mikro-orm.io/api/core/class/Configuration.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>, [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>>>

  #### Returns [MigrationRunner](https://mikro-orm.io/api/migrations/class/MigrationRunner.md)

## Methods<!-- -->[**](#Methods)

### [**](#run)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/migrations/src/MigrationRunner.ts#L18)run

* ****run**(migration, method): Promise\<void>

- #### Parameters

  * ##### migration: [Migration](https://mikro-orm.io/api/migrations/class/Migration.md)
  * ##### method: up | down

  #### Returns Promise\<void>

### [**](#setMasterMigration)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/migrations/src/MigrationRunner.ts#L33)setMasterMigration

* ****setMasterMigration**(trx): void

- #### Parameters

  * ##### trx: any

  #### Returns void

### [**](#unsetMasterMigration)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/migrations/src/MigrationRunner.ts#L37)unsetMasterMigration

* ****unsetMasterMigration**(): void

- #### Returns void
