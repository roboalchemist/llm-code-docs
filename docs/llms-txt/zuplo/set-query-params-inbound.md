# Source: https://www.zuplo.com/docs/policies/set-query-params-inbound.md

# Add or Set Query Parameters Policy

Adds or sets query parameters on the incoming request.

## Configuration

The configuration shows how to configure the policy in the 'policies.json' document.

```json title="config/policies.json"
{
  "name": "my-set-query-params-inbound-policy",
  "policyType": "set-query-params-inbound",
  "handler": {
    "export": "SetQueryParamsInboundPolicy",
    "module": "$import(@zuplo/runtime)",
    "options": {
      "params": [
        {
          "name": "my-key",
          "value": "my-value"
        }
      ]
    }
  }
}
```

### Policy Configuration

- `name` <code className="text-green-600">&lt;string&gt;</code> - The name of your policy instance. This is used as a reference in your routes.
- `policyType` <code className="text-green-600">&lt;string&gt;</code> - The identifier of the policy. This is used by the Zuplo UI. Value should be `set-query-params-inbound`.
- `handler.export` <code className="text-green-600">&lt;string&gt;</code> - The name of the exported type. Value should be `SetQueryParamsInboundPolicy`.
- `handler.module` <code className="text-green-600">&lt;string&gt;</code> - The module containing the policy. Value should be `$import(@zuplo/runtime)`.
- `handler.options` <code className="text-green-600">&lt;object&gt;</code> - The options for this policy. [See Policy Options](#policy-options) below.

### Policy Options

The options for this policy are specified below. All properties are optional unless specifically marked as required.

- `params` **(required)** <code className="text-green-600">&lt;object[]&gt;</code> - An array of query params to set in the request. By default, query parameters will be overwritten if they already exist in the request, specify the overwrite property to change this behavior.
  - `name` **(required)** <code className="text-green-600">&lt;string&gt;</code> - The name of the param.
  - `value` **(required)** <code className="text-green-600">&lt;string&gt;</code> - The value of the param.
  - `overwrite` <code className="text-green-600">&lt;boolean&gt;</code> - Overwrite the value if the param is already present in the request. Defaults to `true`.

## Using the Policy

Read more about [how policies work](/articles/policies)
