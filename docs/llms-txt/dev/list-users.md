# Source: https://dev.writer.com/api-reference-legacy/user/list-users.md

# List users

## OpenAPI

````yaml get /user
paths:
  path: /user
  method: get
  servers:
    - url: https://enterprise-api.writer.com
  request:
    security: []
    parameters:
      path: {}
      query:
        search:
          schema:
            - type: string
              required: false
        sortField:
          schema:
            - type: enum<string>
              enum:
                - id
                - name
                - creationTime
                - deleted
                - modificationTime
                - email
                - lastSeen
              required: false
        sortOrder:
          schema:
            - type: enum<string>
              enum:
                - asc
                - desc
              required: false
        offset:
          schema:
            - type: integer
              required: false
        limit:
          schema:
            - type: integer
              required: false
      header:
        Authorization:
          schema:
            - type: string
              required: true
      cookie: {}
    body: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              result:
                allOf:
                  - type: array
                    items:
                      $ref: '#/components/schemas/UserPublicResponse'
              totalCount:
                allOf:
                  - type: integer
                    format: int64
              pagination:
                allOf:
                  - $ref: '#/components/schemas/Pagination'
            refIdentifier: '#/components/schemas/PaginatedResult_UserPublicResponse'
            requiredProperties:
              - totalCount
              - pagination
        examples:
          example:
            value:
              result:
                - id: 123
                  avatar: <string>
                  accountStatus: invited
                  firstName: <string>
                  lastName: <string>
                  fullName: <string>
                  email: <string>
                  timezone: <string>
                  lastSeenOnline: '2023-11-07T05:31:56Z'
                  invitedBy: 123
                  createdAt: '2023-11-07T05:31:56Z'
              totalCount: 123
              pagination:
                offset: 123
                limit: 123
        description: ''
    '400':
      application/json:
        schemaArray:
          - type: object
            properties:
              tpe:
                allOf:
                  - &ref_0
                    type: string
              errors:
                allOf:
                  - &ref_1
                    type: array
                    items:
                      $ref: '#/components/schemas/FailMessage'
              extras:
                allOf:
                  - &ref_2
                    $ref: '#/components/schemas/Json'
            refIdentifier: '#/components/schemas/FailResponse'
            requiredProperties: &ref_3
              - tpe
              - extras
        examples:
          example:
            value:
              tpe: <string>
              errors:
                - description: <string>
                  key: <string>
                  extras: <any>
              extras: <any>
        description: Bad Request
    '401':
      application/json:
        schemaArray:
          - type: object
            properties:
              tpe:
                allOf:
                  - *ref_0
              errors:
                allOf:
                  - *ref_1
              extras:
                allOf:
                  - *ref_2
            refIdentifier: '#/components/schemas/FailResponse'
            requiredProperties: *ref_3
        examples:
          example:
            value:
              tpe: <string>
              errors:
                - description: <string>
                  key: <string>
                  extras: <any>
              extras: <any>
        description: Unauthorized
    '403':
      application/json:
        schemaArray:
          - type: object
            properties:
              tpe:
                allOf:
                  - *ref_0
              errors:
                allOf:
                  - *ref_1
              extras:
                allOf:
                  - *ref_2
            refIdentifier: '#/components/schemas/FailResponse'
            requiredProperties: *ref_3
        examples:
          example:
            value:
              tpe: <string>
              errors:
                - description: <string>
                  key: <string>
                  extras: <any>
              extras: <any>
        description: Forbidden
    '404':
      application/json:
        schemaArray:
          - type: object
            properties:
              tpe:
                allOf:
                  - *ref_0
              errors:
                allOf:
                  - *ref_1
              extras:
                allOf:
                  - *ref_2
            refIdentifier: '#/components/schemas/FailResponse'
            requiredProperties: *ref_3
        examples:
          example:
            value:
              tpe: <string>
              errors:
                - description: <string>
                  key: <string>
                  extras: <any>
              extras: <any>
        description: Not Found
    '500':
      application/json:
        schemaArray:
          - type: object
            properties:
              tpe:
                allOf:
                  - *ref_0
              errors:
                allOf:
                  - *ref_1
              extras:
                allOf:
                  - *ref_2
            refIdentifier: '#/components/schemas/FailResponse'
            requiredProperties: *ref_3
        examples:
          example:
            value:
              tpe: <string>
              errors:
                - description: <string>
                  key: <string>
                  extras: <any>
              extras: <any>
        description: Internal Server Error
  deprecated: false
  type: path
components:
  schemas:
    FailMessage:
      required:
        - description
        - key
        - extras
      type: object
      properties:
        description:
          type: string
        key:
          type: string
        extras:
          $ref: '#/components/schemas/Json'
    Pagination:
      type: object
      properties:
        offset:
          type: integer
          format: int64
        limit:
          type: integer
    Json: {}
    UserPublicResponse:
      required:
        - id
        - accountStatus
        - firstName
        - fullName
        - createdAt
      type: object
      properties:
        id:
          type: integer
          format: int64
        avatar:
          type: string
        accountStatus:
          type: string
          enum:
            - invited
            - signed_up
        firstName:
          type: string
        lastName:
          type: string
        fullName:
          type: string
        email:
          type: string
        timezone:
          type: string
        lastSeenOnline:
          type: string
          format: date-time
        invitedBy:
          type: integer
          format: int64
        createdAt:
          type: string
          format: date-time

````