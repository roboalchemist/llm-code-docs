# Source: https://www.zuplo.com/docs/policies/graphql-disable-introspection-inbound.md

# GraphQL Disable Introspection Policy

Prevent GraphQL introspection queries on your API to enhance security in
production environments. This policy blocks any attempt to discover your schema
structure through introspection with a `403 Forbidden` response.

With this policy, you'll benefit from:

- **Enhanced API Security**: Hide your GraphQL schema structure from potential
  attackers
- **Selective Protection**: Block introspection only for requests passing
  through Zuplo
- **Production-Ready**: Implement security best practices for GraphQL in
  production
- **Zero Configuration**: Works immediately without any additional setup
- **Development Flexibility**: Keep introspection enabled in development
  environments

## Configuration

The configuration shows how to configure the policy in the 'policies.json' document.

```json title="config/policies.json"
{
  "name": "my-graphql-disable-introspection-inbound-policy",
  "policyType": "graphql-disable-introspection-inbound",
  "handler": {
    "export": "GraphQLDisableIntrospectionInboundPolicy",
    "module": "$import(@zuplo/graphql)",
    "options": {}
  }
}
```

### Policy Configuration

- `name` <code className="text-green-600">&lt;string&gt;</code> - The name of your policy instance. This is used as a reference in your routes.
- `policyType` <code className="text-green-600">&lt;string&gt;</code> - The identifier of the policy. This is used by the Zuplo UI. Value should be `graphql-disable-introspection-inbound`.
- `handler.export` <code className="text-green-600">&lt;string&gt;</code> - The name of the exported type. Value should be `GraphQLDisableIntrospectionInboundPolicy`.
- `handler.module` <code className="text-green-600">&lt;string&gt;</code> - The module containing the policy. Value should be `$import(@zuplo/graphql)`.
- `handler.options` <code className="text-green-600">&lt;object&gt;</code> - The options for this policy. [See Policy Options](#policy-options) below.

### Policy Options

The options for this policy are specified below. All properties are optional unless specifically marked as required.

## Using the Policy

This policy blocks GraphQL introspection queries, which are used to discover the
schema structure of your GraphQL API. Introspection is a powerful feature in
development but can expose sensitive information about your API in production
environments.

### How It Works

The policy examines each GraphQL request and checks if it contains introspection
queries by looking for the presence of `__schema` or `__type` fields in the
query. If an introspection query is detected, the policy returns a
`403 Forbidden` response with the message "Introspection queries are not
allowed".

### Policy Configuration

This policy requires no configuration options. Simply add it to your route's
inbound policies:

```json
{
  "name": "disable-introspection",
  "policyType": "graphql-disable-introspection-inbound",
  "handler": {
    "export": "GraphQLDisableIntrospectionInboundPolicy",
    "module": "$import(@zuplo/graphql)"
  }
}
```

### Usage Examples

#### Applying to a GraphQL Endpoint

Add the policy to your GraphQL route:

```json
{
  "paths": {
    "/graphql": {
      "post": {
        "x-zuplo-route": {
          "policies": {
            "inbound": ["disable-introspection", "rate-limit"]
          },
          "handler": {
            "export": "graphqlHandler",
            "module": "$import(./handlers/graphql)"
          }
        }
      }
    }
  }
}
```

### Security Considerations

- It's recommended to disable introspection in production environments while
  keeping it enabled in development for tooling support
- This policy only blocks introspection queries that pass through Zuplo - you
  can still keep introspection enabled for direct access to your GraphQL server
  during development
- Consider combining this policy with authentication policies to further secure
  your GraphQL API
- While this policy blocks standard introspection queries, it's still important
  to implement proper authorization controls for your GraphQL resolvers

Read more about [how policies work](/articles/policies)
