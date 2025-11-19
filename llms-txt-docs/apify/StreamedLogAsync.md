# Source: https://docs.apify.com/api/client/python/reference/class/StreamedLogAsync.md

# StreamedLogAsync<!-- -->

Async variant of `StreamedLog` that is logging in tasks.

### Hierarchy

* [StreamedLog](https://docs.apify.com/api/client/python/api/client/python/reference/class/StreamedLog.md)
  * *StreamedLogAsync*

## Index[**](#Index)

### Methods

* [**\_\_aenter\_\_](https://docs.apify.com/api/client/python/api/client/python/reference/class/StreamedLogAsync.md#__aenter__)
* [**\_\_aexit\_\_](https://docs.apify.com/api/client/python/api/client/python/reference/class/StreamedLogAsync.md#__aexit__)
* [**\_\_init\_\_](https://docs.apify.com/api/client/python/api/client/python/reference/class/StreamedLogAsync.md#__init__)
* [**start](https://docs.apify.com/api/client/python/api/client/python/reference/class/StreamedLogAsync.md#start)
* [**stop](https://docs.apify.com/api/client/python/api/client/python/reference/class/StreamedLogAsync.md#stop)

## Methods<!-- -->[**](#Methods)

### [**](#__aenter__)[**](https://undefined/apify/apify-client-python/blob/master//src/apify_client/clients/resource_clients/log.py#L359)\_\_aenter\_\_

* **async **\_\_aenter\_\_**(): Self

- Start the streaming task within the context. Exiting the context will cancel the streaming task.

  ***

  #### Returns Self

### [**](#__aexit__)[**](https://undefined/apify/apify-client-python/blob/master//src/apify_client/clients/resource_clients/log.py#L364)\_\_aexit\_\_

* **async **\_\_aexit\_\_**(exc\_type, exc\_val, exc\_tb): None

- Cancel the streaming task.

  ***

  #### Parameters

  * ##### exc\_type: type\[BaseException] | None
  * ##### exc\_val: BaseException | None
  * ##### exc\_tb: TracebackType | None

  #### Returns None

### [**](#__init__)[**](https://undefined/apify/apify-client-python/blob/master//src/apify_client/clients/resource_clients/log.py#L336)\_\_init\_\_

* ****\_\_init\_\_**(to\_logger, \*, from\_start): None

- Overrides [StreamedLog.\_\_init\_\_](https://docs.apify.com/api/client/python/api/client/python/reference/class/StreamedLog.md#__init__)

  Initialize `StreamedLog`.

  ***

  #### Parameters

  * ##### to\_logger: logging.Logger

    The logger to which the logs will be redirected.

  * ##### optionalkeyword-onlyfrom\_start: bool = <!-- -->True

    If `True`, all logs from the start of the actor run will be redirected. If `False`, only newly arrived logs will be redirected. This can be useful for redirecting only a small portion of relevant logs for long-running actors in stand-by.

  #### Returns None

### [**](#start)[**](https://undefined/apify/apify-client-python/blob/master//src/apify_client/clients/resource_clients/log.py#L341)start

* ****start**(): Task

- Start the streaming task. The caller has to handle any cleanup by manually calling the `stop` method.

  ***

  #### Returns Task

### [**](#stop)[**](https://undefined/apify/apify-client-python/blob/master//src/apify_client/clients/resource_clients/log.py#L348)stop

* **async **stop**(): None

- Stop the streaming task.

  ***

  #### Returns None
