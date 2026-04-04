# Source: https://mikro-orm.io/api/libsql/class/LibSqlExceptionConverter.md

# LibSqlExceptionConverter<!-- -->

### Hierarchy

* [ExceptionConverter](https://mikro-orm.io/api/core/class/ExceptionConverter.md)
  * *LibSqlExceptionConverter*

## Index[**](#Index)

### Constructors

* [**constructor](#constructor)

### Methods

* [**convertException](#convertException)

## Constructors<!-- -->[**](#Constructors)

### [**](#constructor)constructor

* ****new LibSqlExceptionConverter**(): [LibSqlExceptionConverter](https://mikro-orm.io/api/libsql/class/LibSqlExceptionConverter.md)

- Inherited from ExceptionConverter.constructor

  #### Returns [LibSqlExceptionConverter](https://mikro-orm.io/api/libsql/class/LibSqlExceptionConverter.md)

## Methods<!-- -->[**](#Methods)

### [**](#convertException)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/libsql/src/LibSqlExceptionConverter.ts#L15)convertException

* ****convertException**(exception): [DriverException](https://mikro-orm.io/api/core/class/DriverException.md)

- Overrides ExceptionConverter.convertException

  * **@inheritDoc**

  * **@link**

    <http://www.sqlite.org/c3ref/c_abort.html>

  * **@link**

    <https://github.com/doctrine/dbal/blob/master/src/Driver/AbstractSQLiteDriver.php>

  ***

  #### Parameters

  * ##### exception: Error & [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)

  #### Returns [DriverException](https://mikro-orm.io/api/core/class/DriverException.md)
