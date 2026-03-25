# Source: https://docs.xano.com/api-reference/request-history/retrieve-api-request-history.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Retrieve API request history

> Retrieve API request history
<br /><br />
<b>Authentication:</b> required
<br /><br />
<b>Required API Scope:</b>
Workspace Request History: Read



## OpenAPI

````yaml apispec_meta_instance.json get /workspace/{workspace_id}/request_history
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
  /workspace/{workspace_id}/request_history:
    get:
      tags:
        - request history
      summary: Retrieve API request history
      description: |-
        Retrieve API request history
        <br /><br />
        <b>Authentication:</b> required
        <br /><br />
        <b>Required API Scope:</b>
        Workspace Request History: Read
      operationId: Xano Metadata API/workspace/{workspace_id}/request_history|GET
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
        - name: branch
          in: query
          description: ''
          required: false
          schema:
            type: string
            default: ''
        - name: apigroup_id
          in: query
          description: ''
          required: false
          schema:
            type: integer
            format: int64
            default: 0
        - name: query_id
          in: query
          description: ''
          required: false
          schema:
            type: integer
            format: int64
            default: 0
        - name: include_output
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
                        status:
                          type: integer
                          format: int64
                          description: ''
                          default: 200
                        verb:
                          type: string
                          description: ''
                          default: GET
                        uri:
                          type: string
                          description: ''
                          default: https://x1234-4567-8901.n7.xano.com/api:meta
                        input:
                          type: object
                          description: ''
                          default:
                            page: 1
                        request_headers:
                          type: array
                          items:
                            type: string
                            description: ''
                          default:
                            - 'Accept: application/json'
                        response_headers:
                          type: array
                          items:
                            type: string
                            description: ''
                          default:
                            - 'Content-Type: application/json'
                        workspace_id:
                          type: integer
                          format: int64
                          description: ''
                        branch_id:
                          type: integer
                          format: int64
                          description: ''
                        api_id:
                          type: integer
                          format: int64
                          description: ''
                        query_id:
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