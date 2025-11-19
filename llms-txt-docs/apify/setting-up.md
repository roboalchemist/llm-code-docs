# Source: https://docs.apify.com/api/client/python/docs/overview/setting-up.md

# Setting up

Copy for LLM

This guide will help you get started with [Apify client for Python](https://github.com/apify/apify-client-python) by setting it up on your computer. Follow the steps below to ensure a smooth installation process.

## Prerequisites[](#prerequisites)

Before installing `apify-client` itself, make sure that your system meets the following requirements:

* **Python 3.10 or higher**: `apify-client` requires Python 3.10 or a newer version. You can download Python from the [official website](https://www.python.org/downloads/).
* **Python package manager**: While this guide uses Pip (the most common package manager), you can also use any package manager you want. You can download Pip from the [official website](https://pip.pypa.io/en/stable/installation/).

### Verifying prerequisites[](#verifying-prerequisites)

To check if Python and the Pip package manager are installed, run the following commands:

```
python --version
```

```
pip --version
```

If these commands return the respective versions, you're ready to continue.

## Installation[](#installation)

Apify client for Python is available as the [`apify-client`](https://pypi.org/project/apify-client/) package on PyPI. To install it, run:

```
pip install apify-client
```

After installation, verify that `apify-client` is installed correctly by checking its version:

```
python -c 'import apify_client; print(apify_client.__version__)'
```

## Authentication and initialization[](#authentication-and-initialization)

To use the client, you need an [API token](https://docs.apify.com/platform/integrations/api#api-token). You can find your token under [Integrations](https://console.apify.com/account/integrations) tab in Apify Console. Copy the token and initialize the client by providing the token (`MY-APIFY-TOKEN`) as a parameter to the `ApifyClient` constructor.

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
