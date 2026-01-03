# Source: https://mikro-orm.io/api/knex/class/PostgreSqlKnexDialect.md

# PostgreSqlKnexDialect<!-- -->

### Hierarchy

* PostgresDialect
  * *PostgreSqlKnexDialect*

## Index[**](#Index)

### Constructors

* [**constructor](#constructor)

### Properties

* [**ormConfig](#ormConfig)

### Methods

* [**queryCompiler](#queryCompiler)
* [**tableCompiler](#tableCompiler)

## Constructors<!-- -->[**](#Constructors)

### [**](#constructor)constructor

* ****new PostgreSqlKnexDialect**(): [PostgreSqlKnexDialect](https://mikro-orm.io/api/knex/class/PostgreSqlKnexDialect.md)

- Inherited from MonkeyPatchable.PostgresDialect.constructor

  #### Returns [PostgreSqlKnexDialect](https://mikro-orm.io/api/knex/class/PostgreSqlKnexDialect.md)

## Properties<!-- -->[**](#Properties)

### [**](#ormConfig)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/dialects/postgresql/PostgreSqlKnexDialect.ts#L8)ormConfig

**ormConfig: [Configuration](https://mikro-orm.io/api/core/class/Configuration.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>, [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>>>

## Methods<!-- -->[**](#Methods)

### [**](#queryCompiler)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/dialects/postgresql/PostgreSqlKnexDialect.ts#L18)queryCompiler

* ****queryCompiler**(): any

- #### Returns any

### [**](#tableCompiler)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/dialects/postgresql/PostgreSqlKnexDialect.ts#L10)tableCompiler

* ****tableCompiler**(): any

- #### Returns any
