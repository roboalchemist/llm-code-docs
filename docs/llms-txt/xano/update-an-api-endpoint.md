# Source: https://docs.xano.com/api-reference/api-group-api/update-an-api-endpoint.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Update an API endpoint

> Update API endpoint code, settings, and authentication rules
<br /><br />
<b>Authentication:</b> required



## OpenAPI

````yaml apispec_meta_instance.json put /workspace/{workspace_id}/apigroup/{apigroup_id}/api/{api_id}
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
  /workspace/{workspace_id}/apigroup/{apigroup_id}/api/{api_id}:
    put:
      tags:
        - api group / api
      summary: Update an API endpoint
      description: |-
        Update API endpoint code, settings, and authentication rules
        <br /><br />
        <b>Authentication:</b> required
      operationId: >-
        Xano Metadata
        API/workspace/{workspace_id}/apigroup/{apigroup_id}/api/{api_id}|PUT
      parameters:
        - name: workspace_id
          in: path
          description: ''
          required: true
          schema:
            type: integer
            format: int64
        - name: apigroup_id
          in: path
          description: ''
          required: true
          schema:
            type: integer
            format: int64
        - name: api_id
          in: path
          description: ''
          required: true
          schema:
            type: integer
            format: int64
        - name: publish
          in: query
          description: ''
          required: false
          schema:
            type: boolean
            default: true
        - name: include_xanoscript
          in: query
          description: ''
          required: false
          schema:
            type: boolean
            default: false
      requestBody:
        content:
          text/x-xanoscript:
            schema:
              type: string
              example: |
                query foo verb=GET {
                  input {
                    int score
                  }
                  stack {
                    var $x1 {
                      value = $input.score + 1
                    }
                  }
                  response = $x1
                }
          multipart/form-data:
            schema:
              type: object
              properties:
                name:
                  type: string
                  description: ''
                description:
                  type: string
                  description: ''
                docs:
                  type: string
                  description: ''
                verb:
                  type: string
                  description: ''
                  enum:
                    - GET
                    - POST
                    - DELETE
                    - PUT
                    - PATCH
                    - HEAD
                auth:
                  type: object
                  description: ''
                tag:
                  type: array
                  items:
                    type: string
                    description: ''
                  nullable: true
                publish:
                  type: boolean
                  description: ''
                  default: true
                include_xanoscript:
                  type: boolean
                  description: ''
                cache:
                  type: object
                  properties:
                    active:
                      type: boolean
                      description: ''
                    ttl:
                      type: integer
                      format: int64
                      description: ''
                      default: 3600
                    input:
                      type: boolean
                      description: ''
                      default: true
                    auth:
                      type: boolean
                      description: ''
                      default: true
                    datasource:
                      type: boolean
                      description: ''
                      default: true
                    ip:
                      type: boolean
                      description: ''
                    headers:
                      type: array
                      items:
                        type: string
                        description: ''
                    env:
                      type: array
                      items:
                        type: string
                        description: ''
              required:
                - name
                - description
                - verb
          application/json:
            schema:
              type: object
              properties:
                name:
                  type: string
                  description: ''
                description:
                  type: string
                  description: ''
                docs:
                  type: string
                  description: ''
                verb:
                  type: string
                  description: ''
                  enum:
                    - GET
                    - POST
                    - DELETE
                    - PUT
                    - PATCH
                    - HEAD
                auth:
                  type: object
                  description: ''
                tag:
                  type: array
                  items:
                    type: string
                    description: ''
                  nullable: true
                publish:
                  type: boolean
                  description: ''
                  default: true
                include_xanoscript:
                  type: boolean
                  description: ''
                cache:
                  type: object
                  properties:
                    active:
                      type: boolean
                      description: ''
                    ttl:
                      type: integer
                      format: int64
                      description: ''
                      default: 3600
                    input:
                      type: boolean
                      description: ''
                      default: true
                    auth:
                      type: boolean
                      description: ''
                      default: true
                    datasource:
                      type: boolean
                      description: ''
                      default: true
                    ip:
                      type: boolean
                      description: ''
                    headers:
                      type: array
                      items:
                        type: string
                        description: ''
                    env:
                      type: array
                      items:
                        type: string
                        description: ''
              required:
                - name
                - description
                - verb
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