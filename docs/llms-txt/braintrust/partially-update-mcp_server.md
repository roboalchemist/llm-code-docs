# Source: https://braintrust.dev/docs/api-reference/mcpservers/partially-update-mcp_server.md

> ## Documentation Index
> Fetch the complete documentation index at: https://braintrust.dev/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Partially update mcp_server

> Partially update a mcp_server object. Specify the fields to update in the payload. Any object-type fields will be deep-merged with existing content. Currently we do not support removing fields or setting them to null.



## OpenAPI

````yaml openapi.yaml patch /v1/mcp_server/{mcp_server_id}
openapi: 3.1.1
info:
  version: 1.0.0
  title: Braintrust API
  description: >-
    API specification for the backend data server. The API is hosted globally at

    https://api.braintrust.dev or in your own environment.


    You can access the OpenAPI spec for this API at
    https://github.com/braintrustdata/braintrust-openapi.
  license:
    name: Apache 2.0
servers:
  - url: https://api.braintrust.dev
security:
  - bearerAuth: []
  - {}
paths:
  /v1/mcp_server/{mcp_server_id}:
    patch:
      tags:
        - McpServers
      summary: Partially update mcp_server
      description: >-
        Partially update a mcp_server object. Specify the fields to update in
        the payload. Any object-type fields will be deep-merged with existing
        content. Currently we do not support removing fields or setting them to
        null.
      operationId: patchMcpServerId
      parameters:
        - $ref: '#/components/parameters/McpServerIdParam'
      requestBody:
        description: Fields to update
        required: false
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/PatchMCPServer'
      responses:
        '200':
          description: Returns the mcp_server object
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/MCPServer'
        '400':
          description: >-
            The request was unacceptable, often due to missing a required
            parameter
          content:
            text/plain:
              schema:
                type: string
            application/json:
              schema:
                nullable: true
        '401':
          description: No valid API key provided
          content:
            text/plain:
              schema:
                type: string
            application/json:
              schema:
                nullable: true
        '403':
          description: The API key doesn’t have permissions to perform the request
          content:
            text/plain:
              schema:
                type: string
            application/json:
              schema:
                nullable: true
        '429':
          description: >-
            Too many requests hit the API too quickly. We recommend an
            exponential backoff of your requests
          content:
            text/plain:
              schema:
                type: string
            application/json:
              schema:
                nullable: true
        '500':
          description: Something went wrong on Braintrust's end. (These are rare.)
          content:
            text/plain:
              schema:
                type: string
            application/json:
              schema:
                nullable: true
      security:
        - bearerAuth: []
        - {}
components:
  parameters:
    McpServerIdParam:
      schema:
        $ref: '#/components/schemas/McpServerIdParam'
      required: true
      description: McpServer id
      name: mcp_server_id
      in: path
  schemas:
    PatchMCPServer:
      type: object
      properties:
        name:
          type: string
          nullable: true
          description: >-
            Name of the MCP server. Within a project, MCP server names are
            unique
        url:
          type: string
          nullable: true
          description: URL of the MCP server endpoint
        description:
          type: string
          nullable: true
          description: Textual description of the MCP server
    MCPServer:
      type: object
      properties:
        id:
          type: string
          format: uuid
          description: Unique identifier for the MCP server
        project_id:
          type: string
          format: uuid
          description: Unique identifier for the project that the MCP server belongs under
        user_id:
          type: string
          nullable: true
          format: uuid
          description: Identifies the user who created the MCP server
        created:
          type: string
          nullable: true
          format: date-time
          description: Date of MCP server creation
        deleted_at:
          type: string
          nullable: true
          format: date-time
          description: >-
            Date of MCP server deletion, or null if the MCP server is still
            active
        name:
          type: string
          description: >-
            Name of the MCP server. Within a project, MCP server names are
            unique
        description:
          type: string
          nullable: true
          description: Textual description of the MCP server
        url:
          type: string
          description: URL of the MCP server endpoint
      required:
        - id
        - project_id
        - name
        - url
    McpServerIdParam:
      type: string
      format: uuid
      description: McpServer id
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      bearerFormat: API key or JWT
      description: >-
        Most Braintrust endpoints are authenticated by providing your API key as
        a header `Authorization: Bearer [api_key]` to your HTTP request. You can
        create an API key in the Braintrust [organization settings
        page](https://www.braintrustdata.com/app/settings?subroute=api-keys).

````