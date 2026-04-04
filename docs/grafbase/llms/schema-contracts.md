# Source: https://grafbase.com/docs/gateway/security/schema-contracts.md

# Schema Contracts

Schema contracts are a powerful feature that allows you to define and enforce a specific subset of the schema either statically or dynamically.

Schema contracts rely on a contracts extension to modify the schema. The marketplace provides a [tag](/extensions/tag) extension which defines the following directive:

```graphql
directive @tag(
  name: String!
) repeatable on FIELD_DEFINITION | INTERFACE | OBJECT | UNION | ARGUMENT_DEFINITION | SCALAR | ENUM | ENUM_VALUE | INPUT_OBJECT | INPUT_FIELD_DEFINITION
```

The directive can be used in any subgraph with the following import:

```graphql
extend schema
  @link(url: "https://grafbase.com/extensions/tag/1.0.0", import: ["@tag"])

type Accounts @tag(name: "private") {
  id: ID!
}
```

In addition to the `@tag` directive, a contract key must be defined to include or exclude certain tags. The [tag](/extensions/tag) accepts a JSON string as follows:

```json
{
  "includedTags": ["public"],
  "excludedTags": ["private"]
}
```

The contract key can be defined either statically in the [configuration](https://grafbase.com/docs/gateway/configuration/graph.md) with:

```toml
# grafbase.toml
[graph.contracts]
default_key = '{"includedTags": ["public"], "excludedTags": ["private"]}'
```

Or it can be dynamically defined by the [on_request](https://docs.rs/grafbase-sdk/latest/grafbase_sdk/trait.HooksExtension.html#method.on_request) hook ([guide](/guides/implementing-gateway-hooks)) for each individual request. Schema contracts will be cached by their contract key in the gateway.

In addition contracts extensions can also modify the subgraph URLs.

## Custom schema contracts

[tag](/extensions/tag) is just one possibility of contracts extension. You can create your own with the [grafbase-sdk](https://docs.rs/grafbase-sdk/latest/grafbase_sdk/trait.ContractsExtension.html).