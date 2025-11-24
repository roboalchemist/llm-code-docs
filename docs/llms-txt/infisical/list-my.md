# Source: https://infisical.com/docs/api-reference/endpoints/ssh/hosts/list-my.md

# List My Hosts

## OpenAPI

````yaml GET /api/v1/ssh/hosts
paths:
  path: /api/v1/ssh/hosts
  method: get
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
      path: {}
      query: {}
      header: {}
      cookie: {}
    body: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: array
            items:
              allOf:
                - type: object
                  properties:
                    id:
                      type: string
                      format: uuid
                    projectId:
                      type: string
                    hostname:
                      type: string
                    alias:
                      type: string
                      nullable: true
                    userCertTtl:
                      type: string
                    hostCertTtl:
                      type: string
                    userSshCaId:
                      type: string
                      format: uuid
                    hostSshCaId:
                      type: string
                      format: uuid
                    loginMappings:
                      type: array
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
                          source:
                            type: string
                            enum:
                              - host
                              - hostGroup
                        required:
                          - loginUser
                          - allowedPrincipals
                          - source
                        additionalProperties: false
                  required:
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
              - id: 3c90c3cc-0d44-4b50-8888-8dd25736052a
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
                    source: host
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