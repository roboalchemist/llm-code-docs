# Source: https://docs.xano.com/xano-features/metadata-api/instance_api/update_an_existing_data_sources_label_and_color_properties.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Update an existing data source's label and color properties

> Update an existing data source's label and color properties



## OpenAPI

````yaml xano-features/metadata-api/metadata_api_instance.json put /workspace/{workspace_id}/datasource/{label}
openapi: 3.0.0
info:
  title: Xano Metadata API (beta)
  description: >-
    The <a href="https://docs.xano.com/xano-features/metadata-api"
    target="_blank">Metadata API</a>

    is currently in <strong>beta</strong> and is the next
      evolution of the Developer API. It provides support
    to programatically manage your Xano instance and uses Access Tokens to

    control access.
  version: 0.0.1
servers:
  - url: https://x8ki-letl-twmt.n7.xano.io/api:meta
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