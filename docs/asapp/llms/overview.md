# Source: https://docs.asapp.com/changelog/overview.md

# Source: https://docs.asapp.com/apis/overview.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.asapp.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Overview

> Overview of the ASAPP API

The ASAPP API is Resource oriented, relying on REST principles. Our APIs accept and respond with JSON.

## Authentication

The ASAPP API uses a combination of an API Id and API Secret to authenticate requests.

```bash  theme={null}
curl -X GET 'https://api.sandbox.asapp.com/conversation/v1/conversations' \
--header 'asapp-api-id: <API KEY ID>' \
--header 'asapp-api-secret: <API TOKEN>' \
```

Learn how to find your API Id and API Secret in the [Developer quickstart](/getting-started/developers).

## Environments

The ASAPP API is available in two environments:

* **Sandbox**: Use the Sandbox environment for development and testing.
* **Production**: Use the Production environment for production use.

Use the API domain to make requests to the relevant environment.

| Environment | API Domain                                                     |
| :---------- | :------------------------------------------------------------- |
| Sandbox     | [https://api.sandbox.asapp.com](https://api.sandbox.asapp.com) |
| Production  | [https://api.asapp.com](https://api.asapp.com)                 |

## Errors

The ASAPP API uses standard HTTP status codes to indicate the success or failure of a request.

| Status Code | Description           |
| :---------- | :-------------------- |
| 200         | OK                    |
| 201         | Created               |
| 204         | No Content            |
| 400         | Bad Request           |
| 401         | Unauthorized          |
| 403         | Forbidden             |
| 404         | Not Found             |
| 429         | Too Many Requests     |
| 500         | Internal Server Error |

We also return a `code` and `message` in the response body for each error. Learn more about error codes in the [Error handling](/getting-started/developers/error-handling) section.
