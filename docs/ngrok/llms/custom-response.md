# Source: https://ngrok.com/docs/traffic-policy/actions/custom-response.md

> ## Documentation Index
> Fetch the complete documentation index at: https://ngrok.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Custom Response Action

> Return a hard-coded response back to the client that made a request to your endpoint.

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

The **Custom Response** Traffic Policy action enables you to return a hard-coded response back to the client that made a request to your endpoint.

## Configuration reference

The [Traffic Policy](/traffic-policy/) configuration
reference for this action.

### Supported phases

`on_http_request`, `on_http_response`

### Type

`custom-response`

### Configuration fields

<ConfigField title="status_code" type="integer" defaultValue="200">
  <p>Status code of the custom response being sent back.</p>
</ConfigField>

<ConfigField title="body" type="string" cel={true}>
  <p>Body of the custom response being sent back.</p>
</ConfigField>

<ConfigField title="headers" type="object" cel={true}>
  <p>
    Map of key-value headers of the custom response to be sent back. If
    `content-type` is not included in `headers`, this action will attempt to
    infer the correct `content-type`. Maximum properties `10`.
  </p>
</ConfigField>

## Behavior

If this action is executed, no subsequent actions in your Traffic Policy will be executed.

### `on_http_request` usage

When used during the `on_http_request` phase, this action bypasses the upstream server and immediately returns the configured response to the caller.
Keep in mind that because this action bypasses the upstream server, request bodies will not be forwarded and will not be visible within the ngrok [Traffic Inspector](/obs/traffic-inspection/).

<Tip>
  When this policy is executed in the `on_http_request` phase, actions defined in the `on_http_response` phase will still be executed.
</Tip>

### `on_http_response` usage

When used during the `on_http_response`, this action overwrites the response from the upstream server with the configured response.

### Inferring content-type

If the `content-type` header is not explicitly specified in `headers`, this action will attempt to infer the correct `content-type` based on the provided content.

### Terminating action

This is a **terminating action**. It will return a response and cause Traffic Policy processing to end without executing any further Actions.

<Warning>
  If this action is executed in the [on\_http\_request phase](#on_http_request-usage), the Traffic Policy will not terminate, but will continue to the [on\_http\_response phase](#on_http_response-usage), where all actions in that change will be executed normally.
</Warning>

## Examples

### Custom HTML maintenance page

The following [Traffic Policy](/traffic-policy/)
configuration demonstrates how to use the `custom-response` action to return a
custom HTML maintenance page back for all requests to your endpoint.

#### Example Traffic Policy document

<CodeGroup>
  ```yaml policy.yml theme={null}
  on_http_request:
    - actions:
        - type: custom-response
          config:
            status_code: 503
            body: <html><body><h1>Service Unavailable</h1><p>Our servers are currently down for maintenance. Please check back later.</p></body></html>
            headers:
              content-type: text/html
  ```

  ```json policy.json theme={null}
  {
    "on_http_request": [
      {
        "actions": [
          {
            "type": "custom-response",
            "config": {
              "status_code": 503,
              "body": "<html><body><h1>Service Unavailable</h1><p>Our servers are currently down for maintenance. Please check back later.</p></body></html>",
              "headers": {
                "content-type": "text/html"
              }
            }
          }
        ]
      }
    ]
  }
  ```
</CodeGroup>

#### Example request

```bash  theme={null}
$ curl -i https://example.ngrok.app/dashboard
```

```http  theme={null}
HTTP/2 503
content-type: text/html

<html>
  <body>
    <h1>Service Unavailable</h1>
    <p>Our servers are currently down for maintenance. Please check back later.</p>
  </body>
</html>
```

In this example, when a request is made to any page on your endpoint, ngrok
returns back the custom HTML maintenance page.

This setup is useful for when you want to temporarily disable your endpoint.

### Custom response for internal endpoint downtime

The following [Traffic Policy](/traffic-policy/)
configuration demonstrates how to use the `custom-response` action to redirect to a URL if an internal endpoint is returning an error.

#### Example Traffic Policy document

<CodeGroup>
  ```yaml policy.yml {3-6} theme={null}
  on_http_request:
    - actions:
        - type: forward-internal
          config:
            url: https://endpoint-1.internal
            on_error: continue
        - type: custom-response
          config:
            status_code: 302
            headers:
              location: https://www.example.com
  ```

  ```json policy.json {5-11} theme={null}
  {
    "on_http_request": [
      {
        "actions": [
          {
            "type": "forward-internal",
            "config": {
              "url": "https://endpoint-1.internal",
              "on_error": "continue"
            }
          },
          {
            "type": "custom-response",
            "config": {
              "status_code": 302,
              "headers": {
                "location": "https://www.example.com"
              }
            }
          }
        ]
      }
    ]
  }
  ```
</CodeGroup>

### Custom JSON API response with CEL interpolation

The following [Traffic Policy](/traffic-policy/)
configuration demonstrates how to use the `custom-response` action to return a
JSON response with CEL Interpolation for the connection start time.

#### Example Traffic Policy document

<CodeGroup>
  ```yaml policy.yml {7} theme={null}
  on_http_request:
    - expressions:
        - req.url.path == '/api/example'
      actions:
        - type: custom-response
          config:
            body: '{"connection-start":"${conn.ts.start}"}'
            headers:
              content-type: application/json
  ```

  ```json policy.json {11} theme={null}
  {
    "on_http_request": [
      {
        "expressions": [
          "req.url.path == '/api/example'"
        ],
        "actions": [
          {
            "type": "custom-response",
            "config": {
              "body": "{\"connection-start\":\"${conn.ts.start}\"}",
              "headers": {
                "content-type": "application/json"
              }
            }
          }
        ]
      }
    ]
  }
  ```
</CodeGroup>

#### Example request

```bash  theme={null}
$ curl https://example.ngrok.app/api/example
```

```http  theme={null}
HTTP/2 200 OK
content-type: application/json

{
  "connection-start": "2024-06-24T15:30:00Z"
}
```

In this example, when a request is made to `/api/example`, ngrok returns a
custom JSON response with the default status code of `200`. The response includes a
`content-type: application/json` header and a JSON body that uses CEL
Interpolation to show the connection start time using the [`conn.ts.start`
variable](/traffic-policy/variables/connection/#conntsstart).

### Custom plaintext response with multiple CEL interpolations

The following [Traffic Policy](/traffic-policy/)
configuration demonstrates how to use the `custom-response` action to return a
`text/plain` response with multiple CEL interpolations.

#### Example Traffic Policy document

<CodeGroup>
  ```yaml policy.yml {8} theme={null}
  on_http_request:
    - expressions:
        - req.url.path == '/api/example'
      actions:
        - type: custom-response
          config:
            status_code: 418
            body: connection began at ${conn.ts.start}, now ${timestamp(time.now)}
            headers:
              content-type: text/plain
  ```

  ```json policy.json {12} theme={null}
  {
    "on_http_request": [
      {
        "expressions": [
          "req.url.path == '/api/example'"
        ],
        "actions": [
          {
            "type": "custom-response",
            "config": {
              "status_code": 418,
              "body": "connection began at ${conn.ts.start}, now ${timestamp(time.now)}",
              "headers": {
                "content-type": "text/plain"
              }
            }
          }
        ]
      }
    ]
  }
  ```
</CodeGroup>

#### Example request

```bash  theme={null}
$ curl https://example.ngrok.app/api/example
```

```http  theme={null}
HTTP/2 418 I'm a teapot
content-type: text/plain

connection began at 2024-06-24T15:30:00Z, now 2024-06-24T16:30:00Z
```

In this example, when a request is made to `/api/example`, ngrok returns a
custom plain text response with a status code of `418`. The response includes a
`content-type: text/plain` header and a body that uses multiple string
interpolations to show the connection start time and the current time.

## Action result variables

The following variables are made available for use in subsequent expressions and
CEL interpolations after the action has run. Variable values will only apply
to the last action execution, results are not concatenated.

<Note>This action does not set any variables after it has been executed.</Note>


Built with [Mintlify](https://mintlify.com).