# Source: https://mikro-orm.io/api/knex/class/LibSqlKnexDialect.md

# LibSqlKnexDialect<!-- -->

### Hierarchy

* BetterSqlite3Dialect
  * *LibSqlKnexDialect*

## Index[**](#Index)

### Constructors

* [**constructor](#constructor)

### Accessors

* [**driverName](#driverName)

### Methods

* [**\_driver](#_driver)
* [**\_query](#_query)
* [**acquireRawConnection](#acquireRawConnection)
* [**tableCompiler](#tableCompiler)
* [**validateConnection](#validateConnection)

## Constructors<!-- -->[**](#Constructors)

### [**](#constructor)constructor

* ****new LibSqlKnexDialect**(): [LibSqlKnexDialect](https://mikro-orm.io/api/knex/class/LibSqlKnexDialect.md)

- Inherited from MonkeyPatchable.BetterSqlite3Dialect.constructor

  #### Returns [LibSqlKnexDialect](https://mikro-orm.io/api/knex/class/LibSqlKnexDialect.md)

## Accessors<!-- -->[**](#Accessors)

### [**](#driverName)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/dialects/sqlite/LibSqlKnexDialect.ts#L6)driverName

* **get driverName(): string

- #### Returns string

## Methods<!-- -->[**](#Methods)

### [**](#_driver)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/dialects/sqlite/LibSqlKnexDialect.ts#L10)\_driver

* ****\_driver**(): any

- #### Returns any

### [**](#_query)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/dialects/sqlite/LibSqlKnexDialect.ts#L14)\_query

* ****\_query**(this, connection, obj): Promise\<any>

- #### Parameters

  * ##### this: any
  * ##### connection: any
  * ##### obj: any

  #### Returns Promise\<any>

### [**](#acquireRawConnection)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/dialects/sqlite/LibSqlKnexDialect.ts#L38)acquireRawConnection

* ****acquireRawConnection**(this): Promise\<any>

- #### Parameters

  * ##### this: any

  #### Returns Promise\<any>

### [**](#tableCompiler)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/dialects/sqlite/LibSqlKnexDialect.ts#L47)tableCompiler

* ****tableCompiler**(): any

- #### Returns any

### [**](#validateConnection)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/dialects/sqlite/LibSqlKnexDialect.ts#L52)validateConnection

* ****validateConnection**(connection): boolean

- #### Parameters

  * ##### connection: any

  #### Returns boolean
