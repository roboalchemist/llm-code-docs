# Source: https://docs.xano.com/xano-features/metadata-api/instance_api/delete_multiple_records_by_their_ids_in_a_single_operation.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete multiple records by their IDs in a single operation

> The request body should contain an array of **row_ids**, where each id identifies a row to be deleted.



## OpenAPI

````yaml xano-features/metadata-api/metadata_api_instance.json post /workspace/{workspace_id}/table/{table_id}/content/bulk/delete
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
  /workspace/{workspace_id}/table/{table_id}/content/bulk/delete:
    post:
      tags:
        - table / content
      summary: Delete multiple records by their IDs in a single operation
      description: >-
        The request body should contain an array of **row_ids**, where each id
        identifies a row to be deleted.

        <br /><br />

        <b>Required API Scope:</b>

        Workspace Content: Delete
      parameters:
        - name: workspace_id
          in: path
          description: ''
          required: true
          schema:
            type: string
        - name: table_id
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
              properties:
                row_ids:
                  type: array
                  items:
                    type: string
              example:
                row_ids:
                  - 1
          multipart/form-data:
            schema:
              type: object
              properties:
                row_ids:
                  type: array
                  items:
                    type: string
              example:
                row_ids:
                  - 1
      responses:
        '200':
          description: Success!
          content:
            application/json:
              schema:
                type: object
                properties:
                  success:
                    type: array
                    items:
                      type: string
                      description: ''
                  success_total:
                    type: integer
                    format: int64
                    description: ''
                  error:
                    type: array
                    items:
                      type: string
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