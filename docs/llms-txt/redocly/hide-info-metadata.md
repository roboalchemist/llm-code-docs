# Source: https://redocly.com/docs/realm/config/openapi/hide-info-metadata.md

# `hideInfoMetadata`

If you include metadata for your APIs, either using the `info.x-metadata` extension or the `metadata` configuration option, that information is displayed in the API reference documentation.

The hideInfoMetadata  is not available in Redoc Community Edition.

Screenshot of API documentation where hideInfoMetadata option is set to false
To omit the metadata section from the API reference documentation, set the `hideInfoMetadata` option.

## Options

| Option | Type | Description |
|  --- | --- | --- |
| hideInfoMetadata | boolean | Optionally hide the **OpenAPI info metadata** section of the API reference page.
Default value is `false`. |


## Examples

The following example hides the `metadata` content from the API documentation.


```yaml redocly.yaml
openapi:
  hideInfoMetadata: true
```


```yaml openapi.yaml
openapi: 3.1.0
info:
  title: Redocly Museum API
  description: Imaginary, but delightful Museum API for interacting with museum services and information.
  Built with love by Redocly.
  version: 1.1.0
  x-metadata:
    createdAt: '2016-11-15T00:53:45.524Z'
    domain: fake-museum-example.com
...
```

Screenshot of API documentation where hideInfoMetadata is set to true
## Resources

- **[OpenAPI configuration](/docs/realm/config/openapi)** - Complete guide to OpenAPI configuration options for customizing API reference documentation
- **[OpenAPI Specification](https://spec.openapis.org/oas/latest.html)** - Official OpenAPI Specification documentation for understanding API description standards
- **[OpenAPI visual reference](https://redocly.com/learn/openapi/openapi-visual-reference)** - Visual guide to OpenAPI specification structure and info metadata customization
- **[Configuration options](/docs/realm/config)** - Explore other project configuration options for comprehensive documentation customization