# Source: https://www.zuplo.com/docs/policies/composite-inbound.md

# Composite Inbound (Group Policies) Policy

Create reusable groups of policies that can be applied together across multiple
routes. This policy allows you to organize and manage collections of policies by
referencing them by their `name`.

With this policy, you'll benefit from:

- **Simplified Management**: Group related policies together for easier
  maintenance
- **Consistent Security**: Apply the same set of policies across multiple routes
- **Reduced Configuration**: Minimize repetitive policy definitions in your
  routes
- **Modular Design**: Create logical policy groupings based on function or
  security level
- **Streamlined Updates**: Change policy configurations in one place and apply
  everywhere

## Configuration

The configuration shows how to configure the policy in the 'policies.json' document.

```json title="config/policies.json"
{
  "name": "my-composite-inbound-policy",
  "policyType": "composite-inbound",
  "handler": {
    "export": "CompositeInboundPolicy",
    "module": "$import(@zuplo/runtime)",
    "options": {
      "policies": ["policy1", "policy2"]
    }
  }
}
```

### Policy Configuration

- `name` <code className="text-green-600">&lt;string&gt;</code> - The name of your policy instance. This is used as a reference in your routes.
- `policyType` <code className="text-green-600">&lt;string&gt;</code> - The identifier of the policy. This is used by the Zuplo UI. Value should be `composite-inbound`.
- `handler.export` <code className="text-green-600">&lt;string&gt;</code> - The name of the exported type. Value should be `CompositeInboundPolicy`.
- `handler.module` <code className="text-green-600">&lt;string&gt;</code> - The module containing the policy. Value should be `$import(@zuplo/runtime)`.
- `handler.options` <code className="text-green-600">&lt;object&gt;</code> - The options for this policy. [See Policy Options](#policy-options) below.

### Policy Options

The options for this policy are specified below. All properties are optional unless specifically marked as required.

- `policies` <code className="text-green-600">&lt;string[]&gt;</code> - The list of policy references (beware circular references).

## Using the Policy

This policy allows you to create groups of other policies for easy reuse across
multiple routes. Policies are referenced by their `name` as defined in your
policies.json file.

### Policy Configuration

The Composite Inbound policy requires a list of policy names to include in the
group:

```json
{
  "policies": [
    "rate-limit-policy",
    "api-key-auth-policy",
    "request-validation-policy"
  ]
}
```

Each policy name in the array must correspond to a valid policy defined in your
policies.json file.

### Usage Examples

#### Creating a Security Group

You can create a security policy group that combines authentication and rate
limiting:

```json
{
  "name": "security-group",
  "handler": {
    "export": "CompositeInboundPolicy",
    "module": "$import(@zuplo/runtime)",
    "options": {
      "policies": ["api-key-auth", "rate-limit"]
    }
  }
}
```

#### Creating a Validation Group

You can create a validation policy group that combines schema validation and
custom validation logic:

```json
{
  "name": "validation-group",
  "handler": {
    "export": "CompositeInboundPolicy",
    "module": "$import(@zuplo/runtime)",
    "options": {
      "policies": ["json-schema-validator", "custom-validation-policy"]
    }
  }
}
```

### Important Considerations

- Be careful not to create circular references, which can cause your gateway to
  fail
- Policies will be executed in the order they are listed in the `policies` array
- Each policy in the composite group must be properly configured in your
  policies.json file
- The composite policy can be used in route definitions just like any other
  policy

Read more about [how policies work](/articles/policies)
