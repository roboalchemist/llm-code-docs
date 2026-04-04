# Source: https://docs.xano.com/api-reference/workflow_test/add-a-workflow-test.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Add a workflow test

> add workspace workflow test
<br /><br />
<b>Authentication:</b> required



## OpenAPI

````yaml apispec_meta_instance.json post /workspace/{workspace_id}/workflow_test
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
  /workspace/{workspace_id}/workflow_test:
    post:
      tags:
        - workflow_test
      summary: Add a workflow test
      description: |-
        add workspace workflow test
        <br /><br />
        <b>Authentication:</b> required
      operationId: Xano Metadata API/workspace/{workspace_id}/workflow_test|POST
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
                workflow_test foo {
                  stack {
                    var $x1 {
                      value = 1 + 2 + 3
                    }
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
                include_xanoscript:
                  type: boolean
                  description: ''
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
                include_xanoscript:
                  type: boolean
                  description: ''
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
                    default: Workflow Test
                  description:
                    type: string
                    description: ''
                    default: My workflow test description
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