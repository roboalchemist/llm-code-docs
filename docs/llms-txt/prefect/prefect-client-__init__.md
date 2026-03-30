# Source: https://docs.prefect.io/v3/api-ref/python/prefect-client-__init__.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# __init__

# `prefect.client`

Asynchronous client implementation for communicating with the [Prefect REST API](https://docs.prefect.io/v3/api-ref/rest-api/).

Explore the client by communicating with an in-memory webserver - no setup required:

\<div class="termy">

```
$ # start python REPL with native await functionality
$ python -m asyncio
from prefect.client.orchestration import get_client
async with get_client() as client:
    response = await client.hello()
    print(response.json())
👋
```

\</div>


Built with [Mintlify](https://mintlify.com).