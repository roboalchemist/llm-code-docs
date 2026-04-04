# Source: https://redocly.com/docs/realm/config/openapi/generated-samples-max-depth.md

# `generatedSamplesMaxDepth`

The `generatedSamplesMaxDepth` option controls how many schema levels automatically generated for payload samples.
The default is 8 which works well for most APIs, but you can adjust it if necessary for your use case.

## Options

| Option | Type | Description |
|  --- | --- | --- |
| generatedSamplesMaxDepth | number | Set the number of levels to generate payload samples.
Default value is `8`. |


## Examples

The following example produces automatically generated payload samples with 3 levels:


```yaml redocly.yaml
openapi:
  generatedSamplesMaxDepth: 3
```

## Resources

- **[OpenAPI configuration](/docs/realm/config/openapi)** - Complete guide to OpenAPI configuration options for customizing API reference documentation
- **[OpenAPI Specification](https://spec.openapis.org/oas/latest.html)** - Official OpenAPI Specification documentation for understanding API description standards
- **[OpenAPI visual reference](https://redocly.com/learn/openapi/openapi-visual-reference)** - Visual guide to OpenAPI specification structure and sample generation depth configuration
- **[Configuration options](/docs/realm/config)** - Explore other project configuration options for comprehensive documentation customization