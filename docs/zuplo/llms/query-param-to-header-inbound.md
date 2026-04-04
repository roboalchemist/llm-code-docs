# Source: https://www.zuplo.com/docs/policies/query-param-to-header-inbound.md

# Query Parameter to Header Policy

Extracts a value from a query parameter and sets it as a header in the request.

This can be used to convert bespoke API keys passed as query parameters into
`Authorization: Bearer ...` headers or transform client requests (which may not
support headers) into downstream ready requests with appropriate headers set.

## Configuration

The configuration shows how to configure the policy in the 'policies.json' document.

```json title="config/policies.json"
{
  "name": "my-query-param-to-header-inbound-policy",
  "policyType": "query-param-to-header-inbound",
  "handler": {
    "export": "QueryParamToHeaderInboundPolicy",
    "module": "$import(@zuplo/runtime)",
    "options": {
      "headerName": "Authorization",
      "headerValue": "Bearer {value}",
      "queryParam": "apiKey",
      "removeFromUrl": true
    }
  }
}
```

### Policy Configuration

- `name` <code className="text-green-600">&lt;string&gt;</code> - The name of your policy instance. This is used as a reference in your routes.
- `policyType` <code className="text-green-600">&lt;string&gt;</code> - The identifier of the policy. This is used by the Zuplo UI. Value should be `query-param-to-header-inbound`.
- `handler.export` <code className="text-green-600">&lt;string&gt;</code> - The name of the exported type. Value should be `QueryParamToHeaderInboundPolicy`.
- `handler.module` <code className="text-green-600">&lt;string&gt;</code> - The module containing the policy. Value should be `$import(@zuplo/runtime)`.
- `handler.options` <code className="text-green-600">&lt;object&gt;</code> - The options for this policy. [See Policy Options](#policy-options) below.

### Policy Options

The options for this policy are specified below. All properties are optional unless specifically marked as required.

- `queryParam` **(required)** <code className="text-green-600">&lt;string&gt;</code> - The name of the query parameter to extract.
- `headerName` **(required)** <code className="text-green-600">&lt;string&gt;</code> - The name of the header to set.
- `headerValue` **(required)** <code className="text-green-600">&lt;string&gt;</code> - The `{value}` template for the header. Use `{value}` to substitute the query parameter value.
- `removeFromUrl` <code className="text-green-600">&lt;boolean&gt;</code> - Whether to remove the query parameter from the URL after extracting it. Defaults to `true`.

## Using the Policy

This policy can be used to transform any query parameter sent by a client into a
downstream ready header. This is especially useful for quickly setting up auth
with MCP Server Handlers or supporting clients that cannot send headers.

### Example: Auth header

To transform a query param into an `Authorization: Bearer` header, add the
policy with the following configuration:

```json
{
  "policies": [
    {
      "name": "query-param-to-header-inbound",
      "policyType": "query-param-to-header-inbound",
      "handler": {
        "export": "QueryParamToHeaderInboundPolicy",
        "module": "$import(@zuplo/runtime)",
        "options": {
          "queryParam": "apiKey",
          "headerName": "Authorization",
          "headerValue": "Bearer {value}"
        }
      }
    }
  ]
}
```

The policy will look for the `apiKey` query parameter and add a
`Authorization: Bearer ...` header with the value derived from the param.

In your route, set the policies like so:

```json
{
  "paths": {
    "/route": {
      "get": {
        "x-zuplo-route": {
          "policies": {
            "inbound": ["query-param-to-header-inbound", "api-key-auth-inbound"]
          }
        }
      }
    }
  }
}
```

Important!! You **must** set the `query-param-to-header-inbound` policy _before_
your API key auth inbound policy. This way, when the request is piped through to
the API key policy, it has the appropriate `Authorization: Bearer ...` header
set!

The flow through your inbound policies becomes:

```txt
Incoming request - /api/endpoint?apiKey=abc123
  --> Query param to header policy
    --> "abc123" transformed to "Authorization: Bearer abc123" header
  --> API key auth policy
    --> Authorized via header!
  --> API - /api/endpoint
```

Notice that the final `api/endpoint` does _not_ contain the query parameter.

By default, it is stripped from the piped request. Set `removeFromUrl` to
`false` if you want to preserve the query parameter.

Read more about [how policies work](/articles/policies)
