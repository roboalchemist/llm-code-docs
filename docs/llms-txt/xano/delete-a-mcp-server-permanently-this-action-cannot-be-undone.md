# Source: https://docs.xano.com/api-reference/mcp-server/delete-a-mcp-server-permanently-this-action-cannot-be-undone.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete a MCP server permanently. This action cannot be undone

> Delete a MCP server permanently. This action cannot be undone
<br /><br />
<b>Authentication:</b> required



## OpenAPI

````yaml apispec_meta_instance.json delete /workspace/{workspace_id}/mcp_server/{mcp_server_id}
openapi: 3.0.0
info:
  title: Xano Metadata API
  description: >-
    The <a href="https://docs.xano.com/xano-features/metadata-api"
    target="_blank">Metadata API</a> provides support

    to programatically manage your Xano instance and uses Access Tokens to

    control access.
  version: 0.0.1
servers:
  - url: https://your-xano-instance.xano.io/api:meta
security: []
paths:
  /workspace/{workspace_id}/mcp_server/{mcp_server_id}:
    delete:
      tags:
        - mcp server
      summary: Delete a MCP server permanently. This action cannot be undone
      description: |-
        Delete a MCP server permanently. This action cannot be undone
        <br /><br />
        <b>Authentication:</b> required
      operationId: >-
        Xano Metadata
        API/workspace/{workspace_id}/mcp_server/{mcp_server_id}|DELETE
      parameters:
        - name: workspace_id
          in: path
          description: ''
          required: true
          schema:
            type: integer
            format: int64
        - name: mcp_server_id
          in: path
          description: ''
          required: true
          schema:
            type: integer
            format: int64
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties: {}
          multipart/form-data:
            schema:
              type: object
              properties: {}
      responses:
        '200':
          description: Success!
          content:
            application/json:
              schema:
                type: object
                properties: {}
        '400':
          description: Input Error. Check the request payload for issues.
        '401':
          description: Unauthorized
        '403':
          description: >-
            Access denied. Additional privileges are needed access the requested
            resource.
        '404':
          description: Not Found. The requested resource does not exist.
        '429':
          description: Rate Limited. Too many requests.
        '500':
          description: Unexpected error
      security:
        - bearerAuth: []
components:
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT

````

Built with [Mintlify](https://mintlify.com).