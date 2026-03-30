# Source: https://ngrok.com/docs/traffic-policy/actions/add-headers.md

> ## Documentation Index
> Fetch the complete documentation index at: https://ngrok.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Add Headers Action

> Add headers to an HTTP request or response before it is delivered upstream or back to the client.

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

The Add Headers action enables you to add custom headers to an HTTP request or
response before delivery to the upstream service or client. This is useful
for attaching metadata like request identifiers, applying security controls, or
adjusting how applications process traffic.

## Configuration reference

The [Traffic Policy](/traffic-policy/) configuration reference for this action.

### Supported phases

`on_http_request`, `on_http_response`

### Type

`add-headers`

### Configuration fields

<ConfigField title="headers" type="object" cel={true}>
  Map of header key to header value to be added.

  Minimum `1`, Maximum `10`.
</ConfigField>

## Behavior

When configured in the `on_http_request` phase, this action will add the specified headers to incoming http requests before reaching the upstream server. When
configured in the `on_http_response` phase, the specified headers are added to the http response from the upstream server.

### Addition only

This action will only add headers to the request or response. If the header already exists
it will append another header with the same key unless it is the `host` header,
see [Special Cases](#special-cases).

To replace or remove headers use the [`remove-headers`](/traffic-policy/actions/remove-headers) action then
add the header with the desired value.

### Case sensitivity

Header keys added through this action are normalized to lowercase per the [HTTP/2 specification](https://datatracker.ietf.org/doc/html/rfc7540#section-8.1.2).

### Ordering

Since actions are run in the order they are specified, to modify headers that have been added by other actions you must place this action
after them in your Traffic Policy document.

### Special cases

* Adding the `host` header override the existing value instead of appending another header.
* You may not add or remove the `user-agent` header.
* You may not use this action to add the `ngrok-skip-browser-warning` header to skip the ngrok browser warning on free accounts. For more information, check out the [free plan limits guide](/pricing-limits/free-plan-limits#removing-the-interstitial-page).

### Non-terminating action

This is a **Non-terminating action**. It does not return a response, and will allow Traffic Policy processing to continue to the next Action in the chain. All **Cloud Endpoint** Traffic Policies must end with a terminating action. This requirement does not apply to **Agent Endpoints**.

## Examples

### Adding client IP headers to all HTTP requests

The following [Traffic Policy](/traffic-policy/)
configuration will add the client IP address to all HTTP requests.

#### Example Traffic Policy document

<CodeGroup>
  ```yaml policy.yml theme={null}
  on_http_request:
    - actions:
      - type: "add-headers"
        config:
          headers:
            x-client-ip: "${conn.client_ip}"
  ```

  ```json policy.json theme={null}
  {
    "on_http_request": [
      {
        "actions": [
          {
            "type": "add-headers",
            "config": {
              "headers": {
                "x-client-ip": "${conn.client_ip}"
              }
            }
          }
        ]
      }
    ]
  }
  ```
</CodeGroup>

For this example, assume that ngrok is pointing at the upstream service
[https://httpbin.org](https://httpbin.org) and the following header is added to all requests:

* `x-client-ip` with the value `${conn.client_ip}` to demonstrate the use of
  CEL interpolation to include the client IP address.

#### Example request

```bash  theme={null}
$ curl -i https://httpbin.ngrok.app/get
```

```http  theme={null}
HTTP/2 200 OK
content-type: application/json

{
  "headers": {
    "X-Client-Ip": "2600:1700:4fa6:1a00:2051:938:7373:5563",
  }
}
```

### Adding headers to an HTTP response

The following [Traffic Policy](/traffic-policy/)
configuration will add headers to the response from the upstream service when the method is `GET` and the URL starts with `/status/200`.

#### Example Traffic Policy document

<CodeGroup>
  ```yaml policy.yml highlight={3} theme={null}
  on_http_response:
    - expressions:
        - "req.method == \"GET\" && req.url.path.startsWith(\"/status/200\")"
      actions:
        - type: "add-headers"
          config:
            headers:
              x-custom-header: "my-custom-value"
              x-string-interpolation-example: "started at ${conn.ts.start}"
  ```

  ```json policy.json highlight={5} theme={null}
  {
    "on_http_response": [
      {
        "expressions": [
          "req.method == \"GET\" && req.url.path.startsWith(\"/status/200\")"
        ],
        "actions": [
          {
            "type": "add-headers",
            "config": {
              "headers": {
                "x-custom-header": "my-custom-value",
                "x-string-interpolation-example": "started at ${conn.ts.start}"
              }
            }
          }
        ]
      }
    ]
  }
  ```
</CodeGroup>

For this example, assume that ngrok is pointing at the upstream service
[https://httpbin.org](https://httpbin.org) and two headers are added:

* `x-custom-header` with the value `my-custom-value`
* `x-string-interpolation-example` with the value `started at ${conn.ts.start}`
  to demonstrate the use of CEL interpolation to include the request connection
  start time.

### Example request

```bash  theme={null}
$ curl -i https://httpbin.ngrok.app/status/200
```

```http  theme={null}
HTTP/2 200 OK
x-custom-header: my-custom-value
x-string-interpolation-example: started at 2024-07-13T00:10:16Z
```

## Action result variables

The following variables are made available for use in subsequent expressions and
CEL interpolations after the action has run. Variable values will only apply
to the last action execution, results are not concatenated.

<ConfigField title="actions.ngrok.add_headers.headers_added" type="object">
  <p>Map of headers that were added by the action.</p>
</ConfigField>


Built with [Mintlify](https://mintlify.com).