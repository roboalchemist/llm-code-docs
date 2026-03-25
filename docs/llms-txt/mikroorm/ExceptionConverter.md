# Source: https://mikro-orm.io/api/core/class/ExceptionConverter.md

# ExceptionConverter<!-- -->

### Hierarchy

* *ExceptionConverter*
  * [OracleExceptionConverter](https://mikro-orm.io/api/oracledb/class/OracleExceptionConverter.md)

## Index[**](#index)

### Constructors

* [**constructor](#constructor)

### Methods

* [**convertException](#convertexception)

## Constructors<!-- -->[**](#constructors)

### [**](#constructor)constructor

* ****new ExceptionConverter**(): [ExceptionConverter](https://mikro-orm.io/api/core/class/ExceptionConverter.md)

* #### Returns [ExceptionConverter](https://mikro-orm.io/api/core/class/ExceptionConverter.md)

## Methods<!-- -->[**](#methods)

### [**](#convertexception)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/ExceptionConverter.ts#L6)convertException

* ****convertException**(exception): [DriverException](https://mikro-orm.io/api/core/class/DriverException.md)

* #### Parameters

  * ##### exception: Error & [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)

  #### Returns [DriverException](https://mikro-orm.io/api/core/class/DriverException.md)
