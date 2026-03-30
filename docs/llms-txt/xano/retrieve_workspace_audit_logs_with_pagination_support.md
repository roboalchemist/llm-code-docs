# Source: https://docs.xano.com/xano-features/metadata-api/instance_api/retrieve_workspace_audit_logs_with_pagination_support.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Retrieve workspace audit logs with pagination support

> Retrieve workspace audit logs with pagination support



## OpenAPI

````yaml xano-features/metadata-api/metadata_api_instance.json get /workspace/{workspace_id}/audit_log
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
  /workspace/{workspace_id}/audit_log:
    get:
      tags:
        - audit logs
      summary: Retrieve workspace audit logs with pagination support
      description: |-
        Retrieve workspace audit logs with pagination support
        <br /><br />
        <b>Authentication:</b> required
        <br /><br />
        <b>Required API Scope:</b>
        Workspace Log: Read
      parameters:
        - name: workspace_id
          in: path
          description: ''
          required: true
          schema:
            type: integer
            format: int64
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
        - name: include_data
          in: query
          description: ''
          required: false
          schema:
            type: boolean
            default: false
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