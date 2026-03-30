# Source: https://www.zuplo.com/docs/policies/change-method-inbound.md

# Change Method Policy

Changes the HTTP method of the incoming request.

## Configuration

The configuration shows how to configure the policy in the 'policies.json' document.

```json title="config/policies.json"
{
  "name": "my-change-method-inbound-policy",
  "policyType": "change-method-inbound",
  "handler": {
    "export": "ChangeMethodInboundPolicy",
    "module": "$import(@zuplo/runtime)",
    "options": {
      "method": "POST"
    }
  }
}
```

### Policy Configuration

- `name` <code className="text-green-600">&lt;string&gt;</code> - The name of your policy instance. This is used as a reference in your routes.
- `policyType` <code className="text-green-600">&lt;string&gt;</code> - The identifier of the policy. This is used by the Zuplo UI. Value should be `change-method-inbound`.
- `handler.export` <code className="text-green-600">&lt;string&gt;</code> - The name of the exported type. Value should be `ChangeMethodInboundPolicy`.
- `handler.module` <code className="text-green-600">&lt;string&gt;</code> - The module containing the policy. Value should be `$import(@zuplo/runtime)`.
- `handler.options` <code className="text-green-600">&lt;object&gt;</code> - The options for this policy. [See Policy Options](#policy-options) below.

### Policy Options

The options for this policy are specified below. All properties are optional unless specifically marked as required.

- `method` **(required)** <code className="text-green-600">&lt;string&gt;</code> - The HTTP Method to be used, e.g. POST, GET, PUT, PATCH, etc.

## Using the Policy

Read more about [how policies work](/articles/policies)
