# Source: https://docs.apify.com/sdk/js/reference/class/PlatformEventManager.md

# PlatformEventManager<!-- -->

Gets an instance of a Node.js' [EventEmitter](https://nodejs.org/api/events.html#events_class_eventemitter) class that emits various events from the SDK or the Apify platform. The event emitter is initialized by calling the [Actor.main](https://docs.apify.com/sdk/js/sdk/js/reference/class/Actor.md#main) function.

**Example usage:**

```
Actor.on('cpuInfo', (data) => {
  if (data.isCpuOverloaded) console.log('Oh no, the CPU is overloaded!');
});
```

The following events are emitted:

* `cpuInfo`: `{ "isCpuOverloaded": Boolean }` The event is emitted approximately every second and it indicates whether the Actor is using the maximum of available CPU resources. If that's the case, the Actor should not add more workload. For example, this event is used by the AutoscaledPool class.
* `migrating`: `void` Emitted when the Actor running on the Apify platform is going to be migrated to another worker server soon. You can use it to persist the state of the Actor and gracefully stop your in-progress tasks, so that they are not interrupted by the migration. For example, this is used by the RequestList class.
* `aborting`: `void` When a user aborts an Actor run on the Apify platform, they can choose to abort gracefully to allow the Actor some time before getting killed. This graceful abort emits the `aborting` event which the SDK uses to gracefully stop running crawls and you can use it to do your own cleanup as well.
* `persistState`: `{ "isMigrating": Boolean }` Emitted in regular intervals (by default 60 seconds) to notify all components of Apify SDK that it is time to persist their state, in order to avoid repeating all work when the Actor restarts. This event is automatically emitted together with the `migrating` event, in which case the `isMigrating` flag is set to `true`. Otherwise the flag is `false`. Note that the `persistState` event is provided merely for user convenience, you can achieve the same effect using `setInterval()` and listening for the `migrating` event.

### Hierarchy

* EventManager
  * *PlatformEventManager*

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

### [**](#constructor)[**](https://github.com/apify/apify-sdk-js/blob/master/packages/apify/src/platform_event_manager.ts#L50)constructor

* ****new PlatformEventManager**(config): [PlatformEventManager](https://docs.apify.com/sdk/js/sdk/js/reference/class/PlatformEventManager.md)

- Overrides EventManager.constructor

  #### Parameters

  * ##### config: [Configuration](https://docs.apify.com/sdk/js/sdk/js/reference/class/Configuration.md) = <!-- -->...

  #### Returns [PlatformEventManager](https://docs.apify.com/sdk/js/sdk/js/reference/class/PlatformEventManager.md)

## Properties<!-- -->[**](#Properties)

### [**](#config)[**](https://github.com/apify/apify-sdk-js/blob/master/packages/apify/src/platform_event_manager.ts#L50)readonlyinheritedconfig

**config: [Configuration](https://docs.apify.com/sdk/js/sdk/js/reference/class/Configuration.md) =

<!-- -->

...

Inherited from EventManager.config

## Methods<!-- -->[**](#Methods)

### [**](#close)[**](https://github.com/apify/apify-sdk-js/blob/master/packages/apify/src/platform_event_manager.ts#L112)close

* ****close**(): Promise\<void>

- Overrides EventManager.close

  Closes websocket providing events from Actor infrastructure and also stops sending internal events of Apify package such as `persistState`. This is automatically called at the end of `Actor.main()`.

  ***

  #### Returns Promise\<void>

### [**](#emit)[**](https://undefined/apify/apify-sdk-js/blob/master/node_modules/@crawlee/core/events/event_manager.d.ts#L36)externalinheritedemit

* ****emit**(event, ...args): void

- Inherited from EventManager.emit

  #### Parameters

  * ##### externalevent: EventTypeName
  * ##### externalrest...args: unknown\[]

  #### Returns void

### [**](#init)[**](https://github.com/apify/apify-sdk-js/blob/master/packages/apify/src/platform_event_manager.ts#L58)init

* ****init**(): Promise\<void>

- Overrides EventManager.init

  Initializes `Actor.events` event emitter by creating a connection to a websocket that provides them. This is an internal function that is automatically called by `Actor.main()`.

  ***

  #### Returns Promise\<void>

### [**](#isInitialized)[**](https://undefined/apify/apify-sdk-js/blob/master/node_modules/@crawlee/core/events/event_manager.d.ts#L37)externalinheritedisInitialized

* ****isInitialized**(): boolean

- Inherited from EventManager.isInitialized

  #### Returns boolean

### [**](#off)[**](https://undefined/apify/apify-sdk-js/blob/master/node_modules/@crawlee/core/events/event_manager.d.ts#L35)externalinheritedoff

* ****off**(event, listener): void

- Inherited from EventManager.off

  #### Parameters

  * ##### externalevent: EventTypeName
  * ##### externaloptionallistener: (...args) => any


  #### Returns void

### [**](#on)[**](https://undefined/apify/apify-sdk-js/blob/master/node_modules/@crawlee/core/events/event_manager.d.ts#L34)externalinheritedon

* ****on**(event, listener): void

- Inherited from EventManager.on

  #### Parameters

  * ##### externalevent: EventTypeName
  * ##### externallistener: (...args) => any


  #### Returns void
