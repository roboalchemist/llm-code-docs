# Source: https://mikro-orm.io/api/knex/class/MariaDbKnexDialect.md

# MariaDbKnexDialect<!-- -->

### Hierarchy

* [MySqlKnexDialect](https://mikro-orm.io/api/knex/class/MySqlKnexDialect.md)
  * *MariaDbKnexDialect*

## Index[**](#Index)

### Constructors

* [**constructor](#constructor)

### Accessors

* [**driverName](#driverName)

### Methods

* [**\_driver](#_driver)
* [**columnCompiler](#columnCompiler)
* [**queryCompiler](#queryCompiler)
* [**validateConnection](#validateConnection)

## Constructors<!-- -->[**](#Constructors)

### [**](#constructor)constructor

* ****new MariaDbKnexDialect**(): [MariaDbKnexDialect](https://mikro-orm.io/api/knex/class/MariaDbKnexDialect.md)

- Inherited from MySqlKnexDialect.constructor

  #### Returns [MariaDbKnexDialect](https://mikro-orm.io/api/knex/class/MariaDbKnexDialect.md)

## Accessors<!-- -->[**](#Accessors)

### [**](#driverName)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/dialects/mysql/MariaDbKnexDialect.ts#L5)driverName

* **get driverName(): string

- #### Returns string

## Methods<!-- -->[**](#Methods)

### [**](#_driver)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/dialects/mysql/MariaDbKnexDialect.ts#L9)\_driver

* ****\_driver**(): any

- #### Returns any

### [**](#columnCompiler)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/dialects/mysql/MySqlKnexDialect.ts#L12)inheritedcolumnCompiler

* ****columnCompiler**(): any

- Inherited from MySqlKnexDialect.columnCompiler

  #### Returns any

### [**](#queryCompiler)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/dialects/mysql/MySqlKnexDialect.ts#L7)inheritedqueryCompiler

* ****queryCompiler**(): any

- Inherited from MySqlKnexDialect.queryCompiler

  #### Returns any

### [**](#validateConnection)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/dialects/mysql/MariaDbKnexDialect.ts#L13)validateConnection

* ****validateConnection**(connection): any

- #### Parameters

  * ##### connection: any

  #### Returns any
