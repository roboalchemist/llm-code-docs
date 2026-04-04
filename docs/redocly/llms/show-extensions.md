# Source: https://redocly.com/docs/realm/config/openapi/show-extensions.md

# `showExtensions`

The `showExtensions` option displays specification extensions ('x-' fields).
Extensions used by Redoc are ignored.
The value can be boolean or an array of strings with names of extensions to display.
When used as boolean and set to `true`, all specification extensions are shown.

Custom extensions are rendered only in the request details section and in individual field details; they do not appear elsewhere in the UI.

## Options

| Option | Type | Description |
|  --- | --- | --- |
| showExtensions | [string] | boolean | Specify which specification extensions ('x-' fields) to display, or use `true` to show them all.
Default value: `false`. |


## Examples

The following example show all specification extensions:


```yaml redocly.yaml
openapi:
  showExtensions: true
```

## Resources

- **[OpenAPI configuration](/docs/realm/config/openapi)** - Complete guide to OpenAPI configuration options for customizing API reference documentation
- **[Specification extensions](/docs/realm/content/api-docs/openapi-extensions)** - Complete list of OpenAPI specification extensions supported in Redoc for enhanced documentation
- **[OpenAPI Specification](https://spec.openapis.org/oas/latest.html)** - Official OpenAPI Specification documentation for understanding API description standards
- **[Configuration options](/docs/realm/config)** - Explore other project configuration options for comprehensive documentation customization