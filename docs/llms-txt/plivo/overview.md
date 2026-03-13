# Source: https://plivo.com/docs/voice/xml/overview.md

# Source: https://plivo.com/docs/voice/sdk/browser/overview.md

# Source: https://plivo.com/docs/voice/concepts/overview.md

# Source: https://plivo.com/docs/voice/client/androidios/overview.md

# Source: https://plivo.com/docs/voice/api/overview.md

# Source: https://plivo.com/docs/voice-agents/sip-trunking/overview.md

# Source: https://plivo.com/docs/voice-agents/audio-streaming/overview.md

# Source: https://plivo.com/docs/voice-agents/audio-streaming/integration-guides/pipecat/overview.md

# Source: https://plivo.com/docs/sip-trunking/interconnection-guides/overview.md

# Source: https://plivo.com/docs/sip-trunking/api/overview.md

# Source: https://plivo.com/docs/programmable-api/verify/overview.md

# Source: https://plivo.com/docs/number-masking/concepts/overview.md

# Source: https://plivo.com/docs/number-masking/api/overview.md

# Source: https://plivo.com/docs/messaging/xml/overview.md

# Source: https://plivo.com/docs/messaging/concepts/overview.md

# Source: https://plivo.com/docs/messaging/api/overview.md

# Source: https://plivo.com/docs/messaging/api/10dlc/overview.md

# Source: https://plivo.com/docs/aiagent/getstarted/overview.md

# Source: https://plivo.com/docs/account/api/overview.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# API Overview

> Authentication, request format, responses, and pagination for Plivo APIs

All Plivo APIs use HTTP verbs and standard HTTP status codes. To secure requests, all APIs are served over HTTPS.

**API Endpoint**

```
https://api.plivo.com/v1/
```

<Note>
  The current version of the APIs is `v1`. Server SDKs are versioned as `latest` and `legacy`.
</Note>

***

## Authentication

All requests to Plivo API are authenticated with `BasicAuth` using your `AUTH ID` and `AUTH TOKEN`. Find your credentials on the [Plivo console](https://cx.plivo.com/home).

<CodeGroup>
  ```python Python theme={null}
  import plivo

  client = plivo.RestClient('<auth_id>', '<auth_token>')
  ```

  ```javascript Node.js theme={null}
  const plivo = require('plivo');

  const client = new plivo.Client('<auth_id>', '<auth_token>');
  ```

  ```ruby Ruby theme={null}
  require 'plivo'

  client = Plivo::RestClient.new('<auth_id>', '<auth_token>')
  ```

  ```php PHP theme={null}
  <?php
  require 'vendor/autoload.php';
  use Plivo\RestClient;

  $client = new RestClient('<auth_id>', '<auth_token>');
  ```

  ```java Java theme={null}
  import com.plivo.api.Plivo;

  Plivo.init("<auth_id>", "<auth_token>");
  ```

  ```csharp .NET theme={null}
  using Plivo;

  var api = new PlivoApi("<auth_id>", "<auth_token>");
  ```

  ```go Go theme={null}
  package main

  import "github.com/plivo/plivo-go/v7"

  func main() {
      client, _ := plivo.NewClient("<auth_id>", "<auth_token>", &plivo.ClientOptions{})
  }
  ```

  ```bash cURL theme={null}
  curl -u "<auth_id>:<auth_token>" \
      https://api.plivo.com/v1/Account/{auth_id}/
  ```
</CodeGroup>

***

## Content Type

Plivo only accepts input of type `application/json`.

* **POST requests**: Arguments must be passed as JSON with `Content-Type: application/json`
* **GET and DELETE requests**: Arguments must be passed in the query string

***

## Timeouts and Proxies

Server SDKs support specifying timeouts and proxy settings for API requests.

<CodeGroup>
  ```python Python theme={null}
  import plivo

  proxies = {
      'http': 'https://username:password@proxyurl:proxyport',
      'https': 'https://username:password@proxyurl:proxyport'
  }
  client = plivo.RestClient('<auth_id>', '<auth_token>', proxies=proxies, timeout=5)
  ```

  ```javascript Node.js theme={null}
  const plivo = require('plivo');

  let options = {
      'timeout': 5000,
      'host': 'https://proxyurl',
      'port': 'proxyport',
      auth: {
          username: 'my-user',
          password: 'my-password'
      }
  };

  const client = new plivo.Client('<auth_id>', '<auth_token>', options);
  ```

  ```ruby Ruby theme={null}
  require 'plivo'

  proxy = {
      proxy_host: "https://proxyurl",
      proxy_port: "proxyport",
      proxy_user: "username",
      proxy_pass: "password"
  }
  client = Plivo::RestClient.new('<auth_id>', '<auth_token>', proxy, timeout=5)
  ```

  ```php PHP theme={null}
  <?php
  require 'vendor/autoload.php';
  use Plivo\RestClient;

  $client = new RestClient('<auth_id>', '<auth_token>', 'https://proxyurl', 'proxyport', 'username', 'password');
  $client->client->setTimeout(5);
  ```

  ```csharp .NET theme={null}
  using Plivo;

  var api = new PlivoApi(
      "<auth_id>", "<auth_token>",
      "https://proxyurl", "proxyport", "username", "password");
  api.Client.SetTimeout(10);
  ```

  ```go Go theme={null}
  package main

  import "github.com/plivo/plivo-go/v7"

  func main() {
      client, _ := plivo.NewClient("<auth_id>", "<auth_token>", &plivo.ClientOptions{
          Timeout: 5 * time.Second,
      })
  }
  ```
</CodeGroup>

***

## Pagination

Plivo uses offset-based pagination to list resources.

| Parameter | Description                                            |
| --------- | ------------------------------------------------------ |
| `limit`   | Number of results to return. Range: 1-20. Default: 20. |
| `offset`  | Number of results to skip for pagination.              |

For example, with 100 results, `limit=10` and `offset=50` returns objects 51-60.

***

## Asynchronous Requests

All Plivo API requests can be made asynchronous. When an async call is made, Plivo returns a generic response with the `api_id`, and the actual response is sent to your callback URL.

| Parameter         | Description                                    |
| ----------------- | ---------------------------------------------- |
| `callback_url`    | URL to receive the API response.               |
| `callback_method` | HTTP method for the callback. Default: `POST`. |

```json Async Response theme={null}
{
  "message": "async api spawned",
  "api_id": "63f0761a-e0ed-11e1-8ea7-12313924e3a6"
}
```

***

## HTTP Status Codes

| Code  | Description                      |
| ----- | -------------------------------- |
| `200` | Request executed successfully    |
| `201` | Resource created                 |
| `202` | Resource changed                 |
| `204` | Resource deleted                 |
| `400` | Parameter missing or invalid     |
| `401` | Authentication failed            |
| `403` | Forbidden                        |
| `404` | Resource not found               |
| `405` | HTTP method not allowed          |
| `429` | Too many requests (rate limited) |
| `500` | Server error                     |

### Troubleshooting Common Errors

| Code  | Common Causes                                   | Solution                                                                      |
| ----- | ----------------------------------------------- | ----------------------------------------------------------------------------- |
| `400` | Missing required parameter, invalid JSON format | Check all required parameters. Verify JSON syntax                             |
| `401` | Invalid Auth ID or Auth Token                   | Verify credentials at Console → API Keys                                      |
| `403` | Account not verified, feature not enabled       | Complete account verification. Contact support                                |
| `404` | Invalid resource ID, typo in endpoint URL       | Verify the resource exists. Check endpoint spelling                           |
| `429` | Rate limit exceeded (300 requests/5 sec)        | Implement exponential backoff                                                 |
| `500` | Temporary server issue                          | Retry after a few seconds. Check [status.plivo.com](https://status.plivo.com) |

***

## Response Format

All API responses are in JSON format. Every response includes an `api_id` to uniquely identify your request.

| Field     | Description                           |
| --------- | ------------------------------------- |
| `api_id`  | Unique identifier for the request.    |
| `message` | Information about the request result. |
| `error`   | Error details if the request failed.  |

<CodeGroup>
  ```json Success theme={null}
  {
    "api_id": "97ceeb52-58b6-11e1-86da-77300b68f8bb",
    "message": "call fired",
    "request_uuid": "75b26856-8638-11e0-802c-6d99d509954e"
  }
  ```

  ```json Error theme={null}
  {
    "api_id": "97ceeb52-58b6-11e1-86da-77300b68f8bb",
    "error": "answer_url parameter is missing"
  }
  ```
</CodeGroup>
