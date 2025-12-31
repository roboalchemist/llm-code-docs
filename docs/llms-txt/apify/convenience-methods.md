# Source: https://docs.apify.com/api/client/python/docs/concepts/convenience-methods.md

# Convenience methods

Copy for LLM

The Apify client provides several convenience methods to handle actions that the API alone cannot perform efficiently, such as waiting for an Actor run to finish without running into network timeouts. These methods simplify common tasks and enhance the usability of the client.

* [`ActorClient.call`](https://docs.apify.com/api/client/python/api/client/python/reference/class/ActorClient.md#call) - Starts an Actor and waits for it to finish, handling network timeouts internally.
* [`ActorClient.start`](https://docs.apify.com/api/client/python/api/client/python/reference/class/ActorClient.md#start) - Explicitly waits for an Actor run to finish with customizable timeouts.

Additionally, storage-related resources offer flexible options for data retrieval:

* [Key-value store](https://docs.apify.com/platform/storage/key-value-store) records can be retrieved as objects, buffers, or streams.
* [Dataset](https://docs.apify.com/platform/storage/dataset) items can be fetched as individual objects, serialized data, or iterated asynchronously.

- Async client
- Sync client

```
from apify_client import ApifyClientAsync

TOKEN = 'MY-APIFY-TOKEN'


async def main() -> None:
    apify_client = ApifyClientAsync(TOKEN)
    actor_client = apify_client.actor('username/actor-name')

    # Start an Actor and waits for it to finish
    finished_actor_run = await actor_client.call()

    # Starts an Actor and waits maximum 60s (1 minute) for the finish
    actor_run = await actor_client.start(wait_for_finish=60)
```

```
from apify_client import ApifyClient

TOKEN = 'MY-APIFY-TOKEN'


def main() -> None:
    apify_client = ApifyClient(TOKEN)
    actor_client = apify_client.actor('username/actor-name')

    # Start an Actor and waits for it to finish
    finished_actor_run = actor_client.call()

    # Starts an Actor and waits maximum 60s (1 minute) for the finish
    actor_run = actor_client.start(wait_for_finish=60)
```
