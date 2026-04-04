# Source: https://docs.apify.com/sdk/python/reference/class/LocalEventManager.md

# LocalEventManager<!-- -->

Event manager for local environments.

It extends the `EventManager` to emit `SystemInfo` events at regular intervals. The `LocalEventManager` is intended to be used in local environments, where the system metrics are required managing the `Snapshotter` and `AutoscaledPool`.

### Hierarchy

* [EventManager](https://crawlee.dev/python/api/class/EventManager)
  * *LocalEventManager*

## Index[**](#Index)

### Methods

* [**\_\_aenter\_\_](https://docs.apify.com/sdk/python/sdk/python/reference/class/LocalEventManager.md#__aenter__)
* [**\_\_aexit\_\_](https://docs.apify.com/sdk/python/sdk/python/reference/class/LocalEventManager.md#__aexit__)
* [**\_\_init\_\_](https://docs.apify.com/sdk/python/sdk/python/reference/class/LocalEventManager.md#__init__)
* [**emit](https://docs.apify.com/sdk/python/sdk/python/reference/class/LocalEventManager.md#emit)
* [**from\_config](https://docs.apify.com/sdk/python/sdk/python/reference/class/LocalEventManager.md#from_config)
* [**off](https://docs.apify.com/sdk/python/sdk/python/reference/class/LocalEventManager.md#off)
* [**on](https://docs.apify.com/sdk/python/sdk/python/reference/class/LocalEventManager.md#on)
* [**wait\_for\_all\_listeners\_to\_complete](https://docs.apify.com/sdk/python/sdk/python/reference/class/LocalEventManager.md#wait_for_all_listeners_to_complete)

### Properties

* [**active](https://docs.apify.com/sdk/python/sdk/python/reference/class/LocalEventManager.md#active)

## Methods<!-- -->[**](#Methods)

### [**](#__aenter__)[**](https://github.com/apify/crawlee-python/blob/3e08b24571bbd21f25523e9aa81bc31ba308628d//src/crawlee/events/_local_event_manager.py#L72)\_\_aenter\_\_

* **async **\_\_aenter\_\_**(): [LocalEventManager](https://crawlee.dev/python/api/class/LocalEventManager)

- Overrides [EventManager.\_\_aenter\_\_](https://crawlee.dev/python/api/class/EventManager#__aenter__)

  Initialize the local event manager upon entering the async context.

  It starts emitting system info events at regular intervals.

  ***

  #### Returns [LocalEventManager](https://crawlee.dev/python/api/class/LocalEventManager)

### [**](#__aexit__)[**](https://github.com/apify/crawlee-python/blob/3e08b24571bbd21f25523e9aa81bc31ba308628d//src/crawlee/events/_local_event_manager.py#L81)\_\_aexit\_\_

* **async **\_\_aexit\_\_**(exc\_type, exc\_value, exc\_traceback): None

- Overrides [EventManager.\_\_aexit\_\_](https://crawlee.dev/python/api/class/EventManager#__aexit__)

  Close the local event manager upon exiting the async context.

  It stops emitting system info events and closes the event manager.

  ***

  #### Parameters

  * ##### exc\_type: [type](https://crawlee.dev/python/api/class/SitemapSource#type)\[BaseException] | None
  * ##### exc\_value: BaseException | None
  * ##### exc\_traceback: TracebackType | None

  #### Returns None

### [**](#__init__)[**](https://github.com/apify/crawlee-python/blob/3e08b24571bbd21f25523e9aa81bc31ba308628d//src/crawlee/events/_local_event_manager.py#L34)\_\_init\_\_

* ****\_\_init\_\_**(system\_info\_interval, \*, persist\_state\_interval, close\_timeout): None

- Overrides [EventManager.\_\_init\_\_](https://crawlee.dev/python/api/class/EventManager#__init__)

  Initialize a new instance.

  In most cases, you should use the `from_config` constructor to create a new instance based on the provided configuration.

  ***

  #### Parameters

  * ##### optionalsystem\_info\_interval: timedelta = <!-- -->timedelta(seconds=1)

    Interval at which `SystemInfo` events are emitted.

  * ##### keyword-onlyoptionalpersist\_state\_interval: timedelta

    Interval between emitted `PersistState` events to maintain state persistence.

  * ##### keyword-onlyoptionalclose\_timeout: timedelta | None

    Optional timeout for canceling pending event listeners if they exceed this duration.

  #### Returns None

### [**](#emit)[**](https://github.com/apify/crawlee-python/blob/3e08b24571bbd21f25523e9aa81bc31ba308628d//src/crawlee/events/_event_manager.py#L239)emit

* ****emit**(\*: , event: [Event](https://crawlee.dev/python/api/enum/Event), event\_data: [EventData](https://crawlee.dev/python/api#EventData)): None
* ****emit**(\*: , event: Literal\[Event.PERSIST\_STATE], event\_data: [EventPersistStateData](https://crawlee.dev/python/api/class/EventPersistStateData)): None
* ****emit**(\*: , event: Literal\[Event.SYSTEM\_INFO], event\_data: [EventSystemInfoData](https://crawlee.dev/python/api/class/EventSystemInfoData)): None
* ****emit**(\*: , event: Literal\[Event.MIGRATING], event\_data: [EventMigratingData](https://crawlee.dev/python/api/class/EventMigratingData)): None
* ****emit**(\*: , event: Literal\[Event.ABORTING], event\_data: [EventAbortingData](https://crawlee.dev/python/api/class/EventAbortingData)): None
* ****emit**(\*: , event: Literal\[Event.EXIT], event\_data: [EventExitData](https://crawlee.dev/python/api/class/EventExitData)): None
* ****emit**(\*: , event: Literal\[Event.CRAWLER\_STATUS], event\_data: [EventCrawlerStatusData](https://crawlee.dev/python/api/class/EventCrawlerStatusData)): None
* ****emit**(\*: , event: [Event](https://crawlee.dev/python/api/enum/Event), event\_data: Any): None

- Inherited from [EventManager.emit](https://crawlee.dev/python/api/class/EventManager#emit)

  Emit an event with the associated data to all registered listeners.

  ***

  #### Parameters

  * ##### keyword-onlyevent: [Event](https://crawlee.dev/python/api/enum/Event)

    The event which will be emitted.

  * ##### keyword-onlyevent\_data: [EventData](https://crawlee.dev/python/api#EventData)

    The data which will be passed to the event listeners.

  #### Returns None

### [**](#from_config)[**](https://github.com/apify/crawlee-python/blob/3e08b24571bbd21f25523e9aa81bc31ba308628d//src/crawlee/events/_local_event_manager.py#L59)from\_config

* ****from\_config**(config): [LocalEventManager](https://crawlee.dev/python/api/class/LocalEventManager)

- Initialize a new instance based on the provided `Configuration`.

  ***

  #### Parameters

  * ##### optionalconfig: [Configuration](https://crawlee.dev/python/api/class/Configuration) | None = <!-- -->None

    The `Configuration` instance. Uses the global (default) one if not provided.

  #### Returns [LocalEventManager](https://crawlee.dev/python/api/class/LocalEventManager)

### [**](#off)[**](https://github.com/apify/crawlee-python/blob/3e08b24571bbd21f25523e9aa81bc31ba308628d//src/crawlee/events/_event_manager.py#L207)off

* ****off**(\*, event, listener): None

- Inherited from [EventManager.off](https://crawlee.dev/python/api/class/EventManager#off)

  Remove a specific listener or all listeners for an event.

  ***

  #### Parameters

  * ##### keyword-onlyevent: [Event](https://crawlee.dev/python/api/enum/Event)

    The Actor event for which to remove listeners.

  * ##### optionalkeyword-onlylistener: EventListener\[Any] | None = <!-- -->None

    The listener which is supposed to be removed. If not passed, all listeners of this event are removed.

  #### Returns None

### [**](#on)[**](https://github.com/apify/crawlee-python/blob/3e08b24571bbd21f25523e9aa81bc31ba308628d//src/crawlee/events/_event_manager.py#L157)on

* ****on**(\*: , event: [Event](https://crawlee.dev/python/api/enum/Event), listener: EventListener\[Any]): None
* ****on**(\*: , event: Literal\[Event.PERSIST\_STATE], listener: EventListener\[EventPersistStateData]): None
* ****on**(\*: , event: Literal\[Event.SYSTEM\_INFO], listener: EventListener\[EventSystemInfoData]): None
* ****on**(\*: , event: Literal\[Event.MIGRATING], listener: EventListener\[EventMigratingData]): None
* ****on**(\*: , event: Literal\[Event.ABORTING], listener: EventListener\[EventAbortingData]): None
* ****on**(\*: , event: Literal\[Event.EXIT], listener: EventListener\[EventExitData]): None
* ****on**(\*: , event: Literal\[Event.CRAWLER\_STATUS], listener: EventListener\[EventCrawlerStatusData]): None
* ****on**(\*: , event: [Event](https://crawlee.dev/python/api/enum/Event), listener: EventListener\[None]): None

- Inherited from [EventManager.on](https://crawlee.dev/python/api/class/EventManager#on)

  Register an event listener for a specific event.

  ***

  #### Parameters

  * ##### keyword-onlyevent: [Event](https://crawlee.dev/python/api/enum/Event)

    The event for which to listen to.

  * ##### keyword-onlylistener: EventListener\[Any]

    The function (sync or async) which is to be called when the event is emitted.

  #### Returns None

### [**](#wait_for_all_listeners_to_complete)[**](https://github.com/apify/crawlee-python/blob/3e08b24571bbd21f25523e9aa81bc31ba308628d//src/crawlee/events/_event_manager.py#L249)wait\_for\_all\_listeners\_to\_complete

* **async **wait\_for\_all\_listeners\_to\_complete**(\*, timeout): None

- Inherited from [EventManager.wait\_for\_all\_listeners\_to\_complete](https://crawlee.dev/python/api/class/EventManager#wait_for_all_listeners_to_complete)

  Wait for all currently executing event listeners to complete.

  ***

  #### Parameters

  * ##### optionalkeyword-onlytimeout: timedelta | None = <!-- -->None

    The maximum time to wait for the event listeners to finish. If they do not complete within the specified timeout, they will be canceled.

  #### Returns None

## Properties<!-- -->[**](#Properties)

### [**](#active)[**](https://github.com/apify/crawlee-python/blob/3e08b24571bbd21f25523e9aa81bc31ba308628d//src/crawlee/events/_event_manager.py#L100)active

**active: bool

Inherited from [EventManager.active](https://crawlee.dev/python/api/class/EventManager#active)

Indicate whether the context is active.
