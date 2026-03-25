# Source: https://redocly.com/docs/realm/config/openapi/max-displayed-enum-values.md

# `maxDisplayedEnumValues`

The `maxDisplayedEnumValues` displays only the specified number of enum values.
The remaining values are hidden in an expandable area.
By default 10 values are displayed which is ideal for usability.

## Options

| Option | Type | Description |
|  --- | --- | --- |
| maxDisplayedEnumValues | number | Sets the number of enum values to display.
Default value: `10`. |


## Examples

The following example displays three enum values for each enum field, any further values are available in an expandable section:


```yaml redocly.yaml
openapi:
  maxDisplayedEnumValues: 3
```

## Resources

- **[OpenAPI configuration](/docs/realm/config/openapi)** - Complete guide to OpenAPI configuration options for customizing API reference documentation
- **[OpenAPI Specification](https://spec.openapis.org/oas/latest.html)** - Official OpenAPI Specification documentation for understanding API description standards
- **[OpenAPI visual reference](https://redocly.com/learn/openapi/openapi-visual-reference)** - Visual guide to OpenAPI specification structure and enum value display configuration
- **[Configuration options](/docs/realm/config)** - Explore other project configuration options for comprehensive documentation customization