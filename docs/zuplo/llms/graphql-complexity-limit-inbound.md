# Source: https://www.zuplo.com/docs/policies/graphql-complexity-limit-inbound.md

# GraphQL Complexity Limit Policy

This policy allows you to add a limit for the depth and a limit for the
complexity of a GraphQL query.

## Configuration

The configuration shows how to configure the policy in the 'policies.json' document.

```json title="config/policies.json"
{
  "name": "my-graphql-complexity-limit-inbound-policy",
  "policyType": "graphql-complexity-limit-inbound",
  "handler": {
    "export": "GraphQLComplexityLimitInboundPolicy",
    "module": "$import(@zuplo/graphql)",
    "options": {
      "useComplexityLimit": {
        "complexityLimit": 10
      },
      "useDepthLimit": {
        "ignore": []
      }
    }
  }
}
```

### Policy Configuration

- `name` <code className="text-green-600">&lt;string&gt;</code> - The name of your policy instance. This is used as a reference in your routes.
- `policyType` <code className="text-green-600">&lt;string&gt;</code> - The identifier of the policy. This is used by the Zuplo UI. Value should be `graphql-complexity-limit-inbound`.
- `handler.export` <code className="text-green-600">&lt;string&gt;</code> - The name of the exported type. Value should be `GraphQLComplexityLimitInboundPolicy`.
- `handler.module` <code className="text-green-600">&lt;string&gt;</code> - The module containing the policy. Value should be `$import(@zuplo/graphql)`.
- `handler.options` <code className="text-green-600">&lt;object&gt;</code> - The options for this policy. [See Policy Options](#policy-options) below.

### Policy Options

The options for this policy are specified below. All properties are optional unless specifically marked as required.

- `useComplexityLimit` **(required)** <code className="text-green-600">&lt;object&gt;</code> - No description available.
  - `complexityLimit` <code className="text-green-600">&lt;number&gt;</code> - The maximum complexity a query is allowed to have.
  - `endpointUrl` <code className="text-green-600">&lt;string&gt;</code> - The endpoint URL to use for the complexity calculation.
- `useDepthLimit` **(required)** <code className="text-green-600">&lt;object&gt;</code> - No description available.
  - `depthLimit` <code className="text-green-600">&lt;number&gt;</code> - The maximum depth a query is allowed to have.
  - `ignore` <code className="text-green-600">&lt;string[]&gt;</code> - The fields to ignore when calculating the depth of a query.

## Using the Policy

### Depth Limit

Limit the depth a GraphQL query is allowed to query for.

- **maxDepth** - Number of levels a GraphQL query is allowed to query for.

This allows you to limit the depth of a GraphQL query. This is useful to prevent
DoS attacks on your GraphQL server.

```
{
  # Level 0
  me {
    # Level 1
    name
    friends {
      # Level 2
      name
      friends {
        # Level 3
        name
        # ...
      }
    }
  }
}
```

### Complexity Limit

Example:

- **maxComplexity** - Maximum complexity allowed for a query.

```
{
  me {
    name  # Complexity +1
    age   # Complexity +1
    email # Complexity +1
    friends {
      name   # Complexity +1
      height # Complexity +1
    }
  }
}
# Total complexity = 5
```

Read more about [how policies work](/articles/policies)
