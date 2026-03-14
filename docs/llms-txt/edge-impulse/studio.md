# Source: https://docs.edgeimpulse.com/studio.md

# Source: https://docs.edgeimpulse.com/apis/studio.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Studio API

The Edge Impulse API exposes programmatic access to most functionality in the studio. You can use the API to edit the labels of many samples at once, train models, or create new impulses. In addition, you can subscribe to events, such as when a new file was processed by the ingestion service. You authenticate with the API using an API Key or with a username/password, see [API Authentication Types](/apis/studio#api-authentication-types).

The API is available at:

```
https://studio.edgeimpulse.com/v1
```

The API is described in [OpenAPI format](https://swagger.io/specification/), which can be used to generate clients in many languages. The OpenAPI definition file is located [here](https://studio.edgeimpulse.com/openapi.yml).

## API authentication types

<table><thead><tr><th width="283">Security Scheme</th><th width="106">Type</th><th width="118">Input</th><th>Name</th></tr></thead><tbody><tr><td>ApiKeyAuthentication</td><td>apiKey</td><td>header</td><td><code>x-api-key</code></td></tr><tr><td>JWTAuthentication</td><td>apiKey</td><td>cookie</td><td><code>jwt</code></td></tr><tr><td>JWTHttpHeaderAuthentication</td><td>apiKey</td><td>header</td><td><code>x-jwt-token</code></td></tr></tbody></table>

### API key

An Edge Impulse API key can be obtained through your Edge Impulse Studio project's dashboard. At the top of the page, click on the **Keys** button to see your project's available API keys, and to generate new keys.

<Frame caption="Edge Impulse project API keys">
  <img src="https://mintcdn.com/edgeimpulse/XwnzH-Jo3nDoEg0b/.assets/images/api-keys.png?fit=max&auto=format&n=XwnzH-Jo3nDoEg0b&q=85&s=c234bd472433ae8da14253f4b7a7757f" width="1600" height="607" data-path=".assets/images/api-keys.png" />
</Frame>

### JWT token

A JWT token can be acquired via the Edge Impulse API [Get JWT token](/apis/studio/login/get-jwt-token) request with your Edge Impulse username and password.

**Example**

```bash  theme={"system"}
curl --request POST \
--url https://studio.edgeimpulse.com/v1/api-login \
--header 'content-type: application/json' \
--data-raw '{"username": "edge-user-01", "password": "reprehenderit ea"}'
```

## Test API requests

If you want to test your API requests directly from this documentation, you can use the provided widget:

<Frame caption="Test API request">
  <img src="https://mintcdn.com/edgeimpulse/XwnzH-Jo3nDoEg0b/.assets/images/api-test-request.png?fit=max&auto=format&n=XwnzH-Jo3nDoEg0b&q=85&s=d76b7a63c55a448e75eba9b2be4075a1" width="1430" height="970" data-path=".assets/images/api-test-request.png" />
</Frame>

And set your `x-api-key` or `x-jwt-token` header or your `jwt` cookie:

<Frame caption="Set authorization header">
  <img src="https://mintcdn.com/edgeimpulse/XwnzH-Jo3nDoEg0b/.assets/images/api-set-authorization.png?fit=max&auto=format&n=XwnzH-Jo3nDoEg0b&q=85&s=0f80c2e29f025a5b37465ec35e1806e1" width="1430" height="970" data-path=".assets/images/api-set-authorization.png" />
</Frame>

## Jobs

Jobs are long-running tasks that are executed asynchronously. Jobs are identified by their job ID, in the form of `job-1569583053767`, which is returned when starting a job. Subsequent job updates are published over the WebSocket API.

<Info>
  Jobs started through the API are subject to the same usage limits (such as compute time used) as through the studio UI.
</Info>

### Updates

There are two events that are published regarding jobs:

* `job-data-{jobId}` - status update on the job, e.g. progress when training a neural network. Provides a single argument: `{ data: 'string with status' }`.
* `job-finished-{jobId}` - indicator that the job finished. Provides a single argument: `{ success: true }` which indicates whether the job was executed successfully.

### Canceling a job

You can also cancel a job through the websocket by sending a `job-cancel` event. Pass in one parameter (the job ID).


Built with [Mintlify](https://mintlify.com).