# Source: https://docs.xano.com/xano-features/metadata-api/instance_api/search_table_records_with_advanced_filtering_and_sorting_options.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Search table records with advanced filtering and sorting options

> Search table records with advanced filtering and sorting options



## OpenAPI

````yaml xano-features/metadata-api/metadata_api_instance.json post /workspace/{workspace_id}/table/{table_id}/content/search
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
  /workspace/{workspace_id}/table/{table_id}/content/search:
    post:
      tags:
        - table / content
      summary: Search table records with advanced filtering and sorting options
      description: |-
        Search table records with advanced filtering and sorting options
        <br /><br />
        <b>Authentication:</b> required
        <br /><br />
        <b>Required API Scope:</b>
        Workspace Content: Read
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
                page:
                  type: integer
                  format: int64
                  description: ''
                  default: 1
                per_page:
                  type: integer
                  format: int64
                  description: ''
                  default: 50
                sort:
                  type: object
                  description: ''
                search:
                  type: object
                  description: ''
              example:
                page: 1
                per_page: 50
                sort:
                  id: desc
                search: []
          multipart/form-data:
            schema:
              type: object
              properties:
                page:
                  type: integer
                  format: int64
                  description: ''
                  default: 1
                per_page:
                  type: integer
                  format: int64
                  description: ''
                  default: 50
                sort:
                  type: object
                  description: ''
                search:
                  type: object
                  description: ''
              example:
                page: 1
                per_page: 50
                sort:
                  id: desc
                search: []
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