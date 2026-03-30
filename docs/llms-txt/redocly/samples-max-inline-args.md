# Source: https://redocly.com/docs/realm/config/graphql/samples-max-inline-args.md

# `samplesMaxInlineArgs`

The `samplesMaxInlineArgs` option sets how many arguments are shown inline in the query sample.
When there are more arguments than the configured value, every argument will be shown on its own line.

## Options

| Option | Type | Description |
|  --- | --- | --- |
| samplesMaxInlineArgs | number | Sets the maximum number of inline arguments for samples.
Default value is `2`. |


## Examples

The following example allows up to five inline arguments to be displayed in code samples.


```yaml redocly.yaml
graphql:
  samplesMaxInlineArgs: 5
```

For longer-named arguments, a lower setting may produce more readable samples.

## Resources

- **[GraphQL](https://graphql.org/)** - Official GraphQL specification and documentation for understanding query language fundamentals
- **[GraphQL configuration](/docs/realm/config/graphql)** - Complete guide to GraphQL configuration options for customizing API reference documentation
- **[JSON samples depth configuration](/docs/realm/config/graphql/json-samples-depth)** - Set the default expand level for JSON payload samples to complement inline argument display
- **[GraphQL configuration](/docs/realm/config/graphql)** - Complete guide to GraphQL configuration options for comprehensive API reference documentation customization