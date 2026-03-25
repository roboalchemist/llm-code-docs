# Source: https://mikro-orm.io/api/migrations/class/Migration.md

# abstractMigration<!-- -->

## Index[**](#index)

### Constructors

* [**constructor](#constructor)

### Methods

* [**addSql](#addsql)
* [**down](#down)
* [**execute](#execute)
* [**getEntityManager](#getentitymanager)
* [**getQueries](#getqueries)
* [**isTransactional](#istransactional)
* [**reset](#reset)
* [**setTransactionContext](#settransactioncontext)
* [**up](#up)

## Constructors<!-- -->[**](#constructors)

### [**](#constructor)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/migrations/src/Migration.ts#L17)constructor

* ****new Migration**(driver, config): [Migration](https://mikro-orm.io/api/migrations/class/Migration.md)

* #### Parameters

  * ##### driver: [AbstractSqlDriver](https://mikro-orm.io/api/sql/class/AbstractSqlDriver.md)<[AbstractSqlConnection](https://mikro-orm.io/api/sql/class/AbstractSqlConnection.md), [AbstractSqlPlatform](https://mikro-orm.io/api/sql/class/AbstractSqlPlatform.md)>

  * ##### config: [Configuration](https://mikro-orm.io/api/core/class/Configuration.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>, [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>>>

  #### Returns [Migration](https://mikro-orm.io/api/migrations/class/Migration.md)

## Methods<!-- -->[**](#methods)

### [**](#addsql)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/migrations/src/Migration.ts#L32)addSql

* ****addSql**(sql): void

* #### Parameters

  * ##### sql: [Query](https://mikro-orm.io/api/migrations.md#Query)

  #### Returns void

### [**](#down)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/migrations/src/Migration.ts#L24)down

* ****down**(): void | Promise\<void>

* #### Returns void | Promise\<void>

### [**](#execute)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/migrations/src/Migration.ts#L49)execute

* ****execute**(sql, params): Promise<[EntityData](https://mikro-orm.io/api/core.md#EntityData)\<Partial\<any>>\[]>

* Executes a raw SQL query. Accepts a string SQL, `raw()` SQL fragment, or a native query builder instance. The `params` parameter is respected only if you use string SQL in the first parameter.

  ***

  #### Parameters

  * ##### sql: [Query](https://mikro-orm.io/api/migrations.md#Query)

  * ##### optionalparams: unknown\[]

  #### Returns Promise<[EntityData](https://mikro-orm.io/api/core.md#EntityData)\<Partial\<any>>\[]>

### [**](#getentitymanager)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/migrations/src/Migration.ts#L57)getEntityManager

* ****getEntityManager**(): [SqlEntityManager](https://mikro-orm.io/api/sql/class/EntityManager.md)<[AbstractSqlDriver](https://mikro-orm.io/api/sql/class/AbstractSqlDriver.md)<[AbstractSqlConnection](https://mikro-orm.io/api/sql/class/AbstractSqlConnection.md), [AbstractSqlPlatform](https://mikro-orm.io/api/sql/class/AbstractSqlPlatform.md)>>

* Creates a cached `EntityManager` instance for this migration, which will respect the current transaction context.

  ***

  #### Returns [SqlEntityManager](https://mikro-orm.io/api/sql/class/EntityManager.md)<[AbstractSqlDriver](https://mikro-orm.io/api/sql/class/AbstractSqlDriver.md)<[AbstractSqlConnection](https://mikro-orm.io/api/sql/class/AbstractSqlConnection.md), [AbstractSqlPlatform](https://mikro-orm.io/api/sql/class/AbstractSqlPlatform.md)>>

### [**](#getqueries)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/migrations/src/Migration.ts#L66)getQueries

* ****getQueries**(): [Query](https://mikro-orm.io/api/migrations.md#Query)\[]

* #### Returns [Query](https://mikro-orm.io/api/migrations.md#Query)\[]

### [**](#istransactional)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/migrations/src/Migration.ts#L28)isTransactional

* ****isTransactional**(): boolean

* #### Returns boolean

### [**](#reset)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/migrations/src/Migration.ts#L36)reset

* ****reset**(): void

* #### Returns void

### [**](#settransactioncontext)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/migrations/src/Migration.ts#L41)setTransactionContext

* ****setTransactionContext**(ctx): void

* #### Parameters

  * ##### ctx: any

  #### Returns void

### [**](#up)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/migrations/src/Migration.ts#L22)abstractup

* ****up**(): void | Promise\<void>

* #### Returns void | Promise\<void>
