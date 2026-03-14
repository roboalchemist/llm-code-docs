# Source: https://mikro-orm.io/api/core/interface/IMigrator.md

# IMigrator<!-- -->

## Index[**](#index)

### Methods

* [**create](#create)
* [**createInitial](#createinitial)
* [**down](#down)
* [**getExecuted](#getexecuted)
* [**getPending](#getpending)
* [**checkSchema](#checkschema)
* [**off](#off)
* [**on](#on)
* [**up](#up)

## Methods<!-- -->[**](#methods)

### [**](#create)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1460)create

* ****create**(path, blank, initial, name): Promise<[MigrationResult](https://mikro-orm.io/api/core.md#MigrationResult)>

* Checks current schema for changes, generates new migration if there are any.

  ***

  #### Parameters

  * ##### optionalpath: string

  * ##### optionalblank: boolean

  * ##### optionalinitial: boolean

  * ##### optionalname: string

  #### Returns Promise<[MigrationResult](https://mikro-orm.io/api/core.md#MigrationResult)>

### [**](#createinitial)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1473)createInitial

* ****createInitial**(path): Promise<[MigrationResult](https://mikro-orm.io/api/core.md#MigrationResult)>

* Creates initial migration. This generates the schema based on metadata, and checks whether all the tables are already present. If yes, it will also automatically log the migration as executed. Initial migration can be created only if the schema is already aligned with the metadata, or when no schema is present - in such case regular migration would have the same effect.

  ***

  #### Parameters

  * ##### optionalpath: string

  #### Returns Promise<[MigrationResult](https://mikro-orm.io/api/core.md#MigrationResult)>

### [**](#down)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1493)down

* ****down**(options): Promise<[MigrationInfo](https://mikro-orm.io/api/core.md#MigrationInfo)\[]>

* Executes down migrations to the given point. Without parameter it will migrate one version down.

  ***

  #### Parameters

  * ##### optionaloptions: string | string\[] | Omit<[MigrateOptions](https://mikro-orm.io/api/core.md#MigrateOptions), from>

  #### Returns Promise<[MigrationInfo](https://mikro-orm.io/api/core.md#MigrationInfo)\[]>

### [**](#getexecuted)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1478)getExecuted

* ****getExecuted**(): Promise<[MigrationRow](https://mikro-orm.io/api/core.md#MigrationRow)\[]>

* Returns list of already executed migrations.

  ***

  #### Returns Promise<[MigrationRow](https://mikro-orm.io/api/core.md#MigrationRow)\[]>

### [**](#getpending)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1483)getPending

* ****getPending**(): Promise<[MigrationInfo](https://mikro-orm.io/api/core.md#MigrationInfo)\[]>

* Returns list of pending (not yet executed) migrations found in the migration directory.

  ***

  #### Returns Promise<[MigrationInfo](https://mikro-orm.io/api/core.md#MigrationInfo)\[]>

### [**](#checkschema)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1465)checkSchema

* ****checkSchema**(): Promise\<boolean>

* Checks current schema for changes.

  ***

  #### Returns Promise\<boolean>

### [**](#off)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1503)off

* ****off**(event, listener): [IMigrator](https://mikro-orm.io/api/core/interface/IMigrator.md)

* Removes event handler.

  ***

  #### Parameters

  * ##### event: [MigratorEvent](https://mikro-orm.io/api/core.md#MigratorEvent)

  * ##### listener: (event) => [MaybePromise](https://mikro-orm.io/api/core.md#MaybePromise)\<void>

  #### Returns [IMigrator](https://mikro-orm.io/api/core/interface/IMigrator.md)

### [**](#on)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1498)on

* ****on**(event, listener): [IMigrator](https://mikro-orm.io/api/core/interface/IMigrator.md)

* Registers event handler.

  ***

  #### Parameters

  * ##### event: [MigratorEvent](https://mikro-orm.io/api/core.md#MigratorEvent)

  * ##### listener: (event) => [MaybePromise](https://mikro-orm.io/api/core.md#MaybePromise)\<void>

  #### Returns [IMigrator](https://mikro-orm.io/api/core/interface/IMigrator.md)

### [**](#up)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1488)up

* ****up**(options): Promise<[MigrationInfo](https://mikro-orm.io/api/core.md#MigrationInfo)\[]>

* Executes specified migrations. Without parameter it will migrate up to the latest version.

  ***

  #### Parameters

  * ##### optionaloptions: string | string\[] | [MigrateOptions](https://mikro-orm.io/api/core.md#MigrateOptions)

  #### Returns Promise<[MigrationInfo](https://mikro-orm.io/api/core.md#MigrationInfo)\[]>
