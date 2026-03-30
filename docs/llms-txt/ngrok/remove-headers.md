# Source: https://ngrok.com/docs/traffic-policy/actions/remove-headers.md

> ## Documentation Index
> Fetch the complete documentation index at: https://ngrok.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Remove Headers Action

> Remove headers from an HTTP request or response before it is delivered upstream or back to the client.

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

The **Remove Headers** Traffic Policy action enables you to remove headers from
an HTTP request before it is sent upstream or from an HTTP response before it is
sent back to the client.

## Configuration reference

The [Traffic Policy](/traffic-policy/) configuration
reference for this action.

### Supported phases

`on_http_request`, `on_http_response`

### Type

`remove-headers`

### Configuration fields

<ConfigField title="headers" type="array of strings" required={true}>
  List of header keys to remove from the request or response.

  Minimum <code>1</code>, Maximum <code>10</code>.
</ConfigField>

## Behavior

### During `on_http_request`

When executed during the `on_http_request` phase, this action will remove the specified headers from incoming HTTP requests before reaching the upstream server.

### During `on_http_response`

When executed during the `on_http_response`, the configured headers are removed from HTTP responses returned from the upstream server before reaching the client.

### Removal only

This action will only remove headers from the request or response.

* If you want to add a header use the [`add-headers`](/traffic-policy/actions/add-headers) action.
* If you want to replace a header, first use this action *then* use the [`add-headers`](/traffic-policy/actions/add-headers) action.

### Ordering

Since actions are run in the order they are specified, to modify headers that have been added by other actions you must place this action
after them in your Traffic Policy document.

### Special cases

* You may not add or remove the `user-agent` header.

### Non-terminating action

This is a **Non-terminating action**. It does not return a response, and will allow Traffic Policy processing to continue to the next Action in the chain. All **Cloud Endpoint** Traffic Policies must end with a terminating action. This requirement does not apply to **Agent Endpoints**.

## Examples

### Removing headers from all requests

If you're getting a lot of requests with `x-client-version` and `x-trace-id`
and it is starting to overwhelm your logging system, remove these headers
from all requests. The following example demonstrates how to remove these headers
using the `remove-headers` action.

#### Example Traffic Policy document

<CodeGroup>
  ```yaml policy.yml theme={null}
  on_http_request:
    - actions:
        - type: remove-headers
          config:
            headers:
              - x-client-version
              - x-trace-id
  ```

  ```json policy.json theme={null}
  {
    "on_http_request": [
      {
        "actions": [
          {
            "type": "remove-headers",
            "config": {
              "headers": [
                "x-client-version",
                "x-trace-id"
              ]
            }
          }
        ]
      }
    ]
  }
  ```
</CodeGroup>

For this example, assume that ngrok is pointing at the upstream service
[https://httpbin.org](https://httpbin.org).

#### Example request

```bash  theme={null}
$ curl -H "x-client-version: 3.1" -H "x-trace-id: abc123" https://httpbin.ngrok.app/get
< HTTP/2 200

{
...
  "headers": {
    "Date": "2024-06-24T15:30:00Z",
  }
...
}
```

In this example even though the `x-client-version` and `x-trace-id` headers were sent,
they were not present on the request that was sent upstream.

## Action result variables

The following variables are made available for use in subsequent expressions and
CEL interpolations after the action has run. Variable values will only apply
to the last action execution, results are not concatenated.

<ConfigField title="actions.ngrok.remove_headers.headers_removed" type="array of strings">
  A list of headers that were successfully removed by the action.
</ConfigField>


Built with [Mintlify](https://mintlify.com).