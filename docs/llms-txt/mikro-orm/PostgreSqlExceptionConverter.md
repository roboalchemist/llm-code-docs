# Source: https://mikro-orm.io/api/postgresql/class/PostgreSqlExceptionConverter.md

# PostgreSqlExceptionConverter<!-- -->

### Hierarchy

* [ExceptionConverter](https://mikro-orm.io/api/core/class/ExceptionConverter.md)
  * *PostgreSqlExceptionConverter*

## Index[**](#Index)

### Constructors

* [**constructor](#constructor)

### Methods

* [**convertException](#convertException)

## Constructors<!-- -->[**](#Constructors)

### [**](#constructor)constructor

* ****new PostgreSqlExceptionConverter**(): [PostgreSqlExceptionConverter](https://mikro-orm.io/api/postgresql/class/PostgreSqlExceptionConverter.md)

- Inherited from ExceptionConverter.constructor

  #### Returns [PostgreSqlExceptionConverter](https://mikro-orm.io/api/postgresql/class/PostgreSqlExceptionConverter.md)

## Methods<!-- -->[**](#Methods)

### [**](#convertException)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/postgresql/src/PostgreSqlExceptionConverter.ts#L14)convertException

* ****convertException**(exception): [DriverException](https://mikro-orm.io/api/core/class/DriverException.md)

- Overrides ExceptionConverter.convertException

  * **@link**

    <http://www.postgresql.org/docs/9.4/static/errcodes-appendix.html>

  * **@link**

    <https://github.com/doctrine/dbal/blob/master/src/Driver/AbstractPostgreSQLDriver.php>

  ***

  #### Parameters

  * ##### exception: Error & [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)

  #### Returns [DriverException](https://mikro-orm.io/api/core/class/DriverException.md)
