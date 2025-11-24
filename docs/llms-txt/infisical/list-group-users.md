# Source: https://infisical.com/docs/api-reference/endpoints/groups/list-group-users.md

# List Group Users

## OpenAPI

````yaml GET /api/v1/groups/{id}/users
paths:
  path: /api/v1/groups/{id}/users
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
      path:
        id:
          schema:
            - type: string
              required: true
              description: The ID of the group to list users for.
      query:
        offset:
          schema:
            - type: number
              required: false
              description: >-
                The offset to start from. If you enter 10, it will start from
                the 10th user.
              maximum: 100
              minimum: 0
              default: 0
        limit:
          schema:
            - type: number
              required: false
              description: The number of users to return.
              maximum: 100
              minimum: 1
              default: 10
        username:
          schema:
            - type: string
              required: false
              description: The username to search for.
        search:
          schema:
            - type: string
              required: false
              description: The text string that user email or name will be filtered by.
        filter:
          schema:
            - type: enum<string>
              enum:
                - existingMembers
                - nonMembers
              required: false
              description: >-
                Whether to filter the list of returned users. 'existingMembers'
                will only return existing users in the group, 'nonMembers' will
                only return users not in the group, undefined will return all
                users in the organization.
      header: {}
      cookie: {}
    body: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              users:
                allOf:
                  - type: array
                    items:
                      type: object
                      properties:
                        email:
                          type: string
                          nullable: true
                        username:
                          type: string
                        firstName:
                          type: string
                          nullable: true
                        lastName:
                          type: string
                          nullable: true
                        id:
                          type: string
                          format: uuid
                        isPartOfGroup:
                          type: boolean
                        joinedGroupAt:
                          type: string
                          format: date-time
                          nullable: true
                      required:
                        - username
                        - id
                        - isPartOfGroup
                        - joinedGroupAt
                      additionalProperties: false
              totalCount:
                allOf:
                  - type: number
            requiredProperties:
              - users
              - totalCount
            additionalProperties: false
        examples:
          example:
            value:
              users:
                - email: <string>
                  username: <string>
                  firstName: <string>
                  lastName: <string>
                  id: 3c90c3cc-0d44-4b50-8888-8dd25736052a
                  isPartOfGroup: true
                  joinedGroupAt: '2023-11-07T05:31:56Z'
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