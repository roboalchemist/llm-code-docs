# Source: https://www.zuplo.com/docs/policies/jwt-scopes-inbound.md

# JWT Scope Validation Policy

Validates that the JWT token includes specific scopes

## Configuration

The configuration shows how to configure the policy in the 'policies.json' document.

```json title="config/policies.json"
{
  "name": "my-jwt-scopes-inbound-policy",
  "policyType": "jwt-scopes-inbound",
  "handler": {
    "export": "JWTScopeValidationInboundPolicy",
    "module": "$import(@zuplo/runtime)",
    "options": {
      "scopes": ["read:users", "write:projects"]
    }
  }
}
```

### Policy Configuration

- `name` <code className="text-green-600">&lt;string&gt;</code> - The name of your policy instance. This is used as a reference in your routes.
- `policyType` <code className="text-green-600">&lt;string&gt;</code> - The identifier of the policy. This is used by the Zuplo UI. Value should be `jwt-scopes-inbound`.
- `handler.export` <code className="text-green-600">&lt;string&gt;</code> - The name of the exported type. Value should be `JWTScopeValidationInboundPolicy`.
- `handler.module` <code className="text-green-600">&lt;string&gt;</code> - The module containing the policy. Value should be `$import(@zuplo/runtime)`.
- `handler.options` <code className="text-green-600">&lt;object&gt;</code> - The options for this policy. [See Policy Options](#policy-options) below.

### Policy Options

The options for this policy are specified below. All properties are optional unless specifically marked as required.

- `scopes` **(required)** <code className="text-green-600">&lt;string[]&gt;</code> - An array of of JWT scopes.

## Using the Policy

Read more about [how policies work](/articles/policies)
