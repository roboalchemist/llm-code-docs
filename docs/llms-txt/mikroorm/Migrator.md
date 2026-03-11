# Source: https://mikro-orm.io/api/migrations/class/Migrator.md

# Migrator<!-- -->

### Hierarchy

* AbstractMigrator<[AbstractSqlDriver](https://mikro-orm.io/api/sql/class/AbstractSqlDriver.md)>
  * *Migrator*

## Index[**](#index)

### Constructors

* [**constructor](#constructor)

### Methods

* [**create](#create)
* [**createInitial](#createinitial)
* [**down](#down)
* [**getExecuted](#getExecuted)
* [**getPending](#getPending)
* [**getStorage](#getstorage)
* [**checkSchema](#checkschema)
* [**off](#off)
* [**on](#on)
* [**up](#up)
* [**register](#register)

## Constructors<!-- -->[**](#constructors)

### [**](#constructor)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/migrations/src/Migrator.ts#L31)constructor

* ****new Migrator**(em): [Migrator](https://mikro-orm.io/api/migrations/class/Migrator.md)

* Overrides AbstractMigrator\<AbstractSqlDriver>.constructor

  #### Parameters

  * ##### em: [SqlEntityManager](https://mikro-orm.io/api/sql/class/EntityManager.md)<[AbstractSqlDriver](https://mikro-orm.io/api/sql/class/AbstractSqlDriver.md)<[AbstractSqlConnection](https://mikro-orm.io/api/sql/class/AbstractSqlConnection.md), [AbstractSqlPlatform](https://mikro-orm.io/api/sql/class/AbstractSqlPlatform.md)>>

  #### Returns [Migrator](https://mikro-orm.io/api/migrations/class/Migrator.md)

## Methods<!-- -->[**](#methods)

### [**](#create)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/migrations/src/Migrator.ts#L90)create

* ****create**(path, blank, initial, name): Promise<[MigrationResult](https://mikro-orm.io/api/core.md#MigrationResult)>

* Overrides AbstractMigrator.create

  * **@inheritDoc**

  ***

  #### Parameters

  * ##### optionalpath: string

  * ##### blank: boolean = <!-- -->false

  * ##### initial: boolean = <!-- -->false

  * ##### optionalname: string

  #### Returns Promise<[MigrationResult](https://mikro-orm.io/api/core.md#MigrationResult)>

### [**](#createinitial)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/migrations/src/Migrator.ts#L122)createInitial

* ****createInitial**(path, name, blank): Promise<[MigrationResult](https://mikro-orm.io/api/core.md#MigrationResult)>

* Overrides AbstractMigrator.createInitial

  * **@inheritDoc**

  ***

  #### Parameters

  * ##### optionalpath: string

  * ##### optionalname: string

  * ##### blank: boolean = <!-- -->false

  #### Returns Promise<[MigrationResult](https://mikro-orm.io/api/core.md#MigrationResult)>

### [**](#down)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/AbstractMigrator.ts#L124)inheriteddown

* ****down**(options): Promise<[MigrationInfo](https://mikro-orm.io/api/core.md#MigrationInfo)\[]>

* Inherited from AbstractMigrator.down

  * **@inheritDoc**

  ***

  #### Parameters

  * ##### optionaloptions: string | string\[] | Omit\<MigrateOptions, from>

  #### Returns Promise<[MigrationInfo](https://mikro-orm.io/api/core.md#MigrationInfo)\[]>

### [**](#getExecuted)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/AbstractMigrator.ts#L98)inheritedgetExecuted

* ****getExecuted**(): Promise<[MigrationRow](https://mikro-orm.io/api/core.md#MigrationRow)\[]>

* Inherited from AbstractMigrator.getExecuted

  * **@inheritDoc**

  ***

  #### Returns Promise<[MigrationRow](https://mikro-orm.io/api/core.md#MigrationRow)\[]>

### [**](#getPending)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/AbstractMigrator.ts#L106)inheritedgetPending

* ****getPending**(): Promise<[MigrationInfo](https://mikro-orm.io/api/core.md#MigrationInfo)\[]>

* Inherited from AbstractMigrator.getPending

  * **@inheritDoc**

  ***

  #### Returns Promise<[MigrationInfo](https://mikro-orm.io/api/core.md#MigrationInfo)\[]>

### [**](#getstorage)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/migrations/src/Migrator.ts#L159)getStorage

* ****getStorage**(): [MigrationStorage](https://mikro-orm.io/api/migrations/class/MigrationStorage.md)

* Overrides AbstractMigrator.getStorage

  #### Returns [MigrationStorage](https://mikro-orm.io/api/migrations/class/MigrationStorage.md)

### [**](#checkschema)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/migrations/src/Migrator.ts#L113)checkSchema

* ****checkSchema**(): Promise\<boolean>

* Overrides AbstractMigrator.checkSchema

  #### Returns Promise\<boolean>

### [**](#off)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/AbstractMigrator.ts#L90)inheritedoff

* ****off**(eventName, listener): this

* Inherited from AbstractMigrator.off

  * **@inheritDoc**

  ***

  #### Parameters

  * ##### eventName: [MigratorEvent](https://mikro-orm.io/api/core.md#MigratorEvent)

  * ##### listener: (event) => [MaybePromise](https://mikro-orm.io/api/core.md#MaybePromise)\<void>

  #### Returns this

### [**](#on)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/AbstractMigrator.ts#L77)inheritedon

* ****on**(eventName, listener): this

* Inherited from AbstractMigrator.on

  * **@inheritDoc**

  ***

  #### Parameters

  * ##### eventName: [MigratorEvent](https://mikro-orm.io/api/core.md#MigratorEvent)

  * ##### listener: (event) => [MaybePromise](https://mikro-orm.io/api/core.md#MaybePromise)\<void>

  #### Returns this

### [**](#up)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/AbstractMigrator.ts#L117)inheritedup

* ****up**(options): Promise<[MigrationInfo](https://mikro-orm.io/api/core.md#MigrationInfo)\[]>

* Inherited from AbstractMigrator.up

  * **@inheritDoc**

  ***

  #### Parameters

  * ##### optionaloptions: string | string\[] | MigrateOptions

  #### Returns Promise<[MigrationInfo](https://mikro-orm.io/api/core.md#MigrationInfo)\[]>

### [**](#register)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/migrations/src/Migrator.ts#L36)staticregister

* ****register**(orm): void

* #### Parameters

  * ##### orm: [MikroORM](https://mikro-orm.io/api/core/class/MikroORM.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>, [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>>, (string | [EntitySchema](https://mikro-orm.io/api/core/class/EntitySchema.md)\<any, never, [EntityCtor](https://mikro-orm.io/api/core.md#EntityCtor)\<any>> | [EntityClass](https://mikro-orm.io/api/core.md#EntityClass)\<Partial\<any>>)\[]>

  #### Returns void
