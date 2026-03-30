# Source: https://redocly.com/docs/realm/config/openapi/sort-required-props-first.md

# `sortRequiredPropsFirst`

By default, fields are rendered in the order they appear in the API description.

The `sortRequiredPropsFirst` option changes the order to display required fields first in each schema section.

## Options

| Option | Type | Description |
|  --- | --- | --- |
| sortRequiredPropsFirst | boolean | Sort the required schema properties before the optional ones.
Default value: `false`. |


## Examples

The following example configures Redoc to show required properties first:


```yaml redocly.yaml
openapi:
  sortRequiredPropsFirst: true
```

## Resources

- **[OpenAPI configuration](/docs/realm/config/openapi)** - Complete guide to OpenAPI configuration options for customizing API reference documentation
- **[OpenAPI Specification](https://spec.openapis.org/oas/latest.html)** - Official OpenAPI Specification documentation for understanding API description standards
- **[OpenAPI visual reference](https://redocly.com/learn/openapi/openapi-visual-reference)** - Visual guide to OpenAPI specification structure and property ordering principles
- **[Configuration options](/docs/realm/config)** - Explore other project configuration options for comprehensive documentation customization