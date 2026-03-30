# Source: https://www.zuplo.com/docs/policies/http-deprecation-outbound.md

# HTTP Deprecation Policy

Sets HTTP deprecation headers on the outgoing response following the IETF HTTP Deprecation Header standard. Supports the Deprecation, Sunset, and Link headers.

## Configuration

The configuration shows how to configure the policy in the 'policies.json' document.

```json title="config/policies.json"
{
  "name": "my-http-deprecation-outbound-policy",
  "policyType": "http-deprecation-outbound",
  "handler": {
    "export": "HttpDeprecationOutboundPolicy",
    "module": "$import(@zuplo/runtime)",
    "options": {
      "deprecation": true,
      "link": "https://example.com/docs/v2-migration",
      "sunset": "2025-06-30T23:59:59Z"
    }
  }
}
```

### Policy Configuration

- `name` <code className="text-green-600">&lt;string&gt;</code> - The name of your policy instance. This is used as a reference in your routes.
- `policyType` <code className="text-green-600">&lt;string&gt;</code> - The identifier of the policy. This is used by the Zuplo UI. Value should be `http-deprecation-outbound`.
- `handler.export` <code className="text-green-600">&lt;string&gt;</code> - The name of the exported type. Value should be `HttpDeprecationOutboundPolicy`.
- `handler.module` <code className="text-green-600">&lt;string&gt;</code> - The module containing the policy. Value should be `$import(@zuplo/runtime)`.
- `handler.options` <code className="text-green-600">&lt;object&gt;</code> - The options for this policy. [See Policy Options](#policy-options) below.

### Policy Options

The options for this policy are specified below. All properties are optional unless specifically marked as required.

- `deprecation` **(required)** <code className="text-green-600">&lt;undefined&gt;</code> - The deprecation value. Use `true` for already deprecated, an ISO 8601 date string for a specific date, or a Unix timestamp number.
- `sunset` <code className="text-green-600">&lt;string&gt;</code> - An ISO 8601 date string indicating when the endpoint will be removed. Sets the Sunset header.
- `link` <code className="text-green-600">&lt;string&gt;</code> - A URL to documentation about the deprecation or migration guide. Sets the Link header.

## Using the Policy

This policy adds HTTP deprecation headers to outgoing responses following the
[IETF HTTP Deprecation Header](https://datatracker.ietf.org/doc/html/draft-ietf-httpapi-deprecation-header)
standard. It supports the `Deprecation`, `Sunset`, and `Link` headers to signal
to API consumers that an endpoint is deprecated.

## Configuration

- `deprecation` **(required)**: The deprecation value. Use `true` to indicate
  the endpoint is already deprecated, an ISO 8601 date string with timezone
  offset (e.g. `"2024-12-31T23:59:59Z"`) for a specific deprecation date, or a
  Unix timestamp number.
- `sunset`: An ISO 8601 date string with timezone offset indicating when the
  endpoint will be removed. Sets the `Sunset` header.
- `link`: A URL to documentation about the deprecation or a migration guide.
  Sets the `Link` header.

## Usage

Apply this policy to outbound responses in your route configuration:

```json
{
  "policies": [
    {
      "name": "http-deprecation-policy",
      "policyType": "http-deprecation-outbound",
      "handler": {
        "export": "HttpDeprecationOutboundPolicy",
        "module": "$import(@zuplo/runtime)",
        "options": {
          "deprecation": "2025-01-15T00:00:00Z",
          "sunset": "2025-06-30T23:59:59Z",
          "link": "https://example.com/docs/v2-migration"
        }
      }
    }
  ]
}
```

If the endpoint is already deprecated and you don't need a specific date, you
can set `deprecation` to `true`:

```json
{
  "policies": [
    {
      "name": "http-deprecation-policy",
      "policyType": "http-deprecation-outbound",
      "handler": {
        "export": "HttpDeprecationOutboundPolicy",
        "module": "$import(@zuplo/runtime)",
        "options": {
          "deprecation": true,
          "link": "https://example.com/docs/v2-migration"
        }
      }
    }
  ]
}
```

## Response Headers

Based on the configuration above, the policy sets the following headers on the
response:

- **`Deprecation`** - Set to the string `"true"` when input is `true`, an
  HTTP-date when input is an ISO 8601 string, or an RFC 9651 timestamp
  (`@epoch`) when input is a Unix timestamp number.
- **`Sunset`** - An HTTP-date indicating when the endpoint will be removed.
- **`Link`** - A link to deprecation documentation, formatted as
  `<URL>; rel="deprecation"; type="text/html"`.

Read more about [how policies work](/articles/policies)
