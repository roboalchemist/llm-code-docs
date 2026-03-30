# Source: https://mikro-orm.io/api/oracledb/class/OracleExceptionConverter.md

# OracleExceptionConverter<!-- -->

### Hierarchy

* [ExceptionConverter](https://mikro-orm.io/api/core/class/ExceptionConverter.md)
  * *OracleExceptionConverter*

## Index[**](#index)

### Constructors

* [**constructor](#constructor)

### Methods

* [**convertException](#convertexception)

## Constructors<!-- -->[**](#constructors)

### [**](#constructor)constructor

* ****new OracleExceptionConverter**(): [OracleExceptionConverter](https://mikro-orm.io/api/oracledb/class/OracleExceptionConverter.md)

* Inherited from ExceptionConverter.constructor

  #### Returns [OracleExceptionConverter](https://mikro-orm.io/api/oracledb/class/OracleExceptionConverter.md)

## Methods<!-- -->[**](#methods)

### [**](#convertexception)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/oracledb/src/OracleExceptionConverter.ts#L26)convertException

* ****convertException**(exception): [DriverException](https://mikro-orm.io/api/core/class/DriverException.md)

* Overrides ExceptionConverter.convertException

  * **@link**

    <https://docs.oracle.com/cd/B28359_01/server.111/b28278/toc.htm>

  ***

  #### Parameters

  * ##### exception: Error & [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)

  #### Returns [DriverException](https://mikro-orm.io/api/core/class/DriverException.md)
