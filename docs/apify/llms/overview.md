# Source: https://docs.apify.com/sdk/python/docs/overview.md

# Source: https://docs.apify.com/sdk/js/docs/readme/overview.md

# Source: https://docs.apify.com/sdk/js/docs/overview.md

# Source: https://docs.apify.com/api/client/python/docs/overview.md

# Overview

Copy for LLM

## Introduction[](#introduction)

The [Apify client for Python](https://github.com/apify/apify-client-python) is the official library to access the [Apify REST API](https://docs.apify.com/api/client/python/api/client/python/api/v2) from your Python applications. It provides useful features like automatic retries and convenience functions that improve the experience of using the Apify API.

Key features:

* Synchronous and asynchronous interfaces for flexible integration
* Automatic retries for improved reliability
* JSON encoding with UTF-8 for all requests and responses
* Comprehensive API coverage for [Actors](https://docs.apify.com/api/client/python/api/client/python/platform/actors), [datasets](https://docs.apify.com/api/client/python/api/client/python/platform/storage/dataset), [key-value stores](https://docs.apify.com/api/client/python/api/client/python/platform/storage/key-value-store), and more

## Prerequisites[](#prerequisites)

Before installing the Apify client, ensure your system meets the following requirements:

* *An Apify account*
* *Python 3.10 or higher*: You can download Python from the [official website](https://www.python.org/downloads/).
* *Python package manager*: While this guide uses [pip](https://pip.pypa.io/en/stable/), you can also use any package manager you want.

To verify that Python and pip are installed, run the following commands:

```
python --version
```

```
pip --version
```

If these commands return the respective versions, you're ready to continue.

## Installation[](#installation)

The Apify client is available as the [`apify-client`](https://pypi.org/project/apify-client/) package on PyPI. To install it, run:

```
pip install apify-client
```

After installation, verify that the client is installed correctly by checking its version:

```
python -c 'import apify_client; print(apify_client.__version__)'
```

## Authentication and initialization[](#authentication-and-initialization)

To use the client, you need an [API token](https://docs.apify.com/api/client/python/api/client/python/platform/integrations/api#api-token). You can find your token under the [Integrations](https://console.apify.com/account/integrations) tab in Apify Console. Copy the token and initialize the client by providing it as a parameter to the `ApifyClient` constructor.

* Async client
* Sync client

```
from apify_client import ApifyClientAsync

TOKEN = 'MY-APIFY-TOKEN'


async def main() -> None:
    # Client initialization with the API token.
    apify_client = ApifyClientAsync(TOKEN)
```

```
from apify_client import ApifyClient

TOKEN = 'MY-APIFY-TOKEN'


def main() -> None:
    # Client initialization with the API token.
    apify_client = ApifyClient(TOKEN)
```

Secure access

The API token is used to authorize your requests to the Apify API. You can be charged for the usage of the underlying services, so do not share your API token with untrusted parties or expose it on the client side of your applications.

## Quick start[](#quick-start)

Now that you have the client set up, let's explore how to run Actors on the Apify platform, provide input to them, and retrieve their results.

### Running your first Actor[](#running-your-first-actor)

To start an Actor, you need its ID (e.g., `john-doe/my-cool-actor`) and an API token. The Actor's ID is a combination of the Actor name and the Actor owner's username. Use the [`ActorClient`](https://docs.apify.com/api/client/python/api/client/python/reference/class/ActorClient.md) to run the Actor and wait for it to complete. You can run both your own Actors and [Actors from Apify Store](https://docs.apify.com/platform/actors/running/actors-in-store).

* Async client
* Sync client

```
from apify_client import ApifyClientAsync

# You can find your API token at https://console.apify.com/settings/integrations.
TOKEN = 'MY-APIFY-TOKEN'


async def main() -> None:
    apify_client = ApifyClientAsync(TOKEN)

    # Start an Actor and wait for it to finish.
    actor_client = apify_client.actor('john-doe/my-cool-actor')
    call_result = await actor_client.call()

    if call_result is None:
        print('Actor run failed.')
        return

    # Fetch results from the Actor run's default dataset.
    dataset_client = apify_client.dataset(call_result['defaultDatasetId'])
    list_items_result = await dataset_client.list_items()
    print(f'Dataset: {list_items_result}')
```

```
from apify_client import ApifyClient

# You can find your API token at https://console.apify.com/settings/integrations.
TOKEN = 'MY-APIFY-TOKEN'


def main() -> None:
    apify_client = ApifyClient(TOKEN)

    # Start an Actor and wait for it to finish.
    actor_client = apify_client.actor('john-doe/my-cool-actor')
    call_result = actor_client.call()

    if call_result is None:
        print('Actor run failed.')
        return

    # Fetch results from the Actor run's default dataset.
    dataset_client = apify_client.dataset(call_result['defaultDatasetId'])
    list_items_result = dataset_client.list_items()
    print(f'Dataset: {list_items_result}')
```

### Providing input to Actor[](#providing-input-to-actor)

Actors often require input, such as URLs to scrape, search terms, or other configuration data. You can pass input as a JSON object when starting the Actor using the [`ActorClient.call`](https://docs.apify.com/api/client/python/api/client/python/reference/class/ActorClient.md#call) method. Actors respect the input schema defined in the Actor's [input schema](https://docs.apify.com/platform/actors/development/actor-definition/input-schema).

* Async client
* Sync client

```
from apify_client import ApifyClientAsync

TOKEN = 'MY-APIFY-TOKEN'


async def main() -> None:
    apify_client = ApifyClientAsync(TOKEN)
    actor_client = apify_client.actor('username/actor-name')

    # Define the input for the Actor.
    run_input = {
        'some': 'input',
    }

    # Start an Actor and waits for it to finish.
    call_result = await actor_client.call(run_input=run_input)
```

```
from apify_client import ApifyClient

TOKEN = 'MY-APIFY-TOKEN'


def main() -> None:
    apify_client = ApifyClient(TOKEN)
    actor_client = apify_client.actor('username/actor-name')

    # Define the input for the Actor.
    run_input = {
        'some': 'input',
    }

    # Start an Actor and waits for it to finish.
    call_result = actor_client.call(run_input=run_input)
```

### Getting results from the dataset[](#getting-results-from-the-dataset)

To get the results from the dataset, you can use the [`DatasetClient`](https://docs.apify.com/api/client/python/api/client/python/reference/class/DatasetClient.md) ([`ApifyClient.dataset`](https://docs.apify.com/api/client/python/api/client/python/reference/class/ApifyClient.md#dataset)) and [`DatasetClient.list_items`](https://docs.apify.com/api/client/python/api/client/python/reference/class/DatasetClient.md#list_items) method. You need to pass the dataset ID to define which dataset you want to access. You can get the dataset ID from the Actor's run dictionary (represented by `defaultDatasetId`).

* Async client
* Sync client

```
from apify_client import ApifyClientAsync

TOKEN = 'MY-APIFY-TOKEN'


async def main() -> None:
    apify_client = ApifyClientAsync(TOKEN)
    dataset_client = apify_client.dataset('dataset-id')

    # Lists items from the Actor's dataset.
    dataset_items = (await dataset_client.list_items()).items
```

```
from apify_client import ApifyClient

TOKEN = 'MY-APIFY-TOKEN'


def main() -> None:
    apify_client = ApifyClient(TOKEN)
    dataset_client = apify_client.dataset('dataset-id')

    # Lists items from the Actor's dataset.
    dataset_items = dataset_client.list_items().items
```

Dataset access

Running an Actor might take time, depending on the Actor's complexity and the amount of data it processes. If you want only to get data and have an immediate response, you should access the existing dataset of the finished [Actor run](https://docs.apify.com/platform/actors/running/runs-and-builds#runs).

## Next steps[](#next-steps)

Now that you're familiar with the basics, explore more advanced features:

* [Asyncio support](https://docs.apify.com/api/client/python/api/client/python/concepts/asyncio-support) - Learn about asynchronous programming with the client

* Common use-case examples like:

  <!-- -->

  * [Passing an input to Actor](https://docs.apify.com/api/client/python/api/client/python/docs/examples/passing-input-to-actor.md)
  * [Retrieve Actor data](https://docs.apify.com/api/client/python/api/client/python/docs/examples/retrieve-actor-data.md)

* [API Reference](https://docs.apify.com/api/client/python/api/client/python/reference.md) - Browse the complete API documentation
