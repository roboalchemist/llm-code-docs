# Source: https://docs.xano.com/api-reference/agent/retrieve-a-specific-agent-by-id.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Retrieve a specific agent by ID

> Retrieve a specific agent by ID
<br /><br />
<b>Authentication:</b> required



## OpenAPI

````yaml apispec_meta_instance.json get /workspace/{workspace_id}/agent/{agent_id}
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
  /workspace/{workspace_id}/agent/{agent_id}:
    get:
      tags:
        - agent
      summary: Retrieve a specific agent by ID
      description: |-
        Retrieve a specific agent by ID
        <br /><br />
        <b>Authentication:</b> required
      operationId: Xano Metadata API/workspace/{workspace_id}/agent/{agent_id}|GET
      parameters:
        - name: workspace_id
          in: path
          description: ''
          required: true
          schema:
            type: integer
            format: int64
        - name: agent_id
          in: path
          description: ''
          required: true
          schema:
            type: integer
            format: int64
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
                    default: Agent Test
                  description:
                    type: string
                    description: ''
                    default: My agent description
                  branch:
                    type: string
                    description: ''
                    default: v1
                  llm:
                    type: string
                    description: ''
                    default: anthropic
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