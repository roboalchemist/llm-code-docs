# Source: https://redocly.com/docs/realm/config/graphql/show-built-in-scalars.md

# `showBuiltInScalars`

Built-in scalars:

- Int
- Float
- String
- Boolean
- ID


## Options

| Option | Type | Description |
|  --- | --- | --- |
| showBuiltInScalars | boolean | Display built-in GraphQL scalar types in the UI.
Default: `false`. |


## Examples

Enable built-in scalars:


```yaml redocly.yaml
graphql:
  showBuiltInScalars: true
```

## Resources

- **[GraphQL configuration](/docs/realm/config/graphql)** - Complete configuration reference for GraphQL docs
- **[GraphQL](https://graphql.org/)** - Official GraphQL specification and documentation