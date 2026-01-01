# Source: https://mikro-orm.io/api/core/class/EventManager.md

# EventManager<!-- -->

## Index[**](#Index)

### Constructors

* [**constructor](#constructor)

### Methods

* [**clone](#clone)
* [**dispatchEvent](#dispatchEvent)
* [**hasListeners](#hasListeners)
* [**registerSubscriber](#registerSubscriber)

## Constructors<!-- -->[**](#Constructors)

### [**](#constructor)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/events/EventManager.ts#L13)constructor

* ****new EventManager**(subscribers): [EventManager](https://mikro-orm.io/api/core/class/EventManager.md)

- #### Parameters

  * ##### subscribers: [EventSubscriber](https://mikro-orm.io/api/core/interface/EventSubscriber.md)\<any>\[]

  #### Returns [EventManager](https://mikro-orm.io/api/core/class/EventManager.md)

## Methods<!-- -->[**](#Methods)

### [**](#clone)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/events/EventManager.ts#L87)clone

* ****clone**(): [EventManager](https://mikro-orm.io/api/core/class/EventManager.md)

- #### Returns [EventManager](https://mikro-orm.io/api/core/class/EventManager.md)

### [**](#dispatchEvent)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/events/EventManager.ts#L29)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/events/EventManager.ts#L30)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/events/EventManager.ts#L31)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/events/EventManager.ts#L32)dispatchEvent

* ****dispatchEvent**\<T>(event, args, meta): unknown
* ****dispatchEvent**\<T>(event, args, meta): unknown
* ****dispatchEvent**\<T>(event, args, meta): Promise\<unknown>

- #### Parameters

  * ##### event: [TransactionEventType](https://mikro-orm.io/api/core.md#TransactionEventType)
  * ##### args: [TransactionEventArgs](https://mikro-orm.io/api/core/interface/TransactionEventArgs.md)
  * ##### optionalmeta: [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<T>

  #### Returns unknown

### [**](#hasListeners)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/events/EventManager.ts#L60)hasListeners

* ****hasListeners**\<T>(event, meta): boolean

- #### Parameters

  * ##### event: [EventType](https://mikro-orm.io/api/core/enum/EventType.md)
  * ##### meta: [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<T>

  #### Returns boolean

### [**](#registerSubscriber)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/events/EventManager.ts#L17)registerSubscriber

* ****registerSubscriber**(subscriber): void

- #### Parameters

  * ##### subscriber: [EventSubscriber](https://mikro-orm.io/api/core/interface/EventSubscriber.md)\<any>

  #### Returns void
