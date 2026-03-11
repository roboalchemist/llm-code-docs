# Source: https://docs.xano.com/api-reference/api-group/get-openapi-spec-for-an-api-group.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get OpenAPI spec for an API group

> Get the OpenAPI specification for an API group. Returns the complete Swagger JSON for all endpoints.
<br /><br />
<b>Authentication:</b> required
<br /><br />
<b>Required API Scope:</b>
Workspace Api: Read



## OpenAPI

````yaml apispec_meta_instance.json get /workspace/{workspace_id}/apigroup/{apigroup_id}/openapi
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
  /workspace/{workspace_id}/apigroup/{apigroup_id}/openapi:
    get:
      tags:
        - api group
      summary: Get OpenAPI spec for an API group
      description: >-
        Get the OpenAPI specification for an API group. Returns the complete
        Swagger JSON for all endpoints.

        <br /><br />

        <b>Authentication:</b> required

        <br /><br />

        <b>Required API Scope:</b>

        Workspace Api: Read
      operationId: >-
        Xano Metadata
        API/workspace/{workspace_id}/apigroup/{apigroup_id}/openapi|GET
      parameters:
        - name: workspace_id
          in: path
          description: ''
          required: true
          schema:
            type: integer
            format: int64
        - name: apigroup_id
          in: path
          description: ''
          required: true
          schema:
            type: integer
            format: int64
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