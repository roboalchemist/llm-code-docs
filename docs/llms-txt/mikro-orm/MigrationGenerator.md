# Source: https://mikro-orm.io/api/migrations/class/MigrationGenerator.md

# abstractMigrationGenerator<!-- -->

### Hierarchy

* *MigrationGenerator*

  * [JSMigrationGenerator](https://mikro-orm.io/api/migrations/class/JSMigrationGenerator.md)
  * [TSMigrationGenerator](https://mikro-orm.io/api/migrations/class/TSMigrationGenerator.md)

### Implements

* [IMigrationGenerator](https://mikro-orm.io/api/core/interface/IMigrationGenerator.md)

## Index[**](#Index)

### Constructors

* [**constructor](#constructor)

### Methods

* [**createStatement](#createStatement)
* [**generate](#generate)
* [**generateMigrationFile](#generateMigrationFile)

## Constructors<!-- -->[**](#Constructors)

### [**](#constructor)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/migrations/src/MigrationGenerator.ts#L13)constructor

* ****new MigrationGenerator**(driver, namingStrategy, options): [MigrationGenerator](https://mikro-orm.io/api/migrations/class/MigrationGenerator.md)

- #### Parameters

  * ##### driver: [AbstractSqlDriver](https://mikro-orm.io/api/knex/class/AbstractSqlDriver.md)<[AbstractSqlConnection](https://mikro-orm.io/api/knex/class/AbstractSqlConnection.md), [AbstractSqlPlatform](https://mikro-orm.io/api/knex/class/AbstractSqlPlatform.md)>
  * ##### namingStrategy: [NamingStrategy](https://mikro-orm.io/api/core/interface/NamingStrategy.md)
  * ##### options: [MigrationsOptions](https://mikro-orm.io/api/core.md#MigrationsOptions)

  #### Returns [MigrationGenerator](https://mikro-orm.io/api/migrations/class/MigrationGenerator.md)

## Methods<!-- -->[**](#Methods)

### [**](#createStatement)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/migrations/src/MigrationGenerator.ts#L37)createStatement

* ****createStatement**(sql, padLeft): string

- Implementation of IMigrationGenerator.createStatement

  Creates single migration statement. By default adds `this.addSql(sql);` to the code.

  ***

  #### Parameters

  * ##### sql: string
  * ##### padLeft: number

  #### Returns string

### [**](#generate)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/migrations/src/MigrationGenerator.ts#L20)generate

* ****generate**(diff, path, name): Promise<\[string, string]>

- Implementation of IMigrationGenerator.generate

  Generates the full contents of migration file. Uses `generateMigrationFile` to get the file contents.

  ***

  #### Parameters

  * ##### diff: { down: string\[]; up: string\[] }
  * * ##### down: string\[]
    * ##### up: string\[]
    ##### optionalpath: string
  * ##### optionalname: string

  #### Returns Promise<\[string, string]>

### [**](#generateMigrationFile)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/migrations/src/MigrationGenerator.ts#L49)abstractgenerateMigrationFile

* ****generateMigrationFile**(className, diff): [MaybePromise](https://mikro-orm.io/api/core.md#MaybePromise)\<string>

- Implementation of IMigrationGenerator.generateMigrationFile

  Returns the file contents of given migration.

  ***

  #### Parameters

  * ##### className: string
  * ##### diff: { down: string\[]; up: string\[] }
    * ##### down: string\[]
    * ##### up: string\[]

  #### Returns [MaybePromise](https://mikro-orm.io/api/core.md#MaybePromise)\<string>
