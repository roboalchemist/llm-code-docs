# Source: https://docs.xano.com/xano-features/metadata-api/instance_api/search_middleware_request_history_using_advanced_filters_and_custom_sorting_options.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Search middleware request history using advanced filters and custom sorting options

> Search middleware request history using advanced filters and custom sorting options



## OpenAPI

````yaml xano-features/metadata-api/metadata_api_instance.json post /workspace/{workspace_id}/middleware_history/search
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
  /workspace/{workspace_id}/middleware_history/search:
    post:
      tags:
        - request history
      summary: >-
        Search middleware request history using advanced filters and custom
        sorting options
      description: >-
        Search middleware request history using advanced filters and custom
        sorting options

        <br /><br />

        <b>Authentication:</b> required

        <br /><br />

        <b>Required API Scope:</b>

        Workspace Request History: Read
      parameters:
        - name: workspace_id
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
                branch:
                  type: string
                  description: ''
                middleware_id:
                  type: integer
                  format: int64
                  description: ''
                query_id:
                  type: integer
                  format: int64
                  description: ''
                function_id:
                  type: integer
                  format: int64
                  description: ''
                task_id:
                  type: integer
                  format: int64
                  description: ''
                search:
                  type: object
                  description: ''
                sort:
                  type: object
                  description: ''
                include_output:
                  type: boolean
                  description: ''
              example:
                page: 1
                per_page: 50
                branch: null
                middleware_id: null
                sort:
                  created_at: desc
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
                branch:
                  type: string
                  description: ''
                middleware_id:
                  type: integer
                  format: int64
                  description: ''
                query_id:
                  type: integer
                  format: int64
                  description: ''
                function_id:
                  type: integer
                  format: int64
                  description: ''
                task_id:
                  type: integer
                  format: int64
                  description: ''
                search:
                  type: object
                  description: ''
                sort:
                  type: object
                  description: ''
                include_output:
                  type: boolean
                  description: ''
              example:
                page: 1
                per_page: 50
                branch: null
                middleware_id: null
                sort:
                  created_at: desc
                search: []
      responses:
        '200':
          description: Success!
          content:
            application/json:
              schema:
                type: object
                properties:
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
                  items:
                    type: array
                    items:
                      type: object
                      properties:
                        id:
                          type: integer
                          format: int64
                          description: ''
                          default: 1
                        created_at:
                          type: string
                          format: timestamptz
                          description: ''
                          default: 2023-04-12 18:34:01+0000
                        duration:
                          type: number
                          description: ''
                          default: 0.025
                        input:
                          type: object
                          description: ''
                          default:
                            page: 1
                        workspace_id:
                          type: integer
                          format: int64
                          description: ''
                        branch:
                          type: string
                          description: ''
                          default: v1
                        middleware_id:
                          type: integer
                          format: int64
                          description: ''
                        query_id:
                          type: integer
                          format: int64
                          description: ''
                        function_id:
                          type: integer
                          format: int64
                          description: ''
                        task_id:
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