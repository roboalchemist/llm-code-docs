# Source: https://ngrok.com/docs/traffic-policy/actions/rate-limit.md

> ## Documentation Index
> Fetch the complete documentation index at: https://ngrok.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Rate Limit Action

> Limit the rate of traffic that successfully reaches your endpoint.

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

The **Rate Limit** Traffic Policy action enables you to configure thresholds
that restrict the throughput of traffic that successfully reaches your endpoint.

Traffic may be limited overall or by attributes of the incoming requests.

## Configuration reference

The [Traffic Policy](/traffic-policy/) configuration
reference for this action.

### Supported phases

`on_http_request`

### Type

`rate-limit`

### Configuration fields

<ConfigField title="name" type="string" required={true}>
  <p>A name for this rate limit configuration. Must be less than <code>1024</code> characters.</p>
</ConfigField>

<ConfigField title="enforce" type="boolean" required={false}>
  <p>Controls whether the rate limit is actively applied at runtime. When enabled, requests exceeding the limit are blocked or throttled as configured. When disabled, the system evaluates the rate limit but does not enforce it, allowing you to test configurations, gather metrics, or return a custom response.</p>
  <p>The default value is <code>true</code>.</p>
</ConfigField>

<ConfigField title="algorithm" type="enum" required={true}>
  <p>The rate limit algorithm to be used.</p>

  <ConfigEnum label="Supported values">
    <ConfigEnumOption>`sliding_window`</ConfigEnumOption>
  </ConfigEnum>
</ConfigField>

<ConfigField title="capacity" type="integer" required={true}>
  <p>The maximum number of requests allowed to reach your upstream server.</p>
  <p>The minimum capacity is <code>1</code> and the maximum capacity is <code>2,000,000,000</code>.</p>
</ConfigField>

<ConfigField title="rate" type="string" required={true}>
  <p>The duration in which events may be limited based on the current capacity. Must be specified as a time duration that is a multiple of ten seconds (for example, <code>"90s"</code>, <code>"10m"</code>).</p>
  <p>The minimum value is <code>"60s"</code> and the maximum value is <code>"24h"</code>.</p>
</ConfigField>

<ConfigField title="bucket_key" type="array of strings" required={true}>
  <p>The elements of this collection define the unique key of a request to track the rate at which the capacity is being met.</p>
  <p>Each bucket key is a CEL expression which includes all valid Traffic Policy [variables](/traffic-policy/variables/) and [macros](/traffic-policy/macros/).</p>

  <ConfigEnum label="Sample buckets">
    <ConfigEnumOption>`req.host` - The Host of the request.</ConfigEnumOption>
    <ConfigEnumOption>`conn.client_ip` - The client IP address.</ConfigEnumOption>
    <ConfigEnumOption>`getReqHeader('X-Example-Header-Name')` - The value for the specified header key, if it exists.</ConfigEnumOption>
  </ConfigEnum>

  <p>Up to ten bucket keys can be specified. For multiple buckets, the action will rate limit by each unique combination of buckets.</p>
</ConfigField>

## Behavior

### Determining the rate limit bucket

When this action is executed, information from the incoming HTTP request is
used to determine which rate limit bucket the request falls into. Each bucket
is defined by specific criteria through the `bucket_key` configuration field
such as client IP, request host, or a header value.

If the bucket has not exceeded its capacity, the request proceeds to the next
action in your policy configuration.

## Multiple buckets

If multiple `bucket_key` values are specified, the action will create a
unique rate limit bucket for each combination of the specified keys. For
example, if you have two `bucket_key` values, such as `req.host` and `conn.client_ip`,
all incoming requests that have the exact same combination of `Host` header and client IP
will be grouped into the same rate limit bucket. To rate limit separately with two different
buckets, you can create multiple `rate-limit` actions instead.

### Rate limit exceeded

If the identified bucket has received more events than its capacity over the
specified duration:

1. The request is rejected with an `HTTP 429—Too Many Requests` status code.
2. The `retry-after` header is included in the response, indicating the number
   of seconds after which the request may be retried.

### Capacity per ingress server

Currently, the `capacity` for each rate limit bucket is applied per ingress
server. This means that each server independently tracks the number of requests
and enforces the rate limits accordingly.

### Non-terminating action

This is a **Non-terminating action**. It does not return a response, and will allow Traffic Policy processing to continue to the next Action in the chain. All **Cloud Endpoint** Traffic Policies must end with a terminating action. This requirement does not apply to **Agent Endpoints**.

## Examples

### Rate limit by host header

The following [Traffic Policy](/traffic-policy/)
configuration demonstrates how to use the `rate-limit` action to rate limit
all incoming requests by the `Host` header.

#### Example Traffic Policy document

<CodeGroup>
  ```yaml policy.yml {10} theme={null}
  on_http_request:
    - actions:
        - type: rate-limit
          config:
            name: Only allow 30 requests per minute
            algorithm: sliding_window
            capacity: 30
            rate: 60s
            bucket_key:
              - 'hasReqHeader(''host'') ? getReqHeader(''host'')[0] : ''unknown'''
  ```

  ```json policy.json {13} theme={null}
  {
    "on_http_request": [
      {
        "actions": [
          {
            "type": "rate-limit",
            "config": {
              "name": "Only allow 30 requests per minute",
              "algorithm": "sliding_window",
              "capacity": 30,
              "rate": "60s",
              "bucket_key": [
                "hasReqHeader('host') ? getReqHeader('host')[0] : 'unknown'"
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
$ curl https://httpbin.ngrok.app/get
```

```http  theme={null}
HTTP/2 429
retry-after: 24
```

In this example, a connection attempt to `httpbin.ngrok.app` using the `curl`
command returns a `429` status code with a `retry-after` header indicating
the number of seconds to wait before retrying the request.

## Action result variables

The following variables are made available for use in subsequent expressions and
CEL interpolations after the action has run. Variable values will only apply
to the last action execution, results are not concatenated.

<ConfigField title="actions.ngrok.rate_limit.bucket_key" type="string">
  <p>The key used for bucketing requests. This is the key used to group and track requests in the rate-limiting process, ensuring that the same bucket is subject to the rate limit across multiple requests.</p>
</ConfigField>

<ConfigField title="actions.ngrok.rate_limit.limited" type="boolean">
  <p>Indicates whether the request was limited by the rate limit. If  `true`, the request was rate-limited based on the configured limits for the specified bucket.</p>
</ConfigField>

<ConfigField title="actions.ngrok.rate_limit.error.code" type="string">
  <p>A machine-readable code describing an error that occurred during the action's execution.</p>
</ConfigField>

<ConfigField title="actions.ngrok.rate_limit.error.message" type="string">
  <p>A human-readable message providing details about an error that occurred during the action's execution.</p>
</ConfigField>


Built with [Mintlify](https://mintlify.com).