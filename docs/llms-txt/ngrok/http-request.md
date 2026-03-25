# Source: https://ngrok.com/docs/traffic-policy/actions/http-request.md

> ## Documentation Index
> Fetch the complete documentation index at: https://ngrok.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# HTTP Request Action

> The HTTP Request action performs an outbound HTTP request to a target URL.

export const ConfigChildren = ({children}) => {
  return <Accordion title="Show Child Properties">
      {children}
    </Accordion>;
};

export const ConfigField = ({title, type, cel = false, defaultValue = false, required = false, children}) => {
  const id = `config-${title.replace(/\.|\s|\*/g, "_")}`;
  return <div className="field pt-2.5 pb-5 my-2.5 border-gray-50 dark:border-gray-800/50 border-b" style={{
    scrollMarginTop: '120px'
  }} id={id}>
      <div className="flex font-mono group/param-head param-head break-all relative">
        <div className="flex-1 flex content-start py-0.5 mr-5">
          <div className="flex items-center flex-wrap gap-2">
            <div class="absolute -top-1.5">
              <a href={`#${id}`} className="-ml-10 flex items-center opacity-0 border-0 group-hover/param-head:opacity-100 py-2 [.expandable-content_&]:-ml-[2.1rem]" aria-label="Navigate to header">
                ​<div className="w-6 h-6 rounded-md flex items-center justify-center shadow-sm text-gray-400 dark:text-white/50 dark:bg-background-dark dark:brightness-[1.35] dark:ring-1 dark:hover::rightness-150 bg-white ring-1 ring-gray-400/30 dark:ring-gray-700/25 hover:ring-gray-400/60 dark:hover:ring-white/20">
                  <svg xmlns="http://www.w3.org/2000/svg" fill="gray" height="12px" viewBox="0 0 576 512"><path d="M0 256C0 167.6 71.6 96 160 96h72c13.3 0 24 10.7 24 24s-10.7 24-24 24H160C98.1 144 48 194.1 48 256s50.1 112 112 112h72c13.3 0 24 10.7 24 24s-10.7 24-24 24H160C71.6 416 0 344.4 0 256zm576 0c0 88.4-71.6 160-160 160H344c-13.3 0-24-10.7-24-24s10.7-24 24-24h72c61.9 0 112-50.1 112-112s-50.1-112-112-112H344c-13.3 0-24-10.7-24-24s10.7-24 24-24h72c88.4 0 160 71.6 160 160zM184 232H392c13.3 0 24 10.7 24 24s-10.7 24-24 24H184c-13.3 0-24-10.7-24-24s10.7-24 24-24z"></path></svg>
                </div>
              </a>
            </div>
            <div className="font-semibold text-primary dark:text-primary-light overflow-wrap-anywhere">{title}</div>
            <div className="inline items-center gap-2 text-xs font-medium [&_div]:inline [&_div]:mr-2 [&_div]:leading-5 [&_a]:inline [&_a]:mr-2 [&_a]:leading-5">
              {type && <div className="flex items-center px-2 py-0.5 rounded-md bg-gray-100/50 dark:bg-white/5 break-all">
                <span className="text-gray-600 dark:text-gray-200 !font-medium">{type}</span>
              </div>}
              {defaultValue && <div className="flex items-center px-2 py-0.5 rounded-md bg-gray-100/50 dark:bg-white/5 break-all">
                  <span class="text-gray-400 dark:text-gray-500">default:</span>
                  <span className="text-gray-600 dark:text-gray-200 !font-medium">{defaultValue}</span>
                </div>}
              {required && <div className="px-2 py-0.5 rounded-md bg-red-100/50 dark:bg-red-400/10 whitespace-nowrap">
                <span className="text-red-600 dark:text-red-300 !font-medium">Required</span>
              </div>}
              {cel && <a className="px-2 py-0.5 rounded-md !border-none bg-blue-100/50 dark:bg-blue-400/10 whitespace-nowrap" href="/traffic-policy/concepts/cel-interpolation">
                <span className="text-blue-600 dark:text-blue-300 !font-medium">Supports CEL</span>
              </a>}
            </div>
          </div>
        </div>
      </div>
      <div className="mt-4 prose-sm prose-gray dark:prose-invert [&_.prose>p:first-child]:mt-0 [&_.prose>p:last-child]:mb-0">
        {children}
      </div>
    </div>;
};

export const YouTubeEmbed = ({className, title, videoId, ...props}) => {
  return <div className={`relative aspect-video mb-3 ${className}`} {...props}>
      <iframe src={`https://www.youtube.com/embed/${videoId}`} allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen className="absolute inset-0 w-full h-full" title={title} />
    </div>;
};

The HTTP Request Traffic Policy action performs an outbound HTTP request to a target URL. You can use it to integrate with external services through internal endpoints or—if enabled—with external APIs.

<Note>
  External requests are supported but disabled by default. [Contact ngrok support](https://ngrok.com/support) to enable external access.
</Note>

<YouTubeEmbed videoId="1VYtIOJsgic" title="Learn about ngrok's http-request action" />

## Configuration reference

The [Traffic Policy](/traffic-policy/) configuration
reference for this action.

### Supported phases

`on_http_request`, `on_http_response`

### Type

`http-request`

### Configuration fields

<ConfigField title="url" type="string" required={true} cel={true}>
  The destination URL for the HTTP request.
</ConfigField>

<ConfigField title="method" type="enum">
  The HTTP method to use for the request.

  <ConfigEnum>
    <ConfigEnumOption>`GET` (default)</ConfigEnumOption>
    <ConfigEnumOption>`PUT`</ConfigEnumOption>
    <ConfigEnumOption>`POST`</ConfigEnumOption>
    <ConfigEnumOption>`PATCH`</ConfigEnumOption>
    <ConfigEnumOption>`DELETE`</ConfigEnumOption>
    <ConfigEnumOption>`OPTIONS`</ConfigEnumOption>
  </ConfigEnum>
</ConfigField>

<ConfigField title="query_params" type="list of objects" cel={true}>
  A list of query parameters to append to the URL. Each item is an object with the following structure:

  ```yaml  theme={null}
  - key: "parameter_name"
    value: "parameter_value"
  ```

  Maximum: `32` entries. Key max length: `128` chars. Value max length: `8192` chars.
</ConfigField>

<ConfigField title="headers" type="object" cel={true}>
  A map of HTTP headers to include in the request. Keys are header names and values are header values.

  Maximum: `10` entries.
</ConfigField>

<ConfigField title="body" type="string" cel={true}>
  The body of the HTTP request. Supported on methods like `POST`, `PUT`, or `PATCH`.
</ConfigField>

<ConfigField title="max_redirects" type="int" defaultValue="10">
  The maximum number of HTTP redirects to follow.

  The minimum allowed is `0`. The maximum allowed is `100`.
</ConfigField>

<ConfigField title="timeout" type="duration" defaultValue="3s">
  The maximum duration as a duration string to wait for the entire request (including retries and redirects).

  The minimum allowed is `1s`. The maximum allowed is `30s`.
</ConfigField>

<ConfigField title="retry_condition" type="string" cel={true} defaultValue="false">
  A CEL expression evaluated after each failed attempt. If `true`, the request is retried (up to `3` times).

  <ConfigEnum>
    <ConfigEnumOption>`attempts` (`int`): Total number of attempts so far</ConfigEnumOption>
    <ConfigEnumOption>`last_attempt.req`: The last request object</ConfigEnumOption>
    <ConfigEnumOption>`last_attempt.res`: The last response object (if any)</ConfigEnumOption>
    <ConfigEnumOption>`last_attempt.error`: The error string (if any)</ConfigEnumOption>
  </ConfigEnum>
</ConfigField>

<ConfigField title="on_error" type="enum">
  Determines how to proceed if the HTTP request fails.

  <ConfigEnum>
    <ConfigEnumOption>`continue` (default) – Proceed with remaining actions</ConfigEnumOption>
    <ConfigEnumOption>`halt` – Stop processing the policy</ConfigEnumOption>
  </ConfigEnum>
</ConfigField>

## Behavior

The `http-request` action issues an outbound HTTP request during either the `on_http_request` or `on_http_response` phase of policy execution. It can include dynamic headers, query parameters, and a request body.

Only specific HTTP methods are supported: `GET`, `POST`, `PUT`, `PATCH`, `DELETE`, and `OPTIONS`. If no method is specified, `GET` is used by default.

### Internal endpoint behavior

By default, the `http-request` action only supports requests to internal ngrok endpoints. Requests to internal endpoints (those with `.internal` domains) are treated differently from public (or external) requests, these requests must resolve to an internal ngrok endpoint running on your account.

These requests also use a direct connection over ngrok's control plane and do not rely on the public internet. If the request targets an internal Agent Endpoint (for example, your self-hosted ngrok agent), it will exit the control plane and traverse the public internet to reach your agent running locally.

### Retry logic

You can use a condition to automatically retry failed requests. This is useful for handling transient errors, like a `500` response. The condition is written using an expression language and has access to:

* `attempts`: number of attempts so far
* `last_attempt.req`: the most recent request
* `last_attempt.res`: the most recent response
* `last_attempt.error`: any error that occurred

```js  theme={null}
last_attempt.res.statusCode == 500
```

The request will retry up to **3 times**.

### Timeout behavior

The `timeout` setting defines the **maximum total time** allowed for the entire `http-request` action, including **all** retry attempts. This prevents long-running or stalled requests from delaying policy evaluation.

The default timeout is `3s`. You can configure any duration between **1 second** and **30 seconds** using standard duration formats like `5s` or `10s`.

#### Timeout error handling

Whether a timeout causes the policy to fail or continue depends on the `on_error` setting:

* `halt` will treat the timeout as a hard failure.
* `continue` will move forward even if the request timed out.

### Loop protection

To prevent endless loops between services, ngrok tracks internal hops. If the same request loops more than 3 times internally, it will be stopped automatically.

### Redirect behavior

By default, the `http-request` action does not follow HTTP redirects. You can enable redirect handling by setting the `max_redirects` field. The allowed range is `0` to `5`. By default it is set to `0`.

If the number of redirects exceeds `max_redirects`, the action fails. Redirect handling only applies to `3xx` responses from the target server.

### Response body size limits

The response body returned by the `http-request` action is limited to **256 KB**. If the body size exceeds this limit, the action fails and returns a `response size exceeded` error.

This limit applies to the decoded body after any decompression and before retries are evaluated.

Each retry is also subject to the **256 KB** response size limit. If the response body exceeds this limit, the attempt fails and the error is included in the `retry_condition` evaluation.

### Error handling

Set `on_error` to control what happens if the request fails:

* `continue`: Policy continues even if the request fails.
* `halt`: Policy stops immediately on failure.

This gives you control over how critical the request is to your policy logic.

### Automatically injected headers

ngrok automatically injects some headers into your request to help with debugging, tracing, and abuse:

| Header               | Purpose                                      |
| -------------------- | -------------------------------------------- |
| `Ngrok-Report-Abuse` | Static URL for reporting abuse               |
| `Ngrok-Req-Type`     | Always set to `http-request`                 |
| `Ngrok-Req-Id`       | Unique request identifier                    |
| `X-Forwarded-For`    | Original client IP address                   |
| `User-Agent`         | Identifies the request as from `ngrok/cloud` |

### CEL interpolation

Certain fields in the `http-request` action support CEL (Common Expression Language) interpolation, allowing dynamic values based on the request context.

The following fields support CEL expressions:

* `url`
* `headers` (values only)
* `query_params` (values only)
* `body`

Expressions must be wrapped in `${...}` and are evaluated at runtime using the current request data.

### Non-terminating action

This is a **Non-terminating action**. It does not return a response, and will allow Traffic Policy processing to continue to the next Action in the chain. All **Cloud Endpoint** Traffic Policies must end with a terminating action. This requirement does not apply to **Agent Endpoints**.

## Examples

### Make a GET request

Performs a simple GET request to an internal endpoint.

<CodeGroup>
  ```yaml policy.yml theme={null}
  on_http_request:
    - name: BasicInternalRequest
      actions:
        - type: http-request
          config:
            url: https://upstream-service.internal/ping
  ```

  ```json policy.json theme={null}
  {
    "on_http_request": [
      {
        "name": "BasicInternalRequest",
        "actions": [
          {
            "type": "http-request",
            "config": {
              "url": "https://upstream-service.internal/ping"
            }
          }
        ]
      }
    ]
  }
  ```
</CodeGroup>

#### Send query parameters

This example sends a GET request with custom query parameters to an internal endpoint.

To simulate this behavior, use [httpbin.org/get](https://httpbin.org/get), which echoes query parameters in the response.

##### Start an internal Agent endpoint

```bash  theme={null}
ngrok http https://httpbin.org --host-header rewrite --url https://httpbin.internal
```

<CodeGroup>
  ```yaml policy.yml {7-11} theme={null}
  on_http_request:
    - name: QueryParamsExample
      actions:
        - type: http-request
          config:
            url: https://httpbin.internal/get
            query_params:
              - key: trace
                value: 'true'
              - key: user
                value: req.headers["x-user-id"]
  ```

  ```json policy.json {10-19} theme={null}
  {
    "on_http_request": [
      {
        "name": "QueryParamsExample",
        "actions": [
          {
            "type": "http-request",
            "config": {
              "url": "https://httpbin.internal/get",
              "query_params": [
                {
                  "key": "trace",
                  "value": "true"
                },
                {
                  "key": "user",
                  "value": "req.headers[\"x-user-id\"]"
                }
              ]
            }
          }
        ]
      }
    ]
  }
  ```
</CodeGroup>

### Make a POST request

This example sends a POST request to an internal endpoint with a custom JSON body and headers.

To simulate this behavior, use [httpbin.org/post](https://httpbin.org/post) behind an internal `.internal` endpoint.

#### Start an Internal Agent Endpoint

```bash  theme={null}
ngrok http https://httpbin.org --host-header rewrite --url https://httpbin.internal
```

#### Example

<CodeGroup>
  ```yaml policy.yml theme={null}
  on_http_request:
    - name: PostWithBody
      actions:
        - type: http-request
          config:
            url: https://httpbin.internal/post
            method: POST
            headers:
              content-type: application/json
              x-custom-header: abc123
            body: '{ "user": "${req.headers[\"x-user-id\"]}" }'
  ```

  ```json policy.json theme={null}
  {
    "on_http_request": [
      {
        "name": "PostWithBody",
        "actions": [
          {
            "type": "http-request",
            "config": {
              "url": "https://httpbin.internal/post",
              "method": "POST",
              "headers": {
                "content-type": "application/json",
                "x-custom-header": "abc123"
              },
              "body": "{ \"user\": \"${req.headers[\\\"x-user-id\\\"]}\" }"
            }
          }
        ]
      }
    ]
  }
  ```
</CodeGroup>

### Follow redirects

This example demonstrates how to follow up to 2 redirects using the `http-request` action.

To simulate this behavior, use [httpbin.org/redirect](https://httpbin.org/redirect) behind an internal `.internal` endpoint.

#### Start an Internal Agent Endpoint

Run the following command to expose `https://httpbin.internal` as a simulated internal service:

```bash  theme={null}
ngrok http https://httpbin.org --host-header rewrite --url https://httpbin.internal
```

#### Example

<CodeGroup>
  ```yaml policy.yml {8} theme={null}
  on_http_request:
    - name: FollowRedirects
      actions:
        - type: http-request
          config:
            url: https://httpbin.internal/redirect/2
            method: GET
            max_redirects: 2
  ```

  ```json policy.json {11} theme={null}
  {
    "on_http_request": [
      {
        "name": "FollowRedirects",
        "actions": [
          {
            "type": "http-request",
            "config": {
              "url": "https://httpbin.internal/redirect/2",
              "method": "GET",
              "max_redirects": 2
            }
          }
        ]
      }
    ]
  }
  ```
</CodeGroup>

## Action result variables

The following variables are made available for use in subsequent expressions and
CEL interpolations after the action has run. Variable values will only apply
to the last action execution, results are not concatenated.

<ConfigField title="actions.ngrok.http_request.error.code" type="string">
  The ngrok error code for an error that occurred during the invocation of an action.
</ConfigField>

<ConfigField title="actions.ngrok.http_request.error.message" type="string">
  The message for an error that occurred during the invocation of an action.
</ConfigField>

<ConfigField title="actions.ngrok.http_request.attempts" type="array of objects">
  A list of HTTP responses for each request attempt.

  <Expandable label="children variables">
    <ConfigField title="attempts[i].resolved_ip" type="string">
      The IP address of the host returning the response.
    </ConfigField>

    <ConfigField title="attempts[i].response_header" type="object">
      A map of HTTP response headers.
    </ConfigField>

    <ConfigField title="attempts[i].response_status_code" type="int">
      The HTTP Status code for the response attempt.
    </ConfigField>

    <ConfigField title="attempts[i].response_time_ms" type="string">
      Time it took to receive the response.
    </ConfigField>
  </Expandable>
</ConfigField>

<ConfigField title="actions.ngrok.http_request.req" type="object">
  The HTTP request.

  <Expandable label="children variables">
    <ConfigField title="req.method" type="string">
      The HTTP method of the request.
    </ConfigField>

    <ConfigField title="req.header" type="object">
      A map of HTTP request headers.
    </ConfigField>

    <ConfigField title="req.url" type="string">
      The request url.
    </ConfigField>

    <ConfigField title="req.body" type="string">
      The request body.
    </ConfigField>
  </Expandable>
</ConfigField>

<ConfigField title="actions.ngrok.http_request.res" type="object">
  The last attempted HTTP response. Unlike `actions.ngrok.attempts[i]` this variable also contains the response body.

  <Expandable label="children variables">
    <ConfigField title="res.resolved_ip" type="string">
      The IP address of the host returning the response.
    </ConfigField>

    <ConfigField title="res.header" type="object">
      A map of HTTP response headers.
    </ConfigField>

    <ConfigField title="res.status_code" type="int">
      The HTTP Status code for the response.
    </ConfigField>

    <ConfigField title="res.time_ms" type="string">
      Time it took to receive the response.
    </ConfigField>

    <ConfigField title="res.body" type="string">
      The response body
    </ConfigField>
  </Expandable>
</ConfigField>


Built with [Mintlify](https://mintlify.com).