# Source: https://redocly.com/docs/realm/content/api-docs/openapi-extensions/x-servers.md

# OpenAPI extension: `x-servers`

Compatibility warning
These specification extensions are supported only in OpenAPI 2.0.
For OpenAPI 3.0 and later, use the `servers` section.

Use `x-servers` in your OpenAPI 2.0 documents to define one or more target hosts for the API.

This specification extension provides compatibility via backporting from the OpenAPI 3.0 [`servers`](https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.0.md#serverObject) object.
It doesn't support templates.

## Location

Use the `x-servers` extension in the root OpenAPI object.

## Options

| Option | Type | Description |
|  --- | --- | --- |
| x-servers | [ [Server Object](https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.0.md#serverObject) ] | A list of server objects used to add one or more target hosts for the API. |


## Examples

The following example show how to adds development and staging hosts to OpenAPi description.


```yaml
swagger: '2.0'
x-servers:
  - url: https://development.example.com/v1
    description: Development server
  - url: https://staging.example.com/v1
    description: Staging server
```

## Resources

- **[Mock server configuration](/docs/realm/config/mock-server)** - Configure mock server settings to complement server definitions for API testing and development
- **[Show extensions configuration](/docs/realm/config/openapi/show-extensions)** - Control which extensions are included in your API reference documentation for optimal presentation
- **[OpenAPI configuration settings](/docs/realm/config/openapi)** - Complete reference for all available OpenAPI configuration options and customization settings
- **[Supported OpenAPI extensions](/docs/realm/content/api-docs/openapi-extensions)** - Complete list of all OpenAPI extensions supported by Redocly for enhanced API documentation