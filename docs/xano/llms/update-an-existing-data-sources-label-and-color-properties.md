# Source: https://docs.xano.com/api-reference/workspace-datasource/update-an-existing-data-sources-label-and-color-properties.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Update an existing data source's label and color properties

> Update an existing data source's label and color properties
<br /><br />
<b>Authentication:</b> required
<br /><br />
<b>Required API Scope:</b>
Instance Workspace: Update



## OpenAPI

````yaml apispec_meta_instance.json put /workspace/{workspace_id}/datasource/{label}
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
  /workspace/{workspace_id}/datasource/{label}:
    put:
      tags:
        - workspace / datasource
      summary: Update an existing data source's label and color properties
      description: |-
        Update an existing data source's label and color properties
        <br /><br />
        <b>Authentication:</b> required
        <br /><br />
        <b>Required API Scope:</b>
        Instance Workspace: Update
      operationId: Xano Metadata API/workspace/{workspace_id}/datasource/{label}|PUT
      parameters:
        - name: workspace_id
          in: path
          description: ''
          required: true
          schema:
            type: integer
            format: int64
        - name: label
          in: path
          description: ''
          required: true
          schema:
            type: string
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                color:
                  type: string
                  description: ''
                  default: '#ebc346'
          multipart/form-data:
            schema:
              type: object
              properties:
                color:
                  type: string
                  description: ''
                  default: '#ebc346'
      responses:
        '200':
          description: Success!
          content:
            application/json:
              schema:
                type: object
                properties:
                  color:
                    type: string
                    description: ''
                    default: '#008000'
                  label:
                    type: string
                    description: ''
                    default: live
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