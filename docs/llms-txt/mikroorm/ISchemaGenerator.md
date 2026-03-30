# Source: https://mikro-orm.io/api/core/interface/ISchemaGenerator.md

# ISchemaGenerator<!-- -->

### Implemented by

* [SqlSchemaGenerator](https://mikro-orm.io/api/sql/class/SqlSchemaGenerator.md)

## Index[**](#index)

### Methods

* [**clear](#clear)
* [**create](#create)
* [**createDatabase](#createdatabase)
* [**drop](#drop)
* [**dropDatabase](#dropdatabase)
* [**ensureDatabase](#ensuredatabase)
* [**ensureIndexes](#ensureindexes)
* [**execute](#execute)
* [**getCreateSchemaSQL](#getcreateschemasql)
* [**getDropSchemaSQL](#getdropschemasql)
* [**getUpdateSchemaMigrationSQL](#getupdateschemamigrationsql)
* [**getUpdateSchemaSQL](#getupdateschemasql)
* [**refresh](#refresh)
* [**update](#update)

## Methods<!-- -->[**](#methods)

### [**](#clear)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1368)clear

* ****clear**(options): Promise\<void>

* #### Parameters

  * ##### optionaloptions: [ClearDatabaseOptions](https://mikro-orm.io/api/core/interface/ClearDatabaseOptions.md)

  #### Returns Promise\<void>

### [**](#create)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1364)create

* ****create**(options): Promise\<void>

* #### Parameters

  * ##### optionaloptions: [CreateSchemaOptions](https://mikro-orm.io/api/core/interface/CreateSchemaOptions.md)

  #### Returns Promise\<void>

### [**](#createdatabase)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1375)createDatabase

* ****createDatabase**(name): Promise\<void>

* #### Parameters

  * ##### optionalname: string

  #### Returns Promise\<void>

### [**](#drop)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1366)drop

* ****drop**(options): Promise\<void>

* #### Parameters

  * ##### optionaloptions: [DropSchemaOptions](https://mikro-orm.io/api/core/interface/DropSchemaOptions.md)

  #### Returns Promise\<void>

### [**](#dropdatabase)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1376)dropDatabase

* ****dropDatabase**(name): Promise\<void>

* #### Parameters

  * ##### optionalname: string

  #### Returns Promise\<void>

### [**](#ensuredatabase)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1374)ensureDatabase

* ****ensureDatabase**(options): Promise\<boolean>

* #### Parameters

  * ##### optionaloptions: [EnsureDatabaseOptions](https://mikro-orm.io/api/core/interface/EnsureDatabaseOptions.md)

  #### Returns Promise\<boolean>

### [**](#ensureindexes)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1377)ensureIndexes

* ****ensureIndexes**(): Promise\<void>

* #### Returns Promise\<void>

### [**](#execute)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1369)execute

* ****execute**(sql, options): Promise\<void>

* #### Parameters

  * ##### sql: string

  * ##### optionaloptions: { wrap?<!-- -->: boolean }

    * ##### optionalwrap: boolean

  #### Returns Promise\<void>

### [**](#getcreateschemasql)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1370)getCreateSchemaSQL

* ****getCreateSchemaSQL**(options): Promise\<string>

* #### Parameters

  * ##### optionaloptions: [CreateSchemaOptions](https://mikro-orm.io/api/core/interface/CreateSchemaOptions.md)

  #### Returns Promise\<string>

### [**](#getdropschemasql)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1371)getDropSchemaSQL

* ****getDropSchemaSQL**(options): Promise\<string>

* #### Parameters

  * ##### optionaloptions: Omit<[DropSchemaOptions](https://mikro-orm.io/api/core/interface/DropSchemaOptions.md), dropDb>

  #### Returns Promise\<string>

### [**](#getupdateschemamigrationsql)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1373)getUpdateSchemaMigrationSQL

* ****getUpdateSchemaMigrationSQL**(options): Promise<{ down: string; up: string }>

* #### Parameters

  * ##### optionaloptions: [UpdateSchemaOptions](https://mikro-orm.io/api/core/interface/UpdateSchemaOptions.md)\<unknown>

  #### Returns Promise<{ down: string; up: string }>

### [**](#getupdateschemasql)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1372)getUpdateSchemaSQL

* ****getUpdateSchemaSQL**(options): Promise\<string>

* #### Parameters

  * ##### optionaloptions: [UpdateSchemaOptions](https://mikro-orm.io/api/core/interface/UpdateSchemaOptions.md)\<unknown>

  #### Returns Promise\<string>

### [**](#refresh)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1367)refresh

* ****refresh**(options): Promise\<void>

* #### Parameters

  * ##### optionaloptions: [RefreshDatabaseOptions](https://mikro-orm.io/api/core/interface/RefreshDatabaseOptions.md)

  #### Returns Promise\<void>

### [**](#update)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1365)update

* ****update**(options): Promise\<void>

* #### Parameters

  * ##### optionaloptions: [UpdateSchemaOptions](https://mikro-orm.io/api/core/interface/UpdateSchemaOptions.md)\<unknown>

  #### Returns Promise\<void>
