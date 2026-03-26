# Source: https://www.zuplo.com/docs/policies/set-status-outbound.md

# Set Status Code Policy

Sets the status code on the on the outgoing response.

## Configuration

The configuration shows how to configure the policy in the 'policies.json' document.

```json title="config/policies.json"
{
  "name": "my-set-status-outbound-policy",
  "policyType": "set-status-outbound",
  "handler": {
    "export": "SetStatusOutboundPolicy",
    "module": "$import(@zuplo/runtime)",
    "options": {
      "status": 200,
      "statusText": "OK"
    }
  }
}
```

### Policy Configuration

- `name` <code className="text-green-600">&lt;string&gt;</code> - The name of your policy instance. This is used as a reference in your routes.
- `policyType` <code className="text-green-600">&lt;string&gt;</code> - The identifier of the policy. This is used by the Zuplo UI. Value should be `set-status-outbound`.
- `handler.export` <code className="text-green-600">&lt;string&gt;</code> - The name of the exported type. Value should be `SetStatusOutboundPolicy`.
- `handler.module` <code className="text-green-600">&lt;string&gt;</code> - The module containing the policy. Value should be `$import(@zuplo/runtime)`.
- `handler.options` <code className="text-green-600">&lt;object&gt;</code> - The options for this policy. [See Policy Options](#policy-options) below.

### Policy Options

The options for this policy are specified below. All properties are optional unless specifically marked as required.

- `status` <code className="text-green-600">&lt;number&gt;</code> - The status code to be used in the response.
- `statusText` <code className="text-green-600">&lt;string&gt;</code> - The statusText to be used in the response.

## Using the Policy

Read more about [how policies work](/articles/policies)
