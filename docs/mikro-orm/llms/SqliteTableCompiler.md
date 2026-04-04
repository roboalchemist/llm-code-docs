# Source: https://mikro-orm.io/api/knex/class/SqliteTableCompiler.md

# SqliteTableCompiler<!-- -->

### Hierarchy

* Sqlite3DialectTableCompiler
  * *SqliteTableCompiler*

## Index[**](#Index)

### Constructors

* [**constructor](#constructor)

### Methods

* [**foreign](#foreign)
* [**foreignKeys](#foreignKeys)

## Constructors<!-- -->[**](#Constructors)

### [**](#constructor)constructor

* ****new SqliteTableCompiler**(): [SqliteTableCompiler](https://mikro-orm.io/api/knex/class/SqliteTableCompiler.md)

- Inherited from MonkeyPatchable.Sqlite3DialectTableCompiler.constructor

  #### Returns [SqliteTableCompiler](https://mikro-orm.io/api/knex/class/SqliteTableCompiler.md)

## Methods<!-- -->[**](#Methods)

### [**](#foreign)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/dialects/sqlite/SqliteTableCompiler.ts#L6)foreign

* ****foreign**(this, foreignInfo): void

- #### Parameters

  * ##### this: any
  * ##### foreignInfo: [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)

  #### Returns void

### [**](#foreignKeys)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/dialects/sqlite/SqliteTableCompiler.ts#L56)foreignKeys

* ****foreignKeys**(this): string

- #### Parameters

  * ##### this: any

  #### Returns string
