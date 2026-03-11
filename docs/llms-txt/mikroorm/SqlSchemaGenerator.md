# Source: https://mikro-orm.io/api/sql/class/SqlSchemaGenerator.md

# SqlSchemaGenerator<!-- -->

### Hierarchy

* AbstractSchemaGenerator<[AbstractSqlDriver](https://mikro-orm.io/api/sql/class/AbstractSqlDriver.md)>
  * *SqlSchemaGenerator*
    * [OracleSchemaGenerator](https://mikro-orm.io/api/oracledb/class/OracleSchemaGenerator.md)

### Implements

* [ISchemaGenerator](https://mikro-orm.io/api/core/interface/ISchemaGenerator.md)

## Index[**](#index)

### Constructors

* [**constructor](#constructor)

### Methods

* [**clear](#clear)
* [**create](#create)
* [**createDatabase](#createdatabase)
* [**createNamespace](#createnamespace)
* [**diffToSQL](#difftosql)
* [**drop](#drop)
* [**dropDatabase](#dropdatabase)
* [**dropNamespace](#dropnamespace)
* [**dropTableIfExists](#droptableifexists)
* [**ensureDatabase](#ensuredatabase)
* [**ensureIndexes](#ensureIndexes)
* [**execute](#execute)
* [**getCreateSchemaSQL](#getcreateschemasql)
* [**getDropSchemaSQL](#getdropschemasql)
* [**getTargetSchema](#gettargetschema)
* [**getUpdateSchemaMigrationSQL](#getupdateschemamigrationsql)
* [**getUpdateSchemaSQL](#getupdateschemasql)
* [**refresh](#refresh)
* [**update](#update)
* [**register](#register)

## Constructors<!-- -->[**](#constructors)

### [**](#constructor)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/AbstractSchemaGenerator.ts#L25)constructor

* ****new SqlSchemaGenerator**(em): [SqlSchemaGenerator](https://mikro-orm.io/api/sql/class/SqlSchemaGenerator.md)

* Inherited from AbstractSchemaGenerator\<AbstractSqlDriver>.constructor

  #### Parameters

  * ##### em: [AbstractSqlDriver](https://mikro-orm.io/api/sql/class/AbstractSqlDriver.md)<[AbstractSqlConnection](https://mikro-orm.io/api/sql/class/AbstractSqlConnection.md), [AbstractSqlPlatform](https://mikro-orm.io/api/sql/class/AbstractSqlPlatform.md)> | [SqlEntityManager](https://mikro-orm.io/api/sql/class/EntityManager.md)<[AbstractSqlDriver](https://mikro-orm.io/api/sql/class/AbstractSqlDriver.md)<[AbstractSqlConnection](https://mikro-orm.io/api/sql/class/AbstractSqlConnection.md), [AbstractSqlPlatform](https://mikro-orm.io/api/sql/class/AbstractSqlPlatform.md)>>

  #### Returns [SqlSchemaGenerator](https://mikro-orm.io/api/sql/class/SqlSchemaGenerator.md)

## Methods<!-- -->[**](#methods)

### [**](#clear)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SqlSchemaGenerator.ts#L179)clear

* ****clear**(options): Promise\<void>

* Implementation of ISchemaGenerator.clear

  Overrides AbstractSchemaGenerator.clear

  #### Parameters

  * ##### optionaloptions: [ClearDatabaseOptions](https://mikro-orm.io/api/core/interface/ClearDatabaseOptions.md)

  #### Returns Promise\<void>

### [**](#create)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SqlSchemaGenerator.ts#L37)create

* ****create**(options): Promise\<void>

* Implementation of ISchemaGenerator.create

  Overrides AbstractSchemaGenerator.create

  #### Parameters

  * ##### optionaloptions: [CreateSchemaOptions](https://mikro-orm.io/api/core/interface/CreateSchemaOptions.md)

  #### Returns Promise\<void>

### [**](#createdatabase)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SqlSchemaGenerator.ts#L525)createDatabase

* ****createDatabase**(name, options): Promise\<void>

* Implementation of ISchemaGenerator.createDatabase

  Overrides AbstractSchemaGenerator.createDatabase

  creates new database and connects to it

  ***

  #### Parameters

  * ##### optionalname: string

  * ##### optionaloptions: { skipOnConnect?<!-- -->: boolean }

    * ##### optionalskipOnConnect: boolean

  #### Returns Promise\<void>

### [**](#createnamespace)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SqlSchemaGenerator.ts#L169)createNamespace

* ****createNamespace**(name): Promise\<void>

* #### Parameters

  * ##### name: string

  #### Returns Promise\<void>

### [**](#difftosql)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SqlSchemaGenerator.ts#L354)diffToSQL

* ****diffToSQL**(schemaDiff, options): string

* #### Parameters

  * ##### schemaDiff: [SchemaDifference](https://mikro-orm.io/api/sql/interface/SchemaDifference.md)

  * ##### options: { dropTables?<!-- -->: boolean; safe?<!-- -->: boolean; schema?<!-- -->: string; wrap?<!-- -->: boolean }

    * ##### optionaldropTables: boolean

    * ##### optionalsafe: boolean

    * ##### optionalschema: string

    * ##### optionalwrap: boolean

  #### Returns string

### [**](#drop)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SqlSchemaGenerator.ts#L159)drop

* ****drop**(options): Promise\<void>

* Implementation of ISchemaGenerator.drop

  Overrides AbstractSchemaGenerator.drop

  #### Parameters

  * ##### options: [DropSchemaOptions](https://mikro-orm.io/api/core/interface/DropSchemaOptions.md) = <!-- -->{}

  #### Returns Promise\<void>

### [**](#dropdatabase)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SqlSchemaGenerator.ts#L537)dropDatabase

* ****dropDatabase**(name): Promise\<void>

* Implementation of ISchemaGenerator.dropDatabase

  Overrides AbstractSchemaGenerator.dropDatabase

  #### Parameters

  * ##### optionalname: string

  #### Returns Promise\<void>

### [**](#dropnamespace)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SqlSchemaGenerator.ts#L174)dropNamespace

* ****dropNamespace**(name): Promise\<void>

* #### Parameters

  * ##### name: string

  #### Returns Promise\<void>

### [**](#droptableifexists)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SqlSchemaGenerator.ts#L587)dropTableIfExists

* ****dropTableIfExists**(name, schema): Promise\<void>

* #### Parameters

  * ##### name: string

  * ##### optionalschema: string

  #### Returns Promise\<void>

### [**](#ensuredatabase)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SqlSchemaGenerator.ts#L46)ensureDatabase

* ****ensureDatabase**(options): Promise\<boolean>

* Implementation of ISchemaGenerator.ensureDatabase

  Overrides AbstractSchemaGenerator.ensureDatabase

  Returns true if the database was created.

  ***

  #### Parameters

  * ##### optionaloptions: [EnsureDatabaseOptions](https://mikro-orm.io/api/core/interface/EnsureDatabaseOptions.md)

  #### Returns Promise\<boolean>

### [**](#ensureIndexes)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/AbstractSchemaGenerator.ts#L121)inheritedensureIndexes

* ****ensureIndexes**(): Promise\<void>

* Implementation of ISchemaGenerator.ensureIndexes

  Inherited from AbstractSchemaGenerator.ensureIndexes

  #### Returns Promise\<void>

### [**](#execute)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SqlSchemaGenerator.ts#L545)execute

* ****execute**(sql, options): Promise\<void>

* Implementation of ISchemaGenerator.execute

  Overrides AbstractSchemaGenerator.execute

  #### Parameters

  * ##### sql: string

  * ##### options: { ctx?<!-- -->: any; wrap?<!-- -->: boolean } = <!-- -->{}

    * ##### optionalctx: any

    * ##### optionalwrap: boolean

  #### Returns Promise\<void>

### [**](#getcreateschemasql)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SqlSchemaGenerator.ts#L98)getCreateSchemaSQL

* ****getCreateSchemaSQL**(options): Promise\<string>

* Implementation of ISchemaGenerator.getCreateSchemaSQL

  Overrides AbstractSchemaGenerator.getCreateSchemaSQL

  #### Parameters

  * ##### options: [CreateSchemaOptions](https://mikro-orm.io/api/core/interface/CreateSchemaOptions.md) = <!-- -->{}

  #### Returns Promise\<string>

### [**](#getdropschemasql)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SqlSchemaGenerator.ts#L217)getDropSchemaSQL

* ****getDropSchemaSQL**(options): Promise\<string>

* Implementation of ISchemaGenerator.getDropSchemaSQL

  Overrides AbstractSchemaGenerator.getDropSchemaSQL

  #### Parameters

  * ##### options: Omit<[DropSchemaOptions](https://mikro-orm.io/api/core/interface/DropSchemaOptions.md), dropDb> = <!-- -->{}

  #### Returns Promise\<string>

### [**](#gettargetschema)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SqlSchemaGenerator.ts#L81)getTargetSchema

* ****getTargetSchema**(schema): DatabaseSchema

* #### Parameters

  * ##### optionalschema: string

  #### Returns DatabaseSchema

### [**](#getupdateschemamigrationsql)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SqlSchemaGenerator.ts#L310)getUpdateSchemaMigrationSQL

* ****getUpdateSchemaMigrationSQL**(options): Promise<{ down: string; up: string }>

* Implementation of ISchemaGenerator.getUpdateSchemaMigrationSQL

  Overrides AbstractSchemaGenerator.getUpdateSchemaMigrationSQL

  #### Parameters

  * ##### options: [UpdateSchemaOptions](https://mikro-orm.io/api/core/interface/UpdateSchemaOptions.md)\<DatabaseSchema> = <!-- -->{}

  #### Returns Promise<{ down: string; up: string }>

### [**](#getupdateschemasql)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SqlSchemaGenerator.ts#L301)getUpdateSchemaSQL

* ****getUpdateSchemaSQL**(options): Promise\<string>

* Implementation of ISchemaGenerator.getUpdateSchemaSQL

  Overrides AbstractSchemaGenerator.getUpdateSchemaSQL

  #### Parameters

  * ##### options: [UpdateSchemaOptions](https://mikro-orm.io/api/core/interface/UpdateSchemaOptions.md)\<DatabaseSchema> = <!-- -->{}

  #### Returns Promise\<string>

### [**](#refresh)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/AbstractSchemaGenerator.ts#L45)inheritedrefresh

* ****refresh**(options): Promise\<void>

* Implementation of ISchemaGenerator.refresh

  Inherited from AbstractSchemaGenerator.refresh

  #### Parameters

  * ##### optionaloptions: [RefreshDatabaseOptions](https://mikro-orm.io/api/core/interface/RefreshDatabaseOptions.md)

  #### Returns Promise\<void>

### [**](#update)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SqlSchemaGenerator.ts#L296)update

* ****update**(options): Promise\<void>

* Implementation of ISchemaGenerator.update

  Overrides AbstractSchemaGenerator.update

  #### Parameters

  * ##### options: [UpdateSchemaOptions](https://mikro-orm.io/api/core/interface/UpdateSchemaOptions.md)\<DatabaseSchema> = <!-- -->{}

  #### Returns Promise\<void>

### [**](#register)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SqlSchemaGenerator.ts#L30)staticregister

* ****register**(orm): void

* #### Parameters

  * ##### orm: [MikroORM](https://mikro-orm.io/api/core/class/MikroORM.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>, [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>>, (string | [EntitySchema](https://mikro-orm.io/api/core/class/EntitySchema.md)\<any, never, [EntityCtor](https://mikro-orm.io/api/core.md#EntityCtor)\<any>> | [EntityClass](https://mikro-orm.io/api/core.md#EntityClass)\<Partial\<any>>)\[]>

  #### Returns void
