# Source: https://docs.xano.com/xano-features/metadata-api/instance_api/update_a_specific_record_by_id.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Update a specific record by ID

> Each table has unique schema, which means that the request body should be updated with the schema relevant to the table being used.



## OpenAPI

````yaml xano-features/metadata-api/metadata_api_instance.json put /workspace/{workspace_id}/table/{table_id}/content/{content_id}
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
  /workspace/{workspace_id}/table/{table_id}/content/{content_id}:
    put:
      tags:
        - table / content
      summary: Update a specific record by ID
      description: >-
        Each table has unique schema, which means that the request body should
        be updated with the schema relevant to the table being used.

        The example below is assuming that the table has a column labeled
        "name".


        <br /><br />

        <b>Required API Scope:</b>

        Workspace Content: Update
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
        - name: content_id
          in: path
          description: ''
          required: true
          schema:
            type: string
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
              description: ''
              example:
                name: test name
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