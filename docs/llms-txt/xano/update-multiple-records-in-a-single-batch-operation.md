# Source: https://docs.xano.com/api-reference/table-content/update-multiple-records-in-a-single-batch-operation.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Update multiple records in a single batch operation

> The request body should contain an array of **items**, where each item represents a row to be updated. For each row, provide the **row_id** and **updates** array that specifies the columns (**path**) to update and the new values (**value**).
The example below is assuming that the table being modified has a column labeled *name*.

<br /><br />
<b>Required API Scope:</b>
Workspace Content: Update



## OpenAPI

````yaml apispec_meta_instance.json post /workspace/{workspace_id}/table/{table_id}/content/bulk/patch
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
  /workspace/{workspace_id}/table/{table_id}/content/bulk/patch:
    post:
      tags:
        - table / content
      summary: Update multiple records in a single batch operation
      description: >-
        The request body should contain an array of **items**, where each item
        represents a row to be updated. For each row, provide the **row_id** and
        **updates** array that specifies the columns (**path**) to update and
        the new values (**value**).

        The example below is assuming that the table being modified has a column
        labeled *name*.


        <br /><br />

        <b>Required API Scope:</b>

        Workspace Content: Update
      operationId: >-
        Xano Metadata
        API/workspace/{workspace_id}/table/{table_id}/content/bulk/patch|POST
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
                items:
                  type: array
                  items:
                    type: object
                    properties:
                      updates:
                        type: object
                        description: ''
                      row_id:
                        type: string
                    required:
                      - row_id
              example:
                items:
                  - row_id: 1
                    updates:
                      name: test name
          multipart/form-data:
            schema:
              type: object
              properties:
                items:
                  type: array
                  items:
                    type: object
                    properties:
                      updates:
                        type: object
                        description: ''
                      row_id:
                        type: string
                    required:
                      - row_id
              example:
                items:
                  - row_id: 1
                    updates:
                      name: test name
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