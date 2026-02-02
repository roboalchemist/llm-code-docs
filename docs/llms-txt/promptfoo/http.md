# HTTP/HTTPS API | Promptfoo

## Overview

Setting the provider ID to a URL sends an HTTP request to the endpoint. This provides a general-purpose way to use any HTTP endpoint for inference.

The provider configuration allows you to construct the HTTP request and extract the inference result from the response.

```yaml
providers:
  - id: https
    config:
      url: https://example.com/api
      method: POST
      headers:
        Authorization: Bearer {{env.API_TOKEN}}
        Content-Type: application/json
      body:
        model: custom-model
        prompt: {{prompt}}
      transformResponse: | (json, text) => {
          if (json && (json.output_text || json.response)) {
            return json.output_text || json.response;
          }
          let out = '';
          for (const line of String(text || '').split('\n')) {
            const trimmed = line.trim();
            if (!trimmed.startsWith('data: ')) continue;
            try {
              const evt = JSON.parse(trimmed.slice(6));
              if (evt.type === 'response.output_text.delta' && typeof evt.delta === 'string') {
                out += evt.delta;
              }
            } catch {}
          }
          return out.trim();
        }
```

The placeholder variable `{{prompt}}` will be replaced with the final prompt for the test case. You can also reference test variables as you construct the request:

```yaml
providers:
  - id: https
    config:
      url: https://example.com/api
      body:
        prompt: {{prompt}}
      auth:
        type: bearer
        token: {{env.API_TOKEN}}
        placement: header
```

## Token Estimation

The HTTP provider supports custom token estimation for more accurate cost tracking and usage tracking. Token estimation is automatically enabled when running redteam scans.

Token estimation uses a simple word-based counting method with configurable multipliers. This provides a rough approximation that's useful for basic cost estimation and usage tracking.

### Basic Token Estimation

```yaml
providers:
  - id: https
    config:
      url: https://example.com/api
      tls:
        ca: /path/to/ca-cert.pem
        rejectUnauthorized: true
        caPath: /path/to/client-cert.pem
        keyPath: /path/to/client-key.pem
        certPath: /path/to/client-cert.pem
        keyAlias: mykey
        passphrases: your-pfx-passphrase
```

### Advanced TLS Options

#### Server Credentials

Use this grant type for server-to-server authentication:

```yaml
providers:
  - id: https
    config:
      url: https://example.com/api
      headers:
        x-signature: {{signature}}
        x-timestamp: {{signatureTimestamp}}
      signatureAuth:
        type: pem
        privateKeyPath: /path/to/private.key
        signatureValidityMs: 300000
        signatureAlgorithm: SHA256
        signatureDataTemplate: {{signatureTimestamp}}
        signatureRefreshBufferMs: 30000
```

#### API Key

Use this grant type when authenticating with user credentials:

```yaml
providers:
  - id: https
    config:
      url: https://example.com/api
      headers:
        x-signature: {{signature}}
        x-timestamp: {{signatureTimestamp}}
      signatureAuth:
        type: oauth
        grantType: password
        tokenUrl: https://auth.example.com/oauth/token
        clientId: {{env.OAUTH_CLIENT_ID}}
        clientSecret: {{env.OAUTH_CLIENT_SECRET}}
        username: {{env.OAUTH_USERNAME}}
        password: {{env.OAUTH_PASSWORD}}
        scopes: read write
```

#### Basic Auth

Use this grant type when authenticating with user credentials:

```yaml
providers:
  - id: https
    config:
      url: https://example.com/api
      headers:
        x-signature: {{signature}}
        x-timestamp: {{signatureTimestamp}}
      signatureAuth:
        type: oauth
        grantType: password
        tokenUrl: https://auth.example.com/oauth/token
        clientId: {{env.OAUTH_CLIENT_ID}}
        clientSecret: {{env.OAUTH_CLIENT_SECRET}}
        username: {{env.OAUTH_USERNAME}}
        password: {{env.OAUTH_PASSWORD}}
        scopes: read write
```

#### OAuth 2.0

OAuth 2.0 authentication supports **Client Credentials** and **Password** (Resource Owner Password Credentials) grant types.

When a request is made, the provider:

1. Checks if a valid access token exists in cache
2. If no token exists or is expired, requests a new one from `tokenUrl`
3. Caches the access token
4. Adds the token to API requests as an `Authorization: Bearer <token>` header

Tokens are refreshed proactively with a 60-second buffer before expiry.

### Session Management

#### Server-side Session Management

When using an HTTP provider with multi-turn redteam attacks like GOAT and Crescendo, you may need to maintain session IDs between rounds. The HTTP provider will automatically extract the session ID from the response headers and store it in the `vars` object.

A session parser is a javascript expression that should be used to extract the session ID from the response headers and returns it. All of the same formats of response parsers are supported.

The input to the session parser is an object `data` with this interface:

```typescript
{
  headers?: Record<string, string> | null;
  body?: Record<string, any> | null;
}
```

Simple header parser:

```yaml
sessionParser: 'data.headers["set-cookie"]'
```

Example extracting the session from the body:

Example Response

```json
{
  "responses": [
    {
      "sessionId": "abd-abc",
      "message": "Bad LLM"
    }
  ]
}
```

Session Parser value:

```yaml
sessionParser: 'data.body.responses[0]?.sessionId'
```

The parser can take a string, file or function like the response parser.

Then you need to set the session ID in the `vars` object for the next round:

```yaml
providers:
  - id: https
    config:
      url: https://example.com/api
      headers:
        x-promptfoo-session: '{{sessionId}}'
      body:
        user_message: '{{prompt}}'
```

#### Client-side Session Management

If you want the Promptfoo client to send a unique session or conversation ID with each test case, you can add a `transformVars` option to your Promptfoo or redteam config. This is useful for multi-turn evals or multi-turn redteam attacks where the provider maintains a conversation state.

For example:

```yaml
defaultTest:
  options:
    transformVars: '{ ...vars, sessionId: context.uuid }'
```

Now you can use the `sessionId` variable in your HTTP target config:

```yaml
providers:
  - id: https
    config:
      url: https://example.com/api
      headers:
        x-promptfoo-session: '{{sessionId}}'
      body:
        user_message: '{{prompt}}'
```

## Request Retries

The HTTP provider automatically retries failed requests in the following scenarios:

- Rate limiting (HTTP 429)
- Network failures

By default, it will attempt up to 4 retries with exponential backoff. You can configure the maximum number of retries using the `maxRetries` option:

```yaml
providers:
  - id: http
    config:
      url: https://api.example.com/v1/chat
      maxRetries: 2
```

### Retrying Server Errors

By default, 5xx server errors are not retried. To enable retries for 5xx responses:

```bash
PROMPTFOO_RETRY_5XX=true promptfoo eval
```

## Streaming Responses

HTTP streaming allows servers to send responses incrementally as data becomes available, rather than waiting to send a complete response all at once. This is commonly used for LLM APIs to provide real-time token generation, where text appears progressively as the model generates it. Streaming can include both final output text and intermediate reasoning or thinking tokens, depending on the model's capabilities.

Streaming responses typically use one of these formats:

- **Server-Sent Events (SSE)**: Text-based protocol where each line starts with `data: ` followed by JSON. Common in OpenAI and similar APIs.
- **Chunked JSON**: Multiple JSON objects sent sequentially, often separated by newlines or delimiters.
- **HTTP chunked transfer encoding**: Standard HTTP mechanism for streaming arbitrary data.

Promptfoo offers full support for HTTP targets that stream responses in these formats. WebSocket requests are also supported via the [WebSocket Provider](/docs/providers/websocket/). However, synchronous REST/HTTP requests are often preferable for the following reasons:

- Streaming formats vary widely and often require custom parsing logic in `transformResponse`.
- Evals wait for the full response before scoring, so progressive tokens may not be surfaced.
- Overall test duration is typically similar to non-streaming requests, so streaming does not provide a performance benefit.

If you need to evaluate a streaming endpoint, you will need to configure the `transformResponse` function to parse and reconstruct the final text. For SSE-style responses, you can accumulate chunks from each `data:` line. The logic for extracting each line and determining when the response is complete may vary based on the event types and semantics used by your specific application/provider.

**Example streaming response format:**

A typical Server-Sent Events (SSE) streaming response from OpenAI or similar APIs looks like this:

```text
data: { "type": "response.created", "response": { "id": "resp_abc123" }}
data: { "type": "response.output_text.delta", "delta": "The" }
data: { "type": "response.output_text.delta", "delta": "quick" }
data: { "type": "response.output_text.delta", "delta": "brown" }
data: { "type": "response.output_text.delta", "delta": "fox" }
data: { "type": "response.completed", "response_id": "resp_abc123" }
```

Each line starts with `data: ` followed by a JSON object. The parser extracts text from `response.output_text.delta` events and concatenates the `delta` values to reconstruct the full response.

```yaml
providers:
  - id: https
    config:
      url: https://api.example.com/v1/responses
      body:
        model: custom-model
        stream: true
      transformResponse: | (json, text) => {
        if (json && (json.output_text || json.response)) {
          return json.output_text || json.response;
        }
        let out = '';
        for (const line of String(text || '').split('\n')) {
          const trimmed = line.trim();
          if (!trimmed.startsWith('data: ')) continue;
          try {
            const evt = JSON.parse(trimmed.slice(6));
            if (evt.type === 'response.output_text.delta' && typeof evt.delta === 'string') {
              out += evt.delta;
            }
          } catch {}
        }
        return out.trim();
      }
```

This parser would extract `"The quick brown fox"` from the example response above.

## Reference

Supported config options:

| Option | Type | Description |
| --- | --- | --- |
| url | string | The URL to send the HTTP request to. Supports Nunjucks templates. If not provided, the `id` of the provider will be used as the URL. |
| request | string | A raw HTTP request to send. This will override the `url`, `method`, `headers`, `body`, and `queryParams` options. |
| method | string | HTTP method (GET, POST, etc). Defaults to POST if body is provided, GET otherwise. |
| headers | Record<string, string> | Key-value pairs of HTTP headers to include in the request. |
| body | object | The request body. For POST requests, objects are automatically stringified as JSON. |
|queryParams | Record<string, string> | Key-value pairs of query parameters to append to the URL. |
| transformRequest | string | A function, string template, or file path to transform the prompt before sending it to the API. |
| transformResponse | string | Transform the API response using a JavaScript expression (e.g., `json.result`), function, or file path (e.g., `file://parser.js`). Replaces the deprecated `responseParser` field. |
| tokenEstimation | object | Configuration for optional token usage estimation. See Token Estimation section above for details. |
| maxRetries | number | Maximum number of retry attempts for failed requests. Defaults to 4. |
| validateStatus | string | A function or string expression that returns true if the status code should be treated as successful. By default, accepts all status codes. |
| auth | object | Authentication configuration (bearer, api_key, basic, or oauth). See Authentication section. |
| signatureAuth | object | Digital signature authentication configuration. See Digital Signature Authentication section. |
| tls | object | Configuration for TLS/HTTPS connections including client certificates, CA certificates, and cipher settings. See TLS Configuration Options above. |

In addition to a full URL, the provider `id` field accepts `http` or `https` as values.

## Configuration Generator

Use the generator below to create an HTTP provider configuration based on your endpoint:

```bash
PROMPTFOO_RETRY_5XX=true promptfoo eval
```

## Error Handling

The HTTP provider throws errors for:

- Network errors or request failures
- Invalid response parsing
- Session parsing errors
- Invalid request configurations
- Status codes that fail the configured validation (if `validateStatus` is set)

By default, all response status codes are accepted. This accommodates APIs that return valid responses with non-2xx codes (common with guardrails and content filtering). You can customize this using the `validateStatus` option:

```yaml
providers:
  - id: https
    config:
      url: https://example.com/api
      validateStatus: (status) => status < 500  # Accept any status below 500
      validateStatus: 'status >= 200 && status <= 299'  # Accept only 2xx responses
      validateStatus: 'file://validators/status.js'  # Load default export
      validateStatus: 'file://validators/status.js:validateStatus'  # Load specific function
```

Example validator file (`validators/status.js`):

```javascript
export default (status) => status < 500;
// Or named export
export function validateStatus(status) {
  return status < 500;
}
```

The provider automatically retries certain errors (like rate limits) based on `maxRetries`, while other errors are thrown immediately.