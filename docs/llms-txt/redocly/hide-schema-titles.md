# Source: https://redocly.com/docs/realm/config/openapi/hide-schema-titles.md

# `hideSchemaTitles`

By default, users can see schema field **title** properties.

The `hideSchemaTitles` option allows the schema field **title** to be hidden.


```yaml redocly.yaml
  schema:
    type: 'object'
    properties:
      name:
        title: Title
        type: string
        description: hooray
```

## Options

| Option | Type | Description |
|  --- | --- | --- |
| hideSchemaTitles | boolean | Hides the schema title next to the type.
Defaults to `false`. |


## Examples

The following example hides the schema **title** properties:


```yaml redocly.yaml
openapi:
  hideSchemaTitles: true
```

## Resources

- **[OpenAPI configuration](/docs/realm/config/openapi)** - Complete guide to OpenAPI configuration options for customizing API reference documentation
- **[OpenAPI Specification](https://spec.openapis.org/oas/latest.html)** - Official OpenAPI Specification documentation for understanding API description standards
- **[OpenAPI visual reference](https://redocly.com/learn/openapi/openapi-visual-reference)** - Visual guide to OpenAPI specification structure and schema title customization
- **[Configuration options](/docs/realm/config)** - Explore other project configuration options for comprehensive documentation customization