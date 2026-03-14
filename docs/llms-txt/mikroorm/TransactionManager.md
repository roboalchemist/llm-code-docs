# Source: https://mikro-orm.io/api/core/class/TransactionManager.md

# TransactionManager<!-- -->

Manages transaction lifecycle and propagation for EntityManager.

## Index[**](#index)

### Constructors

* [**constructor](#constructor)

### Methods

* [**handle](#handle)

## Constructors<!-- -->[**](#constructors)

### [**](#constructor)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/TransactionManager.ts#L16)constructor

* ****new TransactionManager**(em): [TransactionManager](https://mikro-orm.io/api/core/class/TransactionManager.md)

* #### Parameters

  * ##### em: [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>>

  #### Returns [TransactionManager](https://mikro-orm.io/api/core/class/TransactionManager.md)

## Methods<!-- -->[**](#methods)

### [**](#handle)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/TransactionManager.ts#L21)handle

* ****handle**\<T>(cb, options): Promise\<T>

* Main entry point for handling transactional operations with propagation support.

  ***

  #### Parameters

  * ##### cb: (em) => T | Promise\<T>

  *

    ##### options: [TransactionOptions](https://mikro-orm.io/api/core/interface/TransactionOptions.md) = <!-- -->{}

  #### Returns Promise\<T>
