# Source: https://docs.ultravox.ai/sdk-reference/introduction.md

# Source: https://docs.ultravox.ai/api-reference/introduction.md

# Ultravox REST API Overview

<Info>
  <b>Get an API Key</b>

  Using the Ultravox API requires an API key.

  You can [sign-up](https://app.ultravox.ai) for a free account that comes with 30 free minutes for creating calls.
</Info>

## Base URL

The Ultravox API is available at `https://api.ultravox.ai/api/`.

## API Keys

Ultravox API keys are 41 characters long and are made up of two alphanumeric parts separated by a period. The first part is 8 characters long and the second is 32 characters.

For example: `Zk9Ht7Lm.wX7pN9fM3kLj6tRq2bGhA8yE5cZvD4sT`

Throughout the docs we use `aBCDef.123456` for brevity.

## X-API-Key Header

When making API calls, pass your key in using the `X-API-Key` header.

<Warning>
  <b>You should never expose your API key to client code</b>

  If you *really* want to ignore this advice for a local demo, use the X-Unsafe-API-Key header instead at your own risk. It works the same way except that our server will allow it in CORS preflight requests.
</Warning>

Here's an example showing how to use the fictional API key `aBCDef.123456` to get a list of calls:

<CodeGroup>
  ```bash curl theme={null}
  curl --request GET \
  --url https://api.ultravox.ai/api/calls \
  --header 'X-API-Key: aBCDef.123456'
  ```

  ```js JavaScript theme={null}
  fetch('https://api.ultravox.ai/api/calls', {
    method: 'GET',
    headers: {
      'X-API-Key': 'aBCDef.123456'
    }
  })
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error('Error:', error));
  ```
</CodeGroup>

## Rate Limits

The Ultravox API includes safeguards to help maximize stability for all customers. Too many API requests can trigger an error with status code `429`. See [Scaling & Call Concurrency](/gettingstarted/concurrency) for more information on `429` errors and how to properly handle them.

### API Limits

We restrict the number of total API requests per second. This restriction applies to all API endpoints that are part of `https://api.ultravox.ai/api/`.

We restrict at the account and API key level as follows:

| Level          | API Requests per Second |
| -------------- | ----------------------- |
| <b>Account</b> | 500                     |
| <b>API Key</b> | 200                     |

### Call Creation Limits

In addition to the overall [API limits](#api-limits) above, we place additional restrictions on how quickly accounts can create calls in the system.

| Plan Type    | Per Second | Per Minute |
| ------------ | ---------- | ---------- |
| Free / PAYGO | 5          | 30         |
| Pro          | 10         | 120        |
| Scale        | 30         | 360        |

> *Call creation is limited by whichever threshold is reached first (per second or per minute).*

### Call Concurrency Limits

The number of concurrent calls allowed depends on your plan.

| Plan Type    | Concurrency Cap | Priority Access |
| ------------ | --------------- | --------------- |
| Free / PAYGO | 5 calls         | ❌               |
| Pro          | No hard cap\*   | ❌               |
| Scale        | No hard cap\*   | ✅ Up to 100     |

> \*Still subject to infra limits under extreme load.

See [Scaling & Call Concurrency](/gettingstarted/concurrency) for more details on how call concurrency works in Ultravox Realtime.

## Playground

If you want to quickly experiment with prompts and voices, the fastest way to do that is in the [Ultravox Dashboard](https://app.ultravox.ai/playground).

You can also paste in an Ultravox API key throughout the API reference (look for "Authorization" and paste your key where it asks for `X-API-Key`) and test the REST API endpoints.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.ultravox.ai/llms.txt