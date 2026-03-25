# Source: https://redocly.com/docs/realm/config/openapi/sanitize.md

# `sanitize`

The `sanitize` option enables HTML/Markdown sanitization for the OpenAPI description.

## Options

| Option | Type | Description |
|  --- | --- | --- |
| sanitize | boolean | Sanitize HTML/Markdown to prevent [cross-site scripting (XSS) attacks](https://owasp.org/www-community/attacks/xss/).
Default value is `false`. |


## Examples

If set to `true`, the API description is considered untrusted and all HTML/Markdown is sanitized to prevent XSS.


```yaml redocly.yaml
openapi:
  sanitize: true
```

## Resources

- **[OpenAPI configuration](/docs/realm/config/openapi)** - Complete guide to OpenAPI configuration options for customizing API reference documentation
- **[OpenAPI Specification](https://spec.openapis.org/oas/latest.html)** - Official OpenAPI Specification documentation for understanding API description standards
- **[OpenAPI visual reference](https://redocly.com/learn/openapi/openapi-visual-reference)** - Visual guide to OpenAPI specification structure and HTML sanitization practices
- **[Configuration options](/docs/realm/config)** - Explore other project configuration options for comprehensive documentation customization