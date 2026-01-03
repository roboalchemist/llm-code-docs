# Source: https://mikro-orm.io/api/mongodb/class/MongoSchemaGenerator.md

# MongoSchemaGenerator<!-- -->

### Hierarchy

* [AbstractSchemaGenerator](https://mikro-orm.io/api/core/class/AbstractSchemaGenerator.md)<[MongoDriver](https://mikro-orm.io/api/mongodb/class/MongoDriver.md)>
  * *MongoSchemaGenerator*

## Index[**](#Index)

### Constructors

* [**constructor](#constructor)

### Methods

* [**clearDatabase](#clearDatabase)
* [**createDatabase](#createDatabase)
* [**createSchema](#createSchema)
* [**dropDatabase](#dropDatabase)
* [**dropIndexes](#dropIndexes)
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
* [**register](#register)

## Constructors<!-- -->[**](#Constructors)

### [**](#constructor)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/AbstractSchemaGenerator.ts#L26)constructor

* ****new MongoSchemaGenerator**(em): [MongoSchemaGenerator](https://mikro-orm.io/api/mongodb/class/MongoSchemaGenerator.md)

- Inherited from AbstractSchemaGenerator.constructor

  #### Parameters

  * ##### em: [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>> | [MongoDriver](https://mikro-orm.io/api/mongodb/class/MongoDriver.md)

  #### Returns [MongoSchemaGenerator](https://mikro-orm.io/api/mongodb/class/MongoSchemaGenerator.md)

## Methods<!-- -->[**](#Methods)

### [**](#clearDatabase)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/AbstractSchemaGenerator.ts#L59)inheritedclearDatabase

* ****clearDatabase**(options): Promise\<void>

- Inherited from AbstractSchemaGenerator.clearDatabase

  #### Parameters

  * ##### optionaloptions: [ClearDatabaseOptions](https://mikro-orm.io/api/core/interface/ClearDatabaseOptions.md)

  #### Returns Promise\<void>

### [**](#createDatabase)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/AbstractSchemaGenerator.ts#L106)inheritedcreateDatabase

* ****createDatabase**(name): Promise\<void>

- Inherited from AbstractSchemaGenerator.createDatabase

  creates new database and connects to it

  ***

  #### Parameters

  * ##### optionalname: string

  #### Returns Promise\<void>

### [**](#createSchema)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/mongodb/src/MongoSchemaGenerator.ts#L21)createSchema

* ****createSchema**(options): Promise\<void>

- Overrides AbstractSchemaGenerator.createSchema

  #### Parameters

  * ##### options: [MongoCreateSchemaOptions](https://mikro-orm.io/api/mongodb/interface/MongoCreateSchemaOptions.md) = <!-- -->{}

  #### Returns Promise\<void>

### [**](#dropDatabase)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/AbstractSchemaGenerator.ts#L110)inheriteddropDatabase

* ****dropDatabase**(name): Promise\<void>

- Inherited from AbstractSchemaGenerator.dropDatabase

  #### Parameters

  * ##### optionalname: string

  #### Returns Promise\<void>

### [**](#dropIndexes)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/mongodb/src/MongoSchemaGenerator.ts#L76)dropIndexes

* ****dropIndexes**(options): Promise\<void>

- #### Parameters

  * ##### optionaloptions: { collectionsWithFailedIndexes?<!-- -->: string\[]; skipIndexes?<!-- -->: { collection: string; indexName: string }\[] }
    * ##### optionalcollectionsWithFailedIndexes: string\[]
    * ##### optionalskipIndexes: { collection: string; indexName: string }\[]

  #### Returns Promise\<void>

### [**](#dropSchema)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/mongodb/src/MongoSchemaGenerator.ts#L46)dropSchema

* ****dropSchema**(options): Promise\<void>

- Overrides AbstractSchemaGenerator.dropSchema

  #### Parameters

  * ##### options: { dropMigrationsTable?<!-- -->: boolean } = <!-- -->{}
    * ##### optionaldropMigrationsTable: boolean

  #### Returns Promise\<void>

### [**](#ensureDatabase)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/mongodb/src/MongoSchemaGenerator.ts#L66)ensureDatabase

* ****ensureDatabase**(): Promise\<boolean>

- Overrides AbstractSchemaGenerator.ensureDatabase

  Returns true if the database was created.

  ***

  #### Returns Promise\<boolean>

### [**](#ensureIndexes)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/mongodb/src/MongoSchemaGenerator.ts#L102)ensureIndexes

* ****ensureIndexes**(options): Promise\<void>

- Overrides AbstractSchemaGenerator.ensureIndexes

  #### Parameters

  * ##### options: [EnsureIndexesOptions](https://mikro-orm.io/api/mongodb/interface/EnsureIndexesOptions.md) = <!-- -->{}

  #### Returns Promise\<void>

### [**](#execute)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/AbstractSchemaGenerator.ts#L114)inheritedexecute

* ****execute**(query): Promise\<void>

- Inherited from AbstractSchemaGenerator.execute

  #### Parameters

  * ##### query: string

  #### Returns Promise\<void>

### [**](#getCreateSchemaSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/AbstractSchemaGenerator.ts#L79)inheritedgetCreateSchemaSQL

* ****getCreateSchemaSQL**(options): Promise\<string>

- Inherited from AbstractSchemaGenerator.getCreateSchemaSQL

  #### Parameters

  * ##### optionaloptions: [CreateSchemaOptions](https://mikro-orm.io/api/core/interface/CreateSchemaOptions.md)

  #### Returns Promise\<string>

### [**](#getDropSchemaSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/AbstractSchemaGenerator.ts#L87)inheritedgetDropSchemaSQL

* ****getDropSchemaSQL**(options): Promise\<string>

- Inherited from AbstractSchemaGenerator.getDropSchemaSQL

  #### Parameters

  * ##### optionaloptions: Omit<[DropSchemaOptions](https://mikro-orm.io/api/core/interface/DropSchemaOptions.md), dropDb>

  #### Returns Promise\<string>

### [**](#getUpdateSchemaMigrationSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/AbstractSchemaGenerator.ts#L99)inheritedgetUpdateSchemaMigrationSQL

* ****getUpdateSchemaMigrationSQL**(options): Promise<{ down: string; up: string }>

- Inherited from AbstractSchemaGenerator.getUpdateSchemaMigrationSQL

  #### Parameters

  * ##### optionaloptions: [UpdateSchemaOptions](https://mikro-orm.io/api/core/interface/UpdateSchemaOptions.md)\<unknown>

  #### Returns Promise<{ down: string; up: string }>

### [**](#getUpdateSchemaSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/AbstractSchemaGenerator.ts#L95)inheritedgetUpdateSchemaSQL

* ****getUpdateSchemaSQL**(options): Promise\<string>

- Inherited from AbstractSchemaGenerator.getUpdateSchemaSQL

  #### Parameters

  * ##### optionaloptions: [UpdateSchemaOptions](https://mikro-orm.io/api/core/interface/UpdateSchemaOptions.md)\<unknown>

  #### Returns Promise\<string>

### [**](#refreshDatabase)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/mongodb/src/MongoSchemaGenerator.ts#L70)refreshDatabase

* ****refreshDatabase**(options): Promise\<void>

- Overrides AbstractSchemaGenerator.refreshDatabase

  #### Parameters

  * ##### options: [MongoCreateSchemaOptions](https://mikro-orm.io/api/mongodb/interface/MongoCreateSchemaOptions.md) = <!-- -->{}

  #### Returns Promise\<void>

### [**](#updateSchema)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/mongodb/src/MongoSchemaGenerator.ts#L62)updateSchema

* ****updateSchema**(options): Promise\<void>

- Overrides AbstractSchemaGenerator.updateSchema

  #### Parameters

  * ##### options: [MongoCreateSchemaOptions](https://mikro-orm.io/api/mongodb/interface/MongoCreateSchemaOptions.md) = <!-- -->{}

  #### Returns Promise\<void>

### [**](#register)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/mongodb/src/MongoSchemaGenerator.ts#L17)staticregister

* ****register**(orm): void

- #### Parameters

  * ##### orm: [MikroORM](https://mikro-orm.io/api/core/class/MikroORM.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>, [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>>>

  #### Returns void
