# Source: https://infisical.com/docs/api-reference/endpoints/identities/search.md

# Search

> Search machine identities

## OpenAPI

````yaml POST /api/v1/identities/search
paths:
  path: /api/v1/identities/search
  method: post
  servers:
    - url: https://us.infisical.com
      description: Production server (US)
    - url: https://eu.infisical.com
      description: Production server (EU)
    - url: http://localhost:8080
      description: Local server
  request:
    security:
      - title: bearerAuth
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: bearer
              description: An access token in Infisical
          cookie: {}
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
              orderBy:
                allOf:
                  - type: string
                    enum:
                      - name
                      - role
                    default: name
                    description: The column to order identities by.
              orderDirection:
                allOf:
                  - type: string
                    enum:
                      - asc
                      - desc
                    default: asc
                    description: The direction to order identities in.
              limit:
                allOf:
                  - type: number
                    maximum: 100
                    default: 50
                    description: The number of identities to return.
              offset:
                allOf:
                  - type: number
                    default: 0
                    description: >-
                      The offset to start from. If you enter 10, it will start
                      from the 10th identity.
              search:
                allOf:
                  - type: object
                    properties:
                      name:
                        anyOf:
                          - type: string
                            maxLength: 255
                          - type: object
                            properties:
                              $eq:
                                type: string
                                maxLength: 255
                              $contains:
                                type: string
                                maxLength: 255
                              $in:
                                type: array
                                items:
                                  type: string
                                  maxLength: 255
                            additionalProperties: false
                        description: The name of the identity to filter by.
                      role:
                        anyOf:
                          - type: string
                            maxLength: 255
                          - type: object
                            properties:
                              $eq:
                                type: string
                                maxLength: 255
                              $in:
                                type: array
                                items:
                                  type: string
                                  maxLength: 255
                            additionalProperties: false
                        description: The organizational role of the identity to filter by.
                      $or:
                        type: array
                        items:
                          type: object
                          properties:
                            name:
                              anyOf:
                                - type: string
                                  maxLength: 255
                                - type: object
                                  properties:
                                    $eq:
                                      type: string
                                      maxLength: 255
                                    $contains:
                                      type: string
                                      maxLength: 255
                                    $in:
                                      type: array
                                      items:
                                        type: string
                                        maxLength: 255
                                  additionalProperties: false
                              description: The name of the identity to filter by.
                            role:
                              anyOf:
                                - type: string
                                  maxLength: 255
                                - type: object
                                  properties:
                                    $eq:
                                      type: string
                                      maxLength: 255
                                    $in:
                                      type: array
                                      items:
                                        type: string
                                        maxLength: 255
                                  additionalProperties: false
                              description: >-
                                The organizational role of the identity to
                                filter by.
                          additionalProperties: false
                          description: The filters to apply to the search.
                        maxItems: 5
                    additionalProperties: false
                    description: The filters to apply to the search.
            additionalProperties: false
        examples:
          example:
            value:
              orderBy: name
              orderDirection: asc
              limit: 50
              offset: 0
              search:
                name: <string>
                role: <string>
                $or:
                  - name: <string>
                    role: <string>
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              identities:
                allOf:
                  - type: array
                    items:
                      type: object
                      properties:
                        id:
                          type: string
                          format: uuid
                        role:
                          type: string
                        roleId:
                          type: string
                          format: uuid
                          nullable: true
                        orgId:
                          type: string
                          format: uuid
                        createdAt:
                          type: string
                          format: date-time
                        updatedAt:
                          type: string
                          format: date-time
                        identityId:
                          type: string
                          format: uuid
                        lastLoginAuthMethod:
                          type: string
                          nullable: true
                        lastLoginTime:
                          type: string
                          format: date-time
                          nullable: true
                        customRole:
                          type: object
                          properties:
                            id:
                              type: string
                              format: uuid
                            name:
                              type: string
                            slug:
                              type: string
                            permissions: {}
                            description:
                              type: string
                              nullable: true
                          required:
                            - id
                            - name
                            - slug
                          additionalProperties: false
                        identity:
                          type: object
                          properties:
                            name:
                              type: string
                            id:
                              type: string
                              format: uuid
                            hasDeleteProtection:
                              type: boolean
                              default: false
                            orgId:
                              type: string
                              format: uuid
                            authMethods:
                              type: array
                              items:
                                type: string
                          required:
                            - name
                            - id
                            - orgId
                            - authMethods
                          additionalProperties: false
                      required:
                        - id
                        - role
                        - orgId
                        - createdAt
                        - updatedAt
                        - identityId
                        - identity
                      additionalProperties: false
              totalCount:
                allOf:
                  - type: number
            requiredProperties:
              - identities
              - totalCount
            additionalProperties: false
        examples:
          example:
            value:
              identities:
                - id: 3c90c3cc-0d44-4b50-8888-8dd25736052a
                  role: <string>
                  roleId: 3c90c3cc-0d44-4b50-8888-8dd25736052a
                  orgId: 3c90c3cc-0d44-4b50-8888-8dd25736052a
                  createdAt: '2023-11-07T05:31:56Z'
                  updatedAt: '2023-11-07T05:31:56Z'
                  identityId: 3c90c3cc-0d44-4b50-8888-8dd25736052a
                  lastLoginAuthMethod: <string>
                  lastLoginTime: '2023-11-07T05:31:56Z'
                  customRole:
                    id: 3c90c3cc-0d44-4b50-8888-8dd25736052a
                    name: <string>
                    slug: <string>
                    permissions: <any>
                    description: <string>
                  identity:
                    name: <string>
                    id: 3c90c3cc-0d44-4b50-8888-8dd25736052a
                    hasDeleteProtection: false
                    orgId: 3c90c3cc-0d44-4b50-8888-8dd25736052a
                    authMethods:
                      - <string>
              totalCount: 123
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