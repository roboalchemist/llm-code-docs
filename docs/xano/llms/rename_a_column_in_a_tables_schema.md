# Source: https://docs.xano.com/xano-features/metadata-api/instance_api/rename_a_column_in_a_tables_schema.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Rename a column in a table's schema

> Rename a column in a table's schema



## OpenAPI

````yaml xano-features/metadata-api/metadata_api_instance.json post /workspace/{workspace_id}/table/{table_id}/schema/rename
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
  /workspace/{workspace_id}/table/{table_id}/schema/rename:
    post:
      tags:
        - table / schema
      summary: Rename a column in a table's schema
      description: |-
        Rename a column in a table's schema
        <br /><br />
        <b>Authentication:</b> required
        <br /><br />
        <b>Required API Scope:</b>
        Workspace Database: Update
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
                new_name:
                  type: string
                  description: ''
                old_name:
                  type: string
                  description: ''
              required:
                - new_name
                - old_name
              example:
                new_name: new_field
                old_name: old_field
          multipart/form-data:
            schema:
              type: object
              properties:
                new_name:
                  type: string
                  description: ''
                old_name:
                  type: string
                  description: ''
              required:
                - new_name
                - old_name
              example:
                new_name: new_field
                old_name: old_field
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