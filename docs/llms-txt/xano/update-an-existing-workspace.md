# Source: https://docs.xano.com/api-reference/workspace/update-an-existing-workspace.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Update an existing workspace

> Update an existing workspace
<br /><br />
<b>Authentication:</b> required
<br /><br />
<b>Required API Scope:</b>
Instance Workspace: Update



## OpenAPI

````yaml apispec_meta_instance.json put /workspace/{workspace_id}
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
  /workspace/{workspace_id}:
    put:
      tags:
        - workspace
      summary: Update an existing workspace
      description: |-
        Update an existing workspace
        <br /><br />
        <b>Authentication:</b> required
        <br /><br />
        <b>Required API Scope:</b>
        Instance Workspace: Update
      operationId: Xano Metadata API/workspace/{workspace_id}|PUT
      parameters:
        - name: workspace_id
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
                description:
                  type: string
                  description: ''
                swagger:
                  type: boolean
                  description: ''
                documentation:
                  type: object
                  properties:
                    require_token:
                      type: boolean
                      description: ''
              example:
                name: Updated Workspace Name
                description: Updated description
          multipart/form-data:
            schema:
              type: object
              properties:
                name:
                  type: string
                  description: ''
                description:
                  type: string
                  description: ''
                swagger:
                  type: boolean
                  description: ''
                documentation:
                  type: object
                  properties:
                    require_token:
                      type: boolean
                      description: ''
              example:
                name: Updated Workspace Name
                description: Updated description
      responses:
        '200':
          description: Success!
          content:
            application/json:
              schema:
                type: object
                properties:
                  id:
                    type: integer
                    format: int64
                    description: ''
                    default: 1
                  name:
                    type: string
                    description: ''
                    default: My Workspace
                  description:
                    type: string
                    description: ''
                    default: My Workspace Description
                  branch:
                    type: string
                    description: ''
                    default: v1
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