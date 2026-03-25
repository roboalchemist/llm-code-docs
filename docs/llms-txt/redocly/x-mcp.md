# Source: https://redocly.com/docs/realm/content/api-docs/openapi-extensions/x-mcp.md

# OpenAPI extension: `x-mcp`

Beta feature
This feature is currently experimental and may be subject to changes.

Use `x-mcp` to document MCP (Model Context Protocol) servers for consumers.

## Location

The `x-mcp` extension can be added to Root Object.
The root is the outer most level of the OpenAPI description.

## Options

| Option | Type | Description |
|  --- | --- | --- |
| x-mcp | [MCP object](#mcp-object) | MCP server description and configuration. |


### MCP object

| Option | Type | Description |
|  --- | --- | --- |
| protocolVersion | string | **REQUIRED.** The MCP protocol version supported by the server. |
| servers | [ [Server Object](https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.0.md#serverObject) ] | A list of server objects used to add one or more target endpoints for the MCP server. |
| capabilities | [Capabilities object](#capabilities-object) | Server capabilities including supported features like logging, prompts, resources, and tools. |
| tools | [ [Tool object](#tool-object) ] | Array of tools provided by the MCP server. |
| resources | [ [Resource object](#resource-object) ] | Array of resources provided by the MCP server. |
| prompts | [ [Prompt object](#prompt-object) ] | Prompt capabilities configuration with optional `listChanged` boolean property. |


### Capabilities object

| Option | Type | Description |
|  --- | --- | --- |
| logging | object | Logging capabilities configuration.
Empty object indicates basic logging support. |
| prompts | object | Prompt capabilities configuration with optional `listChanged` boolean property. |
| resources | object | Resource capabilities configuration with optional `subscribe` and `listChanged` boolean properties. |
| tools | object | Tool capabilities configuration with optional `listChanged` boolean property. |


### Tool object

| Option | Type | Description |
|  --- | --- | --- |
| name | string | **REQUIRED.** The name of the tool. |
| title | string | Title of the tool. |
| description | string | **REQUIRED.** Description of what the tool does. |
| tags | [ string ] | Tags for the tool. |
| inputSchema | object | JSON Schema describing the expected input parameters for the tool. |
| outputSchema | object | string | JSON Schema describing the tool's output, or a reference to a schema component. |
| security | [ object ] | Security requirements for the tool, following OpenAPI security scheme format. |


### Resource object

| Option | Type | Description |
|  --- | --- | --- |
| name | string | **REQUIRED.** The name of the resource. |
| description | string | Description of the resource. |
| uri | string | URI template for accessing the resource. |
| mimeType | string | MIME type of the resource content. |


### Prompt object

| Option | Type | Description |
|  --- | --- | --- |
| name | string | **REQUIRED.** The name of the prompt. |
| title | string | Title of the prompt. |
| description | string | Description of the prompt. |
| arguments | [ [Argument object](#argument-object) ] | Array of arguments for the prompt. |


### Argument object

| Option | Type | Description |
|  --- | --- | --- |
| name | string | **REQUIRED.** The name of the argument. |
| description | string | Description of the argument. |
| required | boolean | Whether the argument is required. |


## Examples

### `x-mcp` example

Metadata keys can be any string.
The values can be any primitive type, or a list of strings.

The following is an example of an `x-mcp` described within an OpenAPI description file:


```yaml api-clients-mcp.yaml
openapi: 3.2.0
info:
  version: 1.0.0
  title: API Clients MCP
  license:
    name: MIT
servers:
  - url: http://localhost:8080/mcp

paths: {} # no paths

x-mcp:
  protocolVersion: '2025-06-18'
  capabilities:
    logging: {}
    prompts:
      listChanged: true
    resources:
      subscribe: true
    tools:
      listChanged: true
  tools:
    # this is the output of the list/tools call to the MCP
    - name: clients/get
      description: Get a list of clients with all scopes in a service domain.
      inputSchema:
        type: object
        properties:
          clientId:
            type: string
            description: The ID of the client to get.
      outputSchema:
        $ref: '#/components/schemas/Client'
      # we added the OAuth2 security scheme
      security:
        - OAuth2:
            scopes:
              read: Read access
    - name: clients/list
      description: Get a list of clients with all scopes in a service domain.
      inputSchema:
        type: object
        properties:
          paginationToken:
            type: string
            description: The pagination token to get the next page of clients.
      outputSchema:
        type: object
        properties:
          clients:
            type: array
            items:
              $ref: '#/components/schemas/Client'
          paginationToken:
            type: string
            description: The pagination token to get the next page of clients.
  resources: []

components:
  securitySchemes:
    OAuth2:
      type: oauth2
      flows:
        clientCredentials:
          tokenUrl: http://localhost:8080/mcp/token
          scopes:
            read: Read access
            write: Write access
  schemas:
    Client:
      type: object
      properties:
        clientId:
          type: number
          description: The ID of the client.
        scopes:
          type: array
          items:
            type: string
          description: The scopes of the client.
      required:
        - clientId
        - scopes
```

The data is presented similar to the following screenshot:

Example MCP docs
## Resources

- **[Supported OpenAPI extensions](/docs/realm/content/api-docs/openapi-extensions)** - Complete list of all OpenAPI extensions supported by Redocly for enhanced API documentation