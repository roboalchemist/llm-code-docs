# Source: https://docs.xano.com/xano-features/metadata-api/instance_api/update_api_endpoint_code_settings_and_authentication_rules.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Update API endpoint code, settings, and authentication rules

> Update API endpoint code, settings, and authentication rules



## OpenAPI

````yaml xano-features/metadata-api/metadata_api_instance.json put /workspace/{workspace_id}/apigroup/{apigroup_id}/api/{api_id}
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
  /workspace/{workspace_id}/apigroup/{apigroup_id}/api/{api_id}:
    put:
      tags:
        - api group / api
      summary: Update API endpoint code, settings, and authentication rules
      description: |-
        Update API endpoint code, settings, and authentication rules
        <br /><br />
        <b>Authentication:</b> required
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
                  response {
                    value = $x1
                  }
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