# Source: https://www.zuplo.com/docs/policies/composite-outbound.md

# Composite Outbound (Group Policies) Policy

The Composite outbound policy allows you to create groups of other policies, for
easy reuse across multiple routes. Other policies are referenced by their
`name`.

Be careful not to create circular references which can cause your gateway to
fail.

## Configuration

The configuration shows how to configure the policy in the 'policies.json' document.

```json title="config/policies.json"
{
  "name": "my-composite-outbound-policy",
  "policyType": "composite-outbound",
  "handler": {
    "export": "CompositeOutboundPolicy",
    "module": "$import(@zuplo/runtime)",
    "options": {
      "policies": ["policy1", "policy2"]
    }
  }
}
```

### Policy Configuration

- `name` <code className="text-green-600">&lt;string&gt;</code> - The name of your policy instance. This is used as a reference in your routes.
- `policyType` <code className="text-green-600">&lt;string&gt;</code> - The identifier of the policy. This is used by the Zuplo UI. Value should be `composite-outbound`.
- `handler.export` <code className="text-green-600">&lt;string&gt;</code> - The name of the exported type. Value should be `CompositeOutboundPolicy`.
- `handler.module` <code className="text-green-600">&lt;string&gt;</code> - The module containing the policy. Value should be `$import(@zuplo/runtime)`.
- `handler.options` <code className="text-green-600">&lt;object&gt;</code> - The options for this policy. [See Policy Options](#policy-options) below.

### Policy Options

The options for this policy are specified below. All properties are optional unless specifically marked as required.

- `policies` <code className="text-green-600">&lt;string[]&gt;</code> - The list of policy references (beware circular references).

## Using the Policy

Read more about [how policies work](/articles/policies)
