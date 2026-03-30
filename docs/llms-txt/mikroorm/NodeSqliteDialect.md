# Source: https://mikro-orm.io/api/sql/class/NodeSqliteDialect.md

# NodeSqliteDialect<!-- -->

Kysely dialect for `node:sqlite` (Node.js 22.5+, Deno 2.2+).

Bridges `node:sqlite`'s `DatabaseSync` to the `better-sqlite3` interface that Kysely's `SqliteDialect` expects.

* **@example**

  ```
  import { SqliteDriver, NodeSqliteDialect } from '@mikro-orm/sql';

  const orm = await MikroORM.init({
    driver: SqliteDriver,
    dbName: ':memory:',
    driverOptions: new NodeSqliteDialect(':memory:'),
  });
  ```

### Hierarchy

* SqliteDialect
  * *NodeSqliteDialect*

## Index[**](#index)

### Constructors

* [**constructor](#constructor)

### Methods

* [**createAdapter](#createAdapter)
* [**createDriver](#createDriver)
* [**createIntrospector](#createIntrospector)
* [**createQueryCompiler](#createQueryCompiler)

## Constructors<!-- -->[**](#constructors)

### [**](#constructor)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/dialects/sqlite/NodeSqliteDialect.ts#L21)constructor

* ****new NodeSqliteDialect**(dbName): [NodeSqliteDialect](https://mikro-orm.io/api/sql/class/NodeSqliteDialect.md)

* Overrides SqliteDialect.constructor

  #### Parameters

  * ##### dbName: string

  #### Returns [NodeSqliteDialect](https://mikro-orm.io/api/sql/class/NodeSqliteDialect.md)

## Methods<!-- -->[**](#methods)

### [**](#createAdapter)inheritedcreateAdapter

* ****createAdapter**(): DialectAdapter

* Inherited from SqliteDialect.createAdapter

  Creates an adapter for the dialect.

  ***

  #### Returns DialectAdapter

### [**](#createDriver)inheritedcreateDriver

* ****createDriver**(): Driver

* Inherited from SqliteDialect.createDriver

  Creates a driver for the dialect.

  ***

  #### Returns Driver

### [**](#createIntrospector)inheritedcreateIntrospector

* ****createIntrospector**(db): DatabaseIntrospector

* Inherited from SqliteDialect.createIntrospector

  Creates a database introspector that can be used to get database metadata such as the table names and column names of those tables.

  `db` never has any plugins installed. It's created using [Kysely.withoutPlugins](https://mikro-orm.io/api/sql/class/Kysely.md#withoutPlugins).

  ***

  #### Parameters

  * ##### db: [Kysely](https://mikro-orm.io/api/sql/class/Kysely.md)\<any>

  #### Returns DatabaseIntrospector

### [**](#createQueryCompiler)inheritedcreateQueryCompiler

* ****createQueryCompiler**(): QueryCompiler

* Inherited from SqliteDialect.createQueryCompiler

  Creates a query compiler for the dialect.

  ***

  #### Returns QueryCompiler
