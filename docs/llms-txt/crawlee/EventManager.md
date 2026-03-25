# Source: https://crawlee.dev/js/api/core/class/EventManager.md

# abstractEventManager<!-- -->

### Hierarchy

* *EventManager*
  * [LocalEventManager](https://crawlee.dev/js/api/core/class/LocalEventManager.md)

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

* ****new EventManager**(config): [EventManager](https://crawlee.dev/js/api/core/class/EventManager.md)

- #### Parameters

  * ##### config: [Configuration](https://crawlee.dev/js/api/core/class/Configuration.md) = <!-- -->...

  #### Returns [EventManager](https://crawlee.dev/js/api/core/class/EventManager.md)

## Properties<!-- -->[**](#Properties)

### [**](#config)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/events/event_manager.ts#L30)readonlyconfig

**config: [Configuration](https://crawlee.dev/js/api/core/class/Configuration.md) =

<!-- -->

...

## Methods<!-- -->[**](#Methods)

### [**](#close)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/events/event_manager.ts#L55)close

* ****close**(): Promise\<void>

- Clears the internal `persistState` event interval. This is automatically called at the end of `crawler.run()`.

  ***

  #### Returns Promise\<void>

### [**](#emit)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/events/event_manager.ts#L82)emit

* ****emit**(event, ...args): void

- #### Parameters

  * ##### event: [EventTypeName](https://crawlee.dev/js/api/core.md#EventTypeName)
  * ##### rest...args: unknown\[]

  #### Returns void

### [**](#init)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/events/event_manager.ts#L38)init

* ****init**(): Promise\<void>

- Initializes the event manager by creating the `persistState` event interval. This is automatically called at the beginning of `crawler.run()`.

  ***

  #### Returns Promise\<void>

### [**](#isInitialized)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/events/event_manager.ts#L86)isInitialized

* ****isInitialized**(): boolean

- #### Returns boolean

### [**](#off)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/events/event_manager.ts#L74)off

* ****off**(event, listener): void

- #### Parameters

  * ##### event: [EventTypeName](https://crawlee.dev/js/api/core.md#EventTypeName)
  * ##### optionallistener: (...args) => any


  #### Returns void

### [**](#on)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/events/event_manager.ts#L70)on

* ****on**(event, listener): void

- #### Parameters

  * ##### event: [EventTypeName](https://crawlee.dev/js/api/core.md#EventTypeName)
  * ##### listener: (...args) => any


  #### Returns void
