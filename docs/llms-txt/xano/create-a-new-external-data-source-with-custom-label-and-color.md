# Source: https://docs.xano.com/api-reference/workspace-datasource/create-a-new-external-data-source-with-custom-label-and-color.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Create a new external data source with custom label and color

> Create a new external data source with custom label and color
<br /><br />
<b>Authentication:</b> required
<br /><br />
<b>Required API Scope:</b>
Instance Workspace: Create



## OpenAPI

````yaml apispec_meta_instance.json post /workspace/{workspace_id}/datasource
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
  /workspace/{workspace_id}/datasource:
    post:
      tags:
        - workspace / datasource
      summary: Create a new external data source with custom label and color
      description: |-
        Create a new external data source with custom label and color
        <br /><br />
        <b>Authentication:</b> required
        <br /><br />
        <b>Required API Scope:</b>
        Instance Workspace: Create
      operationId: Xano Metadata API/workspace/{workspace_id}/datasource|POST
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
                label:
                  type: string
                  description: ''
                color:
                  type: string
                  description: ''
                  default: '#ebc346'
              required:
                - label
          multipart/form-data:
            schema:
              type: object
              properties:
                label:
                  type: string
                  description: ''
                color:
                  type: string
                  description: ''
                  default: '#ebc346'
              required:
                - label
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