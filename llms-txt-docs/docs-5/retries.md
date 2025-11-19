# Source: https://docs.apify.com/api/client/python/docs/concepts/retries.md

# Retries

Copy for LLM

When dealing with network communication, failures can occasionally occur. The Apify client automatically retries requests that fail due to:

* Network errors
* Internal errors in the Apify API (HTTP status codes 500 and above)
* Rate limit errors (HTTP status code 429)

By default, the client will retry a failed request up to 8 times. The retry intervals use an exponential backoff strategy:

* The first retry occurs after approximately 500 milliseconds.
* The second retry occurs after approximately 1,000 milliseconds, and so on.

You can customize this behavior using the following options in the [`ApifyClient`](https://docs.apify.com/api/client/python/api/client/python/reference/class/ApifyClient.md) constructor:

* `max_retries`: Defines the maximum number of retry attempts.
* `min_delay_between_retries_millis`: Sets the minimum delay between retries (in milliseconds).

Retries with exponential backoff are a common strategy for handling network errors. They help to reduce the load on the server and increase the chances of a successful request.

* Async client
* Sync client

```
from apify_client import ApifyClientAsync

TOKEN = 'MY-APIFY-TOKEN'


async def main() -> None:
    apify_client = ApifyClientAsync(
        token=TOKEN,
        max_retries=8,
        min_delay_between_retries_millis=500,  # 0.5s
        timeout_secs=360,  # 6 mins
    )
```

```
from apify_client import ApifyClient

TOKEN = 'MY-APIFY-TOKEN'


async def main() -> None:
    apify_client = ApifyClient(
        token=TOKEN,
        max_retries=8,
        min_delay_between_retries_millis=500,  # 0.5s
        timeout_secs=360,  # 6 mins
    )
```
