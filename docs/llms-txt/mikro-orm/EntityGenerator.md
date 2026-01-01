# Source: https://mikro-orm.io/api/entity-generator/class/EntityGenerator.md

# EntityGenerator<!-- -->

## Index[**](#Index)

### Constructors

* [**constructor](#constructor)

### Methods

* [**generate](#generate)
* [**register](#register)

## Constructors<!-- -->[**](#Constructors)

### [**](#constructor)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/entity-generator/src/EntityGenerator.ts#L38)constructor

* ****new EntityGenerator**(em): [EntityGenerator](https://mikro-orm.io/api/entity-generator/class/EntityGenerator.md)

- #### Parameters

  * ##### em: [SqlEntityManager](https://mikro-orm.io/api/knex/class/EntityManager.md)<[AbstractSqlDriver](https://mikro-orm.io/api/knex/class/AbstractSqlDriver.md)<[AbstractSqlConnection](https://mikro-orm.io/api/knex/class/AbstractSqlConnection.md), [AbstractSqlPlatform](https://mikro-orm.io/api/knex/class/AbstractSqlPlatform.md)>>

  #### Returns [EntityGenerator](https://mikro-orm.io/api/entity-generator/class/EntityGenerator.md)

## Methods<!-- -->[**](#Methods)

### [**](#generate)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/entity-generator/src/EntityGenerator.ts#L51)generate

* ****generate**(options): Promise\<string\[]>

- #### Parameters

  * ##### options: [GenerateOptions](https://mikro-orm.io/api/core/interface/GenerateOptions.md) = <!-- -->{}

  #### Returns Promise\<string\[]>

### [**](#register)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/entity-generator/src/EntityGenerator.ts#L47)staticregister

* ****register**(orm): void

- #### Parameters

  * ##### orm: [MikroORM](https://mikro-orm.io/api/core/class/MikroORM.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>, [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>>>

  #### Returns void
