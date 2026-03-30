# Source: https://ngrok.com/docs/traffic-policy/actions/url-rewrite.md

> ## Documentation Index
> Fetch the complete documentation index at: https://ngrok.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# URL Rewrite Action

> Modify the incoming request URL using regular expressions before it reaches the upstream server, while keeping the URL seen by the client unchanged.

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

The **URL Rewrite** Traffic Policy action allows you to modify the incoming request URL using regular expressions before it reaches the upstream server, while keeping the URL seen by the client unchanged.

This action is particularly useful for routing users without exposing internal system details.

## Configuration reference

This is the [Traffic Policy](/traffic-policy/) configuration
reference for this action.

### Supported phases

`on_http_request`

### Type

`url-rewrite`

### Configuration fields

<ConfigField title="from" type="string" required={false} cel={true}>
  <p>A regular expression pattern used to match a part of the URL.</p>
  <p>Supports [CEL Interpolation](/traffic-policy/concepts/cel-interpolation).</p>
</ConfigField>

<ConfigField title="to" type="string" required={true} cel={true}>
  <p>A regular expression pattern used to replace the matched part of the URL.</p>
  <p>Supports [CEL Interpolation](/traffic-policy/concepts/cel-interpolation).</p>
</ConfigField>

## Behavior

This action replaces all occurrences of the `from` regular expression in the request URL with the `to` replacement value.

### Matching

Matching is performed against the entire URL, including the scheme, userinfo, host, and port, not just the path.

To match requests that begin with `/products`, use [CEL Interpolation](/traffic-policy/concepts/cel-interpolation) and write `^${req.url.authority}/products`, or use an expression like `req.url.path.startsWith('/products')` in the phase rule's `expressions` field.

### Note about CEL interpolation

All CEL Interpolation will occur **before** regular expressions
are evaluated.

### Non-terminating action

This is a **Non-terminating action**. It does not return a response, and will allow Traffic Policy processing to continue to the next Action in the chain. All **Cloud Endpoint** Traffic Policies must end with a terminating action. This requirement does not apply to **Agent Endpoints**.

## Examples

### Rewrite using paths

The following [Traffic Policy](/traffic-policy/)
configuration demonstrates how to use the `url-rewrite` action to transparently
rewrite the request URL from `/products` to `/products.php`.

#### Example Traffic Policy document

<CodeGroup>
  ```yaml policy.yml theme={null}
  on_http_request:
    - expressions:
        - req.url.path == '/products'
      actions:
        - type: url-rewrite
          config:
            from: /products
            to: /products.php
  ```

  ```json policy.json theme={null}
  {
    "on_http_request": [
      {
        "expressions": [
          "req.url.path == '/products'"
        ],
        "actions": [
          {
            "type": "url-rewrite",
            "config": {
              "from": "/products",
              "to": "/products.php"
            }
          }
        ]
      }
    ]
  }
  ```
</CodeGroup>

This configuration will rewrite any request to `/products` to `/products.php`
without changing the URL seen by the client. This is useful for hiding away
the underlying implementation details of your service.

#### Example request

```bash  theme={null}
$ curl -i https://example.ngrok.app/products
```

```http  theme={null}
HTTP/2 200 OK
```

##### Example server logs

```http  theme={null}
GET /product.php               200 OK
```

#### Conclusion

In this example, a request to `/products` is internally
routed to `/products.php`, and the response is served
from `products.php` while the client remains unaware
of the URL rewrite.

### Rewrite using regular expressions

The following [Traffic Policy](/traffic-policy/)
configuration demonstrates how to use the `url-rewrite` action to transparently
rewrite the request URL from `/products/*` to `/products.php`.

#### Example Traffic Policy document

<CodeGroup>
  ```yaml policy.yml theme={null}
  on_http_request:
    - expressions:
        - req.url.path.startsWith('/products')
      actions:
        - type: url-rewrite
          config:
            from: /products/?([.*]+)?
            to: /products.php?query=$1
  ```

  ```json policy.json theme={null}
  {
    "on_http_request": [
      {
        "expressions": [
          "req.url.path.startsWith('/products')"
        ],
        "actions": [
          {
            "type": "url-rewrite",
            "config": {
              "from": "/products/?([.*]+)?",
              "to": "/products.php?query=$1"
            }
          }
        ]
      }
    ]
  }
  ```
</CodeGroup>

This configuration will rewrite any request to `/products/*` to
`/products.php?query=$1` without changing the URL seen by the client. This is
useful for hiding away the underlying implementation details of your service.

#### Example request

```bash  theme={null}
$ curl -i https://example.ngrok.app/products/123
```

```http  theme={null}
HTTP/2 200 OK
```

##### Example server logs

```http  theme={null}
GET /product.php?query=123          200 OK
```

#### Conclusion

In this example, a request to `/products` is internally routed to
`/products.php?query=123`, and the response is served from `products.php` while
the client remains unaware of the URL rewrite.

### Rewrite using CEL interpolation

The following [Traffic Policy](/traffic-policy/)
configuration demonstrates how to use the `url-rewrite` action to transparently
rewrite the request URL from `/products/*` to `/products.php` using a global
policy rule (no expression) by leveraging [CEL Interpolation](/traffic-policy/concepts/cel-interpolation).

#### Example Traffic Policy document

<CodeGroup>
  ```yaml policy.yml theme={null}
  on_http_request:
    - actions:
        - type: url-rewrite
          config:
            from: ${req.url.authority}/products/?([.*]+)?
            to: /products.php?query=$1
  ```

  ```json policy.json theme={null}
  {
    "on_http_request": [
      {
        "actions": [
          {
            "type": "url-rewrite",
            "config": {
              "from": "${req.url.authority}/products/?([.*]+)?",
              "to": "/products.php?query=$1"
            }
          }
        ]
      }
    ]
  }
  ```
</CodeGroup>

This configuration will rewrite any request urls that start with `/products/*`
to `/products.php?query=$1` without changing the URL seen by the client. It does
this by leveraging [CEL Interpolation](/traffic-policy/concepts/cel-interpolation) to replace the
`from` value with the request URL authority. This is useful for hiding away the
underlying implementation details of your service.

#### Example request

```bash  theme={null}
$ curl -i https://example.ngrok.app/products/123
```

```http  theme={null}
HTTP/2 200 OK
```

##### Example server logs

```http  theme={null}
GET /product.php?query=123          200 OK
```

#### Conclusion

In this example, a request to `/products` is internally routed to
`/products.php?query=123`, and the response is served from `products.php` while
the client remains unaware of the URL rewrite.

## Action result variables

The following variables are made available for use in subsequent expressions and
CEL interpolations after the action has run. Variable values will only apply
to the last action execution, results are not concatenated.

<ConfigField title="actions.ngrok.url_rewrite.matches" type="array of strings">
  <p>List of elements that matched the URL before the rewrite action was applied. These can be specific parts of the URL, such as the domain, path, or query parameters, that were matched based on the action configuration.</p>
</ConfigField>

<ConfigField title="actions.ngrok.url_rewrite.url" type="string">
  <p>The final URL after the rewrite action has been applied. This is the new URL to which the original request is redirected after the specified modifications have been made.</p>
</ConfigField>

<ConfigField title="actions.ngrok.url_rewrite.error.code" type="string">
  <p>A machine-readable code describing an error that occurred during the action's execution.</p>
</ConfigField>

<ConfigField title="actions.ngrok.url_rewrite.error.message" type="string">
  <p>A human-readable message providing details about an error that occurred during the action's execution.</p>
</ConfigField>


Built with [Mintlify](https://mintlify.com).