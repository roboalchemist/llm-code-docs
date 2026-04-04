# Source: https://redocly.com/docs/realm/config/graphql/show-built-in-directives.md

# `showBuiltInDirectives`

Built-in directives:

- skip
- include
- deprecated
- specifiedBy
- oneOf


## Options

| Option | Type | Description |
|  --- | --- | --- |
| showBuiltInDirectives | boolean | Display built-in GraphQL directives in the UI.
Default: `false`. |


## Examples

Enable built-in directives:


```yaml redocly.yaml
graphql:
  showBuiltInDirectives: true
```

## Resources

- **[GraphQL configuration](/docs/realm/config/graphql)** - Complete configuration reference for GraphQL docs
- **[GraphQL](https://graphql.org/)** - Official GraphQL specification and documentation