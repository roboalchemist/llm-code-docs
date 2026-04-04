# Source: https://mikro-orm.io/api/knex/class/SqlSchemaGenerator.md

# SqlSchemaGenerator<!-- -->

### Hierarchy

* [AbstractSchemaGenerator](https://mikro-orm.io/api/core/class/AbstractSchemaGenerator.md)<[AbstractSqlDriver](https://mikro-orm.io/api/knex/class/AbstractSqlDriver.md)>
  * *SqlSchemaGenerator*

### Implements

* [ISchemaGenerator](https://mikro-orm.io/api/core/interface/ISchemaGenerator.md)

## Index[**](#Index)

### Constructors

* [**constructor](#constructor)

### Methods

* [**clearDatabase](#clearDatabase)
* [**createDatabase](#createDatabase)
* [**createNamespace](#createNamespace)
* [**createSchema](#createSchema)
* [**diffToSQL](#diffToSQL)
* [**dropDatabase](#dropDatabase)
* [**dropNamespace](#dropNamespace)
* [**dropSchema](#dropSchema)
* [**ensureDatabase](#ensureDatabase)
* [**ensureIndexes](#ensureIndexes)
* [**execute](#execute)
* [**getCreateSchemaSQL](#getCreateSchemaSQL)
* [**getDropSchemaSQL](#getDropSchemaSQL)
* [**getTargetSchema](#getTargetSchema)
* [**getUpdateSchemaMigrationSQL](#getUpdateSchemaMigrationSQL)
* [**getUpdateSchemaSQL](#getUpdateSchemaSQL)
* [**refreshDatabase](#refreshDatabase)
* [**updateSchema](#updateSchema)
* [**register](#register)

## Constructors<!-- -->[**](#Constructors)

### [**](#constructor)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/AbstractSchemaGenerator.ts#L26)constructor

* ****new SqlSchemaGenerator**(em): [SqlSchemaGenerator](https://mikro-orm.io/api/knex/class/SqlSchemaGenerator.md)

- Inherited from AbstractSchemaGenerator.constructor

  #### Parameters

  * ##### em: [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>> | [AbstractSqlDriver](https://mikro-orm.io/api/knex/class/AbstractSqlDriver.md)<[AbstractSqlConnection](https://mikro-orm.io/api/knex/class/AbstractSqlConnection.md), [AbstractSqlPlatform](https://mikro-orm.io/api/knex/class/AbstractSqlPlatform.md)>

  #### Returns [SqlSchemaGenerator](https://mikro-orm.io/api/knex/class/SqlSchemaGenerator.md)

## Methods<!-- -->[**](#Methods)

### [**](#clearDatabase)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SqlSchemaGenerator.ts#L152)clearDatabase

* ****clearDatabase**(options): Promise\<void>

- Implementation of ISchemaGenerator.clearDatabase

  Overrides AbstractSchemaGenerator.clearDatabase

  #### Parameters

  * ##### optionaloptions: [ClearDatabaseOptions](https://mikro-orm.io/api/core/interface/ClearDatabaseOptions.md)

  #### Returns Promise\<void>

### [**](#createDatabase)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SqlSchemaGenerator.ts#L528)createDatabase

* ****createDatabase**(name): Promise\<void>

- Implementation of ISchemaGenerator.createDatabase

  Overrides AbstractSchemaGenerator.createDatabase

  creates new database and connects to it

  ***

  #### Parameters

  * ##### optionalname: string

  #### Returns Promise\<void>

### [**](#createNamespace)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SqlSchemaGenerator.ts#L142)createNamespace

* ****createNamespace**(name): Promise\<void>

- #### Parameters

  * ##### name: string

  #### Returns Promise\<void>

### [**](#createSchema)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SqlSchemaGenerator.ts#L31)createSchema

* ****createSchema**(options): Promise\<void>

- Implementation of ISchemaGenerator.createSchema

  Overrides AbstractSchemaGenerator.createSchema

  #### Parameters

  * ##### optionaloptions: [CreateSchemaOptions](https://mikro-orm.io/api/core/interface/CreateSchemaOptions.md)

  #### Returns Promise\<void>

### [**](#diffToSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SqlSchemaGenerator.ts#L260)diffToSQL

* ****diffToSQL**(schemaDiff, options): Promise\<string>

- #### Parameters

  * ##### schemaDiff: [SchemaDifference](https://mikro-orm.io/api/knex/interface/SchemaDifference.md)
  * ##### options: { dropTables?<!-- -->: boolean; safe?<!-- -->: boolean; schema?<!-- -->: string; wrap?<!-- -->: boolean }
    * ##### optionaldropTables: boolean
    * ##### optionalsafe: boolean
    * ##### optionalschema: string
    * ##### optionalwrap: boolean

  #### Returns Promise\<string>

### [**](#dropDatabase)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SqlSchemaGenerator.ts#L540)dropDatabase

* ****dropDatabase**(name): Promise\<void>

- Implementation of ISchemaGenerator.dropDatabase

  Overrides AbstractSchemaGenerator.dropDatabase

  #### Parameters

  * ##### optionalname: string

  #### Returns Promise\<void>

### [**](#dropNamespace)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SqlSchemaGenerator.ts#L147)dropNamespace

* ****dropNamespace**(name): Promise\<void>

- #### Parameters

  * ##### name: string

  #### Returns Promise\<void>

### [**](#dropSchema)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SqlSchemaGenerator.ts#L132)dropSchema

* ****dropSchema**(options): Promise\<void>

- Implementation of ISchemaGenerator.dropSchema

  Overrides AbstractSchemaGenerator.dropSchema

  #### Parameters

  * ##### options: [DropSchemaOptions](https://mikro-orm.io/api/core/interface/DropSchemaOptions.md) = <!-- -->{}

  #### Returns Promise\<void>

### [**](#ensureDatabase)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SqlSchemaGenerator.ts#L40)ensureDatabase

* ****ensureDatabase**(options): Promise\<boolean>

- Implementation of ISchemaGenerator.ensureDatabase

  Overrides AbstractSchemaGenerator.ensureDatabase

  Returns true if the database was created.

  ***

  #### Parameters

  * ##### optionaloptions: [EnsureDatabaseOptions](https://mikro-orm.io/api/core/interface/EnsureDatabaseOptions.md)

  #### Returns Promise\<boolean>

### [**](#ensureIndexes)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/AbstractSchemaGenerator.ts#L118)inheritedensureIndexes

* ****ensureIndexes**(): Promise\<void>

- Implementation of ISchemaGenerator.ensureIndexes

  Inherited from AbstractSchemaGenerator.ensureIndexes

  #### Returns Promise\<void>

### [**](#execute)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SqlSchemaGenerator.ts#L548)execute

* ****execute**(sql, options): Promise\<void>

- Implementation of ISchemaGenerator.execute

  Overrides AbstractSchemaGenerator.execute

  #### Parameters

  * ##### sql: string
  * ##### options: { ctx?<!-- -->: any; wrap?<!-- -->: boolean } = <!-- -->{}
    * ##### optionalctx: any
    * ##### optionalwrap: boolean

  #### Returns Promise\<void>

### [**](#getCreateSchemaSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SqlSchemaGenerator.ts#L92)getCreateSchemaSQL

* ****getCreateSchemaSQL**(options): Promise\<string>

- Implementation of ISchemaGenerator.getCreateSchemaSQL

  Overrides AbstractSchemaGenerator.getCreateSchemaSQL

  #### Parameters

  * ##### options: [CreateSchemaOptions](https://mikro-orm.io/api/core/interface/CreateSchemaOptions.md) = <!-- -->{}

  #### Returns Promise\<string>

### [**](#getDropSchemaSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SqlSchemaGenerator.ts#L172)getDropSchemaSQL

* ****getDropSchemaSQL**(options): Promise\<string>

- Implementation of ISchemaGenerator.getDropSchemaSQL

  Overrides AbstractSchemaGenerator.getDropSchemaSQL

  #### Parameters

  * ##### options: Omit<[DropSchemaOptions](https://mikro-orm.io/api/core/interface/DropSchemaOptions.md), dropDb> = <!-- -->{}

  #### Returns Promise\<string>

### [**](#getTargetSchema)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SqlSchemaGenerator.ts#L75)getTargetSchema

* ****getTargetSchema**(schema): DatabaseSchema

- #### Parameters

  * ##### optionalschema: string

  #### Returns DatabaseSchema

### [**](#getUpdateSchemaMigrationSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SqlSchemaGenerator.ts#L231)getUpdateSchemaMigrationSQL

* ****getUpdateSchemaMigrationSQL**(options): Promise<{ down: string; up: string }>

- Implementation of ISchemaGenerator.getUpdateSchemaMigrationSQL

  Overrides AbstractSchemaGenerator.getUpdateSchemaMigrationSQL

  #### Parameters

  * ##### options: [UpdateSchemaOptions](https://mikro-orm.io/api/core/interface/UpdateSchemaOptions.md)\<DatabaseSchema> = <!-- -->{}

  #### Returns Promise<{ down: string; up: string }>

### [**](#getUpdateSchemaSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SqlSchemaGenerator.ts#L222)getUpdateSchemaSQL

* ****getUpdateSchemaSQL**(options): Promise\<string>

- Implementation of ISchemaGenerator.getUpdateSchemaSQL

  Overrides AbstractSchemaGenerator.getUpdateSchemaSQL

  #### Parameters

  * ##### options: [UpdateSchemaOptions](https://mikro-orm.io/api/core/interface/UpdateSchemaOptions.md)\<DatabaseSchema> = <!-- -->{}

  #### Returns Promise\<string>

### [**](#refreshDatabase)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/AbstractSchemaGenerator.ts#L46)inheritedrefreshDatabase

* ****refreshDatabase**(options): Promise\<void>

- Implementation of ISchemaGenerator.refreshDatabase

  Inherited from AbstractSchemaGenerator.refreshDatabase

  #### Parameters

  * ##### optionaloptions: [RefreshDatabaseOptions](https://mikro-orm.io/api/core/interface/RefreshDatabaseOptions.md)

  #### Returns Promise\<void>

### [**](#updateSchema)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SqlSchemaGenerator.ts#L217)updateSchema

* ****updateSchema**(options): Promise\<void>

- Implementation of ISchemaGenerator.updateSchema

  Overrides AbstractSchemaGenerator.updateSchema

  #### Parameters

  * ##### options: [UpdateSchemaOptions](https://mikro-orm.io/api/core/interface/UpdateSchemaOptions.md)\<DatabaseSchema> = <!-- -->{}

  #### Returns Promise\<void>

### [**](#register)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SqlSchemaGenerator.ts#L27)staticregister

* ****register**(orm): void

- #### Parameters

  * ##### orm: [MikroORM](https://mikro-orm.io/api/core/class/MikroORM.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>, [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>>>

  #### Returns void
