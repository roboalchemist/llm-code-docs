# Source: https://mikro-orm.io/api/mongodb/class/MongoSchemaGenerator.md

# MongoSchemaGenerator<!-- -->

### Hierarchy

* AbstractSchemaGenerator<[MongoDriver](https://mikro-orm.io/api/mongodb/class/MongoDriver.md)>
  * *MongoSchemaGenerator*

## Index[**](#index)

### Constructors

* [**constructor](#constructor)

### Methods

* [**clear](#clear)
* [**create](#create)
* [**createDatabase](#createDatabase)
* [**drop](#drop)
* [**dropDatabase](#dropDatabase)
* [**dropIndexes](#dropindexes)
* [**ensureDatabase](#ensuredatabase)
* [**ensureIndexes](#ensureindexes)
* [**execute](#execute)
* [**getCreateSchemaSQL](#getCreateSchemaSQL)
* [**getDropSchemaSQL](#getDropSchemaSQL)
* [**getUpdateSchemaMigrationSQL](#getUpdateSchemaMigrationSQL)
* [**getUpdateSchemaSQL](#getUpdateSchemaSQL)
* [**refresh](#refresh)
* [**update](#update)
* [**register](#register)

## Constructors<!-- -->[**](#constructors)

### [**](#constructor)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/AbstractSchemaGenerator.ts#L25)constructor

* ****new MongoSchemaGenerator**(em): [MongoSchemaGenerator](https://mikro-orm.io/api/mongodb/class/MongoSchemaGenerator.md)

* Inherited from AbstractSchemaGenerator\<MongoDriver>.constructor

  #### Parameters

  * ##### em: [MongoDriver](https://mikro-orm.io/api/mongodb/class/MongoDriver.md) | [MongoEntityManager](https://mikro-orm.io/api/mongodb/class/EntityManager.md)<[MongoDriver](https://mikro-orm.io/api/mongodb/class/MongoDriver.md)>

  #### Returns [MongoSchemaGenerator](https://mikro-orm.io/api/mongodb/class/MongoSchemaGenerator.md)

## Methods<!-- -->[**](#methods)

### [**](#clear)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/AbstractSchemaGenerator.ts#L60)inheritedclear

* ****clear**(options): Promise\<void>

* Inherited from AbstractSchemaGenerator.clear

  #### Parameters

  * ##### optionaloptions: [ClearDatabaseOptions](https://mikro-orm.io/api/core/interface/ClearDatabaseOptions.md)

  #### Returns Promise\<void>

### [**](#create)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/mongodb/src/MongoSchemaGenerator.ts#L24)create

* ****create**(options): Promise\<void>

* Overrides AbstractSchemaGenerator.create

  #### Parameters

  * ##### options: [MongoCreateSchemaOptions](https://mikro-orm.io/api/mongodb/interface/MongoCreateSchemaOptions.md) = <!-- -->{}

  #### Returns Promise\<void>

### [**](#createDatabase)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/AbstractSchemaGenerator.ts#L109)inheritedcreateDatabase

* ****createDatabase**(name): Promise\<void>

* Inherited from AbstractSchemaGenerator.createDatabase

  creates new database and connects to it

  ***

  #### Parameters

  * ##### optionalname: string

  #### Returns Promise\<void>

### [**](#drop)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/mongodb/src/MongoSchemaGenerator.ts#L51)drop

* ****drop**(options): Promise\<void>

* Overrides AbstractSchemaGenerator.drop

  #### Parameters

  * ##### options: { dropMigrationsTable?<!-- -->: boolean } = <!-- -->{}

    * ##### optionaldropMigrationsTable: boolean

  #### Returns Promise\<void>

### [**](#dropDatabase)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/AbstractSchemaGenerator.ts#L113)inheriteddropDatabase

* ****dropDatabase**(name): Promise\<void>

* Inherited from AbstractSchemaGenerator.dropDatabase

  #### Parameters

  * ##### optionalname: string

  #### Returns Promise\<void>

### [**](#dropindexes)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/mongodb/src/MongoSchemaGenerator.ts#L81)dropIndexes

* ****dropIndexes**(options): Promise\<void>

* #### Parameters

  * ##### optionaloptions: { collectionsWithFailedIndexes?<!-- -->: string\[]; skipIndexes?<!-- -->: { collection: string; indexName: string }\[] }

    * ##### optionalcollectionsWithFailedIndexes: string\[]

    * ##### optionalskipIndexes: { collection: string; indexName: string }\[]

  #### Returns Promise\<void>

### [**](#ensuredatabase)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/mongodb/src/MongoSchemaGenerator.ts#L71)ensureDatabase

* ****ensureDatabase**(): Promise\<boolean>

* Overrides AbstractSchemaGenerator.ensureDatabase

  Returns true if the database was created.

  ***

  #### Returns Promise\<boolean>

### [**](#ensureindexes)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/mongodb/src/MongoSchemaGenerator.ts#L113)ensureIndexes

* ****ensureIndexes**(options): Promise\<void>

* Overrides AbstractSchemaGenerator.ensureIndexes

  #### Parameters

  * ##### options: [EnsureIndexesOptions](https://mikro-orm.io/api/mongodb/interface/EnsureIndexesOptions.md) = <!-- -->{}

  #### Returns Promise\<void>

### [**](#execute)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/AbstractSchemaGenerator.ts#L117)inheritedexecute

* ****execute**(query): Promise\<void>

* Inherited from AbstractSchemaGenerator.execute

  #### Parameters

  * ##### query: string

  #### Returns Promise\<void>

### [**](#getCreateSchemaSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/AbstractSchemaGenerator.ts#L82)inheritedgetCreateSchemaSQL

* ****getCreateSchemaSQL**(options): Promise\<string>

* Inherited from AbstractSchemaGenerator.getCreateSchemaSQL

  #### Parameters

  * ##### optionaloptions: [CreateSchemaOptions](https://mikro-orm.io/api/core/interface/CreateSchemaOptions.md)

  #### Returns Promise\<string>

### [**](#getDropSchemaSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/AbstractSchemaGenerator.ts#L90)inheritedgetDropSchemaSQL

* ****getDropSchemaSQL**(options): Promise\<string>

* Inherited from AbstractSchemaGenerator.getDropSchemaSQL

  #### Parameters

  * ##### optionaloptions: Omit<[DropSchemaOptions](https://mikro-orm.io/api/core/interface/DropSchemaOptions.md), dropDb>

  #### Returns Promise\<string>

### [**](#getUpdateSchemaMigrationSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/AbstractSchemaGenerator.ts#L102)inheritedgetUpdateSchemaMigrationSQL

* ****getUpdateSchemaMigrationSQL**(options): Promise<{ down: string; up: string }>

* Inherited from AbstractSchemaGenerator.getUpdateSchemaMigrationSQL

  #### Parameters

  * ##### optionaloptions: [UpdateSchemaOptions](https://mikro-orm.io/api/core/interface/UpdateSchemaOptions.md)\<unknown>

  #### Returns Promise<{ down: string; up: string }>

### [**](#getUpdateSchemaSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/AbstractSchemaGenerator.ts#L98)inheritedgetUpdateSchemaSQL

* ****getUpdateSchemaSQL**(options): Promise\<string>

* Inherited from AbstractSchemaGenerator.getUpdateSchemaSQL

  #### Parameters

  * ##### optionaloptions: [UpdateSchemaOptions](https://mikro-orm.io/api/core/interface/UpdateSchemaOptions.md)\<unknown>

  #### Returns Promise\<string>

### [**](#refresh)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/mongodb/src/MongoSchemaGenerator.ts#L75)refresh

* ****refresh**(options): Promise\<void>

* Overrides AbstractSchemaGenerator.refresh

  #### Parameters

  * ##### options: [MongoCreateSchemaOptions](https://mikro-orm.io/api/mongodb/interface/MongoCreateSchemaOptions.md) = <!-- -->{}

  #### Returns Promise\<void>

### [**](#update)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/mongodb/src/MongoSchemaGenerator.ts#L67)update

* ****update**(options): Promise\<void>

* Overrides AbstractSchemaGenerator.update

  #### Parameters

  * ##### options: [MongoCreateSchemaOptions](https://mikro-orm.io/api/mongodb/interface/MongoCreateSchemaOptions.md) = <!-- -->{}

  #### Returns Promise\<void>

### [**](#register)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/mongodb/src/MongoSchemaGenerator.ts#L17)staticregister

* ****register**(orm): void

* #### Parameters

  * ##### orm: [MikroORM](https://mikro-orm.io/api/core/class/MikroORM.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>, [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>>, (string | [EntitySchema](https://mikro-orm.io/api/core/class/EntitySchema.md)\<any, never, [EntityCtor](https://mikro-orm.io/api/core.md#EntityCtor)\<any>> | [EntityClass](https://mikro-orm.io/api/core.md#EntityClass)\<Partial\<any>>)\[]>

  #### Returns void
