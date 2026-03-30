# Source: https://docs.xano.com/xano-features/metadata-api/instance_api/create_a_new_scheduled_task_using_xanoscript.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Create a new scheduled task using XanoScript

> Create a new scheduled task using XanoScript



## OpenAPI

````yaml xano-features/metadata-api/metadata_api_instance.json post /workspace/{workspace_id}/task
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
  /workspace/{workspace_id}/task:
    post:
      tags:
        - task
      summary: Create a new scheduled task using XanoScript
      description: |-
        Create a new scheduled task using XanoScript
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
      requestBody:
        content:
          text/x-xanoscript:
            schema:
              type: string
              example: |
                task foo {
                  stack {
                    var $x1 {
                      value = $input.score + 1
                    }
                  }
                  schedule {
                    events = [{starts_on: 2025-07-25 20:00:12+0000, freq: 900}]
                  }
                }
          multipart/form-data:
            schema:
              type: object
              properties:
                branch:
                  type: string
                  description: ''
                name:
                  type: string
                  description: ''
                description:
                  type: string
                  description: ''
                docs:
                  type: string
                  description: ''
                datasource:
                  type: string
                  description: ''
                active:
                  type: boolean
                  description: ''
                tag:
                  type: array
                  items:
                    type: string
                    description: ''
                  nullable: true
              required:
                - name
                - description
                - datasource
                - active
          application/json:
            schema:
              type: object
              properties:
                branch:
                  type: string
                  description: ''
                name:
                  type: string
                  description: ''
                description:
                  type: string
                  description: ''
                docs:
                  type: string
                  description: ''
                datasource:
                  type: string
                  description: ''
                active:
                  type: boolean
                  description: ''
                tag:
                  type: array
                  items:
                    type: string
                    description: ''
                  nullable: true
              required:
                - name
                - description
                - datasource
                - active
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
                    default: Task Test
                  description:
                    type: string
                    description: ''
                    default: My tasks description
                  docs:
                    type: string
                    description: ''
                    default: Documentation
                  guid:
                    type: string
                    description: ''
                    default: YE1fwVhQ-enRlc6Sb42Gqru58-0
                  datasource:
                    type: string
                    description: ''
                    default: test
                  active:
                    type: boolean
                    description: ''
                    default: true
                  branch:
                    type: string
                    description: ''
                    default: v1
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