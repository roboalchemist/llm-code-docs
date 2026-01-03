# Source: https://mikro-orm.io/api/core/class/AbstractSchemaGenerator.md

# abstractAbstractSchemaGenerator<!-- --> \<D>

### Hierarchy

* *AbstractSchemaGenerator*

  * [SqlSchemaGenerator](https://mikro-orm.io/api/knex/class/SqlSchemaGenerator.md)
  * [MongoSchemaGenerator](https://mikro-orm.io/api/mongodb/class/MongoSchemaGenerator.md)

### Implements

* [ISchemaGenerator](https://mikro-orm.io/api/core/interface/ISchemaGenerator.md)

## Index[**](#Index)

### Constructors

* [**constructor](#constructor)

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

## Constructors<!-- -->[**](#Constructors)

### [**](#constructor)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/AbstractSchemaGenerator.ts#L26)constructor

* ****new AbstractSchemaGenerator**\<D>(em): [AbstractSchemaGenerator](https://mikro-orm.io/api/core/class/AbstractSchemaGenerator.md)\<D>

- #### Parameters

  * ##### em: D | ReturnType\<D\[createEntityManager]>

  #### Returns [AbstractSchemaGenerator](https://mikro-orm.io/api/core/class/AbstractSchemaGenerator.md)\<D>

## Methods<!-- -->[**](#Methods)

### [**](#clearDatabase)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/AbstractSchemaGenerator.ts#L59)clearDatabase

* ****clearDatabase**(options): Promise\<void>

- Implementation of ISchemaGenerator.clearDatabase

  #### Parameters

  * ##### optionaloptions: [ClearDatabaseOptions](https://mikro-orm.io/api/core/interface/ClearDatabaseOptions.md)

  #### Returns Promise\<void>

### [**](#createDatabase)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/AbstractSchemaGenerator.ts#L106)createDatabase

* ****createDatabase**(name): Promise\<void>

- Implementation of ISchemaGenerator.createDatabase

  creates new database and connects to it

  ***

  #### Parameters

  * ##### optionalname: string

  #### Returns Promise\<void>

### [**](#createSchema)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/AbstractSchemaGenerator.ts#L35)createSchema

* ****createSchema**(options): Promise\<void>

- Implementation of ISchemaGenerator.createSchema

  #### Parameters

  * ##### optionaloptions: [CreateSchemaOptions](https://mikro-orm.io/api/core/interface/CreateSchemaOptions.md)

  #### Returns Promise\<void>

### [**](#dropDatabase)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/AbstractSchemaGenerator.ts#L110)dropDatabase

* ****dropDatabase**(name): Promise\<void>

- Implementation of ISchemaGenerator.dropDatabase

  #### Parameters

  * ##### optionalname: string

  #### Returns Promise\<void>

### [**](#dropSchema)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/AbstractSchemaGenerator.ts#L83)dropSchema

* ****dropSchema**(options): Promise\<void>

- Implementation of ISchemaGenerator.dropSchema

  #### Parameters

  * ##### optionaloptions: [DropSchemaOptions](https://mikro-orm.io/api/core/interface/DropSchemaOptions.md)

  #### Returns Promise\<void>

### [**](#ensureDatabase)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/AbstractSchemaGenerator.ts#L42)ensureDatabase

* ****ensureDatabase**(options): Promise\<boolean>

- Implementation of ISchemaGenerator.ensureDatabase

  Returns true if the database was created.

  ***

  #### Parameters

  * ##### optionaloptions: [EnsureDatabaseOptions](https://mikro-orm.io/api/core/interface/EnsureDatabaseOptions.md)

  #### Returns Promise\<boolean>

### [**](#ensureIndexes)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/AbstractSchemaGenerator.ts#L118)ensureIndexes

* ****ensureIndexes**(): Promise\<void>

- Implementation of ISchemaGenerator.ensureIndexes

  #### Returns Promise\<void>

### [**](#execute)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/AbstractSchemaGenerator.ts#L114)execute

* ****execute**(query): Promise\<void>

- Implementation of ISchemaGenerator.execute

  #### Parameters

  * ##### query: string

  #### Returns Promise\<void>

### [**](#getCreateSchemaSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/AbstractSchemaGenerator.ts#L79)getCreateSchemaSQL

* ****getCreateSchemaSQL**(options): Promise\<string>

- Implementation of ISchemaGenerator.getCreateSchemaSQL

  #### Parameters

  * ##### optionaloptions: [CreateSchemaOptions](https://mikro-orm.io/api/core/interface/CreateSchemaOptions.md)

  #### Returns Promise\<string>

### [**](#getDropSchemaSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/AbstractSchemaGenerator.ts#L87)getDropSchemaSQL

* ****getDropSchemaSQL**(options): Promise\<string>

- Implementation of ISchemaGenerator.getDropSchemaSQL

  #### Parameters

  * ##### optionaloptions: Omit<[DropSchemaOptions](https://mikro-orm.io/api/core/interface/DropSchemaOptions.md), dropDb>

  #### Returns Promise\<string>

### [**](#getUpdateSchemaMigrationSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/AbstractSchemaGenerator.ts#L99)getUpdateSchemaMigrationSQL

* ****getUpdateSchemaMigrationSQL**(options): Promise<{ down: string; up: string }>

- Implementation of ISchemaGenerator.getUpdateSchemaMigrationSQL

  #### Parameters

  * ##### optionaloptions: [UpdateSchemaOptions](https://mikro-orm.io/api/core/interface/UpdateSchemaOptions.md)\<unknown>

  #### Returns Promise<{ down: string; up: string }>

### [**](#getUpdateSchemaSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/AbstractSchemaGenerator.ts#L95)getUpdateSchemaSQL

* ****getUpdateSchemaSQL**(options): Promise\<string>

- Implementation of ISchemaGenerator.getUpdateSchemaSQL

  #### Parameters

  * ##### optionaloptions: [UpdateSchemaOptions](https://mikro-orm.io/api/core/interface/UpdateSchemaOptions.md)\<unknown>

  #### Returns Promise\<string>

### [**](#refreshDatabase)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/AbstractSchemaGenerator.ts#L46)refreshDatabase

* ****refreshDatabase**(options): Promise\<void>

- Implementation of ISchemaGenerator.refreshDatabase

  #### Parameters

  * ##### optionaloptions: [RefreshDatabaseOptions](https://mikro-orm.io/api/core/interface/RefreshDatabaseOptions.md)

  #### Returns Promise\<void>

### [**](#updateSchema)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/AbstractSchemaGenerator.ts#L91)updateSchema

* ****updateSchema**(options): Promise\<void>

- Implementation of ISchemaGenerator.updateSchema

  #### Parameters

  * ##### optionaloptions: [UpdateSchemaOptions](https://mikro-orm.io/api/core/interface/UpdateSchemaOptions.md)\<unknown>

  #### Returns Promise\<void>
