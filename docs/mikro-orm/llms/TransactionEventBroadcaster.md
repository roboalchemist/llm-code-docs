# Source: https://mikro-orm.io/api/core/class/TransactionEventBroadcaster.md

# TransactionEventBroadcaster<!-- -->

## Index[**](#Index)

### Constructors

* [**constructor](#constructor)

### Properties

* [**context](#context)

### Methods

* [**dispatchEvent](#dispatchEvent)
* [**isTopLevel](#isTopLevel)

## Constructors<!-- -->[**](#Constructors)

### [**](#constructor)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/events/TransactionEventBroadcaster.ts#L11)constructor

* ****new TransactionEventBroadcaster**(em, uow, context): [TransactionEventBroadcaster](https://mikro-orm.io/api/core/class/TransactionEventBroadcaster.md)

- #### Parameters

  * ##### em: [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>>
  * ##### optionaluow: [UnitOfWork](https://mikro-orm.io/api/core/class/UnitOfWork.md)
  * ##### optionalcontext: { topLevelTransaction?<!-- -->: boolean }
    * ##### optionaltopLevelTransaction: boolean

  #### Returns [TransactionEventBroadcaster](https://mikro-orm.io/api/core/class/TransactionEventBroadcaster.md)

## Properties<!-- -->[**](#Properties)

### [**](#context)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/events/TransactionEventBroadcaster.ts#L13)optionalreadonlycontext

**context?

<!-- -->

: { topLevelTransaction?

<!-- -->

: boolean }

#### Type declaration

* ##### optionaltopLevelTransaction?<!-- -->: boolean

## Methods<!-- -->[**](#Methods)

### [**](#dispatchEvent)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/events/TransactionEventBroadcaster.ts#L17)dispatchEvent

* ****dispatchEvent**(event, transaction): Promise\<void>

- #### Parameters

  * ##### event: [TransactionEventType](https://mikro-orm.io/api/core.md#TransactionEventType)
  * ##### optionaltransaction: any

  #### Returns Promise\<void>

### [**](#isTopLevel)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/events/TransactionEventBroadcaster.ts#L21)isTopLevel

* ****isTopLevel**(): boolean

- #### Returns boolean
