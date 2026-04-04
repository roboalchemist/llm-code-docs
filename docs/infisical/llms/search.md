# Source: https://infisical.com/docs/api-reference/endpoints/identities/search.md

> ## Documentation Index
> Fetch the complete documentation index at: https://infisical.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Search

> Search machine identities



## OpenAPI

````yaml POST /api/v1/identities/search
openapi: 3.0.3
info:
  title: Infisical API
  description: List of all available APIs that can be consumed
  version: 0.0.1
servers:
  - url: https://us.infisical.com
    description: Production server (US)
  - url: https://eu.infisical.com
    description: Production server (EU)
  - url: http://localhost:8080
    description: Local server
security: []
paths:
  /api/v1/identities/search:
    post:
      tags:
        - Identities
      description: Search machine identities
      operationId: searchMachineIdentities
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                orderBy:
                  type: string
                  enum:
                    - name
                    - role
                  default: name
                  description: The column to order identities by.
                orderDirection:
                  type: string
                  enum:
                    - asc
                    - desc
                  default: asc
                  description: The direction to order identities in.
                limit:
                  type: number
                  maximum: 100
                  default: 50
                  description: The number of identities to return.
                offset:
                  type: number
                  default: 0
                  description: >-
                    The offset to start from. If you enter 10, it will start
                    from the 10th identity.
                search:
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
                              The organizational role of the identity to filter
                              by.
                        additionalProperties: false
                        description: The filters to apply to the search.
                      maxItems: 5
                  additionalProperties: false
                  description: The filters to apply to the search.
              additionalProperties: false
      responses:
        '200':
          description: Default Response
          content:
            application/json:
              schema:
                type: object
                properties:
                  identities:
                    type: array
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
                    type: number
                required:
                  - identities
                  - totalCount
                additionalProperties: false
        '400':
          description: Default Response
          content:
            application/json:
              schema:
                type: object
                properties:
                  reqId:
                    type: string
                  statusCode:
                    type: number
                    enum:
                      - 400
                  message:
                    type: string
                  error:
                    type: string
                  details: {}
                required:
                  - reqId
                  - statusCode
                  - message
                  - error
                additionalProperties: false
        '401':
          description: Default Response
          content:
            application/json:
              schema:
                type: object
                properties:
                  reqId:
                    type: string
                  statusCode:
                    type: number
                    enum:
                      - 401
                  message:
                    type: string
                  error:
                    type: string
                required:
                  - reqId
                  - statusCode
                  - message
                  - error
                additionalProperties: false
        '403':
          description: Default Response
          content:
            application/json:
              schema:
                type: object
                properties:
                  reqId:
                    type: string
                  statusCode:
                    type: number
                    enum:
                      - 403
                  message:
                    type: string
                  details: {}
                  error:
                    type: string
                required:
                  - reqId
                  - statusCode
                  - message
                  - error
                additionalProperties: false
        '404':
          description: Default Response
          content:
            application/json:
              schema:
                type: object
                properties:
                  reqId:
                    type: string
                  statusCode:
                    type: number
                    enum:
                      - 404
                  message:
                    type: string
                  error:
                    type: string
                required:
                  - reqId
                  - statusCode
                  - message
                  - error
                additionalProperties: false
        '422':
          description: Default Response
          content:
            application/json:
              schema:
                type: object
                properties:
                  reqId:
                    type: string
                  statusCode:
                    type: number
                    enum:
                      - 422
                  message: {}
                  error:
                    type: string
                required:
                  - reqId
                  - statusCode
                  - error
                additionalProperties: false
        '500':
          description: Default Response
          content:
            application/json:
              schema:
                type: object
                properties:
                  reqId:
                    type: string
                  statusCode:
                    type: number
                    enum:
                      - 500
                  message:
                    type: string
                  error:
                    type: string
                required:
                  - reqId
                  - statusCode
                  - message
                  - error
                additionalProperties: false
      security:
        - bearerAuth: []
components:
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT
      description: An access token in Infisical

````