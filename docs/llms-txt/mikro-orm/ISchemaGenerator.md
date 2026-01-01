# Source: https://mikro-orm.io/api/core/interface/ISchemaGenerator.md

# ISchemaGenerator<!-- -->

### Implemented by

* [AbstractSchemaGenerator](https://mikro-orm.io/api/core/class/AbstractSchemaGenerator.md)
* [SqlSchemaGenerator](https://mikro-orm.io/api/knex/class/SqlSchemaGenerator.md)

## Index[**](#Index)

### Methods

* [**clearDatabase](#clearDatabase)
* [**createDatabase](#createDatabase)
* [**createSchema](#createSchema)
* [**dropDatabase](#dropDatabase)
* [**dropSchema](#dropSchema)
* [**ensureDatabase](#ensureDatabase)
* [**ensureIndexes](#ensureIndexes)
* [**execute](#execute)
* [**getCreateSchemaSQL](#getCreateSchemaSQL)
* [**getDropSchemaSQL](#getDropSchemaSQL)
* [**getUpdateSchemaMigrationSQL](#getUpdateSchemaMigrationSQL)
* [**getUpdateSchemaSQL](#getUpdateSchemaSQL)
* [**refreshDatabase](#refreshDatabase)
* [**updateSchema](#updateSchema)

## Methods<!-- -->[**](#Methods)

### [**](#clearDatabase)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L921)clearDatabase

* ****clearDatabase**(options): Promise\<void>

- #### Parameters

  * ##### optionaloptions: [ClearDatabaseOptions](https://mikro-orm.io/api/core/interface/ClearDatabaseOptions.md)

  #### Returns Promise\<void>

### [**](#createDatabase)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L916)createDatabase

* ****createDatabase**(name): Promise\<void>

- #### Parameters

  * ##### optionalname: string

  #### Returns Promise\<void>

### [**](#createSchema)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L908)createSchema

* ****createSchema**(options): Promise\<void>

- #### Parameters

  * ##### optionaloptions: [CreateSchemaOptions](https://mikro-orm.io/api/core/interface/CreateSchemaOptions.md)

  #### Returns Promise\<void>

### [**](#dropDatabase)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L917)dropDatabase

* ****dropDatabase**(name): Promise\<void>

- #### Parameters

  * ##### optionalname: string

  #### Returns Promise\<void>

### [**](#dropSchema)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L911)dropSchema

* ****dropSchema**(options): Promise\<void>

- #### Parameters

  * ##### optionaloptions: [DropSchemaOptions](https://mikro-orm.io/api/core/interface/DropSchemaOptions.md)

  #### Returns Promise\<void>

### [**](#ensureDatabase)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L909)ensureDatabase

* ****ensureDatabase**(options): Promise\<boolean>

- #### Parameters

  * ##### optionaloptions: [EnsureDatabaseOptions](https://mikro-orm.io/api/core/interface/EnsureDatabaseOptions.md)

  #### Returns Promise\<boolean>

### [**](#ensureIndexes)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L919)ensureIndexes

* ****ensureIndexes**(): Promise\<void>

- #### Returns Promise\<void>

### [**](#execute)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L918)execute

* ****execute**(sql, options): Promise\<void>

- #### Parameters

  * ##### sql: string
  * ##### optionaloptions: { wrap?<!-- -->: boolean }
    * ##### optionalwrap: boolean

  #### Returns Promise\<void>

### [**](#getCreateSchemaSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L910)getCreateSchemaSQL

* ****getCreateSchemaSQL**(options): Promise\<string>

- #### Parameters

  * ##### optionaloptions: [CreateSchemaOptions](https://mikro-orm.io/api/core/interface/CreateSchemaOptions.md)

  #### Returns Promise\<string>

### [**](#getDropSchemaSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L912)getDropSchemaSQL

* ****getDropSchemaSQL**(options): Promise\<string>

- #### Parameters

  * ##### optionaloptions: Omit<[DropSchemaOptions](https://mikro-orm.io/api/core/interface/DropSchemaOptions.md), dropDb>

  #### Returns Promise\<string>

### [**](#getUpdateSchemaMigrationSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L915)getUpdateSchemaMigrationSQL

* ****getUpdateSchemaMigrationSQL**(options): Promise<{ down: string; up: string }>

- #### Parameters

  * ##### optionaloptions: [UpdateSchemaOptions](https://mikro-orm.io/api/core/interface/UpdateSchemaOptions.md)\<unknown>

  #### Returns Promise<{ down: string; up: string }>

### [**](#getUpdateSchemaSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L914)getUpdateSchemaSQL

* ****getUpdateSchemaSQL**(options): Promise\<string>

- #### Parameters

  * ##### optionaloptions: [UpdateSchemaOptions](https://mikro-orm.io/api/core/interface/UpdateSchemaOptions.md)\<unknown>

  #### Returns Promise\<string>

### [**](#refreshDatabase)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L920)refreshDatabase

* ****refreshDatabase**(options): Promise\<void>

- #### Parameters

  * ##### optionaloptions: [RefreshDatabaseOptions](https://mikro-orm.io/api/core/interface/RefreshDatabaseOptions.md)

  #### Returns Promise\<void>

### [**](#updateSchema)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L913)updateSchema

* ****updateSchema**(options): Promise\<void>

- #### Parameters

  * ##### optionaloptions: [UpdateSchemaOptions](https://mikro-orm.io/api/core/interface/UpdateSchemaOptions.md)\<unknown>

  #### Returns Promise\<void>
