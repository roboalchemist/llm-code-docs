# Source: https://docs.xano.com/xano-features/metadata-api/instance_api/retrieve_all_functions_in_a_workspace_with_optional_filtering_and_pagination.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Retrieve all functions in a workspace with optional filtering and pagination

> Retrieve all functions in a workspace with optional filtering and pagination



## OpenAPI

````yaml xano-features/metadata-api/metadata_api_instance.json get /workspace/{workspace_id}/function
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
  /workspace/{workspace_id}/function:
    get:
      tags:
        - function
      summary: >-
        Retrieve all functions in a workspace with optional filtering and
        pagination
      description: >-
        Retrieve all functions in a workspace with optional filtering and
        pagination

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
        - name: branch
          in: query
          description: ''
          required: false
          schema:
            type: string
            default: ''
        - name: include_draft
          in: query
          description: ''
          required: false
          schema:
            type: boolean
            default: false
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
        - name: search
          in: query
          description: ''
          required: false
          schema:
            type: string
            default: ''
        - name: sort
          in: query
          description: ''
          required: false
          schema:
            type: string
            enum:
              - created_at
              - updated_at
              - name
            default: created_at
        - name: order
          in: query
          description: ''
          required: false
          schema:
            type: string
            enum:
              - asc
              - desc
            default: desc
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