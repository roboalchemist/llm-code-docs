# Source: https://mikro-orm.io/api/oracledb/class/OracleSchemaGenerator.md

# OracleSchemaGenerator<!-- -->

### Hierarchy

* [SqlSchemaGenerator](https://mikro-orm.io/api/sql/class/SqlSchemaGenerator.md)
  * *OracleSchemaGenerator*

## Index[**](#index)

### Constructors

* [**constructor](#constructor)

### Methods

* [**clear](#clear)
* [**create](#create)
* [**createDatabase](#createdatabase)
* [**createNamespace](#createnamespace)
* [**diffToSQL](#diffToSQL)
* [**drop](#drop)
* [**dropDatabase](#dropdatabase)
* [**dropNamespace](#dropnamespace)
* [**dropTableIfExists](#dropTableIfExists)
* [**ensureDatabase](#ensuredatabase)
* [**ensureIndexes](#ensureIndexes)
* [**execute](#execute)
* [**getCreateSchemaSQL](#getCreateSchemaSQL)
* [**getDropSchemaSQL](#getdropschemasql)
* [**getTargetSchema](#getTargetSchema)
* [**getUpdateSchemaMigrationSQL](#getUpdateSchemaMigrationSQL)
* [**getUpdateSchemaSQL](#getUpdateSchemaSQL)
* [**refresh](#refresh)
* [**update](#update)
* [**register](#register)

## Constructors<!-- -->[**](#constructors)

### [**](#constructor)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/AbstractSchemaGenerator.ts#L25)constructor

* ****new OracleSchemaGenerator**(em): [OracleSchemaGenerator](https://mikro-orm.io/api/oracledb/class/OracleSchemaGenerator.md)

* Inherited from SqlSchemaGenerator.constructor

  #### Parameters

  * ##### em: [AbstractSqlDriver](https://mikro-orm.io/api/sql/class/AbstractSqlDriver.md)<[AbstractSqlConnection](https://mikro-orm.io/api/sql/class/AbstractSqlConnection.md), [AbstractSqlPlatform](https://mikro-orm.io/api/sql/class/AbstractSqlPlatform.md)> | [SqlEntityManager](https://mikro-orm.io/api/sql/class/EntityManager.md)<[AbstractSqlDriver](https://mikro-orm.io/api/sql/class/AbstractSqlDriver.md)<[AbstractSqlConnection](https://mikro-orm.io/api/sql/class/AbstractSqlConnection.md), [AbstractSqlPlatform](https://mikro-orm.io/api/sql/class/AbstractSqlPlatform.md)>>

  #### Returns [OracleSchemaGenerator](https://mikro-orm.io/api/oracledb/class/OracleSchemaGenerator.md)

## Methods<!-- -->[**](#methods)

### [**](#clear)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/oracledb/src/OracleSchemaGenerator.ts#L440)clear

* ****clear**(options): Promise\<void>

* Overrides SqlSchemaGenerator.clear

  #### Parameters

  * ##### optionaloptions: [ClearDatabaseOptions](https://mikro-orm.io/api/core/interface/ClearDatabaseOptions.md)

  #### Returns Promise\<void>

### [**](#create)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SqlSchemaGenerator.ts#L37)inheritedcreate

* ****create**(options): Promise\<void>

* Inherited from SqlSchemaGenerator.create

  #### Parameters

  * ##### optionaloptions: [CreateSchemaOptions](https://mikro-orm.io/api/core/interface/CreateSchemaOptions.md)

  #### Returns Promise\<void>

### [**](#createdatabase)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/oracledb/src/OracleSchemaGenerator.ts#L34)createDatabase

* ****createDatabase**(name): Promise\<void>

* Overrides SqlSchemaGenerator.createDatabase

  creates new database and connects to it

  ***

  #### Parameters

  * ##### optionalname: string

  #### Returns Promise\<void>

### [**](#createnamespace)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/oracledb/src/OracleSchemaGenerator.ts#L216)createNamespace

* ****createNamespace**(name): Promise\<void>

* Overrides SqlSchemaGenerator.createNamespace

  #### Parameters

  * ##### name: string

  #### Returns Promise\<void>

### [**](#diffToSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SqlSchemaGenerator.ts#L354)inheriteddiffToSQL

* ****diffToSQL**(schemaDiff, options): string

* Inherited from SqlSchemaGenerator.diffToSQL

  #### Parameters

  * ##### schemaDiff: [SchemaDifference](https://mikro-orm.io/api/sql/interface/SchemaDifference.md)

  * ##### options: { dropTables?<!-- -->: boolean; safe?<!-- -->: boolean; schema?<!-- -->: string; wrap?<!-- -->: boolean }

    * ##### optionaldropTables: boolean

    * ##### optionalsafe: boolean

    * ##### optionalschema: string

    * ##### optionalwrap: boolean

  #### Returns string

### [**](#drop)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SqlSchemaGenerator.ts#L159)inheriteddrop

* ****drop**(options): Promise\<void>

* Inherited from SqlSchemaGenerator.drop

  #### Parameters

  * ##### options: [DropSchemaOptions](https://mikro-orm.io/api/core/interface/DropSchemaOptions.md) = <!-- -->{}

  #### Returns Promise\<void>

### [**](#dropdatabase)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/oracledb/src/OracleSchemaGenerator.ts#L63)dropDatabase

* ****dropDatabase**(name): Promise\<void>

* Overrides SqlSchemaGenerator.dropDatabase

  #### Parameters

  * ##### optionalname: string

  #### Returns Promise\<void>

### [**](#dropnamespace)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/oracledb/src/OracleSchemaGenerator.ts#L236)dropNamespace

* ****dropNamespace**(name): Promise\<void>

* Overrides SqlSchemaGenerator.dropNamespace

  #### Parameters

  * ##### name: string

  #### Returns Promise\<void>

### [**](#dropTableIfExists)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SqlSchemaGenerator.ts#L587)inheriteddropTableIfExists

* ****dropTableIfExists**(name, schema): Promise\<void>

* Inherited from SqlSchemaGenerator.dropTableIfExists

  #### Parameters

  * ##### name: string

  * ##### optionalschema: string

  #### Returns Promise\<void>

### [**](#ensuredatabase)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/oracledb/src/OracleSchemaGenerator.ts#L100)ensureDatabase

* ****ensureDatabase**(options): Promise\<boolean>

* Overrides SqlSchemaGenerator.ensureDatabase

  Returns true if the database was created.

  ***

  #### Parameters

  * ##### optionaloptions: [EnsureDatabaseOptions](https://mikro-orm.io/api/core/interface/EnsureDatabaseOptions.md)

  #### Returns Promise\<boolean>

### [**](#ensureIndexes)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/AbstractSchemaGenerator.ts#L121)inheritedensureIndexes

* ****ensureIndexes**(): Promise\<void>

* Inherited from SqlSchemaGenerator.ensureIndexes

  #### Returns Promise\<void>

### [**](#execute)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SqlSchemaGenerator.ts#L545)inheritedexecute

* ****execute**(sql, options): Promise\<void>

* Inherited from SqlSchemaGenerator.execute

  #### Parameters

  * ##### sql: string

  * ##### options: { ctx?<!-- -->: any; wrap?<!-- -->: boolean } = <!-- -->{}

    * ##### optionalctx: any

    * ##### optionalwrap: boolean

  #### Returns Promise\<void>

### [**](#getCreateSchemaSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SqlSchemaGenerator.ts#L98)inheritedgetCreateSchemaSQL

* ****getCreateSchemaSQL**(options): Promise\<string>

* Inherited from SqlSchemaGenerator.getCreateSchemaSQL

  #### Parameters

  * ##### options: [CreateSchemaOptions](https://mikro-orm.io/api/core/interface/CreateSchemaOptions.md) = <!-- -->{}

  #### Returns Promise\<string>

### [**](#getdropschemasql)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/oracledb/src/OracleSchemaGenerator.ts#L75)getDropSchemaSQL

* ****getDropSchemaSQL**(options): Promise\<string>

* Overrides SqlSchemaGenerator.getDropSchemaSQL

  Oracle uses CASCADE CONSTRAINT in DROP TABLE and has no native enums, so we can generate drop SQL from metadata alone — no DB introspection needed.

  ***

  #### Parameters

  * ##### options: Omit<[DropSchemaOptions](https://mikro-orm.io/api/core/interface/DropSchemaOptions.md), dropDb> = <!-- -->{}

  #### Returns Promise\<string>

### [**](#getTargetSchema)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SqlSchemaGenerator.ts#L81)inheritedgetTargetSchema

* ****getTargetSchema**(schema): DatabaseSchema

* Inherited from SqlSchemaGenerator.getTargetSchema

  #### Parameters

  * ##### optionalschema: string

  #### Returns DatabaseSchema

### [**](#getUpdateSchemaMigrationSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SqlSchemaGenerator.ts#L310)inheritedgetUpdateSchemaMigrationSQL

* ****getUpdateSchemaMigrationSQL**(options): Promise<{ down: string; up: string }>

* Inherited from SqlSchemaGenerator.getUpdateSchemaMigrationSQL

  #### Parameters

  * ##### options: [UpdateSchemaOptions](https://mikro-orm.io/api/core/interface/UpdateSchemaOptions.md)\<DatabaseSchema> = <!-- -->{}

  #### Returns Promise<{ down: string; up: string }>

### [**](#getUpdateSchemaSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SqlSchemaGenerator.ts#L301)inheritedgetUpdateSchemaSQL

* ****getUpdateSchemaSQL**(options): Promise\<string>

* Inherited from SqlSchemaGenerator.getUpdateSchemaSQL

  #### Parameters

  * ##### options: [UpdateSchemaOptions](https://mikro-orm.io/api/core/interface/UpdateSchemaOptions.md)\<DatabaseSchema> = <!-- -->{}

  #### Returns Promise\<string>

### [**](#refresh)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/AbstractSchemaGenerator.ts#L45)inheritedrefresh

* ****refresh**(options): Promise\<void>

* Inherited from SqlSchemaGenerator.refresh

  #### Parameters

  * ##### optionaloptions: [RefreshDatabaseOptions](https://mikro-orm.io/api/core/interface/RefreshDatabaseOptions.md)

  #### Returns Promise\<void>

### [**](#update)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/oracledb/src/OracleSchemaGenerator.ts#L279)update

* ****update**(options): Promise\<void>

* Overrides SqlSchemaGenerator.update

  #### Parameters

  * ##### options: [UpdateSchemaOptions](https://mikro-orm.io/api/core/interface/UpdateSchemaOptions.md)\<DatabaseSchema> = <!-- -->{}

  #### Returns Promise\<void>

### [**](#register)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/oracledb/src/OracleSchemaGenerator.ts#L24)staticregister

* ****register**(orm): void

* Overrides SqlSchemaGenerator.register

  #### Parameters

  * ##### orm: [MikroORM](https://mikro-orm.io/api/core/class/MikroORM.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>, [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>>, (string | [EntitySchema](https://mikro-orm.io/api/core/class/EntitySchema.md)\<any, never, [EntityCtor](https://mikro-orm.io/api/core.md#EntityCtor)\<any>> | [EntityClass](https://mikro-orm.io/api/core.md#EntityClass)\<Partial\<any>>)\[]>

  #### Returns void
