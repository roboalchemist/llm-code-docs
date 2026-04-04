# Source: https://docs.apify.com/sdk/python/reference/class/EventManager.md

# EventManager<!-- -->

Manage events and their listeners, enabling registration, emission, and execution control.

It allows for registering event listeners, emitting events, and ensuring all listeners complete their execution. Built on top of `pyee.asyncio.AsyncIOEventEmitter`. It implements additional features such as waiting for all listeners to complete and emitting `PersistState` events at regular intervals.

### Hierarchy

* *EventManager*
  * [LocalEventManager](https://crawlee.dev/python/api/class/LocalEventManager)

## Index[**](#Index)

### Methods

* [**\_\_aenter\_\_](https://docs.apify.com/sdk/python/sdk/python/reference/class/EventManager.md#__aenter__)
* [**\_\_aexit\_\_](https://docs.apify.com/sdk/python/sdk/python/reference/class/EventManager.md#__aexit__)
* [**\_\_init\_\_](https://docs.apify.com/sdk/python/sdk/python/reference/class/EventManager.md#__init__)
* [**emit](https://docs.apify.com/sdk/python/sdk/python/reference/class/EventManager.md#emit)
* [**off](https://docs.apify.com/sdk/python/sdk/python/reference/class/EventManager.md#off)
* [**on](https://docs.apify.com/sdk/python/sdk/python/reference/class/EventManager.md#on)
* [**wait\_for\_all\_listeners\_to\_complete](https://docs.apify.com/sdk/python/sdk/python/reference/class/EventManager.md#wait_for_all_listeners_to_complete)

### Properties

* [**active](https://docs.apify.com/sdk/python/sdk/python/reference/class/EventManager.md#active)

## Methods<!-- -->[**](#Methods)

### [**](#__aenter__)[**](https://github.com/apify/crawlee-python/blob/3e08b24571bbd21f25523e9aa81bc31ba308628d//src/crawlee/events/_event_manager.py#L104)\_\_aenter\_\_

* **async **\_\_aenter\_\_**(): [EventManager](https://crawlee.dev/python/api/class/EventManager)

- Initialize the event manager upon entering the async context.

  ***

  #### Returns [EventManager](https://crawlee.dev/python/api/class/EventManager)

### [**](#__aexit__)[**](https://github.com/apify/crawlee-python/blob/3e08b24571bbd21f25523e9aa81bc31ba308628d//src/crawlee/events/_event_manager.py#L117)\_\_aexit\_\_

* **async **\_\_aexit\_\_**(exc\_type, exc\_value, exc\_traceback): None

- Close the local event manager upon exiting the async context.

  This will stop listening for the events, and it will wait for all the event listeners to finish.

  ***

  #### Parameters

  * ##### exc\_type: [type](https://crawlee.dev/python/api/class/SitemapSource#type)\[BaseException] | None
  * ##### exc\_value: BaseException | None
  * ##### exc\_traceback: TracebackType | None

  #### Returns None

### [**](#__init__)[**](https://github.com/apify/crawlee-python/blob/3e08b24571bbd21f25523e9aa81bc31ba308628d//src/crawlee/events/_event_manager.py#L63)\_\_init\_\_

* ****\_\_init\_\_**(\*, persist\_state\_interval, close\_timeout): None

- Initialize a new instance.

  ***

  #### Parameters

  * ##### optionalkeyword-onlypersist\_state\_interval: timedelta = <!-- -->timedelta(minutes=1)

    Interval between emitted `PersistState` events to maintain state persistence.

  * ##### optionalkeyword-onlyclose\_timeout: timedelta | None = <!-- -->None

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

- Emit an event with the associated data to all registered listeners.

  ***

  #### Parameters

  * ##### keyword-onlyevent: [Event](https://crawlee.dev/python/api/enum/Event)

    The event which will be emitted.

  * ##### keyword-onlyevent\_data: [EventData](https://crawlee.dev/python/api#EventData)

    The data which will be passed to the event listeners.

  #### Returns None

### [**](#off)[**](https://github.com/apify/crawlee-python/blob/3e08b24571bbd21f25523e9aa81bc31ba308628d//src/crawlee/events/_event_manager.py#L207)off

* ****off**(\*, event, listener): None

- Remove a specific listener or all listeners for an event.

  ***

  #### Parameters

  * ##### keyword-onlyevent: [Event](https://crawlee.dev/python/api/enum/Event)

    The Actor event for which to remove listeners.

  * ##### optionalkeyword-onlylistener: [EventListener](https://crawlee.dev/python/api#EventListener)\[Any] | None = <!-- -->None

    The listener which is supposed to be removed. If not passed, all listeners of this event are removed.

  #### Returns None

### [**](#on)[**](https://github.com/apify/crawlee-python/blob/3e08b24571bbd21f25523e9aa81bc31ba308628d//src/crawlee/events/_event_manager.py#L157)on

* ****on**(\*: , event: [Event](https://crawlee.dev/python/api/enum/Event), listener: [EventListener](https://crawlee.dev/python/api#EventListener)\[Any]): None
* ****on**(\*: , event: Literal\[Event.PERSIST\_STATE], listener: [EventListener](https://crawlee.dev/python/api#EventListener)\[[EventPersistStateData](https://crawlee.dev/python/api/class/EventPersistStateData)]): None
* ****on**(\*: , event: Literal\[Event.SYSTEM\_INFO], listener: [EventListener](https://crawlee.dev/python/api#EventListener)\[[EventSystemInfoData](https://crawlee.dev/python/api/class/EventSystemInfoData)]): None
* ****on**(\*: , event: Literal\[Event.MIGRATING], listener: [EventListener](https://crawlee.dev/python/api#EventListener)\[[EventMigratingData](https://crawlee.dev/python/api/class/EventMigratingData)]): None
* ****on**(\*: , event: Literal\[Event.ABORTING], listener: [EventListener](https://crawlee.dev/python/api#EventListener)\[[EventAbortingData](https://crawlee.dev/python/api/class/EventAbortingData)]): None
* ****on**(\*: , event: Literal\[Event.EXIT], listener: [EventListener](https://crawlee.dev/python/api#EventListener)\[[EventExitData](https://crawlee.dev/python/api/class/EventExitData)]): None
* ****on**(\*: , event: Literal\[Event.CRAWLER\_STATUS], listener: [EventListener](https://crawlee.dev/python/api#EventListener)\[[EventCrawlerStatusData](https://crawlee.dev/python/api/class/EventCrawlerStatusData)]): None
* ****on**(\*: , event: [Event](https://crawlee.dev/python/api/enum/Event), listener: [EventListener](https://crawlee.dev/python/api#EventListener)\[None]): None

- Register an event listener for a specific event.

  ***

  #### Parameters

  * ##### keyword-onlyevent: [Event](https://crawlee.dev/python/api/enum/Event)

    The event for which to listen to.

  * ##### keyword-onlylistener: [EventListener](https://crawlee.dev/python/api#EventListener)\[Any]

    The function (sync or async) which is to be called when the event is emitted.

  #### Returns None

### [**](#wait_for_all_listeners_to_complete)[**](https://github.com/apify/crawlee-python/blob/3e08b24571bbd21f25523e9aa81bc31ba308628d//src/crawlee/events/_event_manager.py#L249)wait\_for\_all\_listeners\_to\_complete

* **async **wait\_for\_all\_listeners\_to\_complete**(\*, timeout): None

- Wait for all currently executing event listeners to complete.

  ***

  #### Parameters

  * ##### optionalkeyword-onlytimeout: timedelta | None = <!-- -->None

    The maximum time to wait for the event listeners to finish. If they do not complete within the specified timeout, they will be canceled.

  #### Returns None

## Properties<!-- -->[**](#Properties)

### [**](#active)[**](https://github.com/apify/crawlee-python/blob/3e08b24571bbd21f25523e9aa81bc31ba308628d//src/crawlee/events/_event_manager.py#L100)active

**active: bool

Indicate whether the context is active.
