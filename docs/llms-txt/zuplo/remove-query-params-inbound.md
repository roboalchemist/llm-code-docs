# Source: https://www.zuplo.com/docs/policies/remove-query-params-inbound.md

# Remove Query Parameters Policy

Remove query parameters from the incoming request

## Configuration

The configuration shows how to configure the policy in the 'policies.json' document.

```json title="config/policies.json"
{
  "name": "my-remove-query-params-inbound-policy",
  "policyType": "remove-query-params-inbound",
  "handler": {
    "export": "RemoveQueryParamsInboundPolicy",
    "module": "$import(@zuplo/runtime)",
    "options": {
      "params": ["param1", "param2"]
    }
  }
}
```

### Policy Configuration

- `name` <code className="text-green-600">&lt;string&gt;</code> - The name of your policy instance. This is used as a reference in your routes.
- `policyType` <code className="text-green-600">&lt;string&gt;</code> - The identifier of the policy. This is used by the Zuplo UI. Value should be `remove-query-params-inbound`.
- `handler.export` <code className="text-green-600">&lt;string&gt;</code> - The name of the exported type. Value should be `RemoveQueryParamsInboundPolicy`.
- `handler.module` <code className="text-green-600">&lt;string&gt;</code> - The module containing the policy. Value should be `$import(@zuplo/runtime)`.
- `handler.options` <code className="text-green-600">&lt;object&gt;</code> - The options for this policy. [See Policy Options](#policy-options) below.

### Policy Options

The options for this policy are specified below. All properties are optional unless specifically marked as required.

- `params` **(required)** <code className="text-green-600">&lt;string[]&gt;</code> - An array of query parameters to be removed from the incoming request.

## Using the Policy

Read more about [how policies work](/articles/policies)
