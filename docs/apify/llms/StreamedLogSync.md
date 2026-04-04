# Source: https://docs.apify.com/api/client/python/reference/class/StreamedLogSync.md

# StreamedLogSync<!-- -->

Sync variant of `StreamedLog` that is logging in threads.

### Hierarchy

* [StreamedLog](https://docs.apify.com/api/client/python/api/client/python/reference/class/StreamedLog.md)
  * *StreamedLogSync*

## Index[**](#Index)

### Methods

* [**\_\_enter\_\_](https://docs.apify.com/api/client/python/api/client/python/reference/class/StreamedLogSync.md#__enter__)
* [**\_\_exit\_\_](https://docs.apify.com/api/client/python/api/client/python/reference/class/StreamedLogSync.md#__exit__)
* [**\_\_init\_\_](https://docs.apify.com/api/client/python/api/client/python/reference/class/StreamedLogSync.md#__init__)
* [**start](https://docs.apify.com/api/client/python/api/client/python/reference/class/StreamedLogSync.md#start)
* [**stop](https://docs.apify.com/api/client/python/api/client/python/reference/class/StreamedLogSync.md#stop)

## Methods<!-- -->[**](#Methods)

### [**](#__enter__)[**](https://undefined/apify/apify-client-python/blob/25ff4e51e07fe25d1d338b042eacba1ec0c63e84//src/apify_client/clients/resource_clients/log.py#L308)\_\_enter\_\_

* ****\_\_enter\_\_**(): Self

- Start the streaming thread within the context. Exiting the context will finish the streaming thread.

  ***

  #### Returns Self

### [**](#__exit__)[**](https://undefined/apify/apify-client-python/blob/25ff4e51e07fe25d1d338b042eacba1ec0c63e84//src/apify_client/clients/resource_clients/log.py#L313)\_\_exit\_\_

* ****\_\_exit\_\_**(exc\_type, exc\_val, exc\_tb): None

- Stop the streaming thread.

  ***

  #### Parameters

  * ##### exc\_type: type\[BaseException] | None
  * ##### exc\_val: BaseException | None
  * ##### exc\_tb: TracebackType | None

  #### Returns None

### [**](#__init__)[**](https://undefined/apify/apify-client-python/blob/25ff4e51e07fe25d1d338b042eacba1ec0c63e84//src/apify_client/clients/resource_clients/log.py#L284)\_\_init\_\_

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

### [**](#start)[**](https://undefined/apify/apify-client-python/blob/25ff4e51e07fe25d1d338b042eacba1ec0c63e84//src/apify_client/clients/resource_clients/log.py#L290)start

* ****start**(): Thread

- Start the streaming thread. The caller has to handle any cleanup by manually calling the `stop` method.

  ***

  #### Returns Thread

### [**](#stop)[**](https://undefined/apify/apify-client-python/blob/25ff4e51e07fe25d1d338b042eacba1ec0c63e84//src/apify_client/clients/resource_clients/log.py#L299)stop

* ****stop**(): None

- Signal the streaming thread to stop logging and wait for it to finish.

  ***

  #### Returns None
