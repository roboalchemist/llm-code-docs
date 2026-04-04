# Source: https://docs.xano.com/api-reference/static-host/retrieve-builds-for-a-static-host.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Retrieve builds for a static host

> Retrieve builds for a static host
<br /><br />
<b>Authentication:</b> required



## OpenAPI

````yaml apispec_meta_instance.json get /workspace/{workspace_id}/static_host/{static_host}/build
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
  /workspace/{workspace_id}/static_host/{static_host}/build:
    get:
      tags:
        - static host
      summary: Retrieve builds for a static host
      description: |-
        Retrieve builds for a static host
        <br /><br />
        <b>Authentication:</b> required
      operationId: >-
        Xano Metadata
        API/workspace/{workspace_id}/static_host/{static_host}/build|GET
      parameters:
        - name: workspace_id
          in: path
          description: ''
          required: true
          schema:
            type: integer
            format: int64
        - name: static_host
          in: path
          description: ''
          required: true
          schema:
            type: string
        - name: page
          in: query
          description: ''
          required: false
          schema:
            type: integer
            format: int64
            default: 1
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
                        name:
                          type: string
                          description: ''
                        description:
                          type: string
                          description: ''
                        canonical:
                          type: string
                          description: ''
                        file_count:
                          type: integer
                          format: int64
                          description: ''
                        file_bytes:
                          type: integer
                          format: int64
                          description: ''
                        original:
                          type: string
                          description: ''
                        type:
                          type: string
                          description: ''
                        status:
                          type: string
                          description: ''
                          default: pending
                        log:
                          type: string
                          description: ''
                        static_host:
                          type: object
                          properties:
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