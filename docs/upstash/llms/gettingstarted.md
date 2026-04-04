# Source: https://upstash.com/docs/vector/sdks/py/gettingstarted.md

# Source: https://upstash.com/docs/search/sdks/py/gettingstarted.md

# Source: https://upstash.com/docs/redis/sdks/ratelimit-ts/gettingstarted.md

# Source: https://upstash.com/docs/redis/sdks/ratelimit-py/gettingstarted.md

# Source: https://upstash.com/docs/redis/sdks/py/gettingstarted.md

# Source: https://upstash.com/docs/qstash/sdks/ts/gettingstarted.md

# Source: https://upstash.com/docs/qstash/sdks/py/gettingstarted.md

> ## Documentation Index
> Fetch the complete documentation index at: https://upstash.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Getting Started

## Install

### PyPI

```bash  theme={"system"}
pip install qstash
```

## Get QStash token

Follow the instructions [here](/qstash/overall/getstarted) to get your QStash token and signing keys.

## Usage

#### Synchronous Client

```python  theme={"system"}
from qstash import QStash

client = QStash("<QSTASH_TOKEN>")
client.message.publish_json(...)
```

#### Asynchronous Client

```python  theme={"system"}
import asyncio

from qstash import AsyncQStash


async def main():
    client = AsyncQStash("<QSTASH_TOKEN>")
    await client.message.publish_json(...)


asyncio.run(main())
```

#### RetryConfig

You can configure the retry policy of the client by passing the configuration to the client constructor.

Note: This isn for sending the request to QStash, not for the retry policy of QStash.

The default number of retries is **5** and the default backoff function is `lambda retry_count: math.exp(retry_count) * 50`.

You can also pass in `False` to disable retrying.

```python  theme={"system"}
from qstash import QStash

client = QStash(
    "<QSTASH_TOKEN>",
    retry={
        "retries": 3,
        "backoff": lambda retry_count: (2**retry_count) * 20,
    },
)
```
