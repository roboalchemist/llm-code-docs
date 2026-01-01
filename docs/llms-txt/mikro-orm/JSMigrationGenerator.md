# Source: https://mikro-orm.io/api/migrations/class/JSMigrationGenerator.md

# JSMigrationGenerator<!-- -->

### Hierarchy

* [MigrationGenerator](https://mikro-orm.io/api/migrations/class/MigrationGenerator.md)
  * *JSMigrationGenerator*

## Index[**](#Index)

### Constructors

* [**constructor](#constructor)

### Methods

* [**createStatement](#createStatement)
* [**generate](#generate)
* [**generateMigrationFile](#generateMigrationFile)

## Constructors<!-- -->[**](#Constructors)

### [**](#constructor)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/migrations/src/MigrationGenerator.ts#L13)constructor

* ****new JSMigrationGenerator**(driver, namingStrategy, options): [JSMigrationGenerator](https://mikro-orm.io/api/migrations/class/JSMigrationGenerator.md)

- Inherited from MigrationGenerator.constructor

  #### Parameters

  * ##### driver: [AbstractSqlDriver](https://mikro-orm.io/api/knex/class/AbstractSqlDriver.md)<[AbstractSqlConnection](https://mikro-orm.io/api/knex/class/AbstractSqlConnection.md), [AbstractSqlPlatform](https://mikro-orm.io/api/knex/class/AbstractSqlPlatform.md)>
  * ##### namingStrategy: [NamingStrategy](https://mikro-orm.io/api/core/interface/NamingStrategy.md)
  * ##### options: [MigrationsOptions](https://mikro-orm.io/api/core.md#MigrationsOptions)

  #### Returns [JSMigrationGenerator](https://mikro-orm.io/api/migrations/class/JSMigrationGenerator.md)

## Methods<!-- -->[**](#Methods)

### [**](#createStatement)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/migrations/src/MigrationGenerator.ts#L37)inheritedcreateStatement

* ****createStatement**(sql, padLeft): string

- Inherited from MigrationGenerator.createStatement

  Creates single migration statement. By default adds `this.addSql(sql);` to the code.

  ***

  #### Parameters

  * ##### sql: string
  * ##### padLeft: number

  #### Returns string

### [**](#generate)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/migrations/src/MigrationGenerator.ts#L20)inheritedgenerate

* ****generate**(diff, path, name): Promise<\[string, string]>

- Inherited from MigrationGenerator.generate

  Generates the full contents of migration file. Uses `generateMigrationFile` to get the file contents.

  ***

  #### Parameters

  * ##### diff: { down: string\[]; up: string\[] }
  * * ##### down: string\[]
    * ##### up: string\[]
    ##### optionalpath: string
  * ##### optionalname: string

  #### Returns Promise<\[string, string]>

### [**](#generateMigrationFile)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/migrations/src/JSMigrationGenerator.ts#L8)generateMigrationFile

* ****generateMigrationFile**(className, diff): string

- Overrides MigrationGenerator.generateMigrationFile

  Returns the file contents of given migration.

  ***

  #### Parameters

  * ##### className: string
  * ##### diff: { down: string\[]; up: string\[] }
    * ##### down: string\[]
    * ##### up: string\[]

  #### Returns string
