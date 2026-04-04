# Source: https://ngrok.com/docs/traffic-policy/actions/forward-internal.md

> ## Documentation Index
> Fetch the complete documentation index at: https://ngrok.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Forward Internal Action

> The Forward Internal action enables you to forward traffic from an endpoint to a internal endpoint within the same ngrok account.

export const ConfigEnumOption = ({children}) => {
  return <div className="space-y-2 px-4 py-2 list-none">{children}</div>;
};

export const ConfigEnum = ({label, children}) => {
  return <div className="m-0 flex flex-shrink-0 list-none flex-col divide-y divide-gray-200 self-start rounded-md border border-gray-200 p-0 dark:divide-gray-800 dark:border-gray-800 [&_li+li]:mt-0 [&_li]:py-2 list-none">
      <div className="px-4 py-2 font-semibold list-none">
        {label ? label : "Possible enum values"}
      </div>
      {children}
    </div>;
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

The **Forward Internal** Traffic Policy action enables you to forward traffic from an endpoint to a internal endpoint within the same ngrok account. This is useful for safely and securely routing traffic from your public endpoints to other services, giving you the ability to choose when and how your endpoints are made publicly available.

## Configuration reference

The [Traffic Policy](/traffic-policy/) configuration
reference for this action.

### Supported phases

`on_tcp_connect`, `on_http_request`

### Type

`forward-internal`

### Configuration fields

<ConfigField title="url" type="string" required={true} cel={true}>
  <p>
    The endpoint to forward to, such as <code>[http://my-internal-endpoint.internal:1234](http://my-internal-endpoint.internal:1234)</code>.
  </p>
</ConfigField>

<ConfigField title="on_error" type="enum">
  <p>
    Whether or not further actions in the Traffic Policy should run if there
    is an error.
  </p>

  <ConfigEnum>
    <ConfigEnumOption>`halt` (default)</ConfigEnumOption>
    <ConfigEnumOption>`continue`</ConfigEnumOption>
  </ConfigEnum>
</ConfigField>

## Behavior

This action forwards a request to an internal endpoint.

Any Traffic Policy associated with the internal endpoint will also be applied to the request when it's forwarded.

If the forwarding is successful, the response from the upstream for the internal endpoint will be sent back to the client making the original request. No further actions in the `inbound` phase will be executed and no traffic will be sent to the upstream for the public endpoint.

If the forwarding is unsuccessful because the specified endpoint doesn't exist, is offline, or encounters another error, the action will return an error and follow the behavior that is specified by `on_error` (see [Managing Fallback Behavior](#on-error)).

<Note>
  Even if you do not plan to send traffic to a local service when creating a forwarding endpoint, you will still need to specify a local port. This port will receive traffic if an expression causes only a subset of traffic to be forwarded or if there is an error forwarding traffic and `on_error` is set to `continue` without a subsequent terminating action.
</Note>

### HTTP headers

When forwarding HTTP requests to another endpoint, the `Host` header will be set to the hostname of the forwarding endpoint. For example, if `https://example.ngrok.app` is forwarding HTTP requests to `https://example.internal`, the `Host` header received by the upstream will be `example.ngrok.app`.

The action will also set the `X-Forwarded-For`, `X-Forwarded-Host`, and `X-Forwarded-Proto` headers when making the upstream request. See [Upstream Headers](/universal-gateway/http#upstream-headers) for more information.

### Managing fallback behavior (`on_error`)

If `on_error` is set to `halt` (default) and the action encounters an error when forwarding traffic, the Traffic Policy chain will halt and no further actions will be executed. For example, if you have a `log` action after the `forward-internal` action and the `url` specified isn't an online endpoint, the `log` action will not be run and the error will be returned.

However, if `on_error` is set to `continue`, actions that appear after the `forward-internal` action will still be executed even if the `forward-internal` action encounters an error. This can be used as a fallback to forward traffic to one of many endpoints depending which are online.

### Valid forward targets

A request may only be forwarded to a internal endpoint on the same account as this endpoint.

The target must be of the same protocol (that is, an HTTP Endpoint may only forward to an HTTP Internal Endpoint).

In addition, the target's Traffic Policy may only specify policy for the current protocol, for example if `forward-internal` is used in the `on_http_request` phase, the internal endpoint may only have `on_http_request` and `on_http_response` sections.

### Terminating action

This is a **terminating action**. It will return a response and cause Traffic Policy processing to end without executing any further Actions.

<Info>
  This action is *not* terminating if `on_error` is set to `continue`.[Learn more](#managing-fallback-behavior-on-error).
</Info>

## Examples

### Basic example

This example configuration will set up a public endpoint (`forward-internal-example.ngrok.app`) forwarding all traffic it receives to a internal endpoint (`example.internal`) that forwards the request to port `80` on your local machine. Since it is forwarding all traffic to the internal endpoint, no traffic will be sent to `8080` which is the upstream port for the public endpoint.

#### Example Traffic Policy document

<CodeGroup>
  ```yaml policy.yml theme={null}
  on_http_request:
    - actions:
        - type: forward-internal
          config:
            url: https://example.internal
  ```

  ```json policy.json theme={null}
  {
    "on_http_request": [
      {
        "actions": [
          {
            "type": "forward-internal",
            "config": {
              "url": "https://example.internal"
            }
          }
        ]
      }
    ]
  }
  ```
</CodeGroup>

#### Start an internal endpoint

```bash  theme={null}
ngrok http 80 --url example.internal
```

#### Start public endpoint with Traffic Policy

```bash  theme={null}
ngrok http 8080 --url forward-internal-example.ngrok.app --traffic-policy-file /path/to/policy.yml
```

### Example request

```bash  theme={null}
$ curl https://forward-internal-example.ngrok.app -v
 ...
> GET / HTTP/2
> Host: forward-internal-example.ngrok.app
> User-Agent: curl/[version]
> Accept: */*
...
```

This request will be forwarded to the internal endpoint `https://example.internal` which will then forward the request to port `80` on your local machine.

```http  theme={null}
GET / HTTP/1.1
Host: forward-internal-example.ngrok.app
User-Agent: curl/[version]
Accept: */*
X-Forwarded-For: [ngrok IP]
X-Forwarded-Host: forward-internal-example.ngrok.app
X-Forwarded-Proto: https
Accept-Encoding: gzip
```

## Action result variables

The following variables are made available for use in subsequent expressions and
CEL interpolations after the action has run. Variable values will only apply
to the last action execution, results are not concatenated.

<Note>This action does not set any variables after it has been executed.</Note>


Built with [Mintlify](https://mintlify.com).