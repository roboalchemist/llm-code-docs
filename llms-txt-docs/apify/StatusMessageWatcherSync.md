# Source: https://docs.apify.com/api/client/python/reference/class/StatusMessageWatcherSync.md

# StatusMessageWatcherSync<!-- -->

Sync variant of `StatusMessageWatcher` that is logging in thread.

### Hierarchy

* [StatusMessageWatcher](https://docs.apify.com/api/client/python/api/client/python/reference/class/StatusMessageWatcher.md)
  * *StatusMessageWatcherSync*

## Index[**](#Index)

### Methods

* [**\_\_enter\_\_](https://docs.apify.com/api/client/python/api/client/python/reference/class/StatusMessageWatcherSync.md#__enter__)
* [**\_\_exit\_\_](https://docs.apify.com/api/client/python/api/client/python/reference/class/StatusMessageWatcherSync.md#__exit__)
* [**\_\_init\_\_](https://docs.apify.com/api/client/python/api/client/python/reference/class/StatusMessageWatcherSync.md#__init__)
* [**start](https://docs.apify.com/api/client/python/api/client/python/reference/class/StatusMessageWatcherSync.md#start)
* [**stop](https://docs.apify.com/api/client/python/api/client/python/reference/class/StatusMessageWatcherSync.md#stop)

## Methods<!-- -->[**](#Methods)

### [**](#__enter__)[**](https://undefined/apify/apify-client-python/blob/master//src/apify_client/clients/resource_clients/log.py#L521)\_\_enter\_\_

* ****\_\_enter\_\_**(): Self

- Start the logging task within the context. Exiting the context will cancel the logging task.

  ***

  #### Returns Self

### [**](#__exit__)[**](https://undefined/apify/apify-client-python/blob/master//src/apify_client/clients/resource_clients/log.py#L526)\_\_exit\_\_

* ****\_\_exit\_\_**(exc\_type, exc\_val, exc\_tb): None

- Cancel the logging task.

  ***

  #### Parameters

  * ##### exc\_type: type\[BaseException] | None
  * ##### exc\_val: BaseException | None
  * ##### exc\_tb: TracebackType | None

  #### Returns None

### [**](#__init__)[**](https://undefined/apify/apify-client-python/blob/master//src/apify_client/clients/resource_clients/log.py#L487)\_\_init\_\_

* ****\_\_init\_\_**(\*, run\_client, to\_logger, check\_period): None

- Overrides [StatusMessageWatcher.\_\_init\_\_](https://docs.apify.com/api/client/python/api/client/python/reference/class/StatusMessageWatcher.md#__init__)

  Initialize `StatusMessageWatcherSync`.

  ***

  #### Parameters

  * ##### keyword-onlyrun\_client: [RunClient](https://docs.apify.com/api/client/python/api/client/python/reference/class/RunClient.md)

    The client for run that will be used to get a status and message.

  * ##### keyword-onlyto\_logger: logging.Logger

    The logger to which the status message will be redirected.

  * ##### optionalkeyword-onlycheck\_period: timedelta = <!-- -->timedelta(seconds=1)

    The period with which the status message will be polled.

  #### Returns None

### [**](#start)[**](https://undefined/apify/apify-client-python/blob/master//src/apify_client/clients/resource_clients/log.py#L502)start

* ****start**(): Thread

- Start the logging thread. The caller has to handle any cleanup by manually calling the `stop` method.

  ***

  #### Returns Thread

### [**](#stop)[**](https://undefined/apify/apify-client-python/blob/master//src/apify_client/clients/resource_clients/log.py#L511)stop

* ****stop**(): None

- Signal the \_logging\_thread thread to stop logging and wait for it to finish.

  ***

  #### Returns None
