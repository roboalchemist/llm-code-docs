# Source: https://crawlee.dev/js/api/core/class/LocalEventManager.md

# LocalEventManager<!-- -->

### Hierarchy

* [EventManager](https://crawlee.dev/js/api/core/class/EventManager.md)
  * *LocalEventManager*

## Index[**](#Index)

### Constructors

* [**constructor](#constructor)

### Properties

* [**config](#config)

### Methods

* [**close](#close)
* [**emit](#emit)
* [**init](#init)
* [**isInitialized](#isInitialized)
* [**off](#off)
* [**on](#on)

## Constructors<!-- -->[**](#Constructors)

### [**](#constructor)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/events/event_manager.ts#L30)constructor

* ****new LocalEventManager**(config): [LocalEventManager](https://crawlee.dev/js/api/core/class/LocalEventManager.md)

- Inherited from EventManager.constructor

  #### Parameters

  * ##### config: [Configuration](https://crawlee.dev/js/api/core/class/Configuration.md) = <!-- -->...

  #### Returns [LocalEventManager](https://crawlee.dev/js/api/core/class/LocalEventManager.md)

## Properties<!-- -->[**](#Properties)

### [**](#config)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/events/event_manager.ts#L30)readonlyinheritedconfig

**config: [Configuration](https://crawlee.dev/js/api/core/class/Configuration.md) =

<!-- -->

...

Inherited from EventManager.config

## Methods<!-- -->[**](#Methods)

### [**](#close)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/events/local_event_manager.ts#L33)close

* ****close**(): Promise\<void>

- Overrides EventManager.close

  Clears the internal `persistState` event interval. This is automatically called at the end of `crawler.run()`.

  ***

  #### Returns Promise\<void>

### [**](#emit)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/events/event_manager.ts#L82)inheritedemit

* ****emit**(event, ...args): void

- Inherited from EventManager.emit

  #### Parameters

  * ##### event: [EventTypeName](https://crawlee.dev/js/api/core.md#EventTypeName)
  * ##### rest...args: unknown\[]

  #### Returns void

### [**](#init)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/events/local_event_manager.ts#L18)init

* ****init**(): Promise\<void>

- Overrides EventManager.init

  Initializes the EventManager and sets up periodic `systemInfo` and `persistState` events. This is automatically called at the beginning of `crawler.run()`.

  ***

  #### Returns Promise\<void>

### [**](#isInitialized)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/events/event_manager.ts#L86)inheritedisInitialized

* ****isInitialized**(): boolean

- Inherited from EventManager.isInitialized

  #### Returns boolean

### [**](#off)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/events/event_manager.ts#L74)inheritedoff

* ****off**(event, listener): void

- Inherited from EventManager.off

  #### Parameters

  * ##### event: [EventTypeName](https://crawlee.dev/js/api/core.md#EventTypeName)
  * ##### optionallistener: (...args) => any


  #### Returns void

### [**](#on)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/events/event_manager.ts#L70)inheritedon

* ****on**(event, listener): void

- Inherited from EventManager.on

  #### Parameters

  * ##### event: [EventTypeName](https://crawlee.dev/js/api/core.md#EventTypeName)
  * ##### listener: (...args) => any


  #### Returns void
