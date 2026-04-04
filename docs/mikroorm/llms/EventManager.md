# Source: https://mikro-orm.io/api/core/class/EventManager.md

# EventManager<!-- -->

## Index[**](#index)

### Constructors

* [**constructor](#constructor)

### Methods

* [**clone](#clone)
* [**dispatchEvent](#dispatchevent)
* [**getSubscribers](#getsubscribers)
* [**hasListeners](#haslisteners)
* [**registerSubscriber](#registersubscriber)

## Constructors<!-- -->[**](#constructors)

### [**](#constructor)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/events/EventManager.ts#L12)constructor

* ****new EventManager**(subscribers): [EventManager](https://mikro-orm.io/api/core/class/EventManager.md)

* #### Parameters

  * ##### subscribers: Iterable<[EventSubscriber](https://mikro-orm.io/api/core/interface/EventSubscriber.md)\<any>, any, any>

  #### Returns [EventManager](https://mikro-orm.io/api/core/class/EventManager.md)

## Methods<!-- -->[**](#methods)

### [**](#clone)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/events/EventManager.ts#L118)clone

* ****clone**(): [EventManager](https://mikro-orm.io/api/core/class/EventManager.md)

* #### Returns [EventManager](https://mikro-orm.io/api/core/class/EventManager.md)

### [**](#dispatchevent)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/events/EventManager.ts#L38)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/events/EventManager.ts#L43)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/events/EventManager.ts#L48)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/events/EventManager.ts#L53)dispatchEvent

* ****dispatchEvent**\<T>(event, args, meta): unknown
* ****dispatchEvent**\<T>(event, args, meta): unknown
* ****dispatchEvent**\<T>(event, args, meta): Promise\<unknown>

* #### Parameters

  * ##### event: [TransactionEventType](https://mikro-orm.io/api/core.md#TransactionEventType)

  * ##### args: [TransactionEventArgs](https://mikro-orm.io/api/core/interface/TransactionEventArgs.md)

  * ##### optionalmeta: [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<T, [EntityCtor](https://mikro-orm.io/api/core.md#EntityCtor)\<T>>

  #### Returns unknown

### [**](#getsubscribers)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/events/EventManager.ts#L34)getSubscribers

* ****getSubscribers**(): Set<[EventSubscriber](https://mikro-orm.io/api/core/interface/EventSubscriber.md)\<any>>

* #### Returns Set<[EventSubscriber](https://mikro-orm.io/api/core/interface/EventSubscriber.md)\<any>>

### [**](#haslisteners)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/events/EventManager.ts#L91)hasListeners

* ****hasListeners**\<T>(event, meta): boolean

* #### Parameters

  * ##### event: [EventType](https://mikro-orm.io/api/core/enum/EventType.md)

  * ##### meta: [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<T, [EntityCtor](https://mikro-orm.io/api/core.md#EntityCtor)\<T>>

  #### Returns boolean

### [**](#registersubscriber)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/events/EventManager.ts#L18)registerSubscriber

* ****registerSubscriber**(subscriber): void

* #### Parameters

  * ##### subscriber: [EventSubscriber](https://mikro-orm.io/api/core/interface/EventSubscriber.md)\<any>

  #### Returns void
