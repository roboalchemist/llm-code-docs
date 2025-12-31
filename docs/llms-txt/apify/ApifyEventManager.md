# Source: https://docs.apify.com/sdk/python/reference/class/ApifyEventManager.md

# ApifyEventManager<!-- -->

Event manager for the Apify platform.

This class extends Crawlee's `EventManager` to provide Apify-specific functionality, including websocket connectivity to the Apify platform for receiving platform events.

The event manager handles:

* Registration and emission of events and their listeners.
* Websocket connection to Apify platform events.
* Processing and validation of platform messages.
* Automatic event forwarding from the platform to local event listeners.

This class should not be used directly. Use the `Actor.on` and `Actor.off` methods to interact with the event system.

## Index[**](#Index)

### Methods

* [**\_\_aenter\_\_](https://docs.apify.com/sdk/python/sdk/python/reference/class/ApifyEventManager.md#__aenter__)
* [**\_\_aexit\_\_](https://docs.apify.com/sdk/python/sdk/python/reference/class/ApifyEventManager.md#__aexit__)
* [**\_\_init\_\_](https://docs.apify.com/sdk/python/sdk/python/reference/class/ApifyEventManager.md#__init__)

## Methods<!-- -->[**](#Methods)

### [**](#__aenter__)[**](https://github.com/apify/apify-sdk-python/blob/f050b2684cf6d5e88bafe381599a3653d220ec14//src/apify/events/_apify_event_manager.py#L70)\_\_aenter\_\_

* **async **\_\_aenter\_\_**(): Self

- #### Returns Self

### [**](#__aexit__)[**](https://github.com/apify/apify-sdk-python/blob/f050b2684cf6d5e88bafe381599a3653d220ec14//src/apify/events/_apify_event_manager.py#L88)\_\_aexit\_\_

* **async **\_\_aexit\_\_**(exc\_type, exc\_value, exc\_traceback): None

- #### Parameters

  * ##### exc\_type: type\[BaseException] | None
  * ##### exc\_value: BaseException | None
  * ##### exc\_traceback: TracebackType | None

  #### Returns None

### [**](#__init__)[**](https://github.com/apify/apify-sdk-python/blob/f050b2684cf6d5e88bafe381599a3653d220ec14//src/apify/events/_apify_event_manager.py#L48)\_\_init\_\_

* ****\_\_init\_\_**(configuration): None

- Initialize a new instance.

  ***

  #### Parameters

  * ##### configuration: [Configuration](https://docs.apify.com/sdk/python/sdk/python/reference/class/Configuration.md)

    The Actor configuration for the event manager.

  #### Returns None
