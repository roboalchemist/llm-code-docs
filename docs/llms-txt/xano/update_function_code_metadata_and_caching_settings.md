# Source: https://docs.xano.com/xano-features/metadata-api/instance_api/update_function_code_metadata_and_caching_settings.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Update function code, metadata, and caching settings

> Update function code, metadata, and caching settings



## OpenAPI

````yaml xano-features/metadata-api/metadata_api_instance.json put /workspace/{workspace_id}/function/{function_id}
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
  /workspace/{workspace_id}/function/{function_id}:
    put:
      tags:
        - function
      summary: Update function code, metadata, and caching settings
      description: |-
        Update function code, metadata, and caching settings
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
        - name: function_id
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
                function foo {
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
      responses:
        '200':
          description: Success!
          content:
            application/json:
              schema:
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
                    default: 2023-04-19 21:01:32+0000
                  updated_at:
                    type: string
                    format: timestamptz
                    description: ''
                    default: 2023-04-19 21:01:32+0000
                  name:
                    type: string
                    description: ''
                    default: Function Test
                  description:
                    type: string
                    description: ''
                    default: My functions description
                  docs:
                    type: string
                    description: ''
                    default: Documentation
                  guid:
                    type: string
                    description: ''
                    default: YE1fwVhQ-enRlc6Sb42Gqru58-0
                  branch:
                    type: string
                    description: ''
                    default: v1
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
                        default:
                          - ''
                      env:
                        type: array
                        items:
                          type: string
                          description: ''
                        default:
                          - ''
                  tag:
                    type: array
                    items:
                      type: string
                      description: ''
                    default:
                      - example tag
                  xanoscript:
                    type: object
                    properties:
                      status:
                        type: string
                        description: ''
                        enum:
                          - ok
                          - error
                      value:
                        type: string
                        description: ''
                      message:
                        type: string
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