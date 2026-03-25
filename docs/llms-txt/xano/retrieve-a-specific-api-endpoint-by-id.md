# Source: https://docs.xano.com/api-reference/api-group-api/retrieve-a-specific-api-endpoint-by-id.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Retrieve a specific API endpoint by ID

> Retrieve a specific API endpoint by ID
<br /><br />
<b>Authentication:</b> required



## OpenAPI

````yaml apispec_meta_instance.json get /workspace/{workspace_id}/apigroup/{apigroup_id}/api/{api_id}
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
    get:
      tags:
        - api group / api
      summary: Retrieve a specific API endpoint by ID
      description: |-
        Retrieve a specific API endpoint by ID
        <br /><br />
        <b>Authentication:</b> required
      operationId: >-
        Xano Metadata
        API/workspace/{workspace_id}/apigroup/{apigroup_id}/api/{api_id}|GET
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
        - name: include_draft
          in: query
          description: ''
          required: false
          schema:
            type: boolean
            default: false
        - name: include_xanoscript
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
                    default: API Test
                  description:
                    type: string
                    description: ''
                    default: My APIs description
                  docs:
                    type: string
                    description: ''
                    default: Documentation
                  guid:
                    type: string
                    description: ''
                    default: YE1fwVhQ-enRlc6Sb42Gqru58-0
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
                  auth:
                    type: object
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
                    default: GET
                  input:
                    type: array
                    items:
                      type: object
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