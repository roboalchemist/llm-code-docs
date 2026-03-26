# Source: https://www.zuplo.com/docs/policies/set-headers-outbound.md

# Set Headers Policy

Adds or sets headers on the on the outgoing response.

## Configuration

The configuration shows how to configure the policy in the 'policies.json' document.

```json title="config/policies.json"
{
  "name": "my-set-headers-outbound-policy",
  "policyType": "set-headers-outbound",
  "handler": {
    "export": "SetHeadersOutboundPolicy",
    "module": "$import(@zuplo/runtime)",
    "options": {
      "headers": [
        {
          "name": "my-header",
          "value": "my-value"
        }
      ]
    }
  }
}
```

### Policy Configuration

- `name` <code className="text-green-600">&lt;string&gt;</code> - The name of your policy instance. This is used as a reference in your routes.
- `policyType` <code className="text-green-600">&lt;string&gt;</code> - The identifier of the policy. This is used by the Zuplo UI. Value should be `set-headers-outbound`.
- `handler.export` <code className="text-green-600">&lt;string&gt;</code> - The name of the exported type. Value should be `SetHeadersOutboundPolicy`.
- `handler.module` <code className="text-green-600">&lt;string&gt;</code> - The module containing the policy. Value should be `$import(@zuplo/runtime)`.
- `handler.options` <code className="text-green-600">&lt;object&gt;</code> - The options for this policy. [See Policy Options](#policy-options) below.

### Policy Options

The options for this policy are specified below. All properties are optional unless specifically marked as required.

- `headers` **(required)** <code className="text-green-600">&lt;object[]&gt;</code> - An array of headers to set on the response. By default, headers will be overwritten if they already exists in the response, specify the overwrite property to change this behavior.
  - `name` **(required)** <code className="text-green-600">&lt;string&gt;</code> - The name of the header.
  - `value` **(required)** <code className="text-green-600">&lt;string&gt;</code> - The value of the header.
  - `overwrite` <code className="text-green-600">&lt;boolean&gt;</code> - Overwrite the value if the header is already present in the response. Defaults to `true`.

## Using the Policy

Read more about [how policies work](/articles/policies)
