# Source: https://docs.xano.com/api-reference/agent-trigger/update-agent-trigger-using-xanoscript.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Update agent trigger using XanoScript

> Update agent trigger using XanoScript
<br /><br />
<b>Authentication:</b> required



## OpenAPI

````yaml apispec_meta_instance.json put /workspace/{workspace_id}/agent/trigger/{trigger_id}
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
  /workspace/{workspace_id}/agent/trigger/{trigger_id}:
    put:
      tags:
        - agent trigger
      summary: Update agent trigger using XanoScript
      description: |-
        Update agent trigger using XanoScript
        <br /><br />
        <b>Authentication:</b> required
      operationId: >-
        Xano Metadata
        API/workspace/{workspace_id}/agent/trigger/{trigger_id}|PUT
      parameters:
        - name: workspace_id
          in: path
          description: ''
          required: true
          schema:
            type: integer
            format: int64
        - name: trigger_id
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
                agent_trigger foo {
                  agent = "my_agent"
                  input {
                    object toolset {
                      schema {
                        int id
                        text name
                        text instructions
                      }
                    }
                    object[] tools {
                      schema {
                        int id
                        text name
                        text instructions
                      }
                    }
                  }
                  stack {
                    var $x1 {
                      value = 123
                    }
                  }
                  actions = {connection: true}
                }
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
                    default: Agent Trigger
                  description:
                    type: string
                    description: ''
                    default: My agent trigger test description
                  guid:
                    type: string
                    description: ''
                    default: YE1fwVhQ-enRlc6Sb42Gqru58-0
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
                  actions:
                    type: object
                    properties:
                      connection:
                        type: boolean
                        description: ''
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