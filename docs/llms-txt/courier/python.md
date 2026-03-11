# Source: https://www.courier.com/docs/sdk-libraries/python.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Courier Python SDK

> Send notifications from your Python backend using the Courier SDK. Supports sync and async clients, typed requests with Pydantic models, and automatic retries.

The Courier Python SDK provides typed access to the [Courier REST API](/reference/get-started) from any Python 3.9+ application. It includes synchronous and asynchronous clients, Pydantic response models, and TypedDict request params.

Available on
<Link href="https://github.com/trycourier/courier-python"><Icon icon="github" iconType="solid" /> GitHub</Link>
and <Link href="https://pypi.org/project/trycourier/"><Icon icon="python" iconType="solid" /> PyPI</Link>.

## Installation

<CodeGroup>
  ```bash pip theme={null}
  pip install trycourier
  ```

  ```bash poetry theme={null}
  poetry add trycourier
  ```

  ```bash pipenv theme={null}
  pipenv install trycourier
  ```
</CodeGroup>

Requires Python 3.9+.

## Quick Start

```python  theme={null}
from courier import Courier

client = Courier()

response = client.send.message(
    message={
        "to": {"email": "you@example.com"},
        "content": {
            "title": "Hello from Courier!",
            "body": "Your first notification, sent with the Python SDK.",
        },
    },
)

print(response.request_id)
```

<Tip>
  The client reads `COURIER_API_KEY` from your environment automatically. You can also pass it explicitly: `Courier(api_key='your-key')`.
</Tip>

## Authentication

Get your API key from [Settings > API Keys](https://app.courier.com/settings/api-keys) in the Courier dashboard. Set it as an environment variable:

```bash  theme={null}
export COURIER_API_KEY="your-api-key"
```

The SDK picks this up by default. To pass it explicitly:

```python  theme={null}
client = Courier(api_key="your-api-key")
```

<Note>
  We recommend using a `.env` file with [python-dotenv](https://pypi.org/project/python-dotenv/) so your API key stays out of source control.
</Note>

## Sending Notifications

### With a template

Design your notification in the [template designer](/platform/content/template-designer/template-designer-overview), then reference it by ID:

```python  theme={null}
response = client.send.message(
    message={
        "to": {"user_id": "user_123"},
        "template": "my-template-id",
        "data": {"orderNumber": "10042", "itemName": "Courier Hoodie"},
    },
)
```

### With inline content

Skip templates and define content directly in code:

```python  theme={null}
response = client.send.message(
    message={
        "to": {"email": "jane@example.com"},
        "content": {
            "title": "Order shipped",
            "body": "Your order {{orderNumber}} has shipped!",
        },
        "data": {"orderNumber": "10042"},
        "routing": {
            "method": "single",
            "channels": ["email"],
        },
    },
)
```

### To multiple recipients

Send to a list of users in a single call:

```python  theme={null}
response = client.send.message(
    message={
        "to": [
            {"user_id": "user_1"},
            {"user_id": "user_2"},
            {"email": "guest@example.com"},
        ],
        "template": "welcome-template",
    },
)
```

## Async Usage

### Basic async client

Import `AsyncCourier` instead of `Courier` and use `await`:

```python  theme={null}
import asyncio
from courier import AsyncCourier

client = AsyncCourier()

async def main():
    response = await client.send.message(
        message={
            "to": {"email": "you@example.com"},
            "content": {
                "title": "Hello from Courier!",
                "body": "Sent from the async Python client.",
            },
        },
    )
    print(response.request_id)

asyncio.run(main())
```

The async client has the same API as the sync client; every method returns an awaitable.

### Using aiohttp instead of httpx

For improved concurrency performance, you can swap the HTTP backend to `aiohttp`:

```bash  theme={null}
pip install trycourier[aiohttp]
```

```python  theme={null}
from courier import AsyncCourier, DefaultAioHttpClient

async with AsyncCourier(http_client=DefaultAioHttpClient()) as client:
    response = await client.send.message(
        message={
            "to": {"user_id": "user_123"},
            "template": "my-template-id",
        },
    )
```

## Available Resources

The SDK covers the full Courier API. Every method is typed and documented with docstrings.

| Resource      | Namespace              | Description                                            |
| ------------- | ---------------------- | ------------------------------------------------------ |
| Send          | `client.send`          | Send messages to one or more recipients                |
| Messages      | `client.messages`      | Retrieve status, history, and content of sent messages |
| Profiles      | `client.profiles`      | Create, update, and retrieve user profiles             |
| Users         | `client.users`         | Manage preferences, tenants, and push tokens per user  |
| Auth          | `client.auth`          | Issue JWT tokens for client-side SDK authentication    |
| Bulk          | `client.bulk`          | Send messages to large recipient lists via jobs        |
| Lists         | `client.lists`         | Manage subscription lists and their subscribers        |
| Audiences     | `client.audiences`     | Define and query audience segments                     |
| Tenants       | `client.tenants`       | Manage tenants for multi-tenant setups                 |
| Automations   | `client.automations`   | Invoke multi-step automation workflows                 |
| Brands        | `client.brands`        | Manage brand settings (logos, colors, templates)       |
| Notifications | `client.notifications` | List and inspect notification templates                |
| Translations  | `client.translations`  | Manage localized content                               |

## Common Operations

### Checking Message Status

After sending, use the `request_id` to check delivery status or get the full event timeline:

```python  theme={null}
message = client.messages.retrieve("your-message-id")
print(message.status)    # e.g. 'DELIVERED'
print(message.delivered)  # timestamp
print(message.channels)  # which channels were used

history = client.messages.history("your-message-id")
for event in history.results:
    print(event.type, event.event)
```

You can also list recent messages with optional filters:

```python  theme={null}
recent = client.messages.list(status="DELIVERED")
```

### Managing User Profiles

Profiles store recipient data (email, phone, custom fields) that Courier uses for delivery. You need a profile before you can send to a `user_id`.

```python  theme={null}
# Create or merge into a profile
client.profiles.create("user_123", profile={
    "email": "jane@example.com",
    "phone_number": "+15551234567",
    "name": "Jane Doe",
})

# Retrieve a profile
profile = client.profiles.retrieve("user_123")
print(profile.profile["email"])

# Partial update (merge)
client.profiles.update("user_123", profile={"name": "Jane Smith"})
```

<Note>
  `create` merges with any existing profile. Use `replace` for a full overwrite (any fields not included will be removed).
</Note>

### Issuing JWT Tokens

If you use Courier's [client-side SDKs](/sdk-libraries/sdks-overview) (React, JavaScript, mobile), your backend needs to issue JWT tokens for user authentication. The `auth.issue_token` method handles this:

```python  theme={null}
result = client.auth.issue_token(
    scope="user_id:user_123 inbox:read:messages inbox:write:events read:preferences write:preferences",
    expires_in="2 days",
)

# Return result.token to your frontend
print(result.token)
```

The `scope` string controls what the token can access. Common scopes:

| Scope                 | Permission                             |
| --------------------- | -------------------------------------- |
| `user_id:<id>`        | Which user the token is for (required) |
| `inbox:read:messages` | Read inbox messages                    |
| `inbox:write:events`  | Mark messages as read/archived         |
| `read:preferences`    | Read notification preferences          |
| `write:preferences`   | Update notification preferences        |
| `write:user-tokens`   | Register push notification tokens      |

### Bulk Sending

For large recipient lists, use the bulk API. It works in three steps: create a job, add users, then run it.

```python  theme={null}
# 1. Create a bulk job
job = client.bulk.create_job(
    message={"event": "welcome-notification"},
)

# 2. Add recipients
client.bulk.add_users(job.job_id, users=[
    {"profile": {"email": "alice@example.com"}, "data": {"name": "Alice"}},
    {"profile": {"email": "bob@example.com"}, "data": {"name": "Bob"}},
])

# 3. Run the job
client.bulk.run_job(job.job_id)

# Check status
status = client.bulk.retrieve_job(job.job_id)
print(status.status)
```

<Warning>
  For email-based bulk jobs, include `profile.email` on each user. The `to.email` field alone is not sufficient for email provider routing.
</Warning>

## Type Safety

Request parameters are TypedDicts, and responses are Pydantic models. This gives you autocomplete and inline docs in your editor.

```python  theme={null}
response = client.send.message(
    message={
        "to": {"user_id": "user_123"},
        "template": "my-template-id",
        "data": {"foo": "bar"},
    },
)

# Response is a Pydantic model
print(response.request_id)
print(response.to_dict())
print(response.to_json())
```

<Tip>
  For VS Code type checking, set `python.analysis.typeCheckingMode` to `basic` in your settings.
</Tip>

## Configuration

### Error Handling

The SDK throws typed errors for API failures. All errors extend `courier.APIError`:

```python  theme={null}
import courier
from courier import Courier

client = Courier()

try:
    client.send.message(
        message={
            "to": {"user_id": "user_123"},
            "template": "my-template-id",
        },
    )
except courier.APIConnectionError as e:
    print("The server could not be reached")
    print(e.__cause__)
except courier.RateLimitError as e:
    print("Rate limited; back off a bit.")
except courier.APIStatusError as e:
    print(f"API error: {e.status_code}")
    print(e.response)
```

| Status Code | Error Type                 |
| ----------- | -------------------------- |
| 400         | `BadRequestError`          |
| 401         | `AuthenticationError`      |
| 403         | `PermissionDeniedError`    |
| 404         | `NotFoundError`            |
| 422         | `UnprocessableEntityError` |
| 429         | `RateLimitError`           |
| >=500       | `InternalServerError`      |
| N/A         | `APIConnectionError`       |

### Retries

The SDK automatically retries failed requests up to 2 times with exponential backoff. Retried errors include connection failures, 408, 409, 429, and 5xx responses.

```python  theme={null}
# Disable retries
client = Courier(max_retries=0)

# Override per-request
client.with_options(max_retries=5).send.message(
    message={
        "to": {"user_id": "user_123"},
        "template": "my-template-id",
    },
)
```

### Timeouts

Requests time out after 60 seconds by default. Configure globally or per-request:

```python  theme={null}
import httpx
from courier import Courier

# Simple timeout
client = Courier(timeout=20.0)  # 20 seconds

# Granular control
client = Courier(
    timeout=httpx.Timeout(60.0, read=5.0, write=10.0, connect=2.0),
)

# Override per-request
client.with_options(timeout=5.0).send.message(
    message={
        "to": {"user_id": "user_123"},
        "template": "my-template-id",
    },
)
```

On timeout, an `APITimeoutError` is thrown. Timed-out requests are retried by default.

### Logging

Enable debug logging with the `COURIER_LOG` environment variable:

```bash  theme={null}
export COURIER_LOG=info   # or 'debug' for full request/response logging
```

The SDK uses Python's standard `logging` module, so it integrates with any logging setup you already have.

### Raw Response Access

Access HTTP headers or stream the response body:

```python  theme={null}
from courier import Courier

client = Courier()

# Get headers + parsed data
response = client.send.with_raw_response.message(
    message={
        "to": {"user_id": "user_123"},
        "template": "my-template-id",
    },
)
print(response.headers.get("x-request-id"))
send_result = response.parse()

# Stream the response
with client.send.with_streaming_response.message(
    message={
        "to": {"user_id": "user_123"},
        "template": "my-template-id",
    },
) as response:
    for line in response.iter_lines():
        print(line)
```

### Custom HTTP Client

Override the default [httpx client](https://www.python-httpx.org/api/#client) for proxies, custom transports, or other advanced use cases:

```python  theme={null}
import httpx
from courier import Courier, DefaultHttpxClient

client = Courier(
    base_url="http://my.test.server.example.com:8083",
    http_client=DefaultHttpxClient(
        proxy="http://my.proxy.example.com",
        transport=httpx.HTTPTransport(local_address="0.0.0.0"),
    ),
)
```

## More Operations

The SDK covers the full [Courier REST API](/reference/get-started). Here are a few more resources beyond what's documented above:

| Resource         | Method                                                    | Use case                                                                                                                                      |
| ---------------- | --------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| User preferences | `client.users.preferences.retrieve(user_id)`              | Fetch a user's notification preferences for your [preference center](/platform/preferences/preferences-overview)                              |
| Cancel a message | `client.messages.cancel(message_id)`                      | Cancel a delayed or queued message before delivery (returns 409 if already delivered)                                                         |
| Push tokens      | `client.users.tokens.add_single(token, user_id=user_id)`  | Register a device push token for [iOS](/sdk-libraries/ios), [Android](/sdk-libraries/android), or [React Native](/sdk-libraries/react-native) |
| Automations      | `client.automations.invoke.invoke_ad_hoc(automation=...)` | Run a multi-step workflow (delay, send, update profile) via [Automations](/platform/automations/automations-overview)                         |

<CardGroup cols={2}>
  <Card title="API Reference" icon="code" href="/reference/get-started">
    Full REST API docs with request/response examples.
  </Card>

  <Card title="Send API" icon="paper-plane" href="/platform/sending/send-message">
    Learn about the Send endpoint, routing, and message options.
  </Card>

  <Card title="Quickstart" icon="bolt" href="/getting-started/quickstart">
    Send your first notification in under two minutes.
  </Card>

  <Card title="GitHub" icon="github" href="https://github.com/trycourier/courier-python">
    Source code, issues, and changelog.
  </Card>
</CardGroup>
