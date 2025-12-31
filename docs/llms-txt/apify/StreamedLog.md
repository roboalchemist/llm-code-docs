# Source: https://docs.apify.com/api/client/python/reference/class/StreamedLog.md

# Source: https://docs.apify.com/api/client/js/reference/class/StreamedLog.md

# Source: https://docs.apify.com/api/client/python/reference/class/StreamedLog.md

# Source: https://docs.apify.com/api/client/js/reference/class/StreamedLog.md

# Source: https://docs.apify.com/api/client/python/reference/class/StreamedLog.md

# Source: https://docs.apify.com/api/client/js/reference/class/StreamedLog.md

# Source: https://docs.apify.com/api/client/python/reference/class/StreamedLog.md

# StreamedLog<!-- -->

Utility class for streaming logs from another Actor.

It uses buffer to deal with possibly chunked logs. Chunked logs are stored in buffer. Chunks are expected to contain specific markers that indicate the start of the log message. Each time a new chunk with complete split marker arrives, the buffer is processed, logged and emptied.

This works only if the logs have datetime marker in ISO format. For example, `2025-05-12T15:35:59.429Z` This is the default log standard for the actors.

### Hierarchy

* *StreamedLog*

  * [StreamedLogSync](https://docs.apify.com/api/client/python/api/client/python/reference/class/StreamedLogSync.md)
  * [StreamedLogAsync](https://docs.apify.com/api/client/python/api/client/python/reference/class/StreamedLogAsync.md)

## Index[**](#Index)

### Methods

* [**\_\_init\_\_](https://docs.apify.com/api/client/python/api/client/python/reference/class/StreamedLog.md#__init__)

## Methods<!-- -->[**](#Methods)

### [**](#__init__)[**](https://undefined/apify/apify-client-python/blob/master//src/apify_client/clients/resource_clients/log.py#L216)\_\_init\_\_

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
