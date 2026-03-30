# Source: https://openrouter.ai/docs/sdks/python/api-reference/endpoints.mdx

***

title: Endpoints - Python SDK
subtitle: Endpoints method reference
headline: Endpoints | OpenRouter Python SDK
canonical-url: '[https://openrouter.ai/docs/sdks/python/api-reference/endpoints](https://openrouter.ai/docs/sdks/python/api-reference/endpoints)'
'og:site\_name': OpenRouter Documentation
'og:title': Endpoints | OpenRouter Python SDK
'og:description': >-
Endpoints method documentation for the OpenRouter Python SDK. Learn how to use
this API endpoint with code examples.
'og:image':
type: url
value: >-
[https://openrouter.ai/dynamic-og?title=Endpoints%20-%20Python%20SDK\&description=Endpoints%20method%20reference](https://openrouter.ai/dynamic-og?title=Endpoints%20-%20Python%20SDK\&description=Endpoints%20method%20reference)
'og:image:width': 1200
'og:image:height': 630
'twitter:card': summary\_large\_image
'twitter:site': '@OpenRouter'
noindex: false
nofollow: false
---------------

{/* banner:start */}

<Warning>
  The Python SDK and docs are currently in beta.
  Report issues on [GitHub](https://github.com/OpenRouterTeam/python-sdk/issues).
</Warning>

{/* banner:end */}

(*endpoints*)

## Overview

Endpoint information

### Available Operations

* [list](#list) - List all endpoints for a model
* [list\_zdr\_endpoints](#list_zdr_endpoints) - Preview the impact of ZDR on the available endpoints

## list

List all endpoints for a model

### Example Usage

{/* UsageSnippet language="python" operationID="listEndpoints" method="get" path="/models/{author}/{slug}/endpoints" */}

```python
from openrouter import OpenRouter
import os

with OpenRouter(
    api_key=os.getenv("OPENROUTER_API_KEY", ""),
) as open_router:

    res = open_router.endpoints.list(author="<value>", slug="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter | Type                                                               | Required             | Description                                                         |
| --------- | ------------------------------------------------------------------ | -------------------- | ------------------------------------------------------------------- |
| `author`  | *str*                                                              | :heavy\_check\_mark: | N/A                                                                 |
| `slug`    | *str*                                                              | :heavy\_check\_mark: | N/A                                                                 |
| `retries` | [Optional\[utils.RetryConfig\]](../../models/utils/retryconfig.md) | :heavy\_minus\_sign: | Configuration to override the default retry behavior of the client. |

### Response

**[operations.ListEndpointsResponse](/docs/sdks/python/api-reference/operations/listendpointsresponse)**

### Errors

| Error Type                         | Status Code | Content Type     |
| ---------------------------------- | ----------- | ---------------- |
| errors.NotFoundResponseError       | 404         | application/json |
| errors.InternalServerResponseError | 500         | application/json |
| errors.OpenRouterDefaultError      | 4XX, 5XX    | \*/\*            |

## list\_zdr\_endpoints

Preview the impact of ZDR on the available endpoints

### Example Usage

{/* UsageSnippet language="python" operationID="listEndpointsZdr" method="get" path="/endpoints/zdr" */}

```python
from openrouter import OpenRouter
import os

with OpenRouter(
    api_key=os.getenv("OPENROUTER_API_KEY", ""),
) as open_router:

    res = open_router.endpoints.list_zdr_endpoints()

    # Handle response
    print(res)

```

### Parameters

| Parameter | Type                                                               | Required             | Description                                                         |
| --------- | ------------------------------------------------------------------ | -------------------- | ------------------------------------------------------------------- |
| `retries` | [Optional\[utils.RetryConfig\]](../../models/utils/retryconfig.md) | :heavy\_minus\_sign: | Configuration to override the default retry behavior of the client. |

### Response

**[operations.ListEndpointsZdrResponse](/docs/sdks/python/api-reference/operations/listendpointszdrresponse)**

### Errors

| Error Type                         | Status Code | Content Type     |
| ---------------------------------- | ----------- | ---------------- |
| errors.InternalServerResponseError | 500         | application/json |
| errors.OpenRouterDefaultError      | 4XX, 5XX    | \*/\*            |
