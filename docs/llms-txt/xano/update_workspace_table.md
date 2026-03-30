# Source: https://docs.xano.com/xano-features/metadata-api/instance_api/update_workspace_table.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# update workspace table

> update workspace table



## OpenAPI

````yaml xano-features/metadata-api/metadata_api_instance.json put /workspace/{workspace_id}/table/{table_id}
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
  /workspace/{workspace_id}/table/{table_id}:
    put:
      tags:
        - table
      summary: update workspace table
      description: |-
        update workspace table
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
        - name: table_id
          in: path
          description: ''
          required: true
          schema:
            type: integer
            format: int64
      requestBody:
        content:
          text/x-xanoscript:
            schema:
              type: string
              example: |
                table book {
                  schema {
                    int id
                    text title
                    text description
                  }
                  index = [
                    {type: "primary", field: [{name: "id"}]}
                  ]
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
                auth:
                  type: boolean
                  description: ''
                guid:
                  type: string
                  description: ''
                  nullable: true
                schema:
                  type: object
                  description: ''
                  nullable: true
                index:
                  type: object
                  description: ''
                  nullable: true
                tag:
                  type: array
                  items:
                    type: string
                    description: ''
                  nullable: true
                autocomplete:
                  type: array
                  items:
                    type: object
                    properties:
                      name:
                        type: string
                        description: ''
                    required:
                      - name
                  nullable: true
              example:
                name: table 123
                description: ''
                docs: ''
                auth: null
                guid: null
                schema: null
                index: null
                autocomplete: []
                tag: []
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
                auth:
                  type: boolean
                  description: ''
                guid:
                  type: string
                  description: ''
                  nullable: true
                schema:
                  type: object
                  description: ''
                  nullable: true
                index:
                  type: object
                  description: ''
                  nullable: true
                tag:
                  type: array
                  items:
                    type: string
                    description: ''
                  nullable: true
                autocomplete:
                  type: array
                  items:
                    type: object
                    properties:
                      name:
                        type: string
                        description: ''
                    required:
                      - name
                  nullable: true
              example:
                name: table 123
                description: ''
                docs: ''
                auth: null
                guid: null
                schema: null
                index: null
                autocomplete: []
                tag: []
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
                    default: Test Database
                  description:
                    type: string
                    description: ''
                    default: My test database description
                  docs:
                    type: string
                    description: ''
                    default: Documentation
                  guid:
                    type: string
                    description: ''
                    default: YE1fwVhQ-enRlc6Sb42Gqru58-0
                  auth:
                    type: boolean
                    description: ''
                    default: true
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