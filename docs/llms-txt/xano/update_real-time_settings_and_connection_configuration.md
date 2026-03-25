# Source: https://docs.xano.com/xano-features/metadata-api/instance_api/update_real-time_settings_and_connection_configuration.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Update real-time settings and connection configuration

> Update real-time settings and connection configuration



## OpenAPI

````yaml xano-features/metadata-api/metadata_api_instance.json put /workspace/{workspace_id}/realtime
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
  /workspace/{workspace_id}/realtime:
    put:
      tags:
        - realtime
      summary: Update real-time settings and connection configuration
      description: |-
        Update real-time settings and connection configuration
        <br /><br />
        <b>Authentication:</b> required
        <br /><br />
        <b>Required API Scope:</b>
        Instance Workspace: Update
      parameters:
        - name: workspace_id
          in: path
          description: ''
          required: true
          schema:
            type: integer
            format: int64
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                enabled:
                  type: boolean
                  description: ''
                hash:
                  type: string
                  description: ''
                channels:
                  type: array
                  items:
                    type: object
                    properties:
                      anonymous_clients:
                        type: boolean
                        description: ''
                      client_authenticated_messaging:
                        type: boolean
                        description: ''
                      client_private_messaging:
                        type: boolean
                        description: ''
                      client_private_messaging_authenticated_only:
                        type: boolean
                        description: ''
                      client_public_messaging:
                        type: boolean
                        description: ''
                      client_public_messaging_authenticated_only:
                        type: boolean
                        description: ''
                      description:
                        type: string
                        description: ''
                      enabled:
                        type: boolean
                        description: ''
                      history:
                        type: string
                        description: ''
                        enum:
                          - 0
                          - 25
                          - 50
                          - 100
                          - 250
                          - 1000
                      id:
                        type: integer
                        format: int64
                        description: ''
                      pattern:
                        type: string
                        description: ''
                      presence:
                        type: boolean
                        description: ''
                      wildcard:
                        type: boolean
                        description: ''
                    required:
                      - pattern
          multipart/form-data:
            schema:
              type: object
              properties:
                enabled:
                  type: boolean
                  description: ''
                hash:
                  type: string
                  description: ''
                channels:
                  type: array
                  items:
                    type: object
                    properties:
                      anonymous_clients:
                        type: boolean
                        description: ''
                      client_authenticated_messaging:
                        type: boolean
                        description: ''
                      client_private_messaging:
                        type: boolean
                        description: ''
                      client_private_messaging_authenticated_only:
                        type: boolean
                        description: ''
                      client_public_messaging:
                        type: boolean
                        description: ''
                      client_public_messaging_authenticated_only:
                        type: boolean
                        description: ''
                      description:
                        type: string
                        description: ''
                      enabled:
                        type: boolean
                        description: ''
                      history:
                        type: string
                        description: ''
                        enum:
                          - 0
                          - 25
                          - 50
                          - 100
                          - 250
                          - 1000
                      id:
                        type: integer
                        format: int64
                        description: ''
                      pattern:
                        type: string
                        description: ''
                      presence:
                        type: boolean
                        description: ''
                      wildcard:
                        type: boolean
                        description: ''
                    required:
                      - pattern
      responses:
        '200':
          description: Success!
          content:
            application/json:
              schema:
                type: object
                properties:
                  enabled:
                    type: boolean
                    description: ''
                  hash:
                    type: string
                    description: ''
                    default: Dl3HlakmBZDhezv6yml7hliTM20
                  channels:
                    type: array
                    items:
                      type: object
                      properties:
                        anonymous_clients:
                          type: boolean
                          description: ''
                        client_authenticated_messaging:
                          type: boolean
                          description: ''
                        client_private_messaging:
                          type: boolean
                          description: ''
                        client_private_messaging_authenticated_only:
                          type: boolean
                          description: ''
                        client_public_messaging:
                          type: boolean
                          description: ''
                        client_public_messaging_authenticated_only:
                          type: boolean
                          description: ''
                        description:
                          type: string
                          description: ''
                        enabled:
                          type: boolean
                          description: ''
                        id:
                          type: integer
                          format: int64
                          description: ''
                        pattern:
                          type: string
                          description: ''
                        presence:
                          type: boolean
                          description: ''
                        wildcard:
                          type: boolean
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