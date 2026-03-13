# Source: https://ngrok.com/docs/traffic-policy/actions/redirect.md

> ## Documentation Index
> Fetch the complete documentation index at: https://ngrok.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Redirect Action

> Redirect incoming requests to new URLs by modifying the original URLs with regular expressions.

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

The Redirect Traffic Policy Action enables users to send HTTP `3xx` responses by transforming the incoming URL using a regular expression and optional CEL interpolation.
It can modify any part of the URL such as scheme, host, port, path, or query, and returns a redirect via the `Location` header.

This action is different from the [URL Rewrite Action](/traffic-policy/actions/url-rewrite/), which changes the request internally while keeping the client's URL unchanged.
Redirects, by contrast, instruct the client to issue a new request to the new URL.

## Configuration reference

The [Traffic Policy](/traffic-policy/) configuration reference for this action.

### Supported phases

`on_http_request`

### Type

`redirect`

### Configuration fields

<ConfigField title="from" type="string" required={false} cel={true}>
  A regular expression pattern used to match a part of the URL.
</ConfigField>

<ConfigField title="to" type="string" required={true} cel={true}>
  A regular expression pattern used to replace the matched part of the URL.
</ConfigField>

<ConfigField title="status_code" type="integer" required={false} defaultValue="302">
  A <code>3xx</code> status code used for redirecting.
</ConfigField>

<ConfigField title="headers" type="object" required={false} cel={true}>
  Map of key-value headers to be added to the response.
  Maximum <code>10</code> headers can be specified.
</ConfigField>

## Behavior

The Redirect Action modifies the request URL and returns an HTTP redirect (`3xx`) response.
It performs the following transformation in sequence:

1. Evaluate any CEL interpolation
2. Apply the regular expression match (`from`)
3. Replace the matched text or URL with the `to` value
4. Send the redirect response

If the rewritten URL is identical to the original, ngrok skips the redirect.

### CEL interpolation

CEL expressions in `${...}` are evaluated before the redirect rule is applied. Interpolations can reference request or connection data.

For example:

```yaml  theme={null}
to: https://example.com?city=${conn.geo.city}
```

If the request originates from San Francisco, the final redirect target is:

```
https://example.com?city=San%20Francisco
```

### Matching

The `from` field is a **regular expression** evaluated against the entire URL (scheme, host, port, path, query, and fragment). Matching is not anchored by default; a substring match anywhere in the URL triggers the redirect.

#### Example

The following example redirects any request that contains `/api/v1/` to `/api/v2/`. The redirect is applied to the entire URL, not just the path.

```yaml  theme={null}
from: /api/v1/
to: /api/v2/
```

Given the above, `https://example.com/foobar/api/v1/users` would be redirected to `https://example.com/foobar/api/v2/users`.

#### Anchoring / path prefix

Anchoring with `^/api/v1/` will not match paths that include the full scheme. To match only the path, use one of the following methods:

<CodeGroup>
  ```yaml Regular Expressions theme={null}
  # Anchor the full URL, capture authority, and rewrite the path segment.
  from: ^((?:https?)://[^/]+)/api/v1/(.*)$
  to: $1/api/v2/$2
  ```

  ```yaml CEL Interpolation theme={null}
  # Compose anchors with CEL to bind the scheme and authority before matching.
  from: ^${req.url.scheme}://${req.url.authority}/api/v1/
  to: ${req.url.scheme}://${req.url.authority}/api/v2/
  ```

  ```yaml Phase Expressions theme={null}
  # Constrain by path in expressions, then use a relative replacement.
  on_http_request:
    - expressions:
        - req.url.path.startsWith('/api/v1/')
      actions:
        - type: redirect
          config:
            from: /api/v1/
            to: /api/v2/
  ```
</CodeGroup>

### Replacement behavior

The `to` value replaces what was matched by `from`.
The replacement is relative to the `from` match.
When `from` is omitted, the redirect action replaces the entire URL.
Capture groups (such as `$1`, `$2`) can be used to insert matched text into the replacement.

When `from` matches a substring, only that segment changes:

```yaml  theme={null}
from: /v1/
to: /v2/
```

Given the above, `https://example.com/api/v1/users` would be redirected to `https://example.com/api/v2/users`.

#### Relative versus absolute replacements

The `to` value is applied relative to the `from` match. When `from` matches part of the URL, only that segment is replaced. When `from` is omitted, ngrok treats the entire URL as matched and replaces it absolutely.

**Relative example**

```yaml  theme={null}
from: /old
to: https://new.example.com/blog
```

Given the above, `https://example.com/old/foo` would become `https://example.com/https://new.example.com/blog/foo`.

**Absolute example**

When a partial match exists, the replacement is relative; when no `from` match is defined, it is absolute:

```yaml  theme={null}
to: https://new.example.com/blog
```

Given the above, any request to `https://example.com` would be redirected to `https://new.example.com/blog`.

**Redirecting to another host**

To redirect cleanly to a new host, match the entire URL:

```yaml  theme={null}
from: ^https?://[^/]+/old/(.*)$
to: https://new.example.com/new/$1
```

Given the above, `https://example.com/old/foo` would be redirected to `https://new.example.com/new/foo`.

<Note>
  If the rewritten URL equals the original, ngrok skips the redirect.
</Note>

### Redirect response

After replacement, the redirect action sends an HTTP redirect with the computed `Location` header. The default status code is `302 Found`.

| Code    | Description        | Behavior                                                             |
| ------- | ------------------ | -------------------------------------------------------------------- |
| **301** | Moved Permanently  | Clients may cache the redirect.                                      |
| **302** | Found (default)    | Temporary redirect; some clients change the request method to `GET`. |
| **303** | See Other          | Forces the next request to use `GET`.                                |
| **307** | Temporary Redirect | Preserves the original request method and body.                      |
| **308** | Permanent Redirect | Preserves the original request method and body.                      |

You can also include up to 10 custom headers in the redirect response.

**Example**

```yaml  theme={null}
from: ^(https?://[^/]+)/products(.*)$
to: $1/store/products$2
status_code: 301
headers:
  x-redirected: true
```

**Result**

```
HTTP/1.1 301 Moved Permanently
location: https://example.ngrok.app/store/products
x-redirected: true
```

Once the redirect is sent, the action ends the current phase and no further actions are executed.

### Non-terminating action

This is a **Non-terminating action**. It does not return a response, and will allow Traffic Policy processing to continue to the next Action in the chain. All **Cloud Endpoint** Traffic Policies must end with a terminating action. This requirement does not apply to **Agent Endpoints**.

## Examples

### Redirect using paths

The following [Traffic Policy](/traffic-policy/) configuration demonstrates how to use the `redirect` action to redirect incoming requests from `/products` to `/store/products`.

#### Example Traffic Policy document

<CodeGroup>
  ```yaml policy.yml theme={null}
  on_http_request:
    - actions:
        - type: redirect
          config:
            from: ^(https?://[^/]+)/products(.*)$
            to: $1/store/products$2
  ```

  ```json policy.json theme={null}
  {
    "on_http_request": [
      {
        "actions": [
          {
            "type": "redirect",
            "config": {
              "from": "^(https?://[^/]+)/products(.*)$",
              "to": "$1/store/products$2"
            }
          }
        ]
      }
    ]
  }
  ```
</CodeGroup>

This configuration will redirect any request from `/products` to `/store/products` with the default `302 Found` status code.

#### Example request

```bash  theme={null}
$ curl -i https://example.ngrok.app/products
```

```http  theme={null}
HTTP/1.1 302 Found
location: https://example.ngrok.app/store/products
```

In this example, a request to `/products` will be redirected to `/store/products` with a `302 Found` status code, and the `Location` header will indicate the new URL.

### Redirect using regular expressions

The following [Traffic Policy](/traffic-policy/) configuration demonstrates how to use the `redirect` action to redirects requests from an old API endpoint to a new one.

#### Example Traffic Policy document

<CodeGroup>
  ```yaml policy.yml theme={null}
  on_http_request:
    - expressions:
        - req.url.path.startsWith('/api/')
      actions:
        - type: redirect
          config:
            from: /api/v1/users?id=([0-9]+)
            to: /api/v2/users/$1/
            status_code: 301
            headers:
              x-redirected: 'true'
  ```

  ```json policy.json theme={null}
  {
    "on_http_request": [
      {
        "expressions": [
          "req.url.path.startsWith('/api/')"
        ],
        "actions": [
          {
            "type": "redirect",
            "config": {
              "from": "/api/v1/users?id=([0-9]+)",
              "to": "/api/v2/users/$1/",
              "status_code": 301,
              "headers": {
                "x-redirected": "true"
              }
            }
          }
        ]
      }
    ]
  }
  ```
</CodeGroup>

In this configuration, requests from `/api/v1/users?id=([0-9]+)` are matched and redirected to `/api/v2/users/$1/` with a `301` status code. Additionally, a custom header `x-redirected: true` is added to the response.

#### Example request

```bash  theme={null}
$ curl -i https://example.ngrok.app/api/v1/users?id=123
```

```http  theme={null}
HTTP/1.1 301 Moved Permanently
location: https://example.ngrok.app/api/v2/users/123/
x-redirected: true
```

The request will be redirected to the new URL `/api/v2/users/123/`, with a `301 Moved Permanently` status and a custom header.

### Redirect with CEL interpolation

The following [Traffic Policy](/traffic-policy/) configuration demonstrates how to use the `redirect` action to redirect users while using CEL Interpolation.

#### Example Traffic Policy document

<CodeGroup>
  ```yaml policy.yml {7} theme={null}
  on_http_request:
    - expressions:
        - req.url.path in ['/api/v2/geo', '/api/v2/geo/']
      actions:
        - type: redirect
          config:
            to: /api/v2/geo?city=${conn.geo.city}
  ```

  ```json policy.json {11} theme={null}
  {
    "on_http_request": [
      {
        "expressions": [
          "req.url.path in ['/api/v2/geo', '/api/v2/geo/']"
        ],
        "actions": [
          {
            "type": "redirect",
            "config": {
              "to": "/api/v2/geo?city=${conn.geo.city}"
            }
          }
        ]
      }
    ]
  }
  ```
</CodeGroup>

This configuration will redirect any request from `/api/v2/geo` or `/api/v2/geo/` to `/api/v2/geo?city=${conn.geo.city}` using CEL Interpolation to insert the city from the connection's geolocation data.

#### Example request

```bash  theme={null}
$ curl -i https://example.ngrok.app/api/v2/geo
```

```http  theme={null}
HTTP/1.1 302 Found
location: https://example.ngrok.app/api/v2/geo?city=San%20Francisco
```

In this example, a request to `https://example.ngrok.app/api/v2/geo` will be redirected to `https://example.ngrok.app/api/v2/geo?city=San Francisco`, with the `302 Found` status code and the `Location` header indicating the new URL that includes the city from the connection's geolocation data.

## Action result variables

The following variables are made available for use in subsequent expressions and
CEL interpolations after the action has run. Variable values will only apply
to the last action execution, results are not concatenated.

<ConfigField title="actions.ngrok.redirect.matches" type="array of strings">
  A list of elements that were matched during redirection. These represent the request components (for example, path or query parameters) that triggered the action and resulted in the redirect.
</ConfigField>

<ConfigField title="actions.ngrok.redirect.url" type="string">
  The URL to which the traffic was redirected. This is the destination URL returned as part of the redirect response after the action was executed.
</ConfigField>

<ConfigField title="actions.ngrok.redirect.error.code" type="string">
  A machine-readable code describing an error that occurred during the action's execution.
</ConfigField>

<ConfigField title="actions.ngrok.redirect.error.message" type="string">
  A human-readable message providing details about an error that occurred during the action's execution.
</ConfigField>


Built with [Mintlify](https://mintlify.com).