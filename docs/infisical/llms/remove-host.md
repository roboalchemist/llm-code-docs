# Source: https://infisical.com/docs/api-reference/endpoints/ssh/groups/remove-host.md

# Remove Host

> Remove an SSH Host from a Host Group

## OpenAPI

````yaml DELETE /api/v1/ssh/host-groups/{sshHostGroupId}/hosts/{hostId}
paths:
  path: /api/v1/ssh/host-groups/{sshHostGroupId}/hosts/{hostId}
  method: delete
  servers:
    - url: https://us.infisical.com
      description: Production server (US)
    - url: https://eu.infisical.com
      description: Production server (EU)
    - url: http://localhost:8080
      description: Local server
  request:
    security: []
    parameters:
      path:
        sshHostGroupId:
          schema:
            - type: string
              required: true
              description: The ID of the SSH host group to delete the host from.
        hostId:
          schema:
            - type: string
              required: true
              description: The ID of the SSH host to delete from the SSH host group.
      query: {}
      header: {}
      cookie: {}
    body: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              id:
                allOf:
                  - type: string
                    format: uuid
              projectId:
                allOf:
                  - type: string
              hostname:
                allOf:
                  - type: string
              alias:
                allOf:
                  - type: string
                    nullable: true
              userCertTtl:
                allOf:
                  - type: string
              hostCertTtl:
                allOf:
                  - type: string
              userSshCaId:
                allOf:
                  - type: string
                    format: uuid
              hostSshCaId:
                allOf:
                  - type: string
                    format: uuid
              loginMappings:
                allOf:
                  - type: array
                    items:
                      type: object
                      properties:
                        loginUser:
                          type: string
                        allowedPrincipals:
                          type: object
                          properties:
                            usernames:
                              type: array
                              items:
                                type: string
                            groups:
                              type: array
                              items:
                                type: string
                          additionalProperties: false
                      required:
                        - loginUser
                        - allowedPrincipals
                      additionalProperties: false
            requiredProperties:
              - id
              - projectId
              - hostname
              - userCertTtl
              - hostCertTtl
              - userSshCaId
              - hostSshCaId
              - loginMappings
            additionalProperties: false
        examples:
          example:
            value:
              id: 3c90c3cc-0d44-4b50-8888-8dd25736052a
              projectId: <string>
              hostname: <string>
              alias: <string>
              userCertTtl: <string>
              hostCertTtl: <string>
              userSshCaId: 3c90c3cc-0d44-4b50-8888-8dd25736052a
              hostSshCaId: 3c90c3cc-0d44-4b50-8888-8dd25736052a
              loginMappings:
                - loginUser: <string>
                  allowedPrincipals:
                    usernames:
                      - <string>
                    groups:
                      - <string>
        description: Default Response
    '400':
      application/json:
        schemaArray:
          - type: object
            properties:
              reqId:
                allOf:
                  - type: string
              statusCode:
                allOf:
                  - type: number
                    enum:
                      - 400
              message:
                allOf:
                  - type: string
              error:
                allOf:
                  - type: string
            requiredProperties:
              - reqId
              - statusCode
              - message
              - error
            additionalProperties: false
        examples:
          example:
            value:
              reqId: <string>
              statusCode: 400
              message: <string>
              error: <string>
        description: Default Response
    '401':
      application/json:
        schemaArray:
          - type: object
            properties:
              reqId:
                allOf:
                  - type: string
              statusCode:
                allOf:
                  - type: number
                    enum:
                      - 401
              message:
                allOf:
                  - type: string
              error:
                allOf:
                  - type: string
            requiredProperties:
              - reqId
              - statusCode
              - message
              - error
            additionalProperties: false
        examples:
          example:
            value:
              reqId: <string>
              statusCode: 401
              message: <string>
              error: <string>
        description: Default Response
    '403':
      application/json:
        schemaArray:
          - type: object
            properties:
              reqId:
                allOf:
                  - type: string
              statusCode:
                allOf:
                  - type: number
                    enum:
                      - 403
              message:
                allOf:
                  - type: string
              details:
                allOf:
                  - {}
              error:
                allOf:
                  - type: string
            requiredProperties:
              - reqId
              - statusCode
              - message
              - error
            additionalProperties: false
        examples:
          example:
            value:
              reqId: <string>
              statusCode: 403
              message: <string>
              details: <any>
              error: <string>
        description: Default Response
    '404':
      application/json:
        schemaArray:
          - type: object
            properties:
              reqId:
                allOf:
                  - type: string
              statusCode:
                allOf:
                  - type: number
                    enum:
                      - 404
              message:
                allOf:
                  - type: string
              error:
                allOf:
                  - type: string
            requiredProperties:
              - reqId
              - statusCode
              - message
              - error
            additionalProperties: false
        examples:
          example:
            value:
              reqId: <string>
              statusCode: 404
              message: <string>
              error: <string>
        description: Default Response
    '422':
      application/json:
        schemaArray:
          - type: object
            properties:
              reqId:
                allOf:
                  - type: string
              statusCode:
                allOf:
                  - type: number
                    enum:
                      - 422
              message:
                allOf:
                  - {}
              error:
                allOf:
                  - type: string
            requiredProperties:
              - reqId
              - statusCode
              - error
            additionalProperties: false
        examples:
          example:
            value:
              reqId: <string>
              statusCode: 422
              message: <any>
              error: <string>
        description: Default Response
    '500':
      application/json:
        schemaArray:
          - type: object
            properties:
              reqId:
                allOf:
                  - type: string
              statusCode:
                allOf:
                  - type: number
                    enum:
                      - 500
              message:
                allOf:
                  - type: string
              error:
                allOf:
                  - type: string
            requiredProperties:
              - reqId
              - statusCode
              - message
              - error
            additionalProperties: false
        examples:
          example:
            value:
              reqId: <string>
              statusCode: 500
              message: <string>
              error: <string>
        description: Default Response
  deprecated: false
  type: path
components:
  schemas: {}

````