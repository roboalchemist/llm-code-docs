# Source: https://www.zuplo.com/docs/policies/clear-headers-outbound.md

# Clear Response Headers Policy

Removes all headers from the response except for those in the exclude list.

## Configuration

The configuration shows how to configure the policy in the 'policies.json' document.

```json title="config/policies.json"
{
  "name": "my-clear-headers-outbound-policy",
  "policyType": "clear-headers-outbound",
  "handler": {
    "export": "ClearHeadersOutboundPolicy",
    "module": "$import(@zuplo/runtime)",
    "options": {
      "exclude": ["my-header", "aws-request-id"]
    }
  }
}
```

### Policy Configuration

- `name` <code className="text-green-600">&lt;string&gt;</code> - The name of your policy instance. This is used as a reference in your routes.
- `policyType` <code className="text-green-600">&lt;string&gt;</code> - The identifier of the policy. This is used by the Zuplo UI. Value should be `clear-headers-outbound`.
- `handler.export` <code className="text-green-600">&lt;string&gt;</code> - The name of the exported type. Value should be `ClearHeadersOutboundPolicy`.
- `handler.module` <code className="text-green-600">&lt;string&gt;</code> - The module containing the policy. Value should be `$import(@zuplo/runtime)`.
- `handler.options` <code className="text-green-600">&lt;object&gt;</code> - The options for this policy. [See Policy Options](#policy-options) below.

### Policy Options

The options for this policy are specified below. All properties are optional unless specifically marked as required.

- `exclude` <code className="text-green-600">&lt;string[]&gt;</code> - The headers that should not be removed.

## Using the Policy

Read more about [how policies work](/articles/policies)
