# Source: https://mikro-orm.io/api/core/class/TransactionEventBroadcaster.md

# TransactionEventBroadcaster<!-- -->

## Index[**](#index)

### Constructors

* [**constructor](#constructor)

### Properties

* [**context](#context)

### Methods

* [**dispatchEvent](#dispatchevent)

## Constructors<!-- -->[**](#constructors)

### [**](#constructor)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/events/TransactionEventBroadcaster.ts#L6)constructor

* ****new TransactionEventBroadcaster**(em, context): [TransactionEventBroadcaster](https://mikro-orm.io/api/core/class/TransactionEventBroadcaster.md)

* #### Parameters

  * ##### em: [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>>

  * ##### optionalcontext: { topLevelTransaction?<!-- -->: boolean }

    * ##### optionaltopLevelTransaction: boolean

  #### Returns [TransactionEventBroadcaster](https://mikro-orm.io/api/core/class/TransactionEventBroadcaster.md)

## Properties<!-- -->[**](#properties)

### [**](#context)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/events/TransactionEventBroadcaster.ts#L8)optionalreadonlycontext

**context?

<!-- -->

: { topLevelTransaction?

<!-- -->

: boolean }

#### Type declaration

* ##### optionaltopLevelTransaction?<!-- -->: boolean

## Methods<!-- -->[**](#methods)

### [**](#dispatchevent)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/events/TransactionEventBroadcaster.ts#L11)dispatchEvent

* ****dispatchEvent**(event, transaction): Promise\<void>

* #### Parameters

  * ##### event: [TransactionEventType](https://mikro-orm.io/api/core.md#TransactionEventType)

  * ##### optionaltransaction: any

  #### Returns Promise\<void>
