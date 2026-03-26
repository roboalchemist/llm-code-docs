# Source: https://www.zuplo.com/docs/policies/graphql-introspection-filter-outbound.md

# GraphQL Introspection Filter Policy

Filters GraphQL introspection responses to exclude specific types and fields.

This policy intercepts GraphQL introspection query responses and removes configured types and fields from the schema. Useful for hiding internal types or sensitive fields from the public schema.

## Configuration

The configuration shows how to configure the policy in the 'policies.json' document.

```json title="config/policies.json"
{
  "name": "my-graphql-introspection-filter-outbound-policy",
  "policyType": "graphql-introspection-filter-outbound",
  "handler": {
    "export": "GraphQLIntrospectionFilterOutboundPolicy",
    "module": "$import(@zuplo/graphql)",
    "options": {
      "excludeTypeFields": {
        "User": ["password", "email"],
        "Query": ["adminUsers"]
      },
      "excludeTypes": "UserInternal"
    }
  }
}
```

### Policy Configuration

- `name` <code className="text-green-600">&lt;string&gt;</code> - The name of your policy instance. This is used as a reference in your routes.
- `policyType` <code className="text-green-600">&lt;string&gt;</code> - The identifier of the policy. This is used by the Zuplo UI. Value should be `graphql-introspection-filter-outbound`.
- `handler.export` <code className="text-green-600">&lt;string&gt;</code> - The name of the exported type. Value should be `GraphQLIntrospectionFilterOutboundPolicy`.
- `handler.module` <code className="text-green-600">&lt;string&gt;</code> - The module containing the policy. Value should be `$import(@zuplo/graphql)`.
- `handler.options` <code className="text-green-600">&lt;object&gt;</code> - The options for this policy. [See Policy Options](#policy-options) below.

### Policy Options

The options for this policy are specified below. All properties are optional unless specifically marked as required.

- `excludeTypes` <code className="text-green-600">&lt;string[]&gt;</code> - GraphQL Types to exclude from the schema (exact match).
- `excludeTypeFields` <code className="text-green-600">&lt;object&gt;</code> - Fields on specific GraphQL Types to exclude.

## Using the Policy

This policy filters GraphQL introspection responses to selectively hide types
and fields from your schema. It intercepts introspection query responses and
removes configured types and fields, allowing you to expose a subset of your
GraphQL schema to external clients (like MCP servers or AI agents).

### How It Works

The policy processes responses from GraphQL introspection queries, which are
typically made by GraphQL clients and development tools to discover your API's
schema structure. When an introspection response is detected (containing
`__schema` as a top level key), the policy filters out:

- Entire types specified in `excludeTypes`
- Specific fields on types specified in `excludeTypeFields`

This allows you to hide internal types, sensitive fields, or admin-only
operations from public consumers while keeping them available for internal use.

### Policy Configuration

Configure the policy with optional `excludeTypes` and `excludeTypeFields`
options:

```json
{
  "name": "filter-introspection",
  "policyType": "graphql-introspection-filter-outbound",
  "handler": {
    "export": "GraphQLIntrospectionFilterOutboundPolicy",
    "module": "$import(@zuplo/graphql)",
    "options": {
      "excludeTypes": ["UserInternal", "AdminType", "DebugInfo"],
      "excludeTypeFields": {
        "User": ["password", "ssn"],
        "Query": ["adminUsers", "debugInfo"]
      }
    }
  }
}
```

### Configuration Options

- **excludeTypes** (optional): Array of GraphQL type names to completely remove
  from the schema. Types must match exactly.

- **excludeTypeFields** (optional): Object mapping type names to arrays of field
  names to remove. Only specified fields on the given types will be filtered.

### Usage Examples

#### Hiding Internal Types

Remove internal implementation types from the public schema:

```json
{
  "name": "hide-internal-types",
  "policyType": "graphql-introspection-filter-outbound",
  "handler": {
    "export": "GraphQLIntrospectionFilterOutboundPolicy",
    "module": "$import(@zuplo/graphql)",
    "options": {
      "excludeTypes": ["InternalMetadata", "DebugInfo", "SystemStatus"]
    }
  }
}
```

#### Filtering Sensitive Fields

Hide sensitive fields like passwords and admin operations:

```json
{
  "name": "filter-sensitive-fields",
  "policyType": "graphql-introspection-filter-outbound",
  "handler": {
    "export": "GraphQLIntrospectionFilterOutboundPolicy",
    "module": "$import(@zuplo/graphql)",
    "options": {
      "excludeTypeFields": {
        "User": ["password", "ssn", "creditCard"],
        "Query": ["adminUsers", "systemDiagnostics"],
        "Mutation": ["deleteAllUsers", "resetDatabase"]
      }
    }
  }
}
```

#### Complete Example with URL Rewrite

Apply filtering on a route that forwards to a GraphQL endpoint:

```json
{
  "paths": {
    "/graphql": {
      "x-zuplo-path": {
        "pathMode": "open-api"
      },
      "post": {
        "summary": "GraphQL API",
        "x-zuplo-route": {
          "corsPolicy": "anything-goes",
          "handler": {
            "export": "urlRewriteHandler",
            "module": "$import(@zuplo/runtime)",
            "options": {
              "rewritePattern": "https://api.example.com/graphql"
            }
          },
          "policies": {
            "outbound": ["filter-introspection"]
          }
        },
        "responses": {}
      }
    }
  }
}
```

### Important Notes

- This policy only filters introspection responses - it does not enforce
  authorization on the actual GraphQL operations. You must still implement
  proper authorization in your GraphQL resolvers.
- If a client tries to query a filtered field or type directly, that will be
  handled by your GraphQL server's validation, not by this policy.
- The policy only processes successful (200 OK) JSON responses that contain
  `__schema` in the response body.
- If the response cannot be parsed as JSON or is not an introspection response,
  the original response is returned unchanged.
- Non-introspection GraphQL queries and mutations pass through without
  modification.

### Security Considerations

- Filtering introspection is a form of security through obscurity - always
  implement proper authentication and authorization at the resolver level
- Consider combining this policy with authentication policies to control who can
  access your GraphQL endpoint
- Use this policy to reduce information disclosure about your API's internal
  structure, but don't rely on it as your only security measure
- Keep in mind that determined attackers may still discover hidden fields
  through other means

Read more about [how policies work](/articles/policies)
