# Source: https://mikro-orm.io/api/core/class/ExceptionConverter.md

# ExceptionConverter<!-- -->

### Hierarchy

* *ExceptionConverter*

  * [MySqlExceptionConverter](https://mikro-orm.io/api/knex/class/MySqlExceptionConverter.md)
  * [PostgreSqlExceptionConverter](https://mikro-orm.io/api/postgresql/class/PostgreSqlExceptionConverter.md)
  * [MariaDbExceptionConverter](https://mikro-orm.io/api/mariadb/class/MariaDbExceptionConverter.md)
  * [SqliteExceptionConverter](https://mikro-orm.io/api/sqlite/class/SqliteExceptionConverter.md)
  * [BetterSqliteExceptionConverter](https://mikro-orm.io/api/better-sqlite/class/BetterSqliteExceptionConverter.md)
  * [LibSqlExceptionConverter](https://mikro-orm.io/api/libsql/class/LibSqlExceptionConverter.md)
  * [MsSqlExceptionConverter](https://mikro-orm.io/api/mssql/class/MsSqlExceptionConverter.md)

## Index[**](#Index)

### Constructors

* [**constructor](#constructor)

### Methods

* [**convertException](#convertException)

## Constructors<!-- -->[**](#Constructors)

### [**](#constructor)constructor

* ****new ExceptionConverter**(): [ExceptionConverter](https://mikro-orm.io/api/core/class/ExceptionConverter.md)

- #### Returns [ExceptionConverter](https://mikro-orm.io/api/core/class/ExceptionConverter.md)

## Methods<!-- -->[**](#Methods)

### [**](#convertException)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/ExceptionConverter.ts#L7)convertException

* ****convertException**(exception): [DriverException](https://mikro-orm.io/api/core/class/DriverException.md)

- #### Parameters

  * ##### exception: Error & [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)

  #### Returns [DriverException](https://mikro-orm.io/api/core/class/DriverException.md)
