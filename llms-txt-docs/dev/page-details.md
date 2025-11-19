# Source: https://dev.writer.com/api-reference-legacy/styleguide/page-details.md

# Page details

## OpenAPI

````yaml get /styleguide/page/{pageId}
paths:
  path: /styleguide/page/{pageId}
  method: get
  servers:
    - url: https://enterprise-api.writer.com
  request:
    security: []
    parameters:
      path:
        pageId:
          schema:
            - type: integer
              required: true
      query: {}
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
              id:
                allOf:
                  - type: integer
                    format: int64
              title:
                allOf:
                  - type: string
              url:
                allOf:
                  - type: string
              section:
                allOf:
                  - $ref: '#/components/schemas/SectionInfo'
              status:
                allOf:
                  - type: string
                    enum:
                      - live
                      - offline
              order:
                allOf:
                  - type: integer
              content:
                allOf:
                  - type: string
              createdAt:
                allOf:
                  - type: string
                    format: date-time
              updatedAt:
                allOf:
                  - type: string
                    format: date-time
              updatedBy:
                allOf:
                  - $ref: '#/components/schemas/SimpleUser'
            refIdentifier: '#/components/schemas/PageWithSectionResponse'
            requiredProperties:
              - id
              - title
              - url
              - status
              - order
              - createdAt
              - updatedAt
        examples:
          example:
            value:
              id: 123
              title: <string>
              url: <string>
              section:
                id: 123
                title: <string>
                url: <string>
              status: live
              order: 123
              content: <string>
              createdAt: '2023-11-07T05:31:56Z'
              updatedAt: '2023-11-07T05:31:56Z'
              updatedBy:
                id: 123
                firstName: <string>
                lastName: <string>
                email: <string>
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