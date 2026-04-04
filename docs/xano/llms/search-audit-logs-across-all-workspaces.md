# Source: https://docs.xano.com/api-reference/audit-logs/search-audit-logs-across-all-workspaces.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Search audit logs across all workspaces

> search audit logs across all workspaces with support for complex filtering and sorting
<br /><br />
<b>Authentication:</b> required



## OpenAPI

````yaml apispec_meta_instance.json post /audit_log/search
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
  /audit_log/search:
    post:
      tags:
        - audit logs
      summary: Search audit logs across all workspaces
      description: >-
        search audit logs across all workspaces with support for complex
        filtering and sorting

        <br /><br />

        <b>Authentication:</b> required
      operationId: Xano Metadata API/audit_log/search|POST
      parameters: []
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
                include_data:
                  type: boolean
                  description: ''
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
                include_data:
                  type: boolean
                  description: ''
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
                    type: array
                    items:
                      type: object
                      properties:
                        id:
                          type: integer
                          format: int64
                          description: ''
                        created_at:
                          type: string
                          format: timestamptz
                          description: ''
                        updated_at:
                          type: string
                          format: timestamptz
                          description: ''
                        type:
                          type: string
                          description: ''
                        msg:
                          type: string
                          description: ''
                        label:
                          type: array
                          items:
                            type: string
                            description: ''
                        data:
                          type: object
                          description: ''
                          nullable: true
                        obj:
                          type: object
                          properties:
                            type:
                              type: string
                              description: ''
                            id:
                              type: integer
                              format: int64
                              description: ''
                        user:
                          type: object
                          properties:
                            id:
                              type: integer
                              format: int64
                              description: ''
                            email:
                              type: string
                              description: ''
                              format: email
                              nullable: true
                          nullable: true
                        workspace:
                          type: object
                          properties:
                            id:
                              type: integer
                              format: int64
                              description: ''
                            name:
                              type: string
                              description: ''
                          nullable: true
                        branch:
                          type: object
                          properties:
                            id:
                              type: integer
                              format: int64
                              description: ''
                            label:
                              type: string
                              description: ''
                              nullable: true
                          nullable: true
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