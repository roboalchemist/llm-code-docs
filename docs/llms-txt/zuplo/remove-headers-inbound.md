# Source: https://www.zuplo.com/docs/policies/remove-headers-inbound.md

# Remove Request Headers Policy

Remove headers from the incoming request.

## Configuration

The configuration shows how to configure the policy in the 'policies.json' document.

```json title="config/policies.json"
{
  "name": "my-remove-headers-inbound-policy",
  "policyType": "remove-headers-inbound",
  "handler": {
    "export": "RemoveHeadersInboundPolicy",
    "module": "$import(@zuplo/runtime)",
    "options": {
      "headers": ["x-request-id", "content-type"]
    }
  }
}
```

### Policy Configuration

- `name` <code className="text-green-600">&lt;string&gt;</code> - The name of your policy instance. This is used as a reference in your routes.
- `policyType` <code className="text-green-600">&lt;string&gt;</code> - The identifier of the policy. This is used by the Zuplo UI. Value should be `remove-headers-inbound`.
- `handler.export` <code className="text-green-600">&lt;string&gt;</code> - The name of the exported type. Value should be `RemoveHeadersInboundPolicy`.
- `handler.module` <code className="text-green-600">&lt;string&gt;</code> - The module containing the policy. Value should be `$import(@zuplo/runtime)`.
- `handler.options` <code className="text-green-600">&lt;object&gt;</code> - The options for this policy. [See Policy Options](#policy-options) below.

### Policy Options

The options for this policy are specified below. All properties are optional unless specifically marked as required.

- `headers` **(required)** <code className="text-green-600">&lt;string[]&gt;</code> - An array of headers to remove from the incoming request.

## Using the Policy

Read more about [how policies work](/articles/policies)
