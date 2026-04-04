# Source: https://www.zuplo.com/docs/policies/remove-headers-outbound.md

# Remove Response Headers Policy

Remove configured headers from the outgoing response.

## Configuration

The configuration shows how to configure the policy in the 'policies.json' document.

```json title="config/policies.json"
{
  "name": "my-remove-headers-outbound-policy",
  "policyType": "remove-headers-outbound",
  "handler": {
    "export": "RemoveHeadersOutboundPolicy",
    "module": "$import(@zuplo/runtime)",
    "options": {
      "headers": ["x-amz-content-sha256", "x-amz-date"]
    }
  }
}
```

### Policy Configuration

- `name` <code className="text-green-600">&lt;string&gt;</code> - The name of your policy instance. This is used as a reference in your routes.
- `policyType` <code className="text-green-600">&lt;string&gt;</code> - The identifier of the policy. This is used by the Zuplo UI. Value should be `remove-headers-outbound`.
- `handler.export` <code className="text-green-600">&lt;string&gt;</code> - The name of the exported type. Value should be `RemoveHeadersOutboundPolicy`.
- `handler.module` <code className="text-green-600">&lt;string&gt;</code> - The module containing the policy. Value should be `$import(@zuplo/runtime)`.
- `handler.options` <code className="text-green-600">&lt;object&gt;</code> - The options for this policy. [See Policy Options](#policy-options) below.

### Policy Options

The options for this policy are specified below. All properties are optional unless specifically marked as required.

- `headers` **(required)** <code className="text-green-600">&lt;string[]&gt;</code> - An array of headers to be removed from the outgoing response.

## Using the Policy

Read more about [how policies work](/articles/policies)
