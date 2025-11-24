# Source: https://docs.apify.com/api/client/python/docs/examples/passing-input-to-actor.md

# Passing input to Actor

Copy for LLM

The efficient way to run an Actor and retrieve results is by passing input data directly to the `call` method. This method allows you to configure the Actor's input, execute it, and either get a reference to the running Actor or wait for its completion.

The following example demonstrates how to pass input to the `apify/instagram-hashtag-scraper` Actor and wait for it to finish.

* Async client
* Sync client

```
import asyncio

from apify_client import ApifyClientAsync

TOKEN = 'MY-APIFY-TOKEN'


async def main() -> None:
    # Client initialization with the API token
    apify_client = ApifyClientAsync(token=TOKEN)

    # Get the Actor client
    actor_client = apify_client.actor('apify/instagram-hashtag-scraper')

    input_data = {'hashtags': ['rainbow'], 'resultsLimit': 20}

    # Run the Actor and wait for it to finish up to 60 seconds.
    # Input is not persisted for next runs.
    run_result = await actor_client.call(run_input=input_data, timeout_secs=60)


if __name__ == '__main__':
    asyncio.run(main())
```

```
from apify_client import ApifyClient

TOKEN = 'MY-APIFY-TOKEN'


def main() -> None:
    # Client initialization with the API token
    apify_client = ApifyClient(token=TOKEN)

    # Get the Actor client
    actor_client = apify_client.actor('apify/instagram-hashtag-scraper')

    input_data = {'hashtags': ['rainbow'], 'resultsLimit': 20}

    # Run the Actor and wait for it to finish up to 60 seconds.
    # Input is not persisted for next runs.
    run_result = actor_client.call(run_input=input_data, timeout_secs=60)


if __name__ == '__main__':
    main()
```
