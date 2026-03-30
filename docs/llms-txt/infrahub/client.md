# Source: https://docs.infrahub.app/python-sdk/sdk_ref/infrahub_sdk/client.md

# Source: https://docs.infrahub.app/python-sdk/guides/client.md

# How to create and configure an Infrahub client

This guide shows you how to create and configure an Infrahub client using the Python SDK. You'll learn how to set up authentication, configure proxy settings, and customize client behavior for your infrastructure automation workflows.

At the end of this guide, you'll have a fully configured client ready to interact with your Infrahub instance.

TL;DR;

If you prefer to jump right in, check out the ["Hello World" example](#hello-world-example) at the end of this guide for a quick reference implementation.

## Prerequisites[​](#prerequisites "Direct link to Prerequisites")

* Python 3.9 or higher
* Infrahub SDK installed (`pip install infrahub-sdk` or `uv add infrahub-sdk`)
* Access to an Infrahub instance (local or remote)
* Valid credentials (API token or username/password) if authentication is required

## Step 1: Create a client instance[​](#step-1-create-a-client-instance "Direct link to Step 1: Create a client instance")

Asynchronous vs. Synchronous Clients

The SDK offers both asynchronous and synchronous client implementations. Choose the one that best fits your application architecture:

* **Asynchronous client** (`InfrahubClient`): Ideal for modern async applications using Python's `async`/`await` syntax
* **Synchronous client** (`InfrahubClientSync`): Better for traditional synchronous workflows or scripts

- Async
- Sync

Create an `InfrahubClient` for async/await workflows:

```
from infrahub_sdk import InfrahubClient

# Connect to local Infrahub instance
client = InfrahubClient()
```

Create an `InfrahubClientSync` for traditional synchronous code:

```
from infrahub_sdk import InfrahubClientSync

# Connect to local Infrahub instance
client = InfrahubClientSync()
```

## Step 2: Configure authentication and address[​](#step-2-configure-authentication-and-address "Direct link to Step 2: Configure authentication and address")

Next, configure the address of your Infrahub instance and set up authentication credentials. Infrahub supports two authentication methods: API tokens and username/password.

Configuration Methods

You can configure the client in two ways:

1. **Environment variables**: Ideal for sensitive information
2. **`Config` object**: Better for explicit configuration in code

You can also combine both methods, where the `Config` object takes precedence over environment variables.

You can find the full list of configuration options in the [SDK configuration reference](/python-sdk/reference/config.md).

### Using API tokens[​](#using-api-tokens "Direct link to Using API tokens")

API tokens provide secure, long-lived authentication and are the recommended method for most use cases, especially for automation scripts and non-interactive applications.

* Async
* Sync

- Code
- Environment

We can set the address and API token directly in the `Config` object:

```
from infrahub_sdk import Config, InfrahubClient
client = InfrahubClient(config=Config(address="http://localhost:8000", api_token="token"))
```

We need to export the address and API token as an environment variable:

```
export INFRAHUB_ADDRESS="http://localhost:8000"
export INFRAHUB_API_TOKEN="token"
```

```
from infrahub_sdk import InfrahubClient
client = InfrahubClient() # token and address are read from the INFRAHUB_API_TOKEN and INFRAHUB_ADDRESS environment variables
```

* Code
* Environment

We can set the address and API token directly in the `Config` object:

```
from infrahub_sdk import Config, InfrahubClientSync
client = InfrahubClientSync(config=Config(address="http://localhost:8000", api_token="token"))
```

We need to export the address and API token as an environment variable:

```
export INFRAHUB_ADDRESS="http://localhost:8000"
export INFRAHUB_API_TOKEN="token"
```

```
from infrahub_sdk import InfrahubClientSync
client = InfrahubClientSync() # token and address are read from the INFRAHUB_API_TOKEN and INFRAHUB_ADDRESS environment variables
```

### Using username/password[​](#using-usernamepassword "Direct link to Using username/password")

For interactive authentication, use username and password. The SDK automatically handles JWT token generation and refresh.

* Async
* Sync

- Code
- Environment

We can set the address, username and password directly in the `Config` object:

```
from infrahub_sdk import Config, InfrahubClient
client = InfrahubClient(config=Config(address="http://localhost:8000", username="admin", password="infrahub"))
```

We need to export the address, username and password as environment variables:

```
export INFRAHUB_ADDRESS="http://localhost:8000"
export INFRAHUB_USERNAME="admin"
export INFRAHUB_PASSWORD="infrahub"
```

```
from infrahub_sdk import InfrahubClient
client = InfrahubClient() # username and password are read from the INFRAHUB_USERNAME and INFRAHUB_PASSWORD environment variables
```

* Code
* Environment

We can set the address, username and password directly in the `Config` object:

```
from infrahub_sdk import Config, InfrahubClientSync
client = InfrahubClientSync(config=Config(address="http://localhost:8000", username="admin", password="infrahub"))
```

We need to export the address, username and password as environment variables:

```
export INFRAHUB_ADDRESS="http://localhost:8000"
export INFRAHUB_USERNAME="admin"
export INFRAHUB_PASSWORD="infrahub"
```

```
from infrahub_sdk import InfrahubClientSync
client = InfrahubClientSync() # username and password are read from the INFRAHUB_USERNAME and INFRAHUB_PASSWORD environment variables
```

success

Your client is now configured and ready to use!

## Step 3: Set the default branch (optional)[​](#step-3-set-the-default-branch-optional "Direct link to Step 3: Set the default branch (optional)")

Configure your client to work with a specific Infrahub branch instead of the default `main` branch. This is particularly useful when working on feature branches or experimental changes, as it eliminates the need to specify the branch name in every method call.

* Code
* Environment

```
from infrahub_sdk import InfrahubClient, Config
config = Config(address="http://localhost:8000", api_token="token", default_branch="other-branch")
client_other_branch = InfrahubClient(config=config)

tag_other_branch = await client_other_branch.get(kind="BuiltinTag", name__value="RED")
tag_main_branch = await client_other_branch.get(kind="BuiltinTag", name__value="RED", branch="main")
```

```
export INFRAHUB_ADDRESS="http://localhost:8000"
export INFRAHUB_API_TOKEN="token"
export INFRAHUB_DEFAULT_BRANCH="other-branch"
```

```
from infrahub_sdk import InfrahubClient
client_other_branch = InfrahubClient()

tag_other_branch = await client_other_branch.get(kind="BuiltinTag", name__value="RED")
tag_main_branch = await client_other_branch.get(kind="BuiltinTag", name__value="RED", branch="main")
```

Branch Configuration

Your client is now configured to use the specified default branch instead of `main`. Remember that you can always override this setting by explicitly passing the `branch` argument to any method call.

## Hello world example[​](#hello-world-example "Direct link to Hello world example")

Let's create a "Hello World" example to verify your client configuration works correctly. This example will connect to your Infrahub instance and query the available accounts.

1. Create a new file called `hello_world.py`:

```
touch hello_world.py
```

File Naming

Avoid naming your script `test.py` as this name could conflict with Python's testing modules.

2. Add the following code to `hello_world.py`:

* Async
* Sync

```
import asyncio

from infrahub_sdk import Config, InfrahubClient


async def hello_world():
    client = InfrahubClient(config=Config(address="http://localhost:8000"))

    # Try to query accounts to validate connection
    try:
        accounts = await client.all(kind="CoreAccount")
        print(f"Successfully connected to Infrahub! Found {len(accounts)} account(s)")
    except Exception as e:
        print(f"Something went wrong: {e}")


asyncio.run(hello_world())
```

```
from infrahub_sdk import Config, InfrahubClientSync


# Test connection and authentication
def hello_world():
    client = InfrahubClientSync(config=Config(address="http://localhost:8000"))

    # Try to query accounts to validate connection
    try:
        accounts = client.all(kind="CoreAccount")
        print(f"Successfully connected to Infrahub! Found {len(accounts)} account(s)")
    except Exception as e:
        print(f"Something went wrong: {e}")


hello_world()
```

3. Export the necessary environment variables:

```
export INFRAHUB_API_TOKEN="06438eb2-8019-4776-878c-0941b1f1d1ec" # This is the default token
```

4. Run the script:

```
python hello_world.py
```

If everything is configured correctly, you should see:

success

`Successfully connected to Infrahub! Found 1 account(s)`

## Advanced use cases[​](#advanced-use-cases "Direct link to Advanced use cases")

### Enable debug logging[​](#enable-debug-logging "Direct link to Enable debug logging")

When developing or troubleshooting, you can enable GraphQL query logging to see exactly what requests are being sent to Infrahub:

* Code
* Environment

```
from infrahub_sdk import Config, InfrahubClient
config = Config(echo_graphql_queries=True)
client = InfrahubClient(config=config)
```

```
export INFRAHUB_ECHO_GRAPHQL_QUERIES=true
```

```
from infrahub_sdk import InfrahubClient
client = InfrahubClient()  # debug flag state is read from the INFRAHUB_ECHO_GRAPHQL_QUERIES environment variables
```

### Configure proxy settings[​](#configure-proxy-settings "Direct link to Configure proxy settings")

When operating in environments with restricted network access or behind corporate firewalls, you can configure the client to route requests through HTTP/HTTPS proxies.

#### Single proxy for all requests[​](#single-proxy-for-all-requests "Direct link to Single proxy for all requests")

To route all traffic through the same proxy server, use the `INFRAHUB_PROXY` environment variable or the `proxy` configuration parameter:

* Async
* Sync

```
from infrahub_sdk import Config, InfrahubClient
config = Config(proxy="http://proxy.example.com:8080")
client = InfrahubClient(config=config)

# Or using environment variable
# export INFRAHUB_PROXY=http://proxy.example.com:8080
client = InfrahubClient()
```

```
from infrahub_sdk import Config, InfrahubClientSync
config = Config(proxy="http://proxy.example.com:8080")
client = InfrahubClientSync(config=config)

# Or using environment variable
# export INFRAHUB_PROXY=http://proxy.example.com:8080
client = InfrahubClientSync()
```

#### Separate proxies for HTTP and HTTPS[​](#separate-proxies-for-http-and-https "Direct link to Separate proxies for HTTP and HTTPS")

In some network environments, you might need to route HTTP and HTTPS traffic through different proxy servers. Use the `INFRAHUB_PROXY_MOUNTS_HTTP` and `INFRAHUB_PROXY_MOUNTS_HTTPS` environment variables for this purpose:

```
export INFRAHUB_PROXY_MOUNTS_HTTP=http://http-proxy.example.com:8080
export INFRAHUB_PROXY_MOUNTS_HTTPS=http://https-proxy.example.com:8080
```

* Async
* Sync

```
from infrahub_sdk import InfrahubClient
# Proxy configuration is read from environment variables
client = InfrahubClient()
```

```
from infrahub_sdk import InfrahubClientSync
# Proxy configuration is read from environment variables
client = InfrahubClientSync()
```

Using both `proxy` and `proxy_mounts`

The `proxy` and `proxy_mounts` configurations are mutually exclusive and cannot be used together. Specifying both will cause a `ValueError` to be raised when the client is initialized.

## Next steps[​](#next-steps "Direct link to Next steps")

Now that you have a fully configured Infrahub client, you're ready to start working with your infrastructure data. Here's what you can explore next:

* **[Query objects and data](/python-sdk/guides/query_data.md)**: Learn how to retrieve objects and data from your Infrahub instance
* **[Create, update and delete objects](/python-sdk/guides/create_update_delete.md)**: Manage your infrastructure data programmatically
* **[Work with branches](/python-sdk/guides/branches.md)**: Use Infrahub's branch-based workflow to manage infrastructure changes
* **[Batch operations](/python-sdk/guides/batch.md)**: Optimize performance with batch operations for multiple objects

## Related resources[​](#related-resources "Direct link to Related resources")

* **[SDK Configuration Reference](/python-sdk/reference/config.md)**: Complete list of all configuration options
* **[Installation Guide](/python-sdk/guides/installation.md)**: Detailed instructions for installing the SDK
* **[Python Typing Guide](/python-sdk/guides/python-typing.md)**: Improve your development experience with type hints
* **[Tracking Guide](/python-sdk/guides/tracking.md)**: Learn how to monitor and trace SDK operations
