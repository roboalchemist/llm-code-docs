# Source: https://redocly.com/docs/realm/config/openapi/hide-replay.md

# `hideReplay`

The `hideReplay` configuration option allows you to control the visibility of the `Try it` buttons associated with API requests.

For example, you might want to hide the `Try it` button in your public API documentation, and make it visible only on your internal website.

The hideReplay  is not available in Redoc Community Edition.

## Options

| Option | Type | Description |
|  --- | --- | --- |
| hideReplay | boolean | Hide the `Replay` component that allows users to interactively send requests to an API.
Defaults to `false`. |


## Examples

The following example hides the `Replay` component from the API reference documentation.


```yaml redocly.yaml
openapi:
  hideReplay: true
```

## Resources

- **[Replay API explorer](https://redocly.com/docs/end-user/test-apis-replay)** - Learn about the interactive API testing features and capabilities used in API reference documentation
- **[OpenAPI configuration](/docs/realm/config/openapi)** - Complete guide to OpenAPI configuration options for customizing API reference documentation
- **[OpenAPI Specification](https://spec.openapis.org/oas/latest.html)** - Official OpenAPI Specification documentation for understanding API description standards
- **[OpenAPI visual reference](https://redocly.com/learn/openapi/openapi-visual-reference)** - Visual guide to OpenAPI specification structure and Replay button customization
- **[Configuration options](/docs/realm/config)** - Explore other project configuration options for comprehensive documentation customization