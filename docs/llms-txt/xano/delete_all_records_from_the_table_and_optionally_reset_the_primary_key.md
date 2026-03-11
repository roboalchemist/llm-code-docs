# Source: https://docs.xano.com/xano-features/metadata-api/instance_api/delete_all_records_from_the_table_and_optionally_reset_the_primary_key.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete all records from the table and optionally reset the primary key

> Delete all records from the table and optionally reset the primary key



## OpenAPI

````yaml xano-features/metadata-api/metadata_api_instance.json delete /workspace/{workspace_id}/table/{table_id}/truncate
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
  /workspace/{workspace_id}/table/{table_id}/truncate:
    delete:
      tags:
        - table / content
      summary: Delete all records from the table and optionally reset the primary key
      description: |-
        Delete all records from the table and optionally reset the primary key
        <br /><br />
        <b>Authentication:</b> required
        <br /><br />
        <b>Required API Scope:</b>
        Workspace Content: Delete
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
        - name: x-data-source
          in: header
          description: ''
          required: false
          schema:
            type: string
            default: live
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                reset:
                  type: boolean
                  description: ''
              required:
                - reset
          multipart/form-data:
            schema:
              type: object
              properties:
                reset:
                  type: boolean
                  description: ''
              required:
                - reset
      responses:
        '200':
          description: Success!
          content:
            application/json:
              schema:
                type: object
                description: ''
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