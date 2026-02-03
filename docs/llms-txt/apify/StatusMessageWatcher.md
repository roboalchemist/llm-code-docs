# Source: https://docs.apify.com/api/client/python/reference/class/StatusMessageWatcher.md

# StatusMessageWatcher<!-- -->

Utility class for logging status messages from another Actor run.

Status message is logged at fixed time intervals, and there is no guarantee that all messages will be logged, especially in cases of frequent status message changes.

### Hierarchy

* *StatusMessageWatcher*

  * [StatusMessageWatcherAsync](https://docs.apify.com/api/client/python/api/client/python/reference/class/StatusMessageWatcherAsync.md)
  * [StatusMessageWatcherSync](https://docs.apify.com/api/client/python/api/client/python/reference/class/StatusMessageWatcherSync.md)

## Index[**](#Index)

### Methods

* [**\_\_init\_\_](https://docs.apify.com/api/client/python/api/client/python/reference/class/StatusMessageWatcher.md#__init__)

## Methods<!-- -->[**](#Methods)

### [**](#__init__)[**](https://undefined/apify/apify-client-python/blob/25ff4e51e07fe25d1d338b042eacba1ec0c63e84//src/apify_client/clients/resource_clients/log.py#L394)\_\_init\_\_

* ****\_\_init\_\_**(\*, to\_logger, check\_period): None

- Initialize `StatusMessageWatcher`.

  ***

  #### Parameters

  * ##### keyword-onlyto\_logger: logging.Logger

    The logger to which the status message will be redirected.

  * ##### optionalkeyword-onlycheck\_period: timedelta = <!-- -->timedelta(seconds=5)

    The period with which the status message will be polled.

  #### Returns None
