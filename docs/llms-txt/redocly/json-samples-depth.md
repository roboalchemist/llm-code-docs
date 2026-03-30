# Source: https://redocly.com/docs/realm/config/graphql/json-samples-depth.md

# `jsonSamplesDepth`

The `jsonSamplesDepth` option sets the default depth for rendering JSON payload samples for queries and responses.
Use this option to set the depth to a comfortable default value for the data structure of your API.

## Options

| Option | Type | Description |
|  --- | --- | --- |
| jsonSamplesDepth | number | Sets the default depth for rendering JSON payload samples.
The default value is `1`. |


## Examples

The following example sets the depth for JSON payload samples to five levels.


```yaml redocly.yaml
graphql:
  jsonSamplesDepth: 5
```

Using this setting, the samples will show up to five levels of nested payload data.

## Resources

- **[GraphQL](https://graphql.org/)** - Official GraphQL specification and documentation for understanding query language fundamentals
- **[GraphQL configuration](/docs/realm/config/graphql)** - Complete guide to GraphQL configuration options for customizing API reference documentation
- **[Samples max inline arguments](/docs/realm/config/graphql/samples-max-inline-args)** - Configure the maximum number of inline arguments for samples to complement JSON payload depth settings
- **[Field expand level](/docs/realm/config/graphql/field-expand-level)** - Set the maximum depth of the Return type in the middle panel for comprehensive data structure display