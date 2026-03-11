# Source: https://redocly.com/docs/realm/content/api-docs/openapi-extensions/x-hide-replay.md

# OpenAPI extension: `x-hideReplay`

Replay lets users make API request from your documentation, to quickly and easily try the experience.
Use `x-hideReplay` to turn off replay for one operation, removing the "Try It" button.

## Location

Use the `x-hideReplay` extension in an Operation declaration.

## Options

| Option | Type | Description |
|  --- | --- | --- |
| x-hideReplay | boolean | Hides the Replay for the operation on which it was set to `true`. |


## Examples

The following example shows how to disable Replay on the `ExamplePath` operation.


```yaml
paths:
  /example:
    get:
      summary: Example operation
      description: Example description
      operationId: examplePath
      responses: [...]
      parameters: [...]
      x-hideReplay: true
```

This operation will have complete documentation, but without interactive features.

## Resources

- **[Show extensions configuration](/docs/realm/config/openapi/show-extensions)** - Control which extensions are included in your API reference documentation for optimal presentation
- **[Mock server configuration](/docs/realm/config/mock-server)** - Configure mock server settings used by Replay for API testing and demonstration
- **[OpenAPI configuration settings](/docs/realm/config/openapi)** - Complete reference for all available OpenAPI configuration options and customization settings
- **[Supported OpenAPI extensions](/docs/realm/content/api-docs/openapi-extensions)** - Complete list of all OpenAPI extensions supported by Redocly for enhanced API documentation