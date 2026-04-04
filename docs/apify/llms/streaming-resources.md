# Source: https://docs.apify.com/api/client/python/docs/concepts/streaming-resources.md

# Streaming resources

Copy for LLM

Certain resources, such as dataset items, key-value store records, and logs, support streaming directly from the Apify API. This allows you to process large resources incrementally without downloading them entirely into memory, making it ideal for handling large or continuously updated data.

Supported streaming methods:

* [`DatasetClient.stream_items`](https://docs.apify.com/api/client/python/api/client/python/reference/class/DatasetClient.md#stream_items) - Stream dataset items incrementally.
* [`KeyValueStoreClient.stream_record`](https://docs.apify.com/api/client/python/api/client/python/reference/class/KeyValueStoreClient.md#stream_record) - Stream key-value store records as raw data.
* [`LogClient.stream`](https://docs.apify.com/api/client/python/api/client/python/reference/class/LogClient.md#stream) - Stream logs in real time.

These methods return a raw, context-managed `impit.Response` object. The response must be consumed within a with block to ensure that the connection is closed automatically, preventing memory leaks or unclosed connections.

The following example demonstrates how to stream the logs of an Actor run incrementally:

* Async client
* Sync client

```
from apify_client import ApifyClientAsync

TOKEN = 'MY-APIFY-TOKEN'


async def main() -> None:
    apify_client = ApifyClientAsync(TOKEN)
    run_client = apify_client.run('MY-RUN-ID')
    log_client = run_client.log()

    async with log_client.stream() as log_stream:
        if log_stream:
            async for bytes_chunk in log_stream.aiter_bytes():
                print(bytes_chunk)
```

```
from apify_client import ApifyClient

TOKEN = 'MY-APIFY-TOKEN'


def main() -> None:
    apify_client = ApifyClient(TOKEN)
    run_client = apify_client.run('MY-RUN-ID')
    log_client = run_client.log()

    with log_client.stream() as log_stream:
        if log_stream:
            for bytes_chunk in log_stream.iter_bytes():
                print(bytes_chunk)
```

Streaming offers several key benefits. It ensures memory efficiency by loading only a small portion of the resource into memory at any given time, making it ideal for handling large data. It enables real-time processing, allowing you to start working with data immediately as it is received. With automatic resource management, using the `with` statement ensures that connections are properly closed, preventing memory leaks or unclosed connections. This approach is valuable for processing large logs, datasets, or files on the fly without the need to download them entirely.
