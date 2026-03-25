# Source: https://docs.xano.com/api-reference/table/update-table-properties.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Update table properties

> Update table properties including name, description, tags, and authentication settings
<br /><br />
<b>Authentication:</b> required
<br /><br />
<b>Required API Scope:</b>
Workspace Database: Update



## OpenAPI

````yaml apispec_meta_instance.json put /workspace/{workspace_id}/table/{table_id}/meta
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
  /workspace/{workspace_id}/table/{table_id}/meta:
    put:
      tags:
        - table
      summary: Update table properties
      description: >-
        Update table properties including name, description, tags, and
        authentication settings

        <br /><br />

        <b>Authentication:</b> required

        <br /><br />

        <b>Required API Scope:</b>

        Workspace Database: Update
      operationId: Xano Metadata API/workspace/{workspace_id}/table/{table_id}/meta|PUT
      parameters:
        - name: workspace_id
          in: path
          description: ''
          required: true
          schema:
            type: integer
            format: int64
        - name: table_id
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
              properties:
                name:
                  type: string
                  description: ''
                  nullable: true
                description:
                  type: string
                  description: ''
                  nullable: true
                tag:
                  type: array
                  items:
                    type: string
                    description: ''
                  nullable: true
                auth:
                  type: boolean
                  description: ''
                  nullable: true
          multipart/form-data:
            schema:
              type: object
              properties:
                name:
                  type: string
                  description: ''
                  nullable: true
                description:
                  type: string
                  description: ''
                  nullable: true
                tag:
                  type: array
                  items:
                    type: string
                    description: ''
                  nullable: true
                auth:
                  type: boolean
                  description: ''
                  nullable: true
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
      deprecated: true
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