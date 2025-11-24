# Source: https://infisical.com/docs/api-reference/endpoints/admin/bootstrap-instance.md

# Bootstrap Instance

## OpenAPI

````yaml POST /api/v1/admin/bootstrap
paths:
  path: /api/v1/admin/bootstrap
  method: post
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
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              email:
                allOf:
                  - type: string
                    format: email
                    minLength: 1
              password:
                allOf:
                  - type: string
                    minLength: 1
              organization:
                allOf:
                  - type: string
                    minLength: 1
            required: true
            requiredProperties:
              - email
              - password
              - organization
            additionalProperties: false
        examples:
          example:
            value:
              email: jsmith@example.com
              password: <string>
              organization: <string>
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              message:
                allOf:
                  - type: string
              user:
                allOf:
                  - type: object
                    properties:
                      username:
                        type: string
                      firstName:
                        type: string
                        nullable: true
                      lastName:
                        type: string
                        nullable: true
                      email:
                        type: string
                        nullable: true
                      id:
                        type: string
                        format: uuid
                      superAdmin:
                        type: boolean
                        default: false
                        nullable: true
                    required:
                      - username
                      - id
                    additionalProperties: false
              organization:
                allOf:
                  - type: object
                    properties:
                      id:
                        type: string
                        format: uuid
                      name:
                        type: string
                      slug:
                        type: string
                    required:
                      - id
                      - name
                      - slug
                    additionalProperties: false
              identity:
                allOf:
                  - type: object
                    properties:
                      id:
                        type: string
                        format: uuid
                      name:
                        type: string
                      credentials:
                        type: object
                        properties:
                          token:
                            type: string
                        required:
                          - token
                        additionalProperties: false
                    required:
                      - id
                      - name
                      - credentials
                    additionalProperties: false
            requiredProperties:
              - message
              - user
              - organization
              - identity
            additionalProperties: false
        examples:
          example:
            value:
              message: <string>
              user:
                username: <string>
                firstName: <string>
                lastName: <string>
                email: <string>
                id: 3c90c3cc-0d44-4b50-8888-8dd25736052a
                superAdmin: false
              organization:
                id: 3c90c3cc-0d44-4b50-8888-8dd25736052a
                name: <string>
                slug: <string>
              identity:
                id: 3c90c3cc-0d44-4b50-8888-8dd25736052a
                name: <string>
                credentials:
                  token: <string>
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