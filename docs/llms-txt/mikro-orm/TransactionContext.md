# Source: https://mikro-orm.io/api/core/class/TransactionContext.md

# TransactionContext<!-- -->

## Index[**](#Index)

### Constructors

* [**constructor](#constructor)

### Properties

* [**em](#em)
* [**id](#id)

### Methods

* [**create](#create)
* [**currentTransactionContext](#currentTransactionContext)
* [**getEntityManager](#getEntityManager)

## Constructors<!-- -->[**](#Constructors)

### [**](#constructor)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/TransactionContext.ts#L9)constructor

* ****new TransactionContext**(em): [TransactionContext](https://mikro-orm.io/api/core/class/TransactionContext.md)

- #### Parameters

  * ##### em: [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>>

  #### Returns [TransactionContext](https://mikro-orm.io/api/core/class/TransactionContext.md)

## Properties<!-- -->[**](#Properties)

### [**](#em)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/TransactionContext.ts#L9)readonlyem

**em: [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>>

### [**](#id)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/TransactionContext.ts#L7)readonlyid

**id: number

## Methods<!-- -->[**](#Methods)

### [**](#create)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/TransactionContext.ts#L16)staticcreate

* ****create**\<T>(em, next): T

- Creates new TransactionContext instance and runs the code inside its domain.

  ***

  #### Parameters

  * ##### em: [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>>
  * ##### next: (...args) => T


  #### Returns T

### [**](#currentTransactionContext)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/TransactionContext.ts#L24)staticcurrentTransactionContext

* ****currentTransactionContext**(): undefined | [TransactionContext](https://mikro-orm.io/api/core/class/TransactionContext.md)

- Returns current TransactionContext (if available).

  ***

  #### Returns undefined | [TransactionContext](https://mikro-orm.io/api/core/class/TransactionContext.md)

### [**](#getEntityManager)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/TransactionContext.ts#L31)staticgetEntityManager

* ****getEntityManager**(name): undefined | [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>>

- Returns current EntityManager (if available).

  ***

  #### Parameters

  * ##### name: string = <!-- -->'default'

  #### Returns undefined | [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>>
