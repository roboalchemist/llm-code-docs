# Source: https://redocly.com/docs/realm/config/openapi/json-samples-expand-level.md

# `jsonSamplesExpandLevel`

The `jsonSamplesExpandLevel` option sets the default expand level for JSON payload samples (response and request body).
The maximum supported value is '+Infinity'.
It can also be configured as a string with the special value `all` that expands all levels.

## Options

| Option | Type | Description |
|  --- | --- | --- |
| jsonSamplesExpandLevel | number | string | Sets the default expand level for JSON payload samples.
Use `all` to expand all levels.
Default value is `2`. |


## Examples

The following example expands the JSON payload samples to a depth of five levels.


```yaml redocly.yaml
openapi:
  jsonSamplesExpandLevel: 5
```

## Resources

- **[OpenAPI configuration](/docs/realm/config/openapi)** - Complete guide to OpenAPI configuration options for customizing API reference documentation
- **[OpenAPI Specification](https://spec.openapis.org/oas/latest.html)** - Official OpenAPI Specification documentation for understanding API description standards
- **[OpenAPI visual reference](https://redocly.com/learn/openapi/openapi-visual-reference)** - Visual guide to OpenAPI specification structure and JSON sample expansion configuration
- **[Configuration options](/docs/realm/config)** - Explore other project configuration options for comprehensive documentation customization