# Source: https://docs.apify.com/api/client/python/reference/class/StatusMessageWatcherAsync.md

# StatusMessageWatcherAsync<!-- -->

Async variant of `StatusMessageWatcher` that is logging in task.

### Hierarchy

* [StatusMessageWatcher](https://docs.apify.com/api/client/python/api/client/python/reference/class/StatusMessageWatcher.md)
  * *StatusMessageWatcherAsync*

## Index[**](#Index)

### Methods

* [**\_\_aenter\_\_](https://docs.apify.com/api/client/python/api/client/python/reference/class/StatusMessageWatcherAsync.md#__aenter__)
* [**\_\_aexit\_\_](https://docs.apify.com/api/client/python/api/client/python/reference/class/StatusMessageWatcherAsync.md#__aexit__)
* [**\_\_init\_\_](https://docs.apify.com/api/client/python/api/client/python/reference/class/StatusMessageWatcherAsync.md#__init__)
* [**start](https://docs.apify.com/api/client/python/api/client/python/reference/class/StatusMessageWatcherAsync.md#start)
* [**stop](https://docs.apify.com/api/client/python/api/client/python/reference/class/StatusMessageWatcherAsync.md#stop)

## Methods<!-- -->[**](#Methods)

### [**](#__aenter__)[**](https://undefined/apify/apify-client-python/blob/25ff4e51e07fe25d1d338b042eacba1ec0c63e84//src/apify_client/clients/resource_clients/log.py#L464)\_\_aenter\_\_

* **async **\_\_aenter\_\_**(): Self

- Start the logging task within the context. Exiting the context will cancel the logging task.

  ***

  #### Returns Self

### [**](#__aexit__)[**](https://undefined/apify/apify-client-python/blob/25ff4e51e07fe25d1d338b042eacba1ec0c63e84//src/apify_client/clients/resource_clients/log.py#L469)\_\_aexit\_\_

* **async **\_\_aexit\_\_**(exc\_type, exc\_val, exc\_tb): None

- Cancel the logging task.

  ***

  #### Parameters

  * ##### exc\_type: type\[BaseException] | None
  * ##### exc\_val: BaseException | None
  * ##### exc\_tb: TracebackType | None

  #### Returns None

### [**](#__init__)[**](https://undefined/apify/apify-client-python/blob/25ff4e51e07fe25d1d338b042eacba1ec0c63e84//src/apify_client/clients/resource_clients/log.py#L432)\_\_init\_\_

* ****\_\_init\_\_**(\*, run\_client, to\_logger, check\_period): None

- Overrides [StatusMessageWatcher.\_\_init\_\_](https://docs.apify.com/api/client/python/api/client/python/reference/class/StatusMessageWatcher.md#__init__)

  Initialize `StatusMessageWatcherAsync`.

  ***

  #### Parameters

  * ##### keyword-onlyrun\_client: [RunClientAsync](https://docs.apify.com/api/client/python/api/client/python/reference/class/RunClientAsync.md)

    The client for run that will be used to get a status and message.

  * ##### keyword-onlyto\_logger: logging.Logger

    The logger to which the status message will be redirected.

  * ##### optionalkeyword-onlycheck\_period: timedelta = <!-- -->timedelta(seconds=1)

    The period with which the status message will be polled.

  #### Returns None

### [**](#start)[**](https://undefined/apify/apify-client-python/blob/25ff4e51e07fe25d1d338b042eacba1ec0c63e84//src/apify_client/clients/resource_clients/log.py#L446)start

* ****start**(): Task

- Start the logging task. The caller has to handle any cleanup by manually calling the `stop` method.

  ***

  #### Returns Task

### [**](#stop)[**](https://undefined/apify/apify-client-python/blob/25ff4e51e07fe25d1d338b042eacba1ec0c63e84//src/apify_client/clients/resource_clients/log.py#L453)stop

* **async **stop**(): None

- Stop the logging task.

  ***

  #### Returns None
