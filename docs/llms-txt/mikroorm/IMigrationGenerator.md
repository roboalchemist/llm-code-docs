# Source: https://mikro-orm.io/api/core/interface/IMigrationGenerator.md

# IMigrationGenerator<!-- -->

### Implemented by

* [MigrationGenerator](https://mikro-orm.io/api/migrations/class/MigrationGenerator.md)

## Index[**](#index)

### Methods

* [**createStatement](#createstatement)
* [**generate](#generate)
* [**generateMigrationFile](#generatemigrationfile)

## Methods<!-- -->[**](#methods)

### [**](#createstatement)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1527)createStatement

* ****createStatement**(sql, padLeft): string

* Creates single migration statement. By default adds `this.addSql(sql);` to the code.

  ***

  #### Parameters

  * ##### sql: string

  * ##### padLeft: number

  #### Returns string

### [**](#generate)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1522)generate

* ****generate**(diff, path, name): Promise<\[string, string]>

* Generates the full contents of migration file. Uses `generateMigrationFile` to get the file contents.

  ***

  #### Parameters

  * ##### diff: [MigrationDiff](https://mikro-orm.io/api/core/interface/MigrationDiff.md)

  * ##### optionalpath: string

  * ##### optionalname: string

  #### Returns Promise<\[string, string]>

### [**](#generatemigrationfile)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1532)generateMigrationFile

* ****generateMigrationFile**(className, diff): [MaybePromise](https://mikro-orm.io/api/core.md#MaybePromise)\<string>

* Returns the file contents of given migration.

  ***

  #### Parameters

  * ##### className: string

  * ##### diff: [MigrationDiff](https://mikro-orm.io/api/core/interface/MigrationDiff.md)

  #### Returns [MaybePromise](https://mikro-orm.io/api/core.md#MaybePromise)\<string>
