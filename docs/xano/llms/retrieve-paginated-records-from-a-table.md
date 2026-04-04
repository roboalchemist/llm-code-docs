# Source: https://docs.xano.com/api-reference/table-content/retrieve-paginated-records-from-a-table.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Retrieve paginated records from a table

> Retrieve paginated records from a table
<br /><br />
<b>Authentication:</b> required
<br /><br />
<b>Required API Scope:</b>
Workspace Content: Read



## OpenAPI

````yaml apispec_meta_instance.json get /workspace/{workspace_id}/table/{table_id}/content
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
  /workspace/{workspace_id}/table/{table_id}/content:
    get:
      tags:
        - table / content
      summary: Retrieve paginated records from a table
      description: |-
        Retrieve paginated records from a table
        <br /><br />
        <b>Authentication:</b> required
        <br /><br />
        <b>Required API Scope:</b>
        Workspace Content: Read
      operationId: Xano Metadata API/workspace/{workspace_id}/table/{table_id}/content|GET
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
        - name: page
          in: query
          description: ''
          required: false
          schema:
            type: integer
            format: int64
            default: 1
        - name: per_page
          in: query
          description: ''
          required: false
          schema:
            type: integer
            format: int64
            default: 50
      responses:
        '200':
          description: Success!
          content:
            application/json:
              schema:
                type: object
                properties:
                  items:
                    type: object
                    description: ''
                  itemsReceived:
                    type: integer
                    format: int64
                    description: ''
                  curPage:
                    type: integer
                    format: int64
                    description: ''
                  nextPage:
                    type: integer
                    format: int64
                    description: ''
                    nullable: true
                  prevPage:
                    type: integer
                    format: int64
                    description: ''
                    nullable: true
                  offset:
                    type: integer
                    format: int64
                    description: ''
                  perPage:
                    type: integer
                    format: int64
                    description: ''
                  itemsTotal:
                    type: integer
                    format: int64
                    description: ''
                  pageTotal:
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