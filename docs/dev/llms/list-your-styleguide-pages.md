# Source: https://dev.writer.com/api-reference-legacy/styleguide/list-your-styleguide-pages.md

# List your styleguide pages

## OpenAPI

````yaml get /styleguide/page
paths:
  path: /styleguide/page
  method: get
  servers:
    - url: https://enterprise-api.writer.com
  request:
    security: []
    parameters:
      path: {}
      query:
        status:
          schema:
            - type: enum<string>
              enum:
                - live
                - offline
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
                      $ref: '#/components/schemas/PagePublicApiResponse'
              totalCount:
                allOf:
                  - type: integer
                    format: int64
              pagination:
                allOf:
                  - $ref: '#/components/schemas/Pagination'
            refIdentifier: '#/components/schemas/PaginatedResult_PagePublicApiResponse'
            requiredProperties:
              - totalCount
              - pagination
        examples:
          example:
            value:
              result:
                - id: 123
                  title: <string>
                  url: <string>
                  section:
                    id: 123
                    title: <string>
                    url: <string>
                  status: live
                  order: 123
                  createdAt: '2023-11-07T05:31:56Z'
                  updatedAt: '2023-11-07T05:31:56Z'
                  updatedBy:
                    id: 123
                    firstName: <string>
                    lastName: <string>
                    email: <string>
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
    SimpleUser:
      required:
        - id
        - firstName
      type: object
      properties:
        id:
          type: integer
          format: int64
        firstName:
          type: string
        lastName:
          type: string
        email:
          type: string
    PagePublicApiResponse:
      required:
        - id
        - title
        - url
        - status
        - order
        - createdAt
        - updatedAt
      type: object
      properties:
        id:
          type: integer
          format: int64
        title:
          type: string
        url:
          type: string
        section:
          $ref: '#/components/schemas/SectionInfo'
        status:
          type: string
          enum:
            - live
            - offline
        order:
          type: integer
        createdAt:
          type: string
          format: date-time
        updatedAt:
          type: string
          format: date-time
        updatedBy:
          $ref: '#/components/schemas/SimpleUser'
    SectionInfo:
      required:
        - id
        - title
        - url
      type: object
      properties:
        id:
          type: integer
          format: int64
        title:
          type: string
        url:
          type: string

````