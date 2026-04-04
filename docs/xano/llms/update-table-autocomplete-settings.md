# Source: https://docs.xano.com/api-reference/table/update-table-autocomplete-settings.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Update table autocomplete settings

> update workspace table's autocomplete
<br /><br />
<b>Authentication:</b> required
<br /><br />
<b>Required API Scope:</b>
Workspace Database: Update



## OpenAPI

````yaml apispec_meta_instance.json put /workspace/{workspace_id}/table/{table_id}/autocomplete
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
  /workspace/{workspace_id}/table/{table_id}/autocomplete:
    put:
      tags:
        - table
      summary: Update table autocomplete settings
      description: |-
        update workspace table's autocomplete
        <br /><br />
        <b>Authentication:</b> required
        <br /><br />
        <b>Required API Scope:</b>
        Workspace Database: Update
      operationId: >-
        Xano Metadata
        API/workspace/{workspace_id}/table/{table_id}/autocomplete|PUT
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
                autocomplete:
                  type: array
                  items:
                    type: object
                    properties:
                      name:
                        type: string
                        description: ''
                    required:
                      - name
              example:
                autocomplete:
                  - name: id
          multipart/form-data:
            schema:
              type: object
              properties:
                autocomplete:
                  type: array
                  items:
                    type: object
                    properties:
                      name:
                        type: string
                        description: ''
                    required:
                      - name
              example:
                autocomplete:
                  - name: id
      responses:
        '200':
          description: Success!
          content:
            application/json:
              schema:
                type: object
                properties:
                  id:
                    type: string
                  autocomplete:
                    type: string
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