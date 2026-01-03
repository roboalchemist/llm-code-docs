# Source: https://mikro-orm.io/api/knex/class/SqliteKnexDialect.md

# SqliteKnexDialect<!-- -->

### Hierarchy

* Sqlite3Dialect
  * *SqliteKnexDialect*

## Index[**](#Index)

### Constructors

* [**constructor](#constructor)

### Methods

* [**\_query](#_query)
* [**processResponse](#processResponse)
* [**tableCompiler](#tableCompiler)

## Constructors<!-- -->[**](#Constructors)

### [**](#constructor)constructor

* ****new SqliteKnexDialect**(): [SqliteKnexDialect](https://mikro-orm.io/api/knex/class/SqliteKnexDialect.md)

- Inherited from MonkeyPatchable.Sqlite3Dialect.constructor

  #### Returns [SqliteKnexDialect](https://mikro-orm.io/api/knex/class/SqliteKnexDialect.md)

## Methods<!-- -->[**](#Methods)

### [**](#_query)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/dialects/sqlite/SqliteKnexDialect.ts#L19)\_query

* ****\_query**(connection, obj): Promise\<unknown>

- #### Parameters

  * ##### connection: any
  * ##### obj: any

  #### Returns Promise\<unknown>

### [**](#processResponse)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/dialects/sqlite/SqliteKnexDialect.ts#L11)processResponse

* ****processResponse**(obj, runner): any

- #### Parameters

  * ##### obj: any
  * ##### runner: any

  #### Returns any

### [**](#tableCompiler)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/dialects/sqlite/SqliteKnexDialect.ts#L6)tableCompiler

* ****tableCompiler**(): any

- #### Returns any
