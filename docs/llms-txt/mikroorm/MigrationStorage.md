# Source: https://mikro-orm.io/api/migrations/class/MigrationStorage.md

# MigrationStorage<!-- -->

## Index[**](#index)

### Constructors

* [**constructor](#constructor)

### Methods

* [**ensureTable](#ensuretable)
* [**executed](#executed)
* [**getExecutedMigrations](#getexecutedmigrations)
* [**logMigration](#logmigration)
* [**setMasterMigration](#setmastermigration)
* [**unlogMigration](#unlogmigration)
* [**unsetMasterMigration](#unsetmastermigration)

## Constructors<!-- -->[**](#constructors)

### [**](#constructor)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/migrations/src/MigrationStorage.ts#L18)constructor

* ****new MigrationStorage**(driver, options): [MigrationStorage](https://mikro-orm.io/api/migrations/class/MigrationStorage.md)

* #### Parameters

  * ##### driver: [AbstractSqlDriver](https://mikro-orm.io/api/sql/class/AbstractSqlDriver.md)<[AbstractSqlConnection](https://mikro-orm.io/api/sql/class/AbstractSqlConnection.md), [AbstractSqlPlatform](https://mikro-orm.io/api/sql/class/AbstractSqlPlatform.md)>

  * ##### options: [MigrationsOptions](https://mikro-orm.io/api/core.md#MigrationsOptions)

  #### Returns [MigrationStorage](https://mikro-orm.io/api/migrations/class/MigrationStorage.md)

## Methods<!-- -->[**](#methods)

### [**](#ensuretable)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/migrations/src/MigrationStorage.ts#L66)ensureTable

* ****ensureTable**(): Promise\<void>

* #### Returns Promise\<void>

### [**](#executed)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/migrations/src/MigrationStorage.ts#L27)executed

* ****executed**(): Promise\<string\[]>

* #### Returns Promise\<string\[]>

### [**](#getexecutedmigrations)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/migrations/src/MigrationStorage.ts#L49)getExecutedMigrations

* ****getExecutedMigrations**(): Promise<[MigrationRow](https://mikro-orm.io/api/core.md#MigrationRow)\[]>

* #### Returns Promise<[MigrationRow](https://mikro-orm.io/api/core.md#MigrationRow)\[]>

### [**](#logmigration)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/migrations/src/MigrationStorage.ts#L32)logMigration

* ****logMigration**(params): Promise\<void>

* #### Parameters

  * ##### params: { name: string }

    * ##### name: string

  #### Returns Promise\<void>

### [**](#setmastermigration)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/migrations/src/MigrationStorage.ts#L111)setMasterMigration

* ****setMasterMigration**(trx): void

* #### Parameters

  * ##### trx: any

  #### Returns void

### [**](#unlogmigration)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/migrations/src/MigrationStorage.ts#L38)unlogMigration

* ****unlogMigration**(params): Promise\<void>

* #### Parameters

  * ##### params: { name: string }

    * ##### name: string

  #### Returns Promise\<void>

### [**](#unsetmastermigration)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/migrations/src/MigrationStorage.ts#L115)unsetMasterMigration

* ****unsetMasterMigration**(): void

* #### Returns void
