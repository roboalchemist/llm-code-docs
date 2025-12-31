# Source: https://docs.apify.com/api/client/python/docs/concepts/error-handling.md

# Error handling

Copy for LLM

When you use the Apify client, it automatically extracts all relevant data from the endpoint and returns it in the expected format. Date strings, for instance, are seamlessly converted to Python `datetime.datetime` objects. If an error occurs, the client raises an [`ApifyApiError`](https://docs.apify.com/api/client/python/api/client/python/reference/class/ApifyApiError.md). This exception wraps the raw JSON errors returned by the API and provides additional context, making it easier to debug any issues that arise.

* Async client
* Sync client

```
from apify_client import ApifyClientAsync

TOKEN = 'MY-APIFY-TOKEN'


async def main() -> None:
    apify_client = ApifyClientAsync(TOKEN)

    try:
        # Try to list items from non-existing dataset
        dataset_client = apify_client.dataset('not-existing-dataset-id')
        dataset_items = (await dataset_client.list_items()).items
    except Exception as ApifyApiError:
        # The exception is an instance of ApifyApiError
        print(ApifyApiError)
```

```
from apify_client import ApifyClient

TOKEN = 'MY-APIFY-TOKEN'


def main() -> None:
    apify_client = ApifyClient(TOKEN)

    try:
        # Try to list items from non-existing dataset
        dataset_client = apify_client.dataset('not-existing-dataset-id')
        dataset_items = dataset_client.list_items().items
    except Exception as ApifyApiError:
        # The exception is an instance of ApifyApiError
        print(ApifyApiError)
```
