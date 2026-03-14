# Source: https://docs.linkup.so/pages/documentation/development/authentication.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.linkup.so/llms.txt
> Use this file to discover all available pages before exploring further.

# Authentication

> Authenticate with the Linkup API

<Card title="Get your API key" icon="key" href="https://app.linkup.so" horizontal="True">
  Create a Linkup account for free to get your API key.
</Card>

## Using cURL

Your API key needs to be sent along all your request as a Bearer token in the `Authorization` header.

```shell curl theme={null}
curl "https://api.linkup.so/v1/search" \
    -G \
    -H "Authorization: Bearer <YOUR_LINKUP_API_KEY>" \
    ...
```

## Using the Python SDK

**Option 1:** Set a `LINKUP_API_KEY` environment variable in your shell before using the SDK.

```shell shell theme={null}
export LINKUP_API_KEY='<YOUR_LINKUP_API_KEY>'
```

**Option 2:**  Set the `LINKUP_API_KEY` environment variable directly within Python, using for instance `os.environ` or [python-dotenv](https://github.com/theskumar/python-dotenv).

```python python theme={null}
import os
from linkup import LinkupClient

os.environ["LINKUP_API_KEY"] = "<YOUR_LINKUP_API_KEY>"
# or dotenv.load_dotenv()
client = LinkupClient()
...
```

**Option 3**: Directly pass the Linkup API key to the Linkup Client.

```python python theme={null}
from linkup import LinkupClient

client = LinkupClient(api_key="<YOUR_LINKUP_API_KEY>")
...
```

## Using the JS SDK

Pass the Linkup API key to the Linkup Client.

```js js theme={null}
import { LinkupClient } from 'linkup-sdk';

const client = new LinkupClient({
  apiKey: '<YOUR_LINKUP_API_KEY>',
});
```

<Info>
  Facing issues? Reach out to our engineering team at [support@linkup.so](mailto:support@linkup.so) or via our [Discord](https://discord.com/invite/9q9mCYJa86) or [book a 15 minutes call](https://calendar.app.google/tEzK3mMKyLyp5Hsv9) with a member of our technical team.
</Info>


Built with [Mintlify](https://mintlify.com).