# Source: https://mikro-orm.io/api/core/interface/IMigrationGenerator.md

# IMigrationGenerator<!-- -->

### Implemented by

* [MigrationGenerator](https://mikro-orm.io/api/migrations/class/MigrationGenerator.md)

## Index[**](#Index)

### Methods

* [**createStatement](#createStatement)
* [**generate](#generate)
* [**generateMigrationFile](#generateMigrationFile)

## Methods<!-- -->[**](#Methods)

### [**](#createStatement)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L1053)createStatement

* ****createStatement**(sql, padLeft): string

- Creates single migration statement. By default adds `this.addSql(sql);` to the code.

  ***

  #### Parameters

  * ##### sql: string
  * ##### padLeft: number

  #### Returns string

### [**](#generate)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L1048)generate

* ****generate**(diff, path, name): Promise<\[string, string]>

- Generates the full contents of migration file. Uses `generateMigrationFile` to get the file contents.

  ***

  #### Parameters

  * ##### diff: [MigrationDiff](https://mikro-orm.io/api/core/interface/MigrationDiff.md)
  * ##### optionalpath: string
  * ##### optionalname: string

  #### Returns Promise<\[string, string]>

### [**](#generateMigrationFile)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L1058)generateMigrationFile

* ****generateMigrationFile**(className, diff): [MaybePromise](https://mikro-orm.io/api/core.md#MaybePromise)\<string>

- Returns the file contents of given migration.

  ***

  #### Parameters

  * ##### className: string
  * ##### diff: [MigrationDiff](https://mikro-orm.io/api/core/interface/MigrationDiff.md)

  #### Returns [MaybePromise](https://mikro-orm.io/api/core.md#MaybePromise)\<string>
