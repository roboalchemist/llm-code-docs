# Source: https://mikro-orm.io/api/sql/class/OracleDialect.md

# OracleDialect<!-- -->

### Implements

* Dialect

## Index[**](#index)

### Constructors

* [**constructor](#constructor)

### Methods

* [**createAdapter](#createadapter)
* [**createDriver](#createdriver)
* [**createIntrospector](#createintrospector)
* [**createQueryCompiler](#createquerycompiler)

## Constructors<!-- -->[**](#constructors)

### [**](#constructor)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/dialects/oracledb/OracleDialect.ts#L249)constructor

* ****new OracleDialect**(config): [OracleDialect](https://mikro-orm.io/api/sql/class/OracleDialect.md)

* #### Parameters

  * ##### config: [OracleDialectConfig](https://mikro-orm.io/api/sql/interface/OracleDialectConfig.md)

  #### Returns [OracleDialect](https://mikro-orm.io/api/sql/class/OracleDialect.md)

## Methods<!-- -->[**](#methods)

### [**](#createadapter)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/dialects/oracledb/OracleDialect.ts#L257)createAdapter

* ****createAdapter**(): OracleAdapter

* Implementation of Dialect.createAdapter

  Creates an adapter for the dialect.

  ***

  #### Returns OracleAdapter

### [**](#createdriver)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/dialects/oracledb/OracleDialect.ts#L253)createDriver

* ****createDriver**(): OracleDriver

* Implementation of Dialect.createDriver

  Creates a driver for the dialect.

  ***

  #### Returns OracleDriver

### [**](#createintrospector)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/dialects/oracledb/OracleDialect.ts#L261)createIntrospector

* ****createIntrospector**(db): DatabaseIntrospector

* Implementation of Dialect.createIntrospector

  Creates a database introspector that can be used to get database metadata such as the table names and column names of those tables.

  `db` never has any plugins installed. It's created using [Kysely.withoutPlugins](https://mikro-orm.io/api/sql/class/Kysely.md#withoutPlugins).

  ***

  #### Parameters

  * ##### db: [Kysely](https://mikro-orm.io/api/sql/class/Kysely.md)\<any>

  #### Returns DatabaseIntrospector

### [**](#createquerycompiler)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/dialects/oracledb/OracleDialect.ts#L265)createQueryCompiler

* ****createQueryCompiler**(): OracleQueryCompiler

* Implementation of Dialect.createQueryCompiler

  Creates a query compiler for the dialect.

  ***

  #### Returns OracleQueryCompiler
